using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.IO;
using System.Numerics;
using System.Threading;
using System.Timers;
using GameHook;
using SoulsFormats;

namespace StJude2021
{
    class Settings
    {
        // C# effect durations in milliseconds.
        public static Dictionary<string, int> EffectDurations = new Dictionary<string, int>()
        {
            ["Cosplay"] = 60000,
            ["CosplayCooldown"] = 120000,  // time between cosplay activations (so an extra 60 seconds after end of last cosplay)
            ["RandomizeMaps"] = 5000,  // short delay after randomized maps are loaded
            ["CameraFOV"] = 30000,
            ["RetroCamera"] = 60000,
            ["InvisiblePlayer"] = 60000,
            ["DeathFollowsYou"] = 20000,
        };
    }

    class GameManager
    {
        public string GamePath { get; }
        public DSRHook Hook { get; }
        public Random Rand { get; }
        PARAM MagicParam { get; set; } = null;  // needed to access max spell casts
        PARAM NPCParam { get; set; } = null;   // needed to match enemy level for "Oops" modifiers
        MapGenerator MapGen { get; }

        Dictionary<string, System.Timers.Timer> Timers { get; } = new Dictionary<string, System.Timers.Timer>()
        {
            ["Cosplay"] = new System.Timers.Timer(Settings.EffectDurations["Cosplay"]),
            ["CosplayCooldown"] = new System.Timers.Timer(Settings.EffectDurations["CosplayCooldown"]),
            ["RandomizeMaps"] = new System.Timers.Timer(Settings.EffectDurations["RandomizeMaps"]),
            ["CameraFOV"] = new System.Timers.Timer(Settings.EffectDurations["CameraFOV"]),
            ["InvisiblePlayer"] = new System.Timers.Timer(Settings.EffectDurations["InvisiblePlayer"]),
        };

        GameFlag? CurrentCosplay { get; set; } = null;
        Dictionary<string, int> PreviousEquipment { get; } = new Dictionary<string, int>()
        {
            ["RH1"] = -1,
            ["RH2"] = -1,
            ["LH1"] = -1,
            ["LH2"] = -1,
            ["Head"] = -1,
            ["Body"] = -1,
            ["Arms"] = -1,
            ["Legs"] = -1,
        };
        static string DefaultGameParamPath { get; } = @"Package\param\GameParam\GameParam.parambnd.dcx";

        static int[] BossDeathFlags { get; } = new int[] { 2, 3, 5, 7, 9, 10, 11, 12, 13, 14 };  // narrowed down to 10 (no Priscilla, no Asylum Demon, no Gwyn, no Pinwheel)
        int DeadBossCount {
            get
            {
                int count = 0;
                foreach (int bossDeathFlag in BossDeathFlags)
                    count += GetFlag(bossDeathFlag) ? 1 : 0;
                return count;
            }
        }

        static string[] MSBStems { get; } = new string[]
        {
            "m10_00_00_00",
            "m10_01_00_00",
            "m10_02_00_00",  // NOTE: No map points for Firelink Shrine.
            "m11_00_00_00",
            "m12_00_00_01",
            "m12_01_00_00",
            "m13_00_00_00",
            "m13_01_00_00",
            "m13_02_00_00",
            "m14_00_00_00",
            "m14_01_00_00",
            "m15_00_00_00",
            "m15_01_00_00",
            "m16_00_00_00",
            "m17_00_00_00",
            "m18_00_00_00",
            "m18_01_00_00",  // NOTE: No map points for Undead Asylum.
        };

