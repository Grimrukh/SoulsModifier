"""
linked:


strings:

"""
from soulstruct.darksouls1r.events import *
from ..entities.m13_02_00_00_entities import *
from ..entities.common_entities import *


def Constructor():
    """ 0: Event 0 """
    RegisterBonfire(
        11320992,
        obj=Objects.o0200_0000,
        reaction_distance=2.0,
        reaction_angle=180.0,
        initial_kindle_level=10,
    )
    RegisterBonfire(
        11320984,
        obj=Objects.o0200_0001,
        reaction_distance=2.0,
        reaction_angle=180.0,
        initial_kindle_level=0,
    )
    RegisterBonfire(
        11320976,
        obj=Objects.o0200_0002,
        reaction_distance=2.0,
        reaction_angle=180.0,
        initial_kindle_level=0,
    )
    RegisterLadder(start_climbing_flag=11320010, stop_climbing_flag=11320011, obj=Objects.o3240_0000)
    RegisterLadder(start_climbing_flag=11320012, stop_climbing_flag=11320013, obj=Objects.o3241_0000)
    RegisterLadder(start_climbing_flag=11320014, stop_climbing_flag=11320015, obj=Objects.o3242_0000)
    RegisterLadder(start_climbing_flag=11320016, stop_climbing_flag=11320017, obj=Objects.o3243_0000)
    RegisterStatue(Objects.o0101_0000, game_map=ASH_LAKE, statue_type=StatueType.Stone)
    RegisterStatue(Objects.o0101_0001, game_map=ASH_LAKE, statue_type=StatueType.Stone)
    RegisterStatue(Objects.o0101_0002, game_map=ASH_LAKE, statue_type=StatueType.Stone)
    RegisterStatue(Objects.o0101_0003, game_map=ASH_LAKE, statue_type=StatueType.Stone)
    RegisterStatue(Objects.o0101_0004, game_map=ASH_LAKE, statue_type=StatueType.Stone)
    RegisterStatue(Objects.o0101_0005, game_map=ASH_LAKE, statue_type=StatueType.Stone)
    RegisterStatue(Objects.o0101_0006, game_map=ASH_LAKE, statue_type=StatueType.Stone)
    RegisterStatue(Objects.o0101_0007, game_map=ASH_LAKE, statue_type=StatueType.Stone)
    SkipLinesIfClient(2)
    DisableObject(Objects.o3970_0000)
    DeleteVFX(VFX.MultiplayerFog1, erase_root_only=False)
    RunEvent(
        11320090,
        slot=0,
        args=(Objects.o3971_0000, VFX.CheckpointFog1, Boxes.CheckpointFog1FrontSide, Boxes.CheckpointFog1BackSide),
    )
    RunEvent(11325000)
    RunEvent(11320800)
    RunEvent(11325001)
    RunEvent(11320200, slot=0, args=(Objects.o3450_0000, 11320200))
    RunEvent(11320200, slot=1, args=(Objects.o3451_0000, 11320201))
    RunEvent(11320580)
    SkipLinesIfFlagOff(2, 11320100)
    RunEvent(11320100)
    SkipLines(3)
    RunEvent(11320110)
    RunEvent(11320100)
    RunEvent(11325100)
    RunEvent(11320101)
    RunEvent(11325150, slot=0, args=(Characters.c3250_0000, 15.0), arg_types="if")
    RunEvent(11325150, slot=1, args=(Characters.c3250_0001, 15.0), arg_types="if")
    RunEvent(11325150, slot=2, args=(Characters.c3250_0002, 10.0), arg_types="if")
    RunEvent(11320300, slot=1, args=(Characters.c3300_0001, 11325203, 11325205, 11325203), arg_types="iIIi")
    RunEvent(11320300, slot=2, args=(Characters.c3300_0002, 11325206, 11325208, 11325206), arg_types="iIIi")
    RunEvent(11320300, slot=3, args=(Characters.c3300_0003, 11325209, 11325211, 11325209), arg_types="iIIi")
    RunEvent(11320300, slot=4, args=(Characters.c3300_0004, 11325212, 11325214, 11325212), arg_types="iIIi")
    RunEvent(11320300, slot=5, args=(Characters.c3300_0005, 11325215, 11325217, 11325215), arg_types="iIIi")
    RunEvent(11320300, slot=6, args=(Characters.c3300_0006, 11325218, 11325220, 11325218), arg_types="iIIi")
    RunEvent(11320300, slot=7, args=(Characters.c3300_0007, 11325221, 11325223, 11325221), arg_types="iIIi")
    RunEvent(11320300, slot=8, args=(Characters.c3300_0008, 11325224, 11325226, 11325224), arg_types="iIIi")
    RunEvent(11320300, slot=9, args=(Characters.c3300_0009, 11325227, 11325229, 11325227), arg_types="iIIi")
    RunEvent(11320300, slot=10, args=(Characters.c3300_0010, 11325230, 11325232, 11325230), arg_types="iIIi")
    RunEvent(11320600, slot=0, args=(Objects.o0110_0000, 11320600))
    
    PatchesAmbush()
    ChannelerAmbush()
    RedPhantomAmbush()
    MakeWorldInvisible()
    OopsAllGwyns()
    OopsAllBonewheels()
    HyperAggression()
    EnemySpeedUp()
    EnemyExtremeSpeedUp()
    EnemySpeedDown()
    EnemyExtremeSpeedDown()
    EnemyHealthRegain()
    EnemyMaxHealthUp()
    EnemyMaxHealthDown()
    EnemyDefenseUp()


def Preconstructor():
    """ 50: Event 50 """
    HumanityRegistration(Characters.c0000_0004, 8446)
    SkipLinesIfFlagOn(1, 1511)
    DisableCharacter(Characters.c0000_0004)
    RunEvent(11320534, slot=0, args=(Characters.c0000_0004, 1490, 1539, 1511))
    RunEvent(11320535, slot=0, args=(Characters.c0000_0004, 1490, 1539, 1514))
    HumanityRegistration(Characters.c0000_0005, 8454)
    SkipLinesIfFlagOn(2, 1547)
    SkipLinesIfFlagOn(1, 1546)
    DisableCharacter(Characters.c0000_0005)
    RunEvent(11320510, slot=1, args=(Characters.c0000_0005, 1547))
    RunEvent(11320520, slot=1, args=(Characters.c0000_0005, 1540, 1569, 1548))
    RunEvent(11320540, slot=0, args=(Characters.c0000_0005, 1540, 1569, 1546))
    RunEvent(11320541, slot=0, args=(Characters.c0000_0005, 1540, 1569, 1549))
    EnableImmortality(Characters.c3450_0000)


