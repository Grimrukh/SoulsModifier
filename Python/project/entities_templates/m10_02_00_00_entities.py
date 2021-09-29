from soulstruct.games import DARK_SOULS_DSR
from soulstruct.game_types import *


class MapPieces(MapPiece):
    """`MapPiece` entity IDs for MSB and EVS use."""

    # noinspection PyMethodParameters
    def _generate_next_value_(name, _, count, __):
        return MapPiece.auto_generate(count, DARK_SOULS_DSR, 1020000)

    m2022B2_0000 = 1023501


class Objects(Object):
    """`Object` entity IDs for MSB and EVS use."""

    # noinspection PyMethodParameters
    def _generate_next_value_(name, _, count, __):
        return Object.auto_generate(count, DARK_SOULS_DSR, 1020000)

    o0020_0000 = 1021700
    o0020_0001 = 1021701
    o0020_0002 = 1021702
    o0020_0003 = 1021703
    o0020_0004 = 1021704
    o0020_0005 = 1021705
    o0020_0006 = 1021706
    o0020_0007 = 1021707
    o0020_0008 = 1021708
    o0020_0009 = 1021709
    o0020_0010 = 1021710
    o0020_0011 = 1021711
    o0020_0012 = 1021712
    o0020_0013 = 1021713
    o0020_0014 = 1021714
    o0020_0015 = 1021715
    o0020_0016 = 1021716
    o0020_0017 = 1021717
    o0020_0018 = 1021718
    o0020_0019 = 1021719
    o0020_0020 = 1021720
    o0020_0021 = 1021721
    o0020_0022 = 1021722
    o0020_0023 = 1021723
    o0020_0024 = 1021724
    o0020_0025 = 1021725
    o0020_0026 = 1021726
    o0020_0027 = 1021727
    o0110_0000 = 1021650
    o0110_0001 = 1021651
    o0110_0002 = 1021652
    o0110_0003 = 1021653
    o0110_0004 = 1021690
    o0200_0000 = 1021960
    o1460_0000 = 1021000
    o1465_0000 = 1021465
    o1475_0000 = 1021300
    o1480_0000 = 1021480
    o1481_0000 = 1021481
    o6100_0000 = 1021201


class Characters(Character):
    """`Character` entity IDs for MSB and EVS use."""

    # noinspection PyMethodParameters
    def _generate_next_value_(name, _, count, __):
        return Character.auto_generate(count, DARK_SOULS_DSR, 1020000)

    c0000_0003 = 6261
    c0000_0011 = 6031
    c0000_0012 = 6041
    c0000_0013 = 6070
    c0000_0014 = 6080
    c0000_0015 = 6090
    c0000_0016 = 6100
    c0000_0017 = 6131
    c0000_0018 = 6270
    c0000_0019 = 6301
    c0000_0020 = 6287
    c0000_0021 = 6292
    c0000_0022 = 6322
    c0000_0024 = 6181
    c0000_PatchesAmbush = 7982
    c1000_0000 = 1020960
    c1000_0002 = 6450
    c2370_TrollChanneler = 7962
    c2510_0000 = 6240
    c2540_0000 = 1020160
    c2540_0001 = 1020161
    c2540_0003 = 1020163
    c2540_0006 = 1020165
    c2540_0007 = 1020166
    c2550_0000 = 1020190
    c2750_0000 = 6060
    c2900_0000 = 1020200
    c2900_0001 = 1020201
    c2900_0002 = 1020202
    c2900_0003 = 1020203
    c2900_0004 = 1020204
    c2900_0005 = 1020205
    c2900_0006 = 1020206
    c2900_0009 = 1020209
    c2900_0010 = 1020210
    c2900_0011 = 1020211
    c2900_0014 = 1020214
    c2910_0000 = 1020212
    c2910_0001 = 1020213
    c3510_0000 = 1020100
    c5330_0000 = 6330


class PlayerStarts(PlayerStart):
    """`PlayerStart` entity IDs for MSB and EVS use."""

    # noinspection PyMethodParameters
    def _generate_next_value_(name, _, count, __):
        return PlayerStart.auto_generate(count, DARK_SOULS_DSR, 1020000)

    c0000_0001 = 1020997
    c0000_0002 = 1020980


class Collisions(Collision):
    """`Collision` entity IDs for MSB and EVS use."""

    # noinspection PyMethodParameters
    def _generate_next_value_(name, _, count, __):
        return Collision.auto_generate(count, DARK_SOULS_DSR, 1020000)

    h0005B2_0000 = 1023500
    h0105B2_0000 = 1023510
    h7000B2_0000 = 1023502
    h8100B2_0000 = 1023600
    h8100B2_0001 = 1023601


class Sounds(SoundEvent):
    """`SoundEvent` entity IDs for MSB and EVS use."""

    # noinspection PyMethodParameters
    def _generate_next_value_(name, _, count, __):
        return SoundEvent.auto_generate(count, DARK_SOULS_DSR, 1020000)

    FirelinkShrineMusic = 1023800


class SpawnPoints(SpawnPointEvent):
    """`SpawnPointEvent` entity IDs for MSB and EVS use."""

    # noinspection PyMethodParameters
    def _generate_next_value_(name, _, count, __):
        return SpawnPointEvent.auto_generate(count, DARK_SOULS_DSR, 1020000)

    SpawnPoint0 = 1022960


class Boxes(RegionBox):
    """`RegionBox` entity IDs for MSB and EVS use."""

    # noinspection PyMethodParameters
    def _generate_next_value_(name, _, count, __):
        return RegionBox.auto_generate(count, DARK_SOULS_DSR, 1020000)

    ArriveFirstTime = 1022100
    ArriveFromAsylumSecondTime = 1022121
    ArriveFromKiln = 1022110
    CurlUpInNest = 1022120
    ElevatorForcedDeath = 1022300
    ElevatorStartArea0 = 1022000
    ElevatorStartArea1 = 1022001
    ElevatorStartArea2 = 1022002
    ElevatorStartArea3 = 1022003
    FemaleUndeadMerchantFleePoint = 1022700
    FirebombHollowNest = 1022711
    HellkiteAttackTargetLongRange = 1022211
    HellkiteAttackTargetShortRange = 1022210
    HellkiteErasureTrigger = 1022220
    HellkiteInvincibilityTrigger = 1022225
    HellkiteRepositioning = 1022200
    HoleToKiln = 1022111
    HollowsProhibited = 1022710
