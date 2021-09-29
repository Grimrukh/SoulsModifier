from soulstruct.games import DARK_SOULS_DSR
from soulstruct.game_types import *


class Flags(Flag):
    SurpriseManusFightActive = 11215028  # bonfire does not spawn


class Objects(Object):
    """`Object` entity IDs for MSB and EVS use."""

    # noinspection PyMethodParameters
    def _generate_next_value_(name, _, count, __):
        return Object.auto_generate(count, DARK_SOULS_DSR, 1210000)

    o0110_0000 = 1211600
    o0110_0001 = 1211601
    o0110_0002 = 1211602
    o0110_0004 = 1211604
    o0110_0005 = 1211605
    o0110_0006 = 1211606
    o0110_0007 = 1211607
    o0200_0000 = 1211963
    o0200_0001 = 1211961
    o0200_0002 = 1211962
    o0200_0003 = 1211950
    o0200_0004 = 1211964
    o0200_0005 = 1211666
    o0200_0200 = 1211512
    o0200_0201 = 1211511
    o0200_0202 = 1211510
    o0200_0210 = 1211515
    o0200_0211 = 1211514
    o0200_0212 = 1211513
    o0500_0100 = 1211650
    o2253 = 1211130
    o2402 = 1211110
    o2610_0000 = 1211300
    o2610_0001 = 1211301
    o2610_0002 = 1211302
    o2611_0000 = 1211303
    o2611_0001 = 1211304
    o2611_0002 = 1211305
    o2611_0003 = 1211306
    o2611_0004 = 1211307
    o2611_0005 = 1211308
    o2612_0000 = 1211309
    o2612_0001 = 1211310
    o2612_0002 = 1211311
    o2612_0003 = 1211312
    o2612_0004 = 1211313
    o2612_0005 = 1211314
    o2613_0000 = 1211315
    o2613_0001 = 1211316
    o2613_0002 = 1211317
    o2613_0003 = 1211318
    o2613_0004 = 1211319
    o2613_0005 = 1211320
    o2613_0006 = 1211321
    o2613_0007 = 1211322
    o2613_0008 = 1211323
    o2620_0000 = 1211240
    o2621_0000 = 1211250
    o2630_0000 = 1211230
    o2700_0000 = 1211000
    o2700_0001 = 1211010
    o2700_0002 = 1211020
    o2700_0003 = 1211030
    o2700_0004 = 1211040
    o2701_0000 = 1211002
    o2701_0001 = 1211012
    o2701_0002 = 1211022
    o2701_0003 = 1211032
    o2701_0004 = 1211042
    o2701_0010 = 1211001
    o2701_0011 = 1211011
    o2701_0012 = 1211021
    o2701_0013 = 1211031
    o2701_0014 = 1211041
    o2720_0000 = 1211120
    o2730_0000 = 1211200
    o2732_0000 = 1211201
    o2760_0000 = 1211220
    o2780_0000 = 1211520
    o2780_0001 = 1211521
    o2780_0002 = 1211522
    o2780_0003 = 1211523
    o2780_0010 = 1211530
    o2780_0011 = 1211531
    o2780_0012 = 1211532
    o2780_0013 = 1211533
    o2780_0020 = 1211540
    o2780_0021 = 1211541
    o2780_0022 = 1211542
    o2780_0023 = 1211543
    o2780_0100 = 1211550
    o2780_0101 = 1211551
    o2780_0102 = 1211552
    o2780_0103 = 1211553
    o2780_0110 = 1211560
    o2780_0111 = 1211561
    o2780_0112 = 1211562
    o2780_0113 = 1211563
    o2780_0120 = 1211570
    o2780_0121 = 1211571
    o2780_0122 = 1211572
    o2780_0123 = 1211573
    o2785_0000 = 1211420
    o2785_0001 = 1211421
    o2785_0002 = 1211422
    o2785_0003 = 1211423
    o2785_0010 = 1211430
    o2785_0011 = 1211431
    o2785_0012 = 1211432
    o2785_0013 = 1211433
    o2785_0020 = 1211440
    o2785_0021 = 1211441
    o2785_0022 = 1211442
    o2785_0023 = 1211443
    o2785_0100 = 1211450
    o2785_0101 = 1211451
    o2785_0102 = 1211452
    o2785_0103 = 1211453
    o2785_0110 = 1211460
    o2785_0111 = 1211461
    o2785_0112 = 1211462
    o2785_0113 = 1211463
    o2785_0120 = 1211470
    o2785_0121 = 1211471
    o2785_0122 = 1211472
    o2785_0123 = 1211473
    o2790_0000 = 1211111
    o2791_0000 = 1211112
    o2795_0000 = 1211210
    o2800_0000 = 1211100
    o2801_0000 = 1211101
    o2909_0001 = 1211790
    o2910_0001 = 1211792
    o2911_0001 = 1211990
    o2912_0001 = 1211988
    o2913 = 1211994
    o2914 = 1211996
    o2915_0000 = 1211890
    o2916_0000 = 1211892
    o2917_0000 = 1211998
    o2919_0000 = 1211690
    o2920_0000 = 1211986
    o2920_0001 = 1211900