        public GameManager(string gamePath, DSRHook hook, Random rand)
        {
            GamePath = gamePath;
            Hook = hook;
            Rand = rand;
            SetParams();
            MapGen = new MapGenerator(GamePath, Rand, NPCParam);

            Timers["Cosplay"].Elapsed += OnCosplayTimerElapsed;
            Timers["Cosplay"].AutoReset = false;
            Timers["RandomizeMaps"].Elapsed += OnRandomizeMapsTimerElapsed;
            Timers["RandomizeMaps"].AutoReset = false;
            Timers["CameraFOV"].Elapsed += OnCameraFOVTimerElapsed;
            Timers["CameraFOV"].AutoReset = false;
            Timers["InvisiblePlayer"].Elapsed += OnInvisiblePlayerTimerElapsed;
            Timers["InvisiblePlayer"].AutoReset = false;

            // DisableHyperAggression();  // no longer used
            RemoveCosplayEquipment();
            Hook.EnableCameraFollow();
            Hook.SetCameraFov(0.75f);

            if (GetFlag(GameFlag.MapsAreRandomized))
            {
                // Reset MSBs on hook startup (as the timer has been lost).
                // Uses a thread, as this takes 10-15 seconds.
                Thread restoreMSBsThread = new Thread(RestoreMSBs);
                restoreMSBsThread.Start();
            }
        }

        public void Run(string mode = "input", string modFilePath = "")
        {
            Thread monitorThread = new Thread(MainMonitor);
            monitorThread.Start();

            Thread hookCheckThread = new Thread(HookCheck);
            hookCheckThread.Start();

            Thread cosplayCheckThread = new Thread(CosplayCheck);
            cosplayCheckThread.Start();

            ModifierChoice modChoice = new ModifierChoice(this, modFilePath);
            modChoice.Run(mode);
        }

        void HookCheck()
        {
            // Disables the hook check flag in a thread, so EMEVD knows this program is running.
            while (true)
            {
                // EMEVD keeps enabling this and gives mod program a few seconds to disable it before complaining.
                if (GetFlag(GameFlag.HookCheckFlag))
                    DisableFlag(GameFlag.HookCheckFlag);
                Thread.Sleep(10);  // less than one frame
            }
        }

        void MainMonitor()
        {
            Console.WriteLine("~~~ EFFECT MONITOR START ~~~");

            while (true)
            {
                // Most flags are handled in EMEVD, including all 'effect' modifiers.

                if (!Hook.Loaded)
                {
                    // Pause, then try again.
                    Thread.Sleep(100);
                    continue;
                }

                if (GetFlag(GameFlag.RandomizedMapsLoaded))
                {
                    // Randomized maps have been loaded in EMEVD. Reset MSBs after a delay.
                    Console.WriteLine("--> Randomized/edited maps loaded. Starting reset countdown.");
                    DisableFlag(GameFlag.RandomizedMapsLoaded);
                    RestartTimer("RandomizeMaps");
                    // MSBs will be reset to default when timer elapses.
                }

                foreach (GameFlag cosplayFlag in Cosplays.CosplayFlags)
                {
                    if (GetFlag(cosplayFlag))
                    {
                        if (cosplayFlag == GameFlag.CosplayLogan)
                            AttuneSorcerer();
                        else if (cosplayFlag == GameFlag.CosplayLaurentius)
                            AttunePyromancer();
                        else if (cosplayFlag == GameFlag.CosplayOswald)
                            AttuneCleric();
                        else if (cosplayFlag == GameFlag.CosplayPharis)
                            EnableFlag(GameFlag.ArrowGift);

                        RecordPreviousEquipment();
                        CurrentCosplay = cosplayFlag;  // threaded `CosplayCheck()` will start forcefully equipping
                        EnableFlag(GameFlag.RequestHealResistances);  // EMEVD implements a one-frame delay
                        DisableFlag(cosplayFlag);
                        RestartTimer("Cosplay");
                        RestartTimer("CosplayCooldown");
                    }
                }

                if (GetFlag(GameFlag.WanderingEnemies))
                {
                    DisableFlag(GameFlag.WanderingEnemies);
                    // This takes 10-15 seconds, so it is threaded.
                    Thread enemyMoveThread = new Thread(MoveEnemiesInAllMaps);
                    enemyMoveThread.Start();
                }
                if (GetFlag(GameFlag.DeathFollowsYou))
                {
                    DisableFlag(GameFlag.DeathFollowsYou);
                    Thread deathFollowsYouThread = new Thread(DeathFollowsYou);
                    deathFollowsYouThread.Start();
                }
                if (GetFlag(GameFlag.ForestMode))
                {
                    DisableFlag(GameFlag.ForestMode);
                    // This takes a few seconds, so it is threaded.
                    Thread forestModeThread = new Thread(EnableForestMode);
                    forestModeThread.Start();
                }
                if (GetFlag(GameFlag.GenderSwitch))
                {
                    DisableFlag(GameFlag.GenderSwitch);
                    GenderSwitch();
                }
                if (GetFlag(GameFlag.TightCamera))
                {
                    DisableFlag(GameFlag.TightCamera);
                    CloseCamera();
                }
                if (GetFlag(GameFlag.WideCamera))
                {
                    DisableFlag(GameFlag.WideCamera);
                    FarCamera();
                }
                if (GetFlag(GameFlag.InvertedCamera))
                {
                    DisableFlag(GameFlag.InvertedCamera);
                    InvertedCamera();
                }
                if (GetFlag(GameFlag.RetroCamera))
                {
                    DisableFlag(GameFlag.RetroCamera);
                    EnableRetroCamera();
                }
                if (GetFlag(GameFlag.InvisiblePlayer))
                {
                    DisableFlag(GameFlag.InvisiblePlayer);
                    MakePlayerInvisible();
                }

                Thread.Sleep(10);  // less than one frame (at 60 Hz)
            }
        }

