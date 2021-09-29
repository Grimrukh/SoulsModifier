from soulstruct.games import DARK_SOULS_DSR
from soulstruct.game_types import *


class MapPieces(MapPiece):
    """`MapPiece` entity IDs for MSB and EVS use."""

    # noinspection PyMethodParameters
    def _generate_next_value_(name, _, count, __):
        return MapPiece.auto_generate(count, DARK_SOULS_DSR, 1100000)

    m2230B0 = 1103100


class Objects(Object):
    """`Object` entity IDs for MSB and EVS use."""

    # noinspection PyMethodParameters
    def _generate_next_value_(name, _, count, __):
        return Object.auto_generate(count, DARK_SOULS_DSR, 1100000)

    o0110_0000 = 1101650
    o0150_00 = 1101011
    o0150_01 = 1101012
    o0150_02 = 1101013
    o0150_03 = 1101014
    o0150_04 = 1101015
    o0150_05 = 1101016
    o0150_06 = 1101017
    o0150_07 = 1101018
    o0150_08 = 1101019
    o0150_09 = 1101020
    o0150_13 = 1101024
    o0150_14 = 1101025
    o0150_18 = 1101029
    o0150_19 = 1101030
    o0150_24 = 1101035
    o0150_27 = 1101038
    o0150_28 = 1101300
    o0150_29 = 1101301
    o0150_30 = 1101302
    o0150_31 = 1101303
    o0150_32 = 1101304
    o0150_33 = 1101305
    o0150_34 = 1101306
    o0150_35 = 1101307
    o0150_36 = 1101308
    o0150_37 = 1101309
    o0150_38 = 1101310
    o0150_39 = 1101311
    o0150_40 = 1101039
    o0150_41 = 1101040
    o0150_42 = 1101041
    o0150_43 = 1101042
    o0150_44 = 1101043
    o0150_45 = 1101044
    o0200_0000 = 1101960
    o0500_0015 = 1101610
    o0500_0100 = 1101600
    o0500_0101 = 1101601
    o1500_0000 = 1101130
    o1510_0000 = 1101140
    o1511_0000 = 1101141
    o1512_0000 = 1101142
    o1513_0000 = 1101143
    o1520_0000 = 1101170
    o1540_0000 = 1101160
    o1550_0000 = 1101150
    o1560_0000 = 1101180
    o1560_0001 = 1101181
    o1570_0000 = 1101120
    o1571_0000 = 1101121
    o1580_0000 = 1101250
    o1600_0000 = 1101990
    o1601_0000 = 1101992
    o1603_0000 = 1101702
    o1604_0000 = 1101750
    o1610_0000 = 1101210
    o1610_0001 = 1101211


class Characters(Character):
    """`Character` entity IDs for MSB and EVS use."""

    # noinspection PyMethodParameters
    def _generate_next_value_(name, _, count, __):
        return Character.auto_generate(count, DARK_SOULS_DSR, 1100000)

    c0000_0003 = 6312
    c0000_0004 = 6422
    c0000_0005 = 6570
    c0000_PatchesAmbush = 7983
    c1000_0000 = 1100960
    c2310_0000 = 1100300
    c2310_0001 = 1100301
    c2310_0002 = 1100302
    c2310_0003 = 1100303
    c2370_TrollChanneler = 7963
    c2500_0011 = 1100100
    c2500_0012 = 1100101
    c2500_0013 = 1100102
    c2500_0014 = 1100104
    c2500_0015 = 1100105
    c2500_0016 = 1100130
    c2500_0017 = 1100132
    c2500_0018 = 1100135
    c2500_0019 = 1100136
    c2500_0020 = 1100137
    c2500_0021 = 1100138
    c2500_0022 = 1100400
    c2500_0023 = 1100401
    c2500_0024 = 1100402
    c2500_0025 = 1100403
    c2500_0026 = 1100404
    c2570_0000 = 1100180
    c2730_0000 = 1100160
    c2731_0000 = 1100161
    c2830_0000 = 1100200
    c2830_0001 = 1100201
    c2830_0002 = 1100202
    c2830_0003 = 1100203
    c2830_0004 = 1100204
    c2830_0005 = 1100205
    c2830_0006 = 1100206
    c2830_0007 = 1100207
    c2830_0008 = 1100208
    c2830_0009 = 1100209
    c2830_0010 = 1100210
    c2830_0011 = 1100211
    c2830_0012 = 1100212
    c2830_0013 = 1100213
    c2840_0011 = 1100900
    c2840_0012 = 1100901
    c2840_0013 = 1100902
    c2840_0014 = 1100903
    c2840_0015 = 1100904
    c2840_0016 = 1100905
    c2840_0017 = 1100906
    c2930_0009 = 1100907
    c2930_0010 = 1100908
    c2930_0011 = 1100909
    c2930_0012 = 1100910
    c2930_0013 = 1100911
    c3420_0000 = 1100170
    c3421_0000 = 1100171
    c3422_0000 = 1100172
    c3490_0001 = 1103900
    c3490_0002 = 1103910
    c3491_0000 = 1103902
    c3491_0001 = 1103901
    c3491_0002 = 1103911
    c3491_0003 = 1103912


