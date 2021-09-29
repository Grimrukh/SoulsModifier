from soulstruct.games import DARK_SOULS_DSR
from soulstruct.game_types import *


class Objects(Object):
    """`Object` entity IDs for MSB and EVS use."""

    # noinspection PyMethodParameters
    def _generate_next_value_(name, _, count, __):
        return Object.auto_generate(count, DARK_SOULS_DSR, 1310000)

    o0020_0000 = 1311250
    o0200_0000 = 1311960
    o0200_0001 = 1311950
    o0200_0002 = 1311961
    o0500_0024 = 1311600
    o3043_0000 = 1311140
    o3044_0000 = 1311141
    o3060_0000 = 1311300
    o3140_0000 = 1311142
    o3140_0001 = 1311143
    o3141_0000 = 1311144
    o3142_0000 = 1311145
    o3143_0000 = 1311148
    o3143_0001 = 1311146
    o3144_0000 = 1311147
    o3452_0000 = 1311400
    o3900_0000 = 1311200
    o3900_0001 = 1311202
    o3901_0000 = 1311201
    o3961_0000 = 1311994
    o3962_0000 = 1311700
    o3963_0000 = 1311710
    o3964_0000 = 1311990


class Characters(Character):
    """`Character` entity IDs for MSB and EVS use."""

    # noinspection PyMethodParameters
    def _generate_next_value_(name, _, count, __):
        return Character.auto_generate(count, DARK_SOULS_DSR, 1310000)

    c0000_0002 = 6071
    c0000_0003 = 6091
    c0000_0004 = 6101
    c0000_0005 = 6321
    c0000_0007 = 6551
    c0000_PatchesAmbush = 7987
    c1000_0000 = 1310960
    c1000_0001 = 1310950
    c1000_0002 = 1310961
    c2370_TrollChanneler = 7967
    c2795_0000 = 1310300
    c2900_0000 = 1310120
    c2900_0001 = 1310121
    c2900_0002 = 1310122
    c2910_0018 = 1310251
    c2910_0019 = 1310125
    c2910_0020 = 1310124
    c2910_0021 = 1310123
    c2910_0022 = 1310900
    c2910_0023 = 1310901
    c2910_0024 = 1310902
    c2910_0025 = 1310903
    c2910_0026 = 1310904
    c2950_0007 = 1310905
    c2950_0008 = 1310906
    c2950_0009 = 1310907
    c2950_0010 = 1310908
    c2950_0011 = 1310909
    c2960_0003 = 1310203
    c2960_0004 = 1310204
    c2960_0005 = 1310205
    c2960_0006 = 1310206
    c2960_0007 = 1310207
    c2960_0008 = 1310208
    c2960_0009 = 1310209
    c2960_0010 = 1310210
    c2960_0011 = 1310211
    c2960_0012 = 1310200
    c2960_0013 = 1310201
    c2960_0014 = 1310202
    c2960_0015 = 1310250
    c3300_0000 = 1310400
    c3490_0000 = 1313900
    c3490_0001 = 1313910
    c3491_0000 = 1313901
    c3491_0001 = 1313911
    c3491_0002 = 1313902
    c3491_0003 = 1313912
    c5220_0000 = 1310800
    c5220_0001 = 1310810


class PlayerStarts(PlayerStart):
    """`PlayerStart` entity IDs for MSB and EVS use."""

    # noinspection PyMethodParameters
    def _generate_next_value_(name, _, count, __):
        return PlayerStart.auto_generate(count, DARK_SOULS_DSR, 1310000)

    c0000_0001 = 1310998
    c0000_0006 = 1310970


class Collisions(Collision):
    """`Collision` entity IDs for MSB and EVS use."""

    # noinspection PyMethodParameters
    def _generate_next_value_(name, _, count, __):
        return Collision.auto_generate(count, DARK_SOULS_DSR, 1310000)

    h1001B1 = 1313000
    h1002B1 = 1313001
    h1005B1 = 1313004


class Sounds(SoundEvent):
    """`SoundEvent` entity IDs for MSB and EVS use."""

    # noinspection PyMethodParameters
    def _generate_next_value_(name, _, count, __):
        return SoundEvent.auto_generate(count, DARK_SOULS_DSR, 1310000)

    NitoMusic = 1313800


class VFX(VFXEvent):
    """`VFXEvent` entity IDs for MSB and EVS use."""

    # noinspection PyMethodParameters
    def _generate_next_value_(name, _, count, __):
        return VFXEvent.auto_generate(count, DARK_SOULS_DSR, 1310000)

    BossEntranceFog = 1311991
    CheckpointFog1 = 1311701
    ColoredLight00 = 1313200
    ColoredLight01 = 1313201
    ColoredLight02 = 1313202
    ColoredLight03 = 1313203
    ColoredLight04 = 1313204
    ColoredLight05 = 1313205
    ColoredLight06 = 1313206
    ColoredLight07 = 1313207
    ColoredLight08 = 1313208
    ColoredLight09 = 1313209
    ColoredLight10 = 1313210
    ColoredLight11 = 1313211
    ColoredLight12 = 1313212
    ColoredLight13 = 1313213
    ColoredLight14 = 1313214
    ColoredLight15 = 1313215
    ColoredLight16 = 1313216
    ColoredLight17 = 1313217
    ColoredLight18 = 1313218
    ColoredLight19 = 1313219
    ColoredLight20 = 1313220
    ColoredLight21 = 1313221
    ColoredLight22 = 1313222
    ColoredLight23 = 1313223
    ColoredLight24 = 1313224
    ColoredLight25 = 1313225
    ColoredLight26 = 1313226
    ColoredLight27 = 1313227
    ColoredLight28 = 1313228
    ColoredLight29 = 1313229
    ColoredLight30 = 1313230
    ColoredLight31 = 1313231
    ColoredLight32 = 1313232
    ColoredLight33 = 1313233
    ColoredLight34 = 1313234
    ColoredLight35 = 1313235
    ColoredLight36 = 1313236
    ColoredLight37 = 1313237
    ColoredLight38 = 1313238
    ColoredLight39 = 1313239
    ColoredLight40 = 1313240
    ColoredLight41 = 1313241
    ColoredLight42 = 1313242
    ColoredLight43 = 1313243
    ColoredLight44 = 1313244
    ColoredLight45 = 1313245
    ColoredLight46 = 1313246
    ColoredLight47 = 1313247
    ColoredLight48 = 1313248
    GoldenFog = 1311711
    MultiplayerFog1 = 1311995


