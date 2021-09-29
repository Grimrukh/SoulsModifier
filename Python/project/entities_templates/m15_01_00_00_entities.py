from soulstruct.games import DARK_SOULS_DSR
from soulstruct.game_types import *


class MapPieces(MapPiece):
    """`MapPiece` entity IDs for MSB and EVS use."""

    # noinspection PyMethodParameters
    def _generate_next_value_(name, _, count, __):
        return MapPiece.auto_generate(count, DARK_SOULS_DSR, 1510000)

    m9000B1_0000 = 1513400
    m9500B1_0000 = 1513401


class Objects(Object):
    """`Object` entity IDs for MSB and EVS use."""

    # noinspection PyMethodParameters
    def _generate_next_value_(name, _, count, __):
        return Object.auto_generate(count, DARK_SOULS_DSR, 1510000)

    o0110_0001 = 1511651
    o0110_0002 = 1511652
    o0110_0003 = 1511653
    o0110_0004 = 1511654
    o0110_0006 = 1511656
    o0110_0007 = 1511657
    o0110_0008 = 1511658
    o0110_0009 = 1511659
    o0110_0010 = 1511660
    o0110_0011 = 1511661
    o0110_0012 = 1511662
    o0110_0015 = 1511665
    o0110_0016 = 1511666
    o0110_0017 = 1511667
    o0110_0018 = 1511668
    o0110_0019 = 1511669
    o0200_0000 = 1511960
    o0200_0001 = 1511961
    o0200_0002 = 1511950
    o0200_0003 = 1511962
    o0500_0000 = 1511600
    o0500_0008 = 1511601
    o5410_0000 = 1511140
    o5410_0001 = 1511141
    o5600_0000 = 1511050
    o5610_0000 = 1511300
    o5611_0000 = 1511310
    o5620_0000 = 1511402
    o5630_0000 = 1511401
    o5700_0000 = 1511000
    o5710_0000 = 1511200
    o5720_0000 = 1511250
    o5720_0001 = 1511251
    o5720_0002 = 1511252
    o5720_0003 = 1511253
    o5720_0004 = 1511254
    o5720_0006 = 1511256
    o5720_0007 = 1511257
    o5720_0008 = 1511258
    o5720_0009 = 1511259
    o5730_0000 = 1511010
    o5740_0000 = 1511210
    o5750_0001 = 1511301
    o5750_0002 = 1511302
    o5750_0003 = 1511303
    o5750_0004 = 1511304
    o5760_0000 = 1511001
    o5800_0000 = 1511101
    o5801_0000 = 1511102
    o5810_0000 = 1511100
    o5850_0000 = 1511500
    o5860_0000 = 1511990
    o5861_0000 = 1511992
    o5862_0000 = 1511988
    o5863_0000 = 1511994
    o5864_0000 = 1511700
    o5865_0000 = 1511702
    o5867_0000 = 1511890
    o5868_0000 = 1511892
    o5869_0000 = 1511754
    o5870_0000 = 1511750
    o5871_0000 = 1511752
    o5900_0000 = 1511400
    o5905_0000 = 1511450
    o5906_0000 = 1511451
    o5965_0000 = 1511110


