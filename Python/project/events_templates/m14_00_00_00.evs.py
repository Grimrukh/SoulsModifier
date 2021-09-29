"""
linked:


strings:

"""
from soulstruct.darksouls1r.events import *
from ..entities.m14_00_00_00_entities import *
from ..entities.m10_00_00_00_entities import Objects as m10_00_Objects
from ..entities.common_entities import *


def Constructor():
    """ 0: Event 0 """
    RegisterBonfire(
        11400992,
        obj=Objects.o0200_0000,
        reaction_distance=2.0,
        reaction_angle=180.0,
        initial_kindle_level=10,
    )
    RegisterBonfire(
        11400984,
        obj=Objects.o0200_0001,
        reaction_distance=2.0,
        reaction_angle=180.0,
        initial_kindle_level=0,
    )
    RegisterBonfire(
        11400976,
        obj=Objects.o0200_0002,
        reaction_distance=2.0,
        reaction_angle=180.0,
        initial_kindle_level=0,
    )
    RegisterLadder(start_climbing_flag=11400010, stop_climbing_flag=11400011, obj=Objects.o4100_0000)
    RegisterLadder(start_climbing_flag=11400012, stop_climbing_flag=11400013, obj=Objects.o4101_0000)
    RegisterLadder(start_climbing_flag=11400014, stop_climbing_flag=11400015, obj=Objects.o4102_0000)
    RegisterLadder(start_climbing_flag=11400016, stop_climbing_flag=11400017, obj=Objects.o4103_0000)
    RegisterLadder(start_climbing_flag=11400018, stop_climbing_flag=11400019, obj=Objects.o4104_0000)
    RegisterLadder(start_climbing_flag=11400020, stop_climbing_flag=11400021, obj=Objects.o4105_0000)
    RegisterLadder(start_climbing_flag=11400022, stop_climbing_flag=11400023, obj=Objects.o4106_0000)
    RegisterLadder(start_climbing_flag=11400024, stop_climbing_flag=11400025, obj=Objects.o4107_0000)
    RegisterLadder(start_climbing_flag=11400026, stop_climbing_flag=11400027, obj=Objects.o4108_0000)
    RegisterLadder(start_climbing_flag=11400028, stop_climbing_flag=11400029, obj=Objects.o4109_0000)
    RegisterLadder(start_climbing_flag=11400030, stop_climbing_flag=11400031, obj=Objects.o4110_0000)
    RegisterLadder(start_climbing_flag=11400032, stop_climbing_flag=11400033, obj=Objects.o4111_0000)
    RegisterLadder(start_climbing_flag=11400034, stop_climbing_flag=11400035, obj=Objects.o4112_0000)
    RegisterLadder(start_climbing_flag=11400036, stop_climbing_flag=11400037, obj=Objects.o4113_0000)
    RegisterLadder(start_climbing_flag=11400038, stop_climbing_flag=11400039, obj=Objects.o4114_0000)
    RegisterLadder(start_climbing_flag=11400040, stop_climbing_flag=11400041, obj=Objects.o4115_0000)
    RegisterLadder(start_climbing_flag=11400042, stop_climbing_flag=11400043, obj=Objects.o4116_0000)
    RegisterLadder(start_climbing_flag=11400044, stop_climbing_flag=11400045, obj=Objects.o4117_0000)
    RegisterLadder(start_climbing_flag=11400046, stop_climbing_flag=11400047, obj=Objects.o4118_0000)
    RegisterLadder(start_climbing_flag=11400048, stop_climbing_flag=11400049, obj=Objects.o4119_0000)
    RegisterLadder(start_climbing_flag=11400050, stop_climbing_flag=11400051, obj=Objects.o4120_0000)
    RegisterLadder(start_climbing_flag=11400052, stop_climbing_flag=11400053, obj=Objects.o4121_0000)
    RegisterLadder(start_climbing_flag=11400054, stop_climbing_flag=11400055, obj=Objects.o4122_0000)
    RegisterLadder(start_climbing_flag=11400056, stop_climbing_flag=11400057, obj=Objects.o4123_0000)
    RegisterLadder(start_climbing_flag=11400058, stop_climbing_flag=11400059, obj=Objects.o4124_0000)
    RegisterLadder(start_climbing_flag=11400060, stop_climbing_flag=11400061, obj=Objects.o4111_0001)
    RegisterLadder(start_climbing_flag=11400062, stop_climbing_flag=11400063, obj=Objects.o4109_0001)
    RegisterLadder(start_climbing_flag=11400064, stop_climbing_flag=11400065, obj=Objects.o4109_0002)
    RegisterLadder(start_climbing_flag=11400066, stop_climbing_flag=11400067, obj=Objects.o4111_0002)
    RegisterLadder(start_climbing_flag=11400068, stop_climbing_flag=11400069, obj=Objects.o4120_0001)
    RegisterLadder(start_climbing_flag=11400070, stop_climbing_flag=11400071, obj=Objects.o4125_0000)
    SkipLinesIfClient(6)
    DisableObject(Objects.o4952_0000)
    DeleteVFX(VFX.MultiplayerFog1, erase_root_only=False)
    DisableObject(Objects.o4953_0000)
    DeleteVFX(VFX.MultiplayerFog2, erase_root_only=False)
    DisableObject(Objects.o4954_0000)
    DeleteVFX(VFX.MultiplayerFog3, erase_root_only=False)
    IfFlagOn(1, 11000810)
    IfFlagOn(1, 11410810)
    IfFlagOn(1, 11410811)
    SkipLinesIfConditionTrue(2, 1)
    DisableObject(Objects.o0500_0037)
    SkipLines(1)
    EnableTreasure(Objects.o0500_0037)
    RunEvent(
        11400090,
        slot=1,
        args=(Objects.o4956_0000, VFX.CheckpointFog1, Boxes.CheckpointFog1FrontSide, Boxes.CheckpointFog1BackSide),
    )
    RunEvent(11400900)
    RunEvent(11400800)
    RunEvent(11405000)
    RunEvent(11400200)
    RunEvent(11400210)
    RunEvent(11400220)
    RunEvent(11400230)
    RunEvent(140)
    DisableSoundEvent(1403800)
    SkipLinesIfFlagOff(6, 9)
    RunEvent(11405392)
    DisableObject(Objects.o4950_0000)
    DeleteVFX(VFX.QuelaagEntranceFog, erase_root_only=False)
    DisableObject(Objects.o4951_0000)
    DeleteVFX(VFX.QuelaagExitFog, erase_root_only=False)
    SkipLines(7)
    RunEvent(11405390)
    RunEvent(11405391)
    RunEvent(11405393)
    RunEvent(11405392)
    RunEvent(11400001)
    RunEvent(11405394)
    RunEvent(11405395)
    RunEvent(
        11405100,
        slot=0,
        args=(Objects.o4200_0000, Boxes.CreakyBridge00_00, Boxes.CreakyBridge00_01, Boxes.CreakyBridge00_02),
    )
    RunEvent(
        11405110,
        slot=0,
        args=(
            Objects.o4202_0000,
            Boxes.CreakyBridge02_00,
            Boxes.CreakyBridge02_01,
            Boxes.CreakyBridge02_02,
            Boxes.CreakyBridge02_03,
            Boxes.CreakyBridge02_04,
        ),
    )
    RunEvent(
        11405350,
        slot=0,
        args=(
            Characters.c3210_0000,
            Characters.c3220_0000,
            Characters.c3220_0001,
            Characters.c3220_0002,
            Characters.c3220_0003,
            Characters.c3220_0004,
            1,
        ),
    )
    RunEvent(
        11405350,
        slot=3,
        args=(
            Characters.c3210_0002,
            Characters.c3220_0015,
            Characters.c3220_0016,
            Characters.c3220_0017,
            Characters.c3220_0018,
            Characters.c3220_0019,
            0,
        ),
    )
    RunEvent(
        11405350,
        slot=4,
        args=(
            Characters.c3210_0003,
            Characters.c3220_0020,
            Characters.c3220_0021,
            Characters.c3220_0022,
            Characters.c3220_0023,
            Characters.c3220_0024,
            0,
        ),
    )
    RunEvent(11400100, slot=0, args=(11405340, Spheres.MosquitoSpawnerControl1, Spawners.MosquitoSpawner1))
    RunEvent(11400100, slot=1, args=(11405341, Spheres.MosquitoSpawnerControl2, Spawners.MosquitoSpawner2))
    RunEvent(11400100, slot=2, args=(11405342, Spheres.MosquitoSpawnerControl3, Spawners.MosquitoSpawner3))
    RunEvent(11405200, slot=0, args=(Characters.c2060_0012, Objects.o4820_0012))
    RunEvent(11405250, slot=0, args=(Characters.c2811_0000,))
    RunEvent(11405250, slot=1, args=(Characters.c2811_0001,))
    RunEvent(11405250, slot=2, args=(Characters.c2811_0002,))
    RunEvent(11405250, slot=3, args=(Characters.c2811_0003,))
    RunEvent(11405250, slot=4, args=(Characters.c2811_0004,))
    RunEvent(11400850, slot=0, args=(Characters.c2530_0000, 25300200))
    RunEvent(11400850, slot=1, args=(Characters.c2530_0001, 25300200))
    RunEvent(11400850, slot=2, args=(Characters.c2530_0002, 25300200))
    RunEvent(11400850, slot=3, args=(Characters.c2530_0003, 25300200))
    RunEvent(11400850, slot=4, args=(Characters.c2530_0004, 25300200))
    RunEvent(11400850, slot=5, args=(Characters.c2530_0005, 25300200))
    RunEvent(11400850, slot=6, args=(Characters.c2530_0006, 25300200))
    RunEvent(11400850, slot=7, args=(Characters.c2530_0007, 25300200))
    RunEvent(11400850, slot=8, args=(Characters.c2530_0008, 25300200))
    RunEvent(11400600, slot=0, args=(Objects.o0110_0000, 11400600))
    RunEvent(11400600, slot=1, args=(Objects.o0110_0001, 11400601))
    RunEvent(11400600, slot=2, args=(Objects.o0110_0002, 11400602))
    RunEvent(11415170)
    RunEvent(11405843, slot=0, args=(9, Objects.o4950_0000, Boxes.QuelaagFogPrompt, Boxes.QuelaagFogRotationTarget))
    RunEvent(11405846, slot=0, args=(9, Objects.o4950_0000, VFX.QuelaagEntranceFog))
    # <!--!>


