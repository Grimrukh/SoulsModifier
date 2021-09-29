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


@RestartOnRest
def PatchesAmbush():
    """ 11312000: Patches teleports behind the player and attacks. """
    DisableCharacter(Characters.c0000_PatchesAmbush)

    Await(InsideMap(TOMB_OF_THE_GIANTS) and TriggerFlags.PatchesAmbush and IsAlive(Characters.c0000_PatchesAmbush))
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
    """ 11312001: Channeler teleports above the player (no gravity) and uses its buff dance. """
    DisableCharacter(Characters.c2370_TrollChanneler)

    Await(InsideMap(TOMB_OF_THE_GIANTS) and TriggerFlags.ChannelerAmbush and IsAlive(Characters.c2370_TrollChanneler))
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

    AddSpecialEffect(6071, 5470)
    AddSpecialEffect(6091, 5470)
    AddSpecialEffect(6101, 5470)
    AddSpecialEffect(6321, 5470)
    AddSpecialEffect(6551, 5470)
    AddSpecialEffect(1310960, 5470)
    AddSpecialEffect(1310950, 5470)
    AddSpecialEffect(1310961, 5470)
    AddSpecialEffect(1310300, 5470)
    AddSpecialEffect(1310120, 5470)
    AddSpecialEffect(1310121, 5470)
    AddSpecialEffect(1310122, 5470)
    AddSpecialEffect(1310212, 5470)
    AddSpecialEffect(1310213, 5470)
    AddSpecialEffect(1310214, 5470)
    AddSpecialEffect(1310215, 5470)
    AddSpecialEffect(1310216, 5470)
    AddSpecialEffect(1310217, 5470)
    AddSpecialEffect(1310218, 5470)
    AddSpecialEffect(1310219, 5470)
    AddSpecialEffect(1310220, 5470)
    AddSpecialEffect(1310221, 5470)
    AddSpecialEffect(1310222, 5470)
    AddSpecialEffect(1310223, 5470)
    AddSpecialEffect(1310224, 5470)
    AddSpecialEffect(1310225, 5470)
    AddSpecialEffect(1310226, 5470)
    AddSpecialEffect(1310227, 5470)
    AddSpecialEffect(1310228, 5470)
    AddSpecialEffect(1310229, 5470)
    AddSpecialEffect(1310251, 5470)
    AddSpecialEffect(1310125, 5470)
    AddSpecialEffect(1310124, 5470)
    AddSpecialEffect(1310123, 5470)
    AddSpecialEffect(1310900, 5470)
    AddSpecialEffect(1310901, 5470)
    AddSpecialEffect(1310902, 5470)
    AddSpecialEffect(1310903, 5470)
    AddSpecialEffect(1310904, 5470)
    AddSpecialEffect(1310230, 5470)
    AddSpecialEffect(1310231, 5470)
    AddSpecialEffect(1310232, 5470)
    AddSpecialEffect(1310233, 5470)
    AddSpecialEffect(1310234, 5470)
    AddSpecialEffect(1310235, 5470)
    AddSpecialEffect(1310236, 5470)
    AddSpecialEffect(1310237, 5470)
    AddSpecialEffect(1310238, 5470)
    AddSpecialEffect(1310239, 5470)
    AddSpecialEffect(1310240, 5470)
    AddSpecialEffect(1310241, 5470)
    AddSpecialEffect(1310242, 5470)
    AddSpecialEffect(1310243, 5470)
    AddSpecialEffect(1310244, 5470)
    AddSpecialEffect(1310245, 5470)
    AddSpecialEffect(1310905, 5470)
    AddSpecialEffect(1310906, 5470)
    AddSpecialEffect(1310907, 5470)
    AddSpecialEffect(1310908, 5470)
    AddSpecialEffect(1310909, 5470)
    AddSpecialEffect(1310246, 5470)
    AddSpecialEffect(1310247, 5470)
    AddSpecialEffect(1310248, 5470)
    AddSpecialEffect(1310203, 5470)
    AddSpecialEffect(1310204, 5470)
    AddSpecialEffect(1310205, 5470)
    AddSpecialEffect(1310206, 5470)
    AddSpecialEffect(1310207, 5470)
    AddSpecialEffect(1310208, 5470)
    AddSpecialEffect(1310209, 5470)
    AddSpecialEffect(1310210, 5470)
    AddSpecialEffect(1310211, 5470)
    AddSpecialEffect(1310200, 5470)
    AddSpecialEffect(1310201, 5470)
    AddSpecialEffect(1310202, 5470)
    AddSpecialEffect(1310250, 5470)
    AddSpecialEffect(1310400, 5470)
    AddSpecialEffect(1310249, 5470)
    AddSpecialEffect(1310252, 5470)
    AddSpecialEffect(1310253, 5470)
    AddSpecialEffect(1310254, 5470)
    AddSpecialEffect(1310255, 5470)
    AddSpecialEffect(1313900, 5470)
    AddSpecialEffect(1313910, 5470)
    AddSpecialEffect(1313901, 5470)
    AddSpecialEffect(1313911, 5470)
    AddSpecialEffect(1313902, 5470)
    AddSpecialEffect(1313912, 5470)
    AddSpecialEffect(1310800, 5470)
    AddSpecialEffect(1310810, 5470)

    return RESTART


@RestartOnRest
def RedPhantomAmbush():
    """ 11312002: Random red phantom ambushes the player. """
    DisableCharacter(Characters.c2910_0022)
    DisableCharacter(Characters.c2910_0023)
    DisableCharacter(Characters.c2910_0024)
    DisableCharacter(Characters.c2910_0025)
    DisableCharacter(Characters.c2910_0026)
    DisableCharacter(Characters.c2950_0007)
    DisableCharacter(Characters.c2950_0008)
    DisableCharacter(Characters.c2950_0009)
    DisableCharacter(Characters.c2950_0010)
    DisableCharacter(Characters.c2950_0011)

    Await(InsideMap(TOMB_OF_THE_GIANTS) and TriggerFlags.EnemyAmbush)
    DisableFlag(TriggerFlags.EnemyAmbush)

    DisableFlagRange((11812900, 11812999))
    EnableRandomFlagInRange((11812900, 11812909))

    if FlagEnabled(11812900):
        ControlRedPhantom(0, Characters.c2910_0022)
    elif FlagEnabled(11812901):
        ControlRedPhantom(0, Characters.c2910_0023)
    elif FlagEnabled(11812902):
        ControlRedPhantom(0, Characters.c2910_0024)
    elif FlagEnabled(11812903):
        ControlRedPhantom(0, Characters.c2910_0025)
    elif FlagEnabled(11812904):
        ControlRedPhantom(0, Characters.c2910_0026)
    elif FlagEnabled(11812905):
        ControlRedPhantom(0, Characters.c2950_0007)
    elif FlagEnabled(11812906):
        ControlRedPhantom(0, Characters.c2950_0008)
    elif FlagEnabled(11812907):
        ControlRedPhantom(0, Characters.c2950_0009)
    elif FlagEnabled(11812908):
        ControlRedPhantom(0, Characters.c2950_0010)
    elif FlagEnabled(11812909):
        ControlRedPhantom(0, Characters.c2950_0011)
    
    Await(FlagEnabled(11315082))

    return RESTART


@RestartOnRest
def ControlRedPhantom(_, enemy: int):
    """ 11315081: `enemy` moves to player and appears. """
    DisableFlag(11315082)
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
    EnableFlag(11315082)


def MakeWorldInvisible():
    """ 11312003: Disable all map pieces. Undone only by reload. """
    Await(TriggerFlags.InvisibleWorld)   # note you don't need to be standing in the map
    DisableFlag(TriggerFlags.InvisibleWorld)
    for map_piece in range(1318500, 1318556):
        DisableMapPiece(map_piece)
    # No need to restart.


@RestartOnRest
def OopsAllGwyns():
    """ 11312004: Enable Gwyns and warp them to their paired normal characters. """
    DisableCharacter(1310600)
    DisableCharacter(1310601)
    DisableCharacter(1310602)
    DisableCharacter(1310603)
    DisableCharacter(1310604)
    DisableCharacter(1310605)
    DisableCharacter(1310606)
    DisableCharacter(1310607)
    DisableCharacter(1310608)
    DisableCharacter(1310609)
    DisableCharacter(1310610)
    DisableCharacter(1310611)
    DisableCharacter(1310612)
    DisableCharacter(1310613)
    Await(TriggerFlags.OopsAllGwyns)  # note you don't need to be standing in the map
    DisableCharacter(6071)
    EnableCharacter(1310600)
    DisableCharacter(1310121)
    EnableCharacter(1310601)
    DisableCharacter(1310215)
    EnableCharacter(1310602)
    DisableCharacter(1310220)
    EnableCharacter(1310603)
    DisableCharacter(1310225)
    EnableCharacter(1310604)
    DisableCharacter(1310251)
    EnableCharacter(1310605)
    DisableCharacter(1310231)
    EnableCharacter(1310606)
    DisableCharacter(1310236)
    EnableCharacter(1310607)
    DisableCharacter(1310241)
    EnableCharacter(1310608)
    DisableCharacter(1310246)
    EnableCharacter(1310609)
    DisableCharacter(1310205)
    EnableCharacter(1310610)
    DisableCharacter(1310210)
    EnableCharacter(1310611)
    DisableCharacter(1310250)
    EnableCharacter(1310612)
    DisableCharacter(1310254)
    EnableCharacter(1310613)
    WaitFrames(30)  # enough time for other maps to trigger too
    DisableFlag(TriggerFlags.OopsAllGwyns)
    # No need to restart.


