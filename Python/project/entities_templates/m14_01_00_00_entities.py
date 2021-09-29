from soulstruct.games import DARK_SOULS_DSR
from soulstruct.game_types import *


class Objects(Object):
    """`Object` entity IDs for MSB and EVS use."""

    # noinspection PyMethodParameters
    def _generate_next_value_(name, _, count, __):
        return Object.auto_generate(count, DARK_SOULS_DSR, 1410000)

    o0110_0000 = 1411650
    o0110_0001 = 1411651
    o0110_0002 = 1411652
    o0110_0003 = 1411653
    o0200_0001 = 1411961
    o0200_0002 = 1411962
    o0200_0003 = 1411950
    o0200_0004 = 1411960
    o0200_0005 = 1411963
    o0200_0006 = 1411964
    o0500_0000 = 1411600
    o0500_0005 = 1411610
    o4450_0000 = 1411110
    o4500_0000 = 1411100
    o4510_0000 = 1411360
    o4600_0000 = 1411400
    o4610_0000 = 1411121
    o4610_0001 = 1411122
    o4620_0000 = 1411210
    o4621_0000 = 1411211
    o4622_0000 = 1411212
    o4623_0000 = 1411213
    o4624_0000 = 1411214
    o4625_0000 = 1411215
    o4626_0000 = 1411216
    o4627_0000 = 1411217
    o4628_0000 = 1411218
    o4629_0000 = 1411219
    o4630_0000 = 1411220
    o4631_0000 = 1411221
    o4632_0000 = 1411222
    o4633_0000 = 1411200
    o4634_0000 = 1411201
    o4635_0000 = 1411202
    o4636_0000 = 1411203
    o4637_0000 = 1411204
    o4700_0000 = 1411340
    o4800_0000 = 1411300
    o4810_0000 = 1411350
    o4810_0001 = 1411351
    o4840_0000 = 1411250
    o4840_0001 = 1411251
    o4840_0002 = 1411252
    o4840_0003 = 1411253
    o4840_0004 = 1411254
    o4840_0005 = 1411255
    o4840_0006 = 1411256
    o4840_0007 = 1411257
    o4840_0008 = 1411258
    o4840_0009 = 1411259
    o4840_0010 = 1411260
    o4840_0011 = 1411261
    o4840_0012 = 1411262
    o4840_0013 = 1411263
    o4840_0014 = 1411264
    o4840_0015 = 1411265
    o4840_0016 = 1411266
    o4840_0017 = 1411267
    o4840_0018 = 1411268
    o4840_0019 = 1411269
    o4840_0020 = 1411270
    o4840_0021 = 1411271
    o4840_0022 = 1411272
    o4840_0023 = 1411273
    o4840_0024 = 1411274
    o4840_0025 = 1411275
    o4840_0026 = 1411276
    o4840_0027 = 1411277
    o4840_0028 = 1411278
    o4840_0029 = 1411279
    o4840_0030 = 1411280
    o4840_0031 = 1411281
    o4840_0032 = 1411282
    o4840_0033 = 1411283
    o4840_0034 = 1411284
    o4840_0035 = 1411285
    o4840_0036 = 1411286
    o4840_0037 = 1411287
    o4840_0038 = 1411288
    o4840_0039 = 1411289
    o4840_0040 = 1411290
    o4840_0041 = 1411291
    o4840_0042 = 1411292
    o4840_0043 = 1411293
    o4840_0044 = 1411294
    o4840_0045 = 1411295
    o4840_0046 = 1411296
    o4840_0047 = 1411297
    o4960_0000 = 1411710
    o4961_0000 = 1411790
    o4962_0000 = 1411410
    o4963_0000 = 1411412
    o4964_0000 = 1411890
    o4965_0000 = 1411892
    o4966_0000 = 1411994
    o4967_0000 = 1411996
    o4968_0000 = 1411998
    o4969_0000 = 1411988
    o4970_0000 = 1411986
    o4971_0000 = 1411984
    o4972_0000 = 1411990
    o4973_0000 = 1411982