def Preconstructor():
    """ 50: Event 50 """
    HumanityRegistration(Characters.c0000_0010, 8940)
    HumanityRegistration(Characters.c0000_0007, 8940)
    RunEvent(11405030)
    RunEvent(11405029)
    RunEvent(11405032)
    RunEvent(11405035)
    RunEvent(11400901)
    RunEvent(14005990, slot=0, args=(11405031, Characters.c0000_0010))
    SkipLinesIfFlagOn(1, 1257)
    DisableCharacter(Characters.c0000_0004)
    SetTeamTypeAndExitStandbyAnimation(Characters.c0000_0004, TeamType.HostileAlly)
    RunEvent(11400520, slot=0, args=(Characters.c0000_0004, 1250, 1259, 1254))
    RunEvent(11400530, slot=0, args=(Characters.c0000_0004, 1250, 1259, 1257))
    SkipLinesIfFlagRangeAnyOn(1, (1270, 1279))
    EnableFlag(1270)
    RunEvent(11400520, slot=1, args=(Characters.c5340_0000, 1270, 1279, 1272))
    SkipLinesIfFlagOn(2, 1280)
    SetNest(Characters.c3210_0000, Boxes.EingyiNest)
    Move(Characters.c3210_0000, destination=Boxes.EingyiNest, destination_type=CoordEntityType.Region, short_move=True)
    RunEvent(11400520, slot=2, args=(Characters.c3210_0000, 1280, 1289, 1284))
    RunEvent(11400531, slot=0, args=(Characters.c3210_0000, 1280, 1289, 1281))
    RunEvent(11400532, slot=0, args=(Characters.c3210_0000, 1280, 1289, 1286))
    RunEvent(11400501, slot=0, args=(Characters.c3210_0000, 1282))
    RunEvent(11400502, slot=0, args=(Characters.c3210_0000, 1283))
    RunEvent(11400503, slot=0, args=(Characters.c3210_0000, 1287))
    RunEvent(11400533)
    HumanityRegistration(Characters.c0000_0005, 8398)
    SkipLinesIfFlagOn(2, 1296)
    SkipLinesIfFlagOn(1, 1290)
    SkipLines(1)
    DisableCharacter(Characters.c0000_0005)
    RunEvent(11400510, slot=3, args=(Characters.c0000_0005, 1294))
    RunEvent(11400520, slot=3, args=(Characters.c0000_0005, 1290, 1309, 1295))
    RunEvent(11400536, slot=0, args=(Characters.c0000_0005, 1290, 1309, 1291))
    RunEvent(11400537, slot=0, args=(Characters.c0000_0005, 1290, 1309, 1292))
    RunEvent(11400538, slot=0, args=(Characters.c0000_0005, 1290, 1309, 1293))
    RunEvent(11400539, slot=0, args=(Characters.c0000_0005, 1290, 1309, 1296))
    HumanityRegistration(Characters.c0000_0003, 8446)
    SkipLinesIfFlagOn(3, 1512)
    SkipLinesIfFlagOn(2, 1502)
    SkipLinesIfFlagOn(1, 1501)
    DisableCharacter(Characters.c0000_0003)
    RunEvent(11400510, slot=4, args=(Characters.c0000_0003, 1512))
    RunEvent(11400520, slot=4, args=(Characters.c0000_0003, 1490, 1514, 1513))
    RunEvent(11400551, slot=0, args=(Characters.c0000_0003, 1490, 1514, 1501))
    RunEvent(11400552, slot=0, args=(Characters.c0000_0003, 1490, 1514, 1502))
    RunEvent(11400553)
    RunEvent(11400554, slot=0, args=(Characters.c0000_0003,))
    HumanityRegistration(Characters.c0000_0008, 8470)
    HumanityRegistration(Characters.c0000_0009, 8900)
    SkipLinesIfClient(1)
    DisableFlag(11405022)
    SkipLinesIfFlagOn(8, 11405022)
    IfHost(1)
    IfPlayerCovenant(1, Covenant.ForestHunter)
    IfFlagOn(1, 1601)
    SkipLinesIfConditionTrue(2, 1)
    DisableCharacter(Characters.c0000_0008)
    DisableCharacter(Characters.c0000_0009)
    RunEvent(11400520, slot=5, args=(Characters.c0000_0008, 1600, 1619, 1604))
    RunEvent(11400520, slot=6, args=(Characters.c0000_0009, 1760, 1769, 1764))
    RunEvent(11400504, slot=0, args=(Characters.c0000_0008, 1603, Characters.c0000_0009))
    RunEvent(11400560, slot=0, args=(Characters.c0000_0008, 1600, 1619, 1601, Characters.c0000_0009))
    RunEvent(11400566, slot=0, args=(Characters.c0000_0008, Characters.c0000_0009))
    RunEvent(11400567, slot=0, args=(Characters.c0000_0008, Characters.c0000_0009))
    SkipLinesIfConditionFalse(2, 1)
    WaitFrames(1)
    EnableFlag(11405022)
    DisableFlag(1766)