@RestartOnRest
def OopsAllBonewheels():
    """ 11312005: Enable Bonewheels and warp them to their paired normal characters. """
    DisableCharacter(1310401)
    DisableCharacter(1310402)
    DisableCharacter(1310403)
    DisableCharacter(1310404)
    DisableCharacter(1310405)
    DisableCharacter(1310406)
    DisableCharacter(1310407)
    DisableCharacter(1310408)
    DisableCharacter(1310409)
    DisableCharacter(1310410)
    DisableCharacter(1310411)
    DisableCharacter(1310412)
    DisableCharacter(1310413)
    DisableCharacter(1310414)
    DisableCharacter(1310415)
    DisableCharacter(1310416)
    DisableCharacter(1310417)
    DisableCharacter(1310418)
    DisableCharacter(1310419)
    DisableCharacter(1310420)
    DisableCharacter(1310421)
    DisableCharacter(1310422)
    DisableCharacter(1310423)
    DisableCharacter(1310424)
    DisableCharacter(1310425)
    DisableCharacter(1310426)
    DisableCharacter(1310427)
    DisableCharacter(1310428)
    DisableCharacter(1310429)
    DisableCharacter(1310430)
    DisableCharacter(1310431)
    DisableCharacter(1310432)
    DisableCharacter(1310433)
    DisableCharacter(1310434)
    DisableCharacter(1310435)
    DisableCharacter(1310436)
    DisableCharacter(1310437)
    DisableCharacter(1310438)
    DisableCharacter(1310439)
    DisableCharacter(1310440)
    DisableCharacter(1310441)
    DisableCharacter(1310442)
    DisableCharacter(1310443)
    DisableCharacter(1310444)
    DisableCharacter(1310445)
    DisableCharacter(1310446)
    DisableCharacter(1310447)
    DisableCharacter(1310448)
    DisableCharacter(1310449)
    DisableCharacter(1310450)
    DisableCharacter(1310451)
    DisableCharacter(1310452)
    DisableCharacter(1310453)
    DisableCharacter(1310454)
    DisableCharacter(1310455)
    DisableCharacter(1310456)
    DisableCharacter(1310457)
    DisableCharacter(1310458)
    DisableCharacter(1310459)
    DisableCharacter(1310460)
    DisableCharacter(1310461)
    DisableCharacter(1310462)
    DisableCharacter(1310463)
    DisableCharacter(1310464)
    DisableCharacter(1310465)
    DisableCharacter(1310466)
    DisableCharacter(1310467)
    DisableCharacter(1310468)
    DisableCharacter(1310469)
    Await(TriggerFlags.OopsAllBonewheels)  # note you don't need to be standing in the map
    DisableCharacter(6071)
    EnableCharacter(1310401)
    DisableCharacter(6091)
    EnableCharacter(1310402)
    DisableCharacter(6101)
    EnableCharacter(1310403)
    DisableCharacter(6321)
    EnableCharacter(1310404)
    DisableCharacter(6551)
    EnableCharacter(1310405)
    DisableCharacter(1310300)
    EnableCharacter(1310406)
    DisableCharacter(1310120)
    EnableCharacter(1310407)
    DisableCharacter(1310121)
    EnableCharacter(1310408)
    DisableCharacter(1310122)
    EnableCharacter(1310409)
    DisableCharacter(1310212)
    EnableCharacter(1310410)
    DisableCharacter(1310213)
    EnableCharacter(1310411)
    DisableCharacter(1310214)
    EnableCharacter(1310412)
    DisableCharacter(1310215)
    EnableCharacter(1310413)
    DisableCharacter(1310216)
    EnableCharacter(1310414)
    DisableCharacter(1310217)
    EnableCharacter(1310415)
    DisableCharacter(1310218)
    EnableCharacter(1310416)
    DisableCharacter(1310219)
    EnableCharacter(1310417)
    DisableCharacter(1310220)
    EnableCharacter(1310418)
    DisableCharacter(1310221)
    EnableCharacter(1310419)
    DisableCharacter(1310222)
    EnableCharacter(1310420)
    DisableCharacter(1310223)
    EnableCharacter(1310421)
    DisableCharacter(1310224)
    EnableCharacter(1310422)
    DisableCharacter(1310225)
    EnableCharacter(1310423)
    DisableCharacter(1310226)
    EnableCharacter(1310424)
    DisableCharacter(1310227)
    EnableCharacter(1310425)
    DisableCharacter(1310228)
    EnableCharacter(1310426)
    DisableCharacter(1310229)
    EnableCharacter(1310427)
    DisableCharacter(1310251)
    EnableCharacter(1310428)
    DisableCharacter(1310125)
    EnableCharacter(1310429)
    DisableCharacter(1310124)
    EnableCharacter(1310430)
    DisableCharacter(1310123)
    EnableCharacter(1310431)
    DisableCharacter(1310230)
    EnableCharacter(1310432)
    DisableCharacter(1310231)
    EnableCharacter(1310433)
    DisableCharacter(1310232)
    EnableCharacter(1310434)
    DisableCharacter(1310233)
    EnableCharacter(1310435)
    DisableCharacter(1310234)
    EnableCharacter(1310436)
    DisableCharacter(1310235)
    EnableCharacter(1310437)
    DisableCharacter(1310236)
    EnableCharacter(1310438)
    DisableCharacter(1310237)
    EnableCharacter(1310439)
    DisableCharacter(1310238)
    EnableCharacter(1310440)
    DisableCharacter(1310239)
    EnableCharacter(1310441)
    DisableCharacter(1310240)
    EnableCharacter(1310442)
    DisableCharacter(1310241)
    EnableCharacter(1310443)
    DisableCharacter(1310242)
    EnableCharacter(1310444)
    DisableCharacter(1310243)
    EnableCharacter(1310445)
    DisableCharacter(1310244)
    EnableCharacter(1310446)
    DisableCharacter(1310245)
    EnableCharacter(1310447)
    DisableCharacter(1310246)
    EnableCharacter(1310448)
    DisableCharacter(1310247)
    EnableCharacter(1310449)
    DisableCharacter(1310248)
    EnableCharacter(1310450)
    DisableCharacter(1310203)
    EnableCharacter(1310451)
    DisableCharacter(1310204)
    EnableCharacter(1310452)
    DisableCharacter(1310205)
    EnableCharacter(1310453)
    DisableCharacter(1310206)
    EnableCharacter(1310454)
    DisableCharacter(1310207)
    EnableCharacter(1310455)
    DisableCharacter(1310208)
    EnableCharacter(1310456)
    DisableCharacter(1310209)
    EnableCharacter(1310457)
    DisableCharacter(1310210)
    EnableCharacter(1310458)
    DisableCharacter(1310211)
    EnableCharacter(1310459)
    DisableCharacter(1310200)
    EnableCharacter(1310460)
    DisableCharacter(1310201)
    EnableCharacter(1310461)
    DisableCharacter(1310202)
    EnableCharacter(1310462)
    DisableCharacter(1310250)
    EnableCharacter(1310463)
    DisableCharacter(1310400)
    EnableCharacter(1310464)
    DisableCharacter(1310249)
    EnableCharacter(1310465)
    DisableCharacter(1310252)
    EnableCharacter(1310466)
    DisableCharacter(1310253)
    EnableCharacter(1310467)
    DisableCharacter(1310254)
    EnableCharacter(1310468)
    DisableCharacter(1310255)
    EnableCharacter(1310469)
    WaitFrames(30)  # enough time for other maps to trigger too
    DisableFlag(TriggerFlags.OopsAllBonewheels)
    # No need to restart.