class Characters(Character):
    """`Character` entity IDs for MSB and EVS use."""

    # noinspection PyMethodParameters
    def _generate_next_value_(name, _, count, __):
        return Character.auto_generate(count, DARK_SOULS_DSR, 1410000)

    c0000_0002 = 6002
    c0000_0003 = 6004
    c0000_0005 = 6286
    c0000_0007 = 6542
    c0000_0008 = 6560
    c0000_0009 = 6561
    c0000_0010 = 6620
    c0000_PatchesAmbush = 7990
    c1000_0001 = 1410961
    c1000_0002 = 1410962
    c1000_0003 = 1410950
    c1000_0004 = 1410960
    c1000_0005 = 1410963
    c1000_0006 = 1410964
    c2231_0000 = 1410400
    c2240_0007 = 1410900
    c2240_0008 = 1410901
    c2240_0009 = 1410902
    c2240_0010 = 1410903
    c2240_0011 = 1410904
    c2250_0003 = 1410450
    c2250_0004 = 1410451
    c2250_0005 = 1410452
    c2250_0006 = 1410453
    c2250_0007 = 1410454
    c2250_0008 = 1410455
    c2250_0009 = 1410456
    c2370_TrollChanneler = 7970
    c2300_0000 = 1310150
    c3210_0000 = 1410200
    c3210_0001 = 1410201
    c3210_0002 = 1410202
    c3210_0003 = 1410203
    c3210_0004 = 1410204
    c3210_0005 = 1410205
    c3210_0006 = 1410206
    c3210_0007 = 1410207
    c3210_0008 = 1410208
    c3210_0009 = 1410209
    c3210_0010 = 1410210
    c3210_0011 = 1410211
    c3210_0012 = 1410212
    c3210_0013 = 1410213
    c3220_0000 = 1410220
    c3220_0001 = 1410221
    c3220_0002 = 1410222
    c3220_0003 = 1410223
    c3220_0004 = 1410224
    c3220_0005 = 1410225
    c3220_0006 = 1410226
    c3220_0007 = 1410227
    c3220_0008 = 1410228
    c3220_0009 = 1410229
    c3220_0010 = 1410230
    c3220_0011 = 1410231
    c3220_0012 = 1410232
    c3220_0013 = 1410233
    c3220_0014 = 1410234
    c3220_0015 = 1410235
    c3220_0016 = 1410236
    c3220_0017 = 1410237
    c3220_0018 = 1410238
    c3220_0019 = 1410239
    c3220_0020 = 1410240
    c3220_0021 = 1410241
    c3220_0022 = 1410242
    c3220_0023 = 1410243
    c3220_0024 = 1410244
    c3220_0025 = 1410245
    c3220_0026 = 1410246
    c3220_0027 = 1410247
    c3220_0028 = 1410248
    c3220_0029 = 1410249
    c3220_0030 = 1410250
    c3220_0031 = 1410251
    c3220_0032 = 1410252
    c3220_0033 = 1410253
    c3220_0034 = 1410254
    c3220_0035 = 1410255
    c3220_0036 = 1410256
    c3220_0037 = 1410257
    c3220_0038 = 1410258
    c3220_0039 = 1410259
    c3220_0040 = 1410260
    c3220_0041 = 1410261
    c3220_0042 = 1410262
    c3220_0043 = 1410263
    c3220_0044 = 1410264
    c3220_0045 = 1410265
    c3220_0046 = 1410266
    c3220_0047 = 1410267
    c3220_0048 = 1410268
    c3220_0049 = 1410269
    c3220_0050 = 1410270
    c3220_0051 = 1410271
    c3220_0052 = 1410272
    c3220_0053 = 1410273
    c3220_0054 = 1410274
    c3220_0055 = 1410275
    c3220_0056 = 1410276
    c3220_0057 = 1410277
    c3220_0058 = 1410278
    c3220_0059 = 1410279
    c3220_0060 = 1410280
    c3220_0061 = 1410281
    c3220_0062 = 1410282
    c3220_0063 = 1410283
    c3220_0064 = 1410284
    c3220_0065 = 1410285
    c3220_0066 = 1410286
    c3220_0067 = 1410287
    c3220_0068 = 1410288
    c3220_0069 = 1410289
    c3240_0002 = 1410410
    c3240_0003 = 1410411
    c3240_0004 = 1410412
    c3240_0005 = 1410413
    c3240_0009 = 1410905
    c3240_0010 = 1410906
    c3240_0011 = 1410907
    c3300_0000 = 1410110
    c3390_0001 = 1410301
    c3390_0002 = 1410302
    c3390_0003 = 1410303
    c3390_0004 = 1410304
    c3390_0005 = 1410305
    c3390_0006 = 1410306
    c3390_0007 = 1410307
    c3421_0000 = 1410350
    c3421_0001 = 1410351
    c3421_0002 = 1410352
    c3421_0003 = 1410353
    c3421_0004 = 1410354
    c3421_0005 = 1410355
    c3421_0006 = 1410356
    c3421_0007 = 1410357
    c3421_0008 = 1410358
    c3421_0009 = 1410359
    c3421_0010 = 1410360
    c3421_0011 = 1410361
    c3421_0012 = 1410362
    c3421_0013 = 1410363
    c3421_0014 = 1410364
    c3421_0015 = 1410365
    c3421_0016 = 1410366
    c3421_0017 = 1410367
    c3421_0018 = 1410368
    c3421_0019 = 1410369
    c3421_0020 = 1410370
    c3421_0021 = 1410371
    c3421_0022 = 1410372
    c3421_0023 = 1410373
    c3421_0024 = 1410374
    c3421_0025 = 1410375
    c3421_0026 = 1410376
    c3421_0027 = 1410377
    c3421_0028 = 1410378
    c3480_0000 = 1410100
    c3490_0000 = 1413900
    c3490_0001 = 1413910
    c3490_0002 = 1413920
    c3490_0003 = 1413930
    c3491_0000 = 1413901
    c3491_0001 = 1413911
    c3491_0002 = 1413921
    c3491_0003 = 1413902
    c3491_0004 = 1413931
    c3491_0005 = 1413912
    c3491_0006 = 1413922
    c3491_0007 = 1413932
    c5200_0000 = 1410700
    c5201_0000 = 1410710
    c5201_0001 = 1410711
    c5201_0002 = 1410712
    c5201_0003 = 1410713
    c5201_0004 = 1410714
    c5202_0000 = 1410720
    c5202_0001 = 1410721
    c5202_0002 = 1410722
    c5202_0003 = 1410723
    c5202_0004 = 1410724
    c5230_0000 = 1410801
    c5250_0000 = 1410600
    c5400_0000 = 1410800
    c5401_0000 = 1410802


