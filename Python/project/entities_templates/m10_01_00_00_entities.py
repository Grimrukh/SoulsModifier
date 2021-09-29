from soulstruct.games import DARK_SOULS_DSR
from soulstruct.game_types import *


class Objects(Object):
    """`Object` entity IDs for MSB and EVS use."""

    # noinspection PyMethodParameters
    def _generate_next_value_(name, _, count, __):
        return Object.auto_generate(count, DARK_SOULS_DSR, 1010000)

    o0110_0000 = 1011670
    o0110_0001 = 1011671
    o0200_0001 = 1011961
    o0200_0002 = 1011962
    o0200_0005 = 1011964
    o0500_0004 = 1011652
    o0500_0027 = 1011653
    o0500_0034 = 1011654
    o1060 = 1011060
    o1110 = 1011450
    o1111_07 = 1011407
    o1111_08 = 1011408
    o1132_16 = 1011103
    o1154_31 = 1011000
    o1154_47 = 1011504
    o1155 = 1011130
    o1155_0000 = 1011501
    o1155_0001 = 1011502
    o1155_0002 = 1011503
    o1155_0003 = 1011500
    o1200_1000 = 1011100
    o1200_1001 = 1011120
    o1201_1000 = 1011101
    o1201_1001 = 1011121
    o1202 = 1011110
    o1206 = 1011151
    o1207 = 1011148
    o1208 = 1011149
    o1209 = 1011141
    o1210_1000 = 1011142
    o1211_1000 = 1011143
    o1212_1000 = 1011144
    o1213_1000 = 1011145
    o1214_1000 = 1011146
    o1215 = 1011140
    o1216_1000 = 1011150
    o1218_0000 = 1011152
    o1219 = 1011147
    o1252 = 1011010
    o1290 = 1011290
    o1303 = 1011111
    o1305_01 = 1011315
    o1305_02 = 1011316
    o1306 = 1011306
    o1308 = 1011320
    o1308_02 = 1011308
    o1310_0000 = 1011310
    o1312_0000 = 1011312
    o1312_01 = 1011311
    o1313_0000 = 1011313
    o1314_0000 = 1011314
    o1316_0000 = 1011250
    o1317_0000 = 1011252
    o1317_0001 = 1011253
    o1317_0002 = 1011255
    o1317_0003 = 1011254
    o1317_04 = 1011317
    o1318_0000 = 1011251
    o1318_01 = 1011318
    o1323_0000 = 1011106
    o1330_0000 = 1011102
    o1403_0000 = 1011990
    o1404_0000 = 1011992
    o1405_0000 = 1011890
    o1406_0000 = 1011892
    o1407_0000 = 1011994
    o1408_0000 = 1011996
    o1409_0000 = 1011998
    o1410_0000 = 1011988
    o1411_0000 = 1011986
    o1412_0000 = 1011984
    o1413_0000 = 1011790
    o1414_0000 = 1011976
    o1415_0000 = 1011982
    o1416_0000 = 1011702
    o1417_0000 = 1011980
    o1418_0000 = 1011978
    o1419_0000 = 1011700
    o1421_0000 = 1011974
    o1421_0001 = 1011972


