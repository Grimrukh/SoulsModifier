from soulstruct.games import DARK_SOULS_DSR
from soulstruct.game_types import *


class MapPieces(MapPiece):
    """`MapPiece` entity IDs for MSB and EVS use."""

    # noinspection PyMethodParameters
    def _generate_next_value_(name, _, count, __):
        return MapPiece.auto_generate(count, DARK_SOULS_DSR, 1600000)

    m4000B0_0000 = 1603110
    m4001B0_0000 = 1603111
    m4010B0_0000 = 1603112
    m4011B0_0000 = 1603113
    m4012B0_0000 = 1603114
    m4013B0_0000 = 1603115
    m4014B0_0000 = 1603116
    m4015B0_0000 = 1603117
    m4016B0_0000 = 1603118
    m4017B0_0000 = 1603119
    m4018B0_0000 = 1603120


class Objects(Object):
    """`Object` entity IDs for MSB and EVS use."""

    # noinspection PyMethodParameters
    def _generate_next_value_(name, _, count, __):
        return Object.auto_generate(count, DARK_SOULS_DSR, 1600000)

    o0110_0000 = 1601650
    o0110_0001 = 1601651
    o0110_0002 = 1601652
    o0200_0001 = 1601950
    o0200_0002 = 1601961
    o0500_0003 = 1601610
    o0500_0004 = 1601611
    o0504_0001 = 1601600
    o6000_0000 = 1601100
    o6010_0000 = 1601110
    o6010_0001 = 1601111
    o6100_0002 = 1601211
    o6100_0003 = 1601212
    o6100_0004 = 1601221
    o6100_0005 = 1601222
    o6100_0006 = 1601202
    o6100_0007 = 1601231
    o6100_0008 = 1601232
    o6110_0000 = 1601101
    o6200_0000 = 1601200
    o6200_0001 = 1601210
    o6200_0002 = 1601220
    o6200_0003 = 1601230
    o6400_0000 = 1601140
    o6401_0000 = 1601141
    o6410_0000 = 1601142
    o6450_0003 = 1601310
    o6450_0009 = 1601311
    o6450_0010 = 1609999
    o6500_0000 = 1601120
    o6601_0000 = 1601994
    o6602_0000 = 1601996
    o6603_0000 = 1601998
    o6604_0000 = 1601700
    o6605_0000 = 1601702
    o6606_0000 = 1601990


class Characters(Character):
    """`Character` entity IDs for MSB and EVS use."""

    # noinspection PyMethodParameters
    def _generate_next_value_(name, _, count, __):
        return Character.auto_generate(count, DARK_SOULS_DSR, 1600000)

    c0000_0003 = 6180
    c0000_0004 = 6220
    c0000_0006 = 6520
    c0000_0007 = 6271
    c0000_PatchesAmbush = 7993
    c1000_0001 = 1600950
    c1000_0002 = 1600961
    c2370_TrollChanneler = 7973
    c2390_0001 = 1600101
    c2390_0002 = 1600102
    c2390_0003 = 1600103
    c2390_0004 = 1600104
    c2390_0005 = 1600105
    c2390_0006 = 1600106
    c2390_0007 = 1600107
    c2390_0008 = 1600108
    c2390_0009 = 1600109
    c2390_0010 = 1600110
    c2390_0011 = 1600100
    c2390_0012 = 1600900
    c2390_0013 = 1600901
    c2390_0014 = 1600902
    c2390_0015 = 1600903
    c2390_0016 = 1600904
    c2390_0017 = 1600905
    c2670_0000 = 1600350
    c2670_0001 = 1600203
    c2670_0002 = 1600351
    c2670_0003 = 1600205
    c2670_0004 = 1600202
    c2670_0005 = 1600352
    c2670_0006 = 1600353
    c2670_0007 = 1600201
    c2670_0008 = 1600200
    c2670_0009 = 1600354
    c2670_0010 = 1600301
    c2670_0011 = 1600302
    c2670_0012 = 1600252
    c2670_0013 = 1600253
    c2670_0014 = 1600255
    c2670_0015 = 1600206
    c2670_0016 = 1600204
    c2670_0017 = 1600355
    c2670_0018 = 1600207
    c2670_0019 = 1600208
    c2670_0020 = 1600356
    c2670_0021 = 1600357
    c2670_0022 = 1600250
    c2670_0023 = 1600358
    c2670_0024 = 1600359
    c2670_0025 = 1600360
    c2670_0026 = 1600251
    c2670_0027 = 1600254
    c2670_0028 = 1600361
    c2670_0029 = 1600209
    c2670_0030 = 1600210
    c2670_0031 = 1600211
    c2680_0000 = 1600310
    c2680_0001 = 1600300
    c3420_0000 = 1600500
    c3490_0000 = 1603900
    c3490_0001 = 1603910
    c3490_0003 = 1603920
    c3491_0000 = 1603901
    c3491_0001 = 1603911
    c3491_0002 = 1603902
    c3491_0003 = 1603921
    c3491_0004 = 1603912
    c3491_0005 = 1603922
    c3500_0000 = 1600400
    c3500_0001 = 1600401
    c3501_0000 = 1600410
    c3501_0001 = 1600411
    c3501_0002 = 1600412
    c3501_0003 = 1600413
    c3501_0004 = 1600414
    c3501_0005 = 1600415
    c3501_0006 = 1600416
    c3501_0007 = 1600417
    c3501_0008 = 1600418
    c3501_0009 = 1600419
    c3501_0010 = 1600420
    c3501_0011 = 1600421
    c5330_0000 = 6340
    c5390_0000 = 1600800
    c5390_0001 = 1600801
    c5390_0002 = 1600802
    c5390_0003 = 1600803
    c5390_0004 = 1600804