@RestartOnRest
def HyperAggression():
    """ 11312006: Switch AI param of every enemy to its aggressive version. """
    Await(TriggerFlags.HyperAggression or TriggerFlags.HyperAggressionReTrigger)
    
    SetAIParamID(1310300, 279053)
    SetAIParamID(1310120, 290050)
    SetAIParamID(1310121, 290052)
    SetAIParamID(1310122, 290050)
    SetAIParamID(1310212, 291052)
    SetAIParamID(1310213, 291052)
    SetAIParamID(1310214, 291052)
    SetAIParamID(1310215, 291052)
    SetAIParamID(1310216, 291052)
    SetAIParamID(1310217, 291052)
    SetAIParamID(1310218, 291053)
    SetAIParamID(1310219, 291053)
    SetAIParamID(1310220, 291053)
    SetAIParamID(1310221, 291053)
    SetAIParamID(1310222, 291053)
    SetAIParamID(1310223, 291053)
    SetAIParamID(1310224, 291053)
    SetAIParamID(1310225, 291053)
    SetAIParamID(1310226, 291051)
    SetAIParamID(1310227, 291051)
    SetAIParamID(1310228, 291051)
    SetAIParamID(1310229, 291051)
    SetAIParamID(1310251, 291052)
    SetAIParamID(1310125, 291050)
    SetAIParamID(1310124, 291050)
    SetAIParamID(1310123, 291050)
    SetAIParamID(1310900, 291052)
    SetAIParamID(1310901, 291052)
    SetAIParamID(1310902, 291052)
    SetAIParamID(1310903, 291052)
    SetAIParamID(1310904, 291052)
    SetAIParamID(1310230, 294050)
    SetAIParamID(1310231, 294050)
    SetAIParamID(1310232, 294050)
    SetAIParamID(1310233, 294050)
    SetAIParamID(1310234, 294050)
    SetAIParamID(1310235, 294050)
    SetAIParamID(1310236, 294050)
    SetAIParamID(1310237, 294050)
    SetAIParamID(1310238, 294050)
    SetAIParamID(1310239, 295051)
    SetAIParamID(1310240, 295051)
    SetAIParamID(1310241, 295051)
    SetAIParamID(1310242, 295051)
    SetAIParamID(1310243, 295051)
    SetAIParamID(1310244, 295051)
    SetAIParamID(1310245, 295051)
    SetAIParamID(1310905, 295050)
    SetAIParamID(1310906, 295050)
    SetAIParamID(1310907, 295050)
    SetAIParamID(1310908, 295050)
    SetAIParamID(1310909, 295050)
    SetAIParamID(1310246, 296050)
    SetAIParamID(1310247, 296050)
    SetAIParamID(1310248, 296050)
    SetAIParamID(1310203, 296050)
    SetAIParamID(1310204, 296050)
    SetAIParamID(1310205, 296050)
    SetAIParamID(1310206, 296050)
    SetAIParamID(1310207, 296050)
    SetAIParamID(1310208, 296050)
    SetAIParamID(1310209, 296050)
    SetAIParamID(1310210, 296050)
    SetAIParamID(1310211, 296050)
    SetAIParamID(1310200, 296050)
    SetAIParamID(1310201, 296050)
    SetAIParamID(1310202, 296050)
    SetAIParamID(1310250, 296050)
    SetAIParamID(1310400, 330050)
    SetAIParamID(1310249, 332053)
    SetAIParamID(1310252, 332053)
    SetAIParamID(1310253, 332052)
    SetAIParamID(1310254, 332052)
    SetAIParamID(1310255, 332052)
    SetAIParamID(1313900, 349050)
    SetAIParamID(1313910, 349050)
    SetAIParamID(1313901, 349150)
    SetAIParamID(1313911, 349150)
    SetAIParamID(1313902, 349150)
    SetAIParamID(1313912, 349150)
    SetAIParamID(1310800, 522050)
    SetAIParamID(1310600, 537050)
    SetAIParamID(1310601, 537050)
    SetAIParamID(1310602, 537050)
    SetAIParamID(1310603, 537050)
    SetAIParamID(1310604, 537050)
    SetAIParamID(1310605, 537050)
    SetAIParamID(1310606, 537050)
    SetAIParamID(1310607, 537050)
    SetAIParamID(1310608, 537050)
    SetAIParamID(1310609, 537050)
    SetAIParamID(1310610, 537050)
    SetAIParamID(1310611, 537050)
    SetAIParamID(1310612, 537050)
    SetAIParamID(1310613, 537050)
    SetAIParamID(1310401, 293050)
    SetAIParamID(1310402, 293050)
    SetAIParamID(1310403, 293050)
    SetAIParamID(1310404, 293050)
    SetAIParamID(1310405, 293050)
    SetAIParamID(1310406, 293050)
    SetAIParamID(1310407, 293050)
    SetAIParamID(1310408, 293050)
    SetAIParamID(1310409, 293050)
    SetAIParamID(1310410, 293050)
    SetAIParamID(1310411, 293050)
    SetAIParamID(1310412, 293050)
    SetAIParamID(1310413, 293050)
    SetAIParamID(1310414, 293050)
    SetAIParamID(1310415, 293050)
    SetAIParamID(1310416, 293050)
    SetAIParamID(1310417, 293050)
    SetAIParamID(1310418, 293050)
    SetAIParamID(1310419, 293050)
    SetAIParamID(1310420, 293050)
    SetAIParamID(1310421, 293050)
    SetAIParamID(1310422, 293050)
    SetAIParamID(1310423, 293050)
    SetAIParamID(1310424, 293050)
    SetAIParamID(1310425, 293050)
    SetAIParamID(1310426, 293050)
    SetAIParamID(1310427, 293050)
    SetAIParamID(1310428, 293050)
    SetAIParamID(1310429, 293050)
    SetAIParamID(1310430, 293050)
    SetAIParamID(1310431, 293050)
    SetAIParamID(1310432, 293050)
    SetAIParamID(1310433, 293050)
    SetAIParamID(1310434, 293050)
    SetAIParamID(1310435, 293050)
    SetAIParamID(1310436, 293050)
    SetAIParamID(1310437, 293050)
    SetAIParamID(1310438, 293050)
    SetAIParamID(1310439, 293050)
    SetAIParamID(1310440, 293050)
    SetAIParamID(1310441, 293050)
    SetAIParamID(1310442, 293050)
    SetAIParamID(1310443, 293050)
    SetAIParamID(1310444, 293050)
    SetAIParamID(1310445, 293050)
    SetAIParamID(1310446, 293050)
    SetAIParamID(1310447, 293050)
    SetAIParamID(1310448, 293050)
    SetAIParamID(1310449, 293050)
    SetAIParamID(1310450, 293050)
    SetAIParamID(1310451, 293050)
    SetAIParamID(1310452, 293050)
    SetAIParamID(1310453, 293050)
    SetAIParamID(1310454, 293050)
    SetAIParamID(1310455, 293050)
    SetAIParamID(1310456, 293050)
    SetAIParamID(1310457, 293050)
    SetAIParamID(1310458, 293050)
    SetAIParamID(1310459, 293050)
    SetAIParamID(1310460, 293050)
    SetAIParamID(1310461, 293050)
    SetAIParamID(1310462, 293050)
    SetAIParamID(1310463, 293050)
    SetAIParamID(1310464, 293050)
    SetAIParamID(1310465, 293050)
    SetAIParamID(1310466, 293050)
    SetAIParamID(1310467, 293050)
    SetAIParamID(1310468, 293050)
    SetAIParamID(1310469, 293050)
        
    # Common EMEVD manages the flags that control this event.
    Await(not TriggerFlags.HyperAggressionReTrigger)
    
    SetAIParamID(1310300, 279003)
    SetAIParamID(1310120, 290000)
    SetAIParamID(1310121, 290002)
    SetAIParamID(1310122, 290000)
    SetAIParamID(1310212, 291002)
    SetAIParamID(1310213, 291002)
    SetAIParamID(1310214, 291002)
    SetAIParamID(1310215, 291002)
    SetAIParamID(1310216, 291002)
    SetAIParamID(1310217, 291002)
    SetAIParamID(1310218, 291003)
    SetAIParamID(1310219, 291003)
    SetAIParamID(1310220, 291003)
    SetAIParamID(1310221, 291003)
    SetAIParamID(1310222, 291003)
    SetAIParamID(1310223, 291003)
    SetAIParamID(1310224, 291003)
    SetAIParamID(1310225, 291003)
    SetAIParamID(1310226, 291001)
    SetAIParamID(1310227, 291001)
    SetAIParamID(1310228, 291001)
    SetAIParamID(1310229, 291001)
    SetAIParamID(1310251, 291002)
    SetAIParamID(1310125, 291000)
    SetAIParamID(1310124, 291000)
    SetAIParamID(1310123, 291000)
    SetAIParamID(1310900, 291002)
    SetAIParamID(1310901, 291002)
    SetAIParamID(1310902, 291002)
    SetAIParamID(1310903, 291002)
    SetAIParamID(1310904, 291002)
    SetAIParamID(1310230, 294000)
    SetAIParamID(1310231, 294000)
    SetAIParamID(1310232, 294000)
    SetAIParamID(1310233, 294000)
    SetAIParamID(1310234, 294000)
    SetAIParamID(1310235, 294000)
    SetAIParamID(1310236, 294000)
    SetAIParamID(1310237, 294000)
    SetAIParamID(1310238, 294000)
    SetAIParamID(1310239, 295001)
    SetAIParamID(1310240, 295001)
    SetAIParamID(1310241, 295001)
    SetAIParamID(1310242, 295001)
    SetAIParamID(1310243, 295001)
    SetAIParamID(1310244, 295001)
    SetAIParamID(1310245, 295001)
    SetAIParamID(1310905, 295000)
    SetAIParamID(1310906, 295000)
    SetAIParamID(1310907, 295000)
    SetAIParamID(1310908, 295000)
    SetAIParamID(1310909, 295000)
    SetAIParamID(1310246, 296000)
    SetAIParamID(1310247, 296000)
    SetAIParamID(1310248, 296000)
    SetAIParamID(1310203, 296000)
    SetAIParamID(1310204, 296000)
    SetAIParamID(1310205, 296000)
    SetAIParamID(1310206, 296000)
    SetAIParamID(1310207, 296000)
    SetAIParamID(1310208, 296000)
    SetAIParamID(1310209, 296000)
    SetAIParamID(1310210, 296000)
    SetAIParamID(1310211, 296000)
    SetAIParamID(1310200, 296000)
    SetAIParamID(1310201, 296000)
    SetAIParamID(1310202, 296000)
    SetAIParamID(1310250, 296000)
    SetAIParamID(1310400, 330000)
    SetAIParamID(1310249, 332003)
    SetAIParamID(1310252, 332003)
    SetAIParamID(1310253, 332002)
    SetAIParamID(1310254, 332002)
    SetAIParamID(1310255, 332002)
    SetAIParamID(1313900, 349000)
    SetAIParamID(1313910, 349000)
    SetAIParamID(1313901, 349100)
    SetAIParamID(1313911, 349100)
    SetAIParamID(1313902, 349100)
    SetAIParamID(1313912, 349100)
    SetAIParamID(1310800, 522000)
    SetAIParamID(1310600, 537000)
    SetAIParamID(1310601, 537000)
    SetAIParamID(1310602, 537000)
    SetAIParamID(1310603, 537000)
    SetAIParamID(1310604, 537000)
    SetAIParamID(1310605, 537000)
    SetAIParamID(1310606, 537000)
    SetAIParamID(1310607, 537000)
    SetAIParamID(1310608, 537000)
    SetAIParamID(1310609, 537000)
    SetAIParamID(1310610, 537000)
    SetAIParamID(1310611, 537000)
    SetAIParamID(1310612, 537000)
    SetAIParamID(1310613, 537000)
    SetAIParamID(1310401, 293000)
    SetAIParamID(1310402, 293000)
    SetAIParamID(1310403, 293000)
    SetAIParamID(1310404, 293000)
    SetAIParamID(1310405, 293000)
    SetAIParamID(1310406, 293000)
    SetAIParamID(1310407, 293000)
    SetAIParamID(1310408, 293000)
    SetAIParamID(1310409, 293000)
    SetAIParamID(1310410, 293000)
    SetAIParamID(1310411, 293000)
    SetAIParamID(1310412, 293000)
    SetAIParamID(1310413, 293000)
    SetAIParamID(1310414, 293000)
    SetAIParamID(1310415, 293000)
    SetAIParamID(1310416, 293000)
    SetAIParamID(1310417, 293000)
    SetAIParamID(1310418, 293000)
    SetAIParamID(1310419, 293000)
    SetAIParamID(1310420, 293000)
    SetAIParamID(1310421, 293000)
    SetAIParamID(1310422, 293000)
    SetAIParamID(1310423, 293000)
    SetAIParamID(1310424, 293000)
    SetAIParamID(1310425, 293000)
    SetAIParamID(1310426, 293000)
    SetAIParamID(1310427, 293000)
    SetAIParamID(1310428, 293000)
    SetAIParamID(1310429, 293000)
    SetAIParamID(1310430, 293000)
    SetAIParamID(1310431, 293000)
    SetAIParamID(1310432, 293000)
    SetAIParamID(1310433, 293000)
    SetAIParamID(1310434, 293000)
    SetAIParamID(1310435, 293000)
    SetAIParamID(1310436, 293000)
    SetAIParamID(1310437, 293000)
    SetAIParamID(1310438, 293000)
    SetAIParamID(1310439, 293000)
    SetAIParamID(1310440, 293000)
    SetAIParamID(1310441, 293000)
    SetAIParamID(1310442, 293000)
    SetAIParamID(1310443, 293000)
    SetAIParamID(1310444, 293000)
    SetAIParamID(1310445, 293000)
    SetAIParamID(1310446, 293000)
    SetAIParamID(1310447, 293000)
    SetAIParamID(1310448, 293000)
    SetAIParamID(1310449, 293000)
    SetAIParamID(1310450, 293000)
    SetAIParamID(1310451, 293000)
    SetAIParamID(1310452, 293000)
    SetAIParamID(1310453, 293000)
    SetAIParamID(1310454, 293000)
    SetAIParamID(1310455, 293000)
    SetAIParamID(1310456, 293000)
    SetAIParamID(1310457, 293000)
    SetAIParamID(1310458, 293000)
    SetAIParamID(1310459, 293000)
    SetAIParamID(1310460, 293000)
    SetAIParamID(1310461, 293000)
    SetAIParamID(1310462, 293000)
    SetAIParamID(1310463, 293000)
    SetAIParamID(1310464, 293000)
    SetAIParamID(1310465, 293000)
    SetAIParamID(1310466, 293000)
    SetAIParamID(1310467, 293000)
    SetAIParamID(1310468, 293000)
    SetAIParamID(1310469, 293000)
    
    return RESTART