class Characters(Character):
    """`Character` entity IDs for MSB and EVS use."""

    # noinspection PyMethodParameters
    def _generate_next_value_(name, _, count, __):
        return Character.auto_generate(count, DARK_SOULS_DSR, 1010000)

    c0000_0002 = 6001
    c0000_0003 = 6040
    c0000_0004 = 6540
    c0000_0005 = 6072
    c0000_0006 = 6300
    c0000_0010 = 6580
    c0000_0011 = 6590
    c0000_0012 = 6370
    c0000_PatchesAmbush = 7981
    c1000_0001 = 1010961
    c1000_0002 = 1010962
    c1000_0005 = 1010964
    c1000_0008 = 6480
    c2240_0000 = 1010750
    c2250_0000 = 1010700
    c2300_0000 = 1010340
    c2370_0001 = 1010370
    c2370_TrollChanneler = 7961
    c2500_0001 = 1010250
    c2500_0006 = 1010111
    c2500_0008 = 1010251
    c2500_0021 = 1010263
    c2500_0025 = 1010260
    c2500_0026 = 1010261
    c2500_0027 = 1010262
    c2500_0035 = 1010901
    c2500_0036 = 1010902
    c2500_0037 = 1010903
    c2510_0000 = 6230
    c2520_0004 = 1010150
    c2520_0005 = 1010151
    c2520_0006 = 1010152
    c2520_0007 = 1010153
    c2520_0008 = 1010154
    c2520_0009 = 1010155
    c2520_0012 = 1010911
    c2520_0013 = 1010912
    c2540_0007 = 1010102
    c2540_0014 = 1010906
    c2540_0016 = 1010907
    c2540_0017 = 1010908
    c2550_0010 = 1010130
    c2550_0016 = 6010
    c2550_0020 = 1010103
    c2550_0024 = 1010909
    c2550_0025 = 1010910
    c2550_0042 = 1010200
    c2560_0000 = 1010900
    c2570_0000 = 1010320
    c2570_0003 = 1010905
    c2640_0000 = 6190
    c2792_0000 = 1010350
    c2793_0000 = 1010351
    c3300_0000 = 1010400
    c3340_0003 = 1010500
    c3340_0004 = 1010501
    c3340_0007 = 1010510
    c3340_0008 = 1010511
    c3430_0000 = 1010300
    c3430_0001 = 1010302
    c3431_0000 = 1010301
    c3460_0000 = 1010310
    c3490_0000 = 1013900
    c3490_0001 = 1013910
    c3490_0002 = 1013920
    c3490_0003 = 1013930
    c3490_0004 = 1013940
    c3491_0000 = 1013901
    c3491_0001 = 1013911
    c3491_0002 = 1013921
    c3491_0003 = 1013931
    c3491_0004 = 1013941
    c3491_0005 = 1013902
    c3491_0006 = 1013912
    c3491_0007 = 1013922
    c3491_0008 = 1013932
    c3491_0009 = 1013942
    c5350_0000 = 1010800
    c5350_0001 = 1010801
    c5350_0002 = 1010802
    c5352_0000 = 1010810
    c5352_0001 = 1010811


class PlayerStarts(PlayerStart):
    """`PlayerStart` entity IDs for MSB and EVS use."""

    # noinspection PyMethodParameters
    def _generate_next_value_(name, _, count, __):
        return PlayerStart.auto_generate(count, DARK_SOULS_DSR, 1010000)

    c0000_0001 = 1010998
    c0000_0009 = 1010981


class Collisions(Collision):
    """`Collision` entity IDs for MSB and EVS use."""

    # noinspection PyMethodParameters
    def _generate_next_value_(name, _, count, __):
        return Collision.auto_generate(count, DARK_SOULS_DSR, 1010000)

    h1113B1 = 1013210
    h1115B1 = 1013211
    h7004B1 = 1013200


class Sounds(SoundEvent):
    """`SoundEvent` entity IDs for MSB and EVS use."""

    # noinspection PyMethodParameters
    def _generate_next_value_(name, _, count, __):
        return SoundEvent.auto_generate(count, DARK_SOULS_DSR, 1010000)

    BellGargoylesMusic = 1013800
    CapraDemonMusic = 1013803
    RooftopWindSound = 1013801
    TaurusDemonMusic = 1013802


class VFX(VFXEvent):
    """`VFXEvent` entity IDs for MSB and EVS use."""

    # noinspection PyMethodParameters
    def _generate_next_value_(name, _, count, __):
        return VFXEvent.auto_generate(count, DARK_SOULS_DSR, 1010000)

    BellGargoylesEntranceFog = 1011991
    BellGargoylesExitFog = 1011993
    CapraDemonEntranceFog = 1011791
    CheckpointFog1 = 1011701
    CheckpointFog2 = 1011703
    MultiplayerFog1 = 1011995
    MultiplayerFog2 = 1011997
    MultiplayerFog3 = 1011999
    MultiplayerFog4 = 1011989
    MultiplayerFog5 = 1011987
    MultiplayerFog6 = 1011985
    MultiplayerFog7 = 1011983
    MultiplayerFog8 = 1011981
    MultiplayerFog9 = 1011979
    MultiplayerFog10 = 1011977
    MultiplayerFog11 = 1011975
    MultiplayerFog12 = 1011973
    TaurusDemonEntranceFog = 1011891
    TaurusDemonExitFog = 1011893


class SpawnPoints(SpawnPointEvent):
    """`SpawnPointEvent` entity IDs for MSB and EVS use."""

    # noinspection PyMethodParameters
    def _generate_next_value_(name, _, count, __):
        return SpawnPointEvent.auto_generate(count, DARK_SOULS_DSR, 1010000)

    SpawnPoint0 = 1012960
    SpawnPoint1 = 1012961
    SpawnPoint2 = 1012962
    SpawnPoint3 = 1012963
    SpawnPoint4 = 1012964
    SpawnPoint5 = 1012965
    SpawnPoint6 = 1012966
    SpawnPointAtBoss = 1012950