def Event11400090(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11400090: Event 11400090 """
    SkipLinesIfThisEventSlotOff(3)
    DisableObject(arg_0_3)
    DeleteVFX(arg_4_7, erase_root_only=False)
    End()
    IfActionButton(
        1,
        prompt_text=10010403,
        anchor_entity=arg_8_11,
        anchor_type=CoordEntityType.Region,
        model_point=0,
        line_intersects=arg_0_3,
    )
    IfActionButton(
        2,
        prompt_text=10010407,
        anchor_entity=arg_12_15,
        anchor_type=CoordEntityType.Region,
        model_point=0,
        line_intersects=arg_0_3,
    )
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionTrue(2, 2)
    Move(PLAYER, destination=arg_8_11, destination_type=CoordEntityType.Region, short_move=True)
    SkipLines(1)
    Move(PLAYER, destination=arg_12_15, destination_type=CoordEntityType.Region, short_move=True)
    ForceAnimation(PLAYER, 7410)
    DisableObject(arg_0_3)
    DeleteVFX(arg_4_7, erase_root_only=True)


def Event11405390():
    """ 11405390: Event 11405390 """
    IfFlagOff(1, 9)
    IfActionButton(
        1,
        prompt_text=10010403,
        anchor_entity=Boxes.QuelaagFogPrompt,
        anchor_type=CoordEntityType.Region,
        line_intersects=Objects.o4950_0000,
        boss_version=True,
    )
    IfConditionTrue(0, input_condition=1)
    RotateToFaceEntity(PLAYER, Boxes.QuelaagFogRotationTarget)
    ForceAnimation(PLAYER, 7410)
    Restart()


def Event11405391():
    """ 11405391: Event 11405391 """
    IfFlagOff(1, 9)
    IfFlagOn(1, 11405393)
    IfCharacterType(1, PLAYER, CharacterType.WhitePhantom)
    IfActionButton(
        1,
        prompt_text=10010403,
        anchor_entity=Boxes.QuelaagFogPrompt,
        anchor_type=CoordEntityType.Region,
        trigger_attribute=TriggerAttribute.All,
        line_intersects=Objects.o4950_0000,
    )
    IfConditionTrue(0, input_condition=1)
    RotateToFaceEntity(PLAYER, Boxes.QuelaagFogRotationTarget)
    ForceAnimation(PLAYER, 7410)
    Restart()


def Event11405393():
    """ 11405393: Event 11405393 """
    SkipLinesIfThisEventOn(3)
    IfFlagOff(1, 9)
    IfCharacterInsideRegion(1, PLAYER, region=Boxes.QuelaagCombatStart)
    IfConditionTrue(0, input_condition=1)
    SkipLinesIfClient(1)
    NotifyBossBattleStart()
    ActivateMultiplayerBuffs(Characters.c5280_0000)


@RestartOnRest
def Event11405392():
    """ 11405392: Event 11405392 """
    SkipLinesIfFlagOff(3, 9)
    DisableBackread(Characters.c5280_0000)
    Kill(Characters.c5280_0000, award_souls=False)
    End()
    RunEvent(11405396)
    RunEvent(11405397)
    SkipLinesIfFlagOn(1, 11400000)
    DisableCharacter(Characters.c5280_0000)
    DisableAI(Characters.c5280_0000)
    IfFlagOn(1, 11405393)
    IfCharacterInsideRegion(1, PLAYER, region=Boxes.QuelaagCombatStart)
    IfConditionTrue(0, input_condition=1)
    IfCharacterType(-1, PLAYER, CharacterType.BlackPhantom)
    IfCharacterType(-1, PLAYER, CharacterType.Intruder)
    EndIfConditionTrue(-1)
    SkipLinesIfFlagOn(11, 11400000)
    DeleteVFX(VFX.QuelaagEntranceFog, erase_root_only=False)
    DeleteVFX(VFX.QuelaagExitFog, erase_root_only=False)
    SkipLinesIfMultiplayer(2)
    PlayCutscene(140000, skippable=True, fade_out=False, player_id=PLAYER)
    SkipLines(1)
    PlayCutscene(140000, skippable=False, fade_out=False, player_id=PLAYER)
    WaitFrames(1)
    CreateVFX(VFX.QuelaagEntranceFog)
    CreateVFX(VFX.QuelaagExitFog)
    EnableCharacter(Characters.c5280_0000)
    EnableFlag(11400000)
    EnableAI(Characters.c5280_0000)
    EnableBossHealthBar(Characters.c5280_0000, name=5280, slot=0)


def Event11400001():
    """ 11400001: Event 11400001 """
    IfCharacterDead(0, Characters.c5280_0000)
    EnableFlag(9)
    KillBoss(1400800)
    DisableObject(Objects.o4950_0000)
    DeleteVFX(VFX.QuelaagEntranceFog, erase_root_only=True)
    DisableObject(Objects.o4951_0000)
    DeleteVFX(VFX.QuelaagExitFog, erase_root_only=True)
    DisableNetworkSync()
    Wait(3.0)
    DisableBackread(Characters.c5280_0000)


def Event11405394():
    """ 11405394: Event 11405394 """
    DisableNetworkSync()
    IfFlagOff(1, 9)
    IfFlagOn(1, 11405392)
    SkipLinesIfHost(1)
    IfFlagOn(1, 11405391)
    IfCharacterInsideRegion(1, PLAYER, region=Boxes.QuelaagMusic)
    IfConditionTrue(0, input_condition=1)
    EnableSoundEvent(1403800)


def Event11405395():
    """ 11405395: Event 11405395 """
    DisableNetworkSync()
    IfFlagOn(1, 9)
    IfFlagOn(1, 11405394)
    IfConditionTrue(0, input_condition=1)
    DisableSoundEvent(1403800)


@UnknownRestart
def Event11405396():
    """ 11405396: Event 11405396 """
    IfCharacterAlive(1, Characters.c5280_0000)
    SkipLinesIfConditionTrue(1, 1)
    End()
    IfCharacterBackreadEnabled(0, Characters.c5280_0000)
    CreateNPCPart(
        Characters.c5280_0000,
        npc_part_id=5281,
        part_index=NPCPartType.Part2,
        part_health=300,
        damage_correction=1.0,
        body_damage_correction=1.0,
        is_invincible=False,
        start_in_stop_state=False,
    )
    SetNPCPartEffects(Characters.c5280_0000, npc_part_id=5281, material_sfx_id=75, material_vfx_id=75)
    IfCharacterPartHealthLessThanOrEqual(2, Characters.c5280_0000, npc_part_id=5281, value=0)
    IfHealthLessThanOrEqual(3, Characters.c5280_0000, 0.0)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(3)
    ForceAnimation(Characters.c5280_0000, 3011, wait_for_completion=True)
    Restart()


@UnknownRestart
def Event11405397():
    """ 11405397: Event 11405397 """
    IfCharacterAlive(1, Characters.c5280_0000)
    SkipLinesIfConditionTrue(1, 1)
    End()
    IfCharacterBackreadEnabled(0, Characters.c5280_0000)
    CreateNPCPart(
        Characters.c5280_0000,
        npc_part_id=5280,
        part_index=NPCPartType.Part1,
        part_health=1,
        damage_correction=1.0,
        body_damage_correction=1.0,
        is_invincible=False,
        start_in_stop_state=False,
    )
    SetNPCPartEffects(Characters.c5280_0000, npc_part_id=5280, material_sfx_id=60, material_vfx_id=60)
    IfCharacterPartHealthLessThanOrEqual(2, Characters.c5280_0000, npc_part_id=5280, value=0)
    IfHealthLessThanOrEqual(3, Characters.c5280_0000, 0.0)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(3)
    ForceAnimation(Characters.c5280_0000, 2007, wait_for_completion=True)
    Restart()


@RestartOnRest
def Event11400800():
    """ 11400800: Event 11400800 """
    SkipLinesIfThisEventOff(5)
    DisableCharacter(Characters.c5340_0000)
    DisableSoundEvent(1403801)
    DisableCollision(Collisions.h5810B0)
    DisableCollision(Collisions.h5810B0_0000)
    End()
    IfCharacterDead(0, Characters.c5340_0000)
    EnableFlag(140)
    DisableSoundEvent(1403801)
    DisableCollision(Collisions.h5810B0)
    DisableCollision(Collisions.h5810B0_0000)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterHollow(-1, PLAYER)
    IfConditionTrue(1, input_condition=-1)
    IfPlayerCovenant(1, Covenant.ChaosServant)
    EndIfConditionFalse(1)
    BetrayCurrentCovenant()
    IncrementPvPSin()
    EnableFlag(742)
    SaveRequest()


def Event11405000():
    """ 11405000: Event 11405000 """
    SkipLinesIfThisEventOff(2)
    AddSpecialEffect(Characters.c5340_0000, 5401)
    End()
    IfHealthNotEqual(0, Characters.c5340_0000, 1.0)
    AddSpecialEffect(Characters.c5340_0000, 5401)


@RestartOnRest
def Event11400900():
    """ 11400900: Event 11400900 """
    SkipLinesIfFlagOff(2, 11400902)
    DisableCharacter(Characters.c5240_0000)
    End()
    IfCharacterAlive(1, Characters.c5240_0000)
    SkipLinesIfConditionTrue(2, 1)
    EnableFlag(11400902)
    End()
    DisableNetworkSync()
    IfHealthLessThanOrEqual(0, Characters.c5240_0000, 0.0)
    EnableNetworkSync()
    EzstateAIRequest(Characters.c5240_0000, command_id=1200, slot=0)
    Restart()


def Event11405100(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11405100: Event 11405100 """
    IfCharacterInsideRegion(-1, PLAYER, region=arg_4_7)
    IfCharacterInsideRegion(-1, PLAYER, region=arg_8_11)
    IfCharacterInsideRegion(-1, PLAYER, region=arg_12_15)
    IfConditionTrue(0, input_condition=-1)
    ForceAnimation(arg_0_3, 1, wait_for_completion=True)
    DisableNetworkSync()
    IfCharacterOutsideRegion(1, PLAYER, region=arg_4_7)
    IfCharacterOutsideRegion(1, PLAYER, region=arg_8_11)
    IfCharacterOutsideRegion(1, PLAYER, region=arg_12_15)
    IfConditionTrue(0, input_condition=1)
    EnableNetworkSync()
    Restart()


def Event11405110(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int, arg_20_23: int):
    """ 11405110: Event 11405110 """
    IfCharacterInsideRegion(-1, PLAYER, region=arg_4_7)
    IfCharacterInsideRegion(-1, PLAYER, region=arg_8_11)
    IfCharacterInsideRegion(-1, PLAYER, region=arg_12_15)
    IfCharacterInsideRegion(-1, PLAYER, region=arg_16_19)
    IfCharacterInsideRegion(-1, PLAYER, region=arg_20_23)
    IfConditionTrue(0, input_condition=-1)
    ForceAnimation(arg_0_3, 1, wait_for_completion=True)
    DisableNetworkSync()
    IfCharacterOutsideRegion(1, PLAYER, region=arg_4_7)
    IfCharacterOutsideRegion(1, PLAYER, region=arg_8_11)
    IfCharacterOutsideRegion(1, PLAYER, region=arg_12_15)
    IfCharacterOutsideRegion(1, PLAYER, region=arg_16_19)
    IfCharacterOutsideRegion(1, PLAYER, region=arg_20_23)
    IfConditionTrue(0, input_condition=1)
    EnableNetworkSync()
    Restart()


@RestartOnRest
def Event11405250(_, arg_0_3: int):
    """ 11405250: Event 11405250 """
    IfCharacterDead(1, arg_0_3)
    EndIfConditionTrue(1)
    IfCharacterBackreadEnabled(0, arg_0_3)
    CreateNPCPart(
        arg_0_3,
        npc_part_id=2811,
        part_index=NPCPartType.Part2,
        part_health=100,
        damage_correction=0.0,
        body_damage_correction=0.0,
        is_invincible=True,
        start_in_stop_state=False,
    )
    SetNPCPartBulletDamageScaling(arg_0_3, npc_part_id=2811, desired_scaling=0.0)
    SetNPCPartEffects(arg_0_3, npc_part_id=2811, material_sfx_id=1, material_vfx_id=1)
    IfHealthLessThanOrEqual(0, arg_0_3, 0.0)
    SetNPCPartHealth(arg_0_3, npc_part_id=2811, desired_health=0, overwrite_max=False)


@RestartOnRest
def Event11405300():
    """ 11405300: Event 11405300 """
    RunEvent(11405301, slot=0, args=(1400500, 1, 0, 3290, 3290), arg_types="ihhii")
    RunEvent(11405310, slot=0, args=(1400500, 11405301, 0, 0), arg_types="iiBB")
    RunEvent(11405310, slot=1, args=(1400500, 11405301, 2, 0), arg_types="iiBB")
    RunEvent(
        11405320,
        slot=0,
        args=(1400500, 11405301, Objects.o3910_0000, Objects.o3910_0001, 120, 0),
        arg_types="iiiihh",
    )
    RunEvent(
        11405320,
        slot=1,
        args=(1400500, 11405301, Objects.o3910_0002, Objects.o3910_0003, 126, 0),
        arg_types="iiiihh",
    )
    RunEvent(11405330, slot=0, args=(1400500, 11405301, 1400600, 1400601, 120, 123))
    RunEvent(11405330, slot=1, args=(1400500, 11405301, 1400602, 1400603, 126, 129))
    RunEvent(11405301, slot=1, args=(1400500, 2, 0, 3291, 3291), arg_types="ihhii")
    RunEvent(11405310, slot=2, args=(1400500, 11405302, 5, 0), arg_types="iiBB")
    RunEvent(
        11405320,
        slot=2,
        args=(1400500, 11405302, Objects.o3910_0004, Objects.o3910_0005, 135, 0),
        arg_types="iiiihh",
    )
    RunEvent(11405330, slot=2, args=(1400500, 11405302, 1400604, 1400605, 135, 137))
    RunEvent(11405330, slot=3, args=(1400500, 11405302, 1400606, 1400607, 153, 155))
    RunEvent(11405301, slot=2, args=(1400500, 3, 0, 3292, 3292), arg_types="ihhii")
    RunEvent(11405310, slot=3, args=(1400500, 11405303, 6, 0), arg_types="iiBB")
    RunEvent(11405310, slot=4, args=(1400500, 11405303, 8, 0), arg_types="iiBB")
    RunEvent(
        11405320,
        slot=3,
        args=(1400500, 11405303, Objects.o3910_0006, Objects.o3910_0007, 138, 0),
        arg_types="iiiihh",
    )
    RunEvent(
        11405320,
        slot=4,
        args=(1400500, 11405303, Objects.o3910_0008, Objects.o3910_0009, 144, 0),
        arg_types="iiiihh",
    )
    RunEvent(11405330, slot=4, args=(1400500, 11405303, 1400608, 1400609, 138, 141))
    RunEvent(11405330, slot=5, args=(1400500, 11405303, 1400610, 1400611, 144, 150))
    RunEvent(11405301, slot=3, args=(1400500, 4, 0, 3293, 3293), arg_types="ihhii")
    RunEvent(11405310, slot=5, args=(1400500, 11405304, 4, 0), arg_types="iiBB")
    RunEvent(
        11405320,
        slot=5,
        args=(1400500, 11405304, Objects.o3910_0010, Objects.o3910_0011, 132, 0),
        arg_types="iiiihh",
    )
    RunEvent(11405330, slot=6, args=(1400500, 11405304, 1400612, 1400613, 132, 134))
    RunEvent(11405330, slot=7, args=(1400500, 11405304, 1400614, 1400615, 150, 152))


@UnknownRestart
def Event11405301(_, arg_0_3: int, arg_4_5: short, arg_6_7: short, arg_8_11: int, arg_12_15: int):
    """ 11405301: Event 11405301 """
    EndIfThisEventSlotOn()
    IfCharacterBackreadEnabled(0, arg_0_3)
    CreateNPCPart(
        arg_0_3,
        npc_part_id=arg_6_7,
        part_index=arg_4_5,
        part_health=100,
        damage_correction=1.0,
        body_damage_correction=1.0,
        is_invincible=False,
        start_in_stop_state=False,
    )
    IfCharacterPartHealthLessThanOrEqual(1, arg_0_3, npc_part_id=arg_8_11, value=0)
    IfCharacterDead(2, arg_0_3)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(2)
    DisableFlagRange((11405290, 11405291))
    SkipLinesIfClient(1)
    EnableRandomFlagInRange((11405290, 11405291))
    IfFlagOn(3, 11405290)
    IfFlagOn(4, 11405291)
    IfConditionTrue(-2, input_condition=3)
    IfConditionTrue(-2, input_condition=4)
    IfConditionTrue(0, input_condition=-2)
    SkipLinesIfFinishedConditionTrue(2, 4)
    EnableFlag(11405290)
    SkipLines(1)
    EnableFlag(11405291)
    EnableFlag(arg_12_15)
    SkipLinesIfFlagOff(1, 11405301)
    ForceAnimation(arg_0_3, 8000)
    SkipLinesIfFlagOff(1, 11405302)
    ForceAnimation(arg_0_3, 8010)


@UnknownRestart
def Event11405310(_, arg_0_3: int, arg_4_7: int, arg_8_8: uchar, arg_9_9: uchar):
    """ 11405310: Event 11405310 """
    SkipLinesIfFlagOn(6, arg_4_7)
    IfFlagOn(1, arg_4_7)
    IfCharacterDead(2, arg_0_3)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(2)
    SetDisplayMask(arg_0_3, bit_index=arg_8_8, switch_type=OnOffChange.On)
    SetDisplayMask(arg_0_3, bit_index=arg_9_9, switch_type=OnOffChange.On)


@UnknownRestart
def Event11405320(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_17: short, arg_18_19: short):
    """ 11405320: Event 11405320 """
    DisableObject(arg_8_11)
    DisableObject(arg_12_15)
    EndIfFlagOn(arg_4_7)
    IfFlagOn(1, arg_4_7)
    IfCharacterDead(2, arg_0_3)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(2)
    EnableObject(arg_8_11)
    EnableObject(arg_12_15)
    MoveObjectToCharacter(arg_8_11, character=arg_0_3, model_point=arg_16_17)
    MoveObjectToCharacter(arg_12_15, character=arg_0_3, model_point=arg_18_19)
    DestroyObject(arg_8_11)
    DestroyObject(arg_12_15)


@UnknownRestart
def Event11405330(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int, arg_20_23: int):
    """ 11405330: Event 11405330 """
    EndIfFlagOn(arg_4_7)
    DisableCharacter(arg_8_11)
    DisableCharacter(arg_12_15)
    IfFlagOn(1, arg_4_7)
    IfCharacterDead(2, arg_0_3)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(2)
    ResetAnimation(arg_0_3, disable_interpolation=False)
    Move(
        arg_8_11,
        destination=arg_0_3,
        destination_type=CoordEntityType.Character,
        model_point=arg_16_19,
        copy_draw_parent=arg_0_3,
    )
    Move(
        arg_12_15,
        destination=arg_0_3,
        destination_type=CoordEntityType.Character,
        model_point=arg_20_23,
        copy_draw_parent=arg_0_3,
    )
    EnableCharacter(arg_8_11)
    EnableCharacter(arg_12_15)
    ForceAnimation(arg_8_11, 7000)
    ForceAnimation(arg_12_15, 7000)


@RestartOnRest
def Event11405350(
    _,
    arg_0_3: int,
    arg_4_7: int,
    arg_8_11: int,
    arg_12_15: int,
    arg_16_19: int,
    arg_20_23: int,
    arg_24_27: int,
):
    """ 11405350: Event 11405350 """
    SkipLinesIfEqual(1, left=arg_24_27, right=0)
    SkipLinesIfFlagOn(1, 11400533)
    SkipLinesIfThisEventSlotOff(2)
    SetDisplayMask(arg_0_3, bit_index=2, switch_type=OnOffChange.On)
    End()
    DisableCharacter(arg_4_7)
    DisableCharacter(arg_8_11)
    DisableCharacter(arg_12_15)
    DisableCharacter(arg_16_19)
    DisableCharacter(arg_20_23)
    IfCharacterDead(0, arg_0_3)
    SetDisplayMask(arg_0_3, bit_index=2, switch_type=OnOffChange.On)
    Move(
        arg_4_7,
        destination=arg_0_3,
        destination_type=CoordEntityType.Character,
        model_point=100,
        copy_draw_parent=arg_0_3,
    )
    Move(
        arg_8_11,
        destination=arg_0_3,
        destination_type=CoordEntityType.Character,
        model_point=101,
        copy_draw_parent=arg_0_3,
    )
    Move(
        arg_12_15,
        destination=arg_0_3,
        destination_type=CoordEntityType.Character,
        model_point=102,
        copy_draw_parent=arg_0_3,
    )
    Move(
        arg_16_19,
        destination=arg_0_3,
        destination_type=CoordEntityType.Character,
        model_point=103,
        copy_draw_parent=arg_0_3,
    )
    Move(
        arg_20_23,
        destination=arg_0_3,
        destination_type=CoordEntityType.Character,
        model_point=104,
        copy_draw_parent=arg_0_3,
    )
    EnableCharacter(arg_4_7)
    EnableCharacter(arg_8_11)
    EnableCharacter(arg_12_15)
    EnableCharacter(arg_16_19)
    EnableCharacter(arg_20_23)
    ForceAnimation(arg_4_7, 7000)
    ForceAnimation(arg_8_11, 7000)
    ForceAnimation(arg_12_15, 7000)
    ForceAnimation(arg_16_19, 7000)
    ForceAnimation(arg_20_23, 7000)


def Event11400100(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 11400100: Event 11400100 """
    SkipLinesIfFlagOn(1, arg_0_3)
    IfCharacterInsideRegion(0, PLAYER, region=arg_4_7)
    EnableFlag(arg_0_3)
    DisableSpawner(arg_8_11)
    IfAllPlayersOutsideRegion(0, region=arg_4_7)
    DisableFlag(arg_0_3)
    EnableSpawner(arg_8_11)
    Restart()


@RestartOnRest
def Event11400850(_, arg_0_3: int, arg_4_7: int):
    """ 11400850: Event 11400850 """
    SkipLinesIfThisEventSlotOff(3)
    DisableCharacter(arg_0_3)
    Kill(arg_0_3, award_souls=False)
    End()
    IfCharacterDead(0, arg_0_3)
    EndIfEqual(left=arg_4_7, right=0)
    IfCharacterHuman(-7, PLAYER)
    IfCharacterHollow(-7, PLAYER)
    EndIfConditionFalse(-7)
    AwardItemLot(arg_4_7, host_only=True)


def Event11400600(_, arg_0_3: int, arg_4_7: int):
    """ 11400600: Event 11400600 """
    SkipLinesIfThisEventSlotOff(4)
    EndOfAnimation(arg_0_3, 0)
    DisableObjectActivation(arg_0_3, obj_act_id=-1)
    EnableTreasure(arg_0_3)
    End()
    DisableTreasure(arg_0_3)
    IfObjectActivated(0, obj_act_id=arg_4_7)
    WaitFrames(10)
    EnableTreasure(arg_0_3)


def Event11400200():
    """ 11400200: Event 11400200 """
    SkipLinesIfThisEventOff(2)
    DisableObjectActivation(Objects.o4560_0000, obj_act_id=-1)
    End()
    IfObjectActivated(0, obj_act_id=11400201)
    TriggerMultiplayerEvent(10010)
    IfHealthGreaterThan(0, PLAYER, 0.0)
    DisableBackread(Characters.c5280_0000)
    DisableBackread(Characters.c5340_0000)
    WaitFrames(1)
    SkipLinesIfFlagOn(2, 11010700)
    PlayCutscene(140010, skippable=True, fade_out=False, player_id=PLAYER)
    SkipLines(2)
    PlayCutscene(140015, skippable=True, fade_out=False, player_id=PLAYER)
    EnableFlag(11500200)
    WaitFrames(1)
    SkipLinesIfFlagOn(1, 9)
    EnableBackread(Characters.c5280_0000)
    EnableBackread(Characters.c5340_0000)
    EnableFlag(11400200)
    AwardAchievement(30)
    AwardItemLot(9030, host_only=True)


def Event11415170():
    """ 11415170: Event 11415170 """
    IfMultiplayerEvent(0, 10010)
    DisableNetworkSync()
    PlaySoundEffect(anchor_entity=Objects.o4550_0000, sound_type=SoundType.o_Object, sound_id=130300002)
    WaitRandomSeconds(min_seconds=0.5, max_seconds=2.0)
    PlaySoundEffect(anchor_entity=Objects.o4550_0000, sound_type=SoundType.o_Object, sound_id=130300002)
    WaitRandomSeconds(min_seconds=0.5, max_seconds=2.0)
    PlaySoundEffect(anchor_entity=Objects.o4550_0000, sound_type=SoundType.o_Object, sound_id=130300002)
    Restart()


def Event11400210():
    """ 11400210: Event 11400210 """
    SkipLinesIfThisEventOff(2)
    DisableObject(Objects.o4570_0000)
    End()
    IfObjectDestroyed(0, Objects.o4570_0000)
    EnableFlag(11400210)


def Event11400220():
    """ 11400220: Event 11400220 """
    DisableNetworkSync()
    IfCharacterInsideRegion(0, PLAYER, region=Spheres.QuelanaArea)
    AddSpecialEffect(PLAYER, 4140)
    Restart()


def Event11400230():
    """ 11400230: Event 11400230 """
    DisableNetworkSync()
    SkipLinesIfFlagOff(2, 590)
    EndOfAnimation(m10_00_Objects.o1309, 1)
    End()
    IfSingleplayer(1)
    IfFlagOff(1, 590)
    IfActionButton(
        1,
        prompt_text=10010400,
        anchor_entity=m10_00_Objects.o1309,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        model_point=101,
        trigger_attribute=TriggerAttribute.All,
    )
    IfConditionTrue(0, input_condition=1)
    DisplayDialog(
        10010161,
        anchor_entity=m10_00_Objects.o1309,
        display_distance=3.0,
        button_type=ButtonType.OK_or_Cancel,
        number_buttons=NumberButtons.NoButton,
    )
    Restart()


@RestartOnRest
def Event11405200(_, arg_0_3: int, arg_4_7: int):
    """ 11405200: Event 11405200 """
    SkipLinesIfThisEventSlotOff(2)
    ResetStandbyAnimationSettings(arg_0_3)
    End()
    RestoreObject(arg_4_7)
    DisableCharacterCollision(arg_0_3)
    DisableGravity(arg_0_3)
    Move(arg_0_3, destination=arg_4_7, destination_type=CoordEntityType.Object, model_point=100, short_move=True)
    IfAttacked(-1, arg_0_3, attacker=PLAYER)
    IfObjectDestroyed(-1, arg_4_7)
    IfConditionTrue(0, input_condition=-1)
    ResetStandbyAnimationSettings(arg_0_3)
    EnableCharacterCollision(arg_0_3)
    EnableGravity(arg_0_3)


def Event11400510(_, arg_0_3: int, arg_4_7: int):
    """ 11400510: Event 11400510 """
    IfHealthLessThanOrEqual(1, arg_0_3, 0.8999999761581421)
    IfHealthGreaterThan(1, arg_0_3, 0.0)
    IfAttacked(1, arg_0_3, attacker=PLAYER)
    IfFlagOn(2, arg_4_7)
    IfThisEventSlotOn(2)
    IfFlagOn(3, arg_4_7)
    IfThisEventSlotOff(3)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionFalse(2, 3)
    DisableCharacter(arg_0_3)
    IfFlagOn(0, 703)
    EnableFlag(arg_4_7)
    SetTeamTypeAndExitStandbyAnimation(arg_0_3, TeamType.HostileAlly)
    SaveRequest()


def Event11400520(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11400520: Event 11400520 """
    SkipLinesIfThisEventSlotOff(2)
    DropMandatoryTreasure(arg_0_3)
    End()
    IfHealthLessThanOrEqual(0, arg_0_3, 0.0)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)


def Event11400501(_, arg_0_3: int, arg_4_7: int):
    """ 11400501: Event 11400501 """
    IfFlagOff(1, 1282)
    IfFlagOff(1, 1283)
    IfFlagOff(1, 1284)
    IfFlagOff(1, 1287)
    IfFlagOn(1, 1272)
    IfThisEventOff(1)
    IfFlagOn(2, arg_4_7)
    IfThisEventOn(2)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EnableFlag(arg_4_7)
    SetTeamTypeAndExitStandbyAnimation(arg_0_3, TeamType.HostileAlly)
    SaveRequest()


def Event11400502(_, arg_0_3: int, arg_4_7: int):
    """ 11400502: Event 11400502 """
    IfFlagOff(1, 1282)
    IfFlagOff(1, 1283)
    IfFlagOff(1, 1287)
    IfFlagOn(-2, 1280)
    IfFlagOn(-2, 1281)
    IfConditionTrue(1, input_condition=-2)
    IfHealthLessThanOrEqual(1, arg_0_3, 0.8999999761581421)
    IfHealthGreaterThan(1, arg_0_3, 0.0)
    IfAttacked(1, arg_0_3, attacker=PLAYER)
    IfFlagOn(2, arg_4_7)
    IfThisEventOn(2)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EnableFlag(arg_4_7)
    SetTeamTypeAndExitStandbyAnimation(arg_0_3, TeamType.HostileAlly)
    SaveRequest()


def Event11400503(_, arg_0_3: int, arg_4_7: int):
    """ 11400503: Event 11400503 """
    IfFlagOff(1, 1282)
    IfFlagOff(1, 1283)
    IfFlagOff(1, 1287)
    IfFlagOn(1, 1286)
    IfHealthLessThanOrEqual(1, arg_0_3, 0.8999999761581421)
    IfHealthGreaterThan(1, arg_0_3, 0.0)
    IfAttacked(1, arg_0_3, attacker=PLAYER)
    IfFlagOn(2, arg_4_7)
    IfThisEventOn(2)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EnableFlag(arg_4_7)
    SetTeamTypeAndExitStandbyAnimation(arg_0_3, TeamType.HostileAlly)
    SaveRequest()


def Event11400504(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 11400504: Event 11400504 """
    IfFlagOff(1, 1603)
    IfFlagOn(1, 1601)
    IfHealthLessThanOrEqual(1, arg_0_3, 0.8999999761581421)
    IfHealthGreaterThan(1, arg_0_3, 0.0)
    IfAttacked(1, arg_0_3, attacker=PLAYER)
    IfThisEventOff(1)
    IfFlagOff(2, 1763)
    IfFlagOn(2, 1760)
    IfHealthLessThanOrEqual(2, arg_8_11, 0.8999999761581421)
    IfHealthGreaterThan(2, arg_8_11, 0.0)
    IfAttacked(2, arg_8_11, attacker=PLAYER)
    IfThisEventOff(2)
    IfFlagOn(-2, arg_4_7)
    IfFlagOn(-2, 1763)
    IfFlagOn(-2, 745)
    IfConditionTrue(3, input_condition=-2)
    IfThisEventOff(3)
    IfConditionTrue(4, input_condition=-2)
    IfThisEventOn(4)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(-1, input_condition=4)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionTrue(4, 4)
    SkipLinesIfFlagOn(1, 1604)
    EnableFlag(arg_4_7)
    SkipLinesIfFlagOn(1, 1764)
    EnableFlag(1763)
    EnableCharacter(arg_0_3)
    SetTeamTypeAndExitStandbyAnimation(arg_0_3, TeamType.Enemy)
    EnableCharacter(arg_8_11)
    SetTeamTypeAndExitStandbyAnimation(arg_8_11, TeamType.Enemy)
    EndIfThisEventOn()
    IfCharacterHuman(-7, PLAYER)
    IfCharacterHollow(-7, PLAYER)
    IfConditionTrue(7, input_condition=-7)
    IfPlayerCovenant(7, Covenant.ForestHunter)
    EndIfConditionFalse(7)
    BetrayCurrentCovenant()
    EnableFlag(742)
    EnableFlag(746)
    SaveRequest()


def Event11400530(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11400530: Event 11400530 """
    IfFlagOff(1, 1253)
    IfFlagOn(1, 1256)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)
    EnableCharacter(arg_0_3)
    SetTeamTypeAndExitStandbyAnimation(arg_0_3, TeamType.HostileAlly)


def Event11400531(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11400531: Event 11400531 """
    IfFlagOff(1, 1282)
    IfFlagOff(1, 1283)
    IfFlagOff(1, 1287)
    IfFlagOn(1, 1280)
    IfFlagOn(1, 11400593)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)
    EnableFlag(11405001)
    SetNest(arg_0_3, Boxes.EingyiMoveTarget)
    SetTeamTypeAndExitStandbyAnimation(arg_0_3, TeamType.FightingAlly)
    AICommand(arg_0_3, command_id=10, slot=0)
    ReplanAI(arg_0_3)
    IfCharacterInsideRegion(2, arg_0_3, region=Boxes.EingyiNest)
    IfAttacked(3, arg_0_3, attacker=PLAYER)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    DisableFlag(11405001)
    SkipLinesIfFinishedConditionTrue(1, 3)
    SetTeamTypeAndExitStandbyAnimation(arg_0_3, TeamType.Ally)
    AICommand(arg_0_3, command_id=-1, slot=0)
    ReplanAI(arg_0_3)


def Event11400532(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11400532: Event 11400532 """
    IfFlagOff(1, 1282)
    IfFlagOff(1, 1283)
    IfFlagOff(1, 1287)
    IfFlagOn(1, 1281)
    IfFlagOn(1, 753)
    IfCharacterAlive(1, arg_0_3)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)


@RestartOnRest
def Event11400533():
    """ 11400533: Event 11400533 """
    SkipLinesIfThisEventOff(6)
    DisableCharacter(Characters.c3220_0000)
    DisableCharacter(Characters.c3220_0001)
    DisableCharacter(Characters.c3220_0002)
    DisableCharacter(Characters.c3220_0003)
    DisableCharacter(Characters.c3220_0004)
    End()
    IfCharacterDead(0, Characters.c3210_0000)
    End()


def Event11400536(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11400536: Event 11400536 """
    IfFlagOff(1, 1294)
    IfFlagOn(1, 1290)
    IfPlayerHasWeapon(-1, 1331000, including_box=False)
    IfPlayerHasWeapon(-1, 1331100, including_box=False)
    IfPlayerHasWeapon(-1, 1331200, including_box=False)
    IfPlayerHasWeapon(-1, 1331300, including_box=False)
    IfPlayerHasWeapon(-1, 1331400, including_box=False)
    IfPlayerHasWeapon(-1, 1331500, including_box=False)
    IfPlayerHasWeapon(-1, 1332000, including_box=False)
    IfPlayerHasWeapon(-1, 1332100, including_box=False)
    IfPlayerHasWeapon(-1, 1332200, including_box=False)
    IfPlayerHasWeapon(-1, 1332300, including_box=False)
    IfPlayerHasWeapon(-1, 1332400, including_box=False)
    IfPlayerHasWeapon(-1, 1332500, including_box=False)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)
    EnableCharacter(arg_0_3)


def Event11400537(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11400537: Event 11400537 """
    IfFlagOff(1, 1294)
    IfFlagOn(1, 1293)
    IfFlagOn(1, 11400595)
    IfCharacterAlive(1, arg_0_3)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)


def Event11400538(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11400538: Event 11400538 """
    IfFlagOff(1, 1294)
    IfFlagOn(1, 1291)
    IfFlagOn(1, 10)
    IfCharacterAlive(1, arg_0_3)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)


def Event11400539(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11400539: Event 11400539 """
    IfFlagOn(1, 1290)
    IfFlagOn(1, 10)
    IfFlagOff(2, 1294)
    IfFlagOn(2, 1291)
    IfFlagOff(2, 71400061)
    IfFlagOn(2, 10)
    IfFlagOff(3, 1294)
    IfFlagOn(3, 1292)
    IfCharacterBackreadDisabled(3, arg_0_3)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)
    DisableCharacter(arg_0_3)


def Event11400551(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11400551: Event 11400551 """
    IfFlagOff(1, 1512)
    IfFlagOn(1, 1497)
    IfFlagOn(1, 11020592)
    IfInsideMap(1, game_map=BLIGHTTOWN)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)
    EnableCharacter(arg_0_3)
    EnableFlag(814)


def Event11400552(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11400552: Event 11400552 """
    IfFlagOff(1, 1512)
    IfFlagOn(1, 1501)
    IfFlagOn(1, 11400590)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)
    EnableCharacter(arg_0_3)


def Event11400553():
    """ 11400553: Event 11400553 """
    EndIfClient()
    EndIfThisEventOn()
    IfFlagOn(0, 11400590)
    End()


def Event11400554(_, arg_0_3: int):
    """ 11400554: Event 11400554 """
    SkipLinesIfThisEventOff(2)
    ResetStandbyAnimationSettings(arg_0_3)
    End()
    IfThisEventOn(-1)
    IfFlagOn(-1, 1501)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfThisEventOn(1)
    IfFlagOff(0, 814)
    SetStandbyAnimationSettings(arg_0_3, cancel_animation=7856)


def Event11400560(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int):
    """ 11400560: Event 11400560 """
    IfHost(1)
    IfPlayerCovenant(1, Covenant.ForestHunter)
    IfFlagOff(1, 1603)
    IfFlagOn(1, 1600)
    IfFlagOn(1, 11400582)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)
    EnableCharacter(arg_0_3)
    EnableCharacter(arg_16_19)
    DisableFlag(1766)
    EnableFlag(11405022)