        #region Camera

        void CloseCamera()
        {
            Hook.SetCameraFov(0.2f);
            RestartTimer("CameraFOV");
        }

        void FarCamera()
        {
            Hook.SetCameraFov(2.0f);
            RestartTimer("CameraFOV");
        }

        void InvertedCamera()
        {
            Hook.SetCameraFov(-1.0f);
            RestartTimer("CameraFOV");
        }

        void EnableRetroCamera()
        {
            Console.WriteLine("--> Enabling retro camera mode.");
            Thread retroCameraThread = new Thread(RetroCameraUpdate);
            retroCameraThread.Start();
        }

        void RetroCameraUpdate()
        {
            double maxPlanarDistance = 16.0 * 16.0;  // in XZ plane
            double maxHeightChange = 4.0;  // just enough for Firelink levels

            Hook.DisableCameraFollow();
            
            Stopwatch retroTime = new Stopwatch();
            retroTime.Start();
            while (retroTime.ElapsedMilliseconds < Settings.EffectDurations["RetroCamera"])
            {
                Hook.GetPosition(out float x, out float y, out float z, out float _);
                Vector3 playerPos = new Vector3(x, y, z);
                Hook.GetCameraPosition(out float cx, out float cy, out float cz);
                Vector3 cameraPos = new Vector3(cx, cy, cz);
                double planarDistSq = Math.Pow(playerPos.X - cameraPos.X, 2) + Math.Pow(playerPos.Z - cameraPos.Z, 2);
                double heightDist = Math.Abs(playerPos.Y - cameraPos.Y);
                if (planarDistSq > maxPlanarDistance || heightDist > maxHeightChange)
                {
                    // Reset frozen camera position.
                    Hook.EnableCameraFollow();
                    Thread.Sleep(17);
                    Hook.DisableCameraFollow();
                }
            }
            Hook.EnableCameraFollow();
            retroTime.Stop();
            Console.WriteLine("--> Disabling retro camera mode.");
        }

        void OnCameraFOVTimerElapsed(object source, ElapsedEventArgs e)
        {
            Hook.SetCameraFov(0.75f);
            Console.WriteLine("--> Restored standard camera FOV.");
        }