class Navigation(NavigationEvent):
    """`NavigationEvent` entity IDs for MSB and EVS use."""

    # noinspection PyMethodParameters
    def _generate_next_value_(name, _, count, __):
        return NavigationEvent.auto_generate(count, DARK_SOULS_DSR, 1010000)

    Navmesh_Door05_1 = 1013006
    Navmesh_Door05_2 = 1013008
    Navmesh_Door06 = 1013016
    Navmesh_Door08 = 1013003
    Navmesh_Door10 = 1013000
    Navmesh_Door11 = 1013007
    Navmesh_Door12 = 1013002
    Navmesh_Door13 = 1013010
    Navmesh_Door14 = 1013009
    Navmesh_Door17_4 = 1013004
    Navmesh_Door18 = 1013005
    Navmesh_GateLever = 1013100


class Points(RegionPoint):
    """`RegionPoint` entity IDs for MSB and EVS use."""

    # noinspection PyMethodParameters
    def _generate_next_value_(name, _, count, __):
        return RegionPoint.auto_generate(count, DARK_SOULS_DSR, 1010000)

    LautrecSummonSign = 1012001
    SolaireSummonSign = 1012000


class Cylinders(RegionCylinder):
    """`RegionCylinder` entity IDs for MSB and EVS use."""

    # noinspection PyMethodParameters
    def _generate_next_value_(name, _, count, __):
        return RegionCylinder.auto_generate(count, DARK_SOULS_DSR, 1010000)

    BellGargoylesCutsceneTrigger = 1012999
    BellGargoylesFogRotationTarget = 1012997
    BossOmenCameraEpicenter = 1012510
    BossOmenDust1 = 1012501
    BossOmenDust2 = 1012502
    BossOmenDust3 = 1012503
    BossOmenDust4 = 1012504
    BossOmenDust5 = 1012505
    BossOmenDust6 = 1012506
    BossOmenSoundEffect = 1012520
    CrystalLizardNest = 1012060
    GateClosingHollowNest = 1012201
    HavelCombatArea = 1012799
    HellkiteForcedTurningBridgeDirection = 1012710
    HellkiteForcedTurningTowerDirection = 1012711
    HellkiteMovementTest1 = 1012720
    HellkiteMovementTest2 = 1012721
    HellkiteMovementTest3 = 1012722
    HellkiteMovementTest4 = 1012723
    HellkiteMovementTest5 = 1012724
    HellkiteMovementTest6 = 1012725
    HellkiteMovementTest7 = 1012726
    HellkiteMovementTest8 = 1012727
    HellkiteMovementTest9 = 1012728
    HellkiteMovementTest10 = 1012729
    HellkiteMovementTest11 = 1012730
    HellkiteMovementTest12 = 1012731
    HellkiteMovementTest13 = 1012732
    HellkiteMovementTest14 = 1012733
    HellkiteMovementTest15 = 1012734
    HellkiteMovementTest16 = 1012735
    HellkiteMovementTest17 = 1012736
    TaurusDemonJumpingTarget1 = 1012744
    TaurusDemonJumpingTarget2 = 1012745


