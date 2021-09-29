from soulstruct.games import DARK_SOULS_DSR
from soulstruct.game_types import *


class Objects(Object):
    """`Object` entity IDs for MSB and EVS use."""

    # noinspection PyMethodParameters
    def _generate_next_value_(name, _, count, __):
        return Object.auto_generate(count, DARK_SOULS_DSR, 1400000)

    o0110_0000 = 1401650
    o0110_0001 = 1401651
    o0110_0002 = 1401652
    o0200_0000 = 1401960
    o0200_0001 = 1401961
    o0200_0002 = 1401962
    o0500_0037 = 1401601
    o3910_0000 = 1401500
    o3910_0001 = 1401501
    o3910_0002 = 1401502
    o3910_0003 = 1401503
    o3910_0004 = 1401504
    o3910_0005 = 1401505
    o3910_0006 = 1401506
    o3910_0007 = 1401507
    o3910_0008 = 1401508
    o3910_0009 = 1401509
    o3910_0010 = 1401510
    o3910_0011 = 1401511
    o4000_0000 = 1401100
    o4050_0000 = 1401050
    o4100_0000 = 1401140
    o4101_0000 = 1401141
    o4102_0000 = 1401142
    o4103_0000 = 1401143
    o4104_0000 = 1401144
    o4105_0000 = 1401145
    o4106_0000 = 1401146
    o4107_0000 = 1401147
    o4108_0000 = 1401148
    o4109_0000 = 1401149
    o4109_0001 = 1401166
    o4109_0002 = 1401167
    o4110_0000 = 1401150
    o4111_0000 = 1401151
    o4111_0001 = 1401165
    o4111_0002 = 1401168
    o4112_0000 = 1401152
    o4113_0000 = 1401153
    o4114_0000 = 1401154
    o4115_0000 = 1401155
    o4116_0000 = 1401156
    o4117_0000 = 1401157
    o4118_0000 = 1401158
    o4119_0000 = 1401159
    o4120_0000 = 1401160
    o4120_0001 = 1401169
    o4121_0000 = 1401161
    o4122_0000 = 1401162
    o4123_0000 = 1401163
    o4124_0000 = 1401164
    o4125_0000 = 1401170
    o4200_0000 = 1401000
    o4201_0000 = 1401001
    o4202_0000 = 1401002
    o4550_0000 = 1401111
    o4560_0000 = 1401110
    o4570_0000 = 1401200
    o4820_0012 = 1401300
    o4950_0000 = 1401990
    o4951_0000 = 1401992
    o4952_0000 = 1401994
    o4953_0000 = 1401996
    o4954_0000 = 1401998
    o4956_0000 = 1401702


class Characters(Character):
    """`Character` entity IDs for MSB and EVS use."""

    # noinspection PyMethodParameters
    def _generate_next_value_(name, _, count, __):
        return Character.auto_generate(count, DARK_SOULS_DSR, 1400000)

    c0000_0003 = 6282
    c0000_0004 = 6132
    c0000_0005 = 6170
    c0000_0007 = 6530
    c0000_0008 = 6311
    c0000_0009 = 6421
    c0000_0010 = 6531
    c0000_PatchesAmbush = 7989
    c1000_0000 = 1400960
    c1000_0001 = 1400961
    c1000_0002 = 1400962
    c2060_0006 = 1400900
    c2060_0011 = 1400901
    c2060_0012 = 1400450
    c2060_0015 = 1400902
    c2060_0019 = 1400903
    c2060_0020 = 1400904
    c2370_TrollChanneler = 7969
    c2530_0000 = 1400200
    c2530_0001 = 1400201
    c2530_0002 = 1400202
    c2530_0003 = 1400203
    c2530_0004 = 1400204
    c2530_0005 = 1400205
    c2530_0006 = 1400206
    c2530_0007 = 1400207
    c2530_0008 = 1400208
    c2810_0003 = 1400905
    c2810_0004 = 1400906
    c2810_0005 = 1400907
    c2810_0006 = 1400908
    c2810_0007 = 1400909
    c2811_0000 = 1400100
    c2811_0001 = 1400101
    c2811_0002 = 1400102
    c2811_0003 = 1400103
    c2811_0004 = 1400104
    c3210_0000 = 6160
    c3210_0002 = 1400402
    c3210_0003 = 1400403
    c3220_0000 = 1400411
    c3220_0001 = 1400412
    c3220_0002 = 1400413
    c3220_0003 = 1400414
    c3220_0004 = 1400415
    c3220_0015 = 1400426
    c3220_0016 = 1400427
    c3220_0017 = 1400428
    c3220_0018 = 1400429
    c3220_0019 = 1400430
    c3220_0020 = 1400431
    c3220_0021 = 1400432
    c3220_0022 = 1400433
    c3220_0023 = 1400434
    c3220_0024 = 1400435
    c3490_0000 = 1403900
    c3490_0002 = 1403910
    c3491_0000 = 1403901
    c3491_0001 = 1403902
    c3491_0002 = 1403911
    c3491_0003 = 1403912
    c5240_0000 = 1400000
    c5280_0000 = 1400800
    c5340_0000 = 1400700