def Event11320090(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11320090: Event 11320090 """
    SkipLinesIfThisEventSlotOff(3)
    DisableObject(arg_0_3)
    DeleteVFX(arg_4_7, erase_root_only=True)
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


@RestartOnRest
def Event11320110():
    """ 11320110: Event 11320110 """
    DisableFlag(11325100)
    DisableFlag(11325101)
    DisableCharacter(Characters.c3531_0000)
    DisableCharacter(Characters.c3531_0001)
    DisableCharacter(Characters.c3531_0002)
    DisableCharacter(Characters.c3531_0003)
    DisableCharacter(Characters.c3531_0004)
    DisableCharacter(Characters.c3531_0005)
    DisableCharacter(Characters.c3531_0006)
    EndIfFlagOn(11320100)
    RunEvent(11325121)
    RunEvent(11325110, slot=0, args=(1, 0, 3530, 3530, Characters.c3531_0000, 91, 0, 0), arg_types="hhiiiBBi")
    RunEvent(11325110, slot=1, args=(2, 0, 3531, 3531, Characters.c3531_0001, 92, 0, 1), arg_types="hhiiiBBi")
    RunEvent(11325110, slot=2, args=(3, 0, 3532, 3532, Characters.c3531_0002, 93, 0, 2), arg_types="hhiiiBBi")
    RunEvent(11325110, slot=3, args=(4, 0, 3533, 3533, Characters.c3531_0003, 94, 0, 3), arg_types="hhiiiBBi")
    RunEvent(11325110, slot=4, args=(5, 0, 3534, 3534, Characters.c3531_0004, 95, 0, 4), arg_types="hhiiiBBi")
    RunEvent(11325110, slot=5, args=(6, 0, 3535, 3535, Characters.c3531_0005, 96, 0, 5), arg_types="hhiiiBBi")
    RunEvent(11325110, slot=6, args=(8, 0, 3536, 3536, Characters.c3531_0006, 97, 0, 6), arg_types="hhiiiBBi")


@RestartOnRest
def Event11325100():
    """ 11325100: Event 11325100 """
    IfCharacterBackreadEnabled(1, Characters.c3530_0000)
    IfHasTAEEvent(1, Characters.c3530_0000, tae_event_id=300)
    IfConditionTrue(0, input_condition=1)
    SkipLinesIfFlagOn(8, 11325101)
    EnableFlag(11325101)
    Move(
        Characters.c3530_0000,
        destination=Boxes.HydraJumpAToBSnap,
        destination_type=CoordEntityType.Region,
        short_move=True,
    )
    ForceAnimation(Characters.c3530_0000, 3011, wait_for_completion=True)
    Move(
        Characters.c3530_0000,
        destination=Boxes.HydraJumpAToBAscentSnap,
        destination_type=CoordEntityType.Region,
        short_move=True,
    )
    SetNest(Characters.c3530_0000, Boxes.HydraJumpAToBAscentSnap)
    ForceAnimation(Characters.c3530_0000, 9060, wait_for_completion=True)
    ReplanAI(Characters.c3530_0000)
    Restart()
    DisableFlag(11325101)
    Move(
        Characters.c3530_0000,
        destination=Boxes.HydraJumpBToASnap,
        destination_type=CoordEntityType.Region,
        short_move=True,
    )
    ForceAnimation(Characters.c3530_0000, 3014, wait_for_completion=True)
    Move(
        Characters.c3530_0000,
        destination=Boxes.HydraJumpBToAAscentSnap,
        destination_type=CoordEntityType.Region,
        short_move=True,
    )
    SetNest(Characters.c3530_0000, Boxes.HydraJumpBToAAscentSnap)
    ForceAnimation(Characters.c3530_0000, 9060, wait_for_completion=True)
    ReplanAI(Characters.c3530_0000)
    Restart()


@UnknownRestart
def Event11325110(
    _,
    arg_0_1: short,
    arg_2_3: short,
    arg_4_7: int,
    arg_8_11: int,
    arg_12_15: int,
    arg_16_16: uchar,
    arg_17_17: uchar,
    arg_20_23: int,
):
    """ 11325110: Event 11325110 """
    SkipLinesIfThisEventSlotOff(4)
    SetDisplayMask(Characters.c3530_0000, bit_index=arg_16_16, switch_type=OnOffChange.On)
    SetCollisionMask(Characters.c3530_0000, bit_index=arg_17_17, switch_type=OnOffChange.Off)
    AddSpecialEffect(Characters.c3530_0000, arg_20_23)
    End()
    IfCharacterBackreadEnabled(0, Characters.c3530_0000)
    CreateNPCPart(
        Characters.c3530_0000,
        npc_part_id=arg_2_3,
        part_index=arg_0_1,
        part_health=270,
        damage_correction=1.0,
        body_damage_correction=1.0,
        is_invincible=False,
        start_in_stop_state=False,
    )
    IfCharacterPartHealthLessThanOrEqual(1, Characters.c3530_0000, npc_part_id=arg_4_7, value=0)
    IfFlagOff(1, 11325120)
    IfAttacked(1, Characters.c3530_0000, attacker=PLAYER)
    IfHealthLessThanOrEqual(2, Characters.c3530_0000, 0.0)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(2)
    ResetAnimation(Characters.c3530_0000, disable_interpolation=False)
    Move(
        arg_8_11,
        destination=Characters.c3530_0000,
        destination_type=CoordEntityType.Character,
        model_point=arg_12_15,
        copy_draw_parent=Characters.c3530_0000,
    )
    EnableCharacter(arg_8_11)
    ForceAnimation(arg_8_11, 8100)
    ForceAnimation(Characters.c3530_0000, 8000)
    SetDisplayMask(Characters.c3530_0000, bit_index=arg_16_16, switch_type=OnOffChange.On)
    SetCollisionMask(Characters.c3530_0000, bit_index=arg_17_17, switch_type=OnOffChange.Off)
    AddSpecialEffect(Characters.c3530_0000, arg_20_23)


@UnknownRestart
def Event11325121():
    """ 11325121: Event 11325121 """
    IfHasTAEEvent(0, Characters.c3530_0000, tae_event_id=500)
    EnableFlag(11325120)
    IfHasTAEEvent(0, Characters.c3530_0000, tae_event_id=600)
    DisableFlag(11325120)
    Restart()


@RestartOnRest
def Event11320100():
    """ 11320100: Event 11320100 """
    SkipLinesIfThisEventOff(9)
    DisableCharacter(Characters.c3530_0000)
    DisableCharacter(Characters.c3531_0000)
    DisableCharacter(Characters.c3531_0001)
    DisableCharacter(Characters.c3531_0002)
    DisableCharacter(Characters.c3531_0003)
    DisableCharacter(Characters.c3531_0004)
    DisableCharacter(Characters.c3531_0005)
    DisableCharacter(Characters.c3531_0006)
    End()
    IfCharacterDead(0, Characters.c3530_0000)
    AwardItemLot(35300000, host_only=False)


def Event11320101():
    """ 11320101: Event 11320101 """
    EndIfFlagOn(11320100)
    IfFlagOn(1, 11325110)
    IfFlagOn(1, 11325111)
    IfFlagOn(1, 11325112)
    IfFlagOn(1, 11325113)
    IfFlagOn(1, 11325114)
    IfFlagOn(1, 11325115)
    IfFlagOn(1, 11325116)
    IfConditionTrue(0, input_condition=1)
    Kill(Characters.c3530_0000, award_souls=True)


@RestartOnRest
def Event11325150(_, arg_0_3: int, arg_4_7: float):
    """ 11325150: Event 11325150 """
    EndIfThisEventSlotOn()
    SetStandbyAnimationSettings(arg_0_3, standby_animation=9000)
    IfEntityWithinDistance(-1, arg_0_3, PLAYER, radius=arg_4_7)
    IfAttacked(-1, arg_0_3, attacker=PLAYER)
    IfConditionTrue(0, input_condition=-1)
    SetStandbyAnimationSettings(arg_0_3, cancel_animation=9060)


def Event11325000():
    """ 11325000: Event 11325000 """
    EndIfThisEventOn()
    SetStandbyAnimationSettings(Characters.c3450_0000, standby_animation=9000)
    IfHost(1)
    IfEntityWithinDistance(1, Characters.c3450_0000, PLAYER, radius=30.0)
    IfConditionTrue(0, input_condition=1)
    SetStandbyAnimationSettings(Characters.c3450_0000, cancel_animation=9060)


def Event11320800():
    """ 11320800: Event 11320800 """
    SkipLinesIfThisEventOff(2)
    DisableCharacter(Characters.c3450_0000)
    End()
    IfCharacterDead(0, Characters.c3450_0000)
    EnableFlag(11320800)


@RestartOnRest
def Event11325001():
    """ 11325001: Event 11325001 """
    DisableCharacter(Characters.c3451_0000)
    EndIfFlagOn(11320800)
    SkipLinesIfThisEventOff(4)
    SetDisplayMask(Characters.c3450_0000, bit_index=0, switch_type=OnOffChange.On)
    SetCollisionMask(Characters.c3450_0000, bit_index=1, switch_type=OnOffChange.Off)
    AICommand(Characters.c3450_0000, command_id=20, slot=0)
    End()
    IfCharacterBackreadEnabled(0, Characters.c3450_0000)
    CreateNPCPart(
        Characters.c3450_0000,
        npc_part_id=3451,
        part_index=NPCPartType.Part1,
        part_health=200,
        damage_correction=1.0,
        body_damage_correction=1.0,
        is_invincible=False,
        start_in_stop_state=False,
    )
    IfCharacterPartHealthLessThanOrEqual(1, Characters.c3450_0000, npc_part_id=3451, value=0)
    IfHealthLessThanOrEqual(2, Characters.c3450_0000, 0.0)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(2)
    ForceAnimation(Characters.c3450_0000, 8000)
    IfHasTAEEvent(0, Characters.c3450_0000, tae_event_id=400)
    EnableCharacter(Characters.c3451_0000)
    Move(
        Characters.c3451_0000,
        destination=Characters.c3450_0000,
        destination_type=CoordEntityType.Character,
        model_point=19,
        copy_draw_parent=Characters.c3450_0000,
    )
    ForceAnimation(Characters.c3451_0000, 8100)
    SetDisplayMask(Characters.c3450_0000, bit_index=0, switch_type=OnOffChange.On)
    SetCollisionMask(Characters.c3450_0000, bit_index=1, switch_type=OnOffChange.Off)
    AICommand(Characters.c3450_0000, command_id=20, slot=0)
    ReplanAI(Characters.c3450_0000)
    IfCharacterHuman(-7, PLAYER)
    IfCharacterHollow(-7, PLAYER)
    EndIfConditionFalse(-7)
    AwardItemLot(34510000, host_only=True)


def Event11320200(_, arg_0_3: int, arg_4_7: int):
    """ 11320200: Event 11320200 """
    SkipLinesIfThisEventSlotOff(2)
    DisableObject(arg_0_3)
    End()
    IfObjectDestroyed(0, arg_0_3)
    EnableFlag(arg_4_7)


@RestartOnRest
def Event11320300(_, arg_0_3: int, arg_4_7: uint, arg_8_11: uint, arg_12_15: int):
    """ 11320300: Event 11320300 """
    DisableCharacter(arg_0_3)
    EndIfThisEventSlotOn()
    SkipLinesIfClient(1)
    EnableRandomFlagInRange((arg_4_7, arg_8_11))
    IfFlagOn(0, arg_12_15)
    EnableCharacter(arg_0_3)
    IfCharacterDead(0, arg_0_3)
    IfCharacterHuman(-7, PLAYER)
    IfCharacterHollow(-7, PLAYER)
    EndIfConditionFalse(-7)
    AwardItemLot(33000000, host_only=True)
    End()


def Event11320600(_, arg_0_3: int, arg_4_7: int):
    """ 11320600: Event 11320600 """
    SkipLinesIfThisEventSlotOff(4)
    EndOfAnimation(arg_0_3, 0)
    DisableObjectActivation(arg_0_3, obj_act_id=-1)
    EnableTreasure(arg_0_3)
    End()
    IfObjectActivated(0, obj_act_id=arg_4_7)
    WaitFrames(10)
    EnableTreasure(arg_0_3)


def Event11320510(_, arg_0_3: int, arg_4_7: int):
    """ 11320510: Event 11320510 """
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


def Event11320520(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11320520: Event 11320520 """
    SkipLinesIfThisEventSlotOff(2)
    DropMandatoryTreasure(arg_0_3)
    End()
    IfHealthLessThanOrEqual(0, arg_0_3, 0.0)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)


