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


@RestartOnRest
def PatchesAmbush():
    """ 11102000: Patches teleports behind the player and attacks. """
    DisableCharacter(Characters.c0000_PatchesAmbush)

    Await(InsideMap(PAINTED_WORLD) and TriggerFlags.PatchesAmbush and IsAlive(Characters.c0000_PatchesAmbush))
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
    """ 11102001: Channeler teleports above the player (no gravity) and uses its buff dance. """
    DisableCharacter(Characters.c2370_TrollChanneler)

    Await(InsideMap(PAINTED_WORLD) and TriggerFlags.ChannelerAmbush and IsAlive(Characters.c2370_TrollChanneler))
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

    AddSpecialEffect(6312, 5470)
    AddSpecialEffect(6422, 5470)
    AddSpecialEffect(6570, 5470)
    AddSpecialEffect(1100960, 5470)
    AddSpecialEffect(1100214, 5470)
    AddSpecialEffect(1100215, 5470)
    AddSpecialEffect(1100216, 5470)
    AddSpecialEffect(1100217, 5470)
    AddSpecialEffect(1100218, 5470)
    AddSpecialEffect(1100219, 5470)
    AddSpecialEffect(1100220, 5470)
    AddSpecialEffect(1100221, 5470)
    AddSpecialEffect(1100222, 5470)
    AddSpecialEffect(1100223, 5470)
    AddSpecialEffect(1100224, 5470)
    AddSpecialEffect(1100300, 5470)
    AddSpecialEffect(1100301, 5470)
    AddSpecialEffect(1100302, 5470)
    AddSpecialEffect(1100303, 5470)
    AddSpecialEffect(1100225, 5470)
    AddSpecialEffect(1100226, 5470)
    AddSpecialEffect(1100227, 5470)
    AddSpecialEffect(1100228, 5470)
    AddSpecialEffect(1100229, 5470)
    AddSpecialEffect(1100230, 5470)
    AddSpecialEffect(1100231, 5470)
    AddSpecialEffect(1100232, 5470)
    AddSpecialEffect(1100233, 5470)
    AddSpecialEffect(1100234, 5470)
    AddSpecialEffect(1100235, 5470)
    AddSpecialEffect(1100236, 5470)
    AddSpecialEffect(1100237, 5470)
    AddSpecialEffect(1100238, 5470)
    AddSpecialEffect(1100100, 5470)
    AddSpecialEffect(1100101, 5470)
    AddSpecialEffect(1100102, 5470)
    AddSpecialEffect(1100104, 5470)
    AddSpecialEffect(1100105, 5470)
    AddSpecialEffect(1100130, 5470)
    AddSpecialEffect(1100132, 5470)
    AddSpecialEffect(1100135, 5470)
    AddSpecialEffect(1100136, 5470)
    AddSpecialEffect(1100137, 5470)
    AddSpecialEffect(1100138, 5470)
    AddSpecialEffect(1100400, 5470)
    AddSpecialEffect(1100401, 5470)
    AddSpecialEffect(1100402, 5470)
    AddSpecialEffect(1100403, 5470)
    AddSpecialEffect(1100404, 5470)
    AddSpecialEffect(1100239, 5470)
    AddSpecialEffect(1100240, 5470)
    AddSpecialEffect(1100241, 5470)
    AddSpecialEffect(1100242, 5470)
    AddSpecialEffect(1100243, 5470)
    AddSpecialEffect(1100244, 5470)
    AddSpecialEffect(1100180, 5470)
    AddSpecialEffect(1100160, 5470)
    AddSpecialEffect(1100161, 5470)
    AddSpecialEffect(1100200, 5470)
    AddSpecialEffect(1100201, 5470)
    AddSpecialEffect(1100202, 5470)
    AddSpecialEffect(1100203, 5470)
    AddSpecialEffect(1100204, 5470)
    AddSpecialEffect(1100205, 5470)
    AddSpecialEffect(1100206, 5470)
    AddSpecialEffect(1100207, 5470)
    AddSpecialEffect(1100208, 5470)
    AddSpecialEffect(1100209, 5470)
    AddSpecialEffect(1100210, 5470)
    AddSpecialEffect(1100211, 5470)
    AddSpecialEffect(1100212, 5470)
    AddSpecialEffect(1100213, 5470)
    AddSpecialEffect(1100245, 5470)
    AddSpecialEffect(1100246, 5470)
    AddSpecialEffect(1100247, 5470)
    AddSpecialEffect(1100248, 5470)
    AddSpecialEffect(1100249, 5470)
    AddSpecialEffect(1100250, 5470)
    AddSpecialEffect(1100251, 5470)
    AddSpecialEffect(1100252, 5470)
    AddSpecialEffect(1100253, 5470)
    AddSpecialEffect(1100254, 5470)
    AddSpecialEffect(1100255, 5470)
    AddSpecialEffect(1100900, 5470)
    AddSpecialEffect(1100901, 5470)
    AddSpecialEffect(1100902, 5470)
    AddSpecialEffect(1100903, 5470)
    AddSpecialEffect(1100904, 5470)
    AddSpecialEffect(1100905, 5470)
    AddSpecialEffect(1100906, 5470)
    AddSpecialEffect(1100256, 5470)
    AddSpecialEffect(1100257, 5470)
    AddSpecialEffect(1100258, 5470)
    AddSpecialEffect(1100259, 5470)
    AddSpecialEffect(1100260, 5470)
    AddSpecialEffect(1100261, 5470)
    AddSpecialEffect(1100262, 5470)
    AddSpecialEffect(1100263, 5470)
    AddSpecialEffect(1100264, 5470)
    AddSpecialEffect(1100907, 5470)
    AddSpecialEffect(1100908, 5470)
    AddSpecialEffect(1100909, 5470)
    AddSpecialEffect(1100910, 5470)
    AddSpecialEffect(1100911, 5470)
    AddSpecialEffect(1100170, 5470)
    AddSpecialEffect(1100171, 5470)
    AddSpecialEffect(1100172, 5470)
    AddSpecialEffect(1103900, 5470)
    AddSpecialEffect(1103910, 5470)
    AddSpecialEffect(1103902, 5470)
    AddSpecialEffect(1103901, 5470)
    AddSpecialEffect(1103911, 5470)
    AddSpecialEffect(1103912, 5470)

    return RESTART


@RestartOnRest
def RedPhantomAmbush():
    """ 11102002: Random red phantom ambushes the player. """
    DisableCharacter(Characters.c2840_0011)
    DisableCharacter(Characters.c2840_0012)
    DisableCharacter(Characters.c2840_0013)
    DisableCharacter(Characters.c2840_0014)
    DisableCharacter(Characters.c2840_0015)
    DisableCharacter(Characters.c2840_0016)
    DisableCharacter(Characters.c2840_0017)
    DisableCharacter(Characters.c2930_0009)
    DisableCharacter(Characters.c2930_0010)
    DisableCharacter(Characters.c2930_0011)
    DisableCharacter(Characters.c2930_0012)
    DisableCharacter(Characters.c2930_0013)

    Await(InsideMap(PAINTED_WORLD) and TriggerFlags.EnemyAmbush)
    DisableFlag(TriggerFlags.EnemyAmbush)

    DisableFlagRange((11812900, 11812999))
    EnableRandomFlagInRange((11812900, 11812911))

    if FlagEnabled(11812900):
        ControlRedPhantom(0, Characters.c2840_0011)
    elif FlagEnabled(11812901):
        ControlRedPhantom(0, Characters.c2840_0012)
    elif FlagEnabled(11812902):
        ControlRedPhantom(0, Characters.c2840_0013)
    elif FlagEnabled(11812903):
        ControlRedPhantom(0, Characters.c2840_0014)
    elif FlagEnabled(11812904):
        ControlRedPhantom(0, Characters.c2840_0015)
    elif FlagEnabled(11812905):
        ControlRedPhantom(0, Characters.c2840_0016)
    elif FlagEnabled(11812906):
        ControlRedPhantom(0, Characters.c2840_0017)
    elif FlagEnabled(11812907):
        ControlRedPhantom(0, Characters.c2930_0009)
    elif FlagEnabled(11812908):
        ControlRedPhantom(0, Characters.c2930_0010)
    elif FlagEnabled(11812909):
        ControlRedPhantom(0, Characters.c2930_0011)
    elif FlagEnabled(11812910):
        ControlRedPhantom(0, Characters.c2930_0012)
    elif FlagEnabled(11812911):
        ControlRedPhantom(0, Characters.c2930_0013)
    
    Await(FlagEnabled(11105082))

    return RESTART


@RestartOnRest
def ControlRedPhantom(_, enemy: int):
    """ 11105081: `enemy` moves to player and appears. """
    DisableFlag(11105082)
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
    EnableFlag(11105082)


def MakeWorldInvisible():
    """ 11102003: Disable all map pieces. Undone only by reload. """
    Await(TriggerFlags.InvisibleWorld)   # note you don't need to be standing in the map
    DisableFlag(TriggerFlags.InvisibleWorld)
    for map_piece in range(1108500, 1108561):
        DisableMapPiece(map_piece)
    # No need to restart.


@RestartOnRest
def OopsAllGwyns():
    """ 11102004: Enable Gwyns and warp them to their paired normal characters. """
    DisableCharacter(1100600)
    DisableCharacter(1100601)
    DisableCharacter(1100602)
    DisableCharacter(1100603)
    DisableCharacter(1100604)
    DisableCharacter(1100605)
    DisableCharacter(1100606)
    DisableCharacter(1100607)
    DisableCharacter(1100608)
    DisableCharacter(1100609)
    DisableCharacter(1100610)
    DisableCharacter(1100611)
    DisableCharacter(1100612)
    DisableCharacter(1100613)
    DisableCharacter(1100614)
    DisableCharacter(1100615)
    DisableCharacter(1100616)
    DisableCharacter(1100617)
    DisableCharacter(1100618)
    Await(TriggerFlags.OopsAllGwyns)  # note you don't need to be standing in the map
    DisableCharacter(6312)
    EnableCharacter(1100600)
    DisableCharacter(1100215)
    EnableCharacter(1100601)
    DisableCharacter(1100220)
    EnableCharacter(1100602)
    DisableCharacter(1100300)
    EnableCharacter(1100603)
    DisableCharacter(1100226)
    EnableCharacter(1100604)
    DisableCharacter(1100231)
    EnableCharacter(1100605)
    DisableCharacter(1100236)
    EnableCharacter(1100606)
    DisableCharacter(1100102)
    EnableCharacter(1100607)
    DisableCharacter(1100135)
    EnableCharacter(1100608)
    DisableCharacter(1100401)
    EnableCharacter(1100609)
    DisableCharacter(1100240)
    EnableCharacter(1100610)
    DisableCharacter(1100180)
    EnableCharacter(1100611)
    DisableCharacter(1100202)
    EnableCharacter(1100612)
    DisableCharacter(1100207)
    EnableCharacter(1100613)
    DisableCharacter(1100212)
    EnableCharacter(1100614)
    DisableCharacter(1100248)
    EnableCharacter(1100615)
    DisableCharacter(1100253)
    EnableCharacter(1100616)
    DisableCharacter(1100256)
    EnableCharacter(1100617)
    DisableCharacter(1100261)
    EnableCharacter(1100618)
    WaitFrames(30)  # enough time for other maps to trigger too
    DisableFlag(TriggerFlags.OopsAllGwyns)
    # No need to restart.


