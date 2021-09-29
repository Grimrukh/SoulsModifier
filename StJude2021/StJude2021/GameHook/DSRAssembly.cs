using System;
using System.Collections.Generic;
using System.Linq;
using System.Text.RegularExpressions;

namespace GameHook
{
    // Parses output from https://defuse.ca/online-x86-assembler.htm
    // I like to keep the whole thing for quick reference to line numbers and so on
    static class DSRAssembly
    {
        private readonly static Dictionary<string, int> paramEnums = new Dictionary<string, int>()
        {
            ["EquipParamWeapon"] = 0x0,
            ["EquipParamProtector"] = 0x1,
            ["EquipParamAccessory"] = 0x2,
            ["EquipParamGoods"] = 0x3,
            ["ReinforceParamWeapon"] = 0x4,
            ["ReinforceParamProtector"] = 0x5,
            ["NpcParam"] = 0x6,
            ["AtkParam_Npc"] = 0x7,
            ["AtkParam_Pc"] = 0x8,
            ["NpcThinkParam"] = 0x9,
            ["ObjectParam"] = 0xa,
            ["Bullet"] = 0xb,
            ["BehaviorParam"] = 0xc,
            ["BehaviorParam_PC"] = 0xd,
            ["Magic"] = 0xe,
            ["SpEffectParam"] = 0xf,
            ["SpEffectVfxParam"] = 0x10,
            ["TalkParam"] = 0x11,
            ["MenuColorTableParam"] = 0x12,
            ["ItemLotParam"] = 0x13,
            ["MoveParam"] = 0x14,
            ["CharaInitParam"] = 0x15,
            ["EquipMtrlSetParam"] = 0x16,
            ["FaceGenParam"] = 0x17,
            ["RagdollParam"] = 0x18,
            ["ShopLineupParam"] = 0x19,
            ["QwcChange"] = 0x1a,
            ["QwcJudge"] = 0x1b,
            ["GameAreaParam"] = 0x1c,
            ["SkeletonParam"] = 0x1d,
            ["CalcCorrectGraph"] = 0x1e,
            ["LockCamParam"] = 0x1f,
            ["ObjActParam"] = 0x20,
            ["HitMtrlParam"] = 0x21,
            ["KnockBackParam"] = 0x22,
            ["LevelSyncParam"] = 0x23,
            ["CoolTimeParam"] = 0x24,
            ["WhiteCoolTimeParam"] = 0x25,
            // All_Other_Params = 0x26,
        };

        private readonly static Regex asmLineRx = new Regex(@"^[\w\d]+:\s+((?:[\w\d][\w\d] ?)+)");

        private static byte[] LoadDefuseOutput(string lines)
        {
            List<byte> bytes = new List<byte>();
            foreach (string line in Regex.Split(lines, "[\r\n]+"))
            {
                Match match = asmLineRx.Match(line);
                string hexes = match.Groups[1].Value;
                foreach (Match hex in Regex.Matches(hexes, @"\S+"))
                    bytes.Add(Byte.Parse(hex.Value, System.Globalization.NumberStyles.AllowHexSpecifier));
            }
            return bytes.ToArray();
        }

        public static byte[] BonfireWarp { get; } = LoadDefuseOutput(Resource.BonfireWarp);
        public static byte[] GetItem { get; } = LoadDefuseOutput(Resource.GetItem);
        public static byte[] LevelUp { get; } = LoadDefuseOutput(Resource.LevelUp);
        
        public static byte[] GetParamReloadAssembly(string paramName)
        {
            // Returned byte array still needs to have relative offsets 0x100 (at 0xd8) and 0x118 (at 0x15) resolved
            // once memory address for script has been allocated.
            byte[] asm = LoadDefuseOutput(Resource.ParamReload);
            int paramEnum = paramEnums[paramName];
            int paramEnumSignature = (paramEnum + paramEnum * 8) * 8 + 0x10;
            byte[] signatureBytes = BitConverter.GetBytes(paramEnumSignature);
            Array.Copy(signatureBytes, 0, asm, 0x69, 4);  // write signature into assembly script
            byte[] nameBytes = System.Text.Encoding.ASCII.GetBytes(paramName + "\x00");
            byte[] nameBytes16 = System.Text.Encoding.Convert(System.Text.Encoding.ASCII, System.Text.Encoding.Unicode, nameBytes);
            return asm.Concat(nameBytes16).ToArray();
        }
    }
}