def Event11320534(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11320534: Event 11320534 """
    IfFlagOff(1, 1512)
    IfFlagOff(1, 1547)
    IfFlagOff(1, 1548)
    IfFlagOn(1, 1507)
    IfFlagOn(1, 11410593)
    IfFlagOn(1, 11020606)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)
    EnableCharacter(arg_0_3)


def Event11320535(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11320535: Event 11320535 """
    IfFlagOff(1, 1512)
    IfFlagOff(1, 1547)
    IfFlagOn(1, 1511)
    IfFlagOn(-1, 11320591)
    IfFlagOn(-1, 1548)
    IfConditionTrue(1, input_condition=-1)
    IfCharacterBackreadDisabled(1, arg_0_3)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)
    DisableCharacter(arg_0_3)


def Event11320540(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11320540: Event 11320540 """
    IfFlagOff(1, 1547)
    IfFlagOn(1, 1545)
    IfFlagOn(1, 11020606)
    IfFlagOn(1, 1511)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)
    EnableCharacter(arg_0_3)


def Event11320541(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11320541: Event 11320541 """
    IfFlagOff(1, 1547)
    IfFlagOn(1, 1546)
    IfFlagOn(1, 11320591)
    IfCharacterBackreadDisabled(1, arg_0_3)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)
    DisableCharacter(arg_0_3)


def Event11320580():
    """ 11320580: Event 11320580 """
    IfFlagOn(0, 11325030)
    RotateToFaceEntity(PLAYER, Characters.c3450_0000)
    ForceAnimation(PLAYER, 7910, wait_for_completion=True)
    ForceAnimation(PLAYER, 7911, loop=True)
    IfFlagOff(0, 11325030)
    ResetStandbyAnimationSettings(PLAYER)
    ForceAnimation(PLAYER, 7912, wait_for_completion=True)
    Restart()


@RestartOnRest
def PatchesAmbush():
    """ 11322000: Patches teleports behind the player and attacks. """
    DisableCharacter(Characters.c0000_PatchesAmbush)

    Await(InsideMap(ASH_LAKE) and TriggerFlags.PatchesAmbush and IsAlive(Characters.c0000_PatchesAmbush))
    DisableFlag(TriggerFlags.PatchesAmbush)
    
    EnableInvincibility(Characters.c0000_PatchesAmbush)

    Move(
        Characters.c0000_PatchesAmbush,
        destination=PLAYER,
        model_point=PlayerModelPoints.Behind,
        copy_draw_parent=PLAYER,
    )

    EnableCharacter(Characters.c0000_PatchesAmbush)
    FadeInCharacter(Characters.c0000_PatchesAmbush, 60.0)  # basically invisible while turning around
    RotateToFaceEntity(Characters.c0000_PatchesAmbush, PLAYER)
    ReplanAI(Characters.c0000_PatchesAmbush)
    Wait(0.5)
    DisableInvincibility(Characters.c0000_PatchesAmbush)
    Wait(1.0)
    FadeInCharacter(Characters.c0000_PatchesAmbush, 0.2)

    # Unlike other ambushes, Patches will disappear after ten seconds and be fully healed.
    # If you manage to kill him, he won't respawn when you rest at a bonfire, but will on full map reload (I think).
    Wait(10.0)
    FadeOutCharacter(Characters.c0000_PatchesAmbush, 0.5)
    Wait(0.5)
    AddSpecialEffect(Characters.c0000_PatchesAmbush, 3000)  # full heal
    DisableCharacter(Characters.c0000_PatchesAmbush)

    return RESTART


@RestartOnRest
def ChannelerAmbush():
    """ 11322001: Channeler teleports above the player (no gravity) and uses its buff dance. """
    DisableCharacter(Characters.c2370_TrollChanneler)

    Await(InsideMap(ASH_LAKE) and TriggerFlags.ChannelerAmbush and IsAlive(Characters.c2370_TrollChanneler))
    DisableFlag(TriggerFlags.ChannelerAmbush)

    Move(
        Characters.c2370_TrollChanneler,
        destination=PLAYER,
        model_point=PlayerModelPoints.Above,
        copy_draw_parent=PLAYER,
    )

    EnableCharacter(Characters.c2370_TrollChanneler)
    DisableGravity(Characters.c2370_TrollChanneler)
    DisableCollision(Characters.c2370_TrollChanneler)
    DisableHealthBar(Characters.c2370_TrollChanneler)
    FadeInCharacter(Characters.c2370_TrollChanneler, 0.5)
    ForceAnimation(Characters.c2370_TrollChanneler, 3007)  # buff dance
    Wait(5.0)
    FadeOutCharacter(Characters.c2370_TrollChanneler, 0.5)
    Wait(0.5)
    AddSpecialEffect(Characters.c2370_TrollChanneler, 3000)  # full heal
    DisableCharacter(Characters.c2370_TrollChanneler)

    AddSpecialEffect(6288, 5470)
    AddSpecialEffect(6290, 5470)
    AddSpecialEffect(1320960, 5470)
    AddSpecialEffect(1320961, 5470)
    AddSpecialEffect(1320962, 5470)
    AddSpecialEffect(1320211, 5470)
    AddSpecialEffect(1320212, 5470)
    AddSpecialEffect(1320213, 5470)
    AddSpecialEffect(1320214, 5470)
    AddSpecialEffect(1320215, 5470)
    AddSpecialEffect(1320216, 5470)
    AddSpecialEffect(1320217, 5470)
    AddSpecialEffect(1320218, 5470)
    AddSpecialEffect(1320219, 5470)
    AddSpecialEffect(1320220, 5470)
    AddSpecialEffect(1320100, 5470)
    AddSpecialEffect(1320101, 5470)
    AddSpecialEffect(1320102, 5470)
    AddSpecialEffect(1320221, 5470)
    AddSpecialEffect(1320222, 5470)
    AddSpecialEffect(1320223, 5470)
    AddSpecialEffect(1320224, 5470)
    AddSpecialEffect(1320225, 5470)
    AddSpecialEffect(1320226, 5470)
    AddSpecialEffect(1320227, 5470)
    AddSpecialEffect(1320228, 5470)
    AddSpecialEffect(1320229, 5470)
    AddSpecialEffect(1320230, 5470)
    AddSpecialEffect(1320231, 5470)
    AddSpecialEffect(1320232, 5470)
    AddSpecialEffect(1320233, 5470)
    AddSpecialEffect(1320234, 5470)
    AddSpecialEffect(1320201, 5470)
    AddSpecialEffect(1320202, 5470)
    AddSpecialEffect(1320203, 5470)
    AddSpecialEffect(1320204, 5470)
    AddSpecialEffect(1320205, 5470)
    AddSpecialEffect(1320206, 5470)
    AddSpecialEffect(1320207, 5470)
    AddSpecialEffect(1320208, 5470)
    AddSpecialEffect(1320209, 5470)
    AddSpecialEffect(1320210, 5470)
    AddSpecialEffect(1320800, 5470)
    AddSpecialEffect(1320801, 5470)
    AddSpecialEffect(1323900, 5470)
    AddSpecialEffect(1323910, 5470)
    AddSpecialEffect(1323901, 5470)
    AddSpecialEffect(1323911, 5470)
    AddSpecialEffect(1323902, 5470)
    AddSpecialEffect(1323912, 5470)
    AddSpecialEffect(1320700, 5470)
    AddSpecialEffect(1320701, 5470)
    AddSpecialEffect(1320702, 5470)
    AddSpecialEffect(1320703, 5470)
    AddSpecialEffect(1320704, 5470)
    AddSpecialEffect(1320705, 5470)
    AddSpecialEffect(1320706, 5470)
    AddSpecialEffect(1320707, 5470)

    return RESTART


