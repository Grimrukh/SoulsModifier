from soulstruct.games import DARK_SOULS_DSR
from soulstruct.game_types import *


class Objects(Object):
    """`Object` entity IDs for MSB and EVS use."""

    # noinspection PyMethodParameters
    def _generate_next_value_(name, _, count, __):
        return Object.auto_generate(count, DARK_SOULS_DSR, 1800000)

    o0200_0001 = 1801950
    o8050_0000 = 1801990
    o8051_0000 = 1801994
    o8300 = 1801101
    o8310 = 1801960
    o8311 = 1801110
    o8312 = 1801111


class Characters(Character):
    """`Character` entity IDs for MSB and EVS use."""

    # noinspection PyMethodParameters
    def _generate_next_value_(name, _, count, __):
        return Character.auto_generate(count, DARK_SOULS_DSR, 1800000)

    c0000_0002 = 6544
    c0000_PatchesAmbush = 7995
    c1000_0000 = 1800960
    c2370_TrollChanneler = 7975
    c2790_0001 = 1800200
    c2790_0002 = 1800201
    c2790_0003 = 1800202
    c2790_0004 = 1800203
    c2790_0005 = 1800204
    c2790_0006 = 1800900
    c2790_0007 = 1800901
    c2790_0008 = 1800902
    c2790_0009 = 1800903
    c2790_0010 = 1800904
    c2791_0000 = 1800100
    c2791_0001 = 1800101
    c2791_0002 = 1800102
    c2791_0003 = 1800103
    c2791_0004 = 1800104
    c2791_0005 = 1800105
    c3490_0000 = 1803900
    c3491_0000 = 1803901
    c3491_0001 = 1803902
    c5330_0016 = 6331
    c5330_0017 = 6341
    c5370_0000 = 1800800


class PlayerStarts(PlayerStart):
    """`PlayerStart` entity IDs for MSB and EVS use."""

    # noinspection PyMethodParameters
    def _generate_next_value_(name, _, count, __):
        return PlayerStart.auto_generate(count, DARK_SOULS_DSR, 1800000)

    c0000_0001 = 1800999


class Sounds(SoundEvent):
    """`SoundEvent` entity IDs for MSB and EVS use."""

    # noinspection PyMethodParameters
    def _generate_next_value_(name, _, count, __):
        return SoundEvent.auto_generate(count, DARK_SOULS_DSR, 1800000)

    GwynMusic = 1803800


class VFX(VFXEvent):
    """`VFXEvent` entity IDs for MSB and EVS use."""

    # noinspection PyMethodParameters
    def _generate_next_value_(name, _, count, __):
        return VFXEvent.auto_generate(count, DARK_SOULS_DSR, 1800000)

    GwynEntranceFog = 1801991
    MultiplayerFog1 = 1801995


class SpawnPoints(SpawnPointEvent):
    """`SpawnPointEvent` entity IDs for MSB and EVS use."""

    # noinspection PyMethodParameters
    def _generate_next_value_(name, _, count, __):
        return SpawnPointEvent.auto_generate(count, DARK_SOULS_DSR, 1800000)

    SpawnPoint0 = 1802960
    SpawnPointAtBoss = 1802130


class Points(RegionPoint):
    """`RegionPoint` entity IDs for MSB and EVS use."""

    # noinspection PyMethodParameters
    def _generate_next_value_(name, _, count, __):
        return RegionPoint.auto_generate(count, DARK_SOULS_DSR, 1800000)

    SolaireSpawnPoint = 1802201
    SolaireSummonSign = 1802050


class Spheres(RegionSphere):
    """`RegionSphere` entity IDs for MSB and EVS use."""

    # noinspection PyMethodParameters
    def _generate_next_value_(name, _, count, __):
        return RegionSphere.auto_generate(count, DARK_SOULS_DSR, 1800000)

    GwynMusic = 1802990


class Boxes(RegionBox):
    """`RegionBox` entity IDs for MSB and EVS use."""

    # noinspection PyMethodParameters
    def _generate_next_value_(name, _, count, __):
        return RegionBox.auto_generate(count, DARK_SOULS_DSR, 1800000)

    ArrivalFromFirelinkOrAbyss = 1802110
    ArrivalUnknown = 1802120
    FirelinkAltarLocked = 1802100
    GhostKnightMovement1 = 1802000
    GhostKnightMovement2 = 1802001
    GhostKnightMovement3 = 1802002
    GhostKnightMovement4 = 1802003
    GhostKnightMovement5 = 1802004
    GhostKnightMovement6 = 1802005
    GhostKnightMovementGoal = 1802006
    GwynCombatStart = 1802996
    GwynFogPrompt = 1802998
    GwynFogRotationTarget = 1802997
    InvaderSpawn00 = 1804000
    InvaderSpawn01 = 1804001
    InvaderSpawn02 = 1804002
    SolaireFogTrigger = 1802200