class PlayerStarts(PlayerStart):
    """`PlayerStart` entity IDs for MSB and EVS use."""

    # noinspection PyMethodParameters
    def _generate_next_value_(name, _, count, __):
        return PlayerStart.auto_generate(count, DARK_SOULS_DSR, 1600000)

    c0000_0001 = 1600999
    c0000_0002 = 1600970


class Collisions(Collision):
    """`Collision` entity IDs for MSB and EVS use."""

    # noinspection PyMethodParameters
    def _generate_next_value_(name, _, count, __):
        return Collision.auto_generate(count, DARK_SOULS_DSR, 1600000)

    h0000B0_0000 = 1603200
    h0000B0_0002 = 1603250
    h0001B0_0000 = 1603201
    h0001B0_0001 = 1603251
    h0002B0_0000 = 1603202
    h0002B0_0001 = 1603252
    h0003B0_0000 = 1603203
    h0003B0_0001 = 1603253
    h0004B0_0000 = 1603204
    h0004B0_0001 = 1603254
    h0005B0_0000 = 1603205
    h0005B0_0001 = 1603255
    h0006B0_0000 = 1603206
    h0010B0_0000 = 1603207
    h0010B0_0001 = 1603257
    h0011B0_0000 = 1603208
    h0011B0_0001 = 1603258
    h0012B0_0000 = 1603209
    h0012B0_0001 = 1603259
    h0020B0_0000 = 1603210
    h0020B0_0001 = 1603260
    h0021B0_0000 = 1603211
    h0021B0_0001 = 1603261
    h0022B0_0000 = 1603212
    h0022B0_0001 = 1603262
    h0023B0_0000 = 1603213
    h0023B0_0001 = 1603263
    h0024B0_0000 = 1603214
    h0024B0_0001 = 1603264
    h0025B0_0000 = 1603215
    h0025B0_0001 = 1603265
    h0026B0_0000 = 1603216
    h0026B0_0001 = 1603266
    h0027B0_0000 = 1603217
    h0027B0_0001 = 1603267
    h0040B0_0000 = 1603300
    h0106B0_0000 = 1603256
    h0130B0_0000 = 1603121
    h0154B0_0000 = 1603122
    h7000B0_0000 = 1603100
    h7000B0_0001 = 1603102
    h7001B0_0000 = 1603101
    h8000B0_0000 = 1603103
    h8000B0_0001 = 1603104
    h9000B0_0000 = 1603310
    h9000B0_0001 = 1603311


class Sounds(SoundEvent):
    """`SoundEvent` entity IDs for MSB and EVS use."""

    # noinspection PyMethodParameters
    def _generate_next_value_(name, _, count, __):
        return SoundEvent.auto_generate(count, DARK_SOULS_DSR, 1600000)

    FourKingsMusic = 1603800
    JareelMusic = 1603801
    WaterSound = 1603850


class VFX(VFXEvent):
    """`VFXEvent` entity IDs for MSB and EVS use."""

    # noinspection PyMethodParameters
    def _generate_next_value_(name, _, count, __):
        return VFXEvent.auto_generate(count, DARK_SOULS_DSR, 1600000)

    CheckpointFog1 = 1601701
    CheckpointFog2 = 1601703
    FourKingsEntranceFog = 1601991
    MultiplayerFog1 = 1601995
    MultiplayerFog2 = 1601997
    MultiplayerFog3 = 1601999


class Spawners(SpawnerEvent):
    """`SpawnerEvent` entity IDs for MSB and EVS use."""

    # noinspection PyMethodParameters
    def _generate_next_value_(name, _, count, __):
        return SpawnerEvent.auto_generate(count, DARK_SOULS_DSR, 1600000)

    FourKingsSpawner = 1603000


class SpawnPoints(SpawnPointEvent):
    """`SpawnPointEvent` entity IDs for MSB and EVS use."""

    # noinspection PyMethodParameters
    def _generate_next_value_(name, _, count, __):
        return SpawnPointEvent.auto_generate(count, DARK_SOULS_DSR, 1600000)

    SpawnPoint0 = 1602960
    SpawnPoint1 = 1602961
    SpawnPointAtBoss = 1602950


class Points(RegionPoint):
    """`RegionPoint` entity IDs for MSB and EVS use."""

    # noinspection PyMethodParameters
    def _generate_next_value_(name, _, count, __):
        return RegionPoint.auto_generate(count, DARK_SOULS_DSR, 1600000)

    WitchBeatriceSummonSign = 1602000


