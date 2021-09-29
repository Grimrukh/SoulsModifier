using System;
using System.Collections.Generic;
using System.IO;
using System.Threading;

namespace StJude2021
{
    class ModifierChoice
    {
        GameManager Manager { get; }

        static Dictionary<string, GameFlag> CosplayCommandFlags { get; } = new Dictionary<string, GameFlag>()
        {
            ["giantdad"] = GameFlag.CosplayGiantDad,
            ["gwyn"] = GameFlag.CosplayGwyn,
            ["havel"] = GameFlag.CosplayHavel,
            ["mildred"] = GameFlag.CosplayMildred,
            ["pugilist"] = GameFlag.CosplayUFC,
            ["crystal"] = GameFlag.CosplayCrystal,
            ["sorcerer"] = GameFlag.CosplayLogan,
            ["archer"] = GameFlag.CosplayPharis,
            ["pyromancer"] = GameFlag.CosplayLaurentius,
            ["cleric"] = GameFlag.CosplayOswald,
            ["noob"] = GameFlag.CosplayNoob,
        };

        static Dictionary<string, int> EffectModifiers { get; } = new Dictionary<string, int>()
        {
            ["PlayerSpeedUp"] = 11812600,
            ["PlayerExtremeSpeedUp"] = 11812601,
            ["PlayerSpeedDown"] = 11812602,
            ["PlayerExtremeSpeedDown"] = 11812603,
            ["PlayerHealthRegain"] = 11812604,
            ["PlayerHealthDrain"] = 11812605,
            ["PlayerMaxHealthUp"] = 11812606,
            ["PlayerMaxHealthDown"] = 11812607,
            ["PlayerStaminaRegenUp"] = 11812608,
            ["PlayerExtremeStaminaRegenUp"] = 11812609,
            ["PlayerStaminaRegenDown"] = 11812610,
            ["PlayerMaxEquipLoadUp"] = 11812611,
            ["PlayerMaxEquipLoadDown"] = 11812612,
            ["PlayerDefenseUp"] = 11812613,
            ["PlayerInvincible"] = 11812614,
            ["PlayerDefenseDown"] = 11812615,
            ["PlayerInstantDeath"] = 11812616,
            ["PlayerExterminate"] = 11812617,
            ["PlayerDetectionDown"] = 11812618,
            ["PlayerSoulDrain"] = 11812619,
            ["PlayerSturdy"] = 11812620,
            ["PlayerFragile"] = 11812621,
            ["PlayerWeakHeals"] = 11812622,
            ["PlayerPainfulHeals"] = 11812623,
            ["PlayerEggInfection"] = 11812624,
            ["PlayerBinocularsMode"] = 11812625,
            ["PlayerThorny"] = 11812626,
            ["PlayerFallControl"] = 11812627,
            ["PlayerFireWeapon"] = 11812628,
            ["PlayerMagicWeapon"] = 11812629,
            ["PlayerLightningWeapon"] = 11812630,
            ["PlayerFullHeal"] = 11812631,
            ["PlayerOneHPPreHeal"] = 11812632,
            ["PlayerSoulBoost"] = 11812633,
            ["PlayerSoulSteal"] = 11812634,
            ["EnemySpeedUp"] = 11812700,
            ["EnemyExtremeSpeedUp"] = 11812701,
            ["EnemySpeedDown"] = 11812702,
            ["EnemyExtremeSpeedDown"] = 11812703,
            ["EnemyHealthRegain"] = 11812704,
            ["EnemyMaxHealthUp"] = 11812705,
            ["EnemyMaxHealthDown"] = 11812706,
            ["EnemyDefenseUp"] = 11812707,
        };

        string ModifierFileDir { get; }
        
        public ModifierChoice(GameManager manager, string modFilePath = "")
        {
            Manager = manager;
            ModifierFileDir = modFilePath;
        }