class PlayerStarts(PlayerStart):
    """`PlayerStart` entity IDs for MSB and EVS use."""

    # noinspection PyMethodParameters
    def _generate_next_value_(name, _, count, __):
        return PlayerStart.auto_generate(count, DARK_SOULS_DSR, 1400000)

    c0000_0001 = 1400999
    c0000_0002 = 1400980


class Collisions(Collision):
    """`Collision` entity IDs for MSB and EVS use."""

    # noinspection PyMethodParameters
    def _generate_next_value_(name, _, count, __):
        return Collision.auto_generate(count, DARK_SOULS_DSR, 1400000)

    h5810B0 = 1403100
    h5810B0_0000 = 1403101


class Sounds(SoundEvent):
    """`SoundEvent` entity IDs for MSB and EVS use."""

    # noinspection PyMethodParameters
    def _generate_next_value_(name, _, count, __):
        return SoundEvent.auto_generate(count, DARK_SOULS_DSR, 1400000)

    FairLadyMusic = 1403801
    QuelaagMusic = 1403800


class VFX(VFXEvent):
    """`VFXEvent` entity IDs for MSB and EVS use."""

    # noinspection PyMethodParameters
    def _generate_next_value_(name, _, count, __):
        return VFXEvent.auto_generate(count, DARK_SOULS_DSR, 1400000)

    CheckpointFog1 = 1401703
    MultiplayerFog1 = 1401995
    MultiplayerFog2 = 1401997
    MultiplayerFog3 = 1401999
    QuelaagEntranceFog = 1401991
    QuelaagExitFog = 1401993


class Spawners(SpawnerEvent):
    """`SpawnerEvent` entity IDs for MSB and EVS use."""

    # noinspection PyMethodParameters
    def _generate_next_value_(name, _, count, __):
        return SpawnerEvent.auto_generate(count, DARK_SOULS_DSR, 1400000)

    MosquitoSpawner1 = 1403000
    MosquitoSpawner2 = 1403001
    MosquitoSpawner3 = 1403002


class SpawnPoints(SpawnPointEvent):
    """`SpawnPointEvent` entity IDs for MSB and EVS use."""

    # noinspection PyMethodParameters
    def _generate_next_value_(name, _, count, __):
        return SpawnPointEvent.auto_generate(count, DARK_SOULS_DSR, 1400000)

    SpawnPoint0 = 1402960
    SpawnPoint1 = 1402961
    SpawnPoint2 = 1402962
    SpawnPointAtBoss = 1402950


class Points(RegionPoint):
    """`RegionPoint` entity IDs for MSB and EVS use."""

    # noinspection PyMethodParameters
    def _generate_next_value_(name, _, count, __):
        return RegionPoint.auto_generate(count, DARK_SOULS_DSR, 1400000)

    MildredInvaderSpawn = 1402060
    MildredSummonSign = 1402050
    UnusedBossWarpTest = 1402099


class Spheres(RegionSphere):
    """`RegionSphere` entity IDs for MSB and EVS use."""

    # noinspection PyMethodParameters
    def _generate_next_value_(name, _, count, __):
        return RegionSphere.auto_generate(count, DARK_SOULS_DSR, 1400000)

    FairLadyArea = 1402800
    MildredInvaderTrigger = 1402061
    MosquitoSpawnerControl1 = 1402200
    MosquitoSpawnerControl2 = 1402201
    MosquitoSpawnerControl3 = 1402202
    QuelanaArea = 1402400
    UnusedCeaselessPostSnap = 1402798
    UnusedCeaselessPreSnap = 1402797


class Boxes(RegionBox):
    """`RegionBox` entity IDs for MSB and EVS use."""

    # noinspection PyMethodParameters
    def _generate_next_value_(name, _, count, __):
        return RegionBox.auto_generate(count, DARK_SOULS_DSR, 1400000)

    CheckpointFog1BackSide = 1402603
    CheckpointFog1FrontSide = 1402602
    CreakyBridge00_00 = 1402000
    CreakyBridge00_01 = 1402001
    CreakyBridge00_02 = 1402002
    CreakyBridge01_00 = 1402010
    CreakyBridge01_01 = 1402011
    CreakyBridge01_02 = 1402012
    CreakyBridge02_00 = 1402020
    CreakyBridge02_01 = 1402021
    CreakyBridge02_02 = 1402022
    CreakyBridge02_03 = 1402023
    CreakyBridge02_04 = 1402024
    EingyiMoveTarget = 1402301
    EingyiNest = 1402300
    InvaderSpawn00 = 1404000
    InvaderSpawn01 = 1404001
    InvaderSpawn02 = 1404002
    InvaderSpawn10 = 1404010
    InvaderSpawn11 = 1404011
    InvaderSpawn12 = 1404012
    InvaderSpawn13 = 1404013
    QuelaagCombatStart = 1402996
    QuelaagFogPrompt = 1402998
    QuelaagFogRotationTarget = 1402997
    QuelaagMusic = 1402990
    UnusedBossExitTest = 1402098
    UnusedCeaselessTrigger = 1402799
    WallHuggerCombatArea = 1402100