def Event11400566(_, arg_0_3: int, arg_4_7: int):
    """ 11400566: Event 11400566 """
    SkipLinesIfHost(1)
    EndIfFlagOn(11405022)
    IfFlagOn(1, 746)
    EndIfConditionFalse(1)
    WaitFrames(1)
    DisableCharacter(arg_0_3)
    DisableCharacter(arg_4_7)
    EnableFlag(1766)
    DisableFlag(11405022)


def Event11400567(_, arg_0_3: int, arg_4_7: int):
    """ 11400567: Event 11400567 """
    IfHost(1)
    IfPlayerCovenant(2, Covenant.ForestHunter)
    IfConditionFalse(1, input_condition=2)
    IfFlagOff(1, 746)
    IfConditionTrue(0, input_condition=1)
    WaitFrames(1)
    DisableCharacter(arg_0_3)
    DisableCharacter(arg_4_7)
    DisableFlag(11405022)


def Event140():
    """ 140: Event 140 """
    DisableNetworkSync()
    IfThisEventOn(1)
    IfActionButton(
        1,
        prompt_text=10010182,
        anchor_entity=Objects.o0200_0000,
        anchor_type=CoordEntityType.Object,
        max_distance=3.4000000953674316,
        model_point=-1,
    )
    IfConditionTrue(0, input_condition=1)
    DisplayDialog(
        10010184,
        anchor_entity=Objects.o0200_0000,
        display_distance=3.4000000953674316,
        button_type=ButtonType.Yes_or_No,
        number_buttons=NumberButtons.NoButton,
    )
    Restart()