@RestartOnRest
def RedPhantomAmbush():
    """ 11322002: No phantoms in this map, so it acts as an extra Patches trigger. """
    Await(InsideMap(ASH_LAKE) and TriggerFlags.EnemyAmbush)
    DisableFlag(TriggerFlags.EnemyAmbush)
    if IsAlive(Characters.c0000_PatchesAmbush):
        EnableFlag(TriggerFlags.PatchesAmbush)
    return RESTART


@RestartOnRest
def ControlRedPhantom(_, enemy: int):
    """ 11325081: `enemy` moves to player and appears. """
    DisableFlag(11325082)
    Move(enemy, destination=PLAYER, model_point=PlayerModelPoints.InFront, copy_draw_parent=PLAYER)
    EnableCharacter(enemy)
    EnableImmortality(enemy)
    FadeInCharacter(enemy, 0.5)
    ReplanAI(enemy)

    Await(HealthRatio(enemy) <= 0.01)
    FadeOutCharacter(enemy, 0.5)
    Wait(0.5)
    AddSpecialEffect(enemy, 3000)  # full heal
    DisableCharacter(enemy)
    EnableFlag(11325082)


def MakeWorldInvisible():
    """ 11322003: Disable all map pieces. Undone only by reload. """
    Await(TriggerFlags.InvisibleWorld)   # note you don't need to be standing in the map
    DisableFlag(TriggerFlags.InvisibleWorld)
    for map_piece in range(1328500, 1328543):
        DisableMapPiece(map_piece)
    # No need to restart.


@RestartOnRest
def OopsAllGwyns():
    """ 11322004: Enable Gwyns and warp them to their paired normal characters. """
    DisableCharacter(1320600)
    DisableCharacter(1320601)
    DisableCharacter(1320602)
    DisableCharacter(1320603)
    DisableCharacter(1320604)
    DisableCharacter(1320605)
    DisableCharacter(1320606)
    DisableCharacter(1320607)
    DisableCharacter(1320608)
    DisableCharacter(1320609)
    Await(TriggerFlags.OopsAllGwyns)  # note you don't need to be standing in the map
    DisableCharacter(6288)
    EnableCharacter(1320600)
    DisableCharacter(1320211)
    EnableCharacter(1320601)
    DisableCharacter(1320216)
    EnableCharacter(1320602)
    DisableCharacter(1320100)
    EnableCharacter(1320603)
    DisableCharacter(1320223)
    EnableCharacter(1320604)
    DisableCharacter(1320228)
    EnableCharacter(1320605)
    DisableCharacter(1320233)
    EnableCharacter(1320606)
    DisableCharacter(1320204)
    EnableCharacter(1320607)
    DisableCharacter(1320209)
    EnableCharacter(1320608)
    DisableCharacter(1320705)
    EnableCharacter(1320609)
    WaitFrames(30)  # enough time for other maps to trigger too
    DisableFlag(TriggerFlags.OopsAllGwyns)
    # No need to restart.


@RestartOnRest
def OopsAllBonewheels():
    """ 11322005: Enable Bonewheels and warp them to their paired normal characters. """
    DisableCharacter(1320400)
    DisableCharacter(1320401)
    DisableCharacter(1320402)
    DisableCharacter(1320403)
    DisableCharacter(1320404)
    DisableCharacter(1320405)
    DisableCharacter(1320406)
    DisableCharacter(1320407)
    DisableCharacter(1320408)
    DisableCharacter(1320409)
    DisableCharacter(1320410)
    DisableCharacter(1320411)
    DisableCharacter(1320412)
    DisableCharacter(1320413)
    DisableCharacter(1320414)
    DisableCharacter(1320415)
    DisableCharacter(1320416)
    DisableCharacter(1320417)
    DisableCharacter(1320418)
    DisableCharacter(1320419)
    DisableCharacter(1320420)
    DisableCharacter(1320421)
    DisableCharacter(1320422)
    DisableCharacter(1320423)
    DisableCharacter(1320424)
    DisableCharacter(1320425)
    DisableCharacter(1320426)
    DisableCharacter(1320427)
    DisableCharacter(1320428)
    DisableCharacter(1320429)
    DisableCharacter(1320430)
    DisableCharacter(1320431)
    DisableCharacter(1320432)
    DisableCharacter(1320433)
    DisableCharacter(1320434)
    DisableCharacter(1320435)
    DisableCharacter(1320436)
    DisableCharacter(1320437)
    DisableCharacter(1320438)
    DisableCharacter(1320439)
    DisableCharacter(1320440)
    DisableCharacter(1320441)
    DisableCharacter(1320442)
    DisableCharacter(1320443)
    DisableCharacter(1320444)
    DisableCharacter(1320445)
    DisableCharacter(1320446)
    Await(TriggerFlags.OopsAllBonewheels)  # note you don't need to be standing in the map
    DisableCharacter(6288)
    EnableCharacter(1320400)
    DisableCharacter(6290)
    EnableCharacter(1320401)
    DisableCharacter(1320211)
    EnableCharacter(1320402)
    DisableCharacter(1320212)
    EnableCharacter(1320403)
    DisableCharacter(1320213)
    EnableCharacter(1320404)
    DisableCharacter(1320214)
    EnableCharacter(1320405)
    DisableCharacter(1320215)
    EnableCharacter(1320406)
    DisableCharacter(1320216)
    EnableCharacter(1320407)
    DisableCharacter(1320217)
    EnableCharacter(1320408)
    DisableCharacter(1320218)
    EnableCharacter(1320409)
    DisableCharacter(1320219)
    EnableCharacter(1320410)
    DisableCharacter(1320220)
    EnableCharacter(1320411)
    DisableCharacter(1320100)
    EnableCharacter(1320412)
    DisableCharacter(1320101)
    EnableCharacter(1320413)
    DisableCharacter(1320102)
    EnableCharacter(1320414)
    DisableCharacter(1320221)
    EnableCharacter(1320415)
    DisableCharacter(1320222)
    EnableCharacter(1320416)
    DisableCharacter(1320223)
    EnableCharacter(1320417)
    DisableCharacter(1320224)
    EnableCharacter(1320418)
    DisableCharacter(1320225)
    EnableCharacter(1320419)
    DisableCharacter(1320226)
    EnableCharacter(1320420)
    DisableCharacter(1320227)
    EnableCharacter(1320421)
    DisableCharacter(1320228)
    EnableCharacter(1320422)
    DisableCharacter(1320229)
    EnableCharacter(1320423)
    DisableCharacter(1320230)
    EnableCharacter(1320424)
    DisableCharacter(1320231)
    EnableCharacter(1320425)
    DisableCharacter(1320232)
    EnableCharacter(1320426)
    DisableCharacter(1320233)
    EnableCharacter(1320427)
    DisableCharacter(1320234)
    EnableCharacter(1320428)
    DisableCharacter(1320201)
    EnableCharacter(1320429)
    DisableCharacter(1320202)
    EnableCharacter(1320430)
    DisableCharacter(1320203)
    EnableCharacter(1320431)
    DisableCharacter(1320204)
    EnableCharacter(1320432)
    DisableCharacter(1320205)
    EnableCharacter(1320433)
    DisableCharacter(1320206)
    EnableCharacter(1320434)
    DisableCharacter(1320207)
    EnableCharacter(1320435)
    DisableCharacter(1320208)
    EnableCharacter(1320436)
    DisableCharacter(1320209)
    EnableCharacter(1320437)
    DisableCharacter(1320210)
    EnableCharacter(1320438)
    DisableCharacter(1320801)
    EnableCharacter(1320439)
    DisableCharacter(1320701)
    EnableCharacter(1320440)
    DisableCharacter(1320702)
    EnableCharacter(1320441)
    DisableCharacter(1320703)
    EnableCharacter(1320442)
    DisableCharacter(1320704)
    EnableCharacter(1320443)
    DisableCharacter(1320705)
    EnableCharacter(1320444)
    DisableCharacter(1320706)
    EnableCharacter(1320445)
    DisableCharacter(1320707)
    EnableCharacter(1320446)
    WaitFrames(30)  # enough time for other maps to trigger too
    DisableFlag(TriggerFlags.OopsAllBonewheels)
    # No need to restart.