class SpawnPoints(SpawnPointEvent):
    """`SpawnPointEvent` entity IDs for MSB and EVS use."""

    # noinspection PyMethodParameters
    def _generate_next_value_(name, _, count, __):
        return SpawnPointEvent.auto_generate(count, DARK_SOULS_DSR, 1310000)

    SpawnPoint0 = 1312960
    SpawnPoint1 = 1312961
    SpawnPointAtBoss = 1312950


class Points(RegionPoint):
    """`RegionPoint` entity IDs for MSB and EVS use."""

    # noinspection PyMethodParameters
    def _generate_next_value_(name, _, count, __):
        return RegionPoint.auto_generate(count, DARK_SOULS_DSR, 1310000)

    LeeroyInvaderSpawn = 1312000


class Spheres(RegionSphere):
    """`RegionSphere` entity IDs for MSB and EVS use."""

    # noinspection PyMethodParameters
    def _generate_next_value_(name, _, count, __):
        return RegionSphere.auto_generate(count, DARK_SOULS_DSR, 1310000)

    ColoredLightRegion00 = 1313300
    ColoredLightRegion01 = 1313301
    ColoredLightRegion02 = 1313302
    ColoredLightRegion03 = 1313303
    ColoredLightRegion04 = 1313304
    ColoredLightRegion05 = 1313305
    ColoredLightRegion06 = 1313306
    ColoredLightRegion07 = 1313307
    ColoredLightRegion08 = 1313308
    ColoredLightRegion09 = 1313309
    ColoredLightRegion10 = 1313310
    ColoredLightRegion11 = 1313311
    ColoredLightRegion12 = 1313312
    ColoredLightRegion13 = 1313313
    ColoredLightRegion14 = 1313314
    ColoredLightRegion15 = 1313315
    ColoredLightRegion16 = 1313316
    ColoredLightRegion17 = 1313317
    ColoredLightRegion18 = 1313318
    ColoredLightRegion19 = 1313319
    ColoredLightRegion20 = 1313320
    ColoredLightRegion21 = 1313321
    ColoredLightRegion22 = 1313322
    ColoredLightRegion23 = 1313323
    ColoredLightRegion24 = 1313324
    ColoredLightRegion25 = 1313325
    ColoredLightRegion26 = 1313326
    ColoredLightRegion27 = 1313327
    ColoredLightRegion28 = 1313328
    ColoredLightRegion29 = 1313329
    ColoredLightRegion30 = 1313330
    ColoredLightRegion31 = 1313331
    ColoredLightRegion32 = 1313332
    ColoredLightRegion33 = 1313333
    ColoredLightRegion34 = 1313334
    ColoredLightRegion35 = 1313335
    ColoredLightRegion36 = 1313336
    ColoredLightRegion37 = 1313337
    ColoredLightRegion38 = 1313338
    ColoredLightRegion39 = 1313339
    ColoredLightRegion40 = 1313340
    ColoredLightRegion41 = 1313341
    ColoredLightRegion42 = 1313342
    ColoredLightRegion43 = 1313343
    ColoredLightRegion44 = 1313344
    ColoredLightRegion45 = 1313345
    ColoredLightRegion46 = 1313346
    ColoredLightRegion47 = 1313347
    ColoredLightRegion48 = 1313348
    LeeroyInvaderTrigger = 1312001


class Boxes(RegionBox):
    """`RegionBox` entity IDs for MSB and EVS use."""

    # noinspection PyMethodParameters
    def _generate_next_value_(name, _, count, __):
        return RegionBox.auto_generate(count, DARK_SOULS_DSR, 1310000)

    ArrivalInCoffin = 1312110
    AtGoldenFog = 1312610
    BoneTowerAmbushTrigger = 1312251
    BoneTowerWarpPoint = 1312250
    CheckpointFog1BackSide = 1312601
    CheckpointFog1FrontSide = 1312600
    CoffinSlide0 = 1313100
    CoffinSlide1 = 1313101
    CoffinSlide2 = 1313102
    CoffinSlide3 = 1313103
    CoffinSlide4 = 1313104
    InvaderSpawn00 = 1314000
    InvaderSpawn01 = 1314001
    InvaderSpawn10 = 1314010
    InvaderSpawn11 = 1314011
    InvaderSpawn12 = 1314012
    InvaderSpawn13 = 1314013
    NitoCutsceneTrigger = 1312999
    NitoFogPrompt = 1312998
    NitoFogRotationTarget = 1312997
    NitoMusic = 1312990
    PatchesKickTrigger = 1313400
    PatchesPointAfterKickCutscene = 1312121
    PlayerPointAfterKickCutscene = 1312120
