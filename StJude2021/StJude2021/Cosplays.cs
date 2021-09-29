using System.Collections.Generic;
using System.Linq;
using GameHook;

namespace StJude2021
{
    class CosplaySetup
    {
        int MaxDeadBossCount { get; } = 10;
        (int id, int levels) RH1 { get; }
        (int id, int levels) RH2 { get; }
        (int id, int levels) LH1 { get; }
        (int id, int levels) LH2 { get; }
        (int id, int levels) Head { get; }
        (int id, int levels) Body { get; }
        (int id, int levels) Arms { get; }
        (int id, int levels) Legs { get; }
        
        public CosplaySetup(
            (int, int) rh1, (int, int) rh2, (int, int) lh1, (int, int) lh2,
            (int, int) head, (int, int) body, (int, int) arms, (int, int) legs
        )
        {
            RH1 = rh1;
            RH2 = rh2;
            LH1 = lh1;
            LH2 = lh2;
            Head = head;
            Body = body;
            Arms = arms;
            Legs = legs;
        }

        public void EquipCosplay(DSRHook hook, int deadBossCount)
        {
            hook.RightHand1 = RH1.id + (RH1.levels * deadBossCount / MaxDeadBossCount);
            hook.RightHand2 = RH2.id + (RH2.levels * deadBossCount / MaxDeadBossCount);
            hook.LeftHand1 = LH1.id + (LH1.levels * deadBossCount / MaxDeadBossCount);
            hook.LeftHand2 = LH2.id + (LH2.levels * deadBossCount / MaxDeadBossCount);
            hook.ArmorHead = Head.id + (Head.levels * deadBossCount / MaxDeadBossCount);
            hook.ArmorBody = Body.id + (Body.levels * deadBossCount / MaxDeadBossCount);
            hook.ArmorArms = Arms.id + (Arms.levels * deadBossCount / MaxDeadBossCount);
            hook.ArmorLegs = Legs.id + (Legs.levels * deadBossCount / MaxDeadBossCount);
        }
    }

    class Cosplays
    {
        public static GameFlag[] CosplayFlags { get; } = new GameFlag[]
        {
            GameFlag.CosplayGiantDad,
            GameFlag.CosplayGwyn,
            GameFlag.CosplayHavel,
            GameFlag.CosplayMildred,
            GameFlag.CosplayUFC,
            GameFlag.CosplayCrystal,
            GameFlag.CosplayLogan,
            GameFlag.CosplayPharis,
            GameFlag.CosplayLaurentius,
            GameFlag.CosplayOswald,
            GameFlag.CosplayNoob,
        };

        public static Dictionary<GameFlag, CosplaySetup> Equipment { get; } = new Dictionary<GameFlag, CosplaySetup>()
        {
            [GameFlag.CosplayGiantDad] = new CosplaySetup(
                (3000000, 5),
                (900000, 0),
                (3002000, 5),
                (900000, 0),
                (3004000, 0),
                (3005000, 5),
                (3006000, 5),
                (3007000, 5)
            ),
            [GameFlag.CosplayGwyn] = new CosplaySetup(
                (3010000, 5),
                (900000, 0),
                (900000, 0),
                (900000, 0),
                (3014000, 0),
                (3015000, 0),
                (3016000, 0),
                (3017000, 0)
            ),
            [GameFlag.CosplayHavel] = new CosplaySetup(
                (3020000, 5),
                (900000, 0),
                (3022000, 5),
                (900000, 0),
                (3024000, 0),
                (3025000, 0),
                (3026000, 0),
                (3027000, 0)
            ),
            [GameFlag.CosplayMildred] = new CosplaySetup(
                (3030000, 15),
                (900000, 0),
                (3032000, 15),
                (900000, 0),
                (3034000, 10),
                (3035000, 10),
                (3036000, 10),
                (3037000, 10)
            ),
            [GameFlag.CosplayUFC] = new CosplaySetup(
                (3040000, 15),
                (900000, 0),
                (3040000, 15),  // same as RH1
                (900000, 0),
                (3044000, 5),
                (3045000, 5),
                (3046000, 5),
                (3047000, 5)
            ),
            [GameFlag.CosplayCrystal] = new CosplaySetup(
                (3050000, 5),
                (900000, 0),
                (3052000, 5),
                (900000, 0),
                (3054000, 5),
                (3055000, 5),
                (3056000, 5),
                (3057000, 5)
            ),
            [GameFlag.CosplayLogan] = new CosplaySetup(
                (3060000, 0),
                (900000, 0),
                (3062000, 15),
                (900000, 0),
                (3064000, 5),
                (3065000, 5),
                (3066000, 10),
                (3067000, 10)
            ),
            [GameFlag.CosplayPharis] = new CosplaySetup(
                (3070000, 15),
                (900000, 0),
                (3072000, 15),
                (900000, 0),
                (3074000, 10),
                (3075000, 10),
                (3076000, 10),
                (3077000, 10)
            ),
            [GameFlag.CosplayLaurentius] = new CosplaySetup(
                (3080000, 15),
                (900000, 0),
                (3082000, 15),
                (900000, 0),
                (3084000, 10),
                (3085000, 10),
                (3086000, 10),
                (3087000, 10)
            ),
            [GameFlag.CosplayOswald] = new CosplaySetup(
                (3090000, 15),
                (900000, 0),
                (3092000, 15),
                (900000, 0),
                (3094000, 5),
                (3095000, 5),
                (3096000, 5),
                (3097000, 5)
            ),
            [GameFlag.CosplayNoob] = new CosplaySetup(
                (3100000, 5),
                (900000, 0),
                (3102000, 15),
                (900000, 0),
                (3104000, 10),
                (3105000, 10),
                (3106000, 10),
                (3107000, 10)
            ),
        };
    }        
}