@RestartOnRest
def OopsAllBonewheels():
    """ 11102005: Enable Bonewheels and warp them to their paired normal characters. """
    DisableCharacter(1100405)
    DisableCharacter(1100406)
    DisableCharacter(1100407)
    DisableCharacter(1100408)
    DisableCharacter(1100409)
    DisableCharacter(1100410)
    DisableCharacter(1100411)
    DisableCharacter(1100412)
    DisableCharacter(1100413)
    DisableCharacter(1100414)
    DisableCharacter(1100415)
    DisableCharacter(1100416)
    DisableCharacter(1100417)
    DisableCharacter(1100418)
    DisableCharacter(1100419)
    DisableCharacter(1100420)
    DisableCharacter(1100421)
    DisableCharacter(1100422)
    DisableCharacter(1100423)
    DisableCharacter(1100424)
    DisableCharacter(1100425)
    DisableCharacter(1100426)
    DisableCharacter(1100427)
    DisableCharacter(1100428)
    DisableCharacter(1100429)
    DisableCharacter(1100430)
    DisableCharacter(1100431)
    DisableCharacter(1100432)
    DisableCharacter(1100433)
    DisableCharacter(1100434)
    DisableCharacter(1100435)
    DisableCharacter(1100436)
    DisableCharacter(1100437)
    DisableCharacter(1100438)
    DisableCharacter(1100439)
    DisableCharacter(1100440)
    DisableCharacter(1100441)
    DisableCharacter(1100442)
    DisableCharacter(1100443)
    DisableCharacter(1100444)
    DisableCharacter(1100445)
    DisableCharacter(1100446)
    DisableCharacter(1100447)
    DisableCharacter(1100448)
    DisableCharacter(1100449)
    DisableCharacter(1100450)
    DisableCharacter(1100451)
    DisableCharacter(1100452)
    DisableCharacter(1100453)
    DisableCharacter(1100454)
    DisableCharacter(1100455)
    DisableCharacter(1100456)
    DisableCharacter(1100457)
    DisableCharacter(1100458)
    DisableCharacter(1100459)
    DisableCharacter(1100460)
    DisableCharacter(1100461)
    DisableCharacter(1100462)
    DisableCharacter(1100463)
    DisableCharacter(1100464)
    DisableCharacter(1100465)
    DisableCharacter(1100466)
    DisableCharacter(1100467)
    DisableCharacter(1100468)
    DisableCharacter(1100469)
    DisableCharacter(1100470)
    DisableCharacter(1100471)
    DisableCharacter(1100472)
    DisableCharacter(1100473)
    DisableCharacter(1100474)
    DisableCharacter(1100475)
    DisableCharacter(1100476)
    DisableCharacter(1100477)
    DisableCharacter(1100478)
    DisableCharacter(1100479)
    DisableCharacter(1100480)
    DisableCharacter(1100481)
    DisableCharacter(1100482)
    DisableCharacter(1100483)
    DisableCharacter(1100484)
    DisableCharacter(1100485)
    DisableCharacter(1100486)
    DisableCharacter(1100487)
    DisableCharacter(1100488)
    DisableCharacter(1100489)
    DisableCharacter(1100490)
    DisableCharacter(1100491)
    DisableCharacter(1100492)
    DisableCharacter(1100493)
    DisableCharacter(1100494)
    Await(TriggerFlags.OopsAllBonewheels)  # note you don't need to be standing in the map
    DisableCharacter(6312)
    EnableCharacter(1100405)
    DisableCharacter(6422)
    EnableCharacter(1100406)
    DisableCharacter(6570)
    EnableCharacter(1100407)
    DisableCharacter(1100214)
    EnableCharacter(1100408)
    DisableCharacter(1100215)
    EnableCharacter(1100409)
    DisableCharacter(1100216)
    EnableCharacter(1100410)
    DisableCharacter(1100217)
    EnableCharacter(1100411)
    DisableCharacter(1100218)
    EnableCharacter(1100412)
    DisableCharacter(1100219)
    EnableCharacter(1100413)
    DisableCharacter(1100220)
    EnableCharacter(1100414)
    DisableCharacter(1100221)
    EnableCharacter(1100415)
    DisableCharacter(1100222)
    EnableCharacter(1100416)
    DisableCharacter(1100223)
    EnableCharacter(1100417)
    DisableCharacter(1100224)
    EnableCharacter(1100418)
    DisableCharacter(1100300)
    EnableCharacter(1100419)
    DisableCharacter(1100301)
    EnableCharacter(1100420)
    DisableCharacter(1100302)
    EnableCharacter(1100421)
    DisableCharacter(1100303)
    EnableCharacter(1100422)
    DisableCharacter(1100225)
    EnableCharacter(1100423)
    DisableCharacter(1100226)
    EnableCharacter(1100424)
    DisableCharacter(1100227)
    EnableCharacter(1100425)
    DisableCharacter(1100228)
    EnableCharacter(1100426)
    DisableCharacter(1100229)
    EnableCharacter(1100427)
    DisableCharacter(1100230)
    EnableCharacter(1100428)
    DisableCharacter(1100231)
    EnableCharacter(1100429)
    DisableCharacter(1100232)
    EnableCharacter(1100430)
    DisableCharacter(1100233)
    EnableCharacter(1100431)
    DisableCharacter(1100234)
    EnableCharacter(1100432)
    DisableCharacter(1100235)
    EnableCharacter(1100433)
    DisableCharacter(1100236)
    EnableCharacter(1100434)
    DisableCharacter(1100237)
    EnableCharacter(1100435)
    DisableCharacter(1100238)
    EnableCharacter(1100436)
    DisableCharacter(1100100)
    EnableCharacter(1100437)
    DisableCharacter(1100101)
    EnableCharacter(1100438)
    DisableCharacter(1100102)
    EnableCharacter(1100439)
    DisableCharacter(1100104)
    EnableCharacter(1100440)
    DisableCharacter(1100105)
    EnableCharacter(1100441)
    DisableCharacter(1100130)
    EnableCharacter(1100442)
    DisableCharacter(1100132)
    EnableCharacter(1100443)
    DisableCharacter(1100135)
    EnableCharacter(1100444)
    DisableCharacter(1100136)
    EnableCharacter(1100445)
    DisableCharacter(1100137)
    EnableCharacter(1100446)
    DisableCharacter(1100138)
    EnableCharacter(1100447)
    DisableCharacter(1100400)
    EnableCharacter(1100448)
    DisableCharacter(1100401)
    EnableCharacter(1100449)
    DisableCharacter(1100402)
    EnableCharacter(1100450)
    DisableCharacter(1100403)
    EnableCharacter(1100451)
    DisableCharacter(1100404)
    EnableCharacter(1100452)
    DisableCharacter(1100239)
    EnableCharacter(1100453)
    DisableCharacter(1100240)
    EnableCharacter(1100454)
    DisableCharacter(1100241)
    EnableCharacter(1100455)
    DisableCharacter(1100242)
    EnableCharacter(1100456)
    DisableCharacter(1100243)
    EnableCharacter(1100457)
    DisableCharacter(1100244)
    EnableCharacter(1100458)
    DisableCharacter(1100180)
    EnableCharacter(1100459)
    DisableCharacter(1100161)
    EnableCharacter(1100460)
    DisableCharacter(1100200)
    EnableCharacter(1100461)
    DisableCharacter(1100201)
    EnableCharacter(1100462)
    DisableCharacter(1100202)
    EnableCharacter(1100463)
    DisableCharacter(1100203)
    EnableCharacter(1100464)
    DisableCharacter(1100204)
    EnableCharacter(1100465)
    DisableCharacter(1100205)
    EnableCharacter(1100466)
    DisableCharacter(1100206)
    EnableCharacter(1100467)
    DisableCharacter(1100207)
    EnableCharacter(1100468)
    DisableCharacter(1100208)
    EnableCharacter(1100469)
    DisableCharacter(1100209)
    EnableCharacter(1100470)
    DisableCharacter(1100210)
    EnableCharacter(1100471)
    DisableCharacter(1100211)
    EnableCharacter(1100472)
    DisableCharacter(1100212)
    EnableCharacter(1100473)
    DisableCharacter(1100213)
    EnableCharacter(1100474)
    DisableCharacter(1100245)
    EnableCharacter(1100475)
    DisableCharacter(1100246)
    EnableCharacter(1100476)
    DisableCharacter(1100247)
    EnableCharacter(1100477)
    DisableCharacter(1100248)
    EnableCharacter(1100478)
    DisableCharacter(1100249)
    EnableCharacter(1100479)
    DisableCharacter(1100250)
    EnableCharacter(1100480)
    DisableCharacter(1100251)
    EnableCharacter(1100481)
    DisableCharacter(1100252)
    EnableCharacter(1100482)
    DisableCharacter(1100253)
    EnableCharacter(1100483)
    DisableCharacter(1100254)
    EnableCharacter(1100484)
    DisableCharacter(1100255)
    EnableCharacter(1100485)
    DisableCharacter(1100256)
    EnableCharacter(1100486)
    DisableCharacter(1100257)
    EnableCharacter(1100487)
    DisableCharacter(1100258)
    EnableCharacter(1100488)
    DisableCharacter(1100259)
    EnableCharacter(1100489)
    DisableCharacter(1100260)
    EnableCharacter(1100490)
    DisableCharacter(1100261)
    EnableCharacter(1100491)
    DisableCharacter(1100262)
    EnableCharacter(1100492)
    DisableCharacter(1100263)
    EnableCharacter(1100493)
    DisableCharacter(1100264)
    EnableCharacter(1100494)
    WaitFrames(30)  # enough time for other maps to trigger too
    DisableFlag(TriggerFlags.OopsAllBonewheels)
    # No need to restart.


