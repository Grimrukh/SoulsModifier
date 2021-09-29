from soulstruct.games import DARK_SOULS_DSR
from soulstruct.game_types import *


class Objects(Object):
    """`Object` entity IDs for MSB and EVS use."""

    # noinspection PyMethodParameters
    def _generate_next_value_(name, _, count, __):
        return Object.auto_generate(count, DARK_SOULS_DSR, 1810000)

    o0200_0000 = 1811960
    o0200_0001 = 1811961
    o0500_0000 = 1811600
    o0500_0008 = 1811650
    o0500_0023 = 1811602
    o0500_0024 = 1811604
    o0500_0025 = 1811606
    o0500_0026 = 1811608
    o0500_0027 = 1811610
    o0500_0028 = 1811612
    o0500_0029 = 1811615
    o0500_0030 = 1811618
    o0500_0031 = 1811621
    o0500_0032 = 1811624
    o0500_0033 = 1811601
    o0500_0034 = 1811603
    o0500_0035 = 1811605
    o0500_0036 = 1811607
    o0500_0037 = 1811609
    o0500_0038 = 1811611
    o0500_0039 = 1811614
    o0500_0040 = 1811617
    o0500_0041 = 1811620
    o0500_0042 = 1811623
    o0500_0043 = 1811613
    o0500_0044 = 1811616
    o0500_0045 = 1811619
    o0500_0046 = 1811622
    o8500_0000 = 1811140
    o8501_0000 = 1811141
    o8510_0000 = 1811200
    o8510_0001 = 1811201
    o8511_0000 = 1811202
    o8520_0000 = 1811210
    o8520_0001 = 1811211
    o8521_0000 = 1811212
    o8530_0000 = 1811215
    o8530_0001 = 1811216
    o8531_0000 = 1811217
    o8540_0000 = 1811100
    o8540_0001 = 1811101
    o8540_0002 = 1811102
    o8540_0003 = 1811103
    o8540_0004 = 1811104
    o8540_0005 = 1811105
    o8540_06 = 1811106
    o8541_0001 = 1811111
    o8542_0000 = 1811115
    o8544_0000 = 1811110
    o8550 = 1811300
    o8600_0000 = 1811230
    o8600_0001 = 1811231
    o8600_0002 = 1811232
    o8600_0003 = 1811233
    o8600_0004 = 1811234
    o8600_0005 = 1811235
    o8600_0006 = 1811236
    o8600_0007 = 1811237
    o8600_0008 = 1811238
    o8600_0009 = 1811239
    o8950_0000 = 1811990
    o8952_0000 = 1811700
    o8953_0000 = 1811890


class Characters(Character):
    """`Character` entity IDs for MSB and EVS use."""

    # noinspection PyMethodParameters
    def _generate_next_value_(name, _, count, __):
        return Character.auto_generate(count, DARK_SOULS_DSR, 1810000)

    c0000_0002 = 6023
    c0000_0003 = 6024
    c0000_PatchesAmbush = 7996
    c1000_0000 = 1810960
    c1000_0001 = 1810961
    c1000_0002 = 6450
    c2230_0000 = 1810810
    c2232_0000 = 1810800
    c2370_TrollChanneler = 7976
    c2500_0000 = 1810101
    c2500_0001 = 1810102
    c2500_0002 = 1810103
    c2500_0003 = 1810104
    c2500_0005 = 1810106
    c2500_0006 = 1810107
    c2500_0007 = 1810108
    c2500_0009 = 1810110
    c2500_0010 = 1810111
    c2500_0011 = 1810112
    c2500_0012 = 1810201
    c2500_0013 = 1810202
    c2500_0014 = 1810203
    c2500_0015 = 1810204
    c2500_0016 = 1810205
    c2500_0017 = 1810206
    c2500_0018 = 1810207
    c2500_0019 = 1810208
    c2500_0020 = 1810209
    c2500_0021 = 1810210
    c2550_0000 = 1810113
    c2550_0001 = 1810211
    c2550_0002 = 1810212
    c2792_0000 = 1810200
    c2792_0001 = 1810213
    c3490_0000 = 1813900
    c3491_0000 = 1813901
    c3491_0001 = 1813902


class PlayerStarts(PlayerStart):
    """`PlayerStart` entity IDs for MSB and EVS use."""

    # noinspection PyMethodParameters
    def _generate_next_value_(name, _, count, __):
        return PlayerStart.auto_generate(count, DARK_SOULS_DSR, 1810000)

    c0000_0001 = 1810998


class Collisions(Collision):
    """`Collision` entity IDs for MSB and EVS use."""

    # noinspection PyMethodParameters
    def _generate_next_value_(name, _, count, __):
        return Collision.auto_generate(count, DARK_SOULS_DSR, 1810000)

    h0006B1 = 1813120
    h0050B1 = 1813100
    h0051B1 = 1813101
    h0052B1 = 1813102
    h0053B1 = 1813103
    h0054B1 = 1813104
    h0091B1 = 1813105
    h0550B1_0000 = 1813121