class Boxes(RegionBox):
    """`RegionBox` entity IDs for MSB and EVS use."""

    # noinspection PyMethodParameters
    def _generate_next_value_(name, _, count, __):
        return RegionBox.auto_generate(count, DARK_SOULS_DSR, 1010000)

    AbsolutionReset_Andre = 1012013
    AbsolutionReset_Griggs = 1012011
    AbsolutionReset_Lautrec = 1012015
    AbsolutionReset_MaleUndeadMerchant = 1012014
    AbsolutionReset_Rhea = 1012012
    AbsolutionReset_Solaire = 1012010
    ArmoredTuskAreaAfterGate = 1012771
    ArmoredTuskAreaBeforeGate = 1012770
    ArmoredTuskPointAfterGate = 1012773
    ArmoredTuskPointBeforeGate = 1012772
    AssassinAmbush0 = 1012150
    AssassinAmbush1 = 1012151
    BellGargoylesCombatStart = 1012996
    BellGargoylesFogPrompt = 1012998
    BellGargoylesMusic = 1012990
    BellGargoylesMusicStop = 1012610
    BossSignOccurrenceArea = 1012500
    BurningBarrelTrigger = 1012101
    CapraDemonCombatStart = 1012886
    CapraDemonFogPrompt = 1012888
    CapraDemonFogRotationTarget = 1012887
    CapraDemonMusic = 1012880
    ChannelerCombatArea = 1012775
    ChannelerTargetArea = 1012776
    ChannelerWaitingArea = 1012777
    CheckpointFog1BackSide = 1012601
    CheckpointFog1FrontSide = 1012600
    CheckpointFog2BackSide = 1012603
    CheckpointFog2FrontSide = 1012602
    FleeingHollowCombatTrigger = 1012122
    FleeingHollowFleeTrigger = 1012121
    FleeingHollowNest = 1012120
    GargoyleNarrowPassageCombatArea = 1012793
    GargoyleWalkableArea1 = 1012790
    GargoyleWalkableArea2 = 1012791
    GargoyleWalkableArea3 = 1012792
    GateClosingHollowTrigger = 1012200
    HellkiteBackBC = 1012321
    HellkiteBackstepManagement1 = 1012750
    HellkiteBackstepManagement2 = 1012751
    HellkiteBesideBridge1 = 1012760
    HellkiteBesideBridge2 = 1012761
    HellkiteBesideBridge3 = 1012762
    HellkiteBesideBridge4 = 1012763
    HellkiteCanChasePlayerBridgeSide = 1012714
    HellkiteCanChasePlayerTowerSide = 1012715
    HellkiteControlAreaA = 1012330
    HellkiteControlAreaB = 1012331
    HellkiteControlAreaC = 1012332
    HellkiteControlAreaD = 1012333
    HellkiteControlAreaE_FormerDepth140 = 1012334
    HellkiteControlAreaF1 = 1012335
    HellkiteControlAreaF2 = 1012336
    HellkiteControlAreaG = 1012337
    HellkiteControlAreaH = 1012338
    HellkiteControlHomecoming = 1012340
    HellkiteEntryProhibitedBridgeSide = 1012712
    HellkiteEntryProhibitedTowerSide = 1012713
    HellkiteFrontBC = 1012311
    HellkiteJumpingAttackManagement1 = 1012752
    HellkiteJumpingAttackManagement2 = 1012753
    HellkiteMovementArea = 1012305
    HellkitePointA = 1012300
    HellkitePointA2 = 1012302
    HellkitePointB = 1012310
    HellkitePointC = 1012320
    HellkiteReactionA = 1012301
    HellkiteTakeoffBreathManagement1 = 1012716
    HellkiteTakeoffBreathManagement2 = 1012717
    HollowDoorKickSnap = 1012171
    HollowDoorKickTrigger = 1012170
    InvaderSpawn000 = 1014000
    InvaderSpawn010 = 1014010
    InvaderSpawn011 = 1014011
    InvaderSpawn100 = 1014100
    InvaderSpawn101 = 1014101
    InvaderSpawn200 = 1014200
    InvaderSpawn210 = 1014210
    LowerBurgShortcutLockedSide = 1012400
    LowerBurgShortcutUnlockedSide = 1012401
    NearHellkiteStairs = 1012315
    OnTaurusDemonBridge = 1012742
    OnTaurusDemonTower = 1012743
    SecondBellGargoyleNest = 1012651
    SecondBellGargoyleSpawn = 1012650
    SolaireAtSunlightAltar = 1012530
    SolaireFogRotationTarget = 1012781
    SolaireFogTrigger = 1012780
    TaurusDemonCombatStart = 1012896
    TaurusDemonFogPrompt = 1012898
    TaurusDemonFogRotationTarget = 1012897
    TaurusDemonJumpDownSnap = 1012740
    TaurusDemonJumpUpSnap = 1012741
    TaurusDemonMusic = 1012890
    TaurusDemonTrigger = 1012701
    TitaniteDemonMeleeCombatArea = 1012795
    TitaniteDemonNest = 1012798
    TitaniteDemonRangedCombatArea1 = 1012796
    TitaniteDemonRangedCombatArea2 = 1012797
    TowerArcherTrigger = 1012050
    UnusedBerenikeKnightAmbush = 1012107
    UnusedHollowDoorBreakTrigger = 1012100
    UnusedParishAmbush = 1012106
    UnusedTaurusDemonBait = 1012700
    UnusedUndeadAssassinAmbush = 1012130
    WarriorAmbushTrigger = 1012110