class PlayerStarts(PlayerStart):
    """`PlayerStart` entity IDs for MSB and EVS use."""

    # noinspection PyMethodParameters
    def _generate_next_value_(name, _, count, __):
        return PlayerStart.auto_generate(count, DARK_SOULS_DSR, 1410000)

    c0000_0001 = 1410998
    c0000_0006 = 1410980


class Collisions(Collision):
    """`Collision` entity IDs for MSB and EVS use."""

    # noinspection PyMethodParameters
    def _generate_next_value_(name, _, count, __):
        return Collision.auto_generate(count, DARK_SOULS_DSR, 1410000)

    h0008B1 = 1413100
    h0042B1 = 1413000
    h1008B1 = 1413101
    h4300B1 = 1413200


class Sounds(SoundEvent):
    """`SoundEvent` entity IDs for MSB and EVS use."""

    # noinspection PyMethodParameters
    def _generate_next_value_(name, _, count, __):
        return SoundEvent.auto_generate(count, DARK_SOULS_DSR, 1410000)

    BedOfChaosBossMusic = 1413800
    CeaselessDischargeMusic = 1413801
    CentipedeDemonMusic = 1413802
    EggPrayerSound = 1413806
    FiresageDemonMusic = 1413803
    LavaSound = 1413805


class VFX(VFXEvent):
    """`VFXEvent` entity IDs for MSB and EVS use."""

    # noinspection PyMethodParameters
    def _generate_next_value_(name, _, count, __):
        return VFXEvent.auto_generate(count, DARK_SOULS_DSR, 1410000)

    BedOfChaosEntranceFog = 1411991
    BedSealLeft = 1413401
    BedSealRight = 1413400
    BedSealRootLeft = 1413410
    BedSealRootRight = 1413411
    CeaselessEntranceFog = 1411791
    CentipedeEntranceFog = 1411891
    CentipedeExitFog = 1411893
    FiresageEntranceFog = 1411411
    FiresageExitFog = 1411413
    GoldenFog = 1411711
    MultiplayerFog1 = 1411995
    MultiplayerFog2 = 1411997
    MultiplayerFog3 = 1411999
    MultiplayerFog4 = 1411989
    MultiplayerFog5 = 1411987
    MultiplayerFog6 = 1411985
    MultiplayerFog7 = 1411983