@RestartOnRest
def EnemySpeedUp():
    """ 11312200: Temporary enemy effect. """
    Await(TriggerFlags.EnemySpeedUp)
    AddSpecialEffect(6071, 200000)
    AddSpecialEffect(6091, 200000)
    AddSpecialEffect(6101, 200000)
    AddSpecialEffect(6321, 200000)
    AddSpecialEffect(6551, 200000)
    AddSpecialEffect(1310960, 200000)
    AddSpecialEffect(1310950, 200000)
    AddSpecialEffect(1310961, 200000)
    AddSpecialEffect(1310300, 200000)
    AddSpecialEffect(1310120, 200000)
    AddSpecialEffect(1310121, 200000)
    AddSpecialEffect(1310122, 200000)
    AddSpecialEffect(1310212, 200000)
    AddSpecialEffect(1310213, 200000)
    AddSpecialEffect(1310214, 200000)
    AddSpecialEffect(1310215, 200000)
    AddSpecialEffect(1310216, 200000)
    AddSpecialEffect(1310217, 200000)
    AddSpecialEffect(1310218, 200000)
    AddSpecialEffect(1310219, 200000)
    AddSpecialEffect(1310220, 200000)
    AddSpecialEffect(1310221, 200000)
    AddSpecialEffect(1310222, 200000)
    AddSpecialEffect(1310223, 200000)
    AddSpecialEffect(1310224, 200000)
    AddSpecialEffect(1310225, 200000)
    AddSpecialEffect(1310226, 200000)
    AddSpecialEffect(1310227, 200000)
    AddSpecialEffect(1310228, 200000)
    AddSpecialEffect(1310229, 200000)
    AddSpecialEffect(1310251, 200000)
    AddSpecialEffect(1310125, 200000)
    AddSpecialEffect(1310124, 200000)
    AddSpecialEffect(1310123, 200000)
    AddSpecialEffect(1310900, 200000)
    AddSpecialEffect(1310901, 200000)
    AddSpecialEffect(1310902, 200000)
    AddSpecialEffect(1310903, 200000)
    AddSpecialEffect(1310904, 200000)
    AddSpecialEffect(1310230, 200000)
    AddSpecialEffect(1310231, 200000)
    AddSpecialEffect(1310232, 200000)
    AddSpecialEffect(1310233, 200000)
    AddSpecialEffect(1310234, 200000)
    AddSpecialEffect(1310235, 200000)
    AddSpecialEffect(1310236, 200000)
    AddSpecialEffect(1310237, 200000)
    AddSpecialEffect(1310238, 200000)
    AddSpecialEffect(1310239, 200000)
    AddSpecialEffect(1310240, 200000)
    AddSpecialEffect(1310241, 200000)
    AddSpecialEffect(1310242, 200000)
    AddSpecialEffect(1310243, 200000)
    AddSpecialEffect(1310244, 200000)
    AddSpecialEffect(1310245, 200000)
    AddSpecialEffect(1310905, 200000)
    AddSpecialEffect(1310906, 200000)
    AddSpecialEffect(1310907, 200000)
    AddSpecialEffect(1310908, 200000)
    AddSpecialEffect(1310909, 200000)
    AddSpecialEffect(1310246, 200000)
    AddSpecialEffect(1310247, 200000)
    AddSpecialEffect(1310248, 200000)
    AddSpecialEffect(1310203, 200000)
    AddSpecialEffect(1310204, 200000)
    AddSpecialEffect(1310205, 200000)
    AddSpecialEffect(1310206, 200000)
    AddSpecialEffect(1310207, 200000)
    AddSpecialEffect(1310208, 200000)
    AddSpecialEffect(1310209, 200000)
    AddSpecialEffect(1310210, 200000)
    AddSpecialEffect(1310211, 200000)
    AddSpecialEffect(1310200, 200000)
    AddSpecialEffect(1310201, 200000)
    AddSpecialEffect(1310202, 200000)
    AddSpecialEffect(1310250, 200000)
    AddSpecialEffect(1310400, 200000)
    AddSpecialEffect(1310249, 200000)
    AddSpecialEffect(1310252, 200000)
    AddSpecialEffect(1310253, 200000)
    AddSpecialEffect(1310254, 200000)
    AddSpecialEffect(1310255, 200000)
    AddSpecialEffect(1313900, 200000)
    AddSpecialEffect(1313910, 200000)
    AddSpecialEffect(1313901, 200000)
    AddSpecialEffect(1313911, 200000)
    AddSpecialEffect(1313902, 200000)
    AddSpecialEffect(1313912, 200000)
    AddSpecialEffect(1310800, 200000)
    AddSpecialEffect(1310810, 200000)
    WaitFrames(10)  # give other loaded maps time to trigger
    DisableFlag(TriggerFlags.EnemySpeedUp)
    return RESTART