class Sounds(SoundEvent):
    """`SoundEvent` entity IDs for MSB and EVS use."""

    # noinspection PyMethodParameters
    def _generate_next_value_(name, _, count, __):
        return SoundEvent.auto_generate(count, DARK_SOULS_DSR, 1810000)

    AsylumDemonMusic = 1813800
    StrayDemonMusic = 1813801


class VFX(VFXEvent):
    """`VFXEvent` entity IDs for MSB and EVS use."""

    # noinspection PyMethodParameters
    def _generate_next_value_(name, _, count, __):
        return VFXEvent.auto_generate(count, DARK_SOULS_DSR, 1810000)

    AsylumTopEntranceFog = 1811991
    CheckpointFog1 = 1811701
    StrayDemonLadderFog = 1811891


class Messages(MessageEvent):
    """`MessageEvent` entity IDs for MSB and EVS use."""

    # noinspection PyMethodParameters
    def _generate_next_value_(name, _, count, __):
        return MessageEvent.auto_generate(count, DARK_SOULS_DSR, 1810000)

    TutorialMessage08 = 1813220
    TutorialMessage09 = 1813221
    TutorialMessageClass00 = 1813200
    TutorialMessageClass01 = 1813201
    TutorialMessageClass02 = 1813202
    TutorialMessageClass03 = 1813203
    TutorialMessageClass04 = 1813204
    TutorialMessageHint00 = 1813210


class SpawnPoints(SpawnPointEvent):
    """`SpawnPointEvent` entity IDs for MSB and EVS use."""

    # noinspection PyMethodParameters
    def _generate_next_value_(name, _, count, __):
        return SpawnPointEvent.auto_generate(count, DARK_SOULS_DSR, 1810000)

    SpawnPoint00 = 1812960
    SpawnPoint01 = 1812961
    SpawnPointAtStart = 1812900


class Navigation(NavigationEvent):
    """`NavigationEvent` entity IDs for MSB and EVS use."""

    # noinspection PyMethodParameters
    def _generate_next_value_(name, _, count, __):
        return NavigationEvent.auto_generate(count, DARK_SOULS_DSR, 1810000)

    Navmesh_Bank00 = 1813300
    Navmesh_Bank01 = 1813301
    Navmesh_Bank02 = 1813302
    Navmesh_Bank03 = 1813303
    Navmesh_Bank04 = 1813304
    Navmesh_Bank05 = 1813305
    Navmesh_Bank06 = 1813306


class Spheres(RegionSphere):
    """`RegionSphere` entity IDs for MSB and EVS use."""

    # noinspection PyMethodParameters
    def _generate_next_value_(name, _, count, __):
        return RegionSphere.auto_generate(count, DARK_SOULS_DSR, 1810000)

    StrayCeilingBreakTrigger = 1812400


class Boxes(RegionBox):
    """`RegionBox` entity IDs for MSB and EVS use."""

    # noinspection PyMethodParameters
    def _generate_next_value_(name, _, count, __):
        return RegionBox.auto_generate(count, DARK_SOULS_DSR, 1810000)

    ArcherHollowFleeTarget = 1812102
    ArcherHollowFleeTrigger = 1812101
    ArrivalInFirelink = 1812110
    AsylumDemonCombatStart = 1812996
    AsylumDemonFogPrompt = 1812998
    AsylumDemonFogRotationTarget = 1812997
    AsylumDemonJumpedPoint1 = 1812300
    AsylumDemonJumpedPoint2 = 1812302
    AsylumDemonMusic = 1812990
    AsylumDemonUndergroundTrigger = 1812311
    AsylumDemonWatchingBalcony = 1812301
    AtCliffEdge = 1812000
    BallTrapTrigger = 1812120
    CheckpointFog1BackSide = 1812601
    CheckpointFog1FrontSide = 1812600
    FirelinkStartPoint = 1812090
    GameStartPoint = 1812100
    OscarDeathTrigger = 1812121
    PlayerAboveAsylumDemon = 1812350
    PlayerEscapesAsylumDemon = 1812320
    PlayerOnIndoorBalcony1 = 1812351
    PlayerOnIndoorBalcony2 = 1812352
    ShortcutGateLockedSide = 1812021
    ShortcutGateUnlockedSide = 1812020
    SnugglyItemDrop = 1812201
    SnugglyItemPickup = 1812200
    SnugglyNest = 1812001
    StartPointAfterCutscene = 1812011
    StartingCell = 1812010
    StrayDemonCombatStart = 1812896
    StrayDemonMusic = 1812890
    StrayDemonWaitingPoint = 1812305
