using PropertyHook;
using System;
using System.Collections.Generic;
using System.Threading;
using System.Runtime.InteropServices;

namespace GameHook
{
    internal class DSRHook : PHook
    {
        DSROffsets Offsets { get; set; }

        PHPointer GroupMaskAddr { get; set; }
        PHPointer ChrDbgAddr { get; set; }
        PHPointer ChrClassBasePtr { get; set; }
        PHPointer ItemGetAddr { get; set; }
        PHPointer BonfireWarpAddr { get; set; }
        PHPointer CameraFovAddr { get; set; }
        PHPointer CameraFovAsmPtr { get; set; }
        PHPointer DisableCameraFollowAddr { get; set; }
        PHPointer InfiniteDurabilityAddr { get; set; }
        PHPointer AutowalkAddr { get; set; }

        PHPointer CamMan { get; set; }
        PHPointer ChrClassWarp { get; set; }
        PHPointer ChrFollowCam { get; set; }
        PHPointer WorldChrBase { get; set; }
        PHPointer ChrData1 { get; set; }
        PHPointer ChrMapData { get; set; }
        PHPointer ChrAnimData { get; set; }
        PHPointer ChrPosData { get; set; }
        PHPointer ChrData2 { get; set; }
        PHPointer ChrSpellData { get; set; }
        PHPointer GraphicsData { get; set; }
        PHPointer MenuMan { get; set; }
        PHPointer EventFlags { get; set; }
        PHPointer ThumbstickInput { get; set; }

        static Dictionary<int, string> VersionStrings { get; } = new Dictionary<int, string>
        {
            [0x4869400] = "1.01",
            [0x496BE00] = "1.01.1",
            [0x37CB400] = "1.01.2",
            [0x3817800] = "1.03",
        };



        public DSRHook(int refreshInterval, int minLifetime) :
            base(refreshInterval, minLifetime, p => p.MainWindowTitle == "DARK SOULS™: REMASTERED")
        {
            Offsets = new DSROffsets();
            CamMan = RegisterRelativeAOB(DSROffsets.CamManBaseAOB, 3, 7, DSROffsets.CamManOffset1, DSROffsets.CamManOffset2);
            ChrFollowCam = RegisterRelativeAOB(DSROffsets.ChrFollowCamAOB, 3, 7, DSROffsets.ChrFollowCamOffset1, DSROffsets.ChrFollowCamOffset2, DSROffsets.ChrFollowCamOffset3);
            GroupMaskAddr = RegisterRelativeAOB(DSROffsets.GroupMaskAOB, 2, 7);
            GraphicsData = RegisterRelativeAOB(DSROffsets.GraphicsDataAOB, 3, 7, DSROffsets.GraphicsDataOffset1, DSROffsets.GraphicsDataOffset2);
            ChrClassWarp = RegisterRelativeAOB(DSROffsets.ChrClassWarpAOB, 3, 7, DSROffsets.ChrClassWarpOffset1);
            WorldChrBase = RegisterRelativeAOB(DSROffsets.WorldChrBaseAOB, 3, 7, DSROffsets.WorldChrBaseOffset1);
            ChrDbgAddr = RegisterRelativeAOB(DSROffsets.ChrDbgAOB, 2, 7);
            MenuMan = RegisterRelativeAOB(DSROffsets.MenuManAOB, 3, 7, DSROffsets.MenuManOffset1);
            ChrClassBasePtr = RegisterRelativeAOB(DSROffsets.ChrClassBaseAOB, 3, 7);
            EventFlags = RegisterRelativeAOB(DSROffsets.EventFlagsAOB, 3, 7, DSROffsets.EventFlagsOffset1, DSROffsets.EventFlagsOffset2);
            ItemGetAddr = RegisterAbsoluteAOB(DSROffsets.ItemGetAOB);
            BonfireWarpAddr = RegisterAbsoluteAOB(DSROffsets.BonfireWarpAOB);
            CameraFovAddr = RegisterAbsoluteAOB(DSROffsets.CameraFovAOB);
            AutowalkAddr = RegisterAbsoluteAOB(DSROffsets.AutowalkAOB);

            ChrData1 = CreateChildPointer(WorldChrBase, (int)DSROffsets.WorldChrBase.ChrData1);
            ChrMapData = CreateBasePointer(IntPtr.Zero);
            ChrAnimData = CreateBasePointer(IntPtr.Zero);
            ChrPosData = CreateBasePointer(IntPtr.Zero);
            ChrData2 = CreateChildPointer(ChrClassBasePtr, DSROffsets.ChrData2Offset1, DSROffsets.ChrData2Offset2);
            ChrSpellData = CreateChildPointer(ChrData2, (int)DSROffsets.ChrData2.Spells);
            ThumbstickInput = CreateBasePointer(IntPtr.Zero);

            OnHooked += DSRHook_OnHooked;
        }

