"""
linked:


strings:

"""
from soulstruct.darksouls1r.events import *
from ..entities.m18_01_00_00_entities import *
from ..entities.m10_02_00_00_entities import SpawnPoints as m10_02_SpawnPoints, Boxes as m10_02_Boxes
from ..entities.common_entities import *


def Constructor():
    """ 0: Event 0 """
    RegisterBonfire(
        11810992,
        obj=Objects.o0200_0000,
        reaction_distance=1.0,
        reaction_angle=180.0,
        initial_kindle_level=0,
    )
    RegisterBonfire(
        11810984,
        obj=Objects.o0200_0001,
        reaction_distance=1.0,
        reaction_angle=180.0,
        initial_kindle_level=0,
    )
    RegisterLadder(start_climbing_flag=11810010, stop_climbing_flag=11810011, obj=Objects.o8500_0000)
    DisableCollision(Collisions.h0550B1_0000)
    DisableFlag(11810315)
    DisableFlag(11810112)
    DisableObjectActivation(Objects.o8540_0000, obj_act_id=-1)
    DisableObjectActivation(Objects.o8540_0001, obj_act_id=-1)
    DisableObjectActivation(Objects.o8540_0002, obj_act_id=-1)
    SkipLinesIfOutsideMap(4, game_map=UNDEAD_ASYLUM)
    SkipLinesIfFlagOn(3, 11810002)
    PlayCutscene(
        180101,
        skippable=True,
        fade_out=True,
        player_id=PLAYER,
        move_to_region=Boxes.StartPointAfterCutscene,
        move_to_map=UNDEAD_ASYLUM,
    )
    EnableFlag(11810002)
    SetRespawnPoint(SpawnPoints.SpawnPointAtStart)
    RunEvent(
        11810090,
        slot=0,
        args=(Objects.o8952_0000, VFX.CheckpointFog1, Boxes.CheckpointFog1FrontSide, Boxes.CheckpointFog1BackSide),
    )
    RunEvent(11810000)
    RunEvent(11810150)
    RunEvent(11810211)
    RunEvent(11810200, slot=1, args=(Objects.o8520_0000, Objects.o8520_0001, Objects.o8521_0000))
    RunEvent(11810310)
    RunEvent(11810311)
    RunEvent(11810312)
    RunEvent(11810313)
    RunEvent(11810120)
    RunEvent(11810110)
    RunEvent(11810111)
    RunEvent(11810450)
    RunEvent(11810320)
    RunEvent(11810300)
    RunEvent(11810850, slot=0, args=(Characters.c2792_0000, 27907000))
    RunEvent(11810850, slot=1, args=(Characters.c2792_0001, 27907000))
    SkipLinesIfClient(44)
    RunEvent(11810641, slot=0, args=(3, 111, 11810601, 51810800))
    RunEvent(11810641, slot=1, args=(3, 270, 11810602, 51810810))
    RunEvent(11810641, slot=2, args=(3, 271, 11810603, 51810820))
    RunEvent(11810641, slot=3, args=(3, 272, 11810604, 51810830))
    RunEvent(11810641, slot=4, args=(3, 275, 11810605, 51810840))
    RunEvent(11810641, slot=5, args=(3, 293, 11810606, 51810850))
    RunEvent(11810641, slot=6, args=(3, 350, 11810607, 51810860))
    RunEvent(11810641, slot=7, args=(3, 500, 11810607, 51810860))
    RunEvent(11810641, slot=8, args=(3, 370, 11810608, 51810870))
    RunEvent(11810641, slot=9, args=(3, 375, 11810609, 51810880))
    RunEvent(11810641, slot=10, args=(3, 376, 11810610, 51810890))
    RunEvent(11810641, slot=11, args=(3, 380, 11810611, 51810900))
    RunEvent(11810641, slot=12, args=(3, 385, 11810612, 51810910))
    RunEvent(11810641, slot=13, args=(3, 501, 11810613, 51810920))
    RunEvent(11810641, slot=14, args=(0, 1330000, 11810614, 51810930))
    RunEvent(11810641, slot=15, args=(0, 1332000, 11810615, 51810940))
    RunEvent(11810641, slot=16, args=(0, 1396000, 11810616, 51810950))
    RunEvent(11810641, slot=17, args=(1, 190000, 11810617, 51810960))
    RunEvent(11810641, slot=18, args=(1, 290000, 11810618, 51810970))
    RunEvent(11810641, slot=19, args=(1, 560000, 11810619, 51810980))
    RunEvent(11810641, slot=20, args=(2, 130, 11810620, 51810990))
    RunEvent(11810641, slot=21, args=(3, 711, 11810621, 51811000))
    RunEvent(11810600)
    RunEvent(11815110, slot=0, args=(11810601, 3000, 51810800))
    RunEvent(11815110, slot=1, args=(11810602, 3010, 51810810))
    RunEvent(11815110, slot=2, args=(11810603, 3020, 51810820))
    RunEvent(11815110, slot=3, args=(11810604, 3030, 51810830))
    RunEvent(11815110, slot=4, args=(11810605, 3040, 51810840))
    RunEvent(11815110, slot=5, args=(11810606, 3050, 51810850))
    RunEvent(11815110, slot=6, args=(11810607, 3060, 51810860))
    RunEvent(11815110, slot=7, args=(11810608, 3070, 51810870))
    RunEvent(11815110, slot=8, args=(11810609, 3080, 51810880))
    RunEvent(11815110, slot=9, args=(11810610, 3090, 51810890))
    RunEvent(11815110, slot=10, args=(11810611, 3100, 51810900))
    RunEvent(11815110, slot=11, args=(11810612, 3110, 51810910))
    RunEvent(11815110, slot=12, args=(11810613, 3120, 51810920))
    RunEvent(11815110, slot=13, args=(11810614, 3130, 51810930))
    RunEvent(11815110, slot=14, args=(11810615, 3140, 51810940))
    RunEvent(11815110, slot=15, args=(11810616, 3150, 51810950))
    RunEvent(11815110, slot=16, args=(11810617, 3160, 51810960))
    RunEvent(11815110, slot=17, args=(11810618, 3170, 51810970))
    RunEvent(11815110, slot=18, args=(11810619, 3180, 51810980))
    RunEvent(11815110, slot=19, args=(11810620, 3190, 51810990))
    RunEvent(11815110, slot=20, args=(11810621, 3200, 51811000))
    RunEvent(11810100, slot=0, args=(11810100, Objects.o8540_0000, 10010869))
    RunEvent(11810100, slot=1, args=(11810101, Objects.o8540_0001, 10010869))
    RunEvent(11810100, slot=2, args=(11810102, Objects.o8540_0002, 10010869))
    RunEvent(11810100, slot=3, args=(11810103, Objects.o8540_0003, 10010869))
    RunEvent(11810100, slot=4, args=(11810104, Objects.o8540_0004, 10010875))
    RunEvent(11810100, slot=5, args=(11810105, Objects.o8540_0005, 0))
    RunEvent(11810100, slot=6, args=(11810106, Objects.o8540_06, 10010871))
    RunEvent(11815150)
    RunEvent(
        11810400,
        slot=0,
        args=(0, Objects.o0500_0033, Objects.o0500_0023, Objects.o0500_0023, 0, 0, 0, 0),
        arg_types="BiiiBBBB",
    )
    RunEvent(
        11810400,
        slot=1,
        args=(1, Objects.o0500_0034, Objects.o0500_0024, Objects.o0500_0024, 0, 0, 0, 0),
        arg_types="BiiiBBBB",
    )
    RunEvent(
        11810400,
        slot=2,
        args=(2, Objects.o0500_0035, Objects.o0500_0025, Objects.o0500_0025, 0, 0, 0, 0),
        arg_types="BiiiBBBB",
    )
    RunEvent(
        11810400,
        slot=3,
        args=(3, Objects.o0500_0036, Objects.o0500_0026, Objects.o0500_0026, 0, 0, 0, 0),
        arg_types="BiiiBBBB",
    )
    RunEvent(
        11810400,
        slot=4,
        args=(4, Objects.o0500_0037, Objects.o0500_0027, Objects.o0500_0027, 0, 0, 0, 0),
        arg_types="BiiiBBBB",
    )
    RunEvent(
        11810400,
        slot=5,
        args=(5, Objects.o0500_0038, Objects.o0500_0028, Objects.o0500_0043, 0, 0, 0, 0),
        arg_types="BiiiBBBB",
    )
    RunEvent(
        11810400,
        slot=6,
        args=(6, Objects.o0500_0039, Objects.o0500_0029, Objects.o0500_0044, 1, 0, 0, 0),
        arg_types="BiiiBBBB",
    )
    RunEvent(
        11810400,
        slot=7,
        args=(7, Objects.o0500_0040, Objects.o0500_0030, Objects.o0500_0045, 0, 0, 0, 0),
        arg_types="BiiiBBBB",
    )
    RunEvent(
        11810400,
        slot=8,
        args=(8, Objects.o0500_0041, Objects.o0500_0031, Objects.o0500_0046, 0, 0, 0, 0),
        arg_types="BiiiBBBB",
    )
    RunEvent(
        11810400,
        slot=9,
        args=(9, Objects.o0500_0042, Objects.o0500_0032, Objects.o0500_0032, 0, 0, 0, 0),
        arg_types="BiiiBBBB",
    )
    DisableSoundEvent(1813800)
    SkipLinesIfFlagOn(2, 11810312)
    DisableFlag(11810310)
    DisableFlag(11810314)
    SkipLinesIfFlagOff(1, 61810105)
    DisableObjectActivation(Objects.o8541_0001, obj_act_id=-1)
    SkipLinesIfFlagOff(7, 16)
    RunEvent(11815392)
    DisableObject(Objects.o8950_0000)
    DeleteVFX(VFX.AsylumTopEntranceFog, erase_root_only=False)
    EndOfAnimation(Objects.o8542_0000, 1)
    EndOfAnimation(Objects.o8541_0001, 1)
    DisableObjectActivation(Objects.o8541_0001, obj_act_id=-1)
    SkipLines(6)
    RunEvent(11815390)
    RunEvent(11815393)
    RunEvent(11815392)
    RunEvent(11810001)
    RunEvent(11815394)
    RunEvent(11815395)
    DisableObject(Objects.o8953_0000)
    DeleteVFX(VFX.StrayDemonLadderFog, erase_root_only=False)
    DisableSoundEvent(1813801)
    # <!--!>

    EndIfFlagOff(11810000)
    SkipLinesIfFlagOff(2, 11810900)
    RunEvent(11815382)
    SkipLines(4)
    RunEvent(11815382)
    RunEvent(11810900)
    RunEvent(11815384)
    RunEvent(11815385)


