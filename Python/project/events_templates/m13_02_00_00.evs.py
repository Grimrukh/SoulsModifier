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
    # <!--!>


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