        public void Run(string mode = "file")
        {
            if (mode == "file")
                FileMode();
            else if (mode == "input")
                InputMode();
            else if (mode == "auto")
                AutoMode();
            else
                throw new Exception($"Invalid modifier choice mode: {mode}. Must be 'file' (default), 'input', or 'auto'.");
        }

        void InputMode()
        {
            Console.WriteLine("Type 'help' to see all modifier commands.\n");
            Console.WriteLine("Type 'effect_help' to see all sub-options for the 'effect' modifier command.\n");
            while (true)
            {
                Console.Write(">>> ");
                string input = Console.ReadLine();
                if (!Manager.Hook.Loaded)
                {
                    Console.WriteLine("Game is not loaded! Command not processed.");
                    continue;
                }
                switch (input)
                {
                    case "help":
                        Console.WriteLine(string.Join(
                            Environment.NewLine,
                            "Commands:",
                            "    effect",  // prompts for effect name
                            "    randomize_maps",
                            "    aggressive",
                            "    cosplay",  // prompts for cosplay name
                            "    praise",
                            "    tight_camera",
                            "    wide_camera",
                            "    inverted_camera",
                            "    retro_camera",
                            "    gender_switch",
                            "    invisible_player",
                            "    death_follows",
                            "    patches",
                            "    channeler",
                            "    ambush",
                            "    invisible_world",
                            "    manus",
                            "    gwyns",
                            "    bonewheels",
                            "    trees",
                            "    reset_maps (debug)",
                            "    set_fov (debug)",  // prompts for FOV value
                            "    warp_to_firelink (debug)",
                            ""
                            ));
                        break;
                    case "effect_options":
                        Console.WriteLine("Effects:");
                        foreach (string key in EffectModifiers.Keys)
                            Console.WriteLine($"    {key}");
                        Console.WriteLine();
                        break;
                    case "effect":
                        Console.Write("Effect: ");
                        string effectName = Console.ReadLine();
                        if (!EffectModifiers.ContainsKey(effectName))
                            Console.WriteLine("Invalid effect name.");
                        else
                            Manager.EnableFlag(EffectModifiers[effectName]);
                        break;
                    case "randomize_maps":
                        Manager.EnableFlag(GameFlag.WanderingEnemies);
                        break;
                    case "reset_maps":
                        Manager.EnableFlag(GameFlag.RestoreDefaultMSBs);
                        break;
                    case "aggressive":
                        Manager.EnableFlag(GameFlag.HyperAggression);
                        break;
                    case "cosplay":
                        // These duplicates should also remove stat requirements.
                        Console.WriteLine(string.Join(
                            Environment.NewLine,
                            "Enter a Cosplay preset:",
                            "    giantdad",
                            "    gwyn",
                            "    havel",
                            "    mildred",
                            "    pugilist",
                            "    crystal",
                            "    sorcerer",
                            "    archer",
                            "    pyromancer",
                            "    cleric",
                            "    noob",
                            ""
                        ));
                        Console.Write("Character: ");
                        string equipChr = Console.ReadLine().ToLower();
                        if (!CosplayCommandFlags.ContainsKey(equipChr))
                            Console.WriteLine("Invalid equip preset.");
                        else
                            Manager.EnableFlag(CosplayCommandFlags[equipChr]);
                        break;
                    case "praise":
                        Manager.EnableFlag(GameFlag.PraiseTheSun);
                        break;
                    case "tight_camera":
                        Manager.EnableFlag(GameFlag.TightCamera);
                        break;
                    case "wide_camera":
                        Manager.EnableFlag(GameFlag.WideCamera);
                        break;
                    case "inverted_camera":
                        Manager.EnableFlag(GameFlag.InvertedCamera);
                        break;
                    case "retro_camera":
                        Manager.EnableFlag(GameFlag.RetroCamera);
                        break;
                    case "gender_switch":
                        Manager.EnableFlag(GameFlag.GenderSwitch);
                        break;
                    case "invisible_player":
                        Manager.EnableFlag(GameFlag.InvisiblePlayer);
                        break;
                    case "death_follows":
                        Manager.EnableFlag(GameFlag.DeathFollowsYou);
                        break;
                    case "patches":
                        Manager.EnableFlag(GameFlag.PatchesAmbush);
                        break;
                    case "channeler":
                        Manager.EnableFlag(GameFlag.ChannelerAmbush);
                        break;
                    case "ambush":
                        Manager.EnableFlag(GameFlag.EnemyAmbush);
                        break;
                    case "invisible_world":
                        Manager.EnableFlag(GameFlag.InvisibleWorld);
                        break;
                    case "manus":
                        Manager.EnableFlag(GameFlag.WarpToManus);
                        break;
                    case "gwyns":
                        Manager.EnableFlag(GameFlag.SummonGwyns);
                        break;
                    case "bonewheels":
                        Manager.EnableFlag(GameFlag.SummonBonewheels);
                        break;
                    case "trees":
                        Manager.EnableFlag(GameFlag.ForestMode);
                        break;
                    case "set_fov":
                        Console.Write("FOV: ");
                        if (float.TryParse(Console.ReadLine(), out float fov))
                            Manager.Hook.SetCameraFov(fov);
                        else
                            Console.WriteLine("Invalid FOV value. Must be a float.");
                        break;
                    case "warp_to_firelink":
                        Manager.Hook.WarpToBonfire(1022950);
                        break;
                    default:
                        Console.WriteLine("Invalid test command. Type 'help' to see all options.");
                        break;
                }
            }
        }