class Characters(Character):
    """`Character` entity IDs for MSB and EVS use."""

    # noinspection PyMethodParameters
    def _generate_next_value_(name, _, count, __):
        return Character.auto_generate(count, DARK_SOULS_DSR, 1210000)

    c0000_0006 = 6700
    c0000_0013 = 6740
    c0000_PatchesAmbush = 7985
    c1000_0000 = 1210963
    c1000_0001 = 1210961
    c1000_0002 = 1210962
    c1000_0003 = 1210950
    c1000_0005 = 1210964
    c1000_0006 = 1210665
    c1000_0007 = 1210663
    c1000_0008 = 1210661
    c1000_0009 = 1210662
    c1000_0010 = 1210664
    c1000_0011 = 1210666
    c2370_TrollChanneler = 7965
    c2780_0000 = 1210600
    c2780_0001 = 1210601
    c3300_0000 = 1210200
    c3300_0001 = 1210201
    c3300_0002 = 1210202
    c3300_0003 = 1210203
    c3300_0004 = 1210204
    c3471_0000 = 1210800
    c3471_0001 = 1210801
    c3471_0002 = 1210802
    c3472_0000 = 1210810
    c3472_0001 = 1210811
    c3472_0002 = 1210812
    c3490_0000 = 1213900
    c3490_0001 = 1213910
    c3490_0002 = 1213920
    c3491_0000 = 1213901
    c3491_0001 = 1213911
    c3491_0002 = 1213921
    c3491_0003 = 1213902
    c3491_0004 = 1213912
    c3491_0005 = 1213922
    c4090_0000 = 6730
    c4090_0001 = 6731
    c4090_0002 = 6732
    c4100_0000 = 1210820
    c4110_0000 = 6720
    c4120_0004 = 1210150
    c4120_0007 = 1210151
    c4120_0011 = 1210900
    c4120_0012 = 1210901
    c4120_0013 = 1210902
    c4130_0016 = 1210100
    c4130_0017 = 1210104
    c4130_0019 = 1210105
    c4130_0020 = 1210103
    c4130_0022 = 1210101
    c4130_0023 = 1210102
    c4130_0025 = 1210106
    c4130_0027 = 1210107
    c4130_0039 = 1210905
    c4130_0040 = 1210906
    c4130_0041 = 1210907
    c4130_0042 = 1210908
    c4130_0046 = 1210912
    c4130_0047 = 1210913
    c4130_0048 = 1210914
    c4130_0049 = 1210915
    c4140_0000 = 6750
    c4150_0026 = 1210350
    c4150_0028 = 1210916
    c4150_0029 = 1210917
    c4150_0030 = 1210920
    c4160_0002 = 1210260
    c4160_0004 = 1210250
    c4160_0005 = 1210251
    c4160_0006 = 1210252
    c4160_0012 = 1210918
    c4160_0013 = 1210919
    c4160_0015 = 1210921
    c4170_0001 = 1210300
    c4170_0002 = 1210301
    c4170_0003 = 1210302
    c4171_0005 = 1210305
    c4172_0010 = 1210304
    c4172_0018 = 1210303
    c4180_0003 = 1210922
    c4180_0005 = 1210924
    c4180_0006 = 1210925
    c4500_0000 = 1210840
    c4510_0000 = 1210400
    c4510_0001 = 1210401
    c4510_0002 = 1210402
    c4511_0000 = 1210410
    c4520_0000 = 1210500
    c4520_0001 = 1210501
    c4520_0002 = 1210502
    c4531_0000 = 6760


class PlayerStarts(PlayerStart):
    """`PlayerStart` entity IDs for MSB and EVS use."""

    # noinspection PyMethodParameters
    def _generate_next_value_(name, _, count, __):
        return PlayerStart.auto_generate(count, DARK_SOULS_DSR, 1210000)

    c0000_0001 = 1210998
    c0000_0002 = 1210983
    c0000_0003 = 1210981
    c0000_0004 = 1210982
    c0000_0005 = 1210970
    c0000_0007 = 1218210
    c0000_0008 = 1218211
    c0000_0009 = 1218212
    c0000_0010 = 1218213
    c0000_0011 = 1218214
    c0000_0012 = 1218215
    c0000_0014 = 1218200
    c0000_0015 = 1210984
    c0000_ManusWarp = 1210980


class Collisions(Collision):
    """`Collision` entity IDs for MSB and EVS use."""

    # noinspection PyMethodParameters
    def _generate_next_value_(name, _, count, __):
        return Collision.auto_generate(count, DARK_SOULS_DSR, 1210000)

    h0018B1 = 1213009
    h0022B1 = 1213002
    h0023B1 = 1213003
    h0024B1 = 1213004
    h0025B1 = 1213005
    h0026B1 = 1213006
    h0027B1 = 1213007
    h0037B1 = 1213020
    h0066B1 = 1213000
    h0070B1 = 1213021
    h0095B1 = 1213060
    h0095B1_0000 = 1213061
    h0103B1 = 1213031
    h0105B1 = 1213030
    h0107B1 = 1213040
    h5000B1 = 1213200
    h5001B1 = 1213201
    h5002B1 = 1213202
    h5003B1 = 1213203
    h5010B1 = 1213210
    h5011B1 = 1213211
    h5012B1 = 1213212
    h5013B1 = 1213213
    h5020B1 = 1213220
    h5021B1 = 1213221
    h5022B1 = 1213222
    h5023B1 = 1213223
    h5030B1 = 1213230
    h5031B1 = 1213231
    h5032B1 = 1213232
    h5033B1 = 1213233
    h5040B1 = 1213240
    h5041B1 = 1213241
    h5042B1 = 1213242
    h5043B1 = 1213243
    h5050B1 = 1213250
    h5051B1 = 1213251
    h5052B1 = 1213252
    h5053B1 = 1213253
    h5100B1 = 1213300
    h5101B1 = 1213301
    h5102B1 = 1213302
    h5103B1 = 1213303
    h7400B1 = 1213001
    h7600B1 = 1213050
    h7601B1 = 1213051
    h7602B1 = 1213052
    h7603B1 = 1213053
    h7604B1 = 1213054


class Sounds(SoundEvent):
    """`SoundEvent` entity IDs for MSB and EVS use."""

    # noinspection PyMethodParameters
    def _generate_next_value_(name, _, count, __):
        return SoundEvent.auto_generate(count, DARK_SOULS_DSR, 1210000)

    ArtoriasMusic = 1213801
    KalameetMusic = 1213803
    LightIllusoryWallSound0 = 1213810
    LightIllusoryWallSound1 = 1213811
    ManusMusic = 1213802
    SanctuaryGuardianMusic = 1213800


