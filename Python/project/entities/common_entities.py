from soulstruct.game_types import *


class SystemFlags(Flag):
    HookCheck = 11812899


class TriggerFlags(Flag):
    RequestArrows = 1902
    RequestDeathFollowsWarning = 1904
    RequestRepair = 1906
    MapsAreRandomized = 11812896
    RandomizedMapsLoaded = 1908
    HyperAggressionReTrigger = 1910
    RequestHealResistances = 1912

    PatchesAmbush = 11812500
    ChannelerAmbush = 11812501
    EnemyAmbush = 11812502
    InvisibleWorld = 11812503
    SurpriseManusFight = 11812504
    PraiseTheSun = 11812505
    ForestMode = 11812506
    CantStopMoving = 11812508
    MoveEnemies = 11812510
    RestoreDefaultMSBs = 11812511
    HyperAggression = 11812512
    GenderSwitch = 11812513
    CloseCamera = 11812514
    FarCamera = 11812515
    InvertCamera = 11812516
    FreezeCamera = 11812517
    InvisiblePlayer = 11812518
    OopsAllGwyns = 11812520
    OopsAllBonewheels = 11812522

    EquipGiantDad = 11812550
    EquipGwyn = 11812551
    EquipHavel = 11812552
    EquipMildred = 11812553
    EquipPugilist = 11812554
    EquipCrystal = 11812555
    EquipSorcerer = 11812556
    EquipArcher = 11812557
    EquipPyromancer = 11812558
    EquipCleric = 11812559
    EquipRequest = 11812569

    PlayerSpeedUp = 11812600
    PlayerExtremeSpeedUp = 11812601
    PlayerSpeedDown = 11812602
    PlayerExtremeSpeedDown = 11812603
    PlayerHealthRegain = 11812604
    PlayerHealthDrain = 11812605
    PlayerMaxHealthUp = 11812606
    PlayerMaxHealthDown = 11812607
    PlayerStaminaRegenUp = 11812608
    PlayerExtremeStaminaRegenUp = 11812609
    PlayerStaminaRegenDown = 11812610
    PlayerMaxEquipLoadUp = 11812611
    PlayerMaxEquipLoadDown = 11812612
    PlayerDefenseUp = 11812613
    PlayerInvincible = 11812614
    PlayerDefenseDown = 11812615
    PlayerInstantDeath = 11812616
    PlayerExterminate = 11812617
    PlayerDetectionDown = 11812618
    PlayerSoulDrain = 11812619
    PlayerSturdy = 11812620
    PlayerFragile = 11812621
    PlayerWeakHeals = 11812622
    PlayerPainfulHeals = 11812623
    PlayerEggInfection = 11812624
    PlayerBinocularsMode = 11812625
    PlayerThorny = 11812626
    PlayerFallControl = 11812627
    PlayerFireWeapon = 11812628
    PlayerMagicWeapon = 11812629
    PlayerLightningWeapon = 11812630
    PlayerFullHeal = 11812631
    PlayerOneHPPreHeal = 11812632
    PlayerSoulBoost = 11812633
    PlayerSoulSteal = 11812634
    EnemySpeedUp = 11812700
    EnemyExtremeSpeedUp = 11812701
    EnemySpeedDown = 11812702
    EnemyExtremeSpeedDown = 11812703
    EnemyHealthRegain = 11812704
    EnemyMaxHealthUp = 11812705
    EnemyMaxHealthDown = 11812706
    EnemyDefenseUp = 11812707


class PlayerModelPoints(IntEnum):
    Above = 210
    Behind = 233
    InFront = 234


class CommonText(EventText):
    HookConnectionError = 799999
    ManusDefeated = 800000
    InstantDeathWarning = 800001
    DeathFollowsWarning = 800002
    PraiseTheSun = 800003


class CommonEffects(SpecialEffectParam):
    ManusReward = 801
    ChannelerBuff = 802


class CommonItemLots(ItemLotParam):
    ArrowGift = 500