        #endregion

        #region Enemies

        void MoveEnemiesInAllMaps()
        {
            // Randomly move all enemies in every map.
            // Will not take effect in any currently loaded maps until reload.
            Console.WriteLine("--> Randomly moving enemies.");
            foreach (string msbStem in MSBStems)
            {
                if (msbStem == "m18_01_00_00" || msbStem == "m10_02_00_00")  // skip Undead Asylum and Firelink Shrine (no points)
                    continue;
                Console.Write($"----> Editing {msbStem}... ");
                MapGen.MoveAllEnemies(msbStem, maxDistance: 15.0);
                Console.WriteLine("Done.");
            }
            Console.WriteLine("--> All maps edited.");
            EnableFlag(GameFlag.MapsAreRandomized);  // EMEVD will enable a second flag if this is enabled on map load
        }

        void OnRandomizeMapsTimerElapsed(object source, ElapsedEventArgs e)
        {
            RestoreMSBs();
        }

        void EnableForestMode()
        {
            // Add 20 Possessed Trees in random places in every map.
            // Uses the same flag as Randomize Enemies to ensure the game reloads at least once before MSBs are reset.
            Console.WriteLine("--> Growing some trees.");
            foreach (string msbStem in MSBStems)
            {
                if (msbStem == "m18_01_00_00" || msbStem == "m10_02_00_00")  // skip Undead Asylum and Firelink Shrine (no points)
                    continue;
                Console.Write($"----> Editing {msbStem}... ");
                MapGen.AddTrees(msbStem, treeCount: 100);
                Console.WriteLine("Done.");
            }
            Console.WriteLine("--> All maps edited.");
            EnableFlag(GameFlag.MapsAreRandomized);  // EMEVD will enable a second flag if this is enabled on map load
        }

        void RestoreMSBs()
        {
            // Restore default MSBs.
            Console.Write("--> Restoring default MSBs... ");
            foreach (string msbStem in MSBStems)
                File.Copy($@"Package\map\MapStudio\{msbStem}.msb", GamePath + $@"map\MapStudio\{msbStem}.msb", overwrite: true);
            Console.WriteLine("Done.");
            DisableFlag(GameFlag.MapsAreRandomized);
            DisableFlag(GameFlag.RandomizedMapsLoaded);
        }

        #endregion

        #region Player

        void GenderSwitch()
        {
            Hook.IsMale = !Hook.IsMale;
        }

        void ClearAttunementSlots()
        {
            // Un-attune all spells.
            Console.WriteLine("--> Clearing all attunement slots.");
            Hook.Spell1ID = -1;
            Hook.Spell2ID = -1;
            Hook.Spell3ID = -1;
            Hook.Spell4ID = -1;
            Hook.Spell5ID = -1;
            Hook.Spell6ID = -1;
            Hook.Spell7ID = -1;
            Hook.Spell8ID = -1;
            Hook.Spell9ID = -1;
            Hook.Spell10ID = -1;
            Hook.Spell11ID = -1;
            Hook.Spell12ID = -1;
            Hook.Spell1Casts = 0;
            Hook.Spell2Casts = 0;
            Hook.Spell3Casts = 0;
            Hook.Spell4Casts = 0;
            Hook.Spell5Casts = 0;
            Hook.Spell6Casts = 0;
            Hook.Spell7Casts = 0;
            Hook.Spell8Casts = 0;
            Hook.Spell9Casts = 0;
            Hook.Spell10Casts = 0;
            Hook.Spell11Casts = 0;
            Hook.Spell12Casts = 0;
        }

        void RefillSpells()
        {
            // Recover all casts of every non-empty spell slot.
            Console.WriteLine("--> Refilling spell casts.");
            for (int slot = 1; slot <= 12; slot++)
            {
                int spellID = Hook.GetSpellID(slot);
                if (spellID != -1)
                {
                    short maxCasts = Convert.ToInt16(MagicParam.Rows.Find(e => e.ID == spellID)["maxQuantity"].Value);
                    Hook.SetSpellCasts(slot, maxCasts);
                }
            }
        }