class SpawnPoints(SpawnPointEvent):
    """`SpawnPointEvent` entity IDs for MSB and EVS use."""

    # noinspection PyMethodParameters
    def _generate_next_value_(name, _, count, __):
        return SpawnPointEvent.auto_generate(count, DARK_SOULS_DSR, 1410000)

    SpawnPoint1 = 1412961
    SpawnPoint2 = 1412962
    SpawnPoint3 = 1412950
    SpawnPoint4 = 1412960
    SpawnPoint5 = 1412963
    SpawnPoint6 = 1412964


class Points(RegionPoint):
    """`RegionPoint` entity IDs for MSB and EVS use."""

    # noinspection PyMethodParameters
    def _generate_next_value_(name, _, count, __):
        return RegionPoint.auto_generate(count, DARK_SOULS_DSR, 1410000)

    KirkInvaderSpawn1 = 1412001
    KirkInvaderSpawn2 = 1412002
    SolaireSummonSign = 1412000


class Spheres(RegionSphere):
    """`RegionSphere` entity IDs for MSB and EVS use."""

    # noinspection PyMethodParameters
    def _generate_next_value_(name, _, count, __):
        return RegionSphere.auto_generate(count, DARK_SOULS_DSR, 1410000)

    BedCentralFloorBreakTrigger = 1412100
    BedOfChaosMusic = 1412990
    CeaselessA00 = 1412700
    CeaselessA01 = 1412701
    CeaselessA02 = 1412702
    CeaselessA03 = 1412703
    CeaselessA04 = 1412704
    CeaselessA05 = 1412705
    CeaselessA06 = 1412706
    CeaselessA07 = 1412710
    CeaselessA08 = 1412711
    CeaselessA09 = 1412712
    CeaselessA10 = 1412713
    CeaselessA11 = 1412714
    CeaselessA12 = 1412720
    CeaselessC01 = 1412730
    CeaselessPostClingSnap = 1412798
    CeaselessPreClingSnap = 1412797
    PlayerHasEnteredIzalith = 1412510
    ShortcutElevatorStartFromBottom = 1412403
    ShortcutElevatorStartFromTop = 1412402
    ShortcutElevatorSummonFromBottom = 1412401
    ShortcutElevatorSummonFromTop = 1412400
    UnusedCeaselessPoint1 = 1412721
    UnusedCeaselessPoint2 = 1412722
    UnusedCeaselessPoint3 = 1412723
    UnusedCeaselessPoint4 = 1412724


