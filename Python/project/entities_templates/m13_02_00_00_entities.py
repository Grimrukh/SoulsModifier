from soulstruct.games import DARK_SOULS_DSR
from soulstruct.game_types import *


class Objects(Object):
    """`Object` entity IDs for MSB and EVS use."""

    # noinspection PyMethodParameters
    def _generate_next_value_(name, _, count, __):
        return Object.auto_generate(count, DARK_SOULS_DSR, 1320000)

    o0101_0000 = 1321900
    o0101_0001 = 1321901
    o0101_0002 = 1321902
    o0101_0003 = 1321903
    o0101_0004 = 1321904
    o0101_0005 = 1321905
    o0101_0006 = 1321906
    o0101_0007 = 1321907
    o0110_0000 = 1321650
    o0200_0000 = 1321960
    o0200_0001 = 1321961
    o0200_0002 = 1321962
    o3240_0000 = 1321140
    o3241_0000 = 1321141
    o3242_0000 = 1321142
    o3243_0000 = 1321143
    o3450_0000 = 1321200
    o3451_0000 = 1321201
    o3970_0000 = 1321994
    o3971_0000 = 1321700


class Characters(Character):
    """`Character` entity IDs for MSB and EVS use."""

    # noinspection PyMethodParameters
    def _generate_next_value_(name, _, count, __):
        return Character.auto_generate(count, DARK_SOULS_DSR, 1320000)

    c0000_0004 = 6288
    c0000_0005 = 6290
    c0000_PatchesAmbush = 7988
    c1000_0000 = 1320960
    c1000_0001 = 1320961
    c1000_0002 = 1320962
    c2370_TrollChanneler = 7968
    c3250_0000 = 1320100
    c3250_0001 = 1320101
    c3250_0002 = 1320102
    c3300_0001 = 1320201
    c3300_0002 = 1320202
    c3300_0003 = 1320203
    c3300_0004 = 1320204
    c3300_0005 = 1320205
    c3300_0006 = 1320206
    c3300_0007 = 1320207
    c3300_0008 = 1320208
    c3300_0009 = 1320209
    c3300_0010 = 1320210
    c3450_0000 = 1320800
    c3451_0000 = 1320801
    c3490_0000 = 1323900
    c3490_0001 = 1323910
    c3491_0000 = 1323901
    c3491_0001 = 1323911
    c3491_0002 = 1323902
    c3491_0003 = 1323912
    c3530_0000 = 1320700
    c3531_0000 = 1320701
    c3531_0001 = 1320702
    c3531_0002 = 1320703
    c3531_0003 = 1320704
    c3531_0004 = 1320705
    c3531_0005 = 1320706
    c3531_0006 = 1320707


class PlayerStarts(PlayerStart):
    """`PlayerStart` entity IDs for MSB and EVS use."""

    # noinspection PyMethodParameters
    def _generate_next_value_(name, _, count, __):
        return PlayerStart.auto_generate(count, DARK_SOULS_DSR, 1320000)

    c0000_0001 = 1320997
    c0000_0002 = 1320980


class VFX(VFXEvent):
    """`VFXEvent` entity IDs for MSB and EVS use."""

    # noinspection PyMethodParameters
    def _generate_next_value_(name, _, count, __):
        return VFXEvent.auto_generate(count, DARK_SOULS_DSR, 1320000)

    CheckpointFog1 = 1321701
    MultiplayerFog1 = 1321995


class SpawnPoints(SpawnPointEvent):
    """`SpawnPointEvent` entity IDs for MSB and EVS use."""

    # noinspection PyMethodParameters
    def _generate_next_value_(name, _, count, __):
        return SpawnPointEvent.auto_generate(count, DARK_SOULS_DSR, 1320000)

    SpawnPoint0 = 1322960
    SpawnPoint1 = 1322961
    SpawnPoint2 = 1322962


class Spheres(RegionSphere):
    """`RegionSphere` entity IDs for MSB and EVS use."""

    # noinspection PyMethodParameters
    def _generate_next_value_(name, _, count, __):
        return RegionSphere.auto_generate(count, DARK_SOULS_DSR, 1320000)

    HydraPointA1 = 1322751
    HydraPointA2 = 1322752
    HydraPointA3 = 1322753
    HydraPointA4 = 1322754
    HydraPointA5 = 1322755
    HydraPointA6 = 1322756
    HydraPointB1 = 1322761
    HydraPointB2 = 1322762
    HydraPointB3 = 1322763
    HydraPointB4 = 1322764
    HydraPointB5 = 1322765
    HydraPointB6 = 1322766
    HydraPointB7 = 1322767


class Boxes(RegionBox):
    """`RegionBox` entity IDs for MSB and EVS use."""

    # noinspection PyMethodParameters
    def _generate_next_value_(name, _, count, __):
        return RegionBox.auto_generate(count, DARK_SOULS_DSR, 1320000)

    CheckpointFog1BackSide = 1322601
    CheckpointFog1FrontSide = 1322600
    HydraAreaA = 1322705
    HydraAreaB = 1322706
    HydraFarBreathArea = 1322770
    HydraFarBreathAreaWithPlayer = 1322771
    HydraJumpAToBAscentSnap = 1322710
    HydraJumpAToBSnap = 1322700
    HydraJumpBToAAscentSnap = 1322711
    HydraJumpBToASnap = 1322701
    HydraPointAToPointBTrigger = 1322703
    HydraPointBToPointATrigger = 1322704
