
namespace StJude2021
{
    enum GameFlag
    {
        // Trigger flags mainly.

        // SPECIAL MODIFIERS (2500)
        PatchesAmbush = 11812500,
        ChannelerAmbush = 11812501,
        EnemyAmbush = 11812502,
        InvisibleWorld = 11812503,
        WarpToManus = 11812504,
        PraiseTheSun = 11812505,
        ForestMode = 11812506,
        // HostileAllies = 11812507,
        DeathFollowsYou = 11812508,
        // MoveBonfire = 11812509,
        WanderingEnemies = 11812510,
        RestoreDefaultMSBs = 11812511,
        HyperAggression = 11812512,
        GenderSwitch = 11812513,
        TightCamera = 11812514,
        WideCamera = 11812515,
        InvertedCamera = 11812516,
        RetroCamera = 11812517,
        InvisiblePlayer = 11812518,
        // SpinningPlayer = 11812519,
        SummonGwyns = 11812520,  // c5370
        SummonTrees = 11812521,  // c3350
        SummonBonewheels = 11812522,  // c2930
        
        // COSPLAY (2550)
        CosplayGiantDad = 11812550,
        CosplayGwyn = 11812551,
        CosplayHavel = 11812552,
        CosplayMildred = 11812553,
        CosplayUFC = 11812554,
        CosplayCrystal = 11812555,
        CosplayLogan = 11812556,
        CosplayPharis = 11812557,
        CosplayLaurentius = 11812558,
        CosplayOswald = 11812559,
        CosplayNoob = 11812560,

        // PLAYER EFFECTS (2600)
        PlayerSpeedUp = 11812600,
        PlayerExtremeSpeedUp = 11812601,
        PlayerSpeedDown = 11812602,
        PlayerExtremeSpeedDown = 11812603,
        PlayerHealthRegain = 11812604,
        PlayerHealthDrain = 11812605,
        PlayerMaxHealthUp = 11812606,
        PlayerMaxHealthDown = 11812607,
        PlayerStaminaRegenUp = 11812608,
        PlayerExtremeStaminaRegenUp = 11812609,
        PlayerStaminaRegenDown = 11812610,
        PlayerMaxEquipLoadUp = 11812611,
        PlayerMaxEquipLoadDown = 11812612,
        PlayerDefenseUp = 11812613,
        PlayerInvincible = 11812614,
        PlayerDefenseDown = 11812615,
        PlayerInstantDeath = 11812616,
        PlayerExterminate = 11812617,
        PlayerDetectionDown = 11812618,
        PlayerSoulDrain = 11812619,
        PlayerSturdy = 11812620,
        PlayerFragile = 11812621,
        PlayerWeakHeals = 11812622,
        PlayerPainfulHeals = 11812623,
        PlayerEggInfection = 11812624,
        PlayerBinocularsMode = 11812625,
        PlayerThorny = 11812626,
        PlayerFallControl = 11812627,
        PlayerFireWeapon = 11812628,
        PlayerMagicWeapon = 11812629,
        PlayerLightningWeapon = 11812630,
        PlayerFullHeal = 11812631,
        PlayerOneHPPreHeal = 11812632,
        PlayerSoulBoost = 11812633,
        PlayerSoulSteal = 11812634,

        // ENEMY EFFECTS (2700)
        EnemySpeedUp = 11812700,
        EnemyExtremeSpeedUp = 11812701,
        EnemySpeedDown = 11812702,
        EnemyExtremeSpeedDown = 11812703,
        EnemyHealthRegain = 11812704,
        EnemyMaxHealthUp = 11812705,
        EnemyMaxHealthDown = 11812706,
        EnemyDefenseUp = 11812707,

        // SYSTEM FLAGS
        ArrowGift = 1902,
        LavaWarning = 1904,
        RequestRepair = 1906,
        RandomizedMapsLoaded = 1908,
        RequestHealResistances = 1912,
        MapsAreRandomized = 11812896,
        HookErrorFlag = 11812898,  // enabled here and impedes game progress
        HookCheckFlag = 11812899,  // continually enabled in common EMEVD and disabled here
    }
}
