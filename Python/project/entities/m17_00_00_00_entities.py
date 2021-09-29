from soulstruct.games import DARK_SOULS_DSR
from soulstruct.game_types import *


class Objects(Object):
    """`Object` entity IDs for MSB and EVS use."""

    # noinspection PyMethodParameters
    def _generate_next_value_(name, _, count, __):
        return Object.auto_generate(count, DARK_SOULS_DSR, 1700000)

    o0101_0000 = 1701900
    o0101_0001 = 1701901
    o0101_0002 = 1701902
    o0101_0003 = 1701903
    o0101_0004 = 1701904
    o0101_0005 = 1701905
    o0101_0006 = 1701906
    o0101_0007 = 1701907
    o0110_0001 = 1701651
    o0110_0002 = 1701652
    o0110_0003 = 1701653
    o0110_0004 = 1701654
    o0110_0006 = 1701656
    o0110_0008 = 1701658
    o0110_0009 = 1701659
    o0110_0010 = 1701660
    o0110_0013 = 1701663
    o0110_0014 = 1701664
    o0110_0015 = 1701665
    o0110_0016 = 1701666
    o0200_0000 = 1701960
    o0200_0001 = 1701961
    o0200_0002 = 1701950
    o0200_0003 = 1701962
    o7199 = 1701109
    o7200_00 = 1701110
    o7201_00 = 1701121
    o7201_01 = 1701101
    o7201_03 = 1701131
    o7201_04 = 1701111
    o7201_05 = 1701102
    o7201_06 = 1701132
    o7202 = 1701401
    o7230_00 = 1701200
    o7230_01 = 1701210
    o7231 = 1701201
    o7231_01 = 1701211
    o7240 = 1701100
    o7241 = 1701130
    o7250 = 1701120
    o7251 = 1701125
    o7300 = 1701140
    o7301 = 1701141
    o7302 = 1701142
    o7303 = 1701143
    o7400 = 1701300
    o7401_00 = 1701500
    o7401_01 = 1701501
    o7401_02 = 1701502
    o7401_03 = 1701503
    o7401_04 = 1701504
    o7401_05 = 1701505
    o7401_06 = 1701506
    o7402 = 1701410
    o7404 = 1701400
    o7500 = 1701800
    o7510 = 1701050
    o7900_0000 = 1701990
    o7901_0000 = 1701890
    o7902_0000 = 1701994
    o7906_0000 = 1701706
    o7907_0000 = 1701710
    o7908_0000 = 1701996


class Characters(Character):
    """`Character` entity IDs for MSB and EVS use."""

    # noinspection PyMethodParameters
    def _generate_next_value_(name, _, count, __):
        return Character.auto_generate(count, DARK_SOULS_DSR, 1700000)

    c0000_0002 = 6032
    c0000_0003 = 6073
    c0000_0004 = 6291
    c0000_0005 = 6610
    c0000_0006 = 6033
    c0000_PatchesAmbush = 7994
    c1000_0000 = 1700960
    c1000_0001 = 1700961
    c1000_0002 = 1700950
    c1000_0003 = 1700962
    c2370_0000 = 1700300
    c2370_0001 = 1700301
    c2370_0002 = 1700900
    c2370_0003 = 1700901
    c2370_0004 = 1700902
    c2370_0005 = 1700903
    c2370_0006 = 1700302
    c2370_TrollChanneler = 7974
    c2690_0000 = 1700100
    c2690_0014 = 1700103
    c2690_0015 = 1700102
    c2700_0000 = 1700101
    c2710_0010 = 1700510
    c2710_0015 = 1700904
    c2710_0016 = 1700905
    c2710_0017 = 1700906
    c2710_0018 = 1700907
    c2711_0000 = 1700500
    c2711_0001 = 1700501
    c2711_0002 = 1700502
    c2780_0000 = 1700400
    c2780_0001 = 1700401
    c2800_0000 = 1700200
    c3230_0000 = 1700350
    c3230_0001 = 1700351
    c3230_0002 = 1700352
    c3250_0000 = 1700250
    c3250_0001 = 1700251
    c3250_0002 = 1700252
    c3250_0003 = 1700253
    c3250_0004 = 1700254
    c3250_0005 = 1700255
    c3300_0000 = 1700450
    c3300_0001 = 1700451
    c3300_0002 = 1700452
    c3300_0003 = 1700453
    c3330_0000 = 1700110
    c3330_0001 = 1700111
    c3330_0002 = 1700112
    c3330_0003 = 1700150
    c3330_0004 = 1700151
    c3330_0005 = 1700120
    c3330_0006 = 1700116
    c3330_0007 = 1700117
    c3330_0008 = 1700118
    c3330_0009 = 1700113
    c3330_0010 = 1700114
    c3330_0012 = 1700115
    c3330_0020 = 1700908
    c3330_0021 = 1700909
    c3461_0000 = 1700190
    c3461_0001 = 1700191
    c3490_0001 = 1703900
    c3490_0002 = 1703910
    c3491_0000 = 1703902
    c3491_0001 = 1703901
    c3491_0002 = 1703911
    c3491_0003 = 1703912
    c5290_0000 = 1700700
    c5290_0001 = 1700800
    c5291_0000 = 1700801