@RestartOnRest
def EnemyExtremeSpeedUp():
    """ 11312201: Temporary enemy effect. """
    Await(TriggerFlags.EnemyExtremeSpeedUp)
    AddSpecialEffect(6071, 200001)
    AddSpecialEffect(6091, 200001)
    AddSpecialEffect(6101, 200001)
    AddSpecialEffect(6321, 200001)
    AddSpecialEffect(6551, 200001)
    AddSpecialEffect(1310960, 200001)
    AddSpecialEffect(1310950, 200001)
    AddSpecialEffect(1310961, 200001)
    AddSpecialEffect(1310300, 200001)
    AddSpecialEffect(1310120, 200001)
    AddSpecialEffect(1310121, 200001)
    AddSpecialEffect(1310122, 200001)
    AddSpecialEffect(1310212, 200001)
    AddSpecialEffect(1310213, 200001)
    AddSpecialEffect(1310214, 200001)
    AddSpecialEffect(1310215, 200001)
    AddSpecialEffect(1310216, 200001)
    AddSpecialEffect(1310217, 200001)
    AddSpecialEffect(1310218, 200001)
    AddSpecialEffect(1310219, 200001)
    AddSpecialEffect(1310220, 200001)
    AddSpecialEffect(1310221, 200001)
    AddSpecialEffect(1310222, 200001)
    AddSpecialEffect(1310223, 200001)
    AddSpecialEffect(1310224, 200001)
    AddSpecialEffect(1310225, 200001)
    AddSpecialEffect(1310226, 200001)
    AddSpecialEffect(1310227, 200001)
    AddSpecialEffect(1310228, 200001)
    AddSpecialEffect(1310229, 200001)
    AddSpecialEffect(1310251, 200001)
    AddSpecialEffect(1310125, 200001)
    AddSpecialEffect(1310124, 200001)
    AddSpecialEffect(1310123, 200001)
    AddSpecialEffect(1310900, 200001)
    AddSpecialEffect(1310901, 200001)
    AddSpecialEffect(1310902, 200001)
    AddSpecialEffect(1310903, 200001)
    AddSpecialEffect(1310904, 200001)
    AddSpecialEffect(1310230, 200001)
    AddSpecialEffect(1310231, 200001)
    AddSpecialEffect(1310232, 200001)
    AddSpecialEffect(1310233, 200001)
    AddSpecialEffect(1310234, 200001)
    AddSpecialEffect(1310235, 200001)
    AddSpecialEffect(1310236, 200001)
    AddSpecialEffect(1310237, 200001)
    AddSpecialEffect(1310238, 200001)
    AddSpecialEffect(1310239, 200001)
    AddSpecialEffect(1310240, 200001)
    AddSpecialEffect(1310241, 200001)
    AddSpecialEffect(1310242, 200001)
    AddSpecialEffect(1310243, 200001)
    AddSpecialEffect(1310244, 200001)
    AddSpecialEffect(1310245, 200001)
    AddSpecialEffect(1310905, 200001)
    AddSpecialEffect(1310906, 200001)
    AddSpecialEffect(1310907, 200001)
    AddSpecialEffect(1310908, 200001)
    AddSpecialEffect(1310909, 200001)
    AddSpecialEffect(1310246, 200001)
    AddSpecialEffect(1310247, 200001)
    AddSpecialEffect(1310248, 200001)
    AddSpecialEffect(1310203, 200001)
    AddSpecialEffect(1310204, 200001)
    AddSpecialEffect(1310205, 200001)
    AddSpecialEffect(1310206, 200001)
    AddSpecialEffect(1310207, 200001)
    AddSpecialEffect(1310208, 200001)
    AddSpecialEffect(1310209, 200001)
    AddSpecialEffect(1310210, 200001)
    AddSpecialEffect(1310211, 200001)
    AddSpecialEffect(1310200, 200001)
    AddSpecialEffect(1310201, 200001)
    AddSpecialEffect(1310202, 200001)
    AddSpecialEffect(1310250, 200001)
    AddSpecialEffect(1310400, 200001)
    AddSpecialEffect(1310249, 200001)
    AddSpecialEffect(1310252, 200001)
    AddSpecialEffect(1310253, 200001)
    AddSpecialEffect(1310254, 200001)
    AddSpecialEffect(1310255, 200001)
    AddSpecialEffect(1313900, 200001)
    AddSpecialEffect(1313910, 200001)
    AddSpecialEffect(1313901, 200001)
    AddSpecialEffect(1313911, 200001)
    AddSpecialEffect(1313902, 200001)
    AddSpecialEffect(1313912, 200001)
    AddSpecialEffect(1310800, 200001)
    AddSpecialEffect(1310810, 200001)
    WaitFrames(10)  # give other loaded maps time to trigger
    DisableFlag(TriggerFlags.EnemyExtremeSpeedUp)
    return RESTART