def Event11405030():
    """ 11405030: Event 11405030 """
    SkipLinesIfClient(1)
    SetNetworkUpdateAuthority(Characters.c0000_0010, UpdateAuthority.Forced)
    SkipLinesIfFlagOn(3, 11405033)
    IfClient(2)
    IfFlagOn(2, 11405031)
    SkipLinesIfConditionTrue(1, 2)
    DisableCharacter(Characters.c0000_0010)
    EndIfFlagOn(9)
    IfHost(1)
    IfCharacterHuman(1, PLAYER)
    IfFlagOn(1, 11400901)
    IfCharacterBackreadEnabled(1, Characters.c0000_0010)
    IfConditionTrue(0, input_condition=1)
    PlaceSummonSign(
        SummonSignType.BlueEyeSign,
        Characters.c0000_0010,
        region=Points.MildredSummonSign,
        summon_flag=11405031,
        dismissal_flag=11405033,
    )


def Event14005990(_, arg_0_3: int, arg_4_7: int):
    """ 14005990: Event 14005990 """
    IfFlagOn(0, arg_0_3)
    EraseNPCSummonSign(summoned_character=arg_4_7)
    IfFlagOff(0, arg_0_3)
    Restart()


def Event11405029():
    """ 11405029: Event 11405029 """
    SkipLinesIfClient(1)
    SetNetworkUpdateAuthority(Characters.c0000_0010, UpdateAuthority.Forced)
    SkipLinesIfFlagOn(3, 11405033)
    IfClient(2)
    IfFlagOn(2, 11405031)
    SkipLinesIfConditionTrue(1, 2)
    DisableCharacter(Characters.c0000_0010)
    EndIfFlagOn(9)
    IfMultiplayerCount(1, arg1=4, arg2=3)
    IfHost(1)
    IfCharacterHuman(1, PLAYER)
    IfFlagOff(1, 11405031)
    IfFlagOff(1, 11405033)
    IfFlagOn(1, 11400901)
    IfCharacterBackreadEnabled(1, Characters.c0000_0010)
    IfCharacterHasSpecialEffect(1, PLAYER, 28)
    IfConditionTrue(0, input_condition=1)
    PlaceSummonSign(
        SummonSignType.BlueEyeSign,
        Characters.c0000_0010,
        region=Points.MildredSummonSign,
        summon_flag=11405031,
        dismissal_flag=11405033,
    )