@RestartOnRest
def HyperAggression():
    """ 11322006: Switch AI param of every enemy to its aggressive version. """
    Await(TriggerFlags.HyperAggression or TriggerFlags.HyperAggressionReTrigger)
    
    SetAIParamID(1320211, 227050)
    SetAIParamID(1320212, 227050)
    SetAIParamID(1320213, 227050)
    SetAIParamID(1320214, 227050)
    SetAIParamID(1320215, 228050)
    SetAIParamID(1320216, 228050)
    SetAIParamID(1320217, 228050)
    SetAIParamID(1320218, 228050)
    SetAIParamID(1320219, 228050)
    SetAIParamID(1320220, 228050)
    SetAIParamID(1320100, 325050)
    SetAIParamID(1320101, 325050)
    SetAIParamID(1320102, 325050)
    SetAIParamID(1320221, 327050)
    SetAIParamID(1320222, 327050)
    SetAIParamID(1320223, 327050)
    SetAIParamID(1320224, 327050)
    SetAIParamID(1320225, 327050)
    SetAIParamID(1320226, 327050)
    SetAIParamID(1320227, 327050)
    SetAIParamID(1320228, 327050)
    SetAIParamID(1320229, 327050)
    SetAIParamID(1320230, 327050)
    SetAIParamID(1320231, 327050)
    SetAIParamID(1320232, 327050)
    SetAIParamID(1320233, 327050)
    SetAIParamID(1320234, 327050)
    SetAIParamID(1320201, 330050)
    SetAIParamID(1320202, 330050)
    SetAIParamID(1320203, 330050)
    SetAIParamID(1320204, 330050)
    SetAIParamID(1320205, 330050)
    SetAIParamID(1320206, 330050)
    SetAIParamID(1320207, 330050)
    SetAIParamID(1320208, 330050)
    SetAIParamID(1320209, 330050)
    SetAIParamID(1320210, 330050)
    SetAIParamID(1320800, 345050)
    SetAIParamID(1323900, 349050)
    SetAIParamID(1323910, 349050)
    SetAIParamID(1323901, 349150)
    SetAIParamID(1323911, 349150)
    SetAIParamID(1323902, 349150)
    SetAIParamID(1323912, 349150)
    SetAIParamID(1320700, 353050)
    SetAIParamID(1320701, 353150)
    SetAIParamID(1320702, 353150)
    SetAIParamID(1320703, 353150)
    SetAIParamID(1320704, 353150)
    SetAIParamID(1320705, 353150)
    SetAIParamID(1320706, 353150)
    SetAIParamID(1320707, 353150)
    SetAIParamID(1320600, 537050)
    SetAIParamID(1320601, 537050)
    SetAIParamID(1320602, 537050)
    SetAIParamID(1320603, 537050)
    SetAIParamID(1320604, 537050)
    SetAIParamID(1320605, 537050)
    SetAIParamID(1320606, 537050)
    SetAIParamID(1320607, 537050)
    SetAIParamID(1320608, 537050)
    SetAIParamID(1320609, 537050)
    SetAIParamID(1320400, 293050)
    SetAIParamID(1320401, 293050)
    SetAIParamID(1320402, 293050)
    SetAIParamID(1320403, 293050)
    SetAIParamID(1320404, 293050)
    SetAIParamID(1320405, 293050)
    SetAIParamID(1320406, 293050)
    SetAIParamID(1320407, 293050)
    SetAIParamID(1320408, 293050)
    SetAIParamID(1320409, 293050)
    SetAIParamID(1320410, 293050)
    SetAIParamID(1320411, 293050)
    SetAIParamID(1320412, 293050)
    SetAIParamID(1320413, 293050)
    SetAIParamID(1320414, 293050)
    SetAIParamID(1320415, 293050)
    SetAIParamID(1320416, 293050)
    SetAIParamID(1320417, 293050)
    SetAIParamID(1320418, 293050)
    SetAIParamID(1320419, 293050)
    SetAIParamID(1320420, 293050)
    SetAIParamID(1320421, 293050)
    SetAIParamID(1320422, 293050)
    SetAIParamID(1320423, 293050)
    SetAIParamID(1320424, 293050)
    SetAIParamID(1320425, 293050)
    SetAIParamID(1320426, 293050)
    SetAIParamID(1320427, 293050)
    SetAIParamID(1320428, 293050)
    SetAIParamID(1320429, 293050)
    SetAIParamID(1320430, 293050)
    SetAIParamID(1320431, 293050)
    SetAIParamID(1320432, 293050)
    SetAIParamID(1320433, 293050)
    SetAIParamID(1320434, 293050)
    SetAIParamID(1320435, 293050)
    SetAIParamID(1320436, 293050)
    SetAIParamID(1320437, 293050)
    SetAIParamID(1320438, 293050)
    SetAIParamID(1320439, 293050)
    SetAIParamID(1320440, 293050)
    SetAIParamID(1320441, 293050)
    SetAIParamID(1320442, 293050)
    SetAIParamID(1320443, 293050)
    SetAIParamID(1320444, 293050)
    SetAIParamID(1320445, 293050)
    SetAIParamID(1320446, 293050)
        
    # Common EMEVD manages the flags that control this event.
    Await(not TriggerFlags.HyperAggressionReTrigger)
    
    SetAIParamID(1320211, 227000)
    SetAIParamID(1320212, 227000)
    SetAIParamID(1320213, 227000)
    SetAIParamID(1320214, 227000)
    SetAIParamID(1320215, 228000)
    SetAIParamID(1320216, 228000)
    SetAIParamID(1320217, 228000)
    SetAIParamID(1320218, 228000)
    SetAIParamID(1320219, 228000)
    SetAIParamID(1320220, 228000)
    SetAIParamID(1320100, 325000)
    SetAIParamID(1320101, 325000)
    SetAIParamID(1320102, 325000)
    SetAIParamID(1320221, 327000)
    SetAIParamID(1320222, 327000)
    SetAIParamID(1320223, 327000)
    SetAIParamID(1320224, 327000)
    SetAIParamID(1320225, 327000)
    SetAIParamID(1320226, 327000)
    SetAIParamID(1320227, 327000)
    SetAIParamID(1320228, 327000)
    SetAIParamID(1320229, 327000)
    SetAIParamID(1320230, 327000)
    SetAIParamID(1320231, 327000)
    SetAIParamID(1320232, 327000)
    SetAIParamID(1320233, 327000)
    SetAIParamID(1320234, 327000)
    SetAIParamID(1320201, 330000)
    SetAIParamID(1320202, 330000)
    SetAIParamID(1320203, 330000)
    SetAIParamID(1320204, 330000)
    SetAIParamID(1320205, 330000)
    SetAIParamID(1320206, 330000)
    SetAIParamID(1320207, 330000)
    SetAIParamID(1320208, 330000)
    SetAIParamID(1320209, 330000)
    SetAIParamID(1320210, 330000)
    SetAIParamID(1320800, 345000)
    SetAIParamID(1323900, 349000)
    SetAIParamID(1323910, 349000)
    SetAIParamID(1323901, 349100)
    SetAIParamID(1323911, 349100)
    SetAIParamID(1323902, 349100)
    SetAIParamID(1323912, 349100)
    SetAIParamID(1320700, 353000)
    SetAIParamID(1320701, 353100)
    SetAIParamID(1320702, 353100)
    SetAIParamID(1320703, 353100)
    SetAIParamID(1320704, 353100)
    SetAIParamID(1320705, 353100)
    SetAIParamID(1320706, 353100)
    SetAIParamID(1320707, 353100)
    SetAIParamID(1320600, 537000)
    SetAIParamID(1320601, 537000)
    SetAIParamID(1320602, 537000)
    SetAIParamID(1320603, 537000)
    SetAIParamID(1320604, 537000)
    SetAIParamID(1320605, 537000)
    SetAIParamID(1320606, 537000)
    SetAIParamID(1320607, 537000)
    SetAIParamID(1320608, 537000)
    SetAIParamID(1320609, 537000)
    SetAIParamID(1320400, 293000)
    SetAIParamID(1320401, 293000)
    SetAIParamID(1320402, 293000)
    SetAIParamID(1320403, 293000)
    SetAIParamID(1320404, 293000)
    SetAIParamID(1320405, 293000)
    SetAIParamID(1320406, 293000)
    SetAIParamID(1320407, 293000)
    SetAIParamID(1320408, 293000)
    SetAIParamID(1320409, 293000)
    SetAIParamID(1320410, 293000)
    SetAIParamID(1320411, 293000)
    SetAIParamID(1320412, 293000)
    SetAIParamID(1320413, 293000)
    SetAIParamID(1320414, 293000)
    SetAIParamID(1320415, 293000)
    SetAIParamID(1320416, 293000)
    SetAIParamID(1320417, 293000)
    SetAIParamID(1320418, 293000)
    SetAIParamID(1320419, 293000)
    SetAIParamID(1320420, 293000)
    SetAIParamID(1320421, 293000)
    SetAIParamID(1320422, 293000)
    SetAIParamID(1320423, 293000)
    SetAIParamID(1320424, 293000)
    SetAIParamID(1320425, 293000)
    SetAIParamID(1320426, 293000)
    SetAIParamID(1320427, 293000)
    SetAIParamID(1320428, 293000)
    SetAIParamID(1320429, 293000)
    SetAIParamID(1320430, 293000)
    SetAIParamID(1320431, 293000)
    SetAIParamID(1320432, 293000)
    SetAIParamID(1320433, 293000)
    SetAIParamID(1320434, 293000)
    SetAIParamID(1320435, 293000)
    SetAIParamID(1320436, 293000)
    SetAIParamID(1320437, 293000)
    SetAIParamID(1320438, 293000)
    SetAIParamID(1320439, 293000)
    SetAIParamID(1320440, 293000)
    SetAIParamID(1320441, 293000)
    SetAIParamID(1320442, 293000)
    SetAIParamID(1320443, 293000)
    SetAIParamID(1320444, 293000)
    SetAIParamID(1320445, 293000)
    SetAIParamID(1320446, 293000)
    
    return RESTART