class Characters(Character):
    """`Character` entity IDs for MSB and EVS use."""

    # noinspection PyMethodParameters
    def _generate_next_value_(name, _, count, __):
        return Character.auto_generate(count, DARK_SOULS_DSR, 1510000)

    c0000_0003 = 6010
    c0000_0004 = 6302
    c0000_0005 = 6283
    c0000_0006 = 6003
    c0000_0009 = 6490
    c0000_0010 = 6500
    c0000_0011 = 6543
    c0000_0012 = 6640
    c0000_0013 = 6650
    c0000_PatchesAmbush = 7992
    c1000_0000 = 1510960
    c1000_0001 = 1510961
    c1000_0002 = 1510950
    c1000_0003 = 1510962
    c2260_0000 = 1510100
    c2260_0003 = 1510110
    c2260_0004 = 1510111
    c2260_0005 = 1510112
    c2260_0006 = 1510113
    c2260_0007 = 1510114
    c2260_0008 = 1510115
    c2260_0010 = 1510117
    c2260_0011 = 1510118
    c2260_0012 = 1510119
    c2300_0000 = 1510250
    c2360_0000 = 1510810
    c2360_0001 = 1510811
    c2370_TrollChanneler = 7972
    c2400_0010 = 1510310
    c2410_0000 = 1510320
    c2410_0001 = 1510305
    c2410_0002 = 1510321
    c2410_0003 = 1510322
    c2410_0004 = 1510323
    c2410_0005 = 1510500
    c2410_0006 = 1510324
    c2410_0007 = 1510325
    c2410_0009 = 1510300
    c2410_0010 = 1510326
    c2410_0011 = 1510327
    c2410_0012 = 1510328
    c2410_0013 = 1510329
    c2410_0014 = 1510301
    c2410_0015 = 1510302
    c2410_0016 = 1510903
    c2410_0017 = 1510904
    c2410_0018 = 1510905
    c2410_0019 = 1510906
    c2410_0020 = 1510907
    c2410_0021 = 1510908
    c2410_0022 = 1510909
    c2780_0000 = 1510200
    c2780_0001 = 1510201
    c2780_0002 = 1510202
    c2780_0003 = 1510203
    c2860_0000 = 6210
    c2870_0000 = 1510400
    c2870_0001 = 1510401
    c2870_0002 = 1510402
    c2870_0003 = 1510403
    c2870_0004 = 1510404
    c2870_0005 = 1510405
    c2870_0008 = 1510408
    c2870_0009 = 1510409
    c2870_0012 = 1510412
    c2870_0013 = 1510413
    c2870_0014 = 1510900
    c2870_0015 = 1510901
    c2870_0016 = 1510902
    c3490_0000 = 1513900
    c3490_0001 = 1513910
    c3490_0003 = 1513920
    c3491_0000 = 1513901
    c3491_0001 = 1513911
    c3491_0002 = 1513902
    c3491_0003 = 1513921
    c3491_0004 = 1513912
    c3491_0005 = 1513922
    c5270_0000 = 1510800
    c5271_0000 = 1510801
    c5310_0000 = 1510600
    c5320_0000 = 1510650
    c5351_0000 = 1510450
    c5351_0001 = 1510452
    c5353_0000 = 1510451
    c5353_0001 = 1510453


class PlayerStarts(PlayerStart):
    """`PlayerStart` entity IDs for MSB and EVS use."""

    # noinspection PyMethodParameters
    def _generate_next_value_(name, _, count, __):
        return PlayerStart.auto_generate(count, DARK_SOULS_DSR, 1510000)

    c0000_0001 = 1510998
    c0000_0002 = 1510980
    c0000_0007 = 1510970
    c0000_0008 = 1510982


class Collisions(Collision):
    """`Collision` entity IDs for MSB and EVS use."""

    # noinspection PyMethodParameters
    def _generate_next_value_(name, _, count, __):
        return Collision.auto_generate(count, DARK_SOULS_DSR, 1510000)

    h0005B1_0000 = 1513405
    h0010B1_0000 = 1513303
    h0010B1_0001 = 1513302
    h0010B1_0002 = 1513301
    h0030B1_0000 = 1513100
    h0030B1_0001 = 1513110
    h0031B1_0000 = 1513101
    h0031B1_0001 = 1513111
    h0031B1_0002 = 1513112
    h0031B1_0003 = 1513113
    h0031B1_0004 = 1513114
    h0031B1_0005 = 1513115
    h0031B1_0006 = 1513116
    h0031B1_0007 = 1513117
    h0031B1_0008 = 1513118
    h0031B1_0009 = 1513119
    h0031B1_0010 = 1513120
    h0031B1_0011 = 1513121
    h0031B1_0012 = 1513122
    h0031B1_0013 = 1513123
    h0031B1_0014 = 1513124
    h0031B1_0015 = 1513125
    h0031B1_0016 = 1513126
    h0031B1_0017 = 1513127
    h0031B1_0018 = 1513128
    h0031B1_0019 = 1513129
    h0031B1_0020 = 1513130
    h0032B1_0000 = 1513102
    h0050B1_0000 = 1513131
    h9000B1_0000 = 1513310


