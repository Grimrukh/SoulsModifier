from soulstruct.games import DARK_SOULS_DSR
from soulstruct.game_types import *


class Objects(Object):
    """`Object` entity IDs for MSB and EVS use."""

    # noinspection PyMethodParameters
    def _generate_next_value_(name, _, count, __):
        return Object.auto_generate(count, DARK_SOULS_DSR, 1200000)

    o0110_0000 = 1201650
    o0110_0001 = 1201651
    o0200_0000 = 1201961
    o0504_0000 = 1201600
    o2110 = 1201000
    o2111 = 1201010
    o2120 = 1201300
    o2300 = 1201200
    o2400 = 1201140
    o2401 = 1201141
    o2900_0000 = 1201990
    o2901_0000 = 1201994
    o2902_0000 = 1201996
    o2903_0000 = 1201998
    o2904_0000 = 1201890
    o2905_0000 = 1201892
    o2906_0000 = 1201700
    o2907_0000 = 1201988
    o2908_0000 = 1201986


class Characters(Character):
    """`Character` entity IDs for MSB and EVS use."""

    # noinspection PyMethodParameters
    def _generate_next_value_(name, _, count, __):
        return Character.auto_generate(count, DARK_SOULS_DSR, 1200000)

    c0000_0002 = 6310
    c0000_0003 = 1200300
    c0000_0004 = 1200301
    c0000_0005 = 1200302
    c0000_0006 = 1200303
    c0000_0007 = 1200304
    c0000_0008 = 1200305
    c0000_0009 = 1200306
    c0000_0012 = 6050
    c0000_0013 = 6420
    c0000_0014 = 6521
    c0000_0015 = 6051
    c0000_PatchesAmbush = 7984
    c1000_0000 = 1200961
    c2270_0000 = 1200703
    c2270_0001 = 1200704
    c2270_0002 = 1200908
    c2270_0003 = 1200909
    c2280_0000 = 1200705
    c2280_0001 = 1200706
    c2280_0002 = 1200707
    c2280_0003 = 1200708
    c2280_0004 = 1200709
    c2280_0005 = 1200710
    c2280_0006 = 1200711
    c2280_0007 = 1200712
    c2280_0008 = 1200904
    c2280_0009 = 1200905
    c2280_0010 = 1200906
    c2280_0011 = 1200907
    c2330_0003 = 1200100
    c2330_0004 = 1200101
    c2330_0005 = 1200102
    c2330_0006 = 1200103
    c2330_0007 = 1200104
    c2330_0008 = 1200105
    c2330_0009 = 1200106
    c2330_0010 = 1200107
    c2330_0011 = 1200108
    c2330_0019 = 1200109
    c2330_0021 = 1200110
    c2330_0023 = 1200111
    c2330_0024 = 1200112
    c2330_0025 = 1200113
    c2330_0026 = 1200090
    c2370_TrollChanneler = 7964
    c2380_0000 = 1200650
    c2380_0001 = 1200651
    c2380_0002 = 1200652
    c2380_0003 = 1200653
    c2380_0004 = 1200654
    c2380_0005 = 1200655
    c2380_0006 = 1200656
    c2380_0007 = 1200900
    c2380_0008 = 1200901
    c2380_0009 = 1200902
    c2380_0010 = 1200903
    c2711_0000 = 1200200
    c2795_0000 = 1200750
    c3230_0000 = 1200801
    c3300_0000 = 1200400
    c3350_0000 = 1200000
    c3350_0001 = 1200001
    c3370_0000 = 1200600
    c3370_0002 = 1200602
    c3410_0001 = 1200250
    c3410_0002 = 1200251
    c3410_0003 = 1200252
    c3410_0004 = 1200253
    c3490_0000 = 1203900
    c3490_0001 = 1203910
    c3490_0002 = 1203920
    c3491_0000 = 1203901
    c3491_0001 = 1203911
    c3491_0002 = 1203921
    c3491_0003 = 1203902
    c3491_0004 = 1203912
    c3491_0005 = 1203922
    c3530_0000 = 1200010
    c3531_0000 = 1200011
    c3531_0001 = 1200012
    c3531_0002 = 1200013
    c3531_0003 = 1200014
    c3531_0004 = 1200015
    c3531_0005 = 1200016
    c3531_0006 = 1200017
    c5210_0000 = 1200800
    c5360_0000 = 1200350
    c5360_0001 = 1200351
    c5360_0002 = 1200352
    c5361_0000 = 6380