        void DSRHook_OnHooked(object sender, PHEventArgs e)
        {
            Offsets = DSROffsets.GetOffsets(Process.MainModule.ModuleMemorySize);
            ChrMapData = CreateChildPointer(ChrData1, (int)DSROffsets.ChrData1.ChrMapData + Offsets.ChrData1Boost1);
            ChrAnimData = CreateChildPointer(ChrMapData, (int)DSROffsets.ChrMapData.ChrAnimData);
            ChrPosData = CreateChildPointer(ChrMapData, (int)DSROffsets.ChrMapData.ChrPosData);
            ThumbstickInput = CreateChildPointer(ChrMapData, 0x88);

            // Using constant addresses for these for now.
            // Note that these are the same in the normal and debug DSR executables.
            CameraFovAddr = CreateBasePointer(new IntPtr(0x140234626));
            CameraFovAsmPtr = CreateBasePointer(new IntPtr(0x13FFE0000));  // outside memory (need to allocate close)
            DisableCameraFollowAddr = CreateBasePointer(new IntPtr(0x14024E502));
            InfiniteDurabilityAddr = CreateBasePointer(new IntPtr(0x14074BAE1));

            // Should add these to a separate hook, but doing it here for now.
            EnableCameraFovScript();
            EnableInfiniteDurability();  // permanently on for the mod, easiest solution
        }

        public string Version
        {
            get
            {
                if (Hooked)
                {
                    int size = Process.MainModule.ModuleMemorySize;
                    if (VersionStrings.TryGetValue(size, out string version))
                        return version;
                    else
                        return $"0x{size:X8}";
                }
                else
                {
                    return "N/A";
                }
            }
        }

        public bool Loaded => ChrFollowCam.Resolve() != IntPtr.Zero;

        public bool Focused => Hooked && User32.GetForegroundProcessID() == Process.Id;

#region Camera

        public void GetCameraPosition(out float x, out float y, out float z)
        {
            x = CamMan.ReadSingle((int)DSROffsets.CamMan.CameraX);
            y = CamMan.ReadSingle((int)DSROffsets.CamMan.CameraY);
            z = CamMan.ReadSingle((int)DSROffsets.CamMan.CameraZ);
        }

        public void GetCameraAngle (out float x, out float y, out float z)
        {
            x = CamMan.ReadSingle((int)DSROffsets.CamMan.CameraAngleX);
            y = CamMan.ReadSingle((int)DSROffsets.CamMan.CameraAngleY);
            z = CamMan.ReadSingle((int)DSROffsets.CamMan.CameraAngleZ);
        }

        public byte[] DumpFollowCam()
        {
            return ChrFollowCam.ReadBytes(0, 512);
        }

        public void UndumpFollowCam(byte[] value)
        {
            ChrFollowCam.WriteBytes(0, value);
        }

        public void DisableCameraFollow()
        {
            DisableCameraFollowAddr.WriteBytes(0, new byte[] { 0x90, 0x90, 0x90, 0x90, 0x90 });
        }

        public void EnableCameraFollow()
        {
            DisableCameraFollowAddr.WriteBytes(0, new byte[] { 0x66, 0x0F, 0x7F, 0x4F, 0x40 });
        }

        void EnableCameraFovScript()
        {
            // Write assembly script and injection.
            byte[] newmemAsm = new byte[]
            {
                0xA1, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,  // mov eax,[valueAddr]
                0x4C, 0x8B, 0xC2,  // mov r8,rdx
                0xE9, 0x00, 0x00, 0x00, 0x00,  // jmp [return]
                0x00, 0x00, 0x40, 0x3f,  // [value = 0.75]
            };
            byte[] injectAsm = new byte[]
            {
                0xE9, 0x00, 0x00, 0x00, 0x00,  // jmp [newmem]
                0x90,  // nop
            };

            
            // Note that this address-specific override of `Allocate()` uses `MEM_RESERVE | MEM_COMMIT`, not just `MEM_COMMIT`.
            IntPtr asmPtr = Allocate(CameraFovAsmPtr.Resolve(), 0x20, Kernel32.PAGE_EXECUTE_READWRITE);
            IntPtr fovPtr = CameraFovAddr.Resolve();
            
#if DEBUG
            Console.WriteLine($"Camera FOV script written.");
#endif

            long asmAddr = asmPtr.ToInt64();
            long fovAddr = fovPtr.ToInt64();
            Array.Copy(BitConverter.GetBytes(asmAddr + 0x11), 0, newmemAsm, 0x1, 8);

            // Calculate and insert `jmp` offsets (always the same, in practice).
            int jmpNewmem = (int)(asmAddr - (fovAddr + 5));
            Array.Copy(BitConverter.GetBytes(jmpNewmem), 0, injectAsm, 0x1, 4);
            int jmpReturn = (int)(fovAddr + 6 - (asmAddr + 17));
            Array.Copy(BitConverter.GetBytes(jmpReturn), 0, newmemAsm, 0xd, 4);

            if (!Kernel32.WriteBytes(Handle, asmPtr, newmemAsm))
            {
                // Script write failed. Do NOT inject, or it will crash the game.
                Console.WriteLine($"Failed to write Camera FOV assembly. Error: {Marshal.GetLastWin32Error()}");
                Console.WriteLine("(This may be because the script was already injected, in which case it should work anyway.)");
                return;
            }

            if (!Kernel32.WriteBytes(Handle, CameraFovAddr.Resolve(), injectAsm))
            {
                Console.WriteLine($"Failed to inject Camera FOV assembly. Error: {Marshal.GetLastWin32Error()}");
                Console.WriteLine("FOV effects will probably not work.");
            }
            else
            {
                Console.WriteLine($"Enabled Camera FOV script.");
            }
        }

