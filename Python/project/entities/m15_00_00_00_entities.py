from soulstruct.games import DARK_SOULS_DSR
from soulstruct.game_types import *


class Objects(Object):
    """`Object` entity IDs for MSB and EVS use."""

    # noinspection PyMethodParameters
    def _generate_next_value_(name, _, count, __):
        return Object.auto_generate(count, DARK_SOULS_DSR, 1500000)

    o0110_0000 = 1501650
    o0110_0002 = 1501652
    o0110_0004 = 1501654
    o0110_0009 = 1501659
    o0110_0010 = 1501660
    o0200_0002 = 1501961
    o0500_0013 = 1501651
    o0500_0014 = 1501658
    o5000_0000 = 1501850
    o5000_0001 = 1501851
    o5000_0002 = 1501852
    o5000_0003 = 1501853
    o5000_0004 = 1501854
    o5000_0010 = 1501855
    o5000_0011 = 1501856
    o5000_0012 = 1501857
    o5000_0013 = 1501858
    o5000_0020 = 1501859
    o5000_0021 = 1501860
    o5000_0022 = 1501861
    o5000_0023 = 1501862
    o5000_0030 = 1501863
    o5000_0031 = 1501864
    o5000_0032 = 1501865
    o5000_0033 = 1501866
    o5010_0000 = 1501800
    o5010_0001 = 1501801
    o5010_0002 = 1501802
    o5010_0003 = 1501803
    o5010_0004 = 1501804
    o5010_0005 = 1501805
    o5010_0006 = 1501806
    o5010_0007 = 1501807
    o5100_0000 = 1501000
    o5110_0000 = 1501020
    o5120_0000 = 1501021
    o5140_0000 = 1501001
    o5150_0000 = 1501990
    o5151_0000 = 1501994
    o5152_0000 = 1501700
    o5153_0000 = 1501702
    o5200_0000 = 1501790
    o5210_0000 = 1501810
    o5210_0001 = 1501811
    o5210_0002 = 1501812
    o5210_0003 = 1501813
    o5300_0000 = 1501010
    o5301_0000 = 1501011
    o5310_0002 = 1501030
    o5310_0003 = 1501031
    o5310_0004 = 1501032
    o5310_0006 = 1501033
    o5310_0007 = 1501034
    o5310_0012 = 1501035
    o5310_0017 = 1501036
    o5400_0000 = 1501140
    o5401_0000 = 1501141
    o5403_0000 = 1501143
    o5404_0000 = 1501142
    o5500_0000 = 1501200
    o5501_0001 = 1501201
    o5501_0002 = 1501202
    o5501_0003 = 1501203
    o5501_0004 = 1501204
    o5501_0005 = 1501205
    o5510_0000 = 1501210
    o5510_0001 = 1501211
    o5510_0002 = 1501212
    o5510_0003 = 1501213
    o5510_0004 = 1501214
    o5510_0005 = 1501215
    o5510_0006 = 1501216
    o5510_0007 = 1501217
    o5560_0001 = 1501100
    o5560_0002 = 1501101
    o5560_0003 = 1501102
    o5560_0004 = 1501103
    o5560_0006 = 1501104
    o5560_0007 = 1501105
    o5560_0009 = 1501106
    o5561_0000 = 1501107
    o5561_0001 = 1501108