@RestartOnRest
def EnemySpeedUp():
    """ 11322200: Temporary enemy effect. """
    Await(TriggerFlags.EnemySpeedUp)
    AddSpecialEffect(6288, 200000)
    AddSpecialEffect(6290, 200000)
    AddSpecialEffect(1320960, 200000)
    AddSpecialEffect(1320961, 200000)
    AddSpecialEffect(1320962, 200000)
    AddSpecialEffect(1320211, 200000)
    AddSpecialEffect(1320212, 200000)
    AddSpecialEffect(1320213, 200000)
    AddSpecialEffect(1320214, 200000)
    AddSpecialEffect(1320215, 200000)
    AddSpecialEffect(1320216, 200000)
    AddSpecialEffect(1320217, 200000)
    AddSpecialEffect(1320218, 200000)
    AddSpecialEffect(1320219, 200000)
    AddSpecialEffect(1320220, 200000)
    AddSpecialEffect(1320100, 200000)
    AddSpecialEffect(1320101, 200000)
    AddSpecialEffect(1320102, 200000)
    AddSpecialEffect(1320221, 200000)
    AddSpecialEffect(1320222, 200000)
    AddSpecialEffect(1320223, 200000)
    AddSpecialEffect(1320224, 200000)
    AddSpecialEffect(1320225, 200000)
    AddSpecialEffect(1320226, 200000)
    AddSpecialEffect(1320227, 200000)
    AddSpecialEffect(1320228, 200000)
    AddSpecialEffect(1320229, 200000)
    AddSpecialEffect(1320230, 200000)
    AddSpecialEffect(1320231, 200000)
    AddSpecialEffect(1320232, 200000)
    AddSpecialEffect(1320233, 200000)
    AddSpecialEffect(1320234, 200000)
    AddSpecialEffect(1320201, 200000)
    AddSpecialEffect(1320202, 200000)
    AddSpecialEffect(1320203, 200000)
    AddSpecialEffect(1320204, 200000)
    AddSpecialEffect(1320205, 200000)
    AddSpecialEffect(1320206, 200000)
    AddSpecialEffect(1320207, 200000)
    AddSpecialEffect(1320208, 200000)
    AddSpecialEffect(1320209, 200000)
    AddSpecialEffect(1320210, 200000)
    AddSpecialEffect(1320800, 200000)
    AddSpecialEffect(1320801, 200000)
    AddSpecialEffect(1323900, 200000)
    AddSpecialEffect(1323910, 200000)
    AddSpecialEffect(1323901, 200000)
    AddSpecialEffect(1323911, 200000)
    AddSpecialEffect(1323902, 200000)
    AddSpecialEffect(1323912, 200000)
    AddSpecialEffect(1320700, 200000)
    AddSpecialEffect(1320701, 200000)
    AddSpecialEffect(1320702, 200000)
    AddSpecialEffect(1320703, 200000)
    AddSpecialEffect(1320704, 200000)
    AddSpecialEffect(1320705, 200000)
    AddSpecialEffect(1320706, 200000)
    AddSpecialEffect(1320707, 200000)
    WaitFrames(10)  # give other loaded maps time to trigger
    DisableFlag(TriggerFlags.EnemySpeedUp)
    return RESTART


@RestartOnRest
def EnemyExtremeSpeedUp():
    """ 11322201: Temporary enemy effect. """
    Await(TriggerFlags.EnemyExtremeSpeedUp)
    AddSpecialEffect(6288, 200001)
    AddSpecialEffect(6290, 200001)
    AddSpecialEffect(1320960, 200001)
    AddSpecialEffect(1320961, 200001)
    AddSpecialEffect(1320962, 200001)
    AddSpecialEffect(1320211, 200001)
    AddSpecialEffect(1320212, 200001)
    AddSpecialEffect(1320213, 200001)
    AddSpecialEffect(1320214, 200001)
    AddSpecialEffect(1320215, 200001)
    AddSpecialEffect(1320216, 200001)
    AddSpecialEffect(1320217, 200001)
    AddSpecialEffect(1320218, 200001)
    AddSpecialEffect(1320219, 200001)
    AddSpecialEffect(1320220, 200001)
    AddSpecialEffect(1320100, 200001)
    AddSpecialEffect(1320101, 200001)
    AddSpecialEffect(1320102, 200001)
    AddSpecialEffect(1320221, 200001)
    AddSpecialEffect(1320222, 200001)
    AddSpecialEffect(1320223, 200001)
    AddSpecialEffect(1320224, 200001)
    AddSpecialEffect(1320225, 200001)
    AddSpecialEffect(1320226, 200001)
    AddSpecialEffect(1320227, 200001)
    AddSpecialEffect(1320228, 200001)
    AddSpecialEffect(1320229, 200001)
    AddSpecialEffect(1320230, 200001)
    AddSpecialEffect(1320231, 200001)
    AddSpecialEffect(1320232, 200001)
    AddSpecialEffect(1320233, 200001)
    AddSpecialEffect(1320234, 200001)
    AddSpecialEffect(1320201, 200001)
    AddSpecialEffect(1320202, 200001)
    AddSpecialEffect(1320203, 200001)
    AddSpecialEffect(1320204, 200001)
    AddSpecialEffect(1320205, 200001)
    AddSpecialEffect(1320206, 200001)
    AddSpecialEffect(1320207, 200001)
    AddSpecialEffect(1320208, 200001)
    AddSpecialEffect(1320209, 200001)
    AddSpecialEffect(1320210, 200001)
    AddSpecialEffect(1320800, 200001)
    AddSpecialEffect(1320801, 200001)
    AddSpecialEffect(1323900, 200001)
    AddSpecialEffect(1323910, 200001)
    AddSpecialEffect(1323901, 200001)
    AddSpecialEffect(1323911, 200001)
    AddSpecialEffect(1323902, 200001)
    AddSpecialEffect(1323912, 200001)
    AddSpecialEffect(1320700, 200001)
    AddSpecialEffect(1320701, 200001)
    AddSpecialEffect(1320702, 200001)
    AddSpecialEffect(1320703, 200001)
    AddSpecialEffect(1320704, 200001)
    AddSpecialEffect(1320705, 200001)
    AddSpecialEffect(1320706, 200001)
    AddSpecialEffect(1320707, 200001)
    WaitFrames(10)  # give other loaded maps time to trigger
    DisableFlag(TriggerFlags.EnemyExtremeSpeedUp)
    return RESTART