        public void SetCameraFov(float fov)
        {
            IntPtr fovValuePtr = IntPtr.Add(CameraFovAsmPtr.Resolve(), 0x11);
            if (!Kernel32.WriteBytes(Handle, fovValuePtr, BitConverter.GetBytes(fov)))
                Console.WriteLine($"Attempt to set Camera FOV to {fov}, but failed.");
            else
                Console.WriteLine($"--> Camera FOV set to {fov}.");
        }

        public void DisableCameraFovScript()
        {
            // Write original ASM back to Camera FOV address. Not actually used, but here for reference.

            Free(CameraFovAsmPtr.Resolve());
            byte[] defaultAsm = new byte[] { 0x8b, 0x42, 0x50, 0x4C, 0x8B, 0xC2 };
            Kernel32.WriteBytes(Handle, CameraFovAddr.Resolve(), defaultAsm);
        }

#endregion

#region Player
        public int Health
        {
            get => ChrData1.ReadInt32((int)DSROffsets.ChrData1.Health + Offsets.ChrData1Boost2);
            set => ChrData1.WriteInt32((int)DSROffsets.ChrData1.Health + Offsets.ChrData1Boost2, value);
        }

        public int MaxHealth
        {
            get => ChrData2.ReadInt32((int)DSROffsets.ChrData2.MaxHealth);
            set => ChrData2.WriteInt32((int)DSROffsets.ChrData2.MaxHealth, value);
        }

        public int Stamina
        {
            get => ChrData2.ReadInt32((int)DSROffsets.ChrData2.Stamina);
            set => ChrData2.WriteInt32((int)DSROffsets.ChrData2.Stamina, value);
        }

        public int MaxStamina
        {
            get => ChrData2.ReadInt32((int)DSROffsets.ChrData2.MaxStamina);
            set => ChrData2.WriteInt32((int)DSROffsets.ChrData2.MaxStamina, value);
        }

        public int RightHand1
        {
            get => ChrData2.ReadInt32((int)DSROffsets.ChrData2.RightHand1);
            set => ChrData2.WriteInt32((int)DSROffsets.ChrData2.RightHand1, value);
        }

        public int RightHand2
        {
            get => ChrData2.ReadInt32((int)DSROffsets.ChrData2.RightHand2);
            set => ChrData2.WriteInt32((int)DSROffsets.ChrData2.RightHand2, value);
        }

        public int LeftHand1
        {
            get => ChrData2.ReadInt32((int)DSROffsets.ChrData2.LeftHand1);
            set => ChrData2.WriteInt32((int)DSROffsets.ChrData2.LeftHand1, value);
        }

        public int LeftHand2
        {
            get => ChrData2.ReadInt32((int)DSROffsets.ChrData2.LeftHand2);
            set => ChrData2.WriteInt32((int)DSROffsets.ChrData2.LeftHand2, value);
        }

        public int Arrows1
        {
            get => ChrData2.ReadInt32((int)DSROffsets.ChrData2.Arrows1);
            set => ChrData2.WriteInt32((int)DSROffsets.ChrData2.Arrows1, value);
        }

        public int Bolts1
        {
            get => ChrData2.ReadInt32((int)DSROffsets.ChrData2.Bolts1);
            set => ChrData2.WriteInt32((int)DSROffsets.ChrData2.Bolts1, value);
        }

        public int Arrows2
        {
            get => ChrData2.ReadInt32((int)DSROffsets.ChrData2.Arrows2);
            set => ChrData2.WriteInt32((int)DSROffsets.ChrData2.Arrows2, value);
        }

        public int Bolts2
        {
            get => ChrData2.ReadInt32((int)DSROffsets.ChrData2.Bolts2);
            set => ChrData2.WriteInt32((int)DSROffsets.ChrData2.Bolts2, value);
        }

        public int ArmorHead
        {
            get => ChrData2.ReadInt32((int)DSROffsets.ChrData2.ArmorHead);
            set => ChrData2.WriteInt32((int)DSROffsets.ChrData2.ArmorHead, value);
        }

        public int ArmorBody
        {
            get => ChrData2.ReadInt32((int)DSROffsets.ChrData2.ArmorBody);
            set => ChrData2.WriteInt32((int)DSROffsets.ChrData2.ArmorBody, value);
        }

        public int ArmorArms
        {
            get => ChrData2.ReadInt32((int)DSROffsets.ChrData2.ArmorArms);
            set => ChrData2.WriteInt32((int)DSROffsets.ChrData2.ArmorArms, value);
        }

        public int ArmorLegs
        {
            get => ChrData2.ReadInt32((int)DSROffsets.ChrData2.ArmorLegs);
            set => ChrData2.WriteInt32((int)DSROffsets.ChrData2.ArmorLegs, value);
        }

        public int Ring1
        {
            get => ChrData2.ReadInt32((int)DSROffsets.ChrData2.Ring1);
            set => ChrData2.WriteInt32((int)DSROffsets.ChrData2.Ring1, value);
        }

        public int Ring2
        {
            get => ChrData2.ReadInt32((int)DSROffsets.ChrData2.Ring2);
            set => ChrData2.WriteInt32((int)DSROffsets.ChrData2.Ring2, value);
        }

        public int Good1
        {
            get => ChrData2.ReadInt32((int)DSROffsets.ChrData2.Good1);
            set => ChrData2.WriteInt32((int)DSROffsets.ChrData2.Good1, value);
        }

        public int Good2
        {
            get => ChrData2.ReadInt32((int)DSROffsets.ChrData2.Good2);
            set => ChrData2.WriteInt32((int)DSROffsets.ChrData2.Good2, value);
        }