class PlayerStarts(PlayerStart):
    """`PlayerStart` entity IDs for MSB and EVS use."""

    # noinspection PyMethodParameters
    def _generate_next_value_(name, _, count, __):
        return PlayerStart.auto_generate(count, DARK_SOULS_DSR, 1100000)

    c0000_0001 = 1100999
    c0000_0002 = 1102980


class Collisions(Collision):
    """`Collision` entity IDs for MSB and EVS use."""

    # noinspection PyMethodParameters
    def _generate_next_value_(name, _, count, __):
        return Collision.auto_generate(count, DARK_SOULS_DSR, 1100000)

    h0042B0 = 1103000
    h0148B0_0000 = 1103101


class Sounds(SoundEvent):
    """`SoundEvent` entity IDs for MSB and EVS use."""

    # noinspection PyMethodParameters
    def _generate_next_value_(name, _, count, __):
        return SoundEvent.auto_generate(count, DARK_SOULS_DSR, 1100000)

    CrossbreedPriscillaMusic = 1103800


class VFX(VFXEvent):
    """`VFXEvent` entity IDs for MSB and EVS use."""

    # noinspection PyMethodParameters
    def _generate_next_value_(name, _, count, __):
        return VFXEvent.auto_generate(count, DARK_SOULS_DSR, 1100000)

    BossEntranceFog = 1101991
    BossExitFog = 1101993
    CheckpointFog2 = 1101703
    FireVFX05 = 1103000
    FireVFX06 = 1103001
    MultiplayerFog1 = 1101751


class SpawnPoints(SpawnPointEvent):
    """`SpawnPointEvent` entity IDs for MSB and EVS use."""

    # noinspection PyMethodParameters
    def _generate_next_value_(name, _, count, __):
        return SpawnPointEvent.auto_generate(count, DARK_SOULS_DSR, 1100000)

    SpawnPoint0 = 1102960
    SpawnPointArrival = 1102511
    SpawnPointAtBoss = 1102950


class Navigation(NavigationEvent):
    """`NavigationEvent` entity IDs for MSB and EVS use."""

    # noinspection PyMethodParameters
    def _generate_next_value_(name, _, count, __):
        return NavigationEvent.auto_generate(count, DARK_SOULS_DSR, 1100000)

    CrowDemonActivityPointB = 1102040
    Navmesh_Door = 1102042
    Navmesh_EventNavmesh02 = 1102041


class Points(RegionPoint):
    """`RegionPoint` entity IDs for MSB and EVS use."""

    # noinspection PyMethodParameters
    def _generate_next_value_(name, _, count, __):
        return RegionPoint.auto_generate(count, DARK_SOULS_DSR, 1100000)

    JeremiahInvaderSpawn = 1102010
    UnusedRecoveryFountainSoundEffect = 1102980


class Spheres(RegionSphere):
    """`RegionSphere` entity IDs for MSB and EVS use."""

    # noinspection PyMethodParameters
    def _generate_next_value_(name, _, count, __):
        return RegionSphere.auto_generate(count, DARK_SOULS_DSR, 1100000)

    JeremiahInvaderTrigger = 1102011
    PriscillaWarpPoint0 = 1102810
    PriscillaWarpPoint1 = 1102811
    PriscillaWarpPoint2 = 1102812
    PriscillaWarpPoint3 = 1102813
    PriscillaWarpPoint4 = 1102814
    PriscillaWarpPoint5 = 1102815
    PriscillaWarpPoint6 = 1102816
    PriscillaWarpPoint7 = 1102817
    PriscillaWarpPoint8 = 1102818
    PriscillaWarpPoint9 = 1102819
    UnusedShivaInvaderTrigger = 1102800