class PlayerStarts(PlayerStart):
    """`PlayerStart` entity IDs for MSB and EVS use."""

    # noinspection PyMethodParameters
    def _generate_next_value_(name, _, count, __):
        return PlayerStart.auto_generate(count, DARK_SOULS_DSR, 1200000)

    c0000_0001 = 1200999


class Collisions(Collision):
    """`Collision` entity IDs for MSB and EVS use."""

    # noinspection PyMethodParameters
    def _generate_next_value_(name, _, count, __):
        return Collision.auto_generate(count, DARK_SOULS_DSR, 1200000)

    h0018B0 = 1203150
    h0040B0 = 1203500
    h0041B0 = 1203501
    h0042B0 = 1203502
    h0043B0 = 1203503
    h0044B0 = 1203504


class Sounds(SoundEvent):
    """`SoundEvent` entity IDs for MSB and EVS use."""

    # noinspection PyMethodParameters
    def _generate_next_value_(name, _, count, __):
        return SoundEvent.auto_generate(count, DARK_SOULS_DSR, 1200000)

    MoonlightButterflyMusic = 1203801
    SifMusic = 1203800


class VFX(VFXEvent):
    """`VFXEvent` entity IDs for MSB and EVS use."""

    # noinspection PyMethodParameters
    def _generate_next_value_(name, _, count, __):
        return VFXEvent.auto_generate(count, DARK_SOULS_DSR, 1200000)

    ButterflyEntranceFog = 1201891
    ButterflyExitFog = 1201893
    CheckpointFog1 = 1201701
    DuskSummonSign00 = 1203100
    DuskSummonSign01 = 1203101
    DuskSummonSign02 = 1203102
    DuskSummonSign03 = 1203103
    MultiplayerFog1 = 1201995
    MultiplayerFog2 = 1201997
    MultiplayerFog3 = 1201999
    MultiplayerFog4 = 1201989
    MultiplayerFog5 = 1201987
    OolacilePortal = 1202009
    SifEntranceFog = 1201991


class SpawnPoints(SpawnPointEvent):
    """`SpawnPointEvent` entity IDs for MSB and EVS use."""

    # noinspection PyMethodParameters
    def _generate_next_value_(name, _, count, __):
        return SpawnPointEvent.auto_generate(count, DARK_SOULS_DSR, 1200000)

    SpawnPoint1 = 1202961
    SpawnPointAtBoss = 1202950


class Points(RegionPoint):
    """`RegionPoint` entity IDs for MSB and EVS use."""

    # noinspection PyMethodParameters
    def _generate_next_value_(name, _, count, __):
        return RegionPoint.auto_generate(count, DARK_SOULS_DSR, 1200000)

    CheckpointFog1 = 1201701
    WitchBeatriceSummonSign = 1202010


class Spheres(RegionSphere):
    """`RegionSphere` entity IDs for MSB and EVS use."""

    # noinspection PyMethodParameters
    def _generate_next_value_(name, _, count, __):
        return RegionSphere.auto_generate(count, DARK_SOULS_DSR, 1200000)

    ButterflyAirJunction1 = 1202180
    ButterflyAirJunction2 = 1202181
    ButterflyAirJunction3 = 1202182
    ButterflyAirJunction4 = 1202183
    ButterflyAirJunction5 = 1202184
    ButterflyAirJunction6 = 1202185
    ButterflyAirJunction7 = 1202186
    ButterflyAirJunction8 = 1202187
    ButterflyAirJunction9 = 1202188
    ButterflyAirJunction10 = 1202189
    ButterflyBridgeJunction1 = 1202190
    ButterflyBridgeJunction2 = 1202191
    ButterflyBridgeJunction3 = 1202192
    ButterflyBridgeJunction4 = 1202193
    ButterflyBridgeJunction5 = 1202194
    ButterflyBridgeJunction6_Approx = 1202195
    ButterflyBridgeJunction7 = 1202196
    ButterflyBridgeJunction8 = 1202197
    ButterflyBridgeJunction9 = 1202198
    ButterflyBridgeJunction10 = 1202199
    DuskSummonSpawn00 = 1202000
    DuskSummonSpawn01 = 1202001
    DuskSummonSpawn02 = 1202002
    DuskSummonSpawn03 = 1202003
    SifCutsceneTrigger = 1202999