        public int Good3
        {
            get => ChrData2.ReadInt32((int)DSROffsets.ChrData2.Good3);
            set => ChrData2.WriteInt32((int)DSROffsets.ChrData2.Good3, value);
        }

        public int Good4
        {
            get => ChrData2.ReadInt32((int)DSROffsets.ChrData2.Good4);
            set => ChrData2.WriteInt32((int)DSROffsets.ChrData2.Good4, value);
        }

        public int Good5
        {
            get => ChrData2.ReadInt32((int)DSROffsets.ChrData2.Good5);
            set => ChrData2.WriteInt32((int)DSROffsets.ChrData2.Good5, value);
        }

        public bool IsMale
        {
            get => ChrData2.ReadInt32((int)DSROffsets.ChrData2.Gender) == 1;
            set => ChrData2.WriteInt32((int)DSROffsets.ChrData2.Gender, value ? 1 : 0);
        }

        public float FacingAngle
        {
            get => ChrPosData.ReadSingle((int)DSROffsets.ChrPosData.PosAngle);
            set => ChrPosData.WriteSingle((int)DSROffsets.ChrPosData.PosAngle, value);
        }

        public float GetThumbstickInput()
        {
            Console.WriteLine($"ChrData1: {ChrData1.Resolve().ToInt64():X}");
            Console.WriteLine($"ChrMapData: {ChrMapData.Resolve().ToInt64():X}");
            Console.WriteLine($"ThumbstickInput: {ThumbstickInput.Resolve().ToInt64():X}");
            return ThumbstickInput.ReadSingle(0x218);
        }

        public void GetPosition(out float x, out float y, out float z, out float angle)
        {
            x = ChrPosData.ReadSingle((int)DSROffsets.ChrPosData.PosX);
            y = ChrPosData.ReadSingle((int)DSROffsets.ChrPosData.PosY);
            z = ChrPosData.ReadSingle((int)DSROffsets.ChrPosData.PosZ);
            angle = ChrPosData.ReadSingle((int)DSROffsets.ChrPosData.PosAngle);
        }

        public void GetStablePosition(out float x, out float y, out float z, out float angle)
        {
            x = ChrClassWarp.ReadSingle((int)DSROffsets.ChrClassWarp.StableX + Offsets.ChrClassWarpBoost);
            y = ChrClassWarp.ReadSingle((int)DSROffsets.ChrClassWarp.StableY + Offsets.ChrClassWarpBoost);
            z = ChrClassWarp.ReadSingle((int)DSROffsets.ChrClassWarp.StableZ + Offsets.ChrClassWarpBoost);
            angle = ChrClassWarp.ReadSingle((int)DSROffsets.ChrClassWarp.StableAngle + Offsets.ChrClassWarpBoost);
        }

        public void PosWarp(float x, float y, float z, float angle)
        {
            ChrMapData.WriteSingle((int)DSROffsets.ChrMapData.WarpX, x);
            ChrMapData.WriteSingle((int)DSROffsets.ChrMapData.WarpY, y);
            ChrMapData.WriteSingle((int)DSROffsets.ChrMapData.WarpZ, z);
            ChrMapData.WriteSingle((int)DSROffsets.ChrMapData.WarpAngle, angle);
            ChrMapData.WriteBoolean((int)DSROffsets.ChrMapData.Warp, true);
        }

        public bool NoGravity
        {
            set => ChrData1.WriteFlag32((int)DSROffsets.ChrData1.ChrFlags1 + Offsets.ChrData1Boost1, (uint)DSROffsets.ChrFlags1.NoGravity, value);
        }

        public bool NoCollision
        {
            set => ChrMapData.WriteFlag32((int)DSROffsets.ChrMapData.ChrMapFlags, (uint)DSROffsets.ChrMapFlags.DisableMapHit, value);
        }

        public bool DeathCam
        {
            get => WorldChrBase.ReadBoolean((int)DSROffsets.WorldChrBase.DeathCam);
            set => WorldChrBase.WriteBoolean((int)DSROffsets.WorldChrBase.DeathCam, value);
        }

        public float PlayerOpacity
        {
            get => ChrData1.ReadSingle((int)DSROffsets.ChrData1.Opacity);
            set => ChrData1.WriteSingle((int)DSROffsets.ChrData1.Opacity, value);
        }

        public int LastBonfire
        {
            get => ChrClassWarp.ReadInt32((int)DSROffsets.ChrClassWarp.LastBonfire + Offsets.ChrClassWarpBoost);
            set => ChrClassWarp.WriteInt32((int)DSROffsets.ChrClassWarp.LastBonfire + Offsets.ChrClassWarpBoost, value);
        }

        public float AnimSpeed
        {
            set => ChrAnimData.WriteSingle((int)DSROffsets.ChrAnimData.AnimSpeed, value);
        }

        public void EnableInfiniteDurability()
        {
            InfiniteDurabilityAddr.WriteBytes(0, new byte[] { 0x41, 0x8D, 0x01, 0x90, 0x45, 0x8B, 0xC3 });
        }

        public void DisableInfiniteDurability()
        {
            InfiniteDurabilityAddr.WriteBytes(0, new byte[] { 0x41, 0x8D, 0x41, 0xFF, 0x45, 0x8B, 0xC3 });
        }

        #endregion