@RestartOnRest
def EnemySpeedDown():
    """ 11312202: Temporary enemy effect. """
    Await(TriggerFlags.EnemySpeedDown)
    AddSpecialEffect(6071, 200002)
    AddSpecialEffect(6091, 200002)
    AddSpecialEffect(6101, 200002)
    AddSpecialEffect(6321, 200002)
    AddSpecialEffect(6551, 200002)
    AddSpecialEffect(1310960, 200002)
    AddSpecialEffect(1310950, 200002)
    AddSpecialEffect(1310961, 200002)
    AddSpecialEffect(1310300, 200002)
    AddSpecialEffect(1310120, 200002)
    AddSpecialEffect(1310121, 200002)
    AddSpecialEffect(1310122, 200002)
    AddSpecialEffect(1310212, 200002)
    AddSpecialEffect(1310213, 200002)
    AddSpecialEffect(1310214, 200002)
    AddSpecialEffect(1310215, 200002)
    AddSpecialEffect(1310216, 200002)
    AddSpecialEffect(1310217, 200002)
    AddSpecialEffect(1310218, 200002)
    AddSpecialEffect(1310219, 200002)
    AddSpecialEffect(1310220, 200002)
    AddSpecialEffect(1310221, 200002)
    AddSpecialEffect(1310222, 200002)
    AddSpecialEffect(1310223, 200002)
    AddSpecialEffect(1310224, 200002)
    AddSpecialEffect(1310225, 200002)
    AddSpecialEffect(1310226, 200002)
    AddSpecialEffect(1310227, 200002)
    AddSpecialEffect(1310228, 200002)
    AddSpecialEffect(1310229, 200002)
    AddSpecialEffect(1310251, 200002)
    AddSpecialEffect(1310125, 200002)
    AddSpecialEffect(1310124, 200002)
    AddSpecialEffect(1310123, 200002)
    AddSpecialEffect(1310900, 200002)
    AddSpecialEffect(1310901, 200002)
    AddSpecialEffect(1310902, 200002)
    AddSpecialEffect(1310903, 200002)
    AddSpecialEffect(1310904, 200002)
    AddSpecialEffect(1310230, 200002)
    AddSpecialEffect(1310231, 200002)
    AddSpecialEffect(1310232, 200002)
    AddSpecialEffect(1310233, 200002)
    AddSpecialEffect(1310234, 200002)
    AddSpecialEffect(1310235, 200002)
    AddSpecialEffect(1310236, 200002)
    AddSpecialEffect(1310237, 200002)
    AddSpecialEffect(1310238, 200002)
    AddSpecialEffect(1310239, 200002)
    AddSpecialEffect(1310240, 200002)
    AddSpecialEffect(1310241, 200002)
    AddSpecialEffect(1310242, 200002)
    AddSpecialEffect(1310243, 200002)
    AddSpecialEffect(1310244, 200002)
    AddSpecialEffect(1310245, 200002)
    AddSpecialEffect(1310905, 200002)
    AddSpecialEffect(1310906, 200002)
    AddSpecialEffect(1310907, 200002)
    AddSpecialEffect(1310908, 200002)
    AddSpecialEffect(1310909, 200002)
    AddSpecialEffect(1310246, 200002)
    AddSpecialEffect(1310247, 200002)
    AddSpecialEffect(1310248, 200002)
    AddSpecialEffect(1310203, 200002)
    AddSpecialEffect(1310204, 200002)
    AddSpecialEffect(1310205, 200002)
    AddSpecialEffect(1310206, 200002)
    AddSpecialEffect(1310207, 200002)
    AddSpecialEffect(1310208, 200002)
    AddSpecialEffect(1310209, 200002)
    AddSpecialEffect(1310210, 200002)
    AddSpecialEffect(1310211, 200002)
    AddSpecialEffect(1310200, 200002)
    AddSpecialEffect(1310201, 200002)
    AddSpecialEffect(1310202, 200002)
    AddSpecialEffect(1310250, 200002)
    AddSpecialEffect(1310400, 200002)
    AddSpecialEffect(1310249, 200002)
    AddSpecialEffect(1310252, 200002)
    AddSpecialEffect(1310253, 200002)
    AddSpecialEffect(1310254, 200002)
    AddSpecialEffect(1310255, 200002)
    AddSpecialEffect(1313900, 200002)
    AddSpecialEffect(1313910, 200002)
    AddSpecialEffect(1313901, 200002)
    AddSpecialEffect(1313911, 200002)
    AddSpecialEffect(1313902, 200002)
    AddSpecialEffect(1313912, 200002)
    AddSpecialEffect(1310800, 200002)
    AddSpecialEffect(1310810, 200002)
    WaitFrames(10)  # give other loaded maps time to trigger
    DisableFlag(TriggerFlags.EnemySpeedDown)
    return RESTART


@RestartOnRest
def EnemyExtremeSpeedDown():
    """ 11312203: Temporary enemy effect. """
    Await(TriggerFlags.EnemyExtremeSpeedDown)
    AddSpecialEffect(6071, 200003)
    AddSpecialEffect(6091, 200003)
    AddSpecialEffect(6101, 200003)
    AddSpecialEffect(6321, 200003)
    AddSpecialEffect(6551, 200003)
    AddSpecialEffect(1310960, 200003)
    AddSpecialEffect(1310950, 200003)
    AddSpecialEffect(1310961, 200003)
    AddSpecialEffect(1310300, 200003)
    AddSpecialEffect(1310120, 200003)
    AddSpecialEffect(1310121, 200003)
    AddSpecialEffect(1310122, 200003)
    AddSpecialEffect(1310212, 200003)
    AddSpecialEffect(1310213, 200003)
    AddSpecialEffect(1310214, 200003)
    AddSpecialEffect(1310215, 200003)
    AddSpecialEffect(1310216, 200003)
    AddSpecialEffect(1310217, 200003)
    AddSpecialEffect(1310218, 200003)
    AddSpecialEffect(1310219, 200003)
    AddSpecialEffect(1310220, 200003)
    AddSpecialEffect(1310221, 200003)
    AddSpecialEffect(1310222, 200003)
    AddSpecialEffect(1310223, 200003)
    AddSpecialEffect(1310224, 200003)
    AddSpecialEffect(1310225, 200003)
    AddSpecialEffect(1310226, 200003)
    AddSpecialEffect(1310227, 200003)
    AddSpecialEffect(1310228, 200003)
    AddSpecialEffect(1310229, 200003)
    AddSpecialEffect(1310251, 200003)
    AddSpecialEffect(1310125, 200003)
    AddSpecialEffect(1310124, 200003)
    AddSpecialEffect(1310123, 200003)
    AddSpecialEffect(1310900, 200003)
    AddSpecialEffect(1310901, 200003)
    AddSpecialEffect(1310902, 200003)
    AddSpecialEffect(1310903, 200003)
    AddSpecialEffect(1310904, 200003)
    AddSpecialEffect(1310230, 200003)
    AddSpecialEffect(1310231, 200003)
    AddSpecialEffect(1310232, 200003)
    AddSpecialEffect(1310233, 200003)
    AddSpecialEffect(1310234, 200003)
    AddSpecialEffect(1310235, 200003)
    AddSpecialEffect(1310236, 200003)
    AddSpecialEffect(1310237, 200003)
    AddSpecialEffect(1310238, 200003)
    AddSpecialEffect(1310239, 200003)
    AddSpecialEffect(1310240, 200003)
    AddSpecialEffect(1310241, 200003)
    AddSpecialEffect(1310242, 200003)
    AddSpecialEffect(1310243, 200003)
    AddSpecialEffect(1310244, 200003)
    AddSpecialEffect(1310245, 200003)
    AddSpecialEffect(1310905, 200003)
    AddSpecialEffect(1310906, 200003)
    AddSpecialEffect(1310907, 200003)
    AddSpecialEffect(1310908, 200003)
    AddSpecialEffect(1310909, 200003)
    AddSpecialEffect(1310246, 200003)
    AddSpecialEffect(1310247, 200003)
    AddSpecialEffect(1310248, 200003)
    AddSpecialEffect(1310203, 200003)
    AddSpecialEffect(1310204, 200003)
    AddSpecialEffect(1310205, 200003)
    AddSpecialEffect(1310206, 200003)
    AddSpecialEffect(1310207, 200003)
    AddSpecialEffect(1310208, 200003)
    AddSpecialEffect(1310209, 200003)
    AddSpecialEffect(1310210, 200003)
    AddSpecialEffect(1310211, 200003)
    AddSpecialEffect(1310200, 200003)
    AddSpecialEffect(1310201, 200003)
    AddSpecialEffect(1310202, 200003)
    AddSpecialEffect(1310250, 200003)
    AddSpecialEffect(1310400, 200003)
    AddSpecialEffect(1310249, 200003)
    AddSpecialEffect(1310252, 200003)
    AddSpecialEffect(1310253, 200003)
    AddSpecialEffect(1310254, 200003)
    AddSpecialEffect(1310255, 200003)
    AddSpecialEffect(1313900, 200003)
    AddSpecialEffect(1313910, 200003)
    AddSpecialEffect(1313901, 200003)
    AddSpecialEffect(1313911, 200003)
    AddSpecialEffect(1313902, 200003)
    AddSpecialEffect(1313912, 200003)
    AddSpecialEffect(1310800, 200003)
    AddSpecialEffect(1310810, 200003)
    WaitFrames(10)  # give other loaded maps time to trigger
    DisableFlag(TriggerFlags.EnemyExtremeSpeedDown)
    return RESTART


