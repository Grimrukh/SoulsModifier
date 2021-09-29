"""
linked:


strings:

"""
from soulstruct.darksouls1r.events import *
from ..entities.m11_00_00_00_entities import *
from ..entities.m15_01_00_00_entities import Boxes as m15_01_Boxes, SpawnPoints as m15_01_SpawnPoints
from ..entities.common_entities import *


def Constructor():
    """ 0: Event 0 """
    RegisterBonfire(
        11100992,
        obj=Objects.o0200_0000,
        reaction_distance=2.0,
        reaction_angle=180.0,
        initial_kindle_level=0,
    )
    RegisterLadder(start_climbing_flag=11100010, stop_climbing_flag=11100011, obj=Objects.o1510_0000)
    RegisterLadder(start_climbing_flag=11100014, stop_climbing_flag=11100015, obj=Objects.o1512_0000)
    RegisterLadder(start_climbing_flag=11100016, stop_climbing_flag=11100017, obj=Objects.o1513_0000)
    SkipLinesIfClient(1)
    DisableFlag(11100410)
    SkipLinesIfFlagOn(2, 11100810)
    DisableTreasure(Objects.o0500_0015)
    DisableObject(Objects.o0500_0015)
    SkipLinesIfFlagOff(1, 11100810)
    EnableTreasure(Objects.o0500_0015)
    RunEvent(
        11100090,
        slot=1,
        args=(Objects.o1603_0000, VFX.CheckpointFog2, Boxes.CheckpointFog2FrontSide, Boxes.CheckpointFog2BackSide),
    )
    RunEvent(11105399)
    RunEvent(11100030)
    RunEvent(11100031)
    RunEvent(11100136)
    RunEvent(11100135)
    RunEvent(11100120, slot=0, args=(11100120, 10010868, Objects.o1580_0000))
    RunEvent(11100710)
    RunEvent(11100200)
    RunEvent(11100600, slot=0, args=(Objects.o0110_0000, 11100650))
    RunEvent(11105150, slot=0, args=(Characters.c2500_0011,))
    RunEvent(11105150, slot=1, args=(Characters.c2500_0012,))
    RunEvent(11105150, slot=2, args=(Characters.c2500_0013,))
    RunEvent(11105160, slot=0, args=(Characters.c2500_0014, Boxes.HangingHollow4Trigger))
    RunEvent(11105160, slot=1, args=(Characters.c2500_0015, Boxes.HangingHollow5Trigger))
    RunEvent(
        11105170,
        slot=0,
        args=(Characters.c2500_0016, Boxes.HangingHollowGroupTrigger, 0.20000000298023224),
        arg_types="iif",
    )
    RunEvent(11105170, slot=1, args=(Characters.c2500_0017, Boxes.HangingHollowGroupTrigger, 0.0), arg_types="iif")
    RunEvent(
        11105170,
        slot=2,
        args=(Characters.c2500_0018, Boxes.HangingHollowGroupTrigger, 0.4000000059604645),
        arg_types="iif",
    )
    RunEvent(
        11105170,
        slot=3,
        args=(Characters.c2500_0019, Boxes.HangingHollowGroupTrigger, 0.6000000238418579),
        arg_types="iif",
    )
    RunEvent(
        11105170,
        slot=4,
        args=(Characters.c2500_0020, Boxes.HangingHollow6Trigger, 0.30000001192092896),
        arg_types="iif",
    )
    RunEvent(11105170, slot=5, args=(Characters.c2500_0021, Boxes.HangingHollow6Trigger, 0.0), arg_types="iif")
    RunEvent(11106299)
    RunEvent(11106200, slot=0, args=(Objects.o0150_00, Objects.o0150_00, 12, -1))
    RunEvent(11106200, slot=1, args=(Objects.o0150_01, Objects.o0150_01, 13, 11006200))
    RunEvent(11106200, slot=2, args=(Objects.o0150_02, Objects.o0150_00, 12, 11006200))
    RunEvent(11106200, slot=3, args=(Objects.o0150_03, Objects.o0150_03, 13, 11006200))
    RunEvent(11106200, slot=4, args=(Objects.o0150_04, Objects.o0150_05, 12, 11006205))
    RunEvent(11106200, slot=5, args=(Objects.o0150_05, Objects.o0150_05, 13, -1))
    RunEvent(11106200, slot=6, args=(Objects.o0150_06, Objects.o0150_05, 12, 11006205))
    RunEvent(11106200, slot=7, args=(Objects.o0150_07, Objects.o0150_07, 13, -1))
    RunEvent(11106200, slot=8, args=(Objects.o0150_08, Objects.o0150_08, 13, -1))
    RunEvent(11106200, slot=9, args=(Objects.o0150_09, Objects.o0150_09, 12, -1))
    RunEvent(11106200, slot=13, args=(Objects.o0150_13, Objects.o0150_13, 13, -1))
    RunEvent(11106200, slot=14, args=(Objects.o0150_14, Objects.o0150_14, 12, -1))
    RunEvent(11106200, slot=18, args=(Objects.o0150_18, Objects.o0150_18, 12, -1))
    RunEvent(11106200, slot=19, args=(Objects.o0150_19, Objects.o0150_19, 13, -1))
    RunEvent(11106200, slot=24, args=(Objects.o0150_24, Objects.o0150_24, 12, -1))
    RunEvent(11106200, slot=27, args=(Objects.o0150_27, Objects.o0150_27, 12, -1))
    RunEvent(11106200, slot=28, args=(Objects.o0150_40, Objects.o0150_40, 13, -1))
    RunEvent(11106200, slot=29, args=(Objects.o0150_41, Objects.o0150_41, 12, -1))
    RunEvent(11106200, slot=30, args=(Objects.o0150_42, Objects.o0150_42, 12, -1))
    RunEvent(11106200, slot=31, args=(Objects.o0150_43, Objects.o0150_43, 13, -1))
    RunEvent(11106200, slot=32, args=(Objects.o0150_44, Objects.o0150_44, 12, -1))
    RunEvent(11106200, slot=33, args=(Objects.o0150_45, Objects.o0150_45, 12, -1))
    RunEvent(11100070, slot=0, args=(Objects.o1570_0000, Objects.o0500_0100, 120, 121))
    RunEvent(11100070, slot=1, args=(Objects.o1571_0000, Objects.o0500_0101, 125, 126))
    SkipLinesIfFlagOff(1, 11100400)
    DisableCharacter(Characters.c3420_0000)
    RunEvent(11105370)
    RunEvent(11100100, slot=0, args=(Objects.o1560_0000, Collisions.h0042B0))
    RunEvent(11100100, slot=1, args=(Objects.o1560_0001, VFX.FireVFX06))
    RunEvent(11100400)
    RunEvent(11105371)
    DisableSoundEvent(1103800)
    DisableObject(Objects.o1601_0000)
    DeleteVFX(VFX.BossExitFog, erase_root_only=False)
    SkipLinesIfFlagOff(4, 4)
    RunEvent(11105392)
    DisableObject(Objects.o1600_0000)
    DeleteVFX(VFX.BossEntranceFog, erase_root_only=False)
    SkipLines(10)
    RunEvent(11105390)
    RunEvent(11105391)
    RunEvent(11105393)
    RunEvent(11105392)
    RunEvent(11100000)
    RunEvent(11105394)
    RunEvent(11105395)
    RunEvent(11105396)
    RunEvent(11105397)
    RunEvent(11105398)
    RunEvent(
        11105843,
        slot=0,
        args=(4, Objects.o1600_0000, Boxes.PriscillaFogPrompt, Cylinders.PriscillaFogRotationTarget),
    )
    RunEvent(11105846, slot=0, args=(4, Objects.o1600_0000, VFX.BossEntranceFog))
    # <!--!>


def Preconstructor():
    """ 50: Event 50 """
    RunEvent(11100420)
    HumanityRegistration(Characters.c0000_0005, 8964)
    RunEvent(11105030)
    RunEvent(11100810)
    RunEvent(11105010)
    SkipLinesIfFlagOn(1, 1691)
    SetTeamType(Characters.c2730_0000, TeamType.Ally)
    RunEvent(11100530, slot=0, args=(Characters.c2730_0000, 1690, 1693, 1691))
    RunEvent(11100531, slot=0, args=(Characters.c2730_0000, 1690, 1693, 1692))
    HumanityRegistration(Characters.c0000_0003, 8470)
    HumanityRegistration(Characters.c0000_0004, 8900)
    DisableCharacter(Characters.c0000_0003)
    DisableCharacter(Characters.c0000_0004)
    RunEvent(11100040)
    RunEvent(11100532, slot=0, args=(Characters.c0000_0003, 1600, 1619, 1606, 1607, Characters.c0000_0004))
    RunEvent(11100533, slot=0, args=(Characters.c0000_0003, 1600, 1619, 1608))
    RunEvent(11100534, slot=0, args=(Characters.c0000_0003, 1600, 1619, 1609))
    RunEvent(11100535, slot=0, args=(Characters.c0000_0003, 1600, 1619, 1608, 1609))
    RunEvent(11100300)