@RestartOnRest
def EnemySpeedDown():
    """ 11322202: Temporary enemy effect. """
    Await(TriggerFlags.EnemySpeedDown)
    AddSpecialEffect(6288, 200002)
    AddSpecialEffect(6290, 200002)
    AddSpecialEffect(1320960, 200002)
    AddSpecialEffect(1320961, 200002)
    AddSpecialEffect(1320962, 200002)
    AddSpecialEffect(1320211, 200002)
    AddSpecialEffect(1320212, 200002)
    AddSpecialEffect(1320213, 200002)
    AddSpecialEffect(1320214, 200002)
    AddSpecialEffect(1320215, 200002)
    AddSpecialEffect(1320216, 200002)
    AddSpecialEffect(1320217, 200002)
    AddSpecialEffect(1320218, 200002)
    AddSpecialEffect(1320219, 200002)
    AddSpecialEffect(1320220, 200002)
    AddSpecialEffect(1320100, 200002)
    AddSpecialEffect(1320101, 200002)
    AddSpecialEffect(1320102, 200002)
    AddSpecialEffect(1320221, 200002)
    AddSpecialEffect(1320222, 200002)
    AddSpecialEffect(1320223, 200002)
    AddSpecialEffect(1320224, 200002)
    AddSpecialEffect(1320225, 200002)
    AddSpecialEffect(1320226, 200002)
    AddSpecialEffect(1320227, 200002)
    AddSpecialEffect(1320228, 200002)
    AddSpecialEffect(1320229, 200002)
    AddSpecialEffect(1320230, 200002)
    AddSpecialEffect(1320231, 200002)
    AddSpecialEffect(1320232, 200002)
    AddSpecialEffect(1320233, 200002)
    AddSpecialEffect(1320234, 200002)
    AddSpecialEffect(1320201, 200002)
    AddSpecialEffect(1320202, 200002)
    AddSpecialEffect(1320203, 200002)
    AddSpecialEffect(1320204, 200002)
    AddSpecialEffect(1320205, 200002)
    AddSpecialEffect(1320206, 200002)
    AddSpecialEffect(1320207, 200002)
    AddSpecialEffect(1320208, 200002)
    AddSpecialEffect(1320209, 200002)
    AddSpecialEffect(1320210, 200002)
    AddSpecialEffect(1320800, 200002)
    AddSpecialEffect(1320801, 200002)
    AddSpecialEffect(1323900, 200002)
    AddSpecialEffect(1323910, 200002)
    AddSpecialEffect(1323901, 200002)
    AddSpecialEffect(1323911, 200002)
    AddSpecialEffect(1323902, 200002)
    AddSpecialEffect(1323912, 200002)
    AddSpecialEffect(1320700, 200002)
    AddSpecialEffect(1320701, 200002)
    AddSpecialEffect(1320702, 200002)
    AddSpecialEffect(1320703, 200002)
    AddSpecialEffect(1320704, 200002)
    AddSpecialEffect(1320705, 200002)
    AddSpecialEffect(1320706, 200002)
    AddSpecialEffect(1320707, 200002)
    WaitFrames(10)  # give other loaded maps time to trigger
    DisableFlag(TriggerFlags.EnemySpeedDown)
    return RESTART


@RestartOnRest
def EnemyExtremeSpeedDown():
    """ 11322203: Temporary enemy effect. """
    Await(TriggerFlags.EnemyExtremeSpeedDown)
    AddSpecialEffect(6288, 200003)
    AddSpecialEffect(6290, 200003)
    AddSpecialEffect(1320960, 200003)
    AddSpecialEffect(1320961, 200003)
    AddSpecialEffect(1320962, 200003)
    AddSpecialEffect(1320211, 200003)
    AddSpecialEffect(1320212, 200003)
    AddSpecialEffect(1320213, 200003)
    AddSpecialEffect(1320214, 200003)
    AddSpecialEffect(1320215, 200003)
    AddSpecialEffect(1320216, 200003)
    AddSpecialEffect(1320217, 200003)
    AddSpecialEffect(1320218, 200003)
    AddSpecialEffect(1320219, 200003)
    AddSpecialEffect(1320220, 200003)
    AddSpecialEffect(1320100, 200003)
    AddSpecialEffect(1320101, 200003)
    AddSpecialEffect(1320102, 200003)
    AddSpecialEffect(1320221, 200003)
    AddSpecialEffect(1320222, 200003)
    AddSpecialEffect(1320223, 200003)
    AddSpecialEffect(1320224, 200003)
    AddSpecialEffect(1320225, 200003)
    AddSpecialEffect(1320226, 200003)
    AddSpecialEffect(1320227, 200003)
    AddSpecialEffect(1320228, 200003)
    AddSpecialEffect(1320229, 200003)
    AddSpecialEffect(1320230, 200003)
    AddSpecialEffect(1320231, 200003)
    AddSpecialEffect(1320232, 200003)
    AddSpecialEffect(1320233, 200003)
    AddSpecialEffect(1320234, 200003)
    AddSpecialEffect(1320201, 200003)
    AddSpecialEffect(1320202, 200003)
    AddSpecialEffect(1320203, 200003)
    AddSpecialEffect(1320204, 200003)
    AddSpecialEffect(1320205, 200003)
    AddSpecialEffect(1320206, 200003)
    AddSpecialEffect(1320207, 200003)
    AddSpecialEffect(1320208, 200003)
    AddSpecialEffect(1320209, 200003)
    AddSpecialEffect(1320210, 200003)
    AddSpecialEffect(1320800, 200003)
    AddSpecialEffect(1320801, 200003)
    AddSpecialEffect(1323900, 200003)
    AddSpecialEffect(1323910, 200003)
    AddSpecialEffect(1323901, 200003)
    AddSpecialEffect(1323911, 200003)
    AddSpecialEffect(1323902, 200003)
    AddSpecialEffect(1323912, 200003)
    AddSpecialEffect(1320700, 200003)
    AddSpecialEffect(1320701, 200003)
    AddSpecialEffect(1320702, 200003)
    AddSpecialEffect(1320703, 200003)
    AddSpecialEffect(1320704, 200003)
    AddSpecialEffect(1320705, 200003)
    AddSpecialEffect(1320706, 200003)
    AddSpecialEffect(1320707, 200003)
    WaitFrames(10)  # give other loaded maps time to trigger
    DisableFlag(TriggerFlags.EnemyExtremeSpeedDown)
    return RESTART


@RestartOnRest
def EnemyHealthRegain():
    """ 11322204: Temporary enemy effect. """
    Await(TriggerFlags.EnemyHealthRegain)
    AddSpecialEffect(6288, 200004)
    AddSpecialEffect(6290, 200004)
    AddSpecialEffect(1320960, 200004)
    AddSpecialEffect(1320961, 200004)
    AddSpecialEffect(1320962, 200004)
    AddSpecialEffect(1320211, 200004)
    AddSpecialEffect(1320212, 200004)
    AddSpecialEffect(1320213, 200004)
    AddSpecialEffect(1320214, 200004)
    AddSpecialEffect(1320215, 200004)
    AddSpecialEffect(1320216, 200004)
    AddSpecialEffect(1320217, 200004)
    AddSpecialEffect(1320218, 200004)
    AddSpecialEffect(1320219, 200004)
    AddSpecialEffect(1320220, 200004)
    AddSpecialEffect(1320100, 200004)
    AddSpecialEffect(1320101, 200004)
    AddSpecialEffect(1320102, 200004)
    AddSpecialEffect(1320221, 200004)
    AddSpecialEffect(1320222, 200004)
    AddSpecialEffect(1320223, 200004)
    AddSpecialEffect(1320224, 200004)
    AddSpecialEffect(1320225, 200004)
    AddSpecialEffect(1320226, 200004)
    AddSpecialEffect(1320227, 200004)
    AddSpecialEffect(1320228, 200004)
    AddSpecialEffect(1320229, 200004)
    AddSpecialEffect(1320230, 200004)
    AddSpecialEffect(1320231, 200004)
    AddSpecialEffect(1320232, 200004)
    AddSpecialEffect(1320233, 200004)
    AddSpecialEffect(1320234, 200004)
    AddSpecialEffect(1320201, 200004)
    AddSpecialEffect(1320202, 200004)
    AddSpecialEffect(1320203, 200004)
    AddSpecialEffect(1320204, 200004)
    AddSpecialEffect(1320205, 200004)
    AddSpecialEffect(1320206, 200004)
    AddSpecialEffect(1320207, 200004)
    AddSpecialEffect(1320208, 200004)
    AddSpecialEffect(1320209, 200004)
    AddSpecialEffect(1320210, 200004)
    AddSpecialEffect(1320800, 200004)
    AddSpecialEffect(1320801, 200004)
    AddSpecialEffect(1323900, 200004)
    AddSpecialEffect(1323910, 200004)
    AddSpecialEffect(1323901, 200004)
    AddSpecialEffect(1323911, 200004)
    AddSpecialEffect(1323902, 200004)
    AddSpecialEffect(1323912, 200004)
    AddSpecialEffect(1320700, 200004)
    AddSpecialEffect(1320701, 200004)
    AddSpecialEffect(1320702, 200004)
    AddSpecialEffect(1320703, 200004)
    AddSpecialEffect(1320704, 200004)
    AddSpecialEffect(1320705, 200004)
    AddSpecialEffect(1320706, 200004)
    AddSpecialEffect(1320707, 200004)
    WaitFrames(10)  # give other loaded maps time to trigger
    DisableFlag(TriggerFlags.EnemyHealthRegain)
    return RESTART