@RestartOnRest
def EnemyHealthRegain():
    """ 11312204: Temporary enemy effect. """
    Await(TriggerFlags.EnemyHealthRegain)
    AddSpecialEffect(6071, 200004)
    AddSpecialEffect(6091, 200004)
    AddSpecialEffect(6101, 200004)
    AddSpecialEffect(6321, 200004)
    AddSpecialEffect(6551, 200004)
    AddSpecialEffect(1310960, 200004)
    AddSpecialEffect(1310950, 200004)
    AddSpecialEffect(1310961, 200004)
    AddSpecialEffect(1310300, 200004)
    AddSpecialEffect(1310120, 200004)
    AddSpecialEffect(1310121, 200004)
    AddSpecialEffect(1310122, 200004)
    AddSpecialEffect(1310212, 200004)
    AddSpecialEffect(1310213, 200004)
    AddSpecialEffect(1310214, 200004)
    AddSpecialEffect(1310215, 200004)
    AddSpecialEffect(1310216, 200004)
    AddSpecialEffect(1310217, 200004)
    AddSpecialEffect(1310218, 200004)
    AddSpecialEffect(1310219, 200004)
    AddSpecialEffect(1310220, 200004)
    AddSpecialEffect(1310221, 200004)
    AddSpecialEffect(1310222, 200004)
    AddSpecialEffect(1310223, 200004)
    AddSpecialEffect(1310224, 200004)
    AddSpecialEffect(1310225, 200004)
    AddSpecialEffect(1310226, 200004)
    AddSpecialEffect(1310227, 200004)
    AddSpecialEffect(1310228, 200004)
    AddSpecialEffect(1310229, 200004)
    AddSpecialEffect(1310251, 200004)
    AddSpecialEffect(1310125, 200004)
    AddSpecialEffect(1310124, 200004)
    AddSpecialEffect(1310123, 200004)
    AddSpecialEffect(1310900, 200004)
    AddSpecialEffect(1310901, 200004)
    AddSpecialEffect(1310902, 200004)
    AddSpecialEffect(1310903, 200004)
    AddSpecialEffect(1310904, 200004)
    AddSpecialEffect(1310230, 200004)
    AddSpecialEffect(1310231, 200004)
    AddSpecialEffect(1310232, 200004)
    AddSpecialEffect(1310233, 200004)
    AddSpecialEffect(1310234, 200004)
    AddSpecialEffect(1310235, 200004)
    AddSpecialEffect(1310236, 200004)
    AddSpecialEffect(1310237, 200004)
    AddSpecialEffect(1310238, 200004)
    AddSpecialEffect(1310239, 200004)
    AddSpecialEffect(1310240, 200004)
    AddSpecialEffect(1310241, 200004)
    AddSpecialEffect(1310242, 200004)
    AddSpecialEffect(1310243, 200004)
    AddSpecialEffect(1310244, 200004)
    AddSpecialEffect(1310245, 200004)
    AddSpecialEffect(1310905, 200004)
    AddSpecialEffect(1310906, 200004)
    AddSpecialEffect(1310907, 200004)
    AddSpecialEffect(1310908, 200004)
    AddSpecialEffect(1310909, 200004)
    AddSpecialEffect(1310246, 200004)
    AddSpecialEffect(1310247, 200004)
    AddSpecialEffect(1310248, 200004)
    AddSpecialEffect(1310203, 200004)
    AddSpecialEffect(1310204, 200004)
    AddSpecialEffect(1310205, 200004)
    AddSpecialEffect(1310206, 200004)
    AddSpecialEffect(1310207, 200004)
    AddSpecialEffect(1310208, 200004)
    AddSpecialEffect(1310209, 200004)
    AddSpecialEffect(1310210, 200004)
    AddSpecialEffect(1310211, 200004)
    AddSpecialEffect(1310200, 200004)
    AddSpecialEffect(1310201, 200004)
    AddSpecialEffect(1310202, 200004)
    AddSpecialEffect(1310250, 200004)
    AddSpecialEffect(1310400, 200004)
    AddSpecialEffect(1310249, 200004)
    AddSpecialEffect(1310252, 200004)
    AddSpecialEffect(1310253, 200004)
    AddSpecialEffect(1310254, 200004)
    AddSpecialEffect(1310255, 200004)
    AddSpecialEffect(1313900, 200004)
    AddSpecialEffect(1313910, 200004)
    AddSpecialEffect(1313901, 200004)
    AddSpecialEffect(1313911, 200004)
    AddSpecialEffect(1313902, 200004)
    AddSpecialEffect(1313912, 200004)
    AddSpecialEffect(1310800, 200004)
    AddSpecialEffect(1310810, 200004)
    WaitFrames(10)  # give other loaded maps time to trigger
    DisableFlag(TriggerFlags.EnemyHealthRegain)
    return RESTART


@RestartOnRest
def EnemyMaxHealthUp():
    """ 11312205: Temporary enemy effect. """
    Await(TriggerFlags.EnemyMaxHealthUp)
    AddSpecialEffect(6071, 200005)
    AddSpecialEffect(6091, 200005)
    AddSpecialEffect(6101, 200005)
    AddSpecialEffect(6321, 200005)
    AddSpecialEffect(6551, 200005)
    AddSpecialEffect(1310960, 200005)
    AddSpecialEffect(1310950, 200005)
    AddSpecialEffect(1310961, 200005)
    AddSpecialEffect(1310300, 200005)
    AddSpecialEffect(1310120, 200005)
    AddSpecialEffect(1310121, 200005)
    AddSpecialEffect(1310122, 200005)
    AddSpecialEffect(1310212, 200005)
    AddSpecialEffect(1310213, 200005)
    AddSpecialEffect(1310214, 200005)
    AddSpecialEffect(1310215, 200005)
    AddSpecialEffect(1310216, 200005)
    AddSpecialEffect(1310217, 200005)
    AddSpecialEffect(1310218, 200005)
    AddSpecialEffect(1310219, 200005)
    AddSpecialEffect(1310220, 200005)
    AddSpecialEffect(1310221, 200005)
    AddSpecialEffect(1310222, 200005)
    AddSpecialEffect(1310223, 200005)
    AddSpecialEffect(1310224, 200005)
    AddSpecialEffect(1310225, 200005)
    AddSpecialEffect(1310226, 200005)
    AddSpecialEffect(1310227, 200005)
    AddSpecialEffect(1310228, 200005)
    AddSpecialEffect(1310229, 200005)
    AddSpecialEffect(1310251, 200005)
    AddSpecialEffect(1310125, 200005)
    AddSpecialEffect(1310124, 200005)
    AddSpecialEffect(1310123, 200005)
    AddSpecialEffect(1310900, 200005)
    AddSpecialEffect(1310901, 200005)
    AddSpecialEffect(1310902, 200005)
    AddSpecialEffect(1310903, 200005)
    AddSpecialEffect(1310904, 200005)
    AddSpecialEffect(1310230, 200005)
    AddSpecialEffect(1310231, 200005)
    AddSpecialEffect(1310232, 200005)
    AddSpecialEffect(1310233, 200005)
    AddSpecialEffect(1310234, 200005)
    AddSpecialEffect(1310235, 200005)
    AddSpecialEffect(1310236, 200005)
    AddSpecialEffect(1310237, 200005)
    AddSpecialEffect(1310238, 200005)
    AddSpecialEffect(1310239, 200005)
    AddSpecialEffect(1310240, 200005)
    AddSpecialEffect(1310241, 200005)
    AddSpecialEffect(1310242, 200005)
    AddSpecialEffect(1310243, 200005)
    AddSpecialEffect(1310244, 200005)
    AddSpecialEffect(1310245, 200005)
    AddSpecialEffect(1310905, 200005)
    AddSpecialEffect(1310906, 200005)
    AddSpecialEffect(1310907, 200005)
    AddSpecialEffect(1310908, 200005)
    AddSpecialEffect(1310909, 200005)
    AddSpecialEffect(1310246, 200005)
    AddSpecialEffect(1310247, 200005)
    AddSpecialEffect(1310248, 200005)
    AddSpecialEffect(1310203, 200005)
    AddSpecialEffect(1310204, 200005)
    AddSpecialEffect(1310205, 200005)
    AddSpecialEffect(1310206, 200005)
    AddSpecialEffect(1310207, 200005)
    AddSpecialEffect(1310208, 200005)
    AddSpecialEffect(1310209, 200005)
    AddSpecialEffect(1310210, 200005)
    AddSpecialEffect(1310211, 200005)
    AddSpecialEffect(1310200, 200005)
    AddSpecialEffect(1310201, 200005)
    AddSpecialEffect(1310202, 200005)
    AddSpecialEffect(1310250, 200005)
    AddSpecialEffect(1310400, 200005)
    AddSpecialEffect(1310249, 200005)
    AddSpecialEffect(1310252, 200005)
    AddSpecialEffect(1310253, 200005)
    AddSpecialEffect(1310254, 200005)
    AddSpecialEffect(1310255, 200005)
    AddSpecialEffect(1313900, 200005)
    AddSpecialEffect(1313910, 200005)
    AddSpecialEffect(1313901, 200005)
    AddSpecialEffect(1313911, 200005)
    AddSpecialEffect(1313902, 200005)
    AddSpecialEffect(1313912, 200005)
    AddSpecialEffect(1310800, 200005)
    AddSpecialEffect(1310810, 200005)
    WaitFrames(10)  # give other loaded maps time to trigger
    DisableFlag(TriggerFlags.EnemyMaxHealthUp)
    return RESTART