class Sounds(SoundEvent):
    """`SoundEvent` entity IDs for MSB and EVS use."""

    # noinspection PyMethodParameters
    def _generate_next_value_(name, _, count, __):
        return SoundEvent.auto_generate(count, DARK_SOULS_DSR, 1510000)

    GwyndolinMusic = 1513802
    GwynevereMusic = 1513801
    OrnsteinSmoughMusic = 1513800


class VFX(VFXEvent):
    """`VFXEvent` entity IDs for MSB and EVS use."""

    # noinspection PyMethodParameters
    def _generate_next_value_(name, _, count, __):
        return VFXEvent.auto_generate(count, DARK_SOULS_DSR, 1510000)

    CheckpointFog1 = 1511701
    CheckpointFog2 = 1511703
    GwyndolinEntranceFog1 = 1511891
    GwyndolinEntranceFog2 = 1511893
    LautrecInvasionFog1 = 1511751
    LautrecInvasionFog2 = 1511753
    LautrecInvasionFog3 = 1511755
    MultiplayerFog1 = 1511995
    OrnsteinSmoughEntranceFog1 = 1511991
    OrnsteinSmoughExitFog1 = 1511993
    OrnsteinSmoughExitFog2 = 1511989


class SpawnPoints(SpawnPointEvent):
    """`SpawnPointEvent` entity IDs for MSB and EVS use."""

    # noinspection PyMethodParameters
    def _generate_next_value_(name, _, count, __):
        return SpawnPointEvent.auto_generate(count, DARK_SOULS_DSR, 1510000)

    SpawnPoint0 = 1512960
    SpawnPoint1 = 1512961
    SpawnPoint2 = 1512962
    SpawnPointAtBoss = 1512950
    SpawnPointFromPaintedWorld = 1512501


class Navigation(NavigationEvent):
    """`NavigationEvent` entity IDs for MSB and EVS use."""

    # noinspection PyMethodParameters
    def _generate_next_value_(name, _, count, __):
        return NavigationEvent.auto_generate(count, DARK_SOULS_DSR, 1510000)

    Navmesh_Door00 = 1513250
    Navmesh_Door01 = 1513251
    Navmesh_Door02 = 1513252
    Navmesh_Door03 = 1513253
    Navmesh_Door04 = 1513254
    Navmesh_Door05 = 1513255
    Navmesh_Door06 = 1513256
    Navmesh_Door07 = 1513257
    Navmesh_Door08 = 1513258
    Navmesh_Door09 = 1513259
    Navmesh_GardenGate = 1513200
    Navmesh_RotatingBridge00 = 1513350
    Navmesh_RotatingBridge01 = 1513351
    Navmesh_RotatingBridge02 = 1513352
    Navmesh_RotatingBridge03 = 1513353
    Navmesh_RotatingBridge04 = 1513354


class Points(RegionPoint):
    """`RegionPoint` entity IDs for MSB and EVS use."""

    # noinspection PyMethodParameters
    def _generate_next_value_(name, _, count, __):
        return RegionPoint.auto_generate(count, DARK_SOULS_DSR, 1510000)

    SolaireSummonSign = 1512001


class Spheres(RegionSphere):
    """`RegionSphere` entity IDs for MSB and EVS use."""

    # noinspection PyMethodParameters
    def _generate_next_value_(name, _, count, __):
        return RegionSphere.auto_generate(count, DARK_SOULS_DSR, 1510000)

    GwyndolinInitialPosition = 1512705
    GwyndolinWarpPoint00 = 1512710
    GwyndolinWarpPoint01 = 1512711
    GwyndolinWarpPoint02 = 1512712
    GwyndolinWarpPoint03 = 1512713
    GwyndolinWarpPoint04 = 1512714
    GwyndolinWarpPoint05 = 1512715
    GwyndolinWarpPoint06 = 1512716
    GwyndolinWarpPoint07 = 1512717
    GwyndolinWarpPoint08 = 1512718
    GwyndolinWarpPoint09 = 1512719
    GwyndolinWarpPoint10 = 1512720
    GwyndolinWarpPoint11 = 1512721
    GwyndolinWarpPoint12 = 1512722
    GwyndolinWarpPoint13 = 1512723
    GwyndolinWarpPoint14 = 1512724
    GwyndolinWarpPoint15 = 1512725
    GwyndolinWarpPoint16 = 1512726
    GwyndolinWarpPoint17 = 1512727
    GwyndolinWarpPoint18 = 1512728
    GwyndolinWarpPoint19 = 1512729
    GwyndolinWarpPoint20 = 1512730
    GwyndolinWarpPoint21 = 1512731
    GwyndolinWarpPoint22 = 1512732
    GwyndolinWarpPoint23 = 1512733
    GwyndolinWarpPoint24 = 1512734
    GwyndolinWarpPoint25 = 1512735
    GwyndolinWarpPoint26 = 1512736
    GwyndolinWarpPoint27 = 1512737
    GwyndolinWarpPoint28 = 1512738
    GwyndolinWarpPoint29 = 1512739
    LautrecAggroTrigger = 1512100
    RotatingBridgeFirstUse = 1512350