@RestartOnRest
def HyperAggression():
    """ 11102006: Switch AI param of every enemy to its aggressive version. """
    Await(TriggerFlags.HyperAggression or TriggerFlags.HyperAggressionReTrigger)
    
    SetAIParamID(1100214, 120350)
    SetAIParamID(1100215, 120350)
    SetAIParamID(1100216, 120350)
    SetAIParamID(1100217, 120350)
    SetAIParamID(1100218, 120350)
    SetAIParamID(1100219, 120350)
    SetAIParamID(1100220, 120350)
    SetAIParamID(1100221, 120350)
    SetAIParamID(1100222, 120350)
    SetAIParamID(1100223, 120350)
    SetAIParamID(1100224, 120350)
    SetAIParamID(1100300, 231050)
    SetAIParamID(1100301, 231050)
    SetAIParamID(1100302, 231050)
    SetAIParamID(1100303, 231050)
    SetAIParamID(1100225, 231050)
    SetAIParamID(1100226, 231050)
    SetAIParamID(1100227, 231050)
    SetAIParamID(1100228, 250050)
    SetAIParamID(1100229, 250050)
    SetAIParamID(1100230, 250050)
    SetAIParamID(1100231, 250070)
    SetAIParamID(1100232, 250050)
    SetAIParamID(1100233, 250050)
    SetAIParamID(1100234, 250070)
    SetAIParamID(1100235, 250052)
    SetAIParamID(1100236, 250052)
    SetAIParamID(1100237, 250052)
    SetAIParamID(1100238, 250052)
    SetAIParamID(1100100, 250050)
    SetAIParamID(1100101, 250050)
    SetAIParamID(1100102, 250050)
    SetAIParamID(1100104, 250050)
    SetAIParamID(1100105, 250050)
    SetAIParamID(1100130, 250050)
    SetAIParamID(1100132, 250050)
    SetAIParamID(1100135, 250050)
    SetAIParamID(1100136, 250050)
    SetAIParamID(1100137, 250050)
    SetAIParamID(1100138, 250050)
    SetAIParamID(1100400, 250060)
    SetAIParamID(1100401, 250060)
    SetAIParamID(1100402, 250050)
    SetAIParamID(1100403, 250050)
    SetAIParamID(1100404, 250060)
    SetAIParamID(1100239, 250060)
    SetAIParamID(1100240, 250052)
    SetAIParamID(1100241, 250052)
    SetAIParamID(1100242, 250070)
    SetAIParamID(1100243, 250070)
    SetAIParamID(1100244, 250070)
    SetAIParamID(1100180, 257050)
    SetAIParamID(1100160, 273050)
    SetAIParamID(1100200, 283060)
    SetAIParamID(1100201, 283060)
    SetAIParamID(1100202, 283060)
    SetAIParamID(1100203, 283060)
    SetAIParamID(1100204, 283060)
    SetAIParamID(1100205, 283060)
    SetAIParamID(1100206, 283060)
    SetAIParamID(1100207, 283060)
    SetAIParamID(1100208, 283060)
    SetAIParamID(1100209, 283060)
    SetAIParamID(1100210, 283060)
    SetAIParamID(1100211, 283060)
    SetAIParamID(1100212, 283060)
    SetAIParamID(1100213, 283060)
    SetAIParamID(1100245, 284050)
    SetAIParamID(1100246, 284051)
    SetAIParamID(1100247, 284050)
    SetAIParamID(1100248, 284050)
    SetAIParamID(1100249, 284050)
    SetAIParamID(1100250, 284051)
    SetAIParamID(1100251, 284051)
    SetAIParamID(1100252, 284051)
    SetAIParamID(1100253, 284051)
    SetAIParamID(1100254, 284050)
    SetAIParamID(1100255, 284050)
    SetAIParamID(1100900, 284050)
    SetAIParamID(1100901, 284051)
    SetAIParamID(1100902, 284050)
    SetAIParamID(1100903, 284051)
    SetAIParamID(1100904, 284050)
    SetAIParamID(1100905, 284050)
    SetAIParamID(1100906, 284051)
    SetAIParamID(1100256, 293060)
    SetAIParamID(1100257, 293060)
    SetAIParamID(1100258, 293060)
    SetAIParamID(1100259, 293060)
    SetAIParamID(1100260, 293060)
    SetAIParamID(1100261, 293060)
    SetAIParamID(1100262, 293060)
    SetAIParamID(1100263, 293060)
    SetAIParamID(1100264, 293060)
    SetAIParamID(1100907, 293060)
    SetAIParamID(1100908, 293060)
    SetAIParamID(1100909, 293060)
    SetAIParamID(1100910, 293060)
    SetAIParamID(1100911, 293060)
    SetAIParamID(1100170, 342050)
    SetAIParamID(1103900, 349050)
    SetAIParamID(1103910, 349050)
    SetAIParamID(1103902, 349150)
    SetAIParamID(1103901, 349150)
    SetAIParamID(1103911, 349150)
    SetAIParamID(1103912, 349150)
    SetAIParamID(1100600, 537050)
    SetAIParamID(1100601, 537050)
    SetAIParamID(1100602, 537050)
    SetAIParamID(1100603, 537050)
    SetAIParamID(1100604, 537050)
    SetAIParamID(1100605, 537050)
    SetAIParamID(1100606, 537050)
    SetAIParamID(1100607, 537050)
    SetAIParamID(1100608, 537050)
    SetAIParamID(1100609, 537050)
    SetAIParamID(1100610, 537050)
    SetAIParamID(1100611, 537050)
    SetAIParamID(1100612, 537050)
    SetAIParamID(1100613, 537050)
    SetAIParamID(1100614, 537050)
    SetAIParamID(1100615, 537050)
    SetAIParamID(1100616, 537050)
    SetAIParamID(1100617, 537050)
    SetAIParamID(1100618, 537050)
    SetAIParamID(1100405, 293050)
    SetAIParamID(1100406, 293050)
    SetAIParamID(1100407, 293050)
    SetAIParamID(1100408, 293050)
    SetAIParamID(1100409, 293050)
    SetAIParamID(1100410, 293050)
    SetAIParamID(1100411, 293050)
    SetAIParamID(1100412, 293050)
    SetAIParamID(1100413, 293050)
    SetAIParamID(1100414, 293050)
    SetAIParamID(1100415, 293050)
    SetAIParamID(1100416, 293050)
    SetAIParamID(1100417, 293050)
    SetAIParamID(1100418, 293050)
    SetAIParamID(1100419, 293050)
    SetAIParamID(1100420, 293050)
    SetAIParamID(1100421, 293050)
    SetAIParamID(1100422, 293050)
    SetAIParamID(1100423, 293050)
    SetAIParamID(1100424, 293050)
    SetAIParamID(1100425, 293050)
    SetAIParamID(1100426, 293050)
    SetAIParamID(1100427, 293050)
    SetAIParamID(1100428, 293050)
    SetAIParamID(1100429, 293050)
    SetAIParamID(1100430, 293050)
    SetAIParamID(1100431, 293050)
    SetAIParamID(1100432, 293050)
    SetAIParamID(1100433, 293050)
    SetAIParamID(1100434, 293050)
    SetAIParamID(1100435, 293050)
    SetAIParamID(1100436, 293050)
    SetAIParamID(1100437, 293050)
    SetAIParamID(1100438, 293050)
    SetAIParamID(1100439, 293050)
    SetAIParamID(1100440, 293050)
    SetAIParamID(1100441, 293050)
    SetAIParamID(1100442, 293050)
    SetAIParamID(1100443, 293050)
    SetAIParamID(1100444, 293050)
    SetAIParamID(1100445, 293050)
    SetAIParamID(1100446, 293050)
    SetAIParamID(1100447, 293050)
    SetAIParamID(1100448, 293050)
    SetAIParamID(1100449, 293050)
    SetAIParamID(1100450, 293050)
    SetAIParamID(1100451, 293050)
    SetAIParamID(1100452, 293050)
    SetAIParamID(1100453, 293050)
    SetAIParamID(1100454, 293050)
    SetAIParamID(1100455, 293050)
    SetAIParamID(1100456, 293050)
    SetAIParamID(1100457, 293050)
    SetAIParamID(1100458, 293050)
    SetAIParamID(1100459, 293050)
    SetAIParamID(1100460, 293050)
    SetAIParamID(1100461, 293050)
    SetAIParamID(1100462, 293050)
    SetAIParamID(1100463, 293050)
    SetAIParamID(1100464, 293050)
    SetAIParamID(1100465, 293050)
    SetAIParamID(1100466, 293050)
    SetAIParamID(1100467, 293050)
    SetAIParamID(1100468, 293050)
    SetAIParamID(1100469, 293050)
    SetAIParamID(1100470, 293050)
    SetAIParamID(1100471, 293050)
    SetAIParamID(1100472, 293050)
    SetAIParamID(1100473, 293050)
    SetAIParamID(1100474, 293050)
    SetAIParamID(1100475, 293050)
    SetAIParamID(1100476, 293050)
    SetAIParamID(1100477, 293050)
    SetAIParamID(1100478, 293050)
    SetAIParamID(1100479, 293050)
    SetAIParamID(1100480, 293050)
    SetAIParamID(1100481, 293050)
    SetAIParamID(1100482, 293050)
    SetAIParamID(1100483, 293050)
    SetAIParamID(1100484, 293050)
    SetAIParamID(1100485, 293050)
    SetAIParamID(1100486, 293050)
    SetAIParamID(1100487, 293050)
    SetAIParamID(1100488, 293050)
    SetAIParamID(1100489, 293050)
    SetAIParamID(1100490, 293050)
    SetAIParamID(1100491, 293050)
    SetAIParamID(1100492, 293050)
    SetAIParamID(1100493, 293050)
    SetAIParamID(1100494, 293050)
        
    # Common EMEVD manages the flags that control this event.
    Await(not TriggerFlags.HyperAggressionReTrigger)
    
    SetAIParamID(1100214, 120300)
    SetAIParamID(1100215, 120300)
    SetAIParamID(1100216, 120300)
    SetAIParamID(1100217, 120300)
    SetAIParamID(1100218, 120300)
    SetAIParamID(1100219, 120300)
    SetAIParamID(1100220, 120300)
    SetAIParamID(1100221, 120300)
    SetAIParamID(1100222, 120300)
    SetAIParamID(1100223, 120300)
    SetAIParamID(1100224, 120300)
    SetAIParamID(1100300, 231000)
    SetAIParamID(1100301, 231000)
    SetAIParamID(1100302, 231000)
    SetAIParamID(1100303, 231000)
    SetAIParamID(1100225, 231000)
    SetAIParamID(1100226, 231000)
    SetAIParamID(1100227, 231000)
    SetAIParamID(1100228, 250000)
    SetAIParamID(1100229, 250000)
    SetAIParamID(1100230, 250000)
    SetAIParamID(1100231, 250020)
    SetAIParamID(1100232, 250000)
    SetAIParamID(1100233, 250000)
    SetAIParamID(1100234, 250020)
    SetAIParamID(1100235, 250002)
    SetAIParamID(1100236, 250002)
    SetAIParamID(1100237, 250002)
    SetAIParamID(1100238, 250002)
    SetAIParamID(1100100, 250000)
    SetAIParamID(1100101, 250000)
    SetAIParamID(1100102, 250000)
    SetAIParamID(1100104, 250000)
    SetAIParamID(1100105, 250000)
    SetAIParamID(1100130, 250000)
    SetAIParamID(1100132, 250000)
    SetAIParamID(1100135, 250000)
    SetAIParamID(1100136, 250000)
    SetAIParamID(1100137, 250000)
    SetAIParamID(1100138, 250000)
    SetAIParamID(1100400, 250010)
    SetAIParamID(1100401, 250010)
    SetAIParamID(1100402, 250000)
    SetAIParamID(1100403, 250000)
    SetAIParamID(1100404, 250010)
    SetAIParamID(1100239, 250010)
    SetAIParamID(1100240, 250002)
    SetAIParamID(1100241, 250002)
    SetAIParamID(1100242, 250020)
    SetAIParamID(1100243, 250020)
    SetAIParamID(1100244, 250020)
    SetAIParamID(1100180, 257000)
    SetAIParamID(1100160, 273000)
    SetAIParamID(1100200, 283010)
    SetAIParamID(1100201, 283010)
    SetAIParamID(1100202, 283010)
    SetAIParamID(1100203, 283010)
    SetAIParamID(1100204, 283010)
    SetAIParamID(1100205, 283010)
    SetAIParamID(1100206, 283010)
    SetAIParamID(1100207, 283010)
    SetAIParamID(1100208, 283010)
    SetAIParamID(1100209, 283010)
    SetAIParamID(1100210, 283010)
    SetAIParamID(1100211, 283010)
    SetAIParamID(1100212, 283010)
    SetAIParamID(1100213, 283010)
    SetAIParamID(1100245, 284000)
    SetAIParamID(1100246, 284001)
    SetAIParamID(1100247, 284000)
    SetAIParamID(1100248, 284000)
    SetAIParamID(1100249, 284000)
    SetAIParamID(1100250, 284001)
    SetAIParamID(1100251, 284001)
    SetAIParamID(1100252, 284001)
    SetAIParamID(1100253, 284001)
    SetAIParamID(1100254, 284000)
    SetAIParamID(1100255, 284000)
    SetAIParamID(1100900, 284000)
    SetAIParamID(1100901, 284001)
    SetAIParamID(1100902, 284000)
    SetAIParamID(1100903, 284001)
    SetAIParamID(1100904, 284000)
    SetAIParamID(1100905, 284000)
    SetAIParamID(1100906, 284001)
    SetAIParamID(1100256, 293010)
    SetAIParamID(1100257, 293010)
    SetAIParamID(1100258, 293010)
    SetAIParamID(1100259, 293010)
    SetAIParamID(1100260, 293010)
    SetAIParamID(1100261, 293010)
    SetAIParamID(1100262, 293010)
    SetAIParamID(1100263, 293010)
    SetAIParamID(1100264, 293010)
    SetAIParamID(1100907, 293010)
    SetAIParamID(1100908, 293010)
    SetAIParamID(1100909, 293010)
    SetAIParamID(1100910, 293010)
    SetAIParamID(1100911, 293010)
    SetAIParamID(1100170, 342000)
    SetAIParamID(1103900, 349000)
    SetAIParamID(1103910, 349000)
    SetAIParamID(1103902, 349100)
    SetAIParamID(1103901, 349100)
    SetAIParamID(1103911, 349100)
    SetAIParamID(1103912, 349100)
    SetAIParamID(1100600, 537000)
    SetAIParamID(1100601, 537000)
    SetAIParamID(1100602, 537000)
    SetAIParamID(1100603, 537000)
    SetAIParamID(1100604, 537000)
    SetAIParamID(1100605, 537000)
    SetAIParamID(1100606, 537000)
    SetAIParamID(1100607, 537000)
    SetAIParamID(1100608, 537000)
    SetAIParamID(1100609, 537000)
    SetAIParamID(1100610, 537000)
    SetAIParamID(1100611, 537000)
    SetAIParamID(1100612, 537000)
    SetAIParamID(1100613, 537000)
    SetAIParamID(1100614, 537000)
    SetAIParamID(1100615, 537000)
    SetAIParamID(1100616, 537000)
    SetAIParamID(1100617, 537000)
    SetAIParamID(1100618, 537000)
    SetAIParamID(1100405, 293000)
    SetAIParamID(1100406, 293000)
    SetAIParamID(1100407, 293000)
    SetAIParamID(1100408, 293000)
    SetAIParamID(1100409, 293000)
    SetAIParamID(1100410, 293000)
    SetAIParamID(1100411, 293000)
    SetAIParamID(1100412, 293000)
    SetAIParamID(1100413, 293000)
    SetAIParamID(1100414, 293000)
    SetAIParamID(1100415, 293000)
    SetAIParamID(1100416, 293000)
    SetAIParamID(1100417, 293000)
    SetAIParamID(1100418, 293000)
    SetAIParamID(1100419, 293000)
    SetAIParamID(1100420, 293000)
    SetAIParamID(1100421, 293000)
    SetAIParamID(1100422, 293000)
    SetAIParamID(1100423, 293000)
    SetAIParamID(1100424, 293000)
    SetAIParamID(1100425, 293000)
    SetAIParamID(1100426, 293000)
    SetAIParamID(1100427, 293000)
    SetAIParamID(1100428, 293000)
    SetAIParamID(1100429, 293000)
    SetAIParamID(1100430, 293000)
    SetAIParamID(1100431, 293000)
    SetAIParamID(1100432, 293000)
    SetAIParamID(1100433, 293000)
    SetAIParamID(1100434, 293000)
    SetAIParamID(1100435, 293000)
    SetAIParamID(1100436, 293000)
    SetAIParamID(1100437, 293000)
    SetAIParamID(1100438, 293000)
    SetAIParamID(1100439, 293000)
    SetAIParamID(1100440, 293000)
    SetAIParamID(1100441, 293000)
    SetAIParamID(1100442, 293000)
    SetAIParamID(1100443, 293000)
    SetAIParamID(1100444, 293000)
    SetAIParamID(1100445, 293000)
    SetAIParamID(1100446, 293000)
    SetAIParamID(1100447, 293000)
    SetAIParamID(1100448, 293000)
    SetAIParamID(1100449, 293000)
    SetAIParamID(1100450, 293000)
    SetAIParamID(1100451, 293000)
    SetAIParamID(1100452, 293000)
    SetAIParamID(1100453, 293000)
    SetAIParamID(1100454, 293000)
    SetAIParamID(1100455, 293000)
    SetAIParamID(1100456, 293000)
    SetAIParamID(1100457, 293000)
    SetAIParamID(1100458, 293000)
    SetAIParamID(1100459, 293000)
    SetAIParamID(1100460, 293000)
    SetAIParamID(1100461, 293000)
    SetAIParamID(1100462, 293000)
    SetAIParamID(1100463, 293000)
    SetAIParamID(1100464, 293000)
    SetAIParamID(1100465, 293000)
    SetAIParamID(1100466, 293000)
    SetAIParamID(1100467, 293000)
    SetAIParamID(1100468, 293000)
    SetAIParamID(1100469, 293000)
    SetAIParamID(1100470, 293000)
    SetAIParamID(1100471, 293000)
    SetAIParamID(1100472, 293000)
    SetAIParamID(1100473, 293000)
    SetAIParamID(1100474, 293000)
    SetAIParamID(1100475, 293000)
    SetAIParamID(1100476, 293000)
    SetAIParamID(1100477, 293000)
    SetAIParamID(1100478, 293000)
    SetAIParamID(1100479, 293000)
    SetAIParamID(1100480, 293000)
    SetAIParamID(1100481, 293000)
    SetAIParamID(1100482, 293000)
    SetAIParamID(1100483, 293000)
    SetAIParamID(1100484, 293000)
    SetAIParamID(1100485, 293000)
    SetAIParamID(1100486, 293000)
    SetAIParamID(1100487, 293000)
    SetAIParamID(1100488, 293000)
    SetAIParamID(1100489, 293000)
    SetAIParamID(1100490, 293000)
    SetAIParamID(1100491, 293000)
    SetAIParamID(1100492, 293000)
    SetAIParamID(1100493, 293000)
    SetAIParamID(1100494, 293000)
    
    return RESTART