def Preconstructor():
    """ 50: Event 50 """
    SkipLinesIfClient(11)
    SkipLinesIfFlagOn(10, 705)
    IfNewGameCycleGreaterThanOrEqual(1, completion_count=1)
    SkipLinesIfConditionFalse(8, 1)
    EnableFlag(705)
    EnableFlag(50000082)
    SetRespawnPoint(SpawnPoints.SpawnPointAtStart)
    DisableFlag(11807200)
    DisableFlag(11807210)
    DisableFlag(11807220)
    DisableFlag(11807240)
    RunEvent(11810050)
    RunEvent(11810350)
    RunEvent(11810220)
    HumanityRegistration(Characters.c0000_0002, 8326)
    SkipLinesIfFlagOn(1, 1061)
    DisableCharacter(Characters.c0000_0003)
    SetTeamType(Characters.c0000_0003, TeamType.HostileAlly)
    RunEvent(11810520, slot=0, args=(Characters.c0000_0002, 1060, 1074, 1073))
    RunEvent(11810530, slot=0, args=(Characters.c0000_0002,))
    RunEvent(11810531, slot=0, args=(Characters.c0000_0003, 1060, 1074, 1061))
    RunEvent(11810532, slot=0, args=(Characters.c0000_0003, 1060, 1074, 1062))
    RunEvent(11815010)