class VFX(VFXEvent):
    """`VFXEvent` entity IDs for MSB and EVS use."""

    # noinspection PyMethodParameters
    def _generate_next_value_(name, _, count, __):
        return VFXEvent.auto_generate(count, DARK_SOULS_DSR, 1210000)

    Arena_BR_Searching_b_A = 1213422
    Arena_BR_Searching_b_B = 1213423
    Arena_BR_Searching_b_C = 1213424
    Arena_BR_Searching_b_D = 1213425
    Arena_BR_Searching_s_A = 1213409
    Arena_BR_Searching_s_B = 1213410
    Arena_BR_Searching_s_C = 1213411
    Arena_BR_Searching_s_D = 1213412
    Arena_TransferBonfire2 = 1212666
    Arena_Wanted_1vs1_b_A = 1213416
    Arena_Wanted_1vs1_b_B = 1213417
    Arena_Wanted_1vs1_s_A = 1213403
    Arena_Wanted_1vs1_s_B = 1213404
    Arena_Wanted_2vs2_b_A = 1213418
    Arena_Wanted_2vs2_b_B = 1213419
    Arena_Wanted_2vs2_b_C = 1213420
    Arena_Wanted_2vs2_b_D = 1213421
    Arena_Wanted_2vs2_s_A = 1213405
    Arena_Wanted_2vs2_s_B = 1213406
    Arena_Wanted_2vs2_s_C = 1213407
    Arena_Wanted_2vs2_s_D = 1213408
    ArtoriasEntranceFog = 1211891
    ArtoriasExitFog = 1211893
    ChesterCandlestick = 1213150
    IllusoryFloorLandingAura = 1213125
    KalameetEntranceFog = 1211691
    ManusEntranceFog = 1211991
    ManusRock_o2610_0 = 1213160
    ManusRock_o2610_1 = 1213161
    ManusRock_o2610_2 = 1213162
    ManusRock_o2611_0 = 1213163
    ManusRock_o2611_1 = 1213164
    ManusRock_o2611_2 = 1213165
    ManusRock_o2611_3 = 1213166
    ManusRock_o2611_4 = 1213167
    ManusRock_o2611_5 = 1213168
    ManusRock_o2612_0 = 1213169
    ManusRock_o2612_1 = 1213170
    ManusRock_o2612_2 = 1213171
    ManusRock_o2612_3 = 1213172
    ManusRock_o2612_4 = 1213173
    ManusRock_o2612_5 = 1213174
    ManusRock_o2613_0 = 1213175
    ManusRock_o2613_1 = 1213176
    ManusRock_o2613_2 = 1213177
    ManusRock_o2613_3 = 1213178
    ManusRock_o2613_4 = 1213179
    ManusRock_o2613_5 = 1213180
    ManusRock_o2613_6 = 1213181
    ManusRock_o2613_7 = 1213182
    ManusRock_o2613_8 = 1213183
    MultiplayerFog1 = 1211995
    MultiplayerFog2 = 1211997
    MultiplayerFog3 = 1211999
    MultiplayerFog4 = 1211989
    MultiplayerFog5 = 1211987
    MultiplayerFog6 = 1211901
    SanctuaryGuardianEntranceFog = 1211791
    SanctuaryGuardianExitFog = 1211793
    SifBarrier = 1213110
    SifSummonSign = 1213100


class SpawnPoints(SpawnPointEvent):
    """`SpawnPointEvent` entity IDs for MSB and EVS use."""

    # noinspection PyMethodParameters
    def _generate_next_value_(name, _, count, __):
        return SpawnPointEvent.auto_generate(count, DARK_SOULS_DSR, 1210000)

    Arena_ReturnPoint_1vs1_Narrow = 1218201
    Arena_ReturnPoint_1vs1_Wide = 1218202
    Arena_ReturnPoint_2vs2_Narrow = 1218203
    Arena_ReturnPoint_2vs2_Wide = 1218204
    Arena_ReturnPoint_BR_Narrow = 1218205
    Arena_ReturnPoint_BR_Wide = 1218206
    Arena_ReturnPoint_RankingBoard = 1218146
    SpawnPoint0 = 1212963
    SpawnPoint1 = 1212961
    SpawnPoint2 = 1212962
    SpawnPoint3 = 1212950
    SpawnPoint4 = 1212964


class Navigation(NavigationEvent):
    """`NavigationEvent` entity IDs for MSB and EVS use."""

    # noinspection PyMethodParameters
    def _generate_next_value_(name, _, count, __):
        return NavigationEvent.auto_generate(count, DARK_SOULS_DSR, 1210000)

    Navmesh_Door0 = 1213500