def Event11405032():
    """ 11405032: Event 11405032 """
    EndIfThisEventOn()
    IfFlagOn(1, 11405031)
    IfFlagOn(1, 11405393)
    IfConditionTrue(0, input_condition=1)
    AICommand(Characters.c0000_0010, command_id=10, slot=0)
    ReplanAI(Characters.c0000_0010)
    IfCharacterInsideRegion(0, Characters.c0000_0010, region=Boxes.QuelaagFogPrompt)
    RotateToFaceEntity(Characters.c0000_0010, Boxes.QuelaagFogRotationTarget)
    ForceAnimation(Characters.c0000_0010, 7410)
    AICommand(Characters.c0000_0010, command_id=-1, slot=0)
    ReplanAI(Characters.c0000_0010)


def Event11405035():
    """ 11405035: Event 11405035 """
    DisableNetworkSync()
    EndIfClient()
    EndIfFlagOn(11405036)
    EndIfFlagOn(9)
    IfHost(1)
    IfCharacterHuman(1, PLAYER)
    IfFlagOff(1, 11400901)
    SkipLinesIfThisEventOn(1)
    IfCharacterInsideRegion(1, PLAYER, region=Spheres.MildredInvaderTrigger)
    IfConditionTrue(0, input_condition=1)
    PlaceSummonSign(
        SummonSignType.BlackEyeSign,
        Characters.c0000_0007,
        region=Points.MildredInvaderSpawn,
        summon_flag=11405036,
        dismissal_flag=11405037,
    )
    Wait(20.0)
    Restart()


