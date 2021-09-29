from soulstruct.games import DARK_SOULS_DSR
from soulstruct.game_types import *


class Objects(Object):
    """`Object` entity IDs for MSB and EVS use."""

    # noinspection PyMethodParameters
    def _generate_next_value_(name, _, count, __):
        return Object.auto_generate(count, DARK_SOULS_DSR, 1300000)

    o0200_0000 = 1301960
    o0200_0001 = 1301961
    o0200_0003 = 1301962
    o3000_0000 = 1301102
    o3001_0000 = 1301103
    o3011_0000 = 1301000
    o3011_0001 = 1301002
    o3011_0002 = 1301003
    o3011_0003 = 1301001
    o3020_0000 = 1301100
    o3021_0000 = 1301101
    o3030_0000 = 1301010
    o3031_0000 = 1301011
    o3032_0000 = 1301012
    o3033_0000 = 1301013
    o3034_0000 = 1301014
    o3035_0000 = 1301015
    o3036_0000 = 1301020
    o3040_0000 = 1301140
    o3041_0000 = 1301141
    o3042_0000 = 1301142
    o3043_0000 = 1301143
    o3044_0000 = 1301144
    o3045_0000 = 1301145
    o3046_0000 = 1301146
    o3046_0001 = 1301147
    o3047_0000 = 1301148
    o3048_0000 = 1301149
    o3060_0000 = 1301104
    o3310_5000 = 1301300
    o3310_5001 = 1301301
    o3310_5002 = 1301302
    o3310_5003 = 1301303
    o3311_5000 = 1301304
    o3311_5001 = 1301305
    o3311_5002 = 1301306
    o3311_5003 = 1301307
    o3312_5000 = 1301308
    o3312_5001 = 1301309
    o3312_5002 = 1301310
    o3321_0000 = 1301200
    o3321_0001 = 1301201
    o3321_0002 = 1301202
    o3321_0003 = 1301203
    o3321_0004 = 1301204
    o3321_0005 = 1301205
    o3321_0006 = 1301206
    o3321_0007 = 1301207
    o3321_0008 = 1301208
    o3321_0009 = 1301209
    o3321_0010 = 1301210
    o3321_0011 = 1301212
    o3321_1004 = 1301213
    o3321_1005 = 1301214
    o3321_1006 = 1301215
    o3321_1007 = 1301216
    o3321_1008 = 1301217
    o3321_1009 = 1301218
    o3321_1010 = 1301219
    o3350_0000 = 1301040
    o3661_0000 = 1301050
    o3871_0000 = 1301030
    o3872_0000 = 1301031
    o3951_0000 = 1301994
    o3952_0000 = 1301700
    o3954_0000 = 1301990