class Characters(Character):
    """`Character` entity IDs for MSB and EVS use."""

    # noinspection PyMethodParameters
    def _generate_next_value_(name, _, count, __):
        return Character.auto_generate(count, DARK_SOULS_DSR, 1500000)

    c0000_0004 = 6030
    c0000_0005 = 6250
    c0000_0006 = 6280
    c0000_0007 = 6510
    c0000_0008 = 6043
    c0000_0009 = 6600
    c0000_PatchesAmbush = 7991
    c1000_0002 = 1500961
    c2300_0000 = 1500300
    c2300_0001 = 1500301
    c2300_0002 = 1500302
    c2300_0003 = 1500303
    c2320_0000 = 1500800
    c2370_TrollChanneler = 7971
    c2570_0000 = 1500201
    c2690_0000 = 1500200
    c2690_0004 = 1500110
    c2690_0005 = 1500122
    c2690_0006 = 1500120
    c2690_0007 = 1500121
    c2690_0012 = 1500900
    c2690_0013 = 1500901
    c2690_0014 = 1500902
    c2690_0015 = 1500903
    c2690_0016 = 1500904
    c2690_0017 = 1500905
    c2690_0018 = 1500906
    c2700_0008 = 1500907
    c2700_0009 = 1500908
    c2700_0010 = 1500909
    c2780_0000 = 1500010
    c2860_0000 = 1500101
    c2860_0001 = 1500100
    c2860_0003 = 1500102
    c3490_0000 = 1503900
    c3490_0001 = 1503910
    c3490_0002 = 1503920
    c3491_0000 = 1503901
    c3491_0001 = 1503911
    c3491_0002 = 1503921
    c3491_0003 = 1503902
    c3491_0004 = 1503912
    c3491_0005 = 1503922


class PlayerStarts(PlayerStart):
    """`PlayerStart` entity IDs for MSB and EVS use."""

    # noinspection PyMethodParameters
    def _generate_next_value_(name, _, count, __):
        return PlayerStart.auto_generate(count, DARK_SOULS_DSR, 1500000)

    c0000_0001 = 1500999


class Collisions(Collision):
    """`Collision` entity IDs for MSB and EVS use."""

    # noinspection PyMethodParameters
    def _generate_next_value_(name, _, count, __):
        return Collision.auto_generate(count, DARK_SOULS_DSR, 1500000)

    h0060B0_0000 = 1503300
    h0081B0_0000 = 1503200
    h0081B0_0001 = 1503201
    h0081B0_0002 = 1503202
    h0110B0_0000 = 1503210
    h1100B0_0000 = 1503000


class Sounds(SoundEvent):
    """`SoundEvent` entity IDs for MSB and EVS use."""

    # noinspection PyMethodParameters
    def _generate_next_value_(name, _, count, __):
        return SoundEvent.auto_generate(count, DARK_SOULS_DSR, 1500000)

    IronGolemMusic = 1503800


class VFX(VFXEvent):
    """`VFXEvent` entity IDs for MSB and EVS use."""

    # noinspection PyMethodParameters
    def _generate_next_value_(name, _, count, __):
        return VFXEvent.auto_generate(count, DARK_SOULS_DSR, 1500000)

    AnorLondoWarpRing = 1503010
    ArrowTriggerA = 1503500
    ArrowTriggerB = 1503501
    ArrowTriggerC = 1503502
    ArrowTriggerD = 1503503
    CheckpointFog1 = 1501701
    CheckpointFog2 = 1501703
    IronGolemEntranceFog = 1501991
    MultiplayerFog1 = 1501995


class SpawnPoints(SpawnPointEvent):
    """`SpawnPointEvent` entity IDs for MSB and EVS use."""

    # noinspection PyMethodParameters
    def _generate_next_value_(name, _, count, __):
        return SpawnPointEvent.auto_generate(count, DARK_SOULS_DSR, 1500000)

    SpawnPoint0 = 1502960
    SpawnPoint1 = 1502961
    SpawnPointAtBoss = 1502950


class Navigation(NavigationEvent):
    """`NavigationEvent` entity IDs for MSB and EVS use."""

    # noinspection PyMethodParameters
    def _generate_next_value_(name, _, count, __):
        return NavigationEvent.auto_generate(count, DARK_SOULS_DSR, 1500000)

    Navmesh_CageElevator_0_0 = 1503100
    Navmesh_CageElevator_0_1 = 1503110
    Navmesh_CageElevator_1_0 = 1503101
    Navmesh_CageElevator_1_1 = 1503111
    Navmesh_CageElevator_2_0 = 1503102
    Navmesh_CageElevator_2_1 = 1503112
    Navmesh_CageElevator_3_0 = 1503103
    Navmesh_CageElevator_3_1 = 1503113