        #region Stats
        public byte Class
        {
            get => ChrData2.ReadByte((int)DSROffsets.ChrData2.Class);
            set => ChrData2.WriteByte((int)DSROffsets.ChrData2.Class, value);
        }

        public int Humanity
        {
            get => ChrData2.ReadInt32((int)DSROffsets.ChrData2.Humanity);
            set => ChrData2.WriteInt32((int)DSROffsets.ChrData2.Humanity, value);
        }

        public int Souls
        {
            get => ChrData2.ReadInt32((int)DSROffsets.ChrData2.Souls);
            set => ChrData2.WriteInt32((int)DSROffsets.ChrData2.Souls, value);
        }

        public int SoulLevel
        {
            get => ChrData2.ReadInt32((int)DSROffsets.ChrData2.SoulLevel);
            set => ChrData2.WriteInt32((int)DSROffsets.ChrData2.SoulLevel, value);
        }

        public int Vitality
        {
            get => ChrData2.ReadInt32((int)DSROffsets.ChrData2.Vitality);
            set => ChrData2.WriteInt32((int)DSROffsets.ChrData2.Vitality, value);
        }

        public int Attunement
        {
            get => ChrData2.ReadInt32((int)DSROffsets.ChrData2.Attunement);
            set => ChrData2.WriteInt32((int)DSROffsets.ChrData2.Attunement, value);
        }

        public int Endurance
        {
            get => ChrData2.ReadInt32((int)DSROffsets.ChrData2.Endurance);
            set => ChrData2.WriteInt32((int)DSROffsets.ChrData2.Endurance, value);
        }

        public int Strength
        {
            get => ChrData2.ReadInt32((int)DSROffsets.ChrData2.Strength);
            set => ChrData2.WriteInt32((int)DSROffsets.ChrData2.Strength, value);
        }

        public int Dexterity
        {
            get => ChrData2.ReadInt32((int)DSROffsets.ChrData2.Dexterity);
            set => ChrData2.WriteInt32((int)DSROffsets.ChrData2.Dexterity, value);
        }

        public int Resistance
        {
            get => ChrData2.ReadInt32((int)DSROffsets.ChrData2.Resistance);
            set => ChrData2.WriteInt32((int)DSROffsets.ChrData2.Resistance, value);
        }

        public int Intelligence
        {
            get => ChrData2.ReadInt32((int)DSROffsets.ChrData2.Intelligence);
            set => ChrData2.WriteInt32((int)DSROffsets.ChrData2.Intelligence, value);
        }