class Boxes(RegionBox):
    """`RegionBox` entity IDs for MSB and EVS use."""

    # noinspection PyMethodParameters
    def _generate_next_value_(name, _, count, __):
        return RegionBox.auto_generate(count, DARK_SOULS_DSR, 1510000)

    AnorLondoPalaceArea = 1512400
    ArriveFromPaintedWorld = 1512500
    CannotOpenPalaceGate = 1512000
    CheckpointFog1BackSide = 1512601
    CheckpointFog1FrontSide = 1512600
    CheckpointFog2BackSide = 1512603
    CheckpointFog2FrontSide = 1512602
    DarkmoonKnightArea = 1512450
    Door01_Outside = 1512250
    Door01_Inside = 1512251
    Door07_Outside = 1512252
    Door07_Inside = 1512253
    Door08_Outside = 1512254
    Door08_Inside = 1512255
    GargoyleRetreat0 = 1512790
    GargoyleRetreat1 = 1512791
    GargoyleRetreat2 = 1512792
    GiantBlacksmithCombatArea = 1512750
    GwyndolinBloodstainMoveDestination = 1512421
    GwyndolinBloodstainMoveSource = 1512420
    GwyndolinCombatStart = 1512896
    GwyndolinCorridor = 1512801
    GwyndolinFogPrompt = 1512898
    GwyndolinFogPromptClient = 1512901
    GwyndolinFogRotationTarget = 1512897
    GwyndolinInfiniteCorridorWarpPoint = 1512900
    GwyndolinKneelPrompt = 1512410
    GwyndolinMusic = 1512890
    GwynevereKneelPrompt = 1512411
    GwynevereMusic = 1512800
    InvaderSpawn00 = 1514000
    InvaderSpawn10 = 1514010
    InvaderSpawn11 = 1514011
    InvaderSpawn20 = 1514020
    InvaderSpawn21 = 1514021
    InvaderSpawn22 = 1514022
    LautrecBlackEyeOrbTrigger = 1512101
    MimicNest1 = 1512010
    MimicNest2 = 1512011
    MimicNest3 = 1512012
    MimicNest4 = 1512013
    NoSignZone = 1512795
    OrnsteinSmoughCombatStart = 1512996
    OrnsteinSmoughFogPrompt = 1512998
    OrnsteinSmoughFogRotationTarget = 1512997
    OrnsteinSmoughMusic = 1512990
    PaintedWorldPrompt = 1512510
    PaintingGuardianAmbushTrigger = 1512050
    PlayerPointAfterOrnsteinSmoughPhaseTwo = 1512850
    RotatingBridgeCutsceneTrigger = 1512310
    RotatingBridgeWarpPoint1 = 1512301
    RotatingBridgeWarpPoint2 = 1512302
    RotatingBridgeWarpPoint3 = 1512303
    SentinelsRetreat = 1512780
    SilverKnightDriveReactionArea = 1512060
    SolaireProhibitedFromTomb = 1512770
    SolaireSummonActivityArea = 1512995
    SolaireSummonNest = 1512002
    TitaniteDemonMeleeCombatArea = 1512760
    TitaniteDemonRangedCombatArea = 1512761
    WyvernAttackTarget = 1512700
    WyvernPlungeTarget = 1512701
    c5351Area1 = 1512702
    c5351Area2 = 1512703
