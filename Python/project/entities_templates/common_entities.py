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

    # <!--!>


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