class PlayerStarts(PlayerStart):
    """`PlayerStart` entity IDs for MSB and EVS use."""

    # noinspection PyMethodParameters
    def _generate_next_value_(name, _, count, __):
        return PlayerStart.auto_generate(count, DARK_SOULS_DSR, 1700000)

    c0000_0001 = 1700999


class Collisions(Collision):
    """`Collision` entity IDs for MSB and EVS use."""

    # noinspection PyMethodParameters
    def _generate_next_value_(name, _, count, __):
        return Collision.auto_generate(count, DARK_SOULS_DSR, 1700000)

    h0041B0 = 1703300
    h0042B0 = 1703220
    h0043B0 = 1703221
    h0124B0 = 1703200
    h0124B0_0000 = 1703201
    h0125B0 = 1703210
    h0125B0_0000 = 1703211
    h7500B0 = 1703100
    h7501B0 = 1703101


class Sounds(SoundEvent):
    """`SoundEvent` entity IDs for MSB and EVS use."""

    # noinspection PyMethodParameters
    def _generate_next_value_(name, _, count, __):
        return SoundEvent.auto_generate(count, DARK_SOULS_DSR, 1700000)

    SeathCaveMusic = 1703800
    SeathTowerMusic = 1703801
    SirenSound = 1703500


class VFX(VFXEvent):
    """`VFXEvent` entity IDs for MSB and EVS use."""

    # noinspection PyMethodParameters
    def _generate_next_value_(name, _, count, __):
        return VFXEvent.auto_generate(count, DARK_SOULS_DSR, 1700000)

    CheckpointFog2 = 1701707
    GoldenFog = 1701711
    MultiplayerFog1 = 1701995
    MultiplayerFog2 = 1701997
    SeathCaveEntranceFog = 1701991
    SeathTowerEntranceFog = 1701891


class SpawnPoints(SpawnPointEvent):
    """`SpawnPointEvent` entity IDs for MSB and EVS use."""

    # noinspection PyMethodParameters
    def _generate_next_value_(name, _, count, __):
        return SpawnPointEvent.auto_generate(count, DARK_SOULS_DSR, 1700000)

    SpawnPoint0 = 1702960
    SpawnPoint1 = 1702961
    SpawnPoint2 = 1702962
    SpawnPointAtBoss = 1702950
    SpawnPointInPrison = 1702900


class Navigation(NavigationEvent):
    """`NavigationEvent` entity IDs for MSB and EVS use."""

    # noinspection PyMethodParameters
    def _generate_next_value_(name, _, count, __):
        return NavigationEvent.auto_generate(count, DARK_SOULS_DSR, 1700000)

    Navmesh_AfterRotatingStairs0 = 1703012
    Navmesh_AfterRotatingStairs1 = 1703013
    Navmesh_BeforeRotatingStairs0 = 1703010
    Navmesh_BeforeRotatingStairs1 = 1703011
    Navmesh_PrisonGate00 = 1703000
    Navmesh_PrisonGate01 = 1703001
    Navmesh_PrisonGate02 = 1703002
    Navmesh_PrisonGate03 = 1703003
    Navmesh_PrisonGate04 = 1703004
    Navmesh_PrisonGate05 = 1703005
    Navmesh_PrisonGate06 = 1703006