class Characters(Character):
    """`Character` entity IDs for MSB and EVS use."""

    # noinspection PyMethodParameters
    def _generate_next_value_(name, _, count, __):
        return Character.auto_generate(count, DARK_SOULS_DSR, 1300000)

    c0000_0002 = 6320
    c0000_0004 = 6550
    c0000_PatchesAmbush = 7986
    c1000_0000 = 1300960
    c1000_0001 = 1300961
    c1000_0003 = 1300962
    c2300_0000 = 1300300
    c2370_TrollChanneler = 7966
    c2650_0000 = 1300100
    c2650_0001 = 1300120
    c2650_0002 = 1300140
    c2650_0003 = 1300160
    c2650_0004 = 1300180
    c2650_0005 = 1300200
    c2794_0000 = 1300400
    c2900_0000 = 1300000
    c2900_0001 = 1300001
    c2900_0002 = 1300101
    c2900_0003 = 1300102
    c2900_0004 = 1300103
    c2900_0005 = 1300104
    c2900_0006 = 1300105
    c2900_0007 = 1300106
    c2900_0008 = 1300107
    c2900_0009 = 1300108
    c2900_0010 = 1300109
    c2900_0011 = 1300110
    c2900_0012 = 1300111
    c2900_0013 = 1300112
    c2900_0014 = 1300113
    c2900_0015 = 1300114
    c2900_0016 = 1300161
    c2900_0017 = 1300162
    c2900_0018 = 1300163
    c2900_0019 = 1300164
    c2900_0020 = 1300020
    c2900_0021 = 1300126
    c2900_0022 = 1300121
    c2900_0023 = 1300122
    c2900_0024 = 1300123
    c2900_0025 = 1300124
    c2900_0026 = 1300125
    c2900_0027 = 1300141
    c2900_0028 = 1300142
    c2900_0029 = 1300143
    c2900_0030 = 1300144
    c2900_0031 = 1300145
    c2900_0032 = 1300146
    c2900_0033 = 1300147
    c2900_0034 = 1300900
    c2900_0035 = 1300201
    c2900_0036 = 1300202
    c2900_0037 = 1300203
    c2900_0038 = 1300204
    c2900_0039 = 1300205
    c2900_0040 = 1300901
    c2900_0041 = 1300902
    c2900_0042 = 1300206
    c2900_0043 = 1300207
    c2900_0044 = 1300127
    c2900_0045 = 1300184
    c2900_0046 = 1300185
    c2900_0047 = 1300183
    c2900_0048 = 1300181
    c2900_0049 = 1300182
    c2900_0052 = 1300165
    c2900_0053 = 1300166
    c2900_0054 = 1300903
    c2900_0055 = 1300904
    c2900_0056 = 1300905
    c2900_0057 = 1300906
    c2900_0058 = 1300907
    c2910_0001 = 1300050
    c2920_0000 = 6200
    c2930_0007 = 1300908
    c2930_0008 = 1300909
    c2930_0009 = 1300910
    c3300_0000 = 1300500
    c3300_0001 = 1300501
    c3320_0000 = 1300800
    c3320_0001 = 1300801
    c3320_0002 = 1300802
    c3320_0003 = 1300803
    c3320_0004 = 1300804
    c3320_0005 = 1300805
    c3320_0006 = 1300806
    c3320_0007 = 1300807
    c3320_0008 = 1300808
    c3320_0009 = 1300809
    c3320_0010 = 1300810
    c3320_0011 = 1300811
    c3320_0012 = 1300812
    c3320_0013 = 1300813
    c3320_0014 = 1300814
    c3490_0001 = 1303900
    c3490_0002 = 1303910
    c3491_0000 = 1303902
    c3491_0001 = 1303901
    c3491_0002 = 1303911
    c3491_0003 = 1303912
    c3501_0006 = 1300350
    c3501_0007 = 1300351
    c3501_0008 = 1300352
    c3501_0009 = 1300353
    c3501_0010 = 1300354
    c3501_0011 = 1300355
    c3501_0012 = 1300356
    c3501_0013 = 1300357
    c3501_0014 = 1300358
    c3501_0015 = 1300359
    c3501_0016 = 1300360
    c3501_0019 = 1300363


class PlayerStarts(PlayerStart):
    """`PlayerStart` entity IDs for MSB and EVS use."""

    # noinspection PyMethodParameters
    def _generate_next_value_(name, _, count, __):
        return PlayerStart.auto_generate(count, DARK_SOULS_DSR, 1300000)

    c0000_0001 = 1300999
    c0000_0003 = 1300982


class Sounds(SoundEvent):
    """`SoundEvent` entity IDs for MSB and EVS use."""

    # noinspection PyMethodParameters
    def _generate_next_value_(name, _, count, __):
        return SoundEvent.auto_generate(count, DARK_SOULS_DSR, 1300000)

    PinwheelMusic = 1303800


class VFX(VFXEvent):
    """`VFXEvent` entity IDs for MSB and EVS use."""

    # noinspection PyMethodParameters
    def _generate_next_value_(name, _, count, __):
        return VFXEvent.auto_generate(count, DARK_SOULS_DSR, 1300000)

    CheckpointFog1 = 1301701
    MultiplayerFog1 = 1301995
    PinwheelEntranceFog = 1301991