def Event11100090(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11100090: Event 11100090 """
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


def Event11105390():
    """ 11105390: Event 11105390 """
    IfFlagOff(1, 4)
    IfActionButton(
        1,
        prompt_text=10010403,
        anchor_entity=Boxes.PriscillaFogPrompt,
        anchor_type=CoordEntityType.Region,
        line_intersects=Objects.o1600_0000,
        boss_version=True,
    )
    IfConditionTrue(0, input_condition=1)
    RotateToFaceEntity(PLAYER, Cylinders.PriscillaFogRotationTarget)
    ForceAnimation(PLAYER, 7410)
    Restart()


def Event11105391():
    """ 11105391: Event 11105391 """
    IfFlagOff(1, 4)
    IfFlagOn(1, 11105393)
    IfCharacterType(1, PLAYER, CharacterType.WhitePhantom)
    IfActionButton(
        1,
        prompt_text=10010403,
        anchor_entity=Boxes.PriscillaFogPrompt,
        anchor_type=CoordEntityType.Region,
        trigger_attribute=TriggerAttribute.All,
        line_intersects=Objects.o1600_0000,
    )
    IfConditionTrue(0, input_condition=1)
    RotateToFaceEntity(PLAYER, Cylinders.PriscillaFogRotationTarget)
    ForceAnimation(PLAYER, 7410)
    Restart()


def Event11105393():
    """ 11105393: Event 11105393 """
    SkipLinesIfThisEventOn(3)
    IfFlagOff(1, 4)
    IfCharacterInsideRegion(1, PLAYER, region=Boxes.PriscillaCombatStart)
    IfConditionTrue(0, input_condition=1)
    SkipLinesIfClient(1)
    NotifyBossBattleStart()
    ActivateMultiplayerBuffs(Characters.c2730_0000)
    EnableFlag(11105393)
    IfFlagOn(0, 4)
    End()


@RestartOnRest
def Event11105392():
    """ 11105392: Event 11105392 """
    SkipLinesIfFlagOff(7, 4)
    DisableCharacter(Characters.c2730_0000)
    DisableCharacter(Characters.c2731_0000)
    Kill(Characters.c2730_0000, award_souls=False)
    Kill(Characters.c2731_0000, award_souls=False)
    DisableBackread(Characters.c2730_0000)
    DisableBackread(Characters.c2731_0000)
    End()
    SkipLinesIfFlagOff(1, 1691)
    SetTeamType(Characters.c2730_0000, TeamType.Ally)
    DisableAI(Characters.c2730_0000)
    DisableHealthBar(Characters.c2730_0000)
    IfCharacterAlive(1, Characters.c2730_0000)
    IfFlagOn(1, 11105393)
    IfAttacked(1, Characters.c2730_0000, attacker=PLAYER)
    IfFlagOn(2, 11105393)
    IfCharacterInsideRegion(2, PLAYER, region=Boxes.CrossbreedPriscillaMusic)
    IfFlagOn(2, 1691)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EnableAI(Characters.c2730_0000)
    SetTeamType(Characters.c2730_0000, TeamType.Boss)
    EnableBossHealthBar(Characters.c2730_0000, name=2730, slot=0)
    EnableFlag(11105392)
    IfFlagOn(0, 4)
    End()


def Event11100000():
    """ 11100000: Event 11100000 """
    EndIfThisEventOn()
    IfCharacterDead(0, Characters.c2730_0000)
    EnableFlag(4)
    KillBoss(1100160)
    SkipLinesIfClient(1)
    AwardAchievement(40)
    Kill(Characters.c2731_0000, award_souls=False)
    DisableBackread(Characters.c2731_0000)
    DisableObject(Objects.o1600_0000)
    DeleteVFX(VFX.BossEntranceFog, erase_root_only=True)


def Event11105394():
    """ 11105394: Event 11105394 """
    DisableNetworkSync()
    IfFlagOff(1, 4)
    IfFlagOn(1, 11105390)
    IfCharacterInsideRegion(1, PLAYER, region=Boxes.PriscillaCombatStart)
    SkipLinesIfHost(1)
    IfFlagOn(1, 11105391)
    IfConditionTrue(0, input_condition=1)
    EnableSoundEvent(1103800)
    EnableFlag(11105394)
    IfFlagOn(0, 4)
    End()


def Event11105395():
    """ 11105395: Event 11105395 """
    DisableNetworkSync()
    IfFlagOn(1, 4)
    IfCharacterInsideRegion(1, PLAYER, region=Boxes.CrossbreedPriscillaMusic)
    IfFlagOn(2, 11105380)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    DisableSoundEvent(1103800)
    EnableFlag(11105395)
    IfFlagOn(0, 4)
    End()


@RestartOnRest
def Event11105396():
    """ 11105396: Event 11105396 """
    DisableCharacter(Characters.c2731_0000)
    EndIfFlagOn(4)
    SkipLinesIfThisEventOff(3)
    SetDisplayMask(Characters.c2730_0000, bit_index=0, switch_type=OnOffChange.On)
    SetCollisionMask(Characters.c2730_0000, bit_index=1, switch_type=OnOffChange.Off)
    End()
    IfCharacterBackreadEnabled(0, Characters.c2730_0000)
    CreateNPCPart(
        Characters.c2730_0000,
        npc_part_id=2730,
        part_index=NPCPartType.Part1,
        part_health=158,
        damage_correction=1.0,
        body_damage_correction=1.0,
        is_invincible=False,
        start_in_stop_state=False,
    )
    IfHealthGreaterThan(1, Characters.c2730_0000, 0.0)
    IfCharacterPartHealthLessThanOrEqual(1, Characters.c2730_0000, npc_part_id=2730, value=0)
    IfFlagOff(1, 11105381)
    IfAttacked(1, Characters.c2730_0000, attacker=PLAYER)
    IfHealthLessThanOrEqual(2, Characters.c2730_0000, 0.0)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(2)
    ResetAnimation(Characters.c2730_0000, disable_interpolation=False)
    ForceAnimation(Characters.c2730_0000, 8000)
    IfHasTAEEvent(0, Characters.c2730_0000, tae_event_id=400)
    EnableCharacter(Characters.c2731_0000)
    SetDisplayMask(Characters.c2730_0000, bit_index=0, switch_type=OnOffChange.On)
    SetCollisionMask(Characters.c2730_0000, bit_index=1, switch_type=OnOffChange.Off)
    Move(
        Characters.c2731_0000,
        destination=Characters.c2730_0000,
        destination_type=CoordEntityType.Character,
        model_point=40,
        copy_draw_parent=Characters.c2730_0000,
    )
    ForceAnimation(Characters.c2731_0000, 8100)
    IfCharacterHuman(-7, PLAYER)
    IfCharacterHollow(-7, PLAYER)
    SkipLinesIfConditionFalse(1, -7)
    AwardItemLot(27310000, host_only=True)
    EnableFlag(11105396)
    IfFlagOn(0, 4)
    End()


@RestartOnRest
def Event11105397():
    """ 11105397: Event 11105397 """
    IfHasTAEEvent(0, Characters.c2730_0000, tae_event_id=600)
    DisableHealthBar(Characters.c2730_0000)
    DisableBossHealthBar(Characters.c2730_0000, name=2730, slot=0)
    EnableFlag(11105381)
    DisableFlagRange((11105110, 11105119))
    SkipLinesIfClient(44)
    SetNetworkUpdateAuthority(Characters.c2730_0000, UpdateAuthority.Forced)
    EnableRandomFlagInRange((11105110, 11105119))
    SkipLinesIfFlagOff(3, 11105110)
    IfCharacterInsideRegion(1, Characters.c2730_0000, region=Spheres.PriscillaWarpPoint0)
    SkipLinesIfConditionTrue(2, 1)
    Move(
        Characters.c2730_0000,
        destination=Spheres.PriscillaWarpPoint0,
        destination_type=CoordEntityType.Region,
        short_move=True,
    )
    SkipLinesIfFlagOff(3, 11105111)
    IfCharacterInsideRegion(2, Characters.c2730_0000, region=Spheres.PriscillaWarpPoint1)
    SkipLinesIfConditionTrue(2, 2)
    Move(
        Characters.c2730_0000,
        destination=Spheres.PriscillaWarpPoint1,
        destination_type=CoordEntityType.Region,
        short_move=True,
    )
    SkipLinesIfFlagOff(3, 11105112)
    IfCharacterInsideRegion(3, Characters.c2730_0000, region=Spheres.PriscillaWarpPoint2)
    SkipLinesIfConditionTrue(2, 3)
    Move(
        Characters.c2730_0000,
        destination=Spheres.PriscillaWarpPoint2,
        destination_type=CoordEntityType.Region,
        short_move=True,
    )
    SkipLinesIfFlagOff(3, 11105113)
    IfCharacterInsideRegion(4, Characters.c2730_0000, region=Spheres.PriscillaWarpPoint3)
    SkipLinesIfConditionTrue(2, 4)
    Move(
        Characters.c2730_0000,
        destination=Spheres.PriscillaWarpPoint3,
        destination_type=CoordEntityType.Region,
        short_move=True,
    )
    SkipLinesIfFlagOff(3, 11105114)
    IfCharacterInsideRegion(5, Characters.c2730_0000, region=Spheres.PriscillaWarpPoint4)
    SkipLinesIfConditionTrue(2, 5)
    Move(
        Characters.c2730_0000,
        destination=Spheres.PriscillaWarpPoint4,
        destination_type=CoordEntityType.Region,
        short_move=True,
    )
    SkipLinesIfFlagOff(3, 11105115)
    IfCharacterInsideRegion(6, Characters.c2730_0000, region=Spheres.PriscillaWarpPoint5)
    SkipLinesIfConditionTrue(2, 6)
    Move(
        Characters.c2730_0000,
        destination=Spheres.PriscillaWarpPoint5,
        destination_type=CoordEntityType.Region,
        short_move=True,
    )
    SkipLinesIfFlagOff(3, 11105116)
    IfCharacterInsideRegion(7, Characters.c2730_0000, region=Spheres.PriscillaWarpPoint6)
    SkipLinesIfConditionTrue(2, 7)
    Move(
        Characters.c2730_0000,
        destination=Spheres.PriscillaWarpPoint6,
        destination_type=CoordEntityType.Region,
        short_move=True,
    )
    SkipLinesIfFlagOff(3, 11105117)
    IfCharacterInsideRegion(-1, Characters.c2730_0000, region=Spheres.PriscillaWarpPoint7)
    SkipLinesIfConditionTrue(2, -1)
    Move(
        Characters.c2730_0000,
        destination=Spheres.PriscillaWarpPoint7,
        destination_type=CoordEntityType.Region,
        short_move=True,
    )
    SkipLinesIfFlagOff(3, 11105118)
    IfCharacterInsideRegion(-2, Characters.c2730_0000, region=Spheres.PriscillaWarpPoint8)
    SkipLinesIfConditionTrue(2, -2)
    Move(
        Characters.c2730_0000,
        destination=Spheres.PriscillaWarpPoint8,
        destination_type=CoordEntityType.Region,
        short_move=True,
    )
    SkipLinesIfFlagOff(3, 11105119)
    IfCharacterInsideRegion(-3, Characters.c2730_0000, region=Spheres.PriscillaWarpPoint9)
    SkipLinesIfConditionTrue(2, -3)
    Move(
        Characters.c2730_0000,
        destination=Spheres.PriscillaWarpPoint9,
        destination_type=CoordEntityType.Region,
        short_move=True,
    )
    SkipLines(1)
    Move(
        Characters.c2730_0000,
        destination=Spheres.PriscillaWarpPoint0,
        destination_type=CoordEntityType.Region,
        short_move=True,
    )
    IfDoesNotHaveTAEEvent(0, Characters.c2730_0000, tae_event_id=600)
    Restart()


@RestartOnRest
def Event11105398():
    """ 11105398: Event 11105398 """
    DisableNetworkSync()
    IfHasTAEEvent(0, Characters.c2730_0000, tae_event_id=700)
    EnableHealthBar(Characters.c2730_0000)
    EnableBossHealthBar(Characters.c2730_0000, name=2730, slot=0)
    DisableFlag(11105381)
    IfDoesNotHaveTAEEvent(0, Characters.c2730_0000, tae_event_id=700)
    Restart()


def Event11105399():
    """ 11105399: Event 11105399 """
    EndIfClient()
    DisableNetworkSync()
    IfInsideMap(0, game_map=ANOR_LONDO)
    IfInsideMap(0, game_map=PAINTED_WORLD)
    RestartEvent(11105390)
    RestartEvent(11105391)
    RestartEvent(11105392)
    RestartEvent(11105393)
    RestartEvent(11105394)
    RestartEvent(11105395)
    RestartEvent(11105396)
    RestartEvent(11105397)
    RestartEvent(11105398)
    DisableFlagRange((11105390, 11105399))
    Restart()


@RestartOnRest
def Event11105150(_, arg_0_3: int):
    """ 11105150: Event 11105150 """
    SkipLinesIfThisEventSlotOff(2)
    ResetStandbyAnimationSettings(arg_0_3)
    End()
    DisableCharacterCollision(arg_0_3)
    DisableAI(arg_0_3)
    DisableGravity(arg_0_3)
    IfEntityWithinDistance(0, PLAYER, arg_0_3, radius=5.0)
    EnableGravity(arg_0_3)
    EnableCharacterCollision(arg_0_3)
    SetStandbyAnimationSettings(arg_0_3, cancel_animation=9060)
    EnableAI(arg_0_3)


@RestartOnRest
def Event11105160(_, arg_0_3: int, arg_4_7: int):
    """ 11105160: Event 11105160 """
    SkipLinesIfThisEventSlotOff(2)
    ResetStandbyAnimationSettings(arg_0_3)
    End()
    DisableCharacterCollision(arg_0_3)
    DisableAI(arg_0_3)
    DisableGravity(arg_0_3)
    IfCharacterInsideRegion(0, PLAYER, region=arg_4_7)
    EnableGravity(arg_0_3)
    EnableCharacterCollision(arg_0_3)
    SetStandbyAnimationSettings(arg_0_3, cancel_animation=9060)
    EnableAI(arg_0_3)


@RestartOnRest
def Event11105170(_, arg_0_3: int, arg_4_7: int, arg_8_11: float):
    """ 11105170: Event 11105170 """
    SkipLinesIfThisEventSlotOff(2)
    ResetStandbyAnimationSettings(arg_0_3)
    End()
    DisableCharacterCollision(arg_0_3)
    DisableAI(arg_0_3)
    DisableGravity(arg_0_3)
    IfCharacterInsideRegion(0, PLAYER, region=arg_4_7)
    Wait(arg_8_11)
    EnableGravity(arg_0_3)
    EnableCharacterCollision(arg_0_3)
    SetStandbyAnimationSettings(arg_0_3, cancel_animation=9060)
    EnableAI(arg_0_3)


@RestartOnRest
def Event11106200(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11106200: Event 11106200 """
    DisableNetworkSync()
    SkipLinesIfEqual(1, left=arg_12_15, right=-1)
    IfFlagOn(-1, arg_12_15)
    IfEntityWithinDistance(-1, PLAYER, arg_4_7, radius=7.0)
    IfConditionTrue(0, input_condition=-1)
    ForceAnimation(arg_0_3, arg_8_11, wait_for_completion=True)
    DisableObject(arg_0_3)


@RestartOnRest
def Event11106299():
    """ 11106299: Event 11106299 """
    DisableNetworkSync()
    IfCharacterInsideRegion(0, PLAYER, region=Boxes.CrowsFlockArea)
    RunEvent(11106298, slot=-1, args=(Objects.o0150_28, 13))
    RunEvent(11106298, slot=-1, args=(Objects.o0150_29, 12))
    RunEvent(11106298, slot=-1, args=(Objects.o0150_30, 12))
    RunEvent(11106298, slot=-1, args=(Objects.o0150_31, 13))
    RunEvent(11106298, slot=-1, args=(Objects.o0150_32, 12))
    RunEvent(11106298, slot=-1, args=(Objects.o0150_33, 12))
    RunEvent(11106298, slot=-1, args=(Objects.o0150_34, 13))
    RunEvent(11106298, slot=-1, args=(Objects.o0150_35, 12))
    RunEvent(11106298, slot=-1, args=(Objects.o0150_36, 12))
    RunEvent(11106298, slot=-1, args=(Objects.o0150_37, 13))
    RunEvent(11106298, slot=-1, args=(Objects.o0150_38, 12))
    RunEvent(11106298, slot=-1, args=(Objects.o0150_39, 12))


@UnknownRestart
def Event11106298(_, arg_0_3: int, arg_4_7: int):
    """ 11106298: Event 11106298 """
    ForceAnimation(arg_0_3, arg_4_7, wait_for_completion=True)
    DisableObject(arg_0_3)


def Event11100070(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11100070: Event 11100070 """
    SkipLinesIfThisEventSlotOff(4)
    EndOfAnimation(arg_4_7, arg_12_15)
    PostDestruction(arg_0_3)
    EnableTreasure(arg_4_7)
    End()
    DisableTreasure(arg_4_7)
    SkipLinesIfClient(1)
    CreateObjectVFX(99005, obj=arg_4_7, model_point=90)
    ForceAnimation(arg_4_7, arg_8_11, loop=True)
    IfObjectDestroyed(0, arg_0_3)
    ForceAnimation(arg_4_7, arg_12_15, wait_for_completion=True)
    SkipLinesIfClient(1)
    DeleteObjectVFX(arg_4_7, erase_root=True)
    EnableTreasure(arg_4_7)


@RestartOnRest
def Event11105370():
    """ 11105370: Event 11105370 """
    SkipLinesIfFlagOff(2, 11100410)
    ResetStandbyAnimationSettings(Characters.c3420_0000)
    End()
    IfCharacterType(3, PLAYER, CharacterType.BlackPhantom)
    IfConditionFalse(1, input_condition=3)
    IfCharacterInsideRegion(1, PLAYER, region=Boxes.UndeadDragonWakeTrigger)
    IfConditionFalse(2, input_condition=3)
    IfAttacked(2, Characters.c3420_0000, attacker=PLAYER)
    IfConditionTrue(-2, input_condition=1)
    IfConditionTrue(-2, input_condition=2)
    IfConditionTrue(0, input_condition=-2)
    EnableFlag(11100410)
    ResetStandbyAnimationSettings(Characters.c3420_0000)
    ForceAnimation(Characters.c3420_0000, 9060)
    PlaySoundEffect(
        anchor_entity=Boxes.UndeadDragonSnoringSoundEffect,
        sound_type=SoundType.a_Ambient,
        sound_id=110003420,
    )


@RestartOnRest
def Event11105371():
    """ 11105371: Event 11105371 """
    DisableCharacter(Characters.c3422_0000)
    SkipLinesIfThisEventOff(4)
    IfCharacterBackreadEnabled(0, Characters.c3420_0000)
    SetDisplayMask(Characters.c3420_0000, bit_index=0, switch_type=OnOffChange.On)
    SetDisplayMask(Characters.c3420_0000, bit_index=1, switch_type=OnOffChange.On)
    End()
    IfHasTAEEvent(0, Characters.c3420_0000, tae_event_id=400)
    SetDisplayMask(Characters.c3420_0000, bit_index=0, switch_type=OnOffChange.On)
    SetDisplayMask(Characters.c3420_0000, bit_index=1, switch_type=OnOffChange.On)
    Move(
        Characters.c3422_0000,
        destination=Characters.c3420_0000,
        destination_type=CoordEntityType.Character,
        model_point=30,
        copy_draw_parent=Characters.c3420_0000,
    )
    EnableCharacter(Characters.c3422_0000)
    ForceAnimation(Characters.c3422_0000, 8100, wait_for_completion=True)
    DisableCharacter(Characters.c3422_0000)


def Event11100100(_, arg_0_3: int, arg_4_7: int):
    """ 11100100: Event 11100100 """
    SkipLinesIfThisEventSlotOff(4)
    DestroyObject(arg_0_3)
    ForceAnimation(arg_0_3, 0)
    DeleteVFX(arg_4_7, erase_root_only=False)
    End()
    IfObjectDestroyed(0, arg_0_3)
    DeleteVFX(arg_4_7, erase_root_only=True)


@RestartOnRest
def Event11100400():
    """ 11100400: Event 11100400 """
    EnableImmortality(Characters.c3421_0000)
    EnableInvincibility(Characters.c3421_0000)
    DisableHealthBar(Characters.c3421_0000)
    SkipLinesIfThisEventOff(2)
    DisableCharacter(Characters.c3420_0000)
    End()
    SetBackreadStateAlternate(Characters.c3420_0000, state=True)
    DisableGravity(Characters.c3420_0000)
    IfCharacterDead(0, Characters.c3420_0000)
    EnableFlag(11100400)


def Event11100030():
    """ 11100030: Event 11100030 """
    SkipLinesIfThisEventSlotOff(3)
    EndOfAnimation(Objects.o1500_0000, 2)
    DisableNavmeshType(Navigation.CrowDemonActivityPointB, NavmeshType.Solid)
    End()
    EnableNavmeshType(Navigation.CrowDemonActivityPointB, NavmeshType.Solid)
    IfFlagOff(1, 11100700)
    IfActionButton(
        1,
        prompt_text=10010400,
        anchor_entity=Objects.o1500_0000,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        model_point=100,
        trigger_attribute=TriggerAttribute.All,
    )
    IfConditionTrue(0, input_condition=1)
    Move(PLAYER, destination=Cylinders.ShortcutDoorPlayerSnap, destination_type=CoordEntityType.Region, short_move=True)
    ForceAnimation(PLAYER, 7120)
    ForceAnimation(Objects.o1500_0000, 1, wait_for_completion=True)
    DisableNavmeshType(Navigation.CrowDemonActivityPointB, NavmeshType.Solid)


def Event11100031():
    """ 11100031: Event 11100031 """
    DisableNetworkSync()
    IfFlagOff(1, 11100030)
    IfActionButton(
        1,
        prompt_text=10010400,
        anchor_entity=Objects.o1500_0000,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        model_point=101,
        trigger_attribute=TriggerAttribute.All,
    )
    IfConditionTrue(0, input_condition=1)
    DisplayDialog(
        10010161,
        anchor_entity=Objects.o1500_0000,
        display_distance=3.0,
        button_type=ButtonType.Yes_or_No,
        number_buttons=NumberButtons.NoButton,
    )
    Restart()


def Event11100120(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 11100120: Event 11100120 """
    EndIfThisEventSlotOn()
    IfObjectActivated(0, obj_act_id=arg_0_3)
    EndIfClient()
    DisplayDialog(
        arg_4_7,
        anchor_entity=arg_8_11,
        display_distance=3.0,
        button_type=ButtonType.Yes_or_No,
        number_buttons=NumberButtons.NoButton,
    )


def Event11100135():
    """ 11100135: Event 11100135 """
    SkipLinesIfThisEventSlotOff(4)
    EndOfAnimation(Objects.o1540_0000, 1)
    EndOfAnimation(Objects.o1520_0000, 1)
    DisableNavmeshType(Navigation.Navmesh_EventNavmesh02, NavmeshType.Solid)
    End()
    IfActionButton(
        0,
        prompt_text=10010503,
        anchor_entity=Objects.o1550_0000,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        model_point=192,
        trigger_attribute=TriggerAttribute.All,
    )
    DisableObject(Objects.o0150_07)
    DisableObject(Objects.o0150_08)
    DisableObject(Objects.o0150_09)
    Move(
        PLAYER,
        destination=Objects.o1550_0000,
        destination_type=CoordEntityType.Object,
        model_point=191,
        short_move=True,
    )
    ForceAnimation(PLAYER, 8010)
    ForceAnimation(Objects.o1550_0000, 1, wait_for_completion=True)
    SkipLinesIfSingleplayer(2)
    PlayCutscene(110000, skippable=False, fade_out=False, player_id=PLAYER)
    SkipLines(1)
    PlayCutscene(110000, skippable=True, fade_out=False, player_id=PLAYER)
    ForceAnimation(Objects.o1540_0000, 1)
    ForceAnimation(Objects.o1520_0000, 1)
    DisableNavmeshType(Navigation.Navmesh_EventNavmesh02, NavmeshType.Solid)


def Event11100136():
    """ 11100136: Event 11100136 """
    DisableNetworkSync()
    IfFlagOff(1, 11100135)
    IfActionButton(
        1,
        prompt_text=10010400,
        anchor_entity=Objects.o1520_0000,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        model_point=100,
        trigger_attribute=TriggerAttribute.All,
    )
    IfConditionTrue(0, input_condition=1)
    DisplayDialog(
        10010160,
        anchor_entity=Objects.o1520_0000,
        display_distance=3.0,
        button_type=ButtonType.Yes_or_No,
        number_buttons=NumberButtons.NoButton,
    )
    Restart()


@RestartOnRest
def Event11100420():
    """ 11100420: Event 11100420 """
    SkipLinesIfThisEventOff(3)
    Move(
        Characters.c2570_0000,
        destination=Cylinders.BerenikeKnightAmbushNest,
        destination_type=CoordEntityType.Region,
        short_move=True,
    )
    SetNest(Characters.c2570_0000, Cylinders.BerenikeKnightAmbushNest)
    End()
    DisableAI(Characters.c2570_0000)
    IfCharacterInsideRegion(-1, PLAYER, region=Boxes.BerenikeKnightAmbushTrigger)
    IfAttacked(-1, Characters.c2570_0000, attacker=PLAYER)
    IfAttacked(-1, Characters.c2500_0016, attacker=PLAYER)
    IfAttacked(-1, Characters.c2500_0017, attacker=PLAYER)
    IfAttacked(-1, Characters.c2500_0018, attacker=PLAYER)
    IfAttacked(-1, Characters.c2500_0019, attacker=PLAYER)
    IfConditionTrue(0, input_condition=-1)
    ForceAnimation(Characters.c2570_0000, 500)
    EnableAI(Characters.c2570_0000)
    SetNest(Characters.c2570_0000, Cylinders.BerenikeKnightAmbushNest)


def Event11100710():
    """ 11100710: Event 11100710 """
    DisableFlag(11105380)
    IfHost(1)
    IfFlagOff(1, 1691)
    IfCharacterInsideRegion(1, PLAYER, region=Boxes.ExitCutsceneTrigger)
    IfConditionTrue(0, input_condition=1)
    EnableImmortality(Characters.c2730_0000)
    EndIfClient()
    DisableImmortality(Characters.c2730_0000)
    EnableFlag(11105380)
    SkipLinesIfFlagOn(1, 4)
    IfFlagOn(0, 11105395)
    SkipLinesIfFlagOff(1, 11510400)
    SetMapDrawParamSlot(15, slot=2)
    PlayCutscene(
        110035,
        skippable=True,
        fade_out=False,
        player_id=PLAYER,
        move_to_region=m15_01_Boxes.ArriveFromPaintedWorld,
        move_to_map=ANOR_LONDO,
    )
    WaitFrames(1)
    SkipLinesIfThisEventOn(1)
    AwardItemLot(9030, host_only=True)
    SetRespawnPoint(m15_01_SpawnPoints.SpawnPoint0)
    SaveRequest()
    Restart()


@RestartOnRest
def Event11105010():
    """ 11105010: Event 11105010 """
    EndIfThisEventOn()
    IfCharacterAlive(1, Characters.c2830_0000)
    IfCharacterAlive(1, Characters.c2830_0001)
    IfCharacterAlive(1, Characters.c2830_0002)
    IfCharacterAlive(1, Characters.c2830_0003)
    IfCharacterAlive(1, Characters.c2830_0004)
    IfCharacterAlive(1, Characters.c2830_0005)
    IfCharacterAlive(1, Characters.c2830_0006)
    IfCharacterAlive(1, Characters.c2830_0007)
    IfCharacterAlive(1, Characters.c2830_0008)
    IfCharacterAlive(1, Characters.c2830_0009)
    IfCharacterAlive(1, Characters.c2830_0010)
    IfCharacterAlive(1, Characters.c2830_0011)
    IfCharacterAlive(1, Characters.c2830_0012)
    IfCharacterAlive(1, Characters.c2830_0013)
    EndIfConditionFalse(1)
    DisableCharacterCollision(Characters.c2830_0000)
    DisableCharacterCollision(Characters.c2830_0001)
    DisableCharacterCollision(Characters.c2830_0002)
    DisableCharacterCollision(Characters.c2830_0003)
    DisableCharacterCollision(Characters.c2830_0004)
    DisableCharacterCollision(Characters.c2830_0005)
    DisableCharacterCollision(Characters.c2830_0006)
    DisableCharacterCollision(Characters.c2830_0007)
    DisableCharacterCollision(Characters.c2830_0008)
    DisableCharacterCollision(Characters.c2830_0009)
    DisableCharacterCollision(Characters.c2830_0010)
    DisableCharacterCollision(Characters.c2830_0011)
    DisableCharacterCollision(Characters.c2830_0012)
    DisableCharacterCollision(Characters.c2830_0013)
    DisableAnimations(Characters.c2830_0000)
    DisableAnimations(Characters.c2830_0001)
    DisableAnimations(Characters.c2830_0002)
    DisableAnimations(Characters.c2830_0003)
    DisableAnimations(Characters.c2830_0004)
    DisableAnimations(Characters.c2830_0005)
    DisableAnimations(Characters.c2830_0006)
    DisableAnimations(Characters.c2830_0007)
    DisableAnimations(Characters.c2830_0008)
    DisableAnimations(Characters.c2830_0009)
    DisableAnimations(Characters.c2830_0010)
    DisableAnimations(Characters.c2830_0011)
    DisableAnimations(Characters.c2830_0012)
    DisableAnimations(Characters.c2830_0013)
    DisableGravity(Characters.c2830_0000)
    DisableGravity(Characters.c2830_0001)
    DisableGravity(Characters.c2830_0002)
    DisableGravity(Characters.c2830_0003)
    DisableGravity(Characters.c2830_0004)
    DisableGravity(Characters.c2830_0005)
    DisableGravity(Characters.c2830_0006)
    DisableGravity(Characters.c2830_0007)
    DisableGravity(Characters.c2830_0008)
    DisableGravity(Characters.c2830_0009)
    DisableGravity(Characters.c2830_0010)
    DisableGravity(Characters.c2830_0011)
    DisableGravity(Characters.c2830_0012)
    DisableGravity(Characters.c2830_0013)
    DisableAI(Characters.c2830_0000)
    DisableAI(Characters.c2830_0001)
    DisableAI(Characters.c2830_0002)
    DisableAI(Characters.c2830_0003)
    DisableAI(Characters.c2830_0004)
    DisableAI(Characters.c2830_0005)
    DisableAI(Characters.c2830_0006)
    DisableAI(Characters.c2830_0007)
    DisableAI(Characters.c2830_0008)
    DisableAI(Characters.c2830_0009)
    DisableAI(Characters.c2830_0010)
    DisableAI(Characters.c2830_0011)
    DisableAI(Characters.c2830_0012)
    DisableAI(Characters.c2830_0013)
    SetStandbyAnimationSettings(Characters.c2830_0000, standby_animation=9000)
    SetStandbyAnimationSettings(Characters.c2830_0001, standby_animation=9000)
    SetStandbyAnimationSettings(Characters.c2830_0002, standby_animation=9000)
    SetStandbyAnimationSettings(Characters.c2830_0003, standby_animation=9000)
    SetStandbyAnimationSettings(Characters.c2830_0004, standby_animation=9000)
    SetStandbyAnimationSettings(Characters.c2830_0005, standby_animation=9000)
    SetStandbyAnimationSettings(Characters.c2830_0006, standby_animation=9000)
    SetStandbyAnimationSettings(Characters.c2830_0007, standby_animation=9000)
    SetStandbyAnimationSettings(Characters.c2830_0008, standby_animation=9000)
    SetStandbyAnimationSettings(Characters.c2830_0009, standby_animation=9000)
    SetStandbyAnimationSettings(Characters.c2830_0010, standby_animation=9000)
    SetStandbyAnimationSettings(Characters.c2830_0011, standby_animation=9000)
    SetStandbyAnimationSettings(Characters.c2830_0012, standby_animation=9000)
    SetStandbyAnimationSettings(Characters.c2830_0013, standby_animation=9000)
    Move(Characters.c2830_0000, destination=Boxes.Phalanx00, destination_type=CoordEntityType.Region, short_move=True)
    Move(Characters.c2830_0001, destination=Boxes.Phalanx01, destination_type=CoordEntityType.Region, short_move=True)
    Move(Characters.c2830_0002, destination=Boxes.Phalanx02, destination_type=CoordEntityType.Region, short_move=True)
    Move(Characters.c2830_0003, destination=Boxes.Phalanx03, destination_type=CoordEntityType.Region, short_move=True)
    Move(Characters.c2830_0004, destination=Boxes.Phalanx04, destination_type=CoordEntityType.Region, short_move=True)
    Move(Characters.c2830_0005, destination=Boxes.Phalanx05, destination_type=CoordEntityType.Region, short_move=True)
    Move(Characters.c2830_0006, destination=Boxes.Phalanx06, destination_type=CoordEntityType.Region, short_move=True)
    Move(Characters.c2830_0007, destination=Boxes.Phalanx07, destination_type=CoordEntityType.Region, short_move=True)
    Move(Characters.c2830_0008, destination=Boxes.Phalanx08, destination_type=CoordEntityType.Region, short_move=True)
    Move(Characters.c2830_0009, destination=Boxes.Phalanx09, destination_type=CoordEntityType.Region, short_move=True)
    Move(Characters.c2830_0010, destination=Boxes.Phalanx10, destination_type=CoordEntityType.Region, short_move=True)
    Move(Characters.c2830_0011, destination=Boxes.Phalanx11, destination_type=CoordEntityType.Region, short_move=True)
    Move(Characters.c2830_0012, destination=Boxes.Phalanx12, destination_type=CoordEntityType.Region, short_move=True)
    Move(Characters.c2830_0013, destination=Boxes.Phalanx13, destination_type=CoordEntityType.Region, short_move=True)
    IfCharacterInsideRegion(0, PLAYER, region=Boxes.HollowPhalanxComesApart)
    EnableAI(Characters.c2830_0000)
    EnableAI(Characters.c2830_0001)
    EnableAI(Characters.c2830_0002)
    EnableAI(Characters.c2830_0003)
    EnableAI(Characters.c2830_0004)
    EnableAI(Characters.c2830_0005)
    EnableAI(Characters.c2830_0006)
    EnableAI(Characters.c2830_0007)
    EnableAI(Characters.c2830_0008)
    EnableAI(Characters.c2830_0009)
    EnableAI(Characters.c2830_0010)
    EnableAI(Characters.c2830_0011)
    EnableAI(Characters.c2830_0012)
    EnableAI(Characters.c2830_0013)
    ResetStandbyAnimationSettings(Characters.c2830_0000)
    ResetStandbyAnimationSettings(Characters.c2830_0001)
    ResetStandbyAnimationSettings(Characters.c2830_0002)
    ResetStandbyAnimationSettings(Characters.c2830_0003)
    ResetStandbyAnimationSettings(Characters.c2830_0004)
    ResetStandbyAnimationSettings(Characters.c2830_0005)
    ResetStandbyAnimationSettings(Characters.c2830_0006)
    ResetStandbyAnimationSettings(Characters.c2830_0007)
    ResetStandbyAnimationSettings(Characters.c2830_0008)
    ResetStandbyAnimationSettings(Characters.c2830_0009)
    ResetStandbyAnimationSettings(Characters.c2830_0010)
    ResetStandbyAnimationSettings(Characters.c2830_0011)
    ResetStandbyAnimationSettings(Characters.c2830_0012)
    ResetStandbyAnimationSettings(Characters.c2830_0013)
    EnableGravity(Characters.c2830_0000)
    EnableGravity(Characters.c2830_0001)
    EnableGravity(Characters.c2830_0002)
    EnableGravity(Characters.c2830_0003)
    EnableGravity(Characters.c2830_0004)
    EnableGravity(Characters.c2830_0005)
    EnableGravity(Characters.c2830_0006)
    EnableGravity(Characters.c2830_0007)
    EnableGravity(Characters.c2830_0008)
    EnableGravity(Characters.c2830_0009)
    EnableGravity(Characters.c2830_0010)
    EnableGravity(Characters.c2830_0011)
    EnableGravity(Characters.c2830_0012)
    EnableGravity(Characters.c2830_0013)
    EnableAnimations(Characters.c2830_0000)
    EnableAnimations(Characters.c2830_0001)
    EnableAnimations(Characters.c2830_0002)
    EnableAnimations(Characters.c2830_0003)
    EnableAnimations(Characters.c2830_0004)
    EnableAnimations(Characters.c2830_0005)
    EnableAnimations(Characters.c2830_0006)
    EnableAnimations(Characters.c2830_0007)
    EnableAnimations(Characters.c2830_0008)
    EnableAnimations(Characters.c2830_0009)
    EnableAnimations(Characters.c2830_0010)
    EnableAnimations(Characters.c2830_0011)
    EnableAnimations(Characters.c2830_0012)
    EnableAnimations(Characters.c2830_0013)
    EnableCharacterCollision(Characters.c2830_0000)
    EnableCharacterCollision(Characters.c2830_0001)
    EnableCharacterCollision(Characters.c2830_0002)
    EnableCharacterCollision(Characters.c2830_0003)
    EnableCharacterCollision(Characters.c2830_0004)
    EnableCharacterCollision(Characters.c2830_0005)
    EnableCharacterCollision(Characters.c2830_0006)
    EnableCharacterCollision(Characters.c2830_0007)
    EnableCharacterCollision(Characters.c2830_0008)
    EnableCharacterCollision(Characters.c2830_0009)
    EnableCharacterCollision(Characters.c2830_0010)
    EnableCharacterCollision(Characters.c2830_0011)
    EnableCharacterCollision(Characters.c2830_0012)
    EnableCharacterCollision(Characters.c2830_0013)


@RestartOnRest
def Event11100200():
    """ 11100200: Event 11100200 """
    RunEvent(11105190, slot=0, args=(Characters.c2310_0000, 3010, 3011, 11105230, 11105232))
    RunEvent(11105190, slot=1, args=(Characters.c2310_0001, 3012, 3013, 11105234, 11105236))
    RunEvent(11105195, slot=0, args=(Characters.c2310_0002, 11105240))
    RunEvent(11105195, slot=1, args=(Characters.c2310_0003, 11105244))
    RunEvent(11105200, slot=0, args=(11105190, 11105210, 0, 11105250, 11105230, 11105231, 11105232, 11105233))
    RunEvent(11105200, slot=1, args=(11105191, 11105211, 1, 11105260, 11105234, 11105235, 11105236, 11105237))
    RunEvent(11105200, slot=2, args=(11105195, 11105212, 2, 11105270, 11105238, 11105239, 11105240, 11105241))
    RunEvent(11105200, slot=3, args=(11105196, 11105213, 3, 11105280, 11105242, 11105243, 11105244, 11105245))
    RunEvent(11105220, slot=0, args=(Characters.c2310_0000, 11105210, 10.0, 11105250), arg_types="iifi")
    RunEvent(11105220, slot=1, args=(Characters.c2310_0001, 11105211, 10.0, 11105260), arg_types="iifi")
    RunEvent(11105220, slot=2, args=(Characters.c2310_0002, 11105212, 10.0, 11105270), arg_types="iifi")
    RunEvent(11105220, slot=3, args=(Characters.c2310_0003, 11105213, 10.0, 11105280), arg_types="iifi")
    RunEvent(
        11105250,
        slot=0,
        args=(11105210, Characters.c2310_0000, 1, Navigation.CrowDemonActivityPointB, 11105230, 11105233, 11105232),
    )
    RunEvent(
        11105250,
        slot=1,
        args=(11105210, Characters.c2310_0000, 2, Boxes.CrosDemonActivityPointA, 11105230, 11105233, 11105230),
    )
    RunEvent(
        11105250,
        slot=2,
        args=(11105210, Characters.c2310_0000, 3, Boxes.CrosDemonActivityPointA2, 11105230, 11105233, 11105231),
    )
    RunEvent(
        11105250,
        slot=3,
        args=(11105210, Characters.c2310_0000, 4, Boxes.CrosDemonActivityPointA, 11105230, 11105233, 11105230),
    )
    RunEvent(
        11105250,
        slot=4,
        args=(11105210, Characters.c2310_0000, 5, Boxes.CrosDemonActivityPointB2, 11105230, 11105233, 11105233),
    )
    RunEvent(
        11105250,
        slot=5,
        args=(11105210, Characters.c2310_0000, 6, Navigation.CrowDemonActivityPointB, 11105230, 11105233, 11105232),
    )
    RunEvent(
        11105260,
        slot=0,
        args=(11105211, Characters.c2310_0001, 1, Navigation.CrowDemonActivityPointB, 11105234, 11105237, 11105236),
    )
    RunEvent(
        11105260,
        slot=1,
        args=(11105211, Characters.c2310_0001, 2, Boxes.CrosDemonActivityPointA, 11105234, 11105237, 11105234),
    )
    RunEvent(
        11105260,
        slot=2,
        args=(11105211, Characters.c2310_0001, 3, Boxes.CrosDemonActivityPointA2, 11105234, 11105237, 11105235),
    )
    RunEvent(
        11105260,
        slot=3,
        args=(11105211, Characters.c2310_0001, 4, Boxes.CrosDemonActivityPointA, 11105234, 11105237, 11105234),
    )
    RunEvent(
        11105260,
        slot=4,
        args=(11105211, Characters.c2310_0001, 5, Boxes.CrosDemonActivityPointB2, 11105234, 11105237, 11105237),
    )
    RunEvent(
        11105260,
        slot=5,
        args=(11105211, Characters.c2310_0001, 6, Navigation.CrowDemonActivityPointB, 11105234, 11105237, 11105236),
    )
    RunEvent(
        11105270,
        slot=0,
        args=(11105212, Characters.c2310_0002, 1, Navigation.CrowDemonActivityPointB, 11105238, 11105241, 11105240),
    )
    RunEvent(
        11105270,
        slot=1,
        args=(11105212, Characters.c2310_0002, 2, Boxes.CrosDemonActivityPointA, 11105238, 11105241, 11105238),
    )
    RunEvent(
        11105270,
        slot=2,
        args=(11105212, Characters.c2310_0002, 3, Boxes.CrosDemonActivityPointA2, 11105238, 11105241, 11105239),
    )
    RunEvent(
        11105270,
        slot=3,
        args=(11105212, Characters.c2310_0002, 4, Boxes.CrosDemonActivityPointA, 11105238, 11105241, 11105238),
    )
    RunEvent(
        11105270,
        slot=4,
        args=(11105212, Characters.c2310_0002, 5, Boxes.CrosDemonActivityPointB2, 11105238, 11105241, 11105241),
    )
    RunEvent(
        11105270,
        slot=5,
        args=(11105212, Characters.c2310_0002, 6, Navigation.CrowDemonActivityPointB, 11105238, 11105241, 11105240),
    )
    RunEvent(
        11105280,
        slot=0,
        args=(11105213, Characters.c2310_0003, 1, Navigation.CrowDemonActivityPointB, 11105242, 11105245, 11105244),
    )
    RunEvent(
        11105280,
        slot=1,
        args=(11105213, Characters.c2310_0003, 2, Boxes.CrosDemonActivityPointA, 11105242, 11105245, 11105242),
    )
    RunEvent(
        11105280,
        slot=2,
        args=(11105213, Characters.c2310_0003, 3, Boxes.CrosDemonActivityPointA2, 11105242, 11105245, 11105243),
    )
    RunEvent(
        11105280,
        slot=3,
        args=(11105213, Characters.c2310_0003, 4, Boxes.CrosDemonActivityPointA, 11105242, 11105245, 11105242),
    )
    RunEvent(
        11105280,
        slot=4,
        args=(11105213, Characters.c2310_0003, 5, Boxes.CrosDemonActivityPointB2, 11105242, 11105245, 11105245),
    )
    RunEvent(
        11105280,
        slot=5,
        args=(11105213, Characters.c2310_0003, 6, Navigation.CrowDemonActivityPointB, 11105242, 11105245, 11105244),
    )


@UnknownRestart
def Event11105190(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int):
    """ 11105190: Event 11105190 """
    SkipLinesIfThisEventSlotOff(2)
    ResetStandbyAnimationSettings(arg_0_3)
    End()
    DisableCharacterCollision(arg_0_3)
    DisableGravity(arg_0_3)
    AddSpecialEffect(arg_0_3, 4160)
    SkipLinesIfClient(1)
    IfFlagOn(1, 51100260)
    IfHost(1)
    IfCharacterInsideRegion(1, PLAYER, region=Boxes.CrowDemonTreasureAmbushTrigger)
    IfCharacterInsideRegion(2, PLAYER, region=Boxes.CrowDemonActivityPointB)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EnableCharacterCollision(arg_0_3)
    EnableGravity(arg_0_3)
    ResetStandbyAnimationSettings(arg_0_3)
    SkipLinesIfFinishedConditionFalse(5, 1)
    ForceAnimation(arg_0_3, arg_4_7, wait_for_completion=True)
    CancelSpecialEffect(arg_0_3, 4160)
    SetNest(arg_0_3, Boxes.CrosDemonActivityPointA)
    EnableFlag(arg_12_15)
    Restart()
    ForceAnimation(arg_0_3, arg_8_11, wait_for_completion=True)
    CancelSpecialEffect(arg_0_3, 4160)
    SetNest(arg_0_3, Boxes.CrowDemonActivityPointB)
    EnableFlag(arg_16_19)
    Restart()


@UnknownRestart
def Event11105195(_, arg_0_3: int, arg_4_7: int):
    """ 11105195: Event 11105195 """
    EndIfThisEventSlotOn()
    EnableFlag(arg_4_7)
    IfHasAIStatus(-1, arg_0_3, ai_status=AIStatusType.Battle)
    IfCharacterInsideRegion(-1, PLAYER, region=Boxes.CrosDemonActivityPointB2)
    IfConditionTrue(0, input_condition=-1)
    ForceAnimation(arg_0_3, 3006)


@UnknownRestart
def Event11105200(
    _,
    arg_0_3: int,
    arg_4_7: int,
    arg_8_11: int,
    arg_12_15: int,
    arg_16_19: int,
    arg_20_23: int,
    arg_24_27: int,
    arg_28_31: int,
):
    """ 11105200: Event 11105200 """
    IfFlagOn(0, arg_0_3)
    IfFlagOff(1, arg_16_19)
    IfCharacterInsideRegion(1, PLAYER, region=Boxes.CrosDemonActivityPointA)
    IfFlagOff(2, arg_20_23)
    IfCharacterInsideRegion(2, PLAYER, region=Boxes.CrosDemonActivityPointA2)
    IfFlagOff(3, arg_24_27)
    IfCharacterInsideRegion(3, PLAYER, region=Boxes.CrowDemonActivityPointB)
    IfFlagOff(4, arg_28_31)
    IfCharacterInsideRegion(4, PLAYER, region=Boxes.CrosDemonActivityPointB2)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(-1, input_condition=4)
    IfConditionTrue(0, input_condition=-1)
    EnableFlag(arg_4_7)
    RestartEvent(11105220, slot=arg_8_11)
    SkipLinesIfFinishedConditionFalse(6, 1)
    SkipLinesIfFlagOff(1, arg_20_23)
    RestartEvent(arg_12_15, slot=3)
    SkipLinesIfFlagOff(1, arg_24_27)
    RestartEvent(arg_12_15, slot=1)
    SkipLinesIfFlagOff(1, arg_28_31)
    RestartEvent(arg_12_15, slot=5)
    SkipLinesIfFinishedConditionFalse(6, 2)
    SkipLinesIfFlagOff(1, arg_16_19)
    RestartEvent(arg_12_15, slot=2)
    SkipLinesIfFlagOff(1, arg_24_27)
    RestartEvent(arg_12_15, slot=1)
    SkipLinesIfFlagOff(1, arg_28_31)
    RestartEvent(arg_12_15, slot=5)
    SkipLinesIfFinishedConditionFalse(6, 3)
    SkipLinesIfFlagOff(1, arg_16_19)
    RestartEvent(arg_12_15)
    SkipLinesIfFlagOff(1, arg_20_23)
    RestartEvent(arg_12_15, slot=3)
    SkipLinesIfFlagOff(1, arg_28_31)
    RestartEvent(arg_12_15, slot=5)
    SkipLinesIfFinishedConditionFalse(6, 4)
    SkipLinesIfFlagOff(1, arg_16_19)
    RestartEvent(arg_12_15)
    SkipLinesIfFlagOff(1, arg_20_23)
    RestartEvent(arg_12_15, slot=3)
    SkipLinesIfFlagOff(1, arg_24_27)
    RestartEvent(arg_12_15, slot=4)
    IfFlagOff(0, arg_4_7)
    Restart()


@UnknownRestart
def Event11105220(_, arg_0_3: int, arg_4_7: int, arg_8_11: float, arg_12_15: int):
    """ 11105220: Event 11105220 """
    DisableNetworkSync()
    IfFlagOn(0, arg_4_7)
    Wait(arg_8_11)
    RestartIfFlagOff(arg_4_7)
    DisableFlag(arg_4_7)
    RestartEvent(arg_12_15)
    RestartEvent(arg_12_15, slot=1)
    RestartEvent(arg_12_15, slot=2)
    RestartEvent(arg_12_15, slot=3)
    RestartEvent(arg_12_15, slot=4)
    RestartEvent(arg_12_15, slot=5)
    AICommand(arg_0_3, command_id=-1, slot=0)
    ReplanAI(arg_0_3)
    Restart()


@UnknownRestart
def Event11105250(
    _,
    arg_0_3: int,
    arg_4_7: int,
    arg_8_11: int,
    arg_12_15: int,
    arg_16_19: int,
    arg_20_23: int,
    arg_24_27: int,
):
    """ 11105250: Event 11105250 """
    SkipLinesIfFlagOn(2, arg_0_3)
    IfCharacterDead(0, arg_4_7)
    End()
    AICommand(arg_4_7, command_id=arg_8_11, slot=0)
    ReplanAI(arg_4_7)
    IfCharacterInsideRegion(0, arg_4_7, region=arg_12_15)
    SetNest(arg_4_7, arg_12_15)
    DisableFlagRange((arg_16_19, arg_20_23))
    EnableFlag(arg_24_27)
    DisableFlag(arg_0_3)
    AICommand(arg_4_7, command_id=-1, slot=0)
    ReplanAI(arg_4_7)
    Restart()


@UnknownRestart
def Event11105260(
    _,
    arg_0_3: int,
    arg_4_7: int,
    arg_8_11: int,
    arg_12_15: int,
    arg_16_19: int,
    arg_20_23: int,
    arg_24_27: int,
):
    """ 11105260: Event 11105260 """
    SkipLinesIfFlagOn(2, arg_0_3)
    IfCharacterDead(0, arg_4_7)
    End()
    AICommand(arg_4_7, command_id=arg_8_11, slot=0)
    ReplanAI(arg_4_7)
    IfCharacterInsideRegion(0, arg_4_7, region=arg_12_15)
    SetNest(arg_4_7, arg_12_15)
    DisableFlagRange((arg_16_19, arg_20_23))
    EnableFlag(arg_24_27)
    DisableFlag(arg_0_3)
    AICommand(arg_4_7, command_id=-1, slot=0)
    ReplanAI(arg_4_7)
    Restart()


@UnknownRestart
def Event11105270(
    _,
    arg_0_3: int,
    arg_4_7: int,
    arg_8_11: int,
    arg_12_15: int,
    arg_16_19: int,
    arg_20_23: int,
    arg_24_27: int,
):
    """ 11105270: Event 11105270 """
    SkipLinesIfFlagOn(2, arg_0_3)
    IfCharacterDead(0, arg_4_7)
    End()
    AICommand(arg_4_7, command_id=arg_8_11, slot=0)
    ReplanAI(arg_4_7)
    IfCharacterInsideRegion(0, arg_4_7, region=arg_12_15)
    SetNest(arg_4_7, arg_12_15)
    DisableFlagRange((arg_16_19, arg_20_23))
    EnableFlag(arg_24_27)
    DisableFlag(arg_0_3)
    AICommand(arg_4_7, command_id=-1, slot=0)
    ReplanAI(arg_4_7)
    Restart()


@UnknownRestart
def Event11105280(
    _,
    arg_0_3: int,
    arg_4_7: int,
    arg_8_11: int,
    arg_12_15: int,
    arg_16_19: int,
    arg_20_23: int,
    arg_24_27: int,
):
    """ 11105280: Event 11105280 """
    SkipLinesIfFlagOn(2, arg_0_3)
    IfCharacterDead(0, arg_4_7)
    End()
    AICommand(arg_4_7, command_id=arg_8_11, slot=0)
    ReplanAI(arg_4_7)
    IfCharacterInsideRegion(0, arg_4_7, region=arg_12_15)
    SetNest(arg_4_7, arg_12_15)
    DisableFlagRange((arg_16_19, arg_20_23))
    EnableFlag(arg_24_27)
    DisableFlag(arg_0_3)
    AICommand(arg_4_7, command_id=-1, slot=0)
    ReplanAI(arg_4_7)
    Restart()


def Event11100600(_, arg_0_3: int, arg_4_7: int):
    """ 11100600: Event 11100600 """
    SkipLinesIfThisEventSlotOff(4)
    EndOfAnimation(arg_0_3, 0)
    DisableObjectActivation(arg_0_3, obj_act_id=-1)
    EnableTreasure(arg_0_3)
    End()
    DisableTreasure(arg_0_3)
    IfObjectActivated(0, obj_act_id=arg_4_7)
    WaitFrames(10)
    EnableTreasure(arg_0_3)


def Event11100510(_, arg_0_3: int, arg_4_7: int):
    """ 11100510: Event 11100510 """
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


def Event11100520(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11100520: Event 11100520 """
    SkipLinesIfThisEventSlotOff(2)
    DropMandatoryTreasure(arg_0_3)
    End()
    IfHealthLessThanOrEqual(0, arg_0_3, 0.0)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)


def Event11100530(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11100530: Event 11100530 """
    IfFlagOn(1, 1690)
    IfAttacked(1, arg_0_3, attacker=PLAYER)
    IfHealthGreaterThan(1, arg_0_3, 0.0)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)


def Event11100531(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11100531: Event 11100531 """
    SkipLinesIfThisEventSlotOff(2)
    DisableCharacter(arg_0_3)
    End()
    IfHealthLessThanOrEqual(0, arg_0_3, 0.0)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)


def Event11100040():
    """ 11100040: Event 11100040 """
    DisableNetworkSync()
    Wait(1.0)
    EndIfFlagOn(11100700)
    RegisterLadder(start_climbing_flag=11100012, stop_climbing_flag=11100013, obj=Objects.o1511_0000)


def Event11100532(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int, arg_20_23: int):
    """ 11100532: Event 11100532 """
    DisableMapPiece(1103100)
    DisableCollision(Collisions.h0148B0_0000)
    DisableObject(Objects.o1604_0000)
    DeleteVFX(VFX.MultiplayerFog1, erase_root_only=False)
    IfFlagOn(0, 11100700)
    DisableFlagRange((arg_4_7, arg_8_11))
    SkipLinesIfFlagOff(2, 8111)
    EnableFlag(arg_12_15)
    SkipLines(1)
    EnableFlag(arg_16_19)
    EnableMapPiece(1103100)
    EnableCollision(Collisions.h0148B0_0000)
    DisableObject(Objects.o1511_0000)
    EnableObject(Objects.o1604_0000)
    CreateVFX(VFX.MultiplayerFog1)
    EnableCharacter(arg_0_3)
    EnableCharacter(arg_20_23)
    SetTeamType(arg_20_23, TeamType.WhitePhantom)
    DisableCharacter(Characters.c2830_0000)
    DisableCharacter(Characters.c2830_0001)
    DisableCharacter(Characters.c2830_0002)
    DisableCharacter(Characters.c2830_0003)
    DisableCharacter(Characters.c2830_0004)
    DisableCharacter(Characters.c2830_0005)
    DisableCharacter(Characters.c2830_0006)
    DisableCharacter(Characters.c2830_0007)
    DisableCharacter(Characters.c2830_0008)
    DisableCharacter(Characters.c2830_0009)
    DisableCharacter(Characters.c2830_0010)
    DisableCharacter(Characters.c2830_0011)
    DisableCharacter(Characters.c2830_0012)
    DisableCharacter(Characters.c2830_0013)
    DisableCharacter(Characters.c2500_0022)
    DisableCharacter(Characters.c2500_0023)
    DisableCharacter(Characters.c2500_0024)
    DisableCharacter(Characters.c2500_0025)
    DisableCharacter(Characters.c2500_0026)


def Event11100533(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11100533: Event 11100533 """
    IfFlagOn(1, 1606)
    IfHealthLessThanOrEqual(0, arg_0_3, 0.0)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)
    EnableFlag(8110)


def Event11100534(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11100534: Event 11100534 """
    IfFlagOn(1, 1607)
    IfHealthLessThanOrEqual(0, arg_0_3, 0.0)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)
    EnableFlag(8110)


def Event11100535(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int):
    """ 11100535: Event 11100535 """
    EndIfThisEventOn()
    IfFlagOff(1, 11100700)
    IfFlagOn(1, 8110)
    IfConditionTrue(0, input_condition=1)
    RemoveGoodFromPlayer(116)
    EnableFlag(11100300)
    DisableCharacter(arg_0_3)
    DisableFlagRange((arg_4_7, arg_8_11))
    SkipLinesIfFlagOff(2, 8111)
    EnableFlag(arg_12_15)
    SkipLines(1)
    EnableFlag(arg_16_19)
    DisableFlagRange((1760, 1769))
    EnableFlag(1764)


def Event11100300():
    """ 11100300: Event 11100300 """
    EndIfThisEventOn()
    IfThisEventOn(0)
    SkipLinesIfFlagOff(1, 11400400)
    AwardItemLot(2800, host_only=False)
    SkipLinesIfFlagOff(1, 11400401)
    AwardItemLot(2810, host_only=False)
    SkipLinesIfFlagOff(1, 11400402)
    AwardItemLot(2820, host_only=False)


def Event11105030():
    """ 11105030: Event 11105030 """
    DisableNetworkSync()
    EndIfClient()
    EndIfFlagOn(11105031)
    EndIfFlagOn(4)
    IfHost(1)
    IfCharacterHuman(1, PLAYER)
    IfFlagOff(1, 11100810)
    SkipLinesIfThisEventOn(1)
    IfCharacterInsideRegion(1, PLAYER, region=Spheres.JeremiahInvaderTrigger)
    IfConditionTrue(0, input_condition=1)
    PlaceSummonSign(
        SummonSignType.BlackEyeSign,
        Characters.c0000_0005,
        region=Points.JeremiahInvaderSpawn,
        summon_flag=11105031,
        dismissal_flag=11105032,
    )
    Wait(20.0)
    Restart()


def Event11100810():
    """ 11100810: Event 11100810 """
    SkipLinesIfHost(3)
    IfFlagOn(1, 11105031)
    IfFlagOff(1, 11105032)
    SkipLinesIfConditionTrue(1, 1)
    DisableCharacter(Characters.c0000_0005)
    EndIfThisEventOn()
    IfCharacterDead(0, Characters.c0000_0005)
    EnableFlag(11100810)


def Event11105843(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11105843: Event 11105843 """
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


def Event11105846(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 11105846: Event 11105846 """
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