@RestartOnRest
def EnemyMaxHealthDown():
    """ 11312206: Temporary enemy effect. """
    Await(TriggerFlags.EnemyMaxHealthDown)
    AddSpecialEffect(6071, 200006)
    AddSpecialEffect(6091, 200006)
    AddSpecialEffect(6101, 200006)
    AddSpecialEffect(6321, 200006)
    AddSpecialEffect(6551, 200006)
    AddSpecialEffect(1310960, 200006)
    AddSpecialEffect(1310950, 200006)
    AddSpecialEffect(1310961, 200006)
    AddSpecialEffect(1310300, 200006)
    AddSpecialEffect(1310120, 200006)
    AddSpecialEffect(1310121, 200006)
    AddSpecialEffect(1310122, 200006)
    AddSpecialEffect(1310212, 200006)
    AddSpecialEffect(1310213, 200006)
    AddSpecialEffect(1310214, 200006)
    AddSpecialEffect(1310215, 200006)
    AddSpecialEffect(1310216, 200006)
    AddSpecialEffect(1310217, 200006)
    AddSpecialEffect(1310218, 200006)
    AddSpecialEffect(1310219, 200006)
    AddSpecialEffect(1310220, 200006)
    AddSpecialEffect(1310221, 200006)
    AddSpecialEffect(1310222, 200006)
    AddSpecialEffect(1310223, 200006)
    AddSpecialEffect(1310224, 200006)
    AddSpecialEffect(1310225, 200006)
    AddSpecialEffect(1310226, 200006)
    AddSpecialEffect(1310227, 200006)
    AddSpecialEffect(1310228, 200006)
    AddSpecialEffect(1310229, 200006)
    AddSpecialEffect(1310251, 200006)
    AddSpecialEffect(1310125, 200006)
    AddSpecialEffect(1310124, 200006)
    AddSpecialEffect(1310123, 200006)
    AddSpecialEffect(1310900, 200006)
    AddSpecialEffect(1310901, 200006)
    AddSpecialEffect(1310902, 200006)
    AddSpecialEffect(1310903, 200006)
    AddSpecialEffect(1310904, 200006)
    AddSpecialEffect(1310230, 200006)
    AddSpecialEffect(1310231, 200006)
    AddSpecialEffect(1310232, 200006)
    AddSpecialEffect(1310233, 200006)
    AddSpecialEffect(1310234, 200006)
    AddSpecialEffect(1310235, 200006)
    AddSpecialEffect(1310236, 200006)
    AddSpecialEffect(1310237, 200006)
    AddSpecialEffect(1310238, 200006)
    AddSpecialEffect(1310239, 200006)
    AddSpecialEffect(1310240, 200006)
    AddSpecialEffect(1310241, 200006)
    AddSpecialEffect(1310242, 200006)
    AddSpecialEffect(1310243, 200006)
    AddSpecialEffect(1310244, 200006)
    AddSpecialEffect(1310245, 200006)
    AddSpecialEffect(1310905, 200006)
    AddSpecialEffect(1310906, 200006)
    AddSpecialEffect(1310907, 200006)
    AddSpecialEffect(1310908, 200006)
    AddSpecialEffect(1310909, 200006)
    AddSpecialEffect(1310246, 200006)
    AddSpecialEffect(1310247, 200006)
    AddSpecialEffect(1310248, 200006)
    AddSpecialEffect(1310203, 200006)
    AddSpecialEffect(1310204, 200006)
    AddSpecialEffect(1310205, 200006)
    AddSpecialEffect(1310206, 200006)
    AddSpecialEffect(1310207, 200006)
    AddSpecialEffect(1310208, 200006)
    AddSpecialEffect(1310209, 200006)
    AddSpecialEffect(1310210, 200006)
    AddSpecialEffect(1310211, 200006)
    AddSpecialEffect(1310200, 200006)
    AddSpecialEffect(1310201, 200006)
    AddSpecialEffect(1310202, 200006)
    AddSpecialEffect(1310250, 200006)
    AddSpecialEffect(1310400, 200006)
    AddSpecialEffect(1310249, 200006)
    AddSpecialEffect(1310252, 200006)
    AddSpecialEffect(1310253, 200006)
    AddSpecialEffect(1310254, 200006)
    AddSpecialEffect(1310255, 200006)
    AddSpecialEffect(1313900, 200006)
    AddSpecialEffect(1313910, 200006)
    AddSpecialEffect(1313901, 200006)
    AddSpecialEffect(1313911, 200006)
    AddSpecialEffect(1313902, 200006)
    AddSpecialEffect(1313912, 200006)
    AddSpecialEffect(1310800, 200006)
    AddSpecialEffect(1310810, 200006)
    WaitFrames(10)  # give other loaded maps time to trigger
    DisableFlag(TriggerFlags.EnemyMaxHealthDown)
    return RESTART


@RestartOnRest
def EnemyDefenseUp():
    """ 11312207: Temporary enemy effect. """
    Await(TriggerFlags.EnemyDefenseUp)
    AddSpecialEffect(6071, 200007)
    AddSpecialEffect(6091, 200007)
    AddSpecialEffect(6101, 200007)
    AddSpecialEffect(6321, 200007)
    AddSpecialEffect(6551, 200007)
    AddSpecialEffect(1310960, 200007)
    AddSpecialEffect(1310950, 200007)
    AddSpecialEffect(1310961, 200007)
    AddSpecialEffect(1310300, 200007)
    AddSpecialEffect(1310120, 200007)
    AddSpecialEffect(1310121, 200007)
    AddSpecialEffect(1310122, 200007)
    AddSpecialEffect(1310212, 200007)
    AddSpecialEffect(1310213, 200007)
    AddSpecialEffect(1310214, 200007)
    AddSpecialEffect(1310215, 200007)
    AddSpecialEffect(1310216, 200007)
    AddSpecialEffect(1310217, 200007)
    AddSpecialEffect(1310218, 200007)
    AddSpecialEffect(1310219, 200007)
    AddSpecialEffect(1310220, 200007)
    AddSpecialEffect(1310221, 200007)
    AddSpecialEffect(1310222, 200007)
    AddSpecialEffect(1310223, 200007)
    AddSpecialEffect(1310224, 200007)
    AddSpecialEffect(1310225, 200007)
    AddSpecialEffect(1310226, 200007)
    AddSpecialEffect(1310227, 200007)
    AddSpecialEffect(1310228, 200007)
    AddSpecialEffect(1310229, 200007)
    AddSpecialEffect(1310251, 200007)
    AddSpecialEffect(1310125, 200007)
    AddSpecialEffect(1310124, 200007)
    AddSpecialEffect(1310123, 200007)
    AddSpecialEffect(1310900, 200007)
    AddSpecialEffect(1310901, 200007)
    AddSpecialEffect(1310902, 200007)
    AddSpecialEffect(1310903, 200007)
    AddSpecialEffect(1310904, 200007)
    AddSpecialEffect(1310230, 200007)
    AddSpecialEffect(1310231, 200007)
    AddSpecialEffect(1310232, 200007)
    AddSpecialEffect(1310233, 200007)
    AddSpecialEffect(1310234, 200007)
    AddSpecialEffect(1310235, 200007)
    AddSpecialEffect(1310236, 200007)
    AddSpecialEffect(1310237, 200007)
    AddSpecialEffect(1310238, 200007)
    AddSpecialEffect(1310239, 200007)
    AddSpecialEffect(1310240, 200007)
    AddSpecialEffect(1310241, 200007)
    AddSpecialEffect(1310242, 200007)
    AddSpecialEffect(1310243, 200007)
    AddSpecialEffect(1310244, 200007)
    AddSpecialEffect(1310245, 200007)
    AddSpecialEffect(1310905, 200007)
    AddSpecialEffect(1310906, 200007)
    AddSpecialEffect(1310907, 200007)
    AddSpecialEffect(1310908, 200007)
    AddSpecialEffect(1310909, 200007)
    AddSpecialEffect(1310246, 200007)
    AddSpecialEffect(1310247, 200007)
    AddSpecialEffect(1310248, 200007)
    AddSpecialEffect(1310203, 200007)
    AddSpecialEffect(1310204, 200007)
    AddSpecialEffect(1310205, 200007)
    AddSpecialEffect(1310206, 200007)
    AddSpecialEffect(1310207, 200007)
    AddSpecialEffect(1310208, 200007)
    AddSpecialEffect(1310209, 200007)
    AddSpecialEffect(1310210, 200007)
    AddSpecialEffect(1310211, 200007)
    AddSpecialEffect(1310200, 200007)
    AddSpecialEffect(1310201, 200007)
    AddSpecialEffect(1310202, 200007)
    AddSpecialEffect(1310250, 200007)
    AddSpecialEffect(1310400, 200007)
    AddSpecialEffect(1310249, 200007)
    AddSpecialEffect(1310252, 200007)
    AddSpecialEffect(1310253, 200007)
    AddSpecialEffect(1310254, 200007)
    AddSpecialEffect(1310255, 200007)
    AddSpecialEffect(1313900, 200007)
    AddSpecialEffect(1313910, 200007)
    AddSpecialEffect(1313901, 200007)
    AddSpecialEffect(1313911, 200007)
    AddSpecialEffect(1313902, 200007)
    AddSpecialEffect(1313912, 200007)
    AddSpecialEffect(1310800, 200007)
    AddSpecialEffect(1310810, 200007)
    WaitFrames(10)  # give other loaded maps time to trigger
    DisableFlag(TriggerFlags.EnemyDefenseUp)
    return RESTART