        public int Faith
        {
            get => ChrData2.ReadInt32((int)DSROffsets.ChrData2.Faith);
            set => ChrData2.WriteInt32((int)DSROffsets.ChrData2.Faith, value);
        }
#endregion

#region Spells
        public int Spell1ID
        {
            get => ChrSpellData.ReadInt32((int)DSROffsets.ChrSpells.Spell1ID);
            set => ChrSpellData.WriteInt32((int)DSROffsets.ChrSpells.Spell1ID, value);
        }
        public int Spell1Casts
        {
            get => ChrSpellData.ReadInt32((int)DSROffsets.ChrSpells.Spell1Casts);
            set => ChrSpellData.WriteInt32((int)DSROffsets.ChrSpells.Spell1Casts, value);
        }
        public int Spell2ID
        {
            get => ChrSpellData.ReadInt32((int)DSROffsets.ChrSpells.Spell2ID);
            set => ChrSpellData.WriteInt32((int)DSROffsets.ChrSpells.Spell2ID, value);
        }
        public int Spell2Casts
        {
            get => ChrSpellData.ReadInt32((int)DSROffsets.ChrSpells.Spell2Casts);
            set => ChrSpellData.WriteInt32((int)DSROffsets.ChrSpells.Spell2Casts, value);
        }
        public int Spell3ID
        {
            get => ChrSpellData.ReadInt32((int)DSROffsets.ChrSpells.Spell3ID);
            set => ChrSpellData.WriteInt32((int)DSROffsets.ChrSpells.Spell3ID, value);
        }
        public int Spell3Casts
        {
            get => ChrSpellData.ReadInt32((int)DSROffsets.ChrSpells.Spell3Casts);
            set => ChrSpellData.WriteInt32((int)DSROffsets.ChrSpells.Spell3Casts, value);
        }
        public int Spell4ID
        {
            get => ChrSpellData.ReadInt32((int)DSROffsets.ChrSpells.Spell4ID);
            set => ChrSpellData.WriteInt32((int)DSROffsets.ChrSpells.Spell4ID, value);
        }
        public int Spell4Casts
        {
            get => ChrSpellData.ReadInt32((int)DSROffsets.ChrSpells.Spell4Casts);
            set => ChrSpellData.WriteInt32((int)DSROffsets.ChrSpells.Spell4Casts, value);
        }
        public int Spell5ID
        {
            get => ChrSpellData.ReadInt32((int)DSROffsets.ChrSpells.Spell5ID);
            set => ChrSpellData.WriteInt32((int)DSROffsets.ChrSpells.Spell5ID, value);
        }
        public int Spell5Casts
        {
            get => ChrSpellData.ReadInt32((int)DSROffsets.ChrSpells.Spell5Casts);
            set => ChrSpellData.WriteInt32((int)DSROffsets.ChrSpells.Spell5Casts, value);
        }
        public int Spell6ID
        {
            get => ChrSpellData.ReadInt32((int)DSROffsets.ChrSpells.Spell6ID);
            set => ChrSpellData.WriteInt32((int)DSROffsets.ChrSpells.Spell6ID, value);
        }
        public int Spell6Casts
        {
            get => ChrSpellData.ReadInt32((int)DSROffsets.ChrSpells.Spell6Casts);
            set => ChrSpellData.WriteInt32((int)DSROffsets.ChrSpells.Spell6Casts, value);
        }
        public int Spell7ID
        {
            get => ChrSpellData.ReadInt32((int)DSROffsets.ChrSpells.Spell7ID);
            set => ChrSpellData.WriteInt32((int)DSROffsets.ChrSpells.Spell7ID, value);
        }
        public int Spell7Casts
        {
            get => ChrSpellData.ReadInt32((int)DSROffsets.ChrSpells.Spell7Casts);
            set => ChrSpellData.WriteInt32((int)DSROffsets.ChrSpells.Spell7Casts, value);
        }
        public int Spell8ID
        {
            get => ChrSpellData.ReadInt32((int)DSROffsets.ChrSpells.Spell8ID);
            set => ChrSpellData.WriteInt32((int)DSROffsets.ChrSpells.Spell8ID, value);
        }
        public int Spell8Casts
        {
            get => ChrSpellData.ReadInt32((int)DSROffsets.ChrSpells.Spell8Casts);
            set => ChrSpellData.WriteInt32((int)DSROffsets.ChrSpells.Spell8Casts, value);
        }
        public int Spell9ID
        {
            get => ChrSpellData.ReadInt32((int)DSROffsets.ChrSpells.Spell9ID);
            set => ChrSpellData.WriteInt32((int)DSROffsets.ChrSpells.Spell9ID, value);
        }
        public int Spell9Casts
        {
            get => ChrSpellData.ReadInt32((int)DSROffsets.ChrSpells.Spell9Casts);
            set => ChrSpellData.WriteInt32((int)DSROffsets.ChrSpells.Spell9Casts, value);
        }
        public int Spell10ID
        {
            get => ChrSpellData.ReadInt32((int)DSROffsets.ChrSpells.Spell10ID);
            set => ChrSpellData.WriteInt32((int)DSROffsets.ChrSpells.Spell10ID, value);
        }
        public int Spell10Casts
        {
            get => ChrSpellData.ReadInt32((int)DSROffsets.ChrSpells.Spell10Casts);
            set => ChrSpellData.WriteInt32((int)DSROffsets.ChrSpells.Spell10Casts, value);
        }
        public int Spell11ID
        {
            get => ChrSpellData.ReadInt32((int)DSROffsets.ChrSpells.Spell11ID);
            set => ChrSpellData.WriteInt32((int)DSROffsets.ChrSpells.Spell11ID, value);
        }
        public int Spell11Casts
        {
            get => ChrSpellData.ReadInt32((int)DSROffsets.ChrSpells.Spell11Casts);
            set => ChrSpellData.WriteInt32((int)DSROffsets.ChrSpells.Spell11Casts, value);
        }
        public int Spell12ID
        {
            get => ChrSpellData.ReadInt32((int)DSROffsets.ChrSpells.Spell12ID);
            set => ChrSpellData.WriteInt32((int)DSROffsets.ChrSpells.Spell12ID, value);
        }
        public int Spell12Casts
        {
            get => ChrSpellData.ReadInt32((int)DSROffsets.ChrSpells.Spell12Casts);
            set => ChrSpellData.WriteInt32((int)DSROffsets.ChrSpells.Spell12Casts, value);
        }

        public int GetSpellID(int slot)
        {
            if (slot < 1 || 12 < slot)
                throw new ArgumentException($"Spell slot must be between 1 and 12, not {slot}.");
            return ChrSpellData.ReadInt32((int)DSROffsets.ChrSpells.Spell1ID + (slot - 1) * 0x8);
        }

        public void SetSpellID(int slot, int spellID)
        {
            if (slot < 1 || 12 < slot)
                throw new ArgumentException($"Spell slot must be between 1 and 12, not {slot}.");
            ChrSpellData.WriteInt32((int)DSROffsets.ChrSpells.Spell1ID + (slot - 1) * 0x8, spellID);
        }

        public int GetSpellCasts(int slot)
        {
            // Note that "three" casts in here are used per actual cast.
            if (slot < 1 || 12 < slot)
                throw new ArgumentException($"Spell slot must be between 1 and 12, not {slot}.");
            return ChrSpellData.ReadInt32((int)DSROffsets.ChrSpells.Spell1Casts + (slot - 1) * 0x8) / 3;
        }

