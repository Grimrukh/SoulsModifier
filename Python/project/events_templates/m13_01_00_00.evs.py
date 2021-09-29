"""
linked:


strings:

"""
from soulstruct.darksouls1r.events import *
from ..entities.m13_01_00_00_entities import *
from ..entities.m13_00_00_00_entities import Boxes as m13_00_Boxes
from ..entities.common_entities import *


def Constructor():
    """ 0: Event 0 """
    SkipLinesIfFlagOff(1, 7)
    RegisterBonfire(
        11310920,
        obj=Objects.o0200_0001,
        reaction_distance=2.0,
        reaction_angle=180.0,
        initial_kindle_level=0,
    )
    RegisterBonfire(
        11310992,
        obj=Objects.o0200_0000,
        reaction_distance=2.0,
        reaction_angle=180.0,
        initial_kindle_level=0,
    )
    RegisterBonfire(
        11310984,
        obj=Objects.o0200_0002,
        reaction_distance=2.0,
        reaction_angle=180.0,
        initial_kindle_level=0,
    )
    RegisterLadder(start_climbing_flag=11310010, stop_climbing_flag=11310011, obj=Objects.o3043_0000)
    RegisterLadder(start_climbing_flag=11310012, stop_climbing_flag=11310013, obj=Objects.o3044_0000)
    RegisterLadder(start_climbing_flag=11310014, stop_climbing_flag=11310015, obj=Objects.o3140_0000)
    RegisterLadder(start_climbing_flag=11310016, stop_climbing_flag=11310017, obj=Objects.o3140_0001)
    RegisterLadder(start_climbing_flag=11310018, stop_climbing_flag=11310019, obj=Objects.o3141_0000)
    RegisterLadder(start_climbing_flag=11310020, stop_climbing_flag=11310021, obj=Objects.o3142_0000)
    RegisterLadder(start_climbing_flag=11310022, stop_climbing_flag=11310023, obj=Objects.o3143_0001)
    RegisterLadder(start_climbing_flag=11310024, stop_climbing_flag=11310025, obj=Objects.o3144_0000)
    RegisterLadder(start_climbing_flag=11310026, stop_climbing_flag=11310027, obj=Objects.o3143_0000)
    SkipLinesIfClient(2)
    EnableFlag(401)
    DisableFlag(11310000)
    IfClient(1)
    IfInsideMap(1, game_map=TOMB_OF_THE_GIANTS)
    SkipLinesIfConditionTrue(2, 1)
    DisableObject(Objects.o3961_0000)
    DeleteVFX(VFX.MultiplayerFog1, erase_root_only=False)
    SkipLinesIfFlagOn(2, 11310810)
    DisableTreasure(Objects.o0500_0024)
    DisableObject(Objects.o0500_0024)
    SkipLinesIfFlagOff(1, 11310810)
    EnableTreasure(Objects.o0500_0024)
    RunEvent(
        11310090,
        slot=0,
        args=(Objects.o3962_0000, VFX.CheckpointFog1, Boxes.CheckpointFog1FrontSide, Boxes.CheckpointFog1BackSide),
    )
    RunEvent(11310095)
    RunEvent(11315100)
    RunEvent(11310051)
    RunEvent(11310052)
    RunEvent(11310053)
    RunEvent(11310054)
    RunEvent(11310100)
    RunEvent(11315080)
    RunEvent(11315050, slot=0, args=(Characters.c2960_0012, Characters.c2960_0012, 0.0), arg_types="iif")
    RunEvent(11315050, slot=1, args=(Characters.c2960_0013, Characters.c2960_0014, 0.0), arg_types="iif")
    RunEvent(11315050, slot=2, args=(Characters.c2960_0014, Characters.c2960_0014, 0.0), arg_types="iif")
    RunEvent(11315060, slot=0, args=(Characters.c2960_0003, 51310100, 0.0), arg_types="iif")
    RunEvent(11315060, slot=1, args=(Characters.c2960_0004, 51310100, 0.20000000298023224), arg_types="iif")
    RunEvent(11315060, slot=2, args=(Characters.c2960_0005, 51310100, 0.8999999761581421), arg_types="iif")
    RunEvent(11315060, slot=3, args=(Characters.c2960_0006, 51310100, 1.0), arg_types="iif")
    RunEvent(11315070, slot=0, args=(Characters.c2960_0007, Boxes.BoneTowerAmbushTrigger, 0.0), arg_types="iif")
    RunEvent(
        11315070,
        slot=1,
        args=(Characters.c2960_0008, Boxes.BoneTowerAmbushTrigger, 0.20000000298023224),
        arg_types="iif",
    )
    RunEvent(
        11315070,
        slot=2,
        args=(Characters.c2960_0009, Boxes.BoneTowerAmbushTrigger, 0.4000000059604645),
        arg_types="iif",
    )
    RunEvent(
        11315070,
        slot=3,
        args=(Characters.c2960_0010, Boxes.BoneTowerAmbushTrigger, 0.6000000238418579),
        arg_types="iif",
    )
    RunEvent(
        11315070,
        slot=4,
        args=(Characters.c2960_0011, Boxes.BoneTowerAmbushTrigger, 0.800000011920929),
        arg_types="iif",
    )
    RunEvent(11310820, slot=0, args=(Characters.c2795_0000, 27903000))
    RunEvent(11310820, slot=1, args=(Characters.c3300_0000, 33005000))
    DisableSoundEvent(1313800)
    SkipLinesIfFlagOff(4, 7)
    RunEvent(11315392)
    DisableObject(Objects.o3964_0000)
    DeleteVFX(VFX.BossEntranceFog, erase_root_only=False)
    SkipLines(13)
    RunEvent(11315390)
    RunEvent(11315391)
    RunEvent(11315393)
    RunEvent(11315392)
    RunEvent(11310001)
    RunEvent(11315394)
    RunEvent(11315395)
    RunEvent(11315396)
    RunEvent(11315398)
    RunEvent(11314398)
    RunEvent(11315350, slot=0, args=(Characters.c2900_0000,))
    RunEvent(11315350, slot=1, args=(Characters.c2900_0001,))
    RunEvent(11315350, slot=2, args=(Characters.c2900_0002,))
    RunEvent(11315350, slot=3, args=(Characters.c2910_0021,))
    RunEvent(11315350, slot=4, args=(Characters.c2910_0020,))
    RunEvent(11315350, slot=5, args=(Characters.c2910_0019,))
    RunEvent(11315843, slot=0, args=(7, Objects.o3964_0000, Boxes.NitoFogPrompt, Boxes.NitoFogRotationTarget))
    RunEvent(11315846, slot=0, args=(7, Objects.o3964_0000, VFX.BossEntranceFog))
    # <!--!>