class Cylinders(RegionCylinder):
    """`RegionCylinder` entity IDs for MSB and EVS use."""

    # noinspection PyMethodParameters
    def _generate_next_value_(name, _, count, __):
        return RegionCylinder.auto_generate(count, DARK_SOULS_DSR, 1200000)

    OolacilePortalDestination = 1202502


class Boxes(RegionBox):
    """`RegionBox` entity IDs for MSB and EVS use."""

    # noinspection PyMethodParameters
    def _generate_next_value_(name, _, count, __):
        return RegionBox.auto_generate(count, DARK_SOULS_DSR, 1200000)

    AlvinaTerritory = 1202050
    BufferflyLandmark4 = 1202203
    ButterflyAttackTest = 1202700
    ButterflyFlyingArea1 = 1202220
    ButterflyFlyingArea2 = 1202221
    ButterflyFlyingArea3 = 1202222
    ButterflyFlyingArea4 = 1202223
    ButterflyFlyingArea5 = 1202224
    ButterflyFlyingArea6 = 1202225
    ButterflyFlyingArea7 = 1202226
    ButterflyFlyingArea8 = 1202227
    ButterflyFlyingArea9 = 1202228
    ButterflyFlyingArea10 = 1202229
    ButterflyLandmark1 = 1202200
    ButterflyLandmark2 = 1202201
    ButterflyLandmark3 = 1202202
    ButterflyPlayerPositionMonitor1 = 1202240
    ButterflyPlayerPositionMonitor2 = 1202241
    ButterflyPlayerPositionMonitor3 = 1202242
    ButterflyPlayerPositionMonitor4 = 1202243
    ButterflyPlayerPositionMonitor5 = 1202244
    ButterflyPlayerPositionMonitorNearWall = 1202245
    ButterflyRestArea = 1202210
    CheckpointFog1BackSide = 1202601
    CheckpointFog1FrontSide = 1202600
    CrestDoorPrompt = 1202500
    EntTrigger1 = 1202110
    EntTrigger2 = 1202111
    FrogRayTrigger = 1202113
    GreatFelineNest = 1202732
    GreatFelingCombatArea1 = 1202730
    GreatFelingCombatArea2 = 1202731
    HydraBreath1 = 1202720
    HydraBreath2 = 1202721
    HydraBreath3 = 1202722
    InvaderSpawn000 = 1204000
    InvaderSpawn001 = 1204001
    InvaderSpawn010 = 1204010
    InvaderSpawn011 = 1204011
    InvaderSpawn100 = 1204100
    InvaderSpawn101 = 1204101
    LivingTreeMovementTarget = 1202101
    LivingTreeMovementTrigger = 1202100
    MoonlightButterflyCombatStart = 1202896
    MoonlightButterflyFogPrompt = 1202898
    MoonlightButterflyFogRotationTarget = 1202894
    MoonlightButterflyMusic = 1202890
    MushroomChildEscape = 1202114
    MushroomChildMovement0 = 1202115
    MushroomChildMovement1 = 1202116
    MushroomChildMovement2 = 1202117
    MushroomChildMovement3 = 1202118
    MushroomChildMovement4 = 1202119
    MushroomChildMovement5 = 1202120
    MushroomChildMovement6 = 1202121
    MushroomChildMovement7 = 1202122
    OolacilePortalPrompt = 1202008
    PlayerPointAfterSifCutscene = 1202801
    PlayerPointAfterSifCutsceneIfRescued = 1202802
    SifCombatStart = 1202996
    SifFogPrompt = 1202998
    SifFogRotationTarget = 1202997
    SifMusic = 1202990
    SifOpenDoorPrompt = 1202501
    SifPointAfterSifCutscene = 1202800
    StoneKnightTrigger = 1202112
    TreeLizardNestAfterAmbush1 = 1202710
    TreeLizardNestAfterAmbush2 = 1202711
    TreeLizardNestAfterAmbush3 = 1202712
    WitchBeatriceActivityRange1 = 1202891
    WitchBeatriceActivityRange2 = 1202892