        public void SetSpellCasts(int slot, int casts)
        {
            // Note that "three" casts in here are used per actual cast.
            if (slot < 1 || 12 < slot)
                throw new ArgumentException($"Spell slot must be between 1 and 12, not {slot}.");
            casts *= 3;
            ChrSpellData.WriteInt32((int)DSROffsets.ChrSpells.Spell1Casts + (slot - 1) * 0x8, casts);
        }
#endregion

#region Items
        public void GetItem(int category, int id, int quantity)
        {
            byte[] asm = (byte[])DSRAssembly.GetItem.Clone();

            byte[] bytes = BitConverter.GetBytes(category);
            Array.Copy(bytes, 0, asm, 0x1, 4);
            bytes = BitConverter.GetBytes(quantity);
            Array.Copy(bytes, 0, asm, 0x7, 4);
            bytes = BitConverter.GetBytes(id);
            Array.Copy(bytes, 0, asm, 0xD, 4);
            bytes = BitConverter.GetBytes((ulong)ChrClassBasePtr.Resolve());
            Array.Copy(bytes, 0, asm, 0x19, 8);
            bytes = BitConverter.GetBytes((ulong)ItemGetAddr.Resolve());
            Array.Copy(bytes, 0, asm, 0x46, 8);

            Execute(asm);
        }
#endregion

#region Cheats
        public bool PlayerDeadMode
        {
            get => ChrData1.ReadFlag32((int)DSROffsets.ChrData1.ChrFlags1 + Offsets.ChrData1Boost1, (uint)DSROffsets.ChrFlags1.SetDeadMode);
            set => ChrData1.WriteFlag32((int)DSROffsets.ChrData1.ChrFlags1 + Offsets.ChrData1Boost1, (uint)DSROffsets.ChrFlags1.SetDeadMode, value);
        }

        public bool PlayerNoDead
        {
            set => ChrDbgAddr.WriteBoolean((int)DSROffsets.ChrDbg.PlayerNoDead, value);
        }

        public bool PlayerDisableDamage
        {
            set => ChrData1.WriteFlag32((int)DSROffsets.ChrData1.ChrFlags1 + Offsets.ChrData1Boost1, (uint)DSROffsets.ChrFlags1.DisableDamage, value);
        }

        public bool PlayerNoHit
        {
            set => ChrData1.WriteFlag32((int)DSROffsets.ChrData1.ChrFlags2 + Offsets.ChrData1Boost2, (uint)DSROffsets.ChrFlags2.NoHit, value);
        }

        public bool PlayerNoStamina
        {
            set => ChrData1.WriteFlag32((int)DSROffsets.ChrData1.ChrFlags2 + Offsets.ChrData1Boost2, (uint)DSROffsets.ChrFlags2.NoStaminaConsumption, value);
        }

        public bool PlayerSuperArmor
        {
            set => ChrData1.WriteFlag32((int)DSROffsets.ChrData1.ChrFlags1 + Offsets.ChrData1Boost1, (uint)DSROffsets.ChrFlags1.SetSuperArmor, value);
        }

        public bool PlayerHide
        {
            set => ChrDbgAddr.WriteBoolean((int)DSROffsets.ChrDbg.PlayerHide, value);
        }

        public bool PlayerSilence
        {
            set => ChrDbgAddr.WriteBoolean((int)DSROffsets.ChrDbg.PlayerSilence, value);
        }

        public bool PlayerExterminate
        {
            set => ChrDbgAddr.WriteBoolean((int)DSROffsets.ChrDbg.PlayerExterminate, value);
        }

        public bool PlayerNoGoods
        {
            set => ChrData1.WriteFlag32((int)DSROffsets.ChrData1.ChrFlags2 + Offsets.ChrData1Boost2, (uint)DSROffsets.ChrFlags2.NoGoodsConsume, value);
        }

        public bool AllNoArrow
        {
            set => ChrDbgAddr.WriteBoolean((int)DSROffsets.ChrDbg.AllNoArrowConsume, value);
        }

        public bool AllNoMagicQty
        {
            set => ChrDbgAddr.WriteBoolean((int)DSROffsets.ChrDbg.AllNoMagicQtyConsume, value);
        }

        public bool AllNoDead
        {
            set => ChrDbgAddr.WriteBoolean((int)DSROffsets.ChrDbg.AllNoDead, value);
        }

        public bool AllNoDamage
        {
            set => ChrDbgAddr.WriteBoolean((int)DSROffsets.ChrDbg.AllNoDamage, value);
        }

        public bool AllNoHit
        {
            set => ChrDbgAddr.WriteBoolean((int)DSROffsets.ChrDbg.AllNoHit, value);
        }

        public bool AllNoStamina
        {
            set => ChrDbgAddr.WriteBoolean((int)DSROffsets.ChrDbg.AllNoStaminaConsume, value);
        }

        public bool AllNoAttack
        {
            set => ChrDbgAddr.WriteBoolean((int)DSROffsets.ChrDbg.AllNoAttack, value);
        }

        public bool AllNoMove
        {
            set => ChrDbgAddr.WriteBoolean((int)DSROffsets.ChrDbg.AllNoMove, value);
        }

        public bool AllNoUpdateAI
        {
            set => ChrDbgAddr.WriteBoolean((int)DSROffsets.ChrDbg.AllNoUpdateAI, value);
        }
#endregion

#region Graphics
        public bool DrawMap
        {
            set => GroupMaskAddr.WriteBoolean((int)DSROffsets.GroupMask.Map, value);
        }

        public bool DrawObjects
        {
            set => GroupMaskAddr.WriteBoolean((int)DSROffsets.GroupMask.Objects, value);
        }

        public bool DrawCharacters
        {
            set => GroupMaskAddr.WriteBoolean((int)DSROffsets.GroupMask.Characters, value);
        }

        public bool DrawSFX
        {
            set => GroupMaskAddr.WriteBoolean((int)DSROffsets.GroupMask.SFX, value);
        }

        public bool DrawCutscenes
        {
            set => GroupMaskAddr.WriteBoolean((int)DSROffsets.GroupMask.Cutscenes, value);
        }