class Boxes(RegionBox):
    """`RegionBox` entity IDs for MSB and EVS use."""

    # noinspection PyMethodParameters
    def _generate_next_value_(name, _, count, __):
        return RegionBox.auto_generate(count, DARK_SOULS_DSR, 1410000)

    AtGoldenFog = 1412660
    BedCombatArea0 = 1412820
    BedCombatArea1 = 1412830
    BedCombatArea2 = 1412840
    BedFogPrompt = 1412998
    BedFogRotationTarget = 1412997
    BedLowerBody_a3000 = 1412550
    BedLowerBody_a3001 = 1412552
    BedLowerBody_a3002 = 1412554
    BedLowerBody_a3003 = 1412555
    BedLowerBody_a3004_0 = 1412556
    BedLowerBody_a3004_1 = 1412557
    BedLowerBody_a3005_0 = 1412560
    BedLowerBody_a3005_1 = 1412561
    BedLowerBody_a3006 = 1412564
    BedOfChaosArea0 = 1412600
    BedOfChaosArea1 = 1412601
    BedOfChaosArea2 = 1412602
    BedOfChaosArea3 = 1412603
    BedOfChaosArea4 = 1412604
    BedOfChaosArea5 = 1412605
    BedOfChaosArea6 = 1412606
    BedOfChaosArea7 = 1412607
    BedOfChaosArea8 = 1412608
    BedOfChaosArea9 = 1412609
    BedOfChaosArea10 = 1412610
    BedOfChaosArea11 = 1412611
    BedOfChaosArea12 = 1412612
    BedOfChaosArea13 = 1412613
    BedOfChaosArea14 = 1412614
    BedOfChaosArea15 = 1412615
    BedOfChaosArea16 = 1412616
    BedOfChaosArea17 = 1412617
    BedOfChaosArea18 = 1412618
    BedOfChaosArea19 = 1412619
    BedOfChaosArea20 = 1412620
    BedOfChaosArea21 = 1412621
    BedOfChaosArea22 = 1412622
    BedOfChaosArea23 = 1412623
    BedOfChaosArea24 = 1412624
    BedOfChaosArea25 = 1412625
    BedOfChaosArea26 = 1412626
    BedOfChaosArea27 = 1412627
    BedOfChaosArea28 = 1412628
    BedOfChaosNotify = 1412996
    BedSlide = 1413300
    BedSlideInvincibility = 1412110
    BedUpperBody_a3006 = 1412570
    BedUpperBody_a3007 = 1412572
    BedUpperBody_a3008 = 1412576
    BedUpperBody_a3009 = 1412580
    BedUpperBody_a3010 = 1412584
    BedUpperBody_a3011 = 1412588
    CeaselessAltarArea = 1412796
    CeaselessClings = 1412799
    CeaselessDischargeMusic = 1412690
    CeaselessFogArea = 1412780
    CeaselessFogPrompt = 1412698
    CeaselessFogRotationTarget = 1412697
    CeaselessLowerArea = 1412791
    CeaselessNarrowArea1 = 1412795
    CeaselessNarrowArea2 = 1412794
    CeaselessNotify = 1412696
    CeaselessUpperArea = 1412790
    CeilingRockwormTrigger = 1412302
    CentipedeCombatStart = 1412896
    CentipedeDemonMusic = 1412890
    CentipedeFogPrompt = 1412898
    CentipedeFogRotationTarget = 1412897
    FiresageDemonCombatStart = 1412416
    FiresageDemonFogPrompt = 1412411
    FiresageDemonFogRotationTarget = 1412412
    FiresageDemonMusic = 1412410
    InvaderSpawn000 = 1414000
    InvaderSpawn100 = 1414100
    InvaderSpawn200 = 1414200
    InvaderSpawn300 = 1414300
    InvaderSpawn301 = 1414301
    IzalithShortcutGateBackPrompt = 1412200
    IzalithShortcutGateFrontPrompt = 1412201
    KirkInvaderTrigger1 = 1412010
    KirkInvaderTrigger2 = 1412520
    LavaSound = 1412800
    PlayerInLavaField = 1412530
    RockwormAmbushTrigger1 = 1412300
    RockwormAmbushTrigger2 = 1412301
    SewerFloorBreakTrigger = 1412350
    SiegmeyerNestAfterBattle = 1412360
    SolaireSaved = 1412500
    TitaniteDemonMeleeArea = 1412740
    TitaniteDemonRangedArea1 = 1412741
    TitaniteDemonRangedArea2 = 1412742
    UnusedRockwormDigTrigger1 = 1412312
    UnusedRockwormDigTrigger2 = 1412313
    UnusedRockwormHolePoint = 1412314
    UnusedRockwormMeleeCombatArea = 1412310
    UnusedRockwormRangedCombatArea = 1412311
    UnusedRockwormWallTrigger_a3000 = 1412315
    UnusedRockwormWallTrigger_a3001_0 = 1412316
    UnusedRockwormWallTrigger_a3001_1 = 1412317
    UnusedRockwormWallTrigger_a3004 = 1412318