def Preconstructor():
    """ 50: Event 50 """
    HumanityRegistration(Characters.c0000_0007, 8948)
    RunEvent(11315030)
    RunEvent(11310810)
    HumanityRegistration(Characters.c0000_0002, 8358)
    SkipLinesIfFlagOn(2, 1174)
    SkipLinesIfFlagOn(1, 1173)
    DisableCharacter(Characters.c0000_0002)
    RunEvent(11310502, slot=0, args=(Characters.c0000_0002, 1176))
    RunEvent(11310503, slot=0, args=(Characters.c0000_0002, 1179))
    RunEvent(11310533, slot=0, args=(Characters.c0000_0002, 1170, 1181, 1177))
    RunEvent(11310534, slot=0, args=(Characters.c0000_0002, 1170, 1181, 1180))
    RunEvent(11310530)
    RunEvent(11310531, slot=0, args=(Characters.c0000_0002, 1170, 1181, 1174))
    RunEvent(11310532, slot=0, args=(Characters.c0000_0002, 1170, 1181, 1175))
    SkipLinesIfFlagOn(1, 1216)
    DisableCharacter(Characters.c0000_0003)
    SetTeamType(Characters.c0000_0003, TeamType.HostileAlly)
    RunEvent(11310520, slot=1, args=(Characters.c0000_0003, 1210, 1219, 1214))
    SkipLinesIfFlagOn(1, 1226)
    DisableCharacter(Characters.c0000_0004)
    SetTeamType(Characters.c0000_0004, TeamType.HostileAlly)
    RunEvent(11310520, slot=2, args=(Characters.c0000_0004, 1220, 1229, 1224))
    HumanityRegistration(Characters.c0000_0005, 8478)
    SkipLinesIfFlagRangeAnyOn(1, (1623, 1625))
    DisableCharacter(Characters.c0000_0005)
    RunEvent(11310501, slot=0, args=(Characters.c0000_0005, 1627))
    RunEvent(11310543, slot=0, args=(Characters.c0000_0005, 1625))
    RunEvent(11310542, slot=0, args=(Characters.c0000_0005, 1628))
    RunEvent(11310540, slot=0, args=(Characters.c0000_0005, 1620, 1631, 1623))
    RunEvent(11310541, slot=0, args=(Characters.c0000_0005, 1620, 1631, 1624))
    RunEvent(11310002)