@RestartOnRest
def EnemySpeedUp():
    """ 11102200: Temporary enemy effect. """
    Await(TriggerFlags.EnemySpeedUp)
    AddSpecialEffect(6312, 200000)
    AddSpecialEffect(6422, 200000)
    AddSpecialEffect(6570, 200000)
    AddSpecialEffect(1100960, 200000)
    AddSpecialEffect(1100214, 200000)
    AddSpecialEffect(1100215, 200000)
    AddSpecialEffect(1100216, 200000)
    AddSpecialEffect(1100217, 200000)
    AddSpecialEffect(1100218, 200000)
    AddSpecialEffect(1100219, 200000)
    AddSpecialEffect(1100220, 200000)
    AddSpecialEffect(1100221, 200000)
    AddSpecialEffect(1100222, 200000)
    AddSpecialEffect(1100223, 200000)
    AddSpecialEffect(1100224, 200000)
    AddSpecialEffect(1100300, 200000)
    AddSpecialEffect(1100301, 200000)
    AddSpecialEffect(1100302, 200000)
    AddSpecialEffect(1100303, 200000)
    AddSpecialEffect(1100225, 200000)
    AddSpecialEffect(1100226, 200000)
    AddSpecialEffect(1100227, 200000)
    AddSpecialEffect(1100228, 200000)
    AddSpecialEffect(1100229, 200000)
    AddSpecialEffect(1100230, 200000)
    AddSpecialEffect(1100231, 200000)
    AddSpecialEffect(1100232, 200000)
    AddSpecialEffect(1100233, 200000)
    AddSpecialEffect(1100234, 200000)
    AddSpecialEffect(1100235, 200000)
    AddSpecialEffect(1100236, 200000)
    AddSpecialEffect(1100237, 200000)
    AddSpecialEffect(1100238, 200000)
    AddSpecialEffect(1100100, 200000)
    AddSpecialEffect(1100101, 200000)
    AddSpecialEffect(1100102, 200000)
    AddSpecialEffect(1100104, 200000)
    AddSpecialEffect(1100105, 200000)
    AddSpecialEffect(1100130, 200000)
    AddSpecialEffect(1100132, 200000)
    AddSpecialEffect(1100135, 200000)
    AddSpecialEffect(1100136, 200000)
    AddSpecialEffect(1100137, 200000)
    AddSpecialEffect(1100138, 200000)
    AddSpecialEffect(1100400, 200000)
    AddSpecialEffect(1100401, 200000)
    AddSpecialEffect(1100402, 200000)
    AddSpecialEffect(1100403, 200000)
    AddSpecialEffect(1100404, 200000)
    AddSpecialEffect(1100239, 200000)
    AddSpecialEffect(1100240, 200000)
    AddSpecialEffect(1100241, 200000)
    AddSpecialEffect(1100242, 200000)
    AddSpecialEffect(1100243, 200000)
    AddSpecialEffect(1100244, 200000)
    AddSpecialEffect(1100180, 200000)
    AddSpecialEffect(1100160, 200000)
    AddSpecialEffect(1100161, 200000)
    AddSpecialEffect(1100200, 200000)
    AddSpecialEffect(1100201, 200000)
    AddSpecialEffect(1100202, 200000)
    AddSpecialEffect(1100203, 200000)
    AddSpecialEffect(1100204, 200000)
    AddSpecialEffect(1100205, 200000)
    AddSpecialEffect(1100206, 200000)
    AddSpecialEffect(1100207, 200000)
    AddSpecialEffect(1100208, 200000)
    AddSpecialEffect(1100209, 200000)
    AddSpecialEffect(1100210, 200000)
    AddSpecialEffect(1100211, 200000)
    AddSpecialEffect(1100212, 200000)
    AddSpecialEffect(1100213, 200000)
    AddSpecialEffect(1100245, 200000)
    AddSpecialEffect(1100246, 200000)
    AddSpecialEffect(1100247, 200000)
    AddSpecialEffect(1100248, 200000)
    AddSpecialEffect(1100249, 200000)
    AddSpecialEffect(1100250, 200000)
    AddSpecialEffect(1100251, 200000)
    AddSpecialEffect(1100252, 200000)
    AddSpecialEffect(1100253, 200000)
    AddSpecialEffect(1100254, 200000)
    AddSpecialEffect(1100255, 200000)
    AddSpecialEffect(1100900, 200000)
    AddSpecialEffect(1100901, 200000)
    AddSpecialEffect(1100902, 200000)
    AddSpecialEffect(1100903, 200000)
    AddSpecialEffect(1100904, 200000)
    AddSpecialEffect(1100905, 200000)
    AddSpecialEffect(1100906, 200000)
    AddSpecialEffect(1100256, 200000)
    AddSpecialEffect(1100257, 200000)
    AddSpecialEffect(1100258, 200000)
    AddSpecialEffect(1100259, 200000)
    AddSpecialEffect(1100260, 200000)
    AddSpecialEffect(1100261, 200000)
    AddSpecialEffect(1100262, 200000)
    AddSpecialEffect(1100263, 200000)
    AddSpecialEffect(1100264, 200000)
    AddSpecialEffect(1100907, 200000)
    AddSpecialEffect(1100908, 200000)
    AddSpecialEffect(1100909, 200000)
    AddSpecialEffect(1100910, 200000)
    AddSpecialEffect(1100911, 200000)
    AddSpecialEffect(1100170, 200000)
    AddSpecialEffect(1100171, 200000)
    AddSpecialEffect(1100172, 200000)
    AddSpecialEffect(1103900, 200000)
    AddSpecialEffect(1103910, 200000)
    AddSpecialEffect(1103902, 200000)
    AddSpecialEffect(1103901, 200000)
    AddSpecialEffect(1103911, 200000)
    AddSpecialEffect(1103912, 200000)
    WaitFrames(10)  # give other loaded maps time to trigger
    DisableFlag(TriggerFlags.EnemySpeedUp)
    return RESTART