        public bool FilterOverride
        {
            set => GraphicsData.WriteBoolean((int)DSROffsets.GraphicsData.FilterOverride, value);
        }

        public void SetFilterValues(float brightR, float brightG, float brightB, float contR, float contG, float contB, float saturation, float hue)
        {
            GraphicsData.WriteSingle((int)DSROffsets.GraphicsData.FilterBrightnessR, brightR);
            GraphicsData.WriteSingle((int)DSROffsets.GraphicsData.FilterBrightnessG, brightG);
            GraphicsData.WriteSingle((int)DSROffsets.GraphicsData.FilterBrightnessB, brightB);
            GraphicsData.WriteSingle((int)DSROffsets.GraphicsData.FilterContrastR, contR);
            GraphicsData.WriteSingle((int)DSROffsets.GraphicsData.FilterContrastG, contG);
            GraphicsData.WriteSingle((int)DSROffsets.GraphicsData.FilterContrastB, contB);
            GraphicsData.WriteSingle((int)DSROffsets.GraphicsData.FilterSaturation, saturation);
            GraphicsData.WriteSingle((int)DSROffsets.GraphicsData.FilterHue, hue);
        }
#endregion

#region Flags
        static Dictionary<string, int> EventFlagGroups { get; } = new Dictionary<string, int>()
        {
            {"0", 0x00000},
            {"1", 0x00500},
            {"5", 0x05F00},
            {"6", 0x0B900},
            {"7", 0x11300},
        };

        static Dictionary<string, int> EventFlagAreas { get; } = new Dictionary<string, int>()
        {
            {"000", 00},
            {"100", 01},
            {"101", 02},
            {"102", 03},
            {"110", 04},
            {"120", 05},
            {"121", 06},
            {"130", 07},
            {"131", 08},
            {"132", 09},
            {"140", 10},
            {"141", 11},
            {"150", 12},
            {"151", 13},
            {"160", 14},
            {"170", 15},
            {"180", 16},
            {"181", 17},
        };

        int GetEventFlagOffset(int ID, out uint mask)
        {
            string idString = ID.ToString("D8");
            if (idString.Length == 8)
            {
                string group = idString.Substring(0, 1);
                string area = idString.Substring(1, 3);
                int section = Int32.Parse(idString.Substring(4, 1));
                int number = Int32.Parse(idString.Substring(5, 3));

                if (EventFlagGroups.ContainsKey(group) && EventFlagAreas.ContainsKey(area))
                {
                    int offset = EventFlagGroups[group];
                    offset += EventFlagAreas[area] * 0x500;
                    offset += section * 128;
                    offset += (number - (number % 32)) / 8;

                    mask = 0x80000000 >> (number % 32);
                    return offset;
                }
            }
            throw new ArgumentException("Unknown event flag ID: " + ID);
        }

        public bool ReadEventFlag(int ID)
        {
            int offset = GetEventFlagOffset(ID, out uint mask);
            return EventFlags.ReadFlag32(offset, mask);
        }

        public void WriteEventFlag(int ID, bool state)
        {
            int offset = GetEventFlagOffset(ID, out uint mask);
            EventFlags.WriteFlag32(offset, mask, state);
        }

        public void EnableEventFlag(int ID)
        {
            WriteEventFlag(ID, true);
        }

        public void DisableEventFlag(int ID)
        {
            WriteEventFlag(ID, false);
        }
#endregion

#region Scripts

        public void ReloadParam(string paramName)
        {
            byte[] reloadAsm = DSRAssembly.GetParamReloadAssembly(paramName);
            IntPtr address = Allocate(4048, Kernel32.PAGE_EXECUTE_READWRITE);
            byte[] zerosOffset = BitConverter.GetBytes(address.ToInt64() + 0x10a);
            byte[] paramNameOffset = BitConverter.GetBytes(address.ToInt64() + 0x122);
            Array.Copy(zerosOffset, 0, reloadAsm, 0xd8, 8);
            Array.Copy(paramNameOffset, 0, reloadAsm, 0x13, 8);
            Kernel32.WriteBytes(Handle, address, reloadAsm);
            Execute(address, 0xFFFFFFFF);
            Thread.Sleep(50);  // need to briefly sleep before freeing the memory, or the game will likely crash!
            Free(address);
        }

        public void BonfireWarp()
        {
            byte[] bonfireWarpAsm = (byte[])DSRAssembly.BonfireWarp.Clone();
            byte[] chrClassBasePtr = BitConverter.GetBytes(ChrClassBasePtr.Resolve().ToInt64());
            byte[] bonfireWarpAddr = BitConverter.GetBytes(BonfireWarpAddr.Resolve().ToInt64());
            Array.Copy(chrClassBasePtr, 0, bonfireWarpAsm, 0x2, 8);
            Array.Copy(bonfireWarpAddr, 0, bonfireWarpAsm, 0x18, 8);
            Execute(bonfireWarpAsm);
        }

        public void WarpToBonfire(int bonfireID)
        {
            LastBonfire = bonfireID;
            BonfireWarp();
        }

#endregion

#region Hotkeys
        public void MenuKick()
        {
            MenuMan.WriteInt32((int)DSROffsets.MenuMan.MenuKick, 2);
        }

#if DEBUG
        public void HotkeyTest1()
        {

        }

        public void HotkeyTest2()
        {

        }
#endif
#endregion
    }
}