        void FileMode()
        {
            if (ModifierFileDir == "")
            {
                Console.WriteLine("No modifier file path known. Cannot use 'file' mode.");
                Console.WriteLine("Press ENTER to exit.");
                Console.ReadLine();
                return;
            }
            while (true)
            {
                if (!Directory.Exists(ModifierFileDir))
                {
                    Console.WriteLine($"Could not find directory: {ModifierFileDir}. Terminating program.");
                    Console.WriteLine("Press ENTER to exit.");
                    Console.ReadLine();
                    break;
                }
                else
                {
                    for (int i = 1; i <= 100; i++)
                    {
                        string indexFilePath = $@"{ModifierFileDir}\mod{i}.txt";
                        if (File.Exists(indexFilePath))
                        {
                            Thread.Sleep(50);  // just in case file is still being written
                            GameFlag modifierFlag = ModifierInfo.ModifierIndices[i - 1];  // note zero index
                            string modifierName = ModifierInfo.ModifierNames[modifierFlag];
                            Console.WriteLine($"{modifierName} ({(int)modifierFlag})");
                            Manager.EnableFlag(modifierFlag);
                            File.Delete(indexFilePath);
                        }
                    }
                    Thread.Sleep(10);  // small break between checks (for all files)
                }
            }
        }

        void AutoMode(int intervalMilliseconds = -1)
        {
            // Enables a random modifier at regular intervals.
            if (intervalMilliseconds == -1)
                intervalMilliseconds = GetAutoInterval();
            while (true)
            {
                int randIndex = Manager.Rand.Next(100);
                GameFlag modifierFlag = ModifierInfo.ModifierIndices[randIndex];
                string modifierName = ModifierInfo.ModifierNames[modifierFlag];
                Console.WriteLine($"{modifierName} ({(int)modifierFlag})");
                Manager.EnableFlag(modifierFlag);
                Thread.Sleep(intervalMilliseconds);
            }
        }

        int GetAutoInterval()
        {
            int intervalMilliseconds;
            while (true)
            {
                Console.Write("Type a whole number of seconds between random effects: ");
                if (!int.TryParse(Console.ReadLine(), out int seconds))
                {
                    Console.WriteLine("Invalid number! Must be a whole number.");
                }
                intervalMilliseconds = 1000 * seconds;
                break;
            }
            return intervalMilliseconds;
        }
    }
}