@RestartOnRest
def EnemyExtremeSpeedUp():
    """ 11102201: Temporary enemy effect. """
    Await(TriggerFlags.EnemyExtremeSpeedUp)
    AddSpecialEffect(6312, 200001)
    AddSpecialEffect(6422, 200001)
    AddSpecialEffect(6570, 200001)
    AddSpecialEffect(1100960, 200001)
    AddSpecialEffect(1100214, 200001)
    AddSpecialEffect(1100215, 200001)
    AddSpecialEffect(1100216, 200001)
    AddSpecialEffect(1100217, 200001)
    AddSpecialEffect(1100218, 200001)
    AddSpecialEffect(1100219, 200001)
    AddSpecialEffect(1100220, 200001)
    AddSpecialEffect(1100221, 200001)
    AddSpecialEffect(1100222, 200001)
    AddSpecialEffect(1100223, 200001)
    AddSpecialEffect(1100224, 200001)
    AddSpecialEffect(1100300, 200001)
    AddSpecialEffect(1100301, 200001)
    AddSpecialEffect(1100302, 200001)
    AddSpecialEffect(1100303, 200001)
    AddSpecialEffect(1100225, 200001)
    AddSpecialEffect(1100226, 200001)
    AddSpecialEffect(1100227, 200001)
    AddSpecialEffect(1100228, 200001)
    AddSpecialEffect(1100229, 200001)
    AddSpecialEffect(1100230, 200001)
    AddSpecialEffect(1100231, 200001)
    AddSpecialEffect(1100232, 200001)
    AddSpecialEffect(1100233, 200001)
    AddSpecialEffect(1100234, 200001)
    AddSpecialEffect(1100235, 200001)
    AddSpecialEffect(1100236, 200001)
    AddSpecialEffect(1100237, 200001)
    AddSpecialEffect(1100238, 200001)
    AddSpecialEffect(1100100, 200001)
    AddSpecialEffect(1100101, 200001)
    AddSpecialEffect(1100102, 200001)
    AddSpecialEffect(1100104, 200001)
    AddSpecialEffect(1100105, 200001)
    AddSpecialEffect(1100130, 200001)
    AddSpecialEffect(1100132, 200001)
    AddSpecialEffect(1100135, 200001)
    AddSpecialEffect(1100136, 200001)
    AddSpecialEffect(1100137, 200001)
    AddSpecialEffect(1100138, 200001)
    AddSpecialEffect(1100400, 200001)
    AddSpecialEffect(1100401, 200001)
    AddSpecialEffect(1100402, 200001)
    AddSpecialEffect(1100403, 200001)
    AddSpecialEffect(1100404, 200001)
    AddSpecialEffect(1100239, 200001)
    AddSpecialEffect(1100240, 200001)
    AddSpecialEffect(1100241, 200001)
    AddSpecialEffect(1100242, 200001)
    AddSpecialEffect(1100243, 200001)
    AddSpecialEffect(1100244, 200001)
    AddSpecialEffect(1100180, 200001)
    AddSpecialEffect(1100160, 200001)
    AddSpecialEffect(1100161, 200001)
    AddSpecialEffect(1100200, 200001)
    AddSpecialEffect(1100201, 200001)
    AddSpecialEffect(1100202, 200001)
    AddSpecialEffect(1100203, 200001)
    AddSpecialEffect(1100204, 200001)
    AddSpecialEffect(1100205, 200001)
    AddSpecialEffect(1100206, 200001)
    AddSpecialEffect(1100207, 200001)
    AddSpecialEffect(1100208, 200001)
    AddSpecialEffect(1100209, 200001)
    AddSpecialEffect(1100210, 200001)
    AddSpecialEffect(1100211, 200001)
    AddSpecialEffect(1100212, 200001)
    AddSpecialEffect(1100213, 200001)
    AddSpecialEffect(1100245, 200001)
    AddSpecialEffect(1100246, 200001)
    AddSpecialEffect(1100247, 200001)
    AddSpecialEffect(1100248, 200001)
    AddSpecialEffect(1100249, 200001)
    AddSpecialEffect(1100250, 200001)
    AddSpecialEffect(1100251, 200001)
    AddSpecialEffect(1100252, 200001)
    AddSpecialEffect(1100253, 200001)
    AddSpecialEffect(1100254, 200001)
    AddSpecialEffect(1100255, 200001)
    AddSpecialEffect(1100900, 200001)
    AddSpecialEffect(1100901, 200001)
    AddSpecialEffect(1100902, 200001)
    AddSpecialEffect(1100903, 200001)
    AddSpecialEffect(1100904, 200001)
    AddSpecialEffect(1100905, 200001)
    AddSpecialEffect(1100906, 200001)
    AddSpecialEffect(1100256, 200001)
    AddSpecialEffect(1100257, 200001)
    AddSpecialEffect(1100258, 200001)
    AddSpecialEffect(1100259, 200001)
    AddSpecialEffect(1100260, 200001)
    AddSpecialEffect(1100261, 200001)
    AddSpecialEffect(1100262, 200001)
    AddSpecialEffect(1100263, 200001)
    AddSpecialEffect(1100264, 200001)
    AddSpecialEffect(1100907, 200001)
    AddSpecialEffect(1100908, 200001)
    AddSpecialEffect(1100909, 200001)
    AddSpecialEffect(1100910, 200001)
    AddSpecialEffect(1100911, 200001)
    AddSpecialEffect(1100170, 200001)
    AddSpecialEffect(1100171, 200001)
    AddSpecialEffect(1100172, 200001)
    AddSpecialEffect(1103900, 200001)
    AddSpecialEffect(1103910, 200001)
    AddSpecialEffect(1103902, 200001)
    AddSpecialEffect(1103901, 200001)
    AddSpecialEffect(1103911, 200001)
    AddSpecialEffect(1103912, 200001)
    WaitFrames(10)  # give other loaded maps time to trigger
    DisableFlag(TriggerFlags.EnemyExtremeSpeedUp)
    return RESTART