class Cylinders(RegionCylinder):
    """`RegionCylinder` entity IDs for MSB and EVS use."""

    # noinspection PyMethodParameters
    def _generate_next_value_(name, _, count, __):
        return RegionCylinder.auto_generate(count, DARK_SOULS_DSR, 1700000)

    PisacaNestA = 1702770
    PisacaNestB = 1702771
    PisacaNestC = 1702772
    PisacaRetreatA = 1702760
    PisacaRetreatB = 1702761
    PisacaRetreatC = 1702762
    PishacaAlertArea = 1702100
    SerpentNest1 = 1702150
    SerpentNest2 = 1702151


class Boxes(RegionBox):
    """`RegionBox` entity IDs for MSB and EVS use."""

    # noinspection PyMethodParameters
    def _generate_next_value_(name, _, count, __):
        return RegionBox.auto_generate(count, DARK_SOULS_DSR, 1700000)

    ArmoredTuskRetreat0 = 1702750
    ArmoredTuskRetreat1 = 1702751
    ArmoredTuskRetreat2 = 1702752
    AtGoldenFog = 1702610
    ButterflyAttackTarget = 1702700
    ChannelerWarpPoint_00_00 = 1702301
    ChannelerWarpPoint_00_01 = 1702302
    ChannelerWarpPoint_00_02 = 1702303
    ChannelerWarpPoint_00_03 = 1702304
    ChannelerWarpPoint_00_04 = 1702305
    ChannelerWarpPoint_00_05 = 1702306
    ChannelerWarpPoint_01_00 = 1702311
    ChannelerWarpPoint_01_01 = 1702312
    ChannelerWarpPoint_01_02 = 1702313
    ChannelerWarpPoint_01_03 = 1702314
    ChannelerWarpPoint_02_00 = 1702321
    ChannelerWarpPoint_02_01 = 1702322
    CheckpointFog2BackSide = 1702607
    CheckpointFog2FrontSide = 1702606
    CrystalHollowAttack0 = 1702200
    CrystalHollowAttack1 = 1702201
    ElevatorEnemyWallToggle1 = 1702780
    ElevatorEnemyWallToggle2 = 1702781
    InvaderSpawn00 = 1704000
    InvaderSpawn01 = 1704001
    InvaderSpawn10 = 1704010
    InvaderSpawn11 = 1704011
    LoganHollowPoint = 1702502
    LoganInLibraryPoint = 1702501
    LoganPrison = 1702500
    MimicNest0 = 1702010
    MimicNest1 = 1702011
    NoSignZone = 1704050
    PatrolGroup1_00 = 1702710
    PatrolGroup1_01 = 1702711
    PatrolGroup1_02 = 1702712
    PatrolGroup2_00 = 1702720
    PatrolGroup2_01 = 1702721
    PatrolGroup2_02 = 1702722
    PatrolGroup3_00 = 1702730
    PatrolGroup3_01 = 1702731
    PatrolGroup3_02 = 1702732
    PatrolGroup3_03 = 1702733
    PatrolGroup3_04 = 1702734
    PatrolGroup3_05 = 1702735
    PatrolGroup3_06 = 1702736
    PatrolGroup4_00 = 1702740
    PatrolGroup4_01 = 1702741
    PatrolGroup4_02 = 1702742
    PatrolGroup4_03 = 1702743
    PatrolGroup4_04 = 1702744
    PatrolGroup4_09 = 1702749
    PisacaNestCombatArea = 1702101
    PisacaScaredPoint00 = 1702745
    PisacaScaredPoint01 = 1702746
    PisacaScaredPoint02 = 1702747
    PisacaScaredPoint03 = 1702748
    PlayerCellEscapeTrigger = 1702400
    PlayerJumpingEscapeTrigger = 1702401
    PlayerPointAfterSeathCutscene = 1702801
    PrisonCell1 = 1702402
    PrisonCell2 = 1702403
    PrisonDoorReplaceMediumTrigger = 1702410
    PrisonDoorReplaceOutsideTrigger = 1702420
    SeathCaveCombatStart = 1702996
    SeathCaveFogPrompt = 1702998
    SeathCaveFogRotationTarget = 1702997
    SeathCaveMusic = 1702990
    SeathCutsceneTrigger = 1702999
    SeathPointAfterSeathCutscene = 1702800
    SeathTowerCombatStart = 1702896
    SeathTowerFogExitPrompt = 1702895
    SeathTowerFogExitRotationTarget = 1702894
    SeathTowerFogPrompt = 1702898
    SeathTowerFogRotationTarget = 1702897
    SeathTowerMusic = 1702890