class Points(RegionPoint):
    """`RegionPoint` entity IDs for MSB and EVS use."""

    # noinspection PyMethodParameters
    def _generate_next_value_(name, _, count, __):
        return RegionPoint.auto_generate(count, DARK_SOULS_DSR, 1210000)

    Arena_FogGate = 1219800
    Arena_FogTurn = 1219003
    Arena_Spawn_2v2Big00 = 1215100
    Arena_Spawn_2v2Big01 = 1215101
    Arena_Spawn_2v2Big02 = 1215102
    Arena_Spawn_2v2Big03 = 1215103
    Arena_Spawn_2v2Big04 = 1215104
    Arena_Spawn_2v2Big05 = 1215105
    Arena_Spawn_2v2Big06 = 1215106
    Arena_Spawn_2v2Big07 = 1215107
    Arena_Spawn_2v2Big08 = 1215108
    Arena_Spawn_2v2Big09 = 1215109
    Arena_Spawn_2v2Big10 = 1215110
    Arena_Spawn_2v2Big11 = 1215111
    Arena_Spawn_2v2Big12 = 1215112
    Arena_Spawn_2v2Big13 = 1215113
    Arena_Spawn_2v2Big14 = 1215114
    Arena_Spawn_2v2Big15 = 1215115
    Arena_Spawn_2v2Big16 = 1215116
    Arena_Spawn_2v2Big17 = 1215117
    Arena_Spawn_2v2Big19 = 1215119
    Arena_Spawn_2v2Big21 = 1215121
    Arena_Spawn_2v2Big22 = 1215122
    Arena_Spawn_2v2Big23 = 1215123
    Arena_Spawn_2v2Big25 = 1215125
    Arena_Spawn_2v2Big27 = 1215127
    Arena_Spawn_2v2Big28 = 1215128
    Arena_Spawn_2v2Big29 = 1215129
    Arena_Spawn_2v2Big30 = 1215130
    Arena_Spawn_2v2Big31 = 1215131
    Arena_Spawn_2v2Big32 = 1215132
    Arena_Spawn_2v2Big33 = 1215133
    Arena_Spawn_2v2BigInitial0 = 1215118
    Arena_Spawn_2v2BigInitial1 = 1215120
    Arena_Spawn_2v2BigInitial2 = 1215124
    Arena_Spawn_2v2BigInitial3 = 1215126
    Arena_Spawn_2v2Small04 = 1215604
    Arena_Spawn_2v2Small05 = 1215605
    Arena_Spawn_2v2Small06 = 1215606
    Arena_Spawn_2v2Small07 = 1215607
    Arena_Spawn_2v2Small08 = 1215608
    Arena_Spawn_2v2Small09 = 1215609
    Arena_Spawn_2v2Small10 = 1215610
    Arena_Spawn_2v2Small11 = 1215611
    Arena_Spawn_2v2Small12 = 1215612
    Arena_Spawn_2v2Small13 = 1215613
    Arena_Spawn_2v2Small14 = 1215614
    Arena_Spawn_2v2Small15 = 1215615
    Arena_Spawn_2v2Small16 = 1215616
    Arena_Spawn_2v2Small17 = 1215617
    Arena_Spawn_2v2Small18 = 1215618
    Arena_Spawn_2v2Small19 = 1215619
    Arena_Spawn_2v2Small20 = 1215620
    Arena_Spawn_2v2Small21 = 1215621
    Arena_Spawn_2v2Small22 = 1215622
    Arena_Spawn_2v2SmallInitial0 = 1215600
    Arena_Spawn_2v2SmallInitial1 = 1215601
    Arena_Spawn_2v2SmallInitial2 = 1215602
    Arena_Spawn_2v2SmallInitial3 = 1215603
    Arena_Spawn_3v3Big02 = 1215302
    Arena_Spawn_3v3Big03 = 1215303
    Arena_Spawn_3v3Big06 = 1215306
    Arena_Spawn_3v3Big07 = 1215307
    Arena_Spawn_3v3Big08 = 1215308
    Arena_Spawn_3v3Big09 = 1215309
    Arena_Spawn_3v3Big10 = 1215310
    Arena_Spawn_3v3Big11 = 1215311
    Arena_Spawn_3v3Big12 = 1215312
    Arena_Spawn_3v3Big13 = 1215313
    Arena_Spawn_3v3Big14 = 1215314
    Arena_Spawn_3v3Big15 = 1215315
    Arena_Spawn_3v3Big16 = 1215316
    Arena_Spawn_3v3Big17 = 1215317
    Arena_Spawn_3v3Big18 = 1215318
    Arena_Spawn_3v3Big19 = 1215319
    Arena_Spawn_3v3Big20 = 1215320
    Arena_Spawn_3v3Big21 = 1215321
    Arena_Spawn_3v3Big22 = 1215322
    Arena_Spawn_3v3Big23 = 1215323
    Arena_Spawn_3v3Big24 = 1215324
    Arena_Spawn_3v3Big25 = 1215325
    Arena_Spawn_3v3Big26 = 1215326
    Arena_Spawn_3v3Big27 = 1215327
    Arena_Spawn_3v3Big28 = 1215328
    Arena_Spawn_3v3Big29 = 1215329
    Arena_Spawn_3v3Big30 = 1215330
    Arena_Spawn_3v3Big31 = 1215331
    Arena_Spawn_3v3Big32 = 1215332
    Arena_Spawn_3v3Big33 = 1215333
    Arena_Spawn_3v3Big34 = 1215334
    Arena_Spawn_3v3Big35 = 1215335
    Arena_Spawn_3v3Big37 = 1215337
    Arena_Spawn_3v3Big38 = 1215338
    Arena_Spawn_3v3BigInitial0 = 1215300
    Arena_Spawn_3v3BigInitial1 = 1215301
    Arena_Spawn_3v3BigInitial2 = 1215304
    Arena_Spawn_3v3BigInitial3 = 1215305
    Arena_Spawn_3v3BigInitial4 = 1215336
    Arena_Spawn_3v3BigInitial5 = 1215339
    Arena_Spawn_3v3Small06 = 1215806
    Arena_Spawn_3v3Small07 = 1215807
    Arena_Spawn_3v3Small08 = 1215808
    Arena_Spawn_3v3Small09 = 1215809
    Arena_Spawn_3v3Small10 = 1215810
    Arena_Spawn_3v3Small11 = 1215811
    Arena_Spawn_3v3Small12 = 1215812
    Arena_Spawn_3v3Small13 = 1215813
    Arena_Spawn_3v3Small14 = 1215814
    Arena_Spawn_3v3Small15 = 1215815
    Arena_Spawn_3v3Small16 = 1215816
    Arena_Spawn_3v3Small17 = 1215817
    Arena_Spawn_3v3Small18 = 1215818
    Arena_Spawn_3v3Small19 = 1215819
    Arena_Spawn_3v3Small20 = 1215820
    Arena_Spawn_3v3Small21 = 1215821
    Arena_Spawn_3v3Small22 = 1215822
    Arena_Spawn_3v3Small23 = 1215823
    Arena_Spawn_3v3Small24 = 1215824
    Arena_Spawn_3v3Small25 = 1215825
    Arena_Spawn_3v3Small26 = 1215826
    Arena_Spawn_3v3SmallInitial0 = 1215800
    Arena_Spawn_3v3SmallInitial1 = 1215801
    Arena_Spawn_3v3SmallInitial2 = 1215802
    Arena_Spawn_3v3SmallInitial3 = 1215803
    Arena_Spawn_3v3SmallInitial4 = 1215804
    Arena_Spawn_3v3SmallInitial5 = 1215805
    Arena_Spawn_BR4Big00 = 1215000
    Arena_Spawn_BR4Big01 = 1215001
    Arena_Spawn_BR4Big02 = 1215002
    Arena_Spawn_BR4Big03 = 1215003
    Arena_Spawn_BR4Big04 = 1215004
    Arena_Spawn_BR4Big05 = 1215005
    Arena_Spawn_BR4Big06 = 1215006
    Arena_Spawn_BR4Big07 = 1215007
    Arena_Spawn_BR4Big08 = 1215008
    Arena_Spawn_BR4Big09 = 1215009
    Arena_Spawn_BR4Big10 = 1215010
    Arena_Spawn_BR4Big11 = 1215011
    Arena_Spawn_BR4Big12 = 1215012
    Arena_Spawn_BR4Big13 = 1215013
    Arena_Spawn_BR4Big14 = 1215014
    Arena_Spawn_BR4Big15 = 1215015
    Arena_Spawn_BR4Big16 = 1215016
    Arena_Spawn_BR4Big17 = 1215017
    Arena_Spawn_BR4Big18 = 1215018
    Arena_Spawn_BR4Big20 = 1215020
    Arena_Spawn_BR4Big21 = 1215021
    Arena_Spawn_BR4Big22 = 1215022
    Arena_Spawn_BR4Big24 = 1215024
    Arena_Spawn_BR4Big26 = 1215026
    Arena_Spawn_BR4Big27 = 1215027
    Arena_Spawn_BR4Big29 = 1215029
    Arena_Spawn_BR4Big30 = 1215030
    Arena_Spawn_BR4Big31 = 1215031
    Arena_Spawn_BR4Big32 = 1215032
    Arena_Spawn_BR4BigInitial0 = 1215019
    Arena_Spawn_BR4BigInitial1 = 1215023
    Arena_Spawn_BR4BigInitial2 = 1215025
    Arena_Spawn_BR4BigInitial3 = 1215028
    Arena_Spawn_BR4Small04 = 1215504
    Arena_Spawn_BR4Small05 = 1215505
    Arena_Spawn_BR4Small06 = 1215506
    Arena_Spawn_BR4Small07 = 1215507
    Arena_Spawn_BR4Small08 = 1215508
    Arena_Spawn_BR4Small09 = 1215509
    Arena_Spawn_BR4Small10 = 1215510
    Arena_Spawn_BR4Small11 = 1215511
    Arena_Spawn_BR4Small12 = 1215512
    Arena_Spawn_BR4Small13 = 1215513
    Arena_Spawn_BR4Small14 = 1215514
    Arena_Spawn_BR4Small15 = 1215515
    Arena_Spawn_BR4Small16 = 1215516
    Arena_Spawn_BR4Small17 = 1215517
    Arena_Spawn_BR4Small18 = 1215518
    Arena_Spawn_BR4Small19 = 1215519
    Arena_Spawn_BR4Small20 = 1215520
    Arena_Spawn_BR4Small21 = 1215521
    Arena_Spawn_BR4Small22 = 1215522
    Arena_Spawn_BR4Small23 = 1215523
    Arena_Spawn_BR4Small24 = 1215524
    Arena_Spawn_BR4SmallInitial0 = 1215500
    Arena_Spawn_BR4SmallInitial1 = 1215501
    Arena_Spawn_BR4SmallInitial2 = 1215502
    Arena_Spawn_BR4SmallInitial3 = 1215503
    Arena_Spawn_BR6Big00 = 1215400
    Arena_Spawn_BR6Big07 = 1215407
    Arena_Spawn_BR6Big08 = 1215408
    Arena_Spawn_BR6Big09 = 1215409
    Arena_Spawn_BR6Big10 = 1215410
    Arena_Spawn_BR6Big11 = 1215411
    Arena_Spawn_BR6Big12 = 1215412
    Arena_Spawn_BR6Big13 = 1215413
    Arena_Spawn_BR6Big14 = 1215414
    Arena_Spawn_BR6Big15 = 1215415
    Arena_Spawn_BR6Big16 = 1215416
    Arena_Spawn_BR6Big17 = 1215417
    Arena_Spawn_BR6Big18 = 1215418
    Arena_Spawn_BR6Big19 = 1215419
    Arena_Spawn_BR6Big20 = 1215420
    Arena_Spawn_BR6Big21 = 1215421
    Arena_Spawn_BR6Big22 = 1215422
    Arena_Spawn_BR6Big23 = 1215423
    Arena_Spawn_BR6Big24 = 1215424
    Arena_Spawn_BR6Big25 = 1215425
    Arena_Spawn_BR6Big26 = 1215426
    Arena_Spawn_BR6Big27 = 1215427
    Arena_Spawn_BR6Big28 = 1215428
    Arena_Spawn_BR6Big29 = 1215429
    Arena_Spawn_BR6Big30 = 1215430
    Arena_Spawn_BR6Big31 = 1215431
    Arena_Spawn_BR6Big32 = 1215432
    Arena_Spawn_BR6Big33 = 1215433
    Arena_Spawn_BR6Big34 = 1215434
    Arena_Spawn_BR6Big35 = 1215435
    Arena_Spawn_BR6Big36 = 1215436
    Arena_Spawn_BR6Big37 = 1215437
    Arena_Spawn_BR6Big38 = 1215438
    Arena_Spawn_BR6Big39 = 1215439
    Arena_Spawn_BR6Big40 = 1215440
    Arena_Spawn_BR6Big41 = 1215441
    Arena_Spawn_BR6Big42 = 1215442
    Arena_Spawn_BR6Big43 = 1215443
    Arena_Spawn_BR6Big44 = 1215444
    Arena_Spawn_BR6Big45 = 1215445
    Arena_Spawn_BR6BigInitial0 = 1215033
    Arena_Spawn_BR6BigInitial1 = 1215401
    Arena_Spawn_BR6BigInitial2 = 1215402
    Arena_Spawn_BR6BigInitial3 = 1215403
    Arena_Spawn_BR6BigInitial4 = 1215404
    Arena_Spawn_BR6BigInitial5 = 1215405
    Arena_Spawn_BR6BigInitial6 = 1215406
    Arena_Spawn_BR6Small06 = 1215906
    Arena_Spawn_BR6Small07 = 1215907
    Arena_Spawn_BR6Small08 = 1215908
    Arena_Spawn_BR6Small09 = 1215909
    Arena_Spawn_BR6Small10 = 1215910
    Arena_Spawn_BR6Small11 = 1215911
    Arena_Spawn_BR6Small12 = 1215912
    Arena_Spawn_BR6Small13 = 1215913
    Arena_Spawn_BR6Small14 = 1215914
    Arena_Spawn_BR6Small15 = 1215915
    Arena_Spawn_BR6Small16 = 1215916
    Arena_Spawn_BR6Small17 = 1215917
    Arena_Spawn_BR6Small18 = 1215918
    Arena_Spawn_BR6Small19 = 1215919
    Arena_Spawn_BR6Small20 = 1215920
    Arena_Spawn_BR6Small21 = 1215921
    Arena_Spawn_BR6SmallInitial0 = 1215900
    Arena_Spawn_BR6SmallInitial1 = 1215901
    Arena_Spawn_BR6SmallInitial2 = 1215902
    Arena_Spawn_BR6SmallInitial3 = 1215903
    Arena_Spawn_BR6SmallInitial4 = 1215904
    Arena_Spawn_BR6SmallInitial5 = 1215905
    Arena_Spawn_DuelBig01 = 1215201
    Arena_Spawn_DuelBig02 = 1215202
    Arena_Spawn_DuelBig03 = 1215203
    Arena_Spawn_DuelBig04 = 1215204
    Arena_Spawn_DuelBig05 = 1215205
    Arena_Spawn_DuelBig06 = 1215206
    Arena_Spawn_DuelBig07 = 1215207
    Arena_Spawn_DuelBig08 = 1215208
    Arena_Spawn_DuelBig10 = 1215210
    Arena_Spawn_DuelBig11 = 1215211
    Arena_Spawn_DuelBig12 = 1215212
    Arena_Spawn_DuelBig13 = 1215213
    Arena_Spawn_DuelBig14 = 1215214
    Arena_Spawn_DuelBig15 = 1215215
    Arena_Spawn_DuelBig16 = 1215216
    Arena_Spawn_DuelBig17 = 1215217
    Arena_Spawn_DuelBig18 = 1215218
    Arena_Spawn_DuelBig19 = 1215219
    Arena_Spawn_DuelBig20 = 1215220
    Arena_Spawn_DuelBig21 = 1215221
    Arena_Spawn_DuelBig22 = 1215222
    Arena_Spawn_DuelBig23 = 1215223
    Arena_Spawn_DuelBig24 = 1215224
    Arena_Spawn_DuelBig25 = 1215225
    Arena_Spawn_DuelBig26 = 1215226
    Arena_Spawn_DuelBig27 = 1215227
    Arena_Spawn_DuelBig28 = 1215228
    Arena_Spawn_DuelBig29 = 1215229
    Arena_Spawn_DuelBig30 = 1215230
    Arena_Spawn_DuelBig31 = 1215231
    Arena_Spawn_DuelBig32 = 1215232
    Arena_Spawn_DuelBig33 = 1215233
    Arena_Spawn_DuelBigInitial0 = 1215200
    Arena_Spawn_DuelBigInitial1 = 1215209
    Arena_Spawn_DuelSmall00 = 1215700
    Arena_Spawn_DuelSmall01 = 1215701
    Arena_Spawn_DuelSmall02 = 1215702
    Arena_Spawn_DuelSmall03 = 1215703
    Arena_Spawn_DuelSmall06 = 1215706
    Arena_Spawn_DuelSmall07 = 1215707
    Arena_Spawn_DuelSmall08 = 1215708
    Arena_Spawn_DuelSmall09 = 1215709
    Arena_Spawn_DuelSmall10 = 1215710
    Arena_Spawn_DuelSmall11 = 1215711
    Arena_Spawn_DuelSmall12 = 1215712
    Arena_Spawn_DuelSmall13 = 1215713
    Arena_Spawn_DuelSmall14 = 1215714
    Arena_Spawn_DuelSmall15 = 1215715
    Arena_Spawn_DuelSmall16 = 1215716
    Arena_Spawn_DuelSmall17 = 1215717
    Arena_Spawn_DuelSmall18 = 1215718
    Arena_Spawn_DuelSmall19 = 1215719
    Arena_Spawn_DuelSmall20 = 1215720
    Arena_Spawn_DuelSmall21 = 1215721
    Arena_Spawn_DuelSmall22 = 1215722
    Arena_Spawn_DuelSmall23 = 1215723
    Arena_Spawn_DuelSmall24 = 1215724
    Arena_Spawn_DuelSmall25 = 1215725
    Arena_Spawn_DuelSmall26 = 1215726
    Arena_Spawn_DuelSmallInitial0 = 1215704
    Arena_Spawn_DuelSmallInitial1 = 1215705
    ArrivalFromDarkroot = 1212510
    HostReturnPoint = 1212777
    KalameetBridgeAppearanceSnap = 1212051
    KalameetDeathArea = 1212056