@RestartOnRest
def EnemySpeedDown():
    """ 11102202: Temporary enemy effect. """
    Await(TriggerFlags.EnemySpeedDown)
    AddSpecialEffect(6312, 200002)
    AddSpecialEffect(6422, 200002)
    AddSpecialEffect(6570, 200002)
    AddSpecialEffect(1100960, 200002)
    AddSpecialEffect(1100214, 200002)
    AddSpecialEffect(1100215, 200002)
    AddSpecialEffect(1100216, 200002)
    AddSpecialEffect(1100217, 200002)
    AddSpecialEffect(1100218, 200002)
    AddSpecialEffect(1100219, 200002)
    AddSpecialEffect(1100220, 200002)
    AddSpecialEffect(1100221, 200002)
    AddSpecialEffect(1100222, 200002)
    AddSpecialEffect(1100223, 200002)
    AddSpecialEffect(1100224, 200002)
    AddSpecialEffect(1100300, 200002)
    AddSpecialEffect(1100301, 200002)
    AddSpecialEffect(1100302, 200002)
    AddSpecialEffect(1100303, 200002)
    AddSpecialEffect(1100225, 200002)
    AddSpecialEffect(1100226, 200002)
    AddSpecialEffect(1100227, 200002)
    AddSpecialEffect(1100228, 200002)
    AddSpecialEffect(1100229, 200002)
    AddSpecialEffect(1100230, 200002)
    AddSpecialEffect(1100231, 200002)
    AddSpecialEffect(1100232, 200002)
    AddSpecialEffect(1100233, 200002)
    AddSpecialEffect(1100234, 200002)
    AddSpecialEffect(1100235, 200002)
    AddSpecialEffect(1100236, 200002)
    AddSpecialEffect(1100237, 200002)
    AddSpecialEffect(1100238, 200002)
    AddSpecialEffect(1100100, 200002)
    AddSpecialEffect(1100101, 200002)
    AddSpecialEffect(1100102, 200002)
    AddSpecialEffect(1100104, 200002)
    AddSpecialEffect(1100105, 200002)
    AddSpecialEffect(1100130, 200002)
    AddSpecialEffect(1100132, 200002)
    AddSpecialEffect(1100135, 200002)
    AddSpecialEffect(1100136, 200002)
    AddSpecialEffect(1100137, 200002)
    AddSpecialEffect(1100138, 200002)
    AddSpecialEffect(1100400, 200002)
    AddSpecialEffect(1100401, 200002)
    AddSpecialEffect(1100402, 200002)
    AddSpecialEffect(1100403, 200002)
    AddSpecialEffect(1100404, 200002)
    AddSpecialEffect(1100239, 200002)
    AddSpecialEffect(1100240, 200002)
    AddSpecialEffect(1100241, 200002)
    AddSpecialEffect(1100242, 200002)
    AddSpecialEffect(1100243, 200002)
    AddSpecialEffect(1100244, 200002)
    AddSpecialEffect(1100180, 200002)
    AddSpecialEffect(1100160, 200002)
    AddSpecialEffect(1100161, 200002)
    AddSpecialEffect(1100200, 200002)
    AddSpecialEffect(1100201, 200002)
    AddSpecialEffect(1100202, 200002)
    AddSpecialEffect(1100203, 200002)
    AddSpecialEffect(1100204, 200002)
    AddSpecialEffect(1100205, 200002)
    AddSpecialEffect(1100206, 200002)
    AddSpecialEffect(1100207, 200002)
    AddSpecialEffect(1100208, 200002)
    AddSpecialEffect(1100209, 200002)
    AddSpecialEffect(1100210, 200002)
    AddSpecialEffect(1100211, 200002)
    AddSpecialEffect(1100212, 200002)
    AddSpecialEffect(1100213, 200002)
    AddSpecialEffect(1100245, 200002)
    AddSpecialEffect(1100246, 200002)
    AddSpecialEffect(1100247, 200002)
    AddSpecialEffect(1100248, 200002)
    AddSpecialEffect(1100249, 200002)
    AddSpecialEffect(1100250, 200002)
    AddSpecialEffect(1100251, 200002)
    AddSpecialEffect(1100252, 200002)
    AddSpecialEffect(1100253, 200002)
    AddSpecialEffect(1100254, 200002)
    AddSpecialEffect(1100255, 200002)
    AddSpecialEffect(1100900, 200002)
    AddSpecialEffect(1100901, 200002)
    AddSpecialEffect(1100902, 200002)
    AddSpecialEffect(1100903, 200002)
    AddSpecialEffect(1100904, 200002)
    AddSpecialEffect(1100905, 200002)
    AddSpecialEffect(1100906, 200002)
    AddSpecialEffect(1100256, 200002)
    AddSpecialEffect(1100257, 200002)
    AddSpecialEffect(1100258, 200002)
    AddSpecialEffect(1100259, 200002)
    AddSpecialEffect(1100260, 200002)
    AddSpecialEffect(1100261, 200002)
    AddSpecialEffect(1100262, 200002)
    AddSpecialEffect(1100263, 200002)
    AddSpecialEffect(1100264, 200002)
    AddSpecialEffect(1100907, 200002)
    AddSpecialEffect(1100908, 200002)
    AddSpecialEffect(1100909, 200002)
    AddSpecialEffect(1100910, 200002)
    AddSpecialEffect(1100911, 200002)
    AddSpecialEffect(1100170, 200002)
    AddSpecialEffect(1100171, 200002)
    AddSpecialEffect(1100172, 200002)
    AddSpecialEffect(1103900, 200002)
    AddSpecialEffect(1103910, 200002)
    AddSpecialEffect(1103902, 200002)
    AddSpecialEffect(1103901, 200002)
    AddSpecialEffect(1103911, 200002)
    AddSpecialEffect(1103912, 200002)
    WaitFrames(10)  # give other loaded maps time to trigger
    DisableFlag(TriggerFlags.EnemySpeedDown)
    return RESTART


@RestartOnRest
def EnemyExtremeSpeedDown():
    """ 11102203: Temporary enemy effect. """
    Await(TriggerFlags.EnemyExtremeSpeedDown)
    AddSpecialEffect(6312, 200003)
    AddSpecialEffect(6422, 200003)
    AddSpecialEffect(6570, 200003)
    AddSpecialEffect(1100960, 200003)
    AddSpecialEffect(1100214, 200003)
    AddSpecialEffect(1100215, 200003)
    AddSpecialEffect(1100216, 200003)
    AddSpecialEffect(1100217, 200003)
    AddSpecialEffect(1100218, 200003)
    AddSpecialEffect(1100219, 200003)
    AddSpecialEffect(1100220, 200003)
    AddSpecialEffect(1100221, 200003)
    AddSpecialEffect(1100222, 200003)
    AddSpecialEffect(1100223, 200003)
    AddSpecialEffect(1100224, 200003)
    AddSpecialEffect(1100300, 200003)
    AddSpecialEffect(1100301, 200003)
    AddSpecialEffect(1100302, 200003)
    AddSpecialEffect(1100303, 200003)
    AddSpecialEffect(1100225, 200003)
    AddSpecialEffect(1100226, 200003)
    AddSpecialEffect(1100227, 200003)
    AddSpecialEffect(1100228, 200003)
    AddSpecialEffect(1100229, 200003)
    AddSpecialEffect(1100230, 200003)
    AddSpecialEffect(1100231, 200003)
    AddSpecialEffect(1100232, 200003)
    AddSpecialEffect(1100233, 200003)
    AddSpecialEffect(1100234, 200003)
    AddSpecialEffect(1100235, 200003)
    AddSpecialEffect(1100236, 200003)
    AddSpecialEffect(1100237, 200003)
    AddSpecialEffect(1100238, 200003)
    AddSpecialEffect(1100100, 200003)
    AddSpecialEffect(1100101, 200003)
    AddSpecialEffect(1100102, 200003)
    AddSpecialEffect(1100104, 200003)
    AddSpecialEffect(1100105, 200003)
    AddSpecialEffect(1100130, 200003)
    AddSpecialEffect(1100132, 200003)
    AddSpecialEffect(1100135, 200003)
    AddSpecialEffect(1100136, 200003)
    AddSpecialEffect(1100137, 200003)
    AddSpecialEffect(1100138, 200003)
    AddSpecialEffect(1100400, 200003)
    AddSpecialEffect(1100401, 200003)
    AddSpecialEffect(1100402, 200003)
    AddSpecialEffect(1100403, 200003)
    AddSpecialEffect(1100404, 200003)
    AddSpecialEffect(1100239, 200003)
    AddSpecialEffect(1100240, 200003)
    AddSpecialEffect(1100241, 200003)
    AddSpecialEffect(1100242, 200003)
    AddSpecialEffect(1100243, 200003)
    AddSpecialEffect(1100244, 200003)
    AddSpecialEffect(1100180, 200003)
    AddSpecialEffect(1100160, 200003)
    AddSpecialEffect(1100161, 200003)
    AddSpecialEffect(1100200, 200003)
    AddSpecialEffect(1100201, 200003)
    AddSpecialEffect(1100202, 200003)
    AddSpecialEffect(1100203, 200003)
    AddSpecialEffect(1100204, 200003)
    AddSpecialEffect(1100205, 200003)
    AddSpecialEffect(1100206, 200003)
    AddSpecialEffect(1100207, 200003)
    AddSpecialEffect(1100208, 200003)
    AddSpecialEffect(1100209, 200003)
    AddSpecialEffect(1100210, 200003)
    AddSpecialEffect(1100211, 200003)
    AddSpecialEffect(1100212, 200003)
    AddSpecialEffect(1100213, 200003)
    AddSpecialEffect(1100245, 200003)
    AddSpecialEffect(1100246, 200003)
    AddSpecialEffect(1100247, 200003)
    AddSpecialEffect(1100248, 200003)
    AddSpecialEffect(1100249, 200003)
    AddSpecialEffect(1100250, 200003)
    AddSpecialEffect(1100251, 200003)
    AddSpecialEffect(1100252, 200003)
    AddSpecialEffect(1100253, 200003)
    AddSpecialEffect(1100254, 200003)
    AddSpecialEffect(1100255, 200003)
    AddSpecialEffect(1100900, 200003)
    AddSpecialEffect(1100901, 200003)
    AddSpecialEffect(1100902, 200003)
    AddSpecialEffect(1100903, 200003)
    AddSpecialEffect(1100904, 200003)
    AddSpecialEffect(1100905, 200003)
    AddSpecialEffect(1100906, 200003)
    AddSpecialEffect(1100256, 200003)
    AddSpecialEffect(1100257, 200003)
    AddSpecialEffect(1100258, 200003)
    AddSpecialEffect(1100259, 200003)
    AddSpecialEffect(1100260, 200003)
    AddSpecialEffect(1100261, 200003)
    AddSpecialEffect(1100262, 200003)
    AddSpecialEffect(1100263, 200003)
    AddSpecialEffect(1100264, 200003)
    AddSpecialEffect(1100907, 200003)
    AddSpecialEffect(1100908, 200003)
    AddSpecialEffect(1100909, 200003)
    AddSpecialEffect(1100910, 200003)
    AddSpecialEffect(1100911, 200003)
    AddSpecialEffect(1100170, 200003)
    AddSpecialEffect(1100171, 200003)
    AddSpecialEffect(1100172, 200003)
    AddSpecialEffect(1103900, 200003)
    AddSpecialEffect(1103910, 200003)
    AddSpecialEffect(1103902, 200003)
    AddSpecialEffect(1103901, 200003)
    AddSpecialEffect(1103911, 200003)
    AddSpecialEffect(1103912, 200003)
    WaitFrames(10)  # give other loaded maps time to trigger
    DisableFlag(TriggerFlags.EnemyExtremeSpeedDown)
    return RESTART