def Event11400901():
    """ 11400901: Event 11400901 """
    SkipLinesIfHost(3)
    IfFlagOn(1, 11405036)
    IfFlagOff(1, 11405037)
    SkipLinesIfConditionTrue(1, 1)
    DisableCharacter(Characters.c0000_0007)
    EndIfThisEventOn()
    IfCharacterDead(0, Characters.c0000_0007)
    EnableFlag(11400901)


def Event11405843(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11405843: Event 11405843 """
    IfHost(1)
    IfMultiplayer(1)
    IfFlagOn(1, arg_0_3)
    IfActionButton(
        1,
        prompt_text=10010403,
        anchor_entity=arg_8_11,
        anchor_type=CoordEntityType.Region,
        line_intersects=arg_4_7,
        boss_version=True,
    )
    IfConditionTrue(0, input_condition=1)
    RotateToFaceEntity(PLAYER, arg_12_15)
    ForceAnimation(PLAYER, 7410, wait_for_completion=True)
    Unknown_2003_47()
    Restart()


def Event11405846(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 11405846: Event 11405846 """
    IfMultiplayer(-1)
    IfUnknownPlayerType5(-1)
    IfConditionTrue(1, input_condition=-1)
    IfFlagOn(1, arg_0_3)
    IfConditionTrue(0, input_condition=1)
    EnableObject(arg_4_7)
    CreateVFX(arg_8_11)
    IfUnknownPlayerType5(3)
    IfConditionFalse(2, input_condition=3)
    IfSingleplayer(2)
    IfConditionTrue(0, input_condition=2)
    DisableObject(arg_4_7)
    DeleteVFX(arg_8_11, erase_root_only=True)
    Restart()