class Spheres(RegionSphere):
    """`RegionSphere` entity IDs for MSB and EVS use."""

    # noinspection PyMethodParameters
    def _generate_next_value_(name, _, count, __):
        return RegionSphere.auto_generate(count, DARK_SOULS_DSR, 1210000)

    ChesterInvaderSpawn1 = 1212080
    ChesterInvaderSpawn2 = 1212082
    ChesterInvaderTrigger = 1212081
    SifBarrierPoint = 1212310
    SifSummonSignPrompt = 1212300


class Cylinders(RegionCylinder):
    """`RegionCylinder` entity IDs for MSB and EVS use."""

    # noinspection PyMethodParameters
    def _generate_next_value_(name, _, count, __):
        return RegionCylinder.auto_generate(count, DARK_SOULS_DSR, 1210000)

    Arena_InitialSpawnCylinderLarge_2v20 = 1217100
    Arena_InitialSpawnCylinderLarge_2v21 = 1217101
    Arena_InitialSpawnCylinderLarge_2v22 = 1217102
    Arena_InitialSpawnCylinderLarge_2v23 = 1217103
    Arena_InitialSpawnCylinderLarge_3v30 = 1217300
    Arena_InitialSpawnCylinderLarge_3v31 = 1217301
    Arena_InitialSpawnCylinderLarge_3v32 = 1217302
    Arena_InitialSpawnCylinderLarge_3v33 = 1217303
    Arena_InitialSpawnCylinderLarge_3v34 = 1217304
    Arena_InitialSpawnCylinderLarge_3v35 = 1217305
    Arena_InitialSpawnCylinderLarge_BR40 = 1217000
    Arena_InitialSpawnCylinderLarge_BR41 = 1217001
    Arena_InitialSpawnCylinderLarge_BR42 = 1217002
    Arena_InitialSpawnCylinderLarge_BR43 = 1217003
    Arena_InitialSpawnCylinderLarge_BR60 = 1217400
    Arena_InitialSpawnCylinderLarge_BR61 = 1217401
    Arena_InitialSpawnCylinderLarge_BR62 = 1217402
    Arena_InitialSpawnCylinderLarge_BR63 = 1217403
    Arena_InitialSpawnCylinderLarge_BR64 = 1217404
    Arena_InitialSpawnCylinderLarge_BR65 = 1217405
    Arena_InitialSpawnCylinderLarge_Duel20 = 1217200
    Arena_InitialSpawnCylinderLarge_Duel21 = 1217201
    Arena_InitialSpawnCylinderSmall_2v20 = 1217600
    Arena_InitialSpawnCylinderSmall_2v21 = 1217601
    Arena_InitialSpawnCylinderSmall_2v22 = 1217602
    Arena_InitialSpawnCylinderSmall_2v23 = 1217603
    Arena_InitialSpawnCylinderSmall_3v30 = 1217800
    Arena_InitialSpawnCylinderSmall_3v31 = 1217801
    Arena_InitialSpawnCylinderSmall_3v32 = 1217802
    Arena_InitialSpawnCylinderSmall_3v33 = 1217803
    Arena_InitialSpawnCylinderSmall_3v34 = 1217804
    Arena_InitialSpawnCylinderSmall_3v35 = 1217805
    Arena_InitialSpawnCylinderSmall_BR40 = 1217500
    Arena_InitialSpawnCylinderSmall_BR41 = 1217501
    Arena_InitialSpawnCylinderSmall_BR42 = 1217502
    Arena_InitialSpawnCylinderSmall_BR43 = 1217503
    Arena_InitialSpawnCylinderSmall_BR60 = 1217900
    Arena_InitialSpawnCylinderSmall_BR61 = 1217901
    Arena_InitialSpawnCylinderSmall_BR62 = 1217902
    Arena_InitialSpawnCylinderSmall_BR63 = 1217903
    Arena_InitialSpawnCylinderSmall_BR64 = 1217904
    Arena_InitialSpawnCylinderSmall_BR65 = 1217905
    Arena_InitialSpawnCylinderSmall_Duel1 = 1217700
    Arena_InitialSpawnCylinderSmall_Duel2 = 1217701
    ChainedPrisonerNest = 1212651
    ChainedPrisonerWarpPoint = 1212150
    PlayerPointAfterManusCutscene = 1212022
    SanctuaryGuardianCombatArea = 1212000