@RestartOnRest
def EnemyHealthRegain():
    """ 11102204: Temporary enemy effect. """
    Await(TriggerFlags.EnemyHealthRegain)
    AddSpecialEffect(6312, 200004)
    AddSpecialEffect(6422, 200004)
    AddSpecialEffect(6570, 200004)
    AddSpecialEffect(1100960, 200004)
    AddSpecialEffect(1100214, 200004)
    AddSpecialEffect(1100215, 200004)
    AddSpecialEffect(1100216, 200004)
    AddSpecialEffect(1100217, 200004)
    AddSpecialEffect(1100218, 200004)
    AddSpecialEffect(1100219, 200004)
    AddSpecialEffect(1100220, 200004)
    AddSpecialEffect(1100221, 200004)
    AddSpecialEffect(1100222, 200004)
    AddSpecialEffect(1100223, 200004)
    AddSpecialEffect(1100224, 200004)
    AddSpecialEffect(1100300, 200004)
    AddSpecialEffect(1100301, 200004)
    AddSpecialEffect(1100302, 200004)
    AddSpecialEffect(1100303, 200004)
    AddSpecialEffect(1100225, 200004)
    AddSpecialEffect(1100226, 200004)
    AddSpecialEffect(1100227, 200004)
    AddSpecialEffect(1100228, 200004)
    AddSpecialEffect(1100229, 200004)
    AddSpecialEffect(1100230, 200004)
    AddSpecialEffect(1100231, 200004)
    AddSpecialEffect(1100232, 200004)
    AddSpecialEffect(1100233, 200004)
    AddSpecialEffect(1100234, 200004)
    AddSpecialEffect(1100235, 200004)
    AddSpecialEffect(1100236, 200004)
    AddSpecialEffect(1100237, 200004)
    AddSpecialEffect(1100238, 200004)
    AddSpecialEffect(1100100, 200004)
    AddSpecialEffect(1100101, 200004)
    AddSpecialEffect(1100102, 200004)
    AddSpecialEffect(1100104, 200004)
    AddSpecialEffect(1100105, 200004)
    AddSpecialEffect(1100130, 200004)
    AddSpecialEffect(1100132, 200004)
    AddSpecialEffect(1100135, 200004)
    AddSpecialEffect(1100136, 200004)
    AddSpecialEffect(1100137, 200004)
    AddSpecialEffect(1100138, 200004)
    AddSpecialEffect(1100400, 200004)
    AddSpecialEffect(1100401, 200004)
    AddSpecialEffect(1100402, 200004)
    AddSpecialEffect(1100403, 200004)
    AddSpecialEffect(1100404, 200004)
    AddSpecialEffect(1100239, 200004)
    AddSpecialEffect(1100240, 200004)
    AddSpecialEffect(1100241, 200004)
    AddSpecialEffect(1100242, 200004)
    AddSpecialEffect(1100243, 200004)
    AddSpecialEffect(1100244, 200004)
    AddSpecialEffect(1100180, 200004)
    AddSpecialEffect(1100160, 200004)
    AddSpecialEffect(1100161, 200004)
    AddSpecialEffect(1100200, 200004)
    AddSpecialEffect(1100201, 200004)
    AddSpecialEffect(1100202, 200004)
    AddSpecialEffect(1100203, 200004)
    AddSpecialEffect(1100204, 200004)
    AddSpecialEffect(1100205, 200004)
    AddSpecialEffect(1100206, 200004)
    AddSpecialEffect(1100207, 200004)
    AddSpecialEffect(1100208, 200004)
    AddSpecialEffect(1100209, 200004)
    AddSpecialEffect(1100210, 200004)
    AddSpecialEffect(1100211, 200004)
    AddSpecialEffect(1100212, 200004)
    AddSpecialEffect(1100213, 200004)
    AddSpecialEffect(1100245, 200004)
    AddSpecialEffect(1100246, 200004)
    AddSpecialEffect(1100247, 200004)
    AddSpecialEffect(1100248, 200004)
    AddSpecialEffect(1100249, 200004)
    AddSpecialEffect(1100250, 200004)
    AddSpecialEffect(1100251, 200004)
    AddSpecialEffect(1100252, 200004)
    AddSpecialEffect(1100253, 200004)
    AddSpecialEffect(1100254, 200004)
    AddSpecialEffect(1100255, 200004)
    AddSpecialEffect(1100900, 200004)
    AddSpecialEffect(1100901, 200004)
    AddSpecialEffect(1100902, 200004)
    AddSpecialEffect(1100903, 200004)
    AddSpecialEffect(1100904, 200004)
    AddSpecialEffect(1100905, 200004)
    AddSpecialEffect(1100906, 200004)
    AddSpecialEffect(1100256, 200004)
    AddSpecialEffect(1100257, 200004)
    AddSpecialEffect(1100258, 200004)
    AddSpecialEffect(1100259, 200004)
    AddSpecialEffect(1100260, 200004)
    AddSpecialEffect(1100261, 200004)
    AddSpecialEffect(1100262, 200004)
    AddSpecialEffect(1100263, 200004)
    AddSpecialEffect(1100264, 200004)
    AddSpecialEffect(1100907, 200004)
    AddSpecialEffect(1100908, 200004)
    AddSpecialEffect(1100909, 200004)
    AddSpecialEffect(1100910, 200004)
    AddSpecialEffect(1100911, 200004)
    AddSpecialEffect(1100170, 200004)
    AddSpecialEffect(1100171, 200004)
    AddSpecialEffect(1100172, 200004)
    AddSpecialEffect(1103900, 200004)
    AddSpecialEffect(1103910, 200004)
    AddSpecialEffect(1103902, 200004)
    AddSpecialEffect(1103901, 200004)
    AddSpecialEffect(1103911, 200004)
    AddSpecialEffect(1103912, 200004)
    WaitFrames(10)  # give other loaded maps time to trigger
    DisableFlag(TriggerFlags.EnemyHealthRegain)
    return RESTART


@RestartOnRest
def EnemyMaxHealthUp():
    """ 11102205: Temporary enemy effect. """
    Await(TriggerFlags.EnemyMaxHealthUp)
    AddSpecialEffect(6312, 200005)
    AddSpecialEffect(6422, 200005)
    AddSpecialEffect(6570, 200005)
    AddSpecialEffect(1100960, 200005)
    AddSpecialEffect(1100214, 200005)
    AddSpecialEffect(1100215, 200005)
    AddSpecialEffect(1100216, 200005)
    AddSpecialEffect(1100217, 200005)
    AddSpecialEffect(1100218, 200005)
    AddSpecialEffect(1100219, 200005)
    AddSpecialEffect(1100220, 200005)
    AddSpecialEffect(1100221, 200005)
    AddSpecialEffect(1100222, 200005)
    AddSpecialEffect(1100223, 200005)
    AddSpecialEffect(1100224, 200005)
    AddSpecialEffect(1100300, 200005)
    AddSpecialEffect(1100301, 200005)
    AddSpecialEffect(1100302, 200005)
    AddSpecialEffect(1100303, 200005)
    AddSpecialEffect(1100225, 200005)
    AddSpecialEffect(1100226, 200005)
    AddSpecialEffect(1100227, 200005)
    AddSpecialEffect(1100228, 200005)
    AddSpecialEffect(1100229, 200005)
    AddSpecialEffect(1100230, 200005)
    AddSpecialEffect(1100231, 200005)
    AddSpecialEffect(1100232, 200005)
    AddSpecialEffect(1100233, 200005)
    AddSpecialEffect(1100234, 200005)
    AddSpecialEffect(1100235, 200005)
    AddSpecialEffect(1100236, 200005)
    AddSpecialEffect(1100237, 200005)
    AddSpecialEffect(1100238, 200005)
    AddSpecialEffect(1100100, 200005)
    AddSpecialEffect(1100101, 200005)
    AddSpecialEffect(1100102, 200005)
    AddSpecialEffect(1100104, 200005)
    AddSpecialEffect(1100105, 200005)
    AddSpecialEffect(1100130, 200005)
    AddSpecialEffect(1100132, 200005)
    AddSpecialEffect(1100135, 200005)
    AddSpecialEffect(1100136, 200005)
    AddSpecialEffect(1100137, 200005)
    AddSpecialEffect(1100138, 200005)
    AddSpecialEffect(1100400, 200005)
    AddSpecialEffect(1100401, 200005)
    AddSpecialEffect(1100402, 200005)
    AddSpecialEffect(1100403, 200005)
    AddSpecialEffect(1100404, 200005)
    AddSpecialEffect(1100239, 200005)
    AddSpecialEffect(1100240, 200005)
    AddSpecialEffect(1100241, 200005)
    AddSpecialEffect(1100242, 200005)
    AddSpecialEffect(1100243, 200005)
    AddSpecialEffect(1100244, 200005)
    AddSpecialEffect(1100180, 200005)
    AddSpecialEffect(1100160, 200005)
    AddSpecialEffect(1100161, 200005)
    AddSpecialEffect(1100200, 200005)
    AddSpecialEffect(1100201, 200005)
    AddSpecialEffect(1100202, 200005)
    AddSpecialEffect(1100203, 200005)
    AddSpecialEffect(1100204, 200005)
    AddSpecialEffect(1100205, 200005)
    AddSpecialEffect(1100206, 200005)
    AddSpecialEffect(1100207, 200005)
    AddSpecialEffect(1100208, 200005)
    AddSpecialEffect(1100209, 200005)
    AddSpecialEffect(1100210, 200005)
    AddSpecialEffect(1100211, 200005)
    AddSpecialEffect(1100212, 200005)
    AddSpecialEffect(1100213, 200005)
    AddSpecialEffect(1100245, 200005)
    AddSpecialEffect(1100246, 200005)
    AddSpecialEffect(1100247, 200005)
    AddSpecialEffect(1100248, 200005)
    AddSpecialEffect(1100249, 200005)
    AddSpecialEffect(1100250, 200005)
    AddSpecialEffect(1100251, 200005)
    AddSpecialEffect(1100252, 200005)
    AddSpecialEffect(1100253, 200005)
    AddSpecialEffect(1100254, 200005)
    AddSpecialEffect(1100255, 200005)
    AddSpecialEffect(1100900, 200005)
    AddSpecialEffect(1100901, 200005)
    AddSpecialEffect(1100902, 200005)
    AddSpecialEffect(1100903, 200005)
    AddSpecialEffect(1100904, 200005)
    AddSpecialEffect(1100905, 200005)
    AddSpecialEffect(1100906, 200005)
    AddSpecialEffect(1100256, 200005)
    AddSpecialEffect(1100257, 200005)
    AddSpecialEffect(1100258, 200005)
    AddSpecialEffect(1100259, 200005)
    AddSpecialEffect(1100260, 200005)
    AddSpecialEffect(1100261, 200005)
    AddSpecialEffect(1100262, 200005)
    AddSpecialEffect(1100263, 200005)
    AddSpecialEffect(1100264, 200005)
    AddSpecialEffect(1100907, 200005)
    AddSpecialEffect(1100908, 200005)
    AddSpecialEffect(1100909, 200005)
    AddSpecialEffect(1100910, 200005)
    AddSpecialEffect(1100911, 200005)
    AddSpecialEffect(1100170, 200005)
    AddSpecialEffect(1100171, 200005)
    AddSpecialEffect(1100172, 200005)
    AddSpecialEffect(1103900, 200005)
    AddSpecialEffect(1103910, 200005)
    AddSpecialEffect(1103902, 200005)
    AddSpecialEffect(1103901, 200005)
    AddSpecialEffect(1103911, 200005)
    AddSpecialEffect(1103912, 200005)
    WaitFrames(10)  # give other loaded maps time to trigger
    DisableFlag(TriggerFlags.EnemyMaxHealthUp)
    return RESTART