class SpawnPoints(SpawnPointEvent):
    """`SpawnPointEvent` entity IDs for MSB and EVS use."""

    # noinspection PyMethodParameters
    def _generate_next_value_(name, _, count, __):
        return SpawnPointEvent.auto_generate(count, DARK_SOULS_DSR, 1300000)

    SpawnPoint0 = 1302960
    SpawnPoint1 = 1302961
    SpawnPoint2 = 1302962
    SpawnPointAtBoss = 1302950


class Navigation(NavigationEvent):
    """`NavigationEvent` entity IDs for MSB and EVS use."""

    # noinspection PyMethodParameters
    def _generate_next_value_(name, _, count, __):
        return NavigationEvent.auto_generate(count, DARK_SOULS_DSR, 1300000)

    InvaderSpawn00 = 1304000
    Navmesh_BridgeA = 1304002
    Navmesh_BridgeB = 1304003
    Navmesh_MiddleGate = 1304001


class Points(RegionPoint):
    """`RegionPoint` entity IDs for MSB and EVS use."""

    # noinspection PyMethodParameters
    def _generate_next_value_(name, _, count, __):
        return RegionPoint.auto_generate(count, DARK_SOULS_DSR, 1300000)

    LeeroySummonSign = 1302050


class Cylinders(RegionCylinder):
    """`RegionCylinder` entity IDs for MSB and EVS use."""

    # noinspection PyMethodParameters
    def _generate_next_value_(name, _, count, __):
        return RegionCylinder.auto_generate(count, DARK_SOULS_DSR, 1300000)

    FloorBreakTriggerA = 1302100
    FloorBreakTriggerB = 1302101
    FloorBreakTriggerC = 1302102
    FloorBreakTriggerD = 1302103
    FloorBreakTriggerE = 1302104
    FloorBreakTriggerF = 1302105
    NecromancerNest1 = 1302201
    NecromancerNest2 = 1302202
    NecromancerNest3 = 1302203
    NecromancerNest4 = 1302204
    NecromancerNest5 = 1302205


class Boxes(RegionBox):
    """`RegionBox` entity IDs for MSB and EVS use."""

    # noinspection PyMethodParameters
    def _generate_next_value_(name, _, count, __):
        return RegionBox.auto_generate(count, DARK_SOULS_DSR, 1300000)

    CeilingBreakTrigger = 1302020
    CheckpoingFog1BackSide = 1302651
    CheckpointFog1FrontSide = 1302650
    CoffinArrivalPoint = 1302010
    CoffinMonitor = 1302700
    InvaderSpawn00 = 1304000
    InvaderSpawn10 = 1304010
    InvaderSpawn11 = 1304011
    LeeroyActivityArea = 1302995
    LeeroySummonNest = 1302051
    Navmesh_BridgeA = 1303001
    Navmesh_BridgeB = 1303002
    PatchesBridgeSwitchTrigger1 = 1302001
    PatchesBridgeSwitchTrigger2 = 1302000
    PinwheelCutsceneTrigger = 1302999
    PinwheelFogPrompt = 1302998
    PinwheelFogRotationTarget = 1302997
    PinwheelLogic = 1302500
    PinwheelMusic = 1302990
    PinwheelNotify = 1302996
    PinwheelWarpPoint00 = 1302600
    PinwheelWarpPoint01 = 1302601
    PinwheelWarpPoint02 = 1302602
    PinwheelWarpPoint03 = 1302603
    PinwheelWarpPoint04 = 1302604
    PinwheelWarpPoint05 = 1302605
    PinwheelWarpPoint06 = 1302606
    PinwheelWarpPoint07 = 1302607
    PinwheelWarpPoint08 = 1302608
    PinwheelWarpPoint09 = 1302609
    PinwheelWarpPoint10 = 1302610
    PinwheelWarpPoint11 = 1302611
    PinwheelWarpPoint12 = 1302612
    TitaniteDemonCanAttack = 1302750
    TitaniteDemonCanJump = 1302751
    TitaniteDemonRangedAttack = 1302752
    TitaniteDemonRetreat = 1302753
    VamosCutsceneTrigger = 1302030