class Spheres(RegionSphere):
    """`RegionSphere` entity IDs for MSB and EVS use."""

    # noinspection PyMethodParameters
    def _generate_next_value_(name, _, count, __):
        return RegionSphere.auto_generate(count, DARK_SOULS_DSR, 1600000)

    ChurchelevatorStartFromBottom = 1602211
    ChurchelevatorStartFromTop = 1602210
    DarkrootElevatorStartFromBottom = 1602231
    DarkrootElevatorStartFromTop = 1602230
    FirelinkElevatorStartFromBottom = 1602201
    FirelinkElevatorStartFromTop = 1602200
    SluiceElevatorStartFromBottom = 1602221
    SluiceElevatorStartFromTop = 1602220
    WyvernPoint1 = 1602720
    WyvernPoint2 = 1602721
    WyvernPoint3 = 1602722
    WyvernPoint11 = 1602730
    WyvernPoint12 = 1602731
    WyvernPoint13 = 1602732


class Cylinders(RegionCylinder):
    """`RegionCylinder` entity IDs for MSB and EVS use."""

    # noinspection PyMethodParameters
    def _generate_next_value_(name, _, count, __):
        return RegionCylinder.auto_generate(count, DARK_SOULS_DSR, 1600000)

    AbyssArea = 1602900
    FourKingsDeathCutsceneTrigger = 1602999


class Boxes(RegionBox):
    """`RegionBox` entity IDs for MSB and EVS use."""

    # noinspection PyMethodParameters
    def _generate_next_value_(name, _, count, __):
        return RegionBox.auto_generate(count, DARK_SOULS_DSR, 1600000)

    ArrivalFromKiln = 1602110
    BeatriceTarget = 1602010
    CheckpointFog1BackSide = 1602601
    CheckpointFog1FrontSide = 1602600
    CheckpointFog2BackSide = 1602603
    CheckpointFog2FrontSide = 1602602
    FemaleGhostCombatArea = 1602860
    FemaleGhostNestChange = 1602300
    FemaleGhostNestChangeTrigger = 1602301
    FourKingsFogPrompt = 1602998
    FourKingsFogRotationTarget = 1602997
    FourKingsMusic = 1602990
    FourKingsNotify = 1602996
    GhostAppearArea0 = 1602270
    GhostAppearArea1 = 1602271
    GhostAttackArea0 = 1602250
    GhostAttackArea1 = 1602251
    GhostAttackArea2 = 1602252
    GhostAttackArea3 = 1602253
    GhostAttackArea4 = 1602254
    GhostAttackArea5 = 1602255
    GhostsProhibitedInAbyss = 1602710
    GhostsProhibitedNearSluice = 1602711
    InvaderSpawn100 = 1604100
    InvaderSpawn101 = 1604101
    InvaderSpawn110 = 1604110
    InvaderSpawn111 = 1604111
    InvaderSpawn112 = 1604112
    InvaderSpawn120 = 1604120
    InvaderSpawn121 = 1604121
    JareelMusic = 1602890
    MaleGhostCombatArea1 = 1602850
    MaleGhostCombatArea2 = 1602851
    MaleGhostCombatArea3 = 1602852
    MaleGhostCombatArea4 = 1602853
    MaleGhostCombatArea5 = 1602854
    PlayerPoinAfterFourKingsDeath = 1602120
    UndeadDragonBayLeft = 1602762
    UndeadDragonBayRight = 1602761
    UndeadDragonBiteFront = 1602760
    UndeadDragonBreathFront = 1602763
    UndeadDragonBreathLeft = 1602765
    UndeadDragonBreathRight = 1602764
    WyvernAttackTarget1 = 1602700
    WyvernAttackTarget2 = 1602702
    WyvernAttackTarget3 = 1602703
    WyvernAttackTarget4 = 1602704
    WyvernCombatArea = 1602735
    WyvernGroundBreathGlideArea1 = 1602815
    WyvernGroundBreathGlideArea2 = 1602816
    WyvernGroundGlideAttackArea1 = 1602808
    WyvernGroundGlideAttackArea2 = 1602809
    WyvernGroundGlideAttackArea3 = 1602810
    WyvernGroundGlideAttackArea4 = 1602814
    WyvernGroundRightHandAttackArea1 = 1602811
    WyvernGroundRightHandAttackArea2 = 1602812
    WyvernGroundRightHandAttackArea3 = 1602813
    WyvernGroundTurnBeforeAttackNearGate1 = 1602817
    WyvernGroundTurnBeforeAttackNearGate2 = 1602818
    WyvernGroundWalkArea1 = 1602801
    WyvernGroundWalkArea2 = 1602802
    WyvernGroundWalkArea3 = 1602803
    WyvernGroundWalkArea4 = 1602804
    WyvernGroundWalkArea5 = 1602805
    WyvernGroundWalkArea6 = 1602806
    WyvernGroundWalkArea7 = 1602807
    WyvernNest = 1602736
    WyvernPlungeTarget = 1602701