@RestartOnRest
def EnemyMaxHealthDown():
    """ 11102206: Temporary enemy effect. """
    Await(TriggerFlags.EnemyMaxHealthDown)
    AddSpecialEffect(6312, 200006)
    AddSpecialEffect(6422, 200006)
    AddSpecialEffect(6570, 200006)
    AddSpecialEffect(1100960, 200006)
    AddSpecialEffect(1100214, 200006)
    AddSpecialEffect(1100215, 200006)
    AddSpecialEffect(1100216, 200006)
    AddSpecialEffect(1100217, 200006)
    AddSpecialEffect(1100218, 200006)
    AddSpecialEffect(1100219, 200006)
    AddSpecialEffect(1100220, 200006)
    AddSpecialEffect(1100221, 200006)
    AddSpecialEffect(1100222, 200006)
    AddSpecialEffect(1100223, 200006)
    AddSpecialEffect(1100224, 200006)
    AddSpecialEffect(1100300, 200006)
    AddSpecialEffect(1100301, 200006)
    AddSpecialEffect(1100302, 200006)
    AddSpecialEffect(1100303, 200006)
    AddSpecialEffect(1100225, 200006)
    AddSpecialEffect(1100226, 200006)
    AddSpecialEffect(1100227, 200006)
    AddSpecialEffect(1100228, 200006)
    AddSpecialEffect(1100229, 200006)
    AddSpecialEffect(1100230, 200006)
    AddSpecialEffect(1100231, 200006)
    AddSpecialEffect(1100232, 200006)
    AddSpecialEffect(1100233, 200006)
    AddSpecialEffect(1100234, 200006)
    AddSpecialEffect(1100235, 200006)
    AddSpecialEffect(1100236, 200006)
    AddSpecialEffect(1100237, 200006)
    AddSpecialEffect(1100238, 200006)
    AddSpecialEffect(1100100, 200006)
    AddSpecialEffect(1100101, 200006)
    AddSpecialEffect(1100102, 200006)
    AddSpecialEffect(1100104, 200006)
    AddSpecialEffect(1100105, 200006)
    AddSpecialEffect(1100130, 200006)
    AddSpecialEffect(1100132, 200006)
    AddSpecialEffect(1100135, 200006)
    AddSpecialEffect(1100136, 200006)
    AddSpecialEffect(1100137, 200006)
    AddSpecialEffect(1100138, 200006)
    AddSpecialEffect(1100400, 200006)
    AddSpecialEffect(1100401, 200006)
    AddSpecialEffect(1100402, 200006)
    AddSpecialEffect(1100403, 200006)
    AddSpecialEffect(1100404, 200006)
    AddSpecialEffect(1100239, 200006)
    AddSpecialEffect(1100240, 200006)
    AddSpecialEffect(1100241, 200006)
    AddSpecialEffect(1100242, 200006)
    AddSpecialEffect(1100243, 200006)
    AddSpecialEffect(1100244, 200006)
    AddSpecialEffect(1100180, 200006)
    AddSpecialEffect(1100160, 200006)
    AddSpecialEffect(1100161, 200006)
    AddSpecialEffect(1100200, 200006)
    AddSpecialEffect(1100201, 200006)
    AddSpecialEffect(1100202, 200006)
    AddSpecialEffect(1100203, 200006)
    AddSpecialEffect(1100204, 200006)
    AddSpecialEffect(1100205, 200006)
    AddSpecialEffect(1100206, 200006)
    AddSpecialEffect(1100207, 200006)
    AddSpecialEffect(1100208, 200006)
    AddSpecialEffect(1100209, 200006)
    AddSpecialEffect(1100210, 200006)
    AddSpecialEffect(1100211, 200006)
    AddSpecialEffect(1100212, 200006)
    AddSpecialEffect(1100213, 200006)
    AddSpecialEffect(1100245, 200006)
    AddSpecialEffect(1100246, 200006)
    AddSpecialEffect(1100247, 200006)
    AddSpecialEffect(1100248, 200006)
    AddSpecialEffect(1100249, 200006)
    AddSpecialEffect(1100250, 200006)
    AddSpecialEffect(1100251, 200006)
    AddSpecialEffect(1100252, 200006)
    AddSpecialEffect(1100253, 200006)
    AddSpecialEffect(1100254, 200006)
    AddSpecialEffect(1100255, 200006)
    AddSpecialEffect(1100900, 200006)
    AddSpecialEffect(1100901, 200006)
    AddSpecialEffect(1100902, 200006)
    AddSpecialEffect(1100903, 200006)
    AddSpecialEffect(1100904, 200006)
    AddSpecialEffect(1100905, 200006)
    AddSpecialEffect(1100906, 200006)
    AddSpecialEffect(1100256, 200006)
    AddSpecialEffect(1100257, 200006)
    AddSpecialEffect(1100258, 200006)
    AddSpecialEffect(1100259, 200006)
    AddSpecialEffect(1100260, 200006)
    AddSpecialEffect(1100261, 200006)
    AddSpecialEffect(1100262, 200006)
    AddSpecialEffect(1100263, 200006)
    AddSpecialEffect(1100264, 200006)
    AddSpecialEffect(1100907, 200006)
    AddSpecialEffect(1100908, 200006)
    AddSpecialEffect(1100909, 200006)
    AddSpecialEffect(1100910, 200006)
    AddSpecialEffect(1100911, 200006)
    AddSpecialEffect(1100170, 200006)
    AddSpecialEffect(1100171, 200006)
    AddSpecialEffect(1100172, 200006)
    AddSpecialEffect(1103900, 200006)
    AddSpecialEffect(1103910, 200006)
    AddSpecialEffect(1103902, 200006)
    AddSpecialEffect(1103901, 200006)
    AddSpecialEffect(1103911, 200006)
    AddSpecialEffect(1103912, 200006)
    WaitFrames(10)  # give other loaded maps time to trigger
    DisableFlag(TriggerFlags.EnemyMaxHealthDown)
    return RESTART


@RestartOnRest
def EnemyDefenseUp():
    """ 11102207: Temporary enemy effect. """
    Await(TriggerFlags.EnemyDefenseUp)
    AddSpecialEffect(6312, 200007)
    AddSpecialEffect(6422, 200007)
    AddSpecialEffect(6570, 200007)
    AddSpecialEffect(1100960, 200007)
    AddSpecialEffect(1100214, 200007)
    AddSpecialEffect(1100215, 200007)
    AddSpecialEffect(1100216, 200007)
    AddSpecialEffect(1100217, 200007)
    AddSpecialEffect(1100218, 200007)
    AddSpecialEffect(1100219, 200007)
    AddSpecialEffect(1100220, 200007)
    AddSpecialEffect(1100221, 200007)
    AddSpecialEffect(1100222, 200007)
    AddSpecialEffect(1100223, 200007)
    AddSpecialEffect(1100224, 200007)
    AddSpecialEffect(1100300, 200007)
    AddSpecialEffect(1100301, 200007)
    AddSpecialEffect(1100302, 200007)
    AddSpecialEffect(1100303, 200007)
    AddSpecialEffect(1100225, 200007)
    AddSpecialEffect(1100226, 200007)
    AddSpecialEffect(1100227, 200007)
    AddSpecialEffect(1100228, 200007)
    AddSpecialEffect(1100229, 200007)
    AddSpecialEffect(1100230, 200007)
    AddSpecialEffect(1100231, 200007)
    AddSpecialEffect(1100232, 200007)
    AddSpecialEffect(1100233, 200007)
    AddSpecialEffect(1100234, 200007)
    AddSpecialEffect(1100235, 200007)
    AddSpecialEffect(1100236, 200007)
    AddSpecialEffect(1100237, 200007)
    AddSpecialEffect(1100238, 200007)
    AddSpecialEffect(1100100, 200007)
    AddSpecialEffect(1100101, 200007)
    AddSpecialEffect(1100102, 200007)
    AddSpecialEffect(1100104, 200007)
    AddSpecialEffect(1100105, 200007)
    AddSpecialEffect(1100130, 200007)
    AddSpecialEffect(1100132, 200007)
    AddSpecialEffect(1100135, 200007)
    AddSpecialEffect(1100136, 200007)
    AddSpecialEffect(1100137, 200007)
    AddSpecialEffect(1100138, 200007)
    AddSpecialEffect(1100400, 200007)
    AddSpecialEffect(1100401, 200007)
    AddSpecialEffect(1100402, 200007)
    AddSpecialEffect(1100403, 200007)
    AddSpecialEffect(1100404, 200007)
    AddSpecialEffect(1100239, 200007)
    AddSpecialEffect(1100240, 200007)
    AddSpecialEffect(1100241, 200007)
    AddSpecialEffect(1100242, 200007)
    AddSpecialEffect(1100243, 200007)
    AddSpecialEffect(1100244, 200007)
    AddSpecialEffect(1100180, 200007)
    AddSpecialEffect(1100160, 200007)
    AddSpecialEffect(1100161, 200007)
    AddSpecialEffect(1100200, 200007)
    AddSpecialEffect(1100201, 200007)
    AddSpecialEffect(1100202, 200007)
    AddSpecialEffect(1100203, 200007)
    AddSpecialEffect(1100204, 200007)
    AddSpecialEffect(1100205, 200007)
    AddSpecialEffect(1100206, 200007)
    AddSpecialEffect(1100207, 200007)
    AddSpecialEffect(1100208, 200007)
    AddSpecialEffect(1100209, 200007)
    AddSpecialEffect(1100210, 200007)
    AddSpecialEffect(1100211, 200007)
    AddSpecialEffect(1100212, 200007)
    AddSpecialEffect(1100213, 200007)
    AddSpecialEffect(1100245, 200007)
    AddSpecialEffect(1100246, 200007)
    AddSpecialEffect(1100247, 200007)
    AddSpecialEffect(1100248, 200007)
    AddSpecialEffect(1100249, 200007)
    AddSpecialEffect(1100250, 200007)
    AddSpecialEffect(1100251, 200007)
    AddSpecialEffect(1100252, 200007)
    AddSpecialEffect(1100253, 200007)
    AddSpecialEffect(1100254, 200007)
    AddSpecialEffect(1100255, 200007)
    AddSpecialEffect(1100900, 200007)
    AddSpecialEffect(1100901, 200007)
    AddSpecialEffect(1100902, 200007)
    AddSpecialEffect(1100903, 200007)
    AddSpecialEffect(1100904, 200007)
    AddSpecialEffect(1100905, 200007)
    AddSpecialEffect(1100906, 200007)
    AddSpecialEffect(1100256, 200007)
    AddSpecialEffect(1100257, 200007)
    AddSpecialEffect(1100258, 200007)
    AddSpecialEffect(1100259, 200007)
    AddSpecialEffect(1100260, 200007)
    AddSpecialEffect(1100261, 200007)
    AddSpecialEffect(1100262, 200007)
    AddSpecialEffect(1100263, 200007)
    AddSpecialEffect(1100264, 200007)
    AddSpecialEffect(1100907, 200007)
    AddSpecialEffect(1100908, 200007)
    AddSpecialEffect(1100909, 200007)
    AddSpecialEffect(1100910, 200007)
    AddSpecialEffect(1100911, 200007)
    AddSpecialEffect(1100170, 200007)
    AddSpecialEffect(1100171, 200007)
    AddSpecialEffect(1100172, 200007)
    AddSpecialEffect(1103900, 200007)
    AddSpecialEffect(1103910, 200007)
    AddSpecialEffect(1103902, 200007)
    AddSpecialEffect(1103901, 200007)
    AddSpecialEffect(1103911, 200007)
    AddSpecialEffect(1103912, 200007)
    WaitFrames(10)  # give other loaded maps time to trigger
    DisableFlag(TriggerFlags.EnemyDefenseUp)
    return RESTART