        void AttuneSorcerer()
        {
            Hook.Spell1ID = 3000;  // Soul Arrow
            Hook.Spell2ID = 3020;  // Heavy Soul Arrow
            Hook.Spell3ID = 3040;  // Homing Soulmass
            Hook.Spell4ID = 3060;  // Soul Spear
            Hook.Spell5ID = 3500;  // Cast Light
            Hook.Spell6ID = 3700;  // White Dragon Breath
            Hook.Spell7ID = 3710;  // Dark Orb
            Hook.Spell8ID = 3740;  // Pursuers
            RefillSpells();
        }

        void AttunePyromancer()
        {
            Hook.Spell1ID = 4020;  // Great Fireball
            Hook.Spell2ID = 4040;  // Fire Tempest
            Hook.Spell3ID = 4110;  // Great Combustion
            Hook.Spell4ID = 4210;  // Toxic Mist
            Hook.Spell5ID = 4300;  // Iron Flesh
            Hook.Spell6ID = 4400;  // Power Within
            Hook.Spell7ID = 4510;  // Chaos Storm
            Hook.Spell8ID = 4520;  // Chaos Fire Whip
            RefillSpells();
        }

        void AttuneCleric()
        {
            Hook.Spell1ID = 5010;  // Great Heal
            Hook.Spell2ID = 5040;  // Replenishment
            Hook.Spell3ID = 5110;  // Gravelord Greatsword Dance
            Hook.Spell4ID = 5310;  // Wrath of the Gods
            Hook.Spell5ID = 5510;  // Great Lightning Spear
            Hook.Spell6ID = 5700;  // Karmic Justice
            Hook.Spell7ID = 5900;  // Sunlight Blade
            Hook.Spell8ID = 5320;  // Emit Force
            RefillSpells();
        }

        void RecordPreviousEquipment()
        {
            // Record any previous equipment, except for cosplay equipment (all >= 3000000).
            // Note that this records fists/naked state as well (900000).
            if (Hook.RightHand1 < 3000000)
                PreviousEquipment["RH1"] = Hook.RightHand1;
            if (Hook.RightHand2 < 3000000)
                PreviousEquipment["RH2"] = Hook.RightHand2;
            if (Hook.LeftHand1 < 3000000)
                PreviousEquipment["LH1"] = Hook.LeftHand1;
            if (Hook.LeftHand2 < 3000000)
                PreviousEquipment["LH2"] = Hook.LeftHand2;
            if (Hook.ArmorHead < 3000000)
                PreviousEquipment["Head"] = Hook.ArmorHead;
            if (Hook.ArmorBody < 3000000)
                PreviousEquipment["Body"] = Hook.ArmorBody;
            if (Hook.ArmorArms < 3000000)
                PreviousEquipment["Arms"] = Hook.ArmorArms;
            if (Hook.ArmorLegs < 3000000)
                PreviousEquipment["Legs"] = Hook.ArmorLegs;
        }

        void RemoveCosplayEquipment()
        {
            // Used only on program startup, if cosplay equipment (3000000+) is detected.
            // Sets equipment to Fists/Naked, which may caused glitched slots, but better than permanent cosplay.
            if (Hook.RightHand1 >= 3000000)
                PreviousEquipment["RH1"] = 900000;
            if (Hook.RightHand2 >= 3000000)
                PreviousEquipment["RH2"] = 900000;
            if (Hook.LeftHand1 >= 3000000)
                PreviousEquipment["LH1"] = 900000;
            if (Hook.LeftHand2 >= 3000000)
                PreviousEquipment["LH2"] = 900000;
            if (Hook.ArmorHead >= 3000000)
                PreviousEquipment["Head"] = 900000;
            if (Hook.ArmorBody >= 3000000)
                PreviousEquipment["Body"] = 901000;
            if (Hook.ArmorArms >= 3000000)
                PreviousEquipment["Arms"] = 902000;
            if (Hook.ArmorLegs >= 3000000)
                PreviousEquipment["Legs"] = 903000;
        }