class Cylinders(RegionCylinder):
    """`RegionCylinder` entity IDs for MSB and EVS use."""

    # noinspection PyMethodParameters
    def _generate_next_value_(name, _, count, __):
        return RegionCylinder.auto_generate(count, DARK_SOULS_DSR, 1100000)

    BerenikeKnightAmbushNest = 1102201
    PriscillaFogRotationTarget = 1102997
    ShortcutDoorPlayerSnap = 1102090
    UndeadDragonInitialPosition = 1102110
    UndeadDragonNest = 1102071
    UnusedShortcutDoorPlayerSnap = 1102091
    UnusedWarpPoint = 1102501
    Unused_PriscillaFogExitRotationTarget = 1102994


class Boxes(RegionBox):
    """`RegionBox` entity IDs for MSB and EVS use."""

    # noinspection PyMethodParameters
    def _generate_next_value_(name, _, count, __):
        return RegionBox.auto_generate(count, DARK_SOULS_DSR, 1100000)

    ArrivalPointFromAnorLondo = 1102510
    BerenikeKnightAmbushTrigger = 1102200
    BossWaiting2 = 1102751
    BossWaiting3 = 1102752
    CheckpointFog2BackSide = 1102603
    CheckpointFog2FrontSide = 1102602
    CrosDemonActivityPointA = 1102020
    CrosDemonActivityPointA2 = 1102030
    CrosDemonActivityPointB2 = 1102050
    CrossbreedPriscillaMusic = 1102100
    CrowDemonActivityPointB = 1102040
    CrowDemonPointA = 1102710
    CrowDemonPointA2 = 1102711
    CrowDemonPointB = 1102712
    CrowDemonPointB2 = 1102713
    CrowDemonPoint_CorrectionAB = 1102715
    CrowDemonPoint_CorrectionBA = 1102714
    CrowDemonTreasureAmbushTrigger = 1202021
    CrowsFlockArea = 1102000
    DustGenerationPosition1F = 1102801
    DustGenerationPosition2F = 1102802
    DustGenerationPosition3F = 1102803
    ExitCutsceneTrigger = 1102500
    HangingHollow4Trigger = 1102006
    HangingHollow5Trigger = 1102001
    HangingHollow6Trigger = 1102007
    HangingHollowGroupTrigger = 1102202
    HollowPhalanxComesApart = 1102300
    HollowPhalanxControlArea1 = 1102400
    HollowPhalanxControlArea2 = 1102401
    HollowPhalanxControlArea3 = 1102402
    HollowPhalanxControlArea4 = 1102403
    HollowPhalanxControlArea5 = 1102404
    InvaderSpawn00 = 1104000
    InvaderSpawn01 = 1104001
    InvaderSpawn10 = 1104010
    InvaderSpawn11 = 1104011
    Phalanx00 = 1102830
    Phalanx01 = 1102831
    Phalanx02 = 1102832
    Phalanx03 = 1102833
    Phalanx04 = 1102834
    Phalanx05 = 1102835
    Phalanx06 = 1102836
    Phalanx07 = 1102837
    Phalanx08 = 1102838
    Phalanx09 = 1102839
    Phalanx10 = 1102840
    Phalanx11 = 1102841
    Phalanx12 = 1102842
    Phalanx13 = 1102843
    PriscillaCombatStart = 1102996
    PriscillaFogPrompt = 1102998
    UndeadDragonAcidBreathFront = 1102124
    UndeadDragonAcidBreathLeft1 = 1102126
    UndeadDragonAcidBreathLeft2 = 1102128
    UndeadDragonAcidBreathRight1 = 1102125
    UndeadDragonAcidBreathRight2 = 1102127
    UndeadDragonBite = 1102120
    UndeadDragonSnoringSoundEffect = 1102080
    UndeadDragonSwipeLeft = 1102122
    UndeadDragonSwipeRight1 = 1102121
    UndeadDragonSwipeRight2 = 1102123
    UndeadDragonWakeTrigger = 1102070
    UnusedBossFloorArea1 = 1102760
    UnusedBossFloorArea2 = 1102761
    UnusedBossFloorArea3 = 1102762
    UnusedBossFloorArea4 = 1102763
    UnusedBossFloorArea5 = 1102764
    UnusedBossStaircaseArea1 = 1102700
    UnusedBossStaircaseArea2 = 1102701
    UnusedBossStaircaseArea3 = 1102702
    UnusedBossStaircaseArea4 = 1102703
    UnusedBossStaircaseArea5 = 1102704
    UnusedBossStaircaseArea6 = 1102705
    UnusedBossStaircaseArea7 = 1102706
    UnusedBossStaircaseArea8 = 1102707
    UnusedBossStaircaseArea9 = 1102708
    UnusedBossWaiting = 1102750
    Unused_PriscillaFogExitPrompt = 1102995