def Event11810090(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11810090: Event 11810090 """
    SkipLinesIfThisEventSlotOff(3)
    DisableObject(arg_0_3)
    DeleteVFX(arg_4_7, erase_root_only=False)
    End()
    IfActionButton(
        1,
        prompt_text=10010403,
        anchor_entity=arg_8_11,
        anchor_type=CoordEntityType.Region,
        line_intersects=arg_0_3,
    )
    IfActionButton(
        2,
        prompt_text=10010407,
        anchor_entity=arg_12_15,
        anchor_type=CoordEntityType.Region,
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


def Event11815390():
    """ 11815390: Event 11815390 """
    IfFlagOff(1, 16)
    IfActionButton(
        1,
        prompt_text=10010403,
        anchor_entity=Boxes.AsylumDemonFogPrompt,
        anchor_type=CoordEntityType.Region,
        line_intersects=Objects.o8950_0000,
    )
    IfConditionTrue(0, input_condition=1)
    Move(
        Characters.c2232_0000,
        destination=Boxes.AsylumDemonWatchingBalcony,
        destination_type=CoordEntityType.Region,
        short_move=True,
    )
    RotateToFaceEntity(PLAYER, Boxes.AsylumDemonFogRotationTarget)
    ForceAnimation(PLAYER, 7410)
    DisableSoapstoneMessage(Messages.TutorialMessageHint00)
    ForceAnimation(Objects.o8542_0000, 3)
    SkipLinesIfFlagOff(1, 11810112)
    ForceAnimation(Objects.o8541_0001, 3)
    Restart()


def Event11815393():
    """ 11815393: Event 11815393 """
    SkipLinesIfThisEventOn(5)
    IfFlagOff(1, 16)
    IfCharacterInsideRegion(-1, PLAYER, region=Boxes.AsylumDemonCombatStart)
    IfCharacterInsideRegion(-1, PLAYER, region=Boxes.PlayerAboveAsylumDemon)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    SkipLinesIfClient(1)
    NotifyBossBattleStart()
    ActivateMultiplayerBuffs(Characters.c2232_0000)


@RestartOnRest
def Event11815392():
    """ 11815392: Event 11815392 """
    SkipLinesIfFlagOff(3, 16)
    DisableCharacter(Characters.c2232_0000)
    Kill(Characters.c2232_0000, award_souls=False)
    End()
    IfFlagOff(1, 11810310)
    IfCharacterInsideRegion(1, PLAYER, region=Boxes.AsylumDemonCombatStart)
    IfFlagOn(2, 11810310)
    IfCharacterInsideRegion(2, PLAYER, region=Boxes.AsylumDemonMusic)
    IfFlagOn(3, 11815393)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EnableAI(Characters.c2232_0000)


def Event11810001():
    """ 11810001: Event 11810001 """
    IfHealthLessThanOrEqual(0, Characters.c2232_0000, 0.0)
    PlaySoundEffect(anchor_entity=Characters.c2232_0000, sound_type=SoundType.s_SFX, sound_id=777777777)
    IfCharacterDead(0, Characters.c2232_0000)
    EnableFlag(16)
    KillBoss(1810800)
    DisableObject(Objects.o8950_0000)
    DeleteVFX(VFX.AsylumTopEntranceFog, erase_root_only=True)
    ForceAnimation(Objects.o8541_0001, 1)
    SkipLinesIfFlagOff(1, 11810312)
    ForceAnimation(Objects.o8542_0000, 1)
    DisableObjectActivation(Objects.o8541_0001, obj_act_id=-1)


def Event11815394():
    """ 11815394: Event 11815394 """
    DisableNetworkSync()
    IfFlagOff(0, 11815396)
    IfFlagOff(1, 16)
    IfFlagOn(1, 11810310)
    IfFlagOn(1, 11815392)
    IfCharacterInsideRegion(-1, PLAYER, region=Boxes.AsylumDemonMusic)
    IfCharacterInsideRegion(-1, PLAYER, region=Boxes.PlayerAboveAsylumDemon)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(11815396)
    EnableSoundEvent(1813800)
    EnableBossHealthBar(Characters.c2232_0000, name=2232, slot=0)
    Restart()


def Event11815395():
    """ 11815395: Event 11815395 """
    DisableNetworkSync()
    IfFlagOn(0, 11815396)
    IfFlagOff(1, 11815390)
    IfCharacterOutsideRegion(1, PLAYER, region=Boxes.AsylumDemonMusic)
    IfCharacterDead(2, Characters.c2232_0000)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    DisableFlag(11815396)
    DisableSoundEvent(1813800)
    DisableBossHealthBar(Characters.c2232_0000, name=2232, slot=0)
    Restart()


@RestartOnRest
def Event11810310():
    """ 11810310: Event 11810310 """
    EndIfFlagOn(11810314)
    EndIfThisEventOn()
    EndIfFlagOn(16)
    DisableObject(Objects.o8950_0000)
    DeleteVFX(VFX.AsylumTopEntranceFog, erase_root_only=False)
    DisableHealthBar(Characters.c2232_0000)
    DisableAI(Characters.c2232_0000)
    SetStandbyAnimationSettings(Characters.c2232_0000, standby_animation=9000)
    Move(
        Characters.c2232_0000,
        destination=Boxes.StrayDemonWaitingPoint,
        destination_type=CoordEntityType.Region,
        short_move=True,
    )
    IfCharacterInsideRegion(0, PLAYER, region=Boxes.AsylumDemonCombatStart)
    EnableFlag(11810314)
    AddSpecialEffect(Characters.c2232_0000, 4160)
    ResetStandbyAnimationSettings(Characters.c2232_0000)
    ForceAnimation(Characters.c2232_0000, 9060, wait_for_completion=True)
    CancelSpecialEffect(Characters.c2232_0000, 4160)
    SetNest(Characters.c2232_0000, Boxes.AsylumDemonJumpedPoint1)
    EnableObject(Objects.o8950_0000)
    CreateVFX(VFX.AsylumTopEntranceFog)


def Event11810311():
    """ 11810311: Event 11810311 """
    IfFlagOff(1, 16)
    IfFlagOff(1, 11815390)
    IfFlagOff(1, 11810315)
    IfCharacterInsideRegion(1, PLAYER, region=Boxes.AsylumDemonCombatStart)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(11810315)
    DisableFlag(11810112)
    ForceAnimation(Objects.o8541_0001, 3)
    ForceAnimation(Objects.o8542_0000, 1, wait_for_completion=True)


def Event11810312():
    """ 11810312: Event 11810312 """
    IfFlagOff(1, 16)
    IfFlagOn(1, 11810315)
    IfStandingOnCollision(1, 1813120)
    IfConditionTrue(0, input_condition=1)
    DisableFlag(11810315)
    EnableFlag(11810312)
    DisableObjectActivation(Objects.o8541_0001, obj_act_id=-1)
    SetRespawnPoint(SpawnPoints.SpawnPoint01)
    SaveRequest()
    EnableCollision(Collisions.h0550B1_0000)
    ForceAnimation(Objects.o8542_0000, 3, wait_for_completion=True)
    DisableCollision(Collisions.h0550B1_0000)


def Event11810313():
    """ 11810313: Event 11810313 """
    DisableNetworkSync()
    IfFlagOff(1, 16)
    IfFlagOn(1, 11810312)
    IfFlagOn(1, 61810105)
    IfActionButton(
        1,
        prompt_text=10010400,
        anchor_entity=Objects.o8541_0001,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        model_point=100,
    )
    IfConditionTrue(0, input_condition=1)
    DisplayDialog(
        10010160,
        anchor_entity=Objects.o8541_0001,
        display_distance=3.0,
        button_type=ButtonType.Yes_or_No,
        number_buttons=NumberButtons.NoButton,
    )
    Restart()


def Event11815380():
    """ 11815380: Event 11815380 """
    IfFlagOff(1, 11810900)
    IfActionButton(
        1,
        prompt_text=10010403,
        anchor_entity=1812898,
        anchor_type=CoordEntityType.Region,
        line_intersects=0,
        boss_version=True,
    )
    IfConditionTrue(0, input_condition=1)
    SkipLinesIfClient(1)
    NotifyBossBattleStart()
    RotateToFaceEntity(PLAYER, 1812897)
    ForceAnimation(PLAYER, 7410, wait_for_completion=True)
    ActivateMultiplayerBuffs(Characters.c2230_0000)
    Restart()


@RestartOnRest
def Event11815382():
    """ 11815382: Event 11815382 """
    SkipLinesIfFlagOff(4, 11810900)
    DisableCharacter(Characters.c2230_0000)
    Kill(Characters.c2230_0000, award_souls=False)
    RegisterLadder(start_climbing_flag=11810012, stop_climbing_flag=11810013, obj=Objects.o8501_0000)
    End()
    DisableAI(Characters.c2230_0000)
    EnableInvincibility(Characters.c2230_0000)
    DisableHealthBar(Characters.c2230_0000)
    IfCharacterInsideRegion(0, PLAYER, region=Boxes.StrayDemonCombatStart)
    EnableAI(Characters.c2230_0000)
    DisableInvincibility(Characters.c2230_0000)
    EnableBossHealthBar(Characters.c2230_0000, name=2231, slot=0)
    EnableObject(Objects.o8953_0000)
    CreateVFX(VFX.StrayDemonLadderFog)


def Event11810900():
    """ 11810900: Event 11810900 """
    IfCharacterDead(0, Characters.c2230_0000)
    KillBoss(1810810)
    DisableObject(Objects.o8953_0000)
    DeleteVFX(VFX.StrayDemonLadderFog, erase_root_only=True)
    RegisterLadder(start_climbing_flag=11810012, stop_climbing_flag=11810013, obj=Objects.o8501_0000)


def Event11815384():
    """ 11815384: Event 11815384 """
    DisableNetworkSync()
    IfFlagOn(1, 16)
    IfFlagOn(1, 11815382)
    IfCharacterInsideRegion(1, PLAYER, region=Boxes.StrayDemonMusic)
    IfConditionTrue(0, input_condition=1)
    EnableSoundEvent(1813801)


def Event11815385():
    """ 11815385: Event 11815385 """
    DisableNetworkSync()
    IfFlagOn(1, 11815384)
    IfFlagOn(1, 11810900)
    IfConditionTrue(0, input_condition=1)
    DisableSoundEvent(1813801)


def Event11810000():
    """ 11810000: Event 11810000 """
    EndIfThisEventOn()
    IfCharacterInsideRegion(0, PLAYER, region=Boxes.AtCliffEdge)
    DisableBackread(Characters.c2232_0000)
    IssuePrefetchRequest(0)
    WaitFrames(1)
    PlayCutscene(180125, skippable=True, fade_out=False, player_id=PLAYER)
    PlayCutscene(
        100225,
        skippable=True,
        fade_out=False,
        player_id=PLAYER,
        move_to_region=m10_02_Boxes.ArriveFirstTime,
        move_to_map=FIRELINK_SHRINE,
    )
    WaitFrames(1)
    SkipLinesIfFlagOn(1, 16)
    EnableBackread(Characters.c2232_0000)
    EnableFlag(11810000)
    SetRespawnPoint(m10_02_SpawnPoints.SpawnPoint0)
    SaveRequest()
    AwardAchievement(28)


def Event11810150():
    """ 11810150: Event 11810150 """
    SkipLinesIfFlagOn(3, 11810000)
    DisableObject(Objects.o8550)
    IfFlagOn(0, 11810000)
    EnableObject(Objects.o8550)
    IfActionButton(
        0,
        prompt_text=10010506,
        anchor_entity=Boxes.SnugglyNest,
        anchor_type=CoordEntityType.Region,
        trigger_attribute=TriggerAttribute.All,
    )
    SetStandbyAnimationSettings(PLAYER, standby_animation=7816)
    ForceAnimation(PLAYER, 7815, wait_for_completion=True)
    SkipLinesIfMultiplayer(6)
    ResetStandbyAnimationSettings(PLAYER)
    PlayCutscene(
        180126,
        skippable=True,
        fade_out=False,
        player_id=PLAYER,
        move_to_region=m10_02_Boxes.ArriveFromAsylumSecondTime,
        move_to_map=FIRELINK_SHRINE,
    )
    PlayCutscene(100226, skippable=True, fade_out=False, player_id=PLAYER)
    WaitFrames(1)
    AwardAchievement(28)
    Restart()
    IfActionButton(
        1,
        prompt_text=10010507,
        anchor_entity=Boxes.SnugglyNest,
        anchor_type=CoordEntityType.Region,
        trigger_attribute=TriggerAttribute.All,
    )
    IfCharacterOutsideRegion(2, PLAYER, region=Boxes.SnugglyNest)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    ResetStandbyAnimationSettings(PLAYER)
    SkipLinesIfFinishedConditionTrue(1, 2)
    ForceAnimation(PLAYER, 7817, wait_for_completion=True)
    Restart()


def Event11810100(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 11810100: Event 11810100 """
    SkipLinesIfThisEventSlotOff(5)
    DisableObjectActivation(arg_4_7, obj_act_id=-1, relative_index=0)
    DisableObjectActivation(arg_4_7, obj_act_id=-1, relative_index=1)
    DisableObjectActivation(arg_4_7, obj_act_id=-1, relative_index=2)
    DisableObjectActivation(arg_4_7, obj_act_id=-1, relative_index=3)
    End()
    SkipLinesIfClient(4)
    IfObjectActivated(0, obj_act_id=arg_0_3)
    EnableFlag(arg_0_3)
    SkipLinesIfEqual(1, left=arg_8_11, right=0)
    DisplayDialog(
        arg_8_11,
        anchor_entity=arg_4_7,
        display_distance=3.0,
        button_type=ButtonType.Yes_or_No,
        number_buttons=NumberButtons.NoButton,
    )
    DisableNetworkSync()
    Wait(2.0)
    DisableObjectActivation(arg_4_7, obj_act_id=-1, relative_index=0)
    DisableObjectActivation(arg_4_7, obj_act_id=-1, relative_index=1)
    DisableObjectActivation(arg_4_7, obj_act_id=-1, relative_index=2)
    DisableObjectActivation(arg_4_7, obj_act_id=-1, relative_index=3)


def Event11810120():
    """ 11810120: Event 11810120 """
    DisableNetworkSync()
    IfCharacterInsideRegion(1, PLAYER, region=Boxes.ShortcutGateUnlockedSide)
    IfFlagOn(2, 11810105)
    IfCharacterInsideRegion(2, PLAYER, region=Boxes.ShortcutGateLockedSide)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    AddSpecialEffect(PLAYER, 4150)
    Wait(3.0)
    Restart()


def Event11810110():
    """ 11810110: Event 11810110 """
    SkipLinesIfThisEventOff(3)
    DisableObjectActivation(Objects.o8544_0000, obj_act_id=-1)
    EndOfAnimation(Objects.o8544_0000, 1)
    End()
    IfObjectActivated(0, obj_act_id=11810110)
    EnableFlag(11810110)
    EndIfClient()
    DisplayDialog(
        10010870,
        anchor_entity=Objects.o8544_0000,
        display_distance=3.0,
        button_type=ButtonType.Yes_or_No,
        number_buttons=NumberButtons.NoButton,
    )


def Event11810111():
    """ 11810111: Event 11810111 """
    IfObjectActivated(0, obj_act_id=11810111)
    EnableFlag(11810112)
    Restart()


def Event11810211():
    """ 11810211: Event 11810211 """
    SkipLinesIfThisEventOff(3)
    DisableObject(Objects.o8530_0000)
    EndOfAnimation(Objects.o8530_0001, 0)
    End()
    DisableObject(Objects.o8530_0001)
    DisableObject(Objects.o8531_0000)
    IfCharacterInsideRegion(0, PLAYER, region=Boxes.BallTrapTrigger)
    CreateHazard(
        11810212,
        Objects.o8530_0000,
        model_point=1,
        behavior_param_id=5110,
        target_type=DamageTargetType.Character,
        radius=0.800000011920929,
        life=2.5,
        repetition_time=0.0,
    )
    ForceAnimation(Objects.o8530_0000, 0, wait_for_completion=True)
    DisableObject(Objects.o8530_0000)
    EnableObject(Objects.o8530_0001)
    EndOfAnimation(Objects.o8530_0001, 0)
    EnableObject(Objects.o8531_0000)


def Event11810200(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 11810200: Event 11810200 """
    SkipLinesIfThisEventSlotOff(4)
    DisableObject(arg_0_3)
    DisableObject(arg_4_7)
    DisableObject(arg_8_11)
    End()
    DisableObject(arg_4_7)
    IfObjectDestroyed(0, arg_0_3)
    DisableObject(arg_0_3)
    EnableObject(arg_4_7)
    DestroyObject(arg_4_7)
    DisableObject(arg_8_11)


def Event11810400(
    _,
    arg_0_0: uchar,
    arg_4_7: int,
    arg_8_11: int,
    arg_12_15: int,
    arg_16_16: uchar,
    arg_17_17: uchar,
    arg_18_18: uchar,
    arg_19_19: uchar,
):
    """ 11810400: Event 11810400 """
    IfPlayerClass(1, arg_0_0)
    EndIfConditionFalse(1)
    DisableSoapstoneMessage(Messages.TutorialMessageClass00)
    DisableSoapstoneMessage(Messages.TutorialMessageClass01)
    DisableSoapstoneMessage(Messages.TutorialMessageClass02)
    DisableSoapstoneMessage(Messages.TutorialMessageClass03)
    DisableSoapstoneMessage(Messages.TutorialMessageClass04)
    DisableTreasure(Objects.o0500_0033)
    DisableTreasure(Objects.o0500_0023)
    DisableTreasure(Objects.o0500_0034)
    DisableTreasure(Objects.o0500_0024)
    DisableTreasure(Objects.o0500_0035)
    DisableTreasure(Objects.o0500_0025)
    DisableTreasure(Objects.o0500_0036)
    DisableTreasure(Objects.o0500_0026)
    DisableTreasure(Objects.o0500_0037)
    DisableTreasure(Objects.o0500_0027)
    DisableTreasure(Objects.o0500_0038)
    DisableTreasure(Objects.o0500_0028)
    DisableTreasure(Objects.o0500_0043)
    DisableTreasure(Objects.o0500_0039)
    DisableTreasure(Objects.o0500_0029)
    DisableTreasure(Objects.o0500_0044)
    DisableTreasure(Objects.o0500_0040)
    DisableTreasure(Objects.o0500_0030)
    DisableTreasure(Objects.o0500_0045)
    DisableTreasure(Objects.o0500_0041)
    DisableTreasure(Objects.o0500_0031)
    DisableTreasure(Objects.o0500_0046)
    DisableTreasure(Objects.o0500_0042)
    DisableTreasure(Objects.o0500_0032)
    DisableObject(Objects.o0500_0033)
    DisableObject(Objects.o0500_0023)
    DisableObject(Objects.o0500_0034)
    DisableObject(Objects.o0500_0024)
    DisableObject(Objects.o0500_0035)
    DisableObject(Objects.o0500_0025)
    DisableObject(Objects.o0500_0036)
    DisableObject(Objects.o0500_0026)
    DisableObject(Objects.o0500_0037)
    DisableObject(Objects.o0500_0027)
    DisableObject(Objects.o0500_0038)
    DisableObject(Objects.o0500_0028)
    DisableObject(Objects.o0500_0043)
    DisableObject(Objects.o0500_0039)
    DisableObject(Objects.o0500_0029)
    DisableObject(Objects.o0500_0044)
    DisableObject(Objects.o0500_0040)
    DisableObject(Objects.o0500_0030)
    DisableObject(Objects.o0500_0045)
    DisableObject(Objects.o0500_0041)
    DisableObject(Objects.o0500_0031)
    DisableObject(Objects.o0500_0046)
    DisableObject(Objects.o0500_0042)
    DisableObject(Objects.o0500_0032)
    SetSoapstoneMessageState(Messages.TutorialMessageClass00, state=arg_16_16)
    SetSoapstoneMessageState(Messages.TutorialMessageClass01, state=arg_17_17)
    SetSoapstoneMessageState(Messages.TutorialMessageClass02, state=arg_18_18)
    SetSoapstoneMessageState(Messages.TutorialMessageClass03, state=arg_18_18)
    SetSoapstoneMessageState(Messages.TutorialMessageClass04, state=arg_19_19)
    EnableObject(arg_4_7)
    EnableObject(arg_8_11)
    EnableObject(arg_12_15)
    EnableTreasure(arg_4_7)
    EnableTreasure(arg_8_11)
    EnableTreasure(arg_12_15)


def Event11810450():
    """ 11810450: Event 11810450 """
    EndIfThisEventOn()
    DisableSoapstoneMessage(Messages.TutorialMessage08)
    DisableSoapstoneMessage(Messages.TutorialMessage09)
    IfFlagOn(-1, 11810590)
    IfFlagOn(-1, 50000082)
    IfConditionTrue(0, input_condition=-1)
    EnableSoapstoneMessage(Messages.TutorialMessage08)
    EnableSoapstoneMessage(Messages.TutorialMessage09)


def Event11810220():
    """ 11810220: Event 11810220 """
    SkipLinesIfThisEventOff(4)
    DisableFlag(11810220)
    RestoreObject(Objects.o8510_0000)
    RestoreObject(Objects.o8510_0001)
    RestoreObject(Objects.o8511_0000)
    DisableObject(Objects.o8510_0001)
    IfFlagOn(1, 11810000)
    IfHost(1)
    IfCharacterInsideRegion(1, PLAYER, region=Spheres.StrayCeilingBreakTrigger)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(11810220)
    DisableObject(Objects.o8510_0000)
    EnableObject(Objects.o8510_0001)
    DestroyObject(Objects.o8510_0001)
    DisableObject(Objects.o8511_0000)
    PlaySoundEffect(anchor_entity=Objects.o8510_0000, sound_type=SoundType.o_Object, sound_id=851000000)
    CreateTemporaryVFX(180100, anchor_entity=Objects.o8510_0000, anchor_type=CoordEntityType.Object, model_point=-1)


def Event11810320():
    """ 11810320: Event 11810320 """
    EndIfFlagOn(11810000)
    EnableInvincibility(Characters.c2230_0000)
    IfCharacterBackreadEnabled(0, Characters.c2230_0000)
    AICommand(Characters.c2230_0000, command_id=10, slot=0)
    IfFlagOn(0, 11810000)
    DisableInvincibility(Characters.c2230_0000)
    IfCharacterBackreadEnabled(0, Characters.c2230_0000)
    AICommand(Characters.c2230_0000, command_id=-1, slot=0)


def Event11810300():
    """ 11810300: Event 11810300 """
    EndIfClient()
    EndIfThisEventOn()
    EndIfFlagOn(16)
    SkipLinesIfFlagOn(3, 11810301)
    EnableFlag(50000081)
    EnableFlag(50001661)
    EnableFlag(11810301)
    IfFlagOff(1, 16)
    IfFlagOff(1, 11810090)
    IfHealthLessThanOrEqual(1, Characters.c2232_0000, 0.0)
    IfConditionTrue(0, input_condition=1)
    DisableFlag(50000081)
    DisableFlag(50001661)
    EnableFlag(50001660)


@RestartOnRest
def Event11810850(_, arg_0_3: int, arg_4_7: int):
    """ 11810850: Event 11810850 """
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


@RestartOnRest
def Event11810350():
    """ 11810350: Event 11810350 """
    SkipLinesIfFlagOn(32, 11810000)
    DisableObject(Objects.o0500_0008)
    DisableCharacter(Characters.c2792_0000)
    DisableCharacter(Characters.c2500_0012)
    DisableCharacter(Characters.c2500_0013)
    DisableCharacter(Characters.c2500_0014)
    DisableCharacter(Characters.c2500_0015)
    DisableCharacter(Characters.c2500_0016)
    DisableCharacter(Characters.c2500_0017)
    DisableCharacter(Characters.c2500_0018)
    DisableCharacter(Characters.c2500_0019)
    DisableCharacter(Characters.c2500_0020)
    DisableCharacter(Characters.c2500_0021)
    DisableCharacter(Characters.c2550_0001)
    DisableCharacter(Characters.c2550_0002)
    DisableCharacter(Characters.c2792_0001)
    IfFlagOn(0, 11810000)
    DisableFlag(11810211)
    EnableCharacter(Characters.c2792_0000)
    EnableCharacter(Characters.c2500_0012)
    EnableCharacter(Characters.c2500_0013)
    EnableCharacter(Characters.c2500_0014)
    EnableCharacter(Characters.c2500_0015)
    EnableCharacter(Characters.c2500_0016)
    EnableCharacter(Characters.c2500_0017)
    EnableCharacter(Characters.c2500_0018)
    EnableCharacter(Characters.c2500_0019)
    EnableCharacter(Characters.c2500_0020)
    EnableCharacter(Characters.c2500_0021)
    EnableCharacter(Characters.c2550_0001)
    EnableCharacter(Characters.c2550_0002)
    EnableCharacter(Characters.c2792_0001)
    EnableObject(Objects.o0500_0008)
    EnableTreasure(Objects.o0500_0008)
    DisableObject(Objects.o0500_0000)
    DisableCharacter(Characters.c2500_0000)
    DisableCharacter(Characters.c2500_0001)
    DisableCharacter(Characters.c2500_0002)
    DisableCharacter(Characters.c2500_0003)
    DisableCharacter(Characters.c2500_0005)
    DisableCharacter(Characters.c2500_0006)
    DisableCharacter(Characters.c2500_0007)
    DisableCharacter(Characters.c2500_0009)
    DisableCharacter(Characters.c2500_0010)
    DisableCharacter(Characters.c2500_0011)
    DisableCharacter(Characters.c2550_0000)


def Event11810600():
    """ 11810600: Event 11810600 """
    IfFlagOn(1, 11815200)
    IfFlagOn(2, 11815201)
    IfFlagOn(3, 11815202)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionFalse(5, 1)
    EnableFlag(11815100)
    DisableFlag(11815101)
    DisableFlag(11815102)
    DisableFlagRange((11815200, 11815202))
    Restart()
    SkipLinesIfFinishedConditionFalse(6, 3)
    DisableFlag(11815100)
    DisableFlag(11815101)
    EnableFlag(11815102)
    DisableFlag(71810093)
    DisableFlagRange((11815200, 11815202))
    Restart()
    DisableFlag(11815100)
    EnableFlag(11815101)
    DisableFlag(11815102)
    DisableFlag(71810092)
    DisableFlagRange((11815200, 11815202))
    Restart()


def Event11810641(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11810641: Event 11810641 """
    IfAnyItemDroppedInRegion(0, Boxes.SnugglyItemPickup)
    IfItemDropped(2, arg_4_7, item_type=arg_0_3)
    SkipLinesIfConditionTrue(2, 2)
    EnableFlag(11815201)
    Restart()
    SkipLinesIfFlagOn(3, arg_12_15)
    EnableFlag(11815200)
    SetNextSnugglyTrade(arg_8_11)
    Restart()
    EnableFlag(11815202)
    Restart()


def Event11815110(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 11815110: Event 11815110 """
    EndIfFlagOff(arg_0_3)
    EndIfFlagOn(arg_8_11)
    WaitFrames(1)
    SnugglyItemDrop(arg_4_7, region=Boxes.SnugglyItemDrop, flag=arg_0_3, collision=1813102)


def Event11815150():
    """ 11815150: Event 11815150 """
    IfTimeElapsed(0, 1.0)
    EnableFlag(11815151)


def Event11810050():
    """ 11810050: Event 11810050 """
    IfPlayerCovenant(1, Covenant.DarkmoonBlade)
    EndIfConditionFalse(1)
    EnableFlag(71510036)
    EnableFlag(71510037)


def Event11810510(_, arg_0_3: int, arg_4_7: int):
    """ 11810510: Event 11810510 """
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
    SetTeamType(arg_0_3, TeamType.HostileAlly)
    SaveRequest()


def Event11810520(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11810520: Event 11810520 """
    SkipLinesIfThisEventSlotOff(2)
    DropMandatoryTreasure(arg_0_3)
    End()
    IfHealthLessThanOrEqual(0, arg_0_3, 0.0)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)


def Event11810530(_, arg_0_3: int):
    """ 11810530: Event 11810530 """
    IfFlagOn(1, 1060)
    IfFlagOn(-2, 11810590)
    IfFlagOn(-2, 11810591)
    IfFlagOn(-2, 11810592)
    IfConditionTrue(1, input_condition=-2)
    IfCharacterInsideRegion(-3, PLAYER, region=Boxes.OscarDeathTrigger)
    IfCharacterInsideRegion(-3, PLAYER, region=Boxes.AsylumDemonMusic)
    IfConditionTrue(1, input_condition=-3)
    IfThisEventOff(1)
    IfThisEventOn(2)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(2)
    Kill(arg_0_3, award_souls=True)


def Event11810531(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11810531: Event 11810531 """
    IfFlagOn(1, 1073)
    IfFlagOn(1, 11810000)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)
    EnableCharacter(arg_0_3)


def Event11810532(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11810532: Event 11810532 """
    SkipLinesIfThisEventOff(2)
    DropMandatoryTreasure(arg_0_3)
    End()
    IfFlagOn(1, 1061)
    IfHealthLessThanOrEqual(1, arg_0_3, 0.0)
    IfInsideMap(1, game_map=UNDEAD_ASYLUM)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)


@RestartOnRest
def Event11815010():
    """ 11815010: Event 11815010 """
    EndIfThisEventOn()
    AddSpecialEffect(Characters.c0000_0002, 5492)
    DisableHealthBar(Characters.c0000_0002)
    WaitFrames(5)
    EnableHealthBar(Characters.c0000_0002)