        void CosplayCheck()
        {
            while (true)
            {
                if (CurrentCosplay == null)
                {
                    // Restore any previous equipment, then clear record of it.
                    bool requestRepair = false;
                    if (PreviousEquipment["RH1"] != -1)
                    {
                        Hook.RightHand1 = PreviousEquipment["RH1"];
                        PreviousEquipment["RH1"] = -1;
                        requestRepair = true;
                    }
                    if (PreviousEquipment["RH2"] != -1)
                    {
                        Hook.RightHand2 = PreviousEquipment["RH2"];
                        PreviousEquipment["RH2"] = -1;
                    }
                    if (PreviousEquipment["LH1"] != -1)
                    {
                        Hook.LeftHand1 = PreviousEquipment["LH1"];
                        PreviousEquipment["LH1"] = -1;
                        requestRepair = true;
                    }
                    if (PreviousEquipment["LH2"] != -1)
                    {
                        Hook.LeftHand2 = PreviousEquipment["LH2"];
                        PreviousEquipment["LH2"] = -1;
                    }
                    if (PreviousEquipment["Head"] != -1)
                    {
                        Hook.ArmorHead = PreviousEquipment["Head"];
                        PreviousEquipment["Head"] = -1;
                    }
                    if (PreviousEquipment["Body"] != -1)
                    {
                        Hook.ArmorBody = PreviousEquipment["Body"];
                        PreviousEquipment["Body"] = -1;
                    }
                    if (PreviousEquipment["Arms"] != -1)
                    {
                        Hook.ArmorArms = PreviousEquipment["Arms"];
                        PreviousEquipment["Arms"] = -1;
                    }
                    if (PreviousEquipment["Legs"] != -1)
                    {
                        Hook.ArmorLegs = PreviousEquipment["Legs"];
                        PreviousEquipment["Legs"] = -1;
                    }
                    if (requestRepair)
                        EnableFlag(GameFlag.RequestRepair);
                }
                else
                {
                    // Force-equip cosplay equipment, levelled according to the number of major bosses defeated.
                    Cosplays.Equipment[CurrentCosplay.Value].EquipCosplay(Hook, DeadBossCount);
                }
                Thread.Sleep(100);  // Minor pause between updates.
            }
        }

        void OnCosplayTimerElapsed(object source, ElapsedEventArgs e)
        {
            CurrentCosplay = null;
            ClearAttunementSlots();
        }

        void MakePlayerInvisible()
        {
            Thread fadeOutThread = new Thread(FadeOutPlayer);
            fadeOutThread.Start();
            RestartTimer("InvisiblePlayer");
        }

        void FadeOutPlayer()
        {
            Stopwatch sw = new Stopwatch();
            sw.Start();
            while (sw.ElapsedMilliseconds < 1000)
            {
                Hook.PlayerOpacity = 1.0f - (sw.ElapsedMilliseconds / 1000.0f);
                Thread.Sleep(17);  // about one frame
            }
            Hook.PlayerOpacity = 0.0f;
        }

        void OnInvisiblePlayerTimerElapsed(object source, ElapsedEventArgs e)
        {
            Thread fadeInThread = new Thread(FadeInPlayer);
            fadeInThread.Start();
        }

        void FadeInPlayer()
        {
            Stopwatch sw = new Stopwatch();
            sw.Start();
            while (sw.ElapsedMilliseconds < 1000)
            {
                Hook.PlayerOpacity = sw.ElapsedMilliseconds / 1000.0f;
                Thread.Sleep(17);  // about one frame
            }
            Hook.PlayerOpacity = 1.0f;
        }