def Event11310090(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11310090: Event 11310090 """
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


def Event11310095():
    """ 11310095: Event 11310095 """
    SkipLinesIfFlagOff(5, 11800100)
    EnableFlag(11310096)
    DisableObject(Objects.o3963_0000)
    DeleteVFX(VFX.GoldenFog, erase_root_only=False)
    DisableFlag(401)
    End()
    SkipLinesIfFlagOff(3, 11310096)
    DisableObject(Objects.o3963_0000)
    DeleteVFX(VFX.GoldenFog, erase_root_only=False)
    End()
    EndIfClient()
    IfActionButton(
        0,
        prompt_text=10010410,
        anchor_entity=Boxes.AtGoldenFog,
        anchor_type=CoordEntityType.Region,
        model_point=0,
        line_intersects=Objects.o3963_0000,
    )
    DisplayStatus(10010630, pad_enabled=True)
    Restart()


def Event11315390():
    """ 11315390: Event 11315390 """
    IfFlagOff(1, 7)
    IfCharacterAlive(1, Characters.c5220_0000)
    IfActionButton(
        1,
        prompt_text=10010403,
        anchor_entity=Boxes.NitoFogPrompt,
        anchor_type=CoordEntityType.Region,
        line_intersects=Objects.o3964_0000,
        boss_version=True,
    )
    IfConditionTrue(0, input_condition=1)
    RotateToFaceEntity(PLAYER, Boxes.NitoFogRotationTarget)
    ForceAnimation(PLAYER, 7410)
    Restart()


def Event11315391():
    """ 11315391: Event 11315391 """
    IfFlagOff(1, 7)
    IfFlagOn(1, 11315393)
    IfCharacterType(1, PLAYER, CharacterType.WhitePhantom)
    IfActionButton(
        1,
        prompt_text=10010403,
        anchor_entity=Boxes.NitoFogPrompt,
        anchor_type=CoordEntityType.Region,
        trigger_attribute=TriggerAttribute.All,
        line_intersects=Objects.o3964_0000,
    )
    IfConditionTrue(0, input_condition=1)
    RotateToFaceEntity(PLAYER, Boxes.NitoFogRotationTarget)
    ForceAnimation(PLAYER, 7410)
    Restart()


def Event11315393():
    """ 11315393: Event 11315393 """
    SkipLinesIfThisEventOn(3)
    IfFlagOff(1, 7)
    IfFlagOn(1, 11315390)
    IfConditionTrue(0, input_condition=1)
    SkipLinesIfClient(1)
    NotifyBossBattleStart()
    ActivateMultiplayerBuffs(Characters.c5220_0000)
    DisableFlag(11310050)


@RestartOnRest
def Event11315392():
    """ 11315392: Event 11315392 """
    SkipLinesIfFlagOff(17, 7)
    DisableCharacter(Characters.c5220_0000)
    Kill(Characters.c5220_0000, award_souls=False)
    DisableCharacter(Characters.c5220_0001)
    Kill(Characters.c5220_0001, award_souls=False)
    DisableCharacter(Characters.c2900_0000)
    DisableCharacter(Characters.c2900_0001)
    DisableCharacter(Characters.c2900_0002)
    DisableCharacter(Characters.c2910_0021)
    DisableCharacter(Characters.c2910_0020)
    DisableCharacter(Characters.c2910_0019)
    Kill(Characters.c2900_0000, award_souls=False)
    Kill(Characters.c2900_0001, award_souls=False)
    Kill(Characters.c2900_0002, award_souls=False)
    Kill(Characters.c2910_0021, award_souls=False)
    Kill(Characters.c2910_0020, award_souls=False)
    Kill(Characters.c2910_0019, award_souls=False)
    End()
    SkipLinesIfThisEventOn(1)
    SkipLinesIfFlagOn(1, 11310000)
    DisableCharacter(Characters.c5220_0000)
    DisableAI(Characters.c5220_0000)
    SetStandbyAnimationSettings(Characters.c2900_0000, standby_animation=9001)
    SetStandbyAnimationSettings(Characters.c2900_0001, standby_animation=9001)
    SetStandbyAnimationSettings(Characters.c2900_0002, standby_animation=9001)
    SetStandbyAnimationSettings(Characters.c2910_0021, standby_animation=9001)
    SetStandbyAnimationSettings(Characters.c2910_0020, standby_animation=9001)
    SetStandbyAnimationSettings(Characters.c2910_0019, standby_animation=9001)
    IfHost(1)
    IfFlagOff(1, 11310050)
    IfCharacterInsideRegion(1, PLAYER, region=Boxes.NitoCutsceneTrigger)
    IfConditionTrue(0, input_condition=1)
    DisableCharacter(Characters.c5220_0001)
    SkipLinesIfFlagOn(7, 11310000)
    SkipLinesIfMultiplayer(2)
    PlayCutscene(130100, skippable=True, fade_out=False, player_id=PLAYER)
    SkipLines(1)
    PlayCutscene(130100, skippable=False, fade_out=False, player_id=PLAYER)
    WaitFrames(1)
    EnableCharacter(Characters.c5220_0000)
    EnableFlag(11310000)
    EnableAI(Characters.c5220_0000)
    EnableBossHealthBar(Characters.c5220_0000, name=5220, slot=0)
    EnableFlag(11315392)
    DisableNetworkSync()
    ResetStandbyAnimationSettings(Characters.c2900_0000)
    ForceAnimation(Characters.c2900_0000, 9061)
    Wait(0.30000001192092896)
    SetStandbyAnimationSettings(Characters.c2900_0001, cancel_animation=9061)
    ForceAnimation(Characters.c2900_0001, 9061)
    Wait(0.5)
    SetStandbyAnimationSettings(Characters.c2900_0002, cancel_animation=9061)
    ForceAnimation(Characters.c2900_0002, 9061)
    Wait(0.20000000298023224)
    SetStandbyAnimationSettings(Characters.c2910_0021, cancel_animation=9061)
    ForceAnimation(Characters.c2910_0021, 9061)
    Wait(0.30000001192092896)
    SetStandbyAnimationSettings(Characters.c2910_0020, cancel_animation=9061)
    ForceAnimation(Characters.c2910_0020, 9061)
    Wait(0.699999988079071)
    SetStandbyAnimationSettings(Characters.c2910_0019, cancel_animation=9061)
    ForceAnimation(Characters.c2910_0019, 9061)


def Event11310001():
    """ 11310001: Event 11310001 """
    DisableObject(Objects.o0200_0001)
    IfCharacterDead(0, Characters.c5220_0000)
    EnableFlag(7)
    KillBoss(1310800)
    SkipLinesIfClient(1)
    AwardAchievement(35)
    DisableObject(Objects.o3964_0000)
    DeleteVFX(VFX.BossEntranceFog, erase_root_only=True)
    Kill(Characters.c5220_0001, award_souls=False)
    CreateTemporaryVFX(90014, anchor_entity=Objects.o0200_0001, anchor_type=CoordEntityType.Object, model_point=-1)
    Wait(2.0)
    EnableObject(Objects.o0200_0001)
    RegisterBonfire(
        11310920,
        obj=Objects.o0200_0001,
        reaction_distance=2.0,
        reaction_angle=180.0,
        initial_kindle_level=0,
    )


def Event11315394():
    """ 11315394: Event 11315394 """
    DisableNetworkSync()
    IfFlagOff(1, 7)
    IfFlagOn(1, 11315392)
    SkipLinesIfHost(1)
    IfFlagOn(1, 11315391)
    IfConditionTrue(0, input_condition=1)
    EnableSoundEvent(1313800)


def Event11315395():
    """ 11315395: Event 11315395 """
    DisableNetworkSync()
    IfFlagOn(1, 7)
    IfFlagOn(1, 11315394)
    IfConditionTrue(0, input_condition=1)
    DisableSoundEvent(1313800)


def Event11315396():
    """ 11315396: Event 11315396 """
    IfHealthLessThanOrEqual(0, Characters.c5220_0000, 0.0)
    SkipLinesIfFlagOff(7, 11315370)
    Kill(1310110, award_souls=False)
    Kill(1310111, award_souls=False)
    Kill(1310112, award_souls=False)
    Kill(1310113, award_souls=False)
    Kill(1310114, award_souls=False)
    Kill(1310115, award_souls=False)
    End()
    SkipLinesIfFlagOff(7, 11315371)
    Kill(1310110, award_souls=True)
    Kill(1310111, award_souls=True)
    Kill(1310112, award_souls=False)
    Kill(1310113, award_souls=False)
    Kill(1310114, award_souls=False)
    Kill(1310115, award_souls=False)
    End()
    SkipLinesIfFlagOff(7, 11315372)
    Kill(1310110, award_souls=True)
    Kill(1310111, award_souls=True)
    Kill(1310112, award_souls=True)
    Kill(1310113, award_souls=True)
    Kill(1310114, award_souls=False)
    Kill(1310115, award_souls=False)
    End()
    Kill(1310110, award_souls=True)
    Kill(1310111, award_souls=True)
    Kill(1310112, award_souls=True)
    Kill(1310113, award_souls=True)
    Kill(1310114, award_souls=True)
    Kill(1310115, award_souls=True)


@RestartOnRest
def Event11315397():
    """ 11315397: Event 11315397 """
    DisableObject(Objects.o3900_0000)
    DisableObject(Objects.o3901_0000)
    DisableObject(Objects.o3900_0001)
    DisableCharacter(1310110)
    DisableCharacter(1310111)
    DisableCharacter(1310112)
    DisableCharacter(1310113)
    DisableCharacter(1310114)
    DisableCharacter(1310115)
    RunEvent(
        11315370,
        slot=0,
        args=(11315392, 2, 0, 5220, 5220, Objects.o3900_0000, 1310110, 1310113),
        arg_types="ihhiiiii",
    )
    RunEvent(
        11315370,
        slot=1,
        args=(11315370, 3, 0, 5221, 5221, Objects.o3901_0000, 1310111, 1310114),
        arg_types="ihhiiiii",
    )
    RunEvent(
        11315370,
        slot=2,
        args=(11315371, 4, 0, 5222, 5222, Objects.o3900_0001, 1310112, 1310115),
        arg_types="ihhiiiii",
    )
    IfCharacterBackreadEnabled(0, Characters.c5220_0000)
    SetDisplayMask(Characters.c5220_0000, bit_index=0, switch_type=OnOffChange.On)


@RestartOnRest
def Event11315398():
    """ 11315398: Event 11315398 """
    DisableNetworkSync()
    IfFlagOn(1, 11315390)
    IfCharacterTargeting(1, Characters.c5220_0000, PLAYER)
    IfHasTAEEvent(1, Characters.c5220_0000, tae_event_id=700)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(11313398)
    IfHasTAEEvent(0, Characters.c5220_0000, tae_event_id=710)
    EnableFlag(11313399)
    Restart()


@RestartOnRest
def Event11314398():
    """ 11314398: Event 11314398 """
    IfFlagOn(0, 11313398)
    MoveObjectToCharacter(Objects.o0020_0000, character=PLAYER, model_point=-1)
    DisableFlag(11313398)
    IfFlagOn(0, 11313399)
    CreateHazard(
        11315399,
        Objects.o0020_0000,
        model_point=1,
        behavior_param_id=11300,
        target_type=DamageTargetType.Character,
        radius=0.30000001192092896,
        life=0.30000001192092896,
        repetition_time=0.0,
    )
    CreateTemporaryVFX(15224, anchor_entity=Objects.o0020_0000, anchor_type=CoordEntityType.Object, model_point=-1)
    DisableFlag(11313399)
    Restart()


@UnknownRestart
def Event11315370(
    _,
    arg_0_3: int,
    arg_4_5: short,
    arg_6_7: short,
    arg_8_11: int,
    arg_12_15: int,
    arg_16_19: int,
    arg_20_23: int,
    arg_24_27: int,
):
    """ 11315370: Event 11315370 """
    IfFlagOn(0, arg_0_3)
    CreateNPCPart(
        Characters.c5220_0000,
        npc_part_id=arg_6_7,
        part_index=arg_4_5,
        part_health=200,
        damage_correction=1.0,
        body_damage_correction=1.0,
        is_invincible=False,
        start_in_stop_state=False,
    )
    IfHealthGreaterThan(1, Characters.c5220_0000, 0.0)
    IfCharacterPartHealthLessThanOrEqual(1, Characters.c5220_0000, npc_part_id=arg_8_11, value=0)
    IfHealthLessThanOrEqual(2, Characters.c5220_0000, 0.0)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(2)
    SkipLinesIfFlagOn(5, 11315370)
    SetCollisionMask(Characters.c5220_0000, bit_index=1, switch_type=OnOffChange.Off)
    SetDisplayMask(Characters.c5220_0000, bit_index=1, switch_type=OnOffChange.On)
    SetDisplayMask(Characters.c5220_0000, bit_index=4, switch_type=OnOffChange.On)
    SetDisplayMask(Characters.c5220_0000, bit_index=7, switch_type=OnOffChange.On)
    SkipLines(10)
    SkipLinesIfFlagOn(5, 11315371)
    SetCollisionMask(Characters.c5220_0000, bit_index=2, switch_type=OnOffChange.Off)
    SetDisplayMask(Characters.c5220_0000, bit_index=2, switch_type=OnOffChange.On)
    SetDisplayMask(Characters.c5220_0000, bit_index=5, switch_type=OnOffChange.On)
    SetDisplayMask(Characters.c5220_0000, bit_index=8, switch_type=OnOffChange.On)
    SkipLines(4)
    SetCollisionMask(Characters.c5220_0000, bit_index=3, switch_type=OnOffChange.Off)
    SetDisplayMask(Characters.c5220_0000, bit_index=3, switch_type=OnOffChange.On)
    SetDisplayMask(Characters.c5220_0000, bit_index=6, switch_type=OnOffChange.On)
    SetDisplayMask(Characters.c5220_0000, bit_index=9, switch_type=OnOffChange.On)
    EnableObject(arg_12_15)
    MoveObjectToCharacter(arg_12_15, character=Characters.c5220_0000, model_point=50)
    DestroyObject(arg_12_15)
    EnableCharacter(arg_16_19)
    Move(
        arg_16_19,
        destination=Characters.c5220_0000,
        destination_type=CoordEntityType.Character,
        model_point=50,
        copy_draw_parent=Characters.c5220_0000,
    )
    ForceAnimation(arg_16_19, 7000)
    EnableCharacter(arg_20_23)
    Move(
        arg_20_23,
        destination=Characters.c5220_0000,
        destination_type=CoordEntityType.Character,
        model_point=51,
        copy_draw_parent=Characters.c5220_0000,
    )
    ForceAnimation(arg_20_23, 7000)
    ForceAnimation(Characters.c5220_0000, arg_24_27, wait_for_completion=True)


@RestartOnRest
def Event11315350(_, arg_0_3: int):
    """ 11315350: Event 11315350 """
    EndIfFlagOn(7)
    EndIfThisEventSlotOn()
    EnableImmortality(arg_0_3)
    IfHealthLessThanOrEqual(0, Characters.c5220_0000, 0.0)
    CancelSpecialEffect(arg_0_3, 5451)
    DisableImmortality(arg_0_3)
    Kill(arg_0_3, award_souls=True)


@RestartOnRest
def Event11315100():
    """ 11315100: Event 11315100 """
    RunEvent(11315091)
    RunEvent(11315092)
    RunEvent(11315150, slot=0, args=(11315100, VFX.ColoredLight00, 11315101))
    RunEvent(11315150, slot=1, args=(11315101, VFX.ColoredLight01, 11315102))
    RunEvent(11315150, slot=2, args=(11315102, VFX.ColoredLight02, 11315103))
    RunEvent(11315150, slot=3, args=(11315103, VFX.ColoredLight03, 11315104))
    RunEvent(11315150, slot=4, args=(11315104, VFX.ColoredLight04, 11315105))
    RunEvent(11315150, slot=5, args=(11315105, VFX.ColoredLight05, 11315106))
    RunEvent(11315150, slot=6, args=(11315106, VFX.ColoredLight06, 11315107))
    RunEvent(11315150, slot=7, args=(11315107, VFX.ColoredLight07, 11315108))
    RunEvent(11315150, slot=8, args=(11315108, VFX.ColoredLight08, 11315109))
    RunEvent(11315150, slot=9, args=(11315109, VFX.ColoredLight09, 11315110))
    RunEvent(11315150, slot=10, args=(11315110, VFX.ColoredLight10, 11315111))
    RunEvent(11315150, slot=11, args=(11315111, VFX.ColoredLight11, 11315112))
    RunEvent(11315150, slot=12, args=(11315112, VFX.ColoredLight12, 11315113))
    RunEvent(11315150, slot=13, args=(11315113, VFX.ColoredLight13, 11315114))
    RunEvent(11315150, slot=14, args=(11315114, VFX.ColoredLight14, 11315115))
    RunEvent(11315150, slot=15, args=(11315115, VFX.ColoredLight15, 11315116))
    RunEvent(11315150, slot=16, args=(11315116, VFX.ColoredLight16, 11315117))
    RunEvent(11315150, slot=17, args=(11315117, VFX.ColoredLight17, 11315118))
    RunEvent(11315150, slot=18, args=(11315118, VFX.ColoredLight18, 11315119))
    RunEvent(11315150, slot=19, args=(11315119, VFX.ColoredLight19, 11315120))
    RunEvent(11315150, slot=20, args=(11315120, VFX.ColoredLight20, 11315121))
    RunEvent(11315150, slot=21, args=(11315121, VFX.ColoredLight21, 11315122))
    RunEvent(11315150, slot=22, args=(11315122, VFX.ColoredLight22, 11315123))
    RunEvent(11315150, slot=23, args=(11315123, VFX.ColoredLight23, 11315124))
    RunEvent(11315150, slot=24, args=(11315100, VFX.ColoredLight24, 11315125))
    RunEvent(11315150, slot=25, args=(11315125, VFX.ColoredLight25, 11315126))
    RunEvent(11315150, slot=26, args=(11315126, VFX.ColoredLight26, 11315127))
    RunEvent(11315150, slot=27, args=(11315127, VFX.ColoredLight27, 11315128))
    RunEvent(11315150, slot=28, args=(11315128, VFX.ColoredLight28, 11315129))
    RunEvent(11315150, slot=29, args=(11315129, VFX.ColoredLight29, 11315130))
    RunEvent(11315150, slot=30, args=(11315130, VFX.ColoredLight30, 11315131))
    RunEvent(11315150, slot=31, args=(11315131, VFX.ColoredLight31, 11315132))
    RunEvent(11315150, slot=32, args=(11315132, VFX.ColoredLight32, 11315133))
    RunEvent(11315150, slot=33, args=(11315133, VFX.ColoredLight33, 11315134))
    RunEvent(11315150, slot=34, args=(11315134, VFX.ColoredLight34, 11315135))
    RunEvent(11315150, slot=35, args=(11315135, VFX.ColoredLight35, 11315136))
    RunEvent(11315150, slot=36, args=(11315136, VFX.ColoredLight36, 11315137))
    RunEvent(11315150, slot=37, args=(11315137, VFX.ColoredLight37, 11315138))
    RunEvent(11315150, slot=38, args=(11315138, VFX.ColoredLight38, 11315139))
    RunEvent(11315150, slot=39, args=(11315139, VFX.ColoredLight39, 11315140))
    RunEvent(11315150, slot=40, args=(11315140, VFX.ColoredLight40, 11315141))
    RunEvent(11315150, slot=41, args=(11315141, VFX.ColoredLight41, 11315142))
    RunEvent(11315150, slot=42, args=(11315142, VFX.ColoredLight42, 11315143))
    RunEvent(11315150, slot=43, args=(11315143, VFX.ColoredLight43, 11315144))
    RunEvent(11315150, slot=44, args=(11315144, VFX.ColoredLight44, 11315145))
    RunEvent(11315150, slot=45, args=(11315145, VFX.ColoredLight45, 11315146))
    RunEvent(11315150, slot=46, args=(11315146, VFX.ColoredLight46, 11315147))
    RunEvent(11315150, slot=47, args=(11315147, VFX.ColoredLight47, 11315148))
    RunEvent(11315150, slot=48, args=(11315148, VFX.ColoredLight48, 11315149))


@UnknownRestart
def Event11315150(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 11315150: Event 11315150 """
    DisableNetworkSync()
    SkipLinesIfFlagOn(4, 11315090)
    DeleteVFX(arg_4_7, erase_root_only=False)
    IfFlagOn(1, 11315090)
    IfFlagOn(1, arg_0_3)
    IfConditionTrue(0, input_condition=1)
    CreateVFX(arg_4_7)
    EnableFlag(arg_8_11)
    IfFlagOff(0, 11315090)
    DeleteVFX(arg_4_7, erase_root_only=True)
    DisableFlag(arg_8_11)
    Restart()


@UnknownRestart
def Event11315091():
    """ 11315091: Event 11315091 """
    IfSkullLanternActive(1)
    IfTimeElapsed(1, 2.0)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(11315090)
    RestartEvent(11315092)
    Restart()


@UnknownRestart
def Event11315092():
    """ 11315092: Event 11315092 """
    DisableNetworkSync()
    IfFlagOn(0, 11315090)
    Wait(3.0)
    DisableFlag(11315090)
    Restart()


@RestartOnRest
def Event11315050(_, arg_0_3: int, arg_4_7: int, arg_8_11: float):
    """ 11315050: Event 11315050 """
    SkipLinesIfThisEventSlotOff(2)
    ResetStandbyAnimationSettings(arg_0_3)
    End()
    SetStandbyAnimationSettings(arg_0_3, standby_animation=9000)
    IfEntityWithinDistance(0, arg_4_7, PLAYER, radius=5.0)
    Wait(arg_8_11)
    SetStandbyAnimationSettings(arg_0_3, cancel_animation=9060)
    ReplanAI(arg_0_3)


@RestartOnRest
def Event11315060(_, arg_0_3: int, arg_4_7: int, arg_8_11: float):
    """ 11315060: Event 11315060 """
    SkipLinesIfFlagOff(2, arg_4_7)
    ResetStandbyAnimationSettings(arg_0_3)
    End()
    SetStandbyAnimationSettings(arg_0_3, standby_animation=9000)
    IfHost(1)
    SkipLinesIfClient(1)
    IfFlagOn(1, arg_4_7)
    IfConditionTrue(0, input_condition=1)
    Wait(arg_8_11)
    SetStandbyAnimationSettings(arg_0_3, cancel_animation=9060)
    ReplanAI(arg_0_3)


@RestartOnRest
def Event11315070(_, arg_0_3: int, arg_4_7: int, arg_8_11: float):
    """ 11315070: Event 11315070 """
    SkipLinesIfFlagOff(2, arg_4_7)
    ResetStandbyAnimationSettings(arg_0_3)
    End()
    SetStandbyAnimationSettings(arg_0_3, standby_animation=9000)
    IfCharacterInsideRegion(0, PLAYER, region=arg_4_7)
    Wait(arg_8_11)
    SetStandbyAnimationSettings(arg_0_3, cancel_animation=9060)
    ReplanAI(arg_0_3)


@RestartOnRest
def Event11315080():
    """ 11315080: Event 11315080 """
    EndIfThisEventOn()
    DisableAI(Characters.c2960_0015)
    IfEntityWithinDistance(1, Characters.c2960_0015, PLAYER, radius=7.0)
    IfAttacked(2, Characters.c2960_0015, attacker=PLAYER)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EnableAI(Characters.c2960_0015)
    EndIfFinishedConditionTrue(2)
    SetStandbyAnimationSettings(Characters.c2960_0015, standby_animation=9000)
    ForceAnimation(Characters.c2960_0015, 9070, wait_for_completion=True)
    Move(
        Characters.c2960_0015,
        destination=Boxes.BoneTowerWarpPoint,
        destination_type=CoordEntityType.Region,
        short_move=True,
    )
    IfEntityWithinDistance(-1, Characters.c2910_0018, PLAYER, radius=5.0)
    IfAttacked(-1, Characters.c2910_0018, attacker=PLAYER)
    IfConditionTrue(0, input_condition=-1)
    SetStandbyAnimationSettings(Characters.c2960_0015, cancel_animation=9060)


def Event11310051():
    """ 11310051: Event 11310051 """
    DisableCharacter(Characters.c5220_0001)
    DisableObject(Objects.o3060_0000)
    DisableObjectActivation(Objects.o3060_0000, obj_act_id=-1)
    IfFlagOn(0, 11310050)
    SkipLinesIfFlagOn(1, 7)
    EnableCharacter(Characters.c5220_0001)
    EnableObject(Objects.o3060_0000)
    EnableObjectActivation(Objects.o3060_0000, obj_act_id=-1)
    DisableCharacter(Characters.c2900_0000)
    DisableCharacter(Characters.c2900_0001)
    DisableCharacter(Characters.c2900_0002)
    DisableCharacter(Characters.c2910_0021)
    DisableCharacter(Characters.c2910_0020)
    DisableCharacter(Characters.c2910_0019)
    IfFlagOff(0, 11310050)
    EnableCharacter(Characters.c2900_0000)
    EnableCharacter(Characters.c2900_0001)
    EnableCharacter(Characters.c2900_0002)
    EnableCharacter(Characters.c2910_0021)
    EnableCharacter(Characters.c2910_0020)
    EnableCharacter(Characters.c2910_0019)
    Restart()


def Event11310052():
    """ 11310052: Event 11310052 """
    IfObjectActivated(0, obj_act_id=11315340)
    SetStandbyAnimationSettings(PLAYER, standby_animation=7151, death_animation=6082)
    Wait(3.0)
    PlayCutscene(
        130121,
        skippable=True,
        fade_out=False,
        player_id=PLAYER,
        move_to_region=m13_00_Boxes.CoffinArrivalPoint,
        move_to_map=CATACOMBS,
    )
    PlayCutscene(130021, skippable=True, fade_out=False, player_id=PLAYER)
    WaitFrames(1)
    ResetStandbyAnimationSettings(PLAYER)
    EnableObjectActivation(Objects.o3060_0000, obj_act_id=-1)
    Restart()


def Event11310053():
    """ 11310053: Event 11310053 """
    IfFlagOn(0, 11315020)
    RotateToFaceEntity(PLAYER, Characters.c5220_0001)
    ForceAnimation(PLAYER, 7910, wait_for_completion=True)
    ForceAnimation(PLAYER, 7911, loop=True)
    IfFlagOff(0, 11315020)
    ResetStandbyAnimationSettings(PLAYER)
    ForceAnimation(PLAYER, 7912, wait_for_completion=True)
    Restart()


def Event11310054():
    """ 11310054: Event 11310054 """
    DisableNetworkSync()
    IfSingleplayer(1)
    IfFlagOn(1, 11310050)
    IfEntityWithinDistance(1, Objects.o3060_0000, PLAYER, radius=2.0)
    IfConditionTrue(0, input_condition=1)
    Wait(1.0)
    ResetStandbyAnimationSettings(PLAYER)
    EnableObjectActivation(Objects.o3060_0000, obj_act_id=-1)
    IfEntityBeyondDistance(0, Objects.o3060_0000, PLAYER, radius=3.0)
    Restart()


def Event11310100():
    """ 11310100: Event 11310100 """
    SkipLinesIfThisEventOff(2)
    DisableObject(Objects.o3452_0000)
    End()
    IfObjectDestroyed(0, Objects.o3452_0000)
    End()


@RestartOnRest
def Event11310820(_, arg_0_3: int, arg_4_7: int):
    """ 11310820: Event 11310820 """
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


def Event11310510(_, arg_0_3: int, arg_4_7: int):
    """ 11310510: Event 11310510 """
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


def Event11310520(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11310520: Event 11310520 """
    SkipLinesIfThisEventSlotOff(2)
    DropMandatoryTreasure(arg_0_3)
    End()
    IfHealthLessThanOrEqual(0, arg_0_3, 0.0)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)


def Event11310501(_, arg_0_3: int, arg_4_7: int):
    """ 11310501: Event 11310501 """
    IfFlagOff(1, 1625)
    IfFlagOff(1, 1627)
    IfFlagOff(1, 1628)
    IfFlagOn(-7, 1623)
    IfFlagOn(-7, 1624)
    IfConditionTrue(1, input_condition=-7)
    IfHealthLessThanOrEqual(1, arg_0_3, 0.8999999761581421)
    IfHealthGreaterThan(1, arg_0_3, 0.0)
    IfAttacked(1, arg_0_3, attacker=PLAYER)
    IfThisEventOff(1)
    IfFlagOn(2, arg_4_7)
    IfThisEventOn(2)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EnableFlag(arg_4_7)
    SetTeamTypeAndExitStandbyAnimation(arg_0_3, TeamType.HostileAlly)
    SaveRequest()
    EnableCharacter(arg_0_3)


def Event11310502(_, arg_0_3: int, arg_4_7: int):
    """ 11310502: Event 11310502 """
    IfFlagOff(1, 1176)
    IfFlagOff(1, 1179)
    IfFlagOn(1, 1173)
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
    EnableCharacter(arg_0_3)


def Event11310503(_, arg_0_3: int, arg_4_7: int):
    """ 11310503: Event 11310503 """
    IfFlagOff(1, 1176)
    IfFlagOff(1, 1179)
    IfFlagOn(1, 1174)
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
    SetAIParamID(arg_0_3, 1)
    SaveRequest()
    EnableCharacter(arg_0_3)


def Event11310530():
    """ 11310530: Event 11310530 """
    IfFlagRangeAllOff(7, (1176, 1181))
    IfFlagOn(7, 1171)
    IfFlagRangeAllOff(7, (1195, 1198))
    IfFlagOn(7, 1202)
    IfFlagRangeAllOff(7, (1213, 1215))
    IfFlagOn(7, 1211)
    IfFlagRangeAllOff(7, (1223, 1225))
    IfFlagOn(7, 1221)
    IfConditionTrue(1, input_condition=7)
    IfFlagOn(1, 11020600)
    IfThisEventOff(1)
    IfConditionTrue(2, input_condition=7)
    IfFlagOn(2, 11300005)
    IfConditionTrue(3, input_condition=7)
    IfThisEventOn(3)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    ClearEventValue(600, bit_count=4)
    EnableFlag(11020693)
    DisableFlagRange((1170, 1189))
    EnableFlag(1173)
    EnableCharacter(Characters.c0000_0002)
    DisableFlagRange((1190, 1209))
    EnableFlag(1192)
    DisableFlagRange((1210, 1219))
    EnableFlag(1216)
    EnableCharacter(Characters.c0000_0003)
    DisableFlagRange((1220, 1229))
    EnableFlag(1226)
    EnableCharacter(Characters.c0000_0004)


def Event11310531(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11310531: Event 11310531 """
    IfFlagOff(1, 1176)
    IfFlagOff(1, 1179)
    IfFlagOn(1, 1173)
    IfFlagOn(1, 1214)
    IfFlagOn(1, 1224)
    IfCharacterAlive(1, arg_0_3)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)


def Event11310532(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11310532: Event 11310532 """
    IfHost(1)
    IfFlagOff(1, 1176)
    IfFlagOff(1, 1179)
    IfFlagOn(1, 1174)
    IfFlagOn(1, 11310590)
    IfCharacterBackreadDisabled(1, arg_0_3)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)
    DisableCharacter(arg_0_3)
    ClearEventValue(600, bit_count=4)


def Event11310533(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11310533: Event 11310533 """
    IfFlagOff(1, 1179)
    IfFlagOn(-7, 1173)
    IfFlagOn(-7, 1176)
    IfConditionTrue(1, input_condition=-7)
    IfHealthLessThanOrEqual(1, arg_0_3, 0.0)
    IfThisEventOff(1)
    IfFlagOn(2, arg_12_15)
    IfThisEventOn(2)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)
    EndIfFinishedConditionFalse(2)
    DropMandatoryTreasure(arg_0_3)


def Event11310534(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11310534: Event 11310534 """
    IfFlagOff(1, 1176)
    IfFlagOn(-7, 1174)
    IfFlagOn(-7, 1179)
    IfConditionTrue(1, input_condition=-7)
    IfHealthLessThanOrEqual(1, arg_0_3, 0.0)
    IfThisEventOff(1)
    IfFlagOn(2, arg_12_15)
    IfThisEventOn(2)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)
    EndIfFinishedConditionFalse(2)
    DropMandatoryTreasure(arg_0_3)


def Event11310540(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11310540: Event 11310540 """
    IfFlagOff(1, 1625)
    IfFlagOff(1, 1627)
    IfFlagOff(1, 1628)
    IfFlagRangeAnyOn(2, (1620, 1621))
    IfFlagOn(2, 6)
    IfFlagOn(3, 1173)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)
    EnableCharacter(arg_0_3)


def Event11310541(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11310541: Event 11310541 """
    IfFlagOff(1, 1625)
    IfFlagOff(1, 1627)
    IfFlagOff(1, 1628)
    IfFlagOn(1, 1623)
    IfFlagOn(1, 11310002)
    IfCharacterAlive(1, arg_0_3)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)


def Event11310542(_, arg_0_3: int, arg_4_7: int):
    """ 11310542: Event 11310542 """
    IfFlagOn(1, 1623)
    IfHealthLessThanOrEqual(1, arg_0_3, 0.0)
    IfFlagOn(2, 1624)
    IfHealthLessThanOrEqual(2, arg_0_3, 0.0)
    IfFlagOn(3, arg_4_7)
    IfThisEventOn(3)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    DisableFlag(1625)
    DisableFlag(1627)
    EnableFlag(arg_4_7)
    EndIfFinishedConditionFalse(3)
    DropMandatoryTreasure(arg_0_3)


def Event11310543(_, arg_0_3: int, arg_4_7: int):
    """ 11310543: Event 11310543 """
    IfFlagOff(1, 1627)
    IfFlagOff(1, 1628)
    IfFlagOn(1, 1624)
    IfFlagOn(1, 11310595)
    IfThisEventOff(1)
    IfFlagOn(2, arg_4_7)
    IfThisEventOn(2)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EnableFlag(arg_4_7)
    SetTeamTypeAndExitStandbyAnimation(arg_0_3, TeamType.HostileAlly)
    SaveRequest()
    EnableCharacter(arg_0_3)


def Event11315030():
    """ 11315030: Event 11315030 """
    DisableNetworkSync()
    EndIfClient()
    EndIfFlagOn(11315031)
    EndIfFlagOn(7)
    IfHost(1)
    IfCharacterHuman(1, PLAYER)
    IfFlagOff(1, 11310810)
    SkipLinesIfThisEventOn(1)
    IfCharacterInsideRegion(1, PLAYER, region=Spheres.LeeroyInvaderTrigger)
    IfConditionTrue(0, input_condition=1)
    PlaceSummonSign(
        SummonSignType.BlackEyeSign,
        Characters.c0000_0007,
        region=Points.LeeroyInvaderSpawn,
        summon_flag=11315031,
        dismissal_flag=11315032,
    )
    Wait(20.0)
    Restart()


def Event11310810():
    """ 11310810: Event 11310810 """
    SkipLinesIfHost(3)
    IfFlagOn(1, 11315031)
    IfFlagOff(1, 11315032)
    SkipLinesIfConditionTrue(1, 1)
    DisableCharacter(Characters.c0000_0007)
    EndIfThisEventOn()
    IfCharacterDead(0, Characters.c0000_0007)
    EnableFlag(11310810)


def Event11310002():
    """ 11310002: Event 11310002 """
    EndIfThisEventOn()
    IfHost(1)
    IfFlagOff(1, 1625)
    IfFlagOff(1, 1627)
    IfFlagOff(1, 1628)
    IfFlagOn(1, 1623)
    IfFlagOff(1, 1638)
    IfCharacterInsideRegion(1, PLAYER, region=Boxes.PatchesKickTrigger)
    IfHost(2)
    IfFlagOff(2, 1625)
    IfFlagOff(2, 1627)
    IfFlagOff(2, 1628)
    IfFlagOn(2, 1623)
    IfFlagOn(2, 1638)
    IfCharacterInsideRegion(2, PLAYER, region=Boxes.PatchesKickTrigger)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfMultiplayer(7)
    SkipLinesIfFinishedConditionTrue(2, 2)
    PlayCutscene(
        130111,
        skippable=True,
        fade_out=False,
        player_id=PLAYER,
        move_to_region=Boxes.PlayerPointAfterKickCutscene,
        move_to_map=TOMB_OF_THE_GIANTS,
    )
    SkipLines(1)
    PlayCutscene(
        130110,
        skippable=True,
        fade_out=False,
        player_id=PLAYER,
        move_to_region=Boxes.PlayerPointAfterKickCutscene,
        move_to_map=TOMB_OF_THE_GIANTS,
    )
    WaitFrames(1)
    Move(
        Characters.c0000_0005,
        destination=Boxes.PatchesPointAfterKickCutscene,
        destination_type=CoordEntityType.Region,
    )
    End()
    SkipLinesIfClient(7)
    SkipLinesIfFinishedConditionTrue(2, 2)
    PlayCutscene(
        130111,
        skippable=False,
        fade_out=False,
        player_id=PLAYER,
        move_to_region=Boxes.PlayerPointAfterKickCutscene,
        move_to_map=TOMB_OF_THE_GIANTS,
    )
    SkipLines(1)
    PlayCutscene(
        130110,
        skippable=False,
        fade_out=False,
        player_id=PLAYER,
        move_to_region=Boxes.PlayerPointAfterKickCutscene,
        move_to_map=TOMB_OF_THE_GIANTS,
    )
    WaitFrames(1)
    Move(
        Characters.c0000_0005,
        destination=Boxes.PatchesPointAfterKickCutscene,
        destination_type=CoordEntityType.Region,
    )
    End()
    SkipLinesIfFinishedConditionTrue(2, 2)
    PlayCutscene(130111, skippable=False, fade_out=False, player_id=PLAYER)
    SkipLines(1)
    PlayCutscene(130110, skippable=False, fade_out=False, player_id=PLAYER)
    WaitFrames(1)
    Move(
        Characters.c0000_0005,
        destination=Boxes.PatchesPointAfterKickCutscene,
        destination_type=CoordEntityType.Region,
    )


def Event11315843(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11315843: Event 11315843 """
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


def Event11315846(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 11315846: Event 11315846 """
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