class Points(RegionPoint):
    """`RegionPoint` entity IDs for MSB and EVS use."""

    # noinspection PyMethodParameters
    def _generate_next_value_(name, _, count, __):
        return RegionPoint.auto_generate(count, DARK_SOULS_DSR, 1500000)

    TarkusSummonSign = 1502000


class Spheres(RegionSphere):
    """`RegionSphere` entity IDs for MSB and EVS use."""

    # noinspection PyMethodParameters
    def _generate_next_value_(name, _, count, __):
        return RegionSphere.auto_generate(count, DARK_SOULS_DSR, 1500000)

    AnorLondoWarpPrompt = 1502505
    CageElevatorStart_LowerLeft = 1502062
    CageElevatorStart_LowerRight = 1502063
    CageElevatorStart_UpperLeft = 1502060
    CageElevatorStart_UpperRight = 1502061


class Boxes(RegionBox):
    """`RegionBox` entity IDs for MSB and EVS use."""

    # noinspection PyMethodParameters
    def _generate_next_value_(name, _, count, __):
        return RegionBox.auto_generate(count, DARK_SOULS_DSR, 1500000)

    AnorLondoArrivalPoint = 1502501
    ArrivalFromAnorLondo = 1502500
    ArrowTrapTriggerA = 1502200
    ArrowTrapTriggerB = 1502201
    ArrowTrapTriggerC = 1502202
    ArrowTrapTriggerD = 1502203
    ArrowTrapTriggerE = 1502204
    ArrowTrapTriggerF = 1502205
    AutoBouldersInside = 1502800
    AutoBouldersOutside = 1502801
    BerenikeKnightCombatAreaA = 1502721
    BerenikeKnightCombatAreaB = 1502722
    BerenikeKnightRetreatArea = 1502723
    BombGiantCombatArea = 1502710
    BombTargetA = 1502700
    BombTargetB = 1502701
    BombTargetC = 1502702
    BombTargetD = 1502703
    BombTargetE = 1502704
    BombTargetF = 1502705
    BoulderCrushesSerpentTrigger = 1502110
    BoulderGiantAlertTrigger = 1502101
    BoulderGiantAnimationSnap = 1502100
    BoulderGiantCombatArea = 1502720
    BoulderPitCrushed1 = 1502811
    BoulderPitCrushed2 = 1502812
    BoulderPitStackingTrigger = 1502810
    CheckpointFog1BackSide = 1502601
    CheckpointFog1FrontSide = 1502600
    CheckpointFog2BackSide = 1502603
    CheckpointFog2FrontSide = 1502602
    GateGiantCombatArea = 1502750
    GateInitialization = 1502050
    InvaderSpawn00 = 1504000
    InvaderSpawn01 = 1504001
    InvaderSpawn10 = 1504010
    InvaderSpawn11 = 1504011
    InvaderSpawn12 = 1504012
    InvaderSpawn20 = 1504020
    InvaderSpawn21 = 1504021
    IronGolemCombatStart = 1502996
    IronGolemDoesNotSweep = 1502730
    IronGolemFalls = 1502850
    IronGolemFogPrompt = 1502998
    IronGolemFogRotationTarget = 1502997
    IronGolemMusic = 1502990
    MimicNest = 1502010
    NoSignZone = 1504050
    SiegmeyerMovement = 1502510
    TitaniteDemonCombatAreaA = 1502733
    TitaniteDemonCombatAreaB = 1502734
    TitaniteDemonCombatAreaC = 1502735
    TitaniteDemonRetreat1 = 1502731
    TitaniteDemonRetreat2 = 1502732