        void DeathFollowsYou()
        {
            // Keeps a list of player positions, updated every second.
            // If the player returns too close to a previous position, they lose health.

            // First, request warning message and wait two seconds.
            EnableFlag(GameFlag.LavaWarning);
            Thread.Sleep(2000);
            
            float deathDistSq = 0.1f;
            List<Vector3> positions = new List<Vector3>();
            Stopwatch runTime = new Stopwatch();
            runTime.Start();
            while (runTime.ElapsedMilliseconds < Settings.EffectDurations["DeathFollowsYou"])
            {
                Thread.Sleep(250);  // 4 times per second
                Hook.GetPosition(out float x, out float y, out float z, out float _);
                Vector3 pos = new Vector3(x, y, z);

                foreach (Vector3 oldPos in positions)
                {
                    double distSq = Math.Pow(x - oldPos.X, 2) + Math.Pow(y - oldPos.Y, 2) + Math.Pow(z - oldPos.Z, 2);
                    if (distSq < deathDistSq)
                    {
                        Hook.Health -= 25;
                        break;
                    }
                }

                positions.Add(pos);
            }
            runTime.Stop();
        }

        #endregion

        void SetParams()
        {
            // Load Magic parameters from game (for base spell casts).
            BND3 paramdefBnd = BND3.Read(GamePath + @"paramdef\paramdef.paramdefbnd.dcx");
            PARAMDEF magicParamdef = null;
            PARAMDEF npcParamdef = null;
            foreach (BinderFile file in paramdefBnd.Files)
            {
                PARAMDEF paramdef = PARAMDEF.Read(file.Bytes);
                if (paramdef.ParamType == "MAGIC_PARAM_ST")
                {
                    magicParamdef = paramdef;
                    break;
                }
            }
            foreach (BinderFile file in paramdefBnd.Files)
            {
                PARAMDEF paramdef = PARAMDEF.Read(file.Bytes);
                if (paramdef.ParamType == "NPC_PARAM_ST")
                {
                    npcParamdef = paramdef;
                    break;
                }
            }
            if (magicParamdef == null) throw new Exception("Could not find MAGIC_PARAM_ST paramdef.");
            if (npcParamdef == null) throw new Exception("Could not find NPC_PARAM_ST paramdef.");

            BND3 gameParam = BND3.Read(DefaultGameParamPath);
            foreach (BinderFile file in gameParam.Files)
            {
                PARAM param = PARAM.Read(file.Bytes);
                if (param.ParamType == "MAGIC_PARAM_ST")
                {
                    param.ApplyParamdef(magicParamdef);
                    MagicParam = param;
                }
                else if (param.ParamType == "NPC_PARAM_ST")
                {
                    param.ApplyParamdef(npcParamdef);
                    NPCParam = param;
                }
                if (MagicParam != null && NPCParam != null)
                    break;
            }
            if (MagicParam == null) throw new Exception("Could not find MAGIC_PARAM_ST param.");
            if (NPCParam == null) throw new Exception("Could not find MAGIC_PARAM_ST param.");
        }

        void RestartTimer(string timerName)
        {
            Timers[timerName].Stop();
            Timers[timerName].Start();
        }
        public void EnableFlag(int flag)
        {
            Hook.EnableEventFlag(flag);
        }
        public void EnableFlag(GameFlag flag)
        {
            Hook.EnableEventFlag((int)flag);
        }

        public void DisableFlag(int flag)
        {
            Hook.DisableEventFlag(flag);
        }
        public void DisableFlag(GameFlag flag)
        {
            Hook.DisableEventFlag((int)flag);
        }

        public bool GetFlag(int flag)
        {
            return Hook.ReadEventFlag(flag);
        }
        public bool GetFlag(GameFlag flag)
        {
            return Hook.ReadEventFlag((int)flag);
        }
    }
}