class Boxes(RegionBox):
    """`RegionBox` entity IDs for MSB and EVS use."""

    # noinspection PyMethodParameters
    def _generate_next_value_(name, _, count, __):
        return RegionBox.auto_generate(count, DARK_SOULS_DSR, 1210000)

    AlvinaWarp0 = 1212330
    AlvinaWarp1 = 1212331
    AlvinaWarp2 = 1212332
    Arena_1vs1_Small_Territory_4510 = 1212700
    Arena_1vs1_Small_Summon_Hope_A = 1212703
    Arena_1vs1_Small_Summon_Hope_B = 1212704
    Arena_1vs1_Small_Battle_Room = 1212730
    Arena_1vs1_Large_Territory_4523 = 1212713
    Arena_1vs1_Large_Summon_Hope_A = 1212716
    Arena_1vs1_Large_Summon_Hope_B = 1212717
    Arena_1vs1_Large_Battle_Room = 1212731
    Arena_2vs2_Small_Territory_4511 = 1212701
    Arena_2vs2_Small_Summon_Hope_A1 = 1212705
    Arena_2vs2_Small_Summon_Hope_A2 = 1212706
    Arena_2vs2_Small_Summon_Hope_B1 = 1212707
    Arena_2vs2_Small_Summon_Hope_B2 = 1212708
    Arena_2vs2_Small_Battle_Room = 1212732
    Arena_2vs2_Large_Territory_4524 = 1212714
    Arena_2vs2_Large_Summon_Hope_A1 = 1212718
    Arena_2vs2_Large_Summon_Hope_A2 = 1212719
    Arena_2vs2_Large_Summon_Hope_B1 = 1212720
    Arena_2vs2_Large_Summon_Hope_B2 = 1212721
    Arena_2vs2_Large_Battle_Room = 1212733
    Arena_3vs3_Small_Territory_4510 = 1212793
    Arena_3vs3_Small_Battle_Room = 1212736
    Arena_3vs3_Large_Territory_4523 = 1212796
    Arena_3vs3_Large_Battle_Room = 1212737
    Arena_BR6_Small_Territory_4510 = 1212794
    Arena_BR6_Small_Battle_Room = 1212738
    Arena_BR6_Large_Territory_4523 = 1212797
    Arena_BR6_Large_Battle_Room = 1212739
    Arena_BR_Large_Battle_Room = 1212735
    Arena_BR_Large_Summon_Hope_A = 1212722
    Arena_BR_Large_Summon_Hope_B = 1212723
    Arena_BR_Large_Summon_Hope_C = 1212724
    Arena_BR_Large_Summon_Hope_D = 1212725
    Arena_BR_Large_Territory_4525 = 1212715
    Arena_BR_Small_Battle_Room = 1212734
    Arena_BR_Small_Summon_Hope_A = 1212709
    Arena_BR_Small_Summon_Hope_B = 1212710
    Arena_BR_Small_Summon_Hope_C = 1212711
    Arena_BR_Small_Summon_Hope_D = 1212712
    Arena_BR_Small_Territory_4512 = 1212702
    Arena_FogControlArea0 = 1219001
    Arena_FogControlArea1 = 1219002
    Arena_NoDead_TemporaryCancellation0 = 1212740
    Arena_NoDead_TemporaryCancellation1 = 1212741
    Arena_StreakDisplay = 1218900
    ArtoriasCombatStart = 1212896
    ArtoriasFogPrompt = 1212898
    ArtoriasFogRotationTarget = 1212897
    ArtoriasMusic = 1212890
    BloatheadSorcererFallPreventionArea0 = 1212030
    BloatheadSorcererFallPreventionArea1 = 1212031
    BloatheadSorcererJumpingArea0 = 1212032
    BloatheadSorcererJumpingArea1 = 1212033
    ChainedPrisonerReturn = 1212650
    ChesterInvaderReturnsHomeTrigger1 = 1212084
    ChesterInvaderReturnsHomeTrigger2 = 1212085
    ChesterInvaderTrigger2 = 1212083
    CiaranInitialPosition = 1212352
    CiaranNest = 1212353
    Elevator0_RideArea = 1212105
    Elevator0_StartTrigger = 1212104
    Elevator0_CallDownTrigger = 1212103
    Elevator0_CallUpTrigger = 1212102
    Elevator0_StartFromBottomTrigger = 1212101
    Elevator0_StartFromTopTrigger = 1212100
    Elevator1_RideArea = 1212115
    Elevator1_CallDownTrigger = 1212113
    Elevator1_CallUpTrigger = 1212112
    Elevator1_StartFromBottomTrigger = 1212111
    Elevator1_StartFromTopTrigger = 1212110
    Elevator2_RideArea = 1212125
    Elevator2_StartTrigger = 1212124
    Elevator2_CallDownTrigger = 1212123
    Elevator2_CallUpTrigger = 1212122
    Elevator2_StartFromBottomTrigger = 1212121
    Elevator2_StartFromTopTrigger = 1212120
    Elevator3_RideArea = 1212135
    Elevator3_StartTrigger = 1212134
    Elevator3_CallDownTrigger = 1212133
    Elevator3_CallUpTrigger = 1212132
    Elevator3_StartFromBottomTrigger = 1212131
    Elevator3_StartFromTopTrigger = 1212130
    Elevator4_RideArea = 1212145
    Elevator4_StartTrigger = 1212144
    Elevator4_CallDownTrigger = 1212143
    Elevator4_CallUpTrigger = 1212142
    Elevator4_StartFromBottomTrigger = 1212141
    Elevator4_StartFromTopTrigger = 1212140
    GardenerTrap0 = 1212500
    GardenerTrap1 = 1212501
    GardenerTrap2 = 1212502
    GardenerTrap3 = 1212506
    GardeningAnimation0 = 1212503
    GardeningAnimation0_1 = 1212523
    GardeningAnimation3 = 1212504
    GardeningAnimation3_1 = 1212524
    GardeningAnimation7 = 1212505
    GardeningAnimation7_1 = 1212525
    GoughCombatArea = 1212040
    GoughNestArea = 1212041
    IllusoryFloorFallControl = 1212335
    IllusoryFloorTrigger = 1212336
    InvaderSpawn000 = 1214000
    InvaderSpawn100 = 1214100
    InvaderSpawn101 = 1214101
    InvaderSpawn102 = 1214102
    InvaderSpawn200 = 1214200
    InvaderSpawn201 = 1214201
    InvaderSpawn210 = 1214210
    KalameetAirborne0Appears = 1212052
    KalameetAirborne1StartingPoint = 1212053
    KalameetAirborne2FarBreath = 1212054
    KalameetAirborne2FarBreathB = 1212062
    KalameetAirborne3NearBreath = 1212055
    KalameetBridgeTrigger = 1212050
    KalameetCombatStart = 1212906
    KalameetFogPrompt = 1212908
    KalameetFogRotationTarget = 1212907
    KalameetHates0 = 1212057
    KalameetHates1 = 1212058
    KalameetHates2 = 1212059
    KalameetMusic = 1212900
    KalameetNotifyBattle = 1212909
    KalameetTakeoffPoint0 = 1212060
    KalameetTakeoffPoint1 = 1212061
    KalameetWallTrigger = 1213008
    LesserSanctuaryGuardianCombatStart0 = 1212004
    LesserSanctuaryGuardianCombatStart1 = 1212001
    LesserSanctuaryGuardianCombatStart2 = 1212002
    LesserSanctuaryGuardianNestSwitchingA0 = 1212006
    LesserSanctuaryGuardianNestSwitchingA1 = 1212007
    LesserSanctuaryGuardianNestSwitchingA2 = 1212008
    LesserSanctuaryGuardianNestSwitchingB0 = 1212009
    LesserSanctuaryGuardianNestSwitchingB1 = 1212010
    LesserSanctuaryGuardianNestSwitchingB2 = 1212011
    LesserSanctuaryGuardianNestSwitchingC0 = 1212005
    LesserSanctuaryGuardianReturnTrigger = 1212003
    LightIllusoryWallTrigger0 = 1212200
    LightIllusoryWallTrigger1 = 1212201
    ManusCombatStart = 1212996
    ManusFogPrompt = 1212998
    ManusFogRotationTarget = 1212997
    ManusInvincibleLanding = 1212021
    ManusMusic = 1212990
    MimicNest0 = 1212180
    MimicNest1 = 1212181
    SanctuaryGuardianCombatStart = 1212886
    SanctuaryGuardianFogPrompt = 1212888
    SanctuaryGuardianFogRotationTarget = 1212887
    SanctuaryGuardianMusic = 1212880
    SifRescueTrigger = 1212320
    TestBox = 1212778
    TriggerCiaranNestChange = 1212351
    TriggerCiaranNestRevert = 1212350