@RestartOnRest
def EnemyMaxHealthUp():
    """ 11322205: Temporary enemy effect. """
    Await(TriggerFlags.EnemyMaxHealthUp)
    AddSpecialEffect(6288, 200005)
    AddSpecialEffect(6290, 200005)
    AddSpecialEffect(1320960, 200005)
    AddSpecialEffect(1320961, 200005)
    AddSpecialEffect(1320962, 200005)
    AddSpecialEffect(1320211, 200005)
    AddSpecialEffect(1320212, 200005)
    AddSpecialEffect(1320213, 200005)
    AddSpecialEffect(1320214, 200005)
    AddSpecialEffect(1320215, 200005)
    AddSpecialEffect(1320216, 200005)
    AddSpecialEffect(1320217, 200005)
    AddSpecialEffect(1320218, 200005)
    AddSpecialEffect(1320219, 200005)
    AddSpecialEffect(1320220, 200005)
    AddSpecialEffect(1320100, 200005)
    AddSpecialEffect(1320101, 200005)
    AddSpecialEffect(1320102, 200005)
    AddSpecialEffect(1320221, 200005)
    AddSpecialEffect(1320222, 200005)
    AddSpecialEffect(1320223, 200005)
    AddSpecialEffect(1320224, 200005)
    AddSpecialEffect(1320225, 200005)
    AddSpecialEffect(1320226, 200005)
    AddSpecialEffect(1320227, 200005)
    AddSpecialEffect(1320228, 200005)
    AddSpecialEffect(1320229, 200005)
    AddSpecialEffect(1320230, 200005)
    AddSpecialEffect(1320231, 200005)
    AddSpecialEffect(1320232, 200005)
    AddSpecialEffect(1320233, 200005)
    AddSpecialEffect(1320234, 200005)
    AddSpecialEffect(1320201, 200005)
    AddSpecialEffect(1320202, 200005)
    AddSpecialEffect(1320203, 200005)
    AddSpecialEffect(1320204, 200005)
    AddSpecialEffect(1320205, 200005)
    AddSpecialEffect(1320206, 200005)
    AddSpecialEffect(1320207, 200005)
    AddSpecialEffect(1320208, 200005)
    AddSpecialEffect(1320209, 200005)
    AddSpecialEffect(1320210, 200005)
    AddSpecialEffect(1320800, 200005)
    AddSpecialEffect(1320801, 200005)
    AddSpecialEffect(1323900, 200005)
    AddSpecialEffect(1323910, 200005)
    AddSpecialEffect(1323901, 200005)
    AddSpecialEffect(1323911, 200005)
    AddSpecialEffect(1323902, 200005)
    AddSpecialEffect(1323912, 200005)
    AddSpecialEffect(1320700, 200005)
    AddSpecialEffect(1320701, 200005)
    AddSpecialEffect(1320702, 200005)
    AddSpecialEffect(1320703, 200005)
    AddSpecialEffect(1320704, 200005)
    AddSpecialEffect(1320705, 200005)
    AddSpecialEffect(1320706, 200005)
    AddSpecialEffect(1320707, 200005)
    WaitFrames(10)  # give other loaded maps time to trigger
    DisableFlag(TriggerFlags.EnemyMaxHealthUp)
    return RESTART


@RestartOnRest
def EnemyMaxHealthDown():
    """ 11322206: Temporary enemy effect. """
    Await(TriggerFlags.EnemyMaxHealthDown)
    AddSpecialEffect(6288, 200006)
    AddSpecialEffect(6290, 200006)
    AddSpecialEffect(1320960, 200006)
    AddSpecialEffect(1320961, 200006)
    AddSpecialEffect(1320962, 200006)
    AddSpecialEffect(1320211, 200006)
    AddSpecialEffect(1320212, 200006)
    AddSpecialEffect(1320213, 200006)
    AddSpecialEffect(1320214, 200006)
    AddSpecialEffect(1320215, 200006)
    AddSpecialEffect(1320216, 200006)
    AddSpecialEffect(1320217, 200006)
    AddSpecialEffect(1320218, 200006)
    AddSpecialEffect(1320219, 200006)
    AddSpecialEffect(1320220, 200006)
    AddSpecialEffect(1320100, 200006)
    AddSpecialEffect(1320101, 200006)
    AddSpecialEffect(1320102, 200006)
    AddSpecialEffect(1320221, 200006)
    AddSpecialEffect(1320222, 200006)
    AddSpecialEffect(1320223, 200006)
    AddSpecialEffect(1320224, 200006)
    AddSpecialEffect(1320225, 200006)
    AddSpecialEffect(1320226, 200006)
    AddSpecialEffect(1320227, 200006)
    AddSpecialEffect(1320228, 200006)
    AddSpecialEffect(1320229, 200006)
    AddSpecialEffect(1320230, 200006)
    AddSpecialEffect(1320231, 200006)
    AddSpecialEffect(1320232, 200006)
    AddSpecialEffect(1320233, 200006)
    AddSpecialEffect(1320234, 200006)
    AddSpecialEffect(1320201, 200006)
    AddSpecialEffect(1320202, 200006)
    AddSpecialEffect(1320203, 200006)
    AddSpecialEffect(1320204, 200006)
    AddSpecialEffect(1320205, 200006)
    AddSpecialEffect(1320206, 200006)
    AddSpecialEffect(1320207, 200006)
    AddSpecialEffect(1320208, 200006)
    AddSpecialEffect(1320209, 200006)
    AddSpecialEffect(1320210, 200006)
    AddSpecialEffect(1320800, 200006)
    AddSpecialEffect(1320801, 200006)
    AddSpecialEffect(1323900, 200006)
    AddSpecialEffect(1323910, 200006)
    AddSpecialEffect(1323901, 200006)
    AddSpecialEffect(1323911, 200006)
    AddSpecialEffect(1323902, 200006)
    AddSpecialEffect(1323912, 200006)
    AddSpecialEffect(1320700, 200006)
    AddSpecialEffect(1320701, 200006)
    AddSpecialEffect(1320702, 200006)
    AddSpecialEffect(1320703, 200006)
    AddSpecialEffect(1320704, 200006)
    AddSpecialEffect(1320705, 200006)
    AddSpecialEffect(1320706, 200006)
    AddSpecialEffect(1320707, 200006)
    WaitFrames(10)  # give other loaded maps time to trigger
    DisableFlag(TriggerFlags.EnemyMaxHealthDown)
    return RESTART


@RestartOnRest
def EnemyDefenseUp():
    """ 11322207: Temporary enemy effect. """
    Await(TriggerFlags.EnemyDefenseUp)
    AddSpecialEffect(6288, 200007)
    AddSpecialEffect(6290, 200007)
    AddSpecialEffect(1320960, 200007)
    AddSpecialEffect(1320961, 200007)
    AddSpecialEffect(1320962, 200007)
    AddSpecialEffect(1320211, 200007)
    AddSpecialEffect(1320212, 200007)
    AddSpecialEffect(1320213, 200007)
    AddSpecialEffect(1320214, 200007)
    AddSpecialEffect(1320215, 200007)
    AddSpecialEffect(1320216, 200007)
    AddSpecialEffect(1320217, 200007)
    AddSpecialEffect(1320218, 200007)
    AddSpecialEffect(1320219, 200007)
    AddSpecialEffect(1320220, 200007)
    AddSpecialEffect(1320100, 200007)
    AddSpecialEffect(1320101, 200007)
    AddSpecialEffect(1320102, 200007)
    AddSpecialEffect(1320221, 200007)
    AddSpecialEffect(1320222, 200007)
    AddSpecialEffect(1320223, 200007)
    AddSpecialEffect(1320224, 200007)
    AddSpecialEffect(1320225, 200007)
    AddSpecialEffect(1320226, 200007)
    AddSpecialEffect(1320227, 200007)
    AddSpecialEffect(1320228, 200007)
    AddSpecialEffect(1320229, 200007)
    AddSpecialEffect(1320230, 200007)
    AddSpecialEffect(1320231, 200007)
    AddSpecialEffect(1320232, 200007)
    AddSpecialEffect(1320233, 200007)
    AddSpecialEffect(1320234, 200007)
    AddSpecialEffect(1320201, 200007)
    AddSpecialEffect(1320202, 200007)
    AddSpecialEffect(1320203, 200007)
    AddSpecialEffect(1320204, 200007)
    AddSpecialEffect(1320205, 200007)
    AddSpecialEffect(1320206, 200007)
    AddSpecialEffect(1320207, 200007)
    AddSpecialEffect(1320208, 200007)
    AddSpecialEffect(1320209, 200007)
    AddSpecialEffect(1320210, 200007)
    AddSpecialEffect(1320800, 200007)
    AddSpecialEffect(1320801, 200007)
    AddSpecialEffect(1323900, 200007)
    AddSpecialEffect(1323910, 200007)
    AddSpecialEffect(1323901, 200007)
    AddSpecialEffect(1323911, 200007)
    AddSpecialEffect(1323902, 200007)
    AddSpecialEffect(1323912, 200007)
    AddSpecialEffect(1320700, 200007)
    AddSpecialEffect(1320701, 200007)
    AddSpecialEffect(1320702, 200007)
    AddSpecialEffect(1320703, 200007)
    AddSpecialEffect(1320704, 200007)
    AddSpecialEffect(1320705, 200007)
    AddSpecialEffect(1320706, 200007)
    AddSpecialEffect(1320707, 200007)
    WaitFrames(10)  # give other loaded maps time to trigger
    DisableFlag(TriggerFlags.EnemyDefenseUp)
    return RESTART
