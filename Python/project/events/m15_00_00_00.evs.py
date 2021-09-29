"""
linked:


strings:

"""
from soulstruct.darksouls1r.events import *
from ..entities.m15_00_00_00_entities import *
from ..entities.common_entities import *


def Constructor():
    """ 0: Event 0 """
    CreateProjectileOwner(Characters.c2690_0000)
    SetNetworkUpdateRate(Characters.c2860_0001, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    RegisterBonfire(
        11500984,
        obj=Objects.o0200_0002,
        reaction_distance=2.0,
        reaction_angle=180.0,
        initial_kindle_level=0,
    )
    RegisterLadder(start_climbing_flag=11500010, stop_climbing_flag=11500011, obj=Objects.o5400_0000)
    RegisterLadder(start_climbing_flag=11500012, stop_climbing_flag=11500013, obj=Objects.o5401_0000)
    RegisterLadder(start_climbing_flag=11500014, stop_climbing_flag=11500015, obj=Objects.o5404_0000)
    RegisterLadder(start_climbing_flag=11500016, stop_climbing_flag=11500017, obj=Objects.o5403_0000)
    SkipLinesIfHost(2)
    EnableFlag(11505240)
    DisableFlag(11505360)
    SkipLinesIfClient(2)
    DisableObject(Objects.o5151_0000)
    DeleteVFX(VFX.MultiplayerFog1, erase_root_only=False)
    DisableCollision(Collisions.h0110B0_0000)
    DisableObject(Objects.o5010_0000)
    DisableObject(Objects.o5010_0001)
    DisableObject(Objects.o5010_0002)
    DisableObject(Objects.o5010_0003)
    DisableObject(Objects.o5010_0004)
    DisableObject(Objects.o5010_0005)
    DisableObject(Objects.o5010_0006)
    DisableObject(Objects.o5010_0007)
    SkipLinesIfFlagOn(1, 11500803)
    EndOfAnimation(Objects.o5200_0000, 3)
    SkipLinesIfFlagOff(1, 11500806)
    EndOfAnimation(Objects.o5200_0000, 0)
    SkipLinesIfFlagOff(1, 11500809)
    EndOfAnimation(Objects.o5200_0000, 1)
    SkipLinesIfFlagOff(1, 11500812)
    EndOfAnimation(Objects.o5200_0000, 2)
    DisableCollision(Collisions.h0081B0_0000)
    DisableCollision(Collisions.h0081B0_0001)
    DisableCollision(Collisions.h0081B0_0002)
    SkipLinesIfFlagOff(3, 11500821)
    EnableObject(Objects.o5010_0001)
    EndOfAnimation(Objects.o5010_0001, 5)
    EnableCollision(Collisions.h0081B0_0000)
    SkipLinesIfFlagOff(3, 11500822)
    EnableObject(Objects.o5010_0002)
    EndOfAnimation(Objects.o5010_0002, 6)
    EnableCollision(Collisions.h0081B0_0001)
    SkipLinesIfFlagOff(3, 11500823)
    EnableObject(Objects.o5010_0003)
    EndOfAnimation(Objects.o5010_0003, 7)
    EnableCollision(Collisions.h0081B0_0002)
    SkipLinesIfFlagOff(21, 11500100)
    SkipLinesIfFlagOn(10, 11500101)
    EnableNavmeshType(Navigation.Navmesh_CageElevator_0_0, NavmeshType.Wall)
    EnableNavmeshType(Navigation.Navmesh_CageElevator_0_1, NavmeshType.WallTouchingFloor)
    EnableNavmeshType(Navigation.Navmesh_CageElevator_1_0, NavmeshType.WallTouchingFloor)
    EnableNavmeshType(Navigation.Navmesh_CageElevator_1_1, NavmeshType.Wall)
    EnableNavmeshType(Navigation.Navmesh_CageElevator_2_0, NavmeshType.WallTouchingFloor)
    EnableNavmeshType(Navigation.Navmesh_CageElevator_2_1, NavmeshType.Wall)
    EnableNavmeshType(Navigation.Navmesh_CageElevator_3_0, NavmeshType.Wall)
    EnableNavmeshType(Navigation.Navmesh_CageElevator_3_1, NavmeshType.WallTouchingFloor)
    EndOfAnimation(Objects.o5301_0000, 12)
    SkipLines(9)
    EnableNavmeshType(Navigation.Navmesh_CageElevator_0_0, NavmeshType.WallTouchingFloor)
    EnableNavmeshType(Navigation.Navmesh_CageElevator_0_1, NavmeshType.Wall)
    EnableNavmeshType(Navigation.Navmesh_CageElevator_1_0, NavmeshType.Wall)
    EnableNavmeshType(Navigation.Navmesh_CageElevator_1_1, NavmeshType.WallTouchingFloor)
    EnableNavmeshType(Navigation.Navmesh_CageElevator_2_0, NavmeshType.Wall)
    EnableNavmeshType(Navigation.Navmesh_CageElevator_2_1, NavmeshType.WallTouchingFloor)
    EnableNavmeshType(Navigation.Navmesh_CageElevator_3_0, NavmeshType.WallTouchingFloor)
    EnableNavmeshType(Navigation.Navmesh_CageElevator_3_1, NavmeshType.Wall)
    EndOfAnimation(Objects.o5301_0000, 11)
    SkipLines(4)
    EnableNavmeshType(Navigation.Navmesh_CageElevator_0_0, NavmeshType.Solid)
    EnableNavmeshType(Navigation.Navmesh_CageElevator_1_0, NavmeshType.Solid)
    EnableNavmeshType(Navigation.Navmesh_CageElevator_2_0, NavmeshType.Solid)
    EnableNavmeshType(Navigation.Navmesh_CageElevator_3_0, NavmeshType.Solid)
    RunEvent(
        11500090,
        slot=0,
        args=(Objects.o5152_0000, VFX.CheckpointFog1, Boxes.CheckpointFog1FrontSide, Boxes.CheckpointFog1BackSide),
    )
    RunEvent(
        11500090,
        slot=1,
        args=(Objects.o5153_0000, VFX.CheckpointFog2, Boxes.CheckpointFog2FrontSide, Boxes.CheckpointFog2BackSide),
    )
    RunEvent(11505090)
    RunEvent(11505091)
    RunEvent(11505092)
    RunEvent(11500201)
    RunEvent(11505300)
    RunEvent(11500840)
    RunEvent(11500841, slot=0, args=(11500803,))
    RunEvent(11500841, slot=1, args=(11500806,))
    RunEvent(11500841, slot=2, args=(11500809,))
    RunEvent(11500841, slot=3, args=(11500812,))
    RunEvent(11500790)
    RunEvent(11500791)
    RunEvent(11500795)
    RunEvent(11500796)
    RunEvent(11500797)
    RunEvent(11500798)
    RunEvent(11500830)
    RunEvent(11500831)
    RunEvent(11500850)
    RunEvent(11505255)
    RunEvent(11500100)
    RunEvent(11500102)
    RunEvent(11500103)
    RunEvent(11500106)
    RunEvent(11500107)
    RunEvent(11500110, slot=0, args=(Objects.o5310_0002, 11500110))
    RunEvent(11500110, slot=1, args=(Objects.o5310_0003, 11500111))
    RunEvent(11500110, slot=2, args=(Objects.o5310_0004, 11500112))
    RunEvent(11500110, slot=3, args=(Objects.o5310_0006, 11500113))
    RunEvent(11500110, slot=5, args=(Objects.o5310_0012, 11500115))
    RunEvent(11500110, slot=6, args=(Objects.o5310_0017, 11500116))
    RunEvent(11505050)
    RunEvent(11505051)
    RunEvent(11505055)
    RunEvent(11505110)
    RunEvent(11505101)
    RunEvent(11505102)
    RunEvent(11505111, slot=0, args=(11505111, Boxes.BombTargetA, 1))
    RunEvent(11505111, slot=1, args=(11505112, Boxes.BombTargetB, 2))
    RunEvent(11505111, slot=2, args=(11505113, Boxes.BombTargetC, 3))
    RunEvent(11505111, slot=3, args=(11505114, Boxes.BombTargetD, 4))
    RunEvent(11505111, slot=4, args=(11505115, Boxes.BombTargetE, 5))
    RunEvent(11505111, slot=5, args=(11505116, Boxes.BombTargetF, 6))
    RunEvent(11505111, slot=6, args=(11505117, Boxes.BombGiantCombatArea, -1))
    RunEvent(11505060, slot=0, args=(Characters.c2860_0001,))
    RunEvent(11505060, slot=1, args=(Characters.c2860_0000,))
    RunEvent(11505060, slot=2, args=(Characters.c2860_0003,))
    RunEvent(11505070, slot=0, args=(Characters.c2860_0001,))
    RunEvent(11505070, slot=1, args=(Characters.c2860_0000,))
    RunEvent(11505070, slot=2, args=(Characters.c2860_0003,))
    RunEvent(11505080)
    RunEvent(11500210)
    RunEvent(11500835)
    DisableSoundEvent(1503800)
    SkipLinesIfFlagOff(4, 11)
    RunEvent(11505392)
    DisableObject(Objects.o5150_0000)
    DeleteVFX(VFX.IronGolemEntranceFog, erase_root_only=False)
    SkipLines(9)
    RunEvent(11505390)
    RunEvent(11505391)
    RunEvent(11505393)
    RunEvent(11505392)
    RunEvent(11500001)
    RunEvent(11505394)
    RunEvent(11505395)
    RunEvent(11505350)
    RunEvent(11505353)
    RunEvent(11505010)
    RunEvent(11505011)
    RunEvent(11505012)
    RunEvent(11505013)
    RunEvent(11505014)
    RunEvent(11500900)
    RunEvent(11505015)
    RunEvent(
        11505270,
        slot=0,
        args=(Boxes.ArrowTrapTriggerA, Objects.o5500_0000, VFX.ArrowTriggerA, Objects.o5510_0000, 0, 11505280),
    )
    RunEvent(
        11505270,
        slot=1,
        args=(Boxes.ArrowTrapTriggerB, Objects.o5501_0001, VFX.ArrowTriggerA, Objects.o5510_0001, 90, 11505281),
    )
    RunEvent(
        11505270,
        slot=2,
        args=(Boxes.ArrowTrapTriggerC, Objects.o5501_0002, VFX.ArrowTriggerA, Objects.o5510_0002, 90, 11505282),
    )
    RunEvent(
        11505270,
        slot=3,
        args=(Boxes.ArrowTrapTriggerD, Objects.o5501_0003, VFX.ArrowTriggerA, Objects.o5510_0003, 270, 11505283),
    )
    RunEvent(
        11505270,
        slot=4,
        args=(Boxes.ArrowTrapTriggerE, Objects.o5501_0004, VFX.ArrowTriggerA, Objects.o5510_0004, 180, 11505284),
    )
    RunEvent(
        11505270,
        slot=5,
        args=(Boxes.ArrowTrapTriggerF, Objects.o5501_0005, VFX.ArrowTriggerA, Objects.o5510_0003, 270, 11505285),
    )
    RunEvent(11505260)
    RunEvent(11500860, slot=0, args=(Characters.c0000_0009,))
    RunEvent(11500860, slot=1, args=(Characters.c2300_0000,))
    RunEvent(11500860, slot=2, args=(Characters.c2300_0001,))
    RunEvent(11500860, slot=3, args=(Characters.c2300_0002,))
    RunEvent(11500860, slot=4, args=(Characters.c2300_0003,))
    RunEvent(11500860, slot=5, args=(Characters.c2860_0001,))
    RunEvent(11500860, slot=7, args=(Characters.c2860_0003,))
    RunEvent(11500600, slot=0, args=(Objects.o0110_0000, 11500600))
    RunEvent(11500600, slot=2, args=(Objects.o0110_0002, 11500602))
    RunEvent(11500600, slot=4, args=(Objects.o0110_0004, 11500604))
    RunEvent(11500600, slot=9, args=(Objects.o0110_0009, 11500609))
    RunEvent(11500600, slot=10, args=(Objects.o0110_0010, 11500610))
    RunEvent(
        11505843,
        slot=0,
        args=(11, Objects.o5150_0000, Boxes.IronGolemFogPrompt, Boxes.IronGolemFogRotationTarget),
    )
    RunEvent(11505846, slot=0, args=(11, Objects.o5150_0000, VFX.IronGolemEntranceFog))
    
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
    HumanityRegistration(Characters.c0000_0009, 8980)
    HumanityRegistration(Characters.c0000_0007, 8924)
    RunEvent(11505030)
    RunEvent(11505029)
    RunEvent(11505032)
    RunEvent(11505990, slot=0, args=(11505031, Characters.c0000_0007))
    HumanityRegistration(Characters.c0000_0004, 8334)
    SkipLinesIfFlagOn(3, 1090)
    SkipLinesIfFlagOn(2, 1091)
    SkipLinesIfFlagOn(1, 1096)
    DisableCharacter(Characters.c0000_0004)
    RunEvent(11500510, slot=0, args=(Characters.c0000_0004, 1096))
    RunEvent(11500520, slot=0, args=(Characters.c0000_0004, 1090, 1109, 1097))
    RunEvent(11500530)
    RunEvent(11500531, slot=0, args=(Characters.c0000_0004, 1090, 1109, 1091))
    RunEvent(11500532, slot=0, args=(Characters.c0000_0004, 1090, 1109, 1092))
    SetTeamTypeAndExitStandbyAnimation(Characters.c0000_0008, TeamType.HostileAlly)
    SkipLinesIfFlagOn(1, 1117)
    DisableCharacter(Characters.c0000_0008)
    RunEvent(11500520, slot=1, args=(Characters.c0000_0008, 1110, 1119, 1115))
    RunEvent(11500533, slot=0, args=(Characters.c0000_0008, 1110, 1119, 1117))
    HumanityRegistration(Characters.c0000_0006, 8446)
    SkipLinesIfFlagOn(3, 1514)
    SkipLinesIfFlagOn(2, 1513)
    SkipLinesIfFlagRangeAnyOn(1, (1493, 1511))
    SkipLines(1)
    DisableCharacter(Characters.c0000_0006)
    SkipLinesIfFlagOn(1, 11500200)
    SkipLines(1)
    Move(
        Characters.c0000_0006,
        destination=Boxes.SiegmeyerMovement,
        destination_type=CoordEntityType.Region,
        set_draw_parent=Collisions.h0060B0_0000,
    )
    SkipLinesIfFlagRangeAnyOn(1, (1491, 1492))
    SkipLines(2)
    Kill(Characters.c2690_0006, award_souls=False)
    Kill(Characters.c2690_0007, award_souls=False)
    RunEvent(11500510, slot=2, args=(Characters.c0000_0006, 1512))
    RunEvent(11500520, slot=2, args=(Characters.c0000_0006, 1490, 1539, 1513))
    RunEvent(11500534, slot=0, args=(Characters.c0000_0006, 1490, 1539, 1491))
    RunEvent(11500535, slot=0, args=(Characters.c0000_0006, 1490, 1539, 1492))
    RunEvent(11500536, slot=0, args=(Characters.c0000_0006, 1490, 1539, 1493))
    HumanityRegistration(Characters.c0000_0005, 8422)
    SkipLinesIfFlagRangeAnyOn(1, (1420, 1429))
    EnableFlag(1420)
    RunEvent(11500510, slot=3, args=(Characters.c0000_0005, 1421))
    RunEvent(11500520, slot=3, args=(Characters.c0000_0005, 1420, 1429, 1422))


def Event1000000000():
    """ 1000000000: Event 1000000000 """
    DisableCharacter(Characters.c2690_0000)
    SetNetworkUpdateRate(Characters.c2860_0001, is_fixed=True, update_rate=CharacterUpdateRate.Always)


def Event11500090(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11500090: Event 11500090 """
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


def Event11505300():
    """ 11505300: Event 11505300 """
    CreateHazard(
        11505301,
        Objects.o5000_0000,
        model_point=101,
        behavior_param_id=5040,
        target_type=DamageTargetType.Character,
        radius=0.30000001192092896,
        life=0.0,
        repetition_time=2.0,
    )
    CreateHazard(
        11505302,
        Objects.o5000_0001,
        model_point=101,
        behavior_param_id=5040,
        target_type=DamageTargetType.Character,
        radius=0.30000001192092896,
        life=0.0,
        repetition_time=2.0,
    )
    CreateHazard(
        11505303,
        Objects.o5000_0002,
        model_point=101,
        behavior_param_id=5040,
        target_type=DamageTargetType.Character,
        radius=0.30000001192092896,
        life=0.0,
        repetition_time=2.0,
    )
    CreateHazard(
        11505304,
        Objects.o5000_0003,
        model_point=101,
        behavior_param_id=5040,
        target_type=DamageTargetType.Character,
        radius=0.30000001192092896,
        life=0.0,
        repetition_time=2.0,
    )
    CreateHazard(
        11505305,
        Objects.o5000_0004,
        model_point=101,
        behavior_param_id=5040,
        target_type=DamageTargetType.Character,
        radius=0.30000001192092896,
        life=0.0,
        repetition_time=2.0,
    )
    CreateHazard(
        11505306,
        Objects.o5000_0010,
        model_point=101,
        behavior_param_id=5040,
        target_type=DamageTargetType.Character,
        radius=0.30000001192092896,
        life=0.0,
        repetition_time=2.0,
    )
    CreateHazard(
        11505307,
        Objects.o5000_0011,
        model_point=101,
        behavior_param_id=5040,
        target_type=DamageTargetType.Character,
        radius=0.30000001192092896,
        life=0.0,
        repetition_time=2.0,
    )
    CreateHazard(
        11505308,
        Objects.o5000_0012,
        model_point=101,
        behavior_param_id=5040,
        target_type=DamageTargetType.Character,
        radius=0.30000001192092896,
        life=0.0,
        repetition_time=2.0,
    )
    CreateHazard(
        11505309,
        Objects.o5000_0013,
        model_point=101,
        behavior_param_id=5040,
        target_type=DamageTargetType.Character,
        radius=0.30000001192092896,
        life=0.0,
        repetition_time=2.0,
    )
    CreateHazard(
        11505310,
        Objects.o5000_0020,
        model_point=101,
        behavior_param_id=5040,
        target_type=DamageTargetType.Character,
        radius=0.30000001192092896,
        life=0.0,
        repetition_time=2.0,
    )
    CreateHazard(
        11505311,
        Objects.o5000_0021,
        model_point=101,
        behavior_param_id=5040,
        target_type=DamageTargetType.Character,
        radius=0.30000001192092896,
        life=0.0,
        repetition_time=2.0,
    )
    CreateHazard(
        11505312,
        Objects.o5000_0022,
        model_point=101,
        behavior_param_id=5040,
        target_type=DamageTargetType.Character,
        radius=0.30000001192092896,
        life=0.0,
        repetition_time=2.0,
    )
    CreateHazard(
        11505313,
        Objects.o5000_0023,
        model_point=101,
        behavior_param_id=5040,
        target_type=DamageTargetType.Character,
        radius=0.30000001192092896,
        life=0.0,
        repetition_time=2.0,
    )
    CreateHazard(
        11505314,
        Objects.o5000_0030,
        model_point=101,
        behavior_param_id=5040,
        target_type=DamageTargetType.Character,
        radius=0.30000001192092896,
        life=0.0,
        repetition_time=2.0,
    )
    CreateHazard(
        11505315,
        Objects.o5000_0031,
        model_point=101,
        behavior_param_id=5040,
        target_type=DamageTargetType.Character,
        radius=0.30000001192092896,
        life=0.0,
        repetition_time=2.0,
    )
    CreateHazard(
        11505316,
        Objects.o5000_0032,
        model_point=101,
        behavior_param_id=5040,
        target_type=DamageTargetType.Character,
        radius=0.30000001192092896,
        life=0.0,
        repetition_time=2.0,
    )
    CreateHazard(
        11505317,
        Objects.o5000_0033,
        model_point=101,
        behavior_param_id=5040,
        target_type=DamageTargetType.Character,
        radius=0.30000001192092896,
        life=0.0,
        repetition_time=2.0,
    )
    CreateHazard(
        11505290,
        Objects.o5300_0000,
        model_point=101,
        behavior_param_id=5060,
        target_type=DamageTargetType.Character,
        radius=1.2000000476837158,
        life=0.0,
        repetition_time=0.5,
    )


def Event11505390():
    """ 11505390: Event 11505390 """
    IfFlagOff(1, 11)
    IfActionButton(
        1,
        prompt_text=10010403,
        anchor_entity=Boxes.IronGolemFogPrompt,
        anchor_type=CoordEntityType.Region,
        line_intersects=Objects.o5150_0000,
        boss_version=True,
    )
    IfConditionTrue(0, input_condition=1)
    RotateToFaceEntity(PLAYER, Boxes.IronGolemFogRotationTarget)
    ForceAnimation(PLAYER, 7410)
    Restart()


def Event11505391():
    """ 11505391: Event 11505391 """
    IfFlagOff(1, 11)
    IfFlagOn(1, 11505393)
    IfCharacterType(1, PLAYER, CharacterType.WhitePhantom)
    IfActionButton(
        1,
        prompt_text=10010403,
        anchor_entity=Boxes.IronGolemFogPrompt,
        anchor_type=CoordEntityType.Region,
        trigger_attribute=TriggerAttribute.All,
        line_intersects=Objects.o5150_0000,
    )
    IfConditionTrue(0, input_condition=1)
    RotateToFaceEntity(PLAYER, Boxes.IronGolemFogRotationTarget)
    ForceAnimation(PLAYER, 7410)
    Restart()


def Event11505393():
    """ 11505393: Event 11505393 """
    SkipLinesIfThisEventOn(3)
    IfFlagOff(1, 11)
    IfCharacterInsideRegion(1, PLAYER, region=Boxes.IronGolemCombatStart)
    IfConditionTrue(0, input_condition=1)
    SkipLinesIfClient(1)
    NotifyBossBattleStart()
    ActivateMultiplayerBuffs(Characters.c2320_0000)


@RestartOnRest
def Event11505392():
    """ 11505392: Event 11505392 """
    SkipLinesIfFlagOff(7, 11)
    DisableCharacter(Characters.c2320_0000)
    DropMandatoryTreasure(Characters.c2320_0000)
    DisableBackread(Characters.c2320_0000)
    IfCharacterBackreadEnabled(0, Characters.c2860_0001)
    AICommand(Characters.c2860_0001, command_id=10, slot=0)
    ReplanAI(Characters.c2860_0001)
    End()
    DisableAI(Characters.c2320_0000)
    SetStandbyAnimationSettings(Characters.c2320_0000, standby_animation=9000)
    RunEvent(11505351)
    RunEvent(11505352)
    IfFlagOn(1, 11505393)
    IfCharacterInsideRegion(1, PLAYER, region=Boxes.IronGolemCombatStart)
    IfConditionTrue(0, input_condition=1)
    EnableAI(Characters.c2320_0000)
    SetStandbyAnimationSettings(Characters.c2320_0000, cancel_animation=9060)
    EnableBossHealthBar(Characters.c2320_0000, name=2320, slot=0)


def Event11500001():
    """ 11500001: Event 11500001 """
    DeleteVFX(VFX.AnorLondoWarpRing, erase_root_only=False)
    IfCharacterDead(0, Characters.c2320_0000)
    EnableFlag(11)
    KillBoss(1500800)
    DisableObject(Objects.o5150_0000)
    DeleteVFX(VFX.IronGolemEntranceFog, erase_root_only=True)
    CreateVFX(VFX.AnorLondoWarpRing)
    AICommand(Characters.c2860_0001, command_id=10, slot=0)
    ReplanAI(Characters.c2860_0001)
    DisableFlag(11807020)
    DisableFlag(11807030)
    DisableFlag(11807040)
    DisableFlag(11807050)
    DisableNetworkSync()
    Wait(3.0)
    DisableCharacter(Characters.c2320_0000)
    DisableBackread(Characters.c2320_0000)


def Event11505394():
    """ 11505394: Event 11505394 """
    DisableNetworkSync()
    IfFlagOff(1, 11)
    IfFlagOn(1, 11505392)
    SkipLinesIfHost(1)
    IfFlagOn(1, 11505391)
    IfCharacterInsideRegion(1, PLAYER, region=Boxes.IronGolemCombatStart)
    IfCharacterAlive(1, Characters.c2320_0000)
    IfConditionTrue(0, input_condition=1)
    EnableSoundEvent(1503800)


def Event11505395():
    """ 11505395: Event 11505395 """
    DisableNetworkSync()
    IfFlagOn(1, 11)
    IfFlagOn(1, 11505394)
    IfConditionTrue(0, input_condition=1)
    DisableSoundEvent(1503800)
    PlaySoundEffect(anchor_entity=Boxes.IronGolemMusic, sound_type=SoundType.a_Ambient, sound_id=150100002)


def Event11505350():
    """ 11505350: Event 11505350 """
    EndIfClient()
    IfHasTAEEvent(0, Characters.c2320_0000, tae_event_id=100)
    IfCharacterDead(0, Characters.c2320_0000)


@UnknownRestart
def Event11505351():
    """ 11505351: Event 11505351 """
    EndIfFlagOn(11)
    EnableNetworkSync()
    IfFlagOff(0, 11505355)
    CreateNPCPart(
        Characters.c2320_0000,
        npc_part_id=2320,
        part_index=NPCPartType.Part2,
        part_health=200,
        damage_correction=1.0,
        body_damage_correction=1.0,
        is_invincible=False,
        start_in_stop_state=False,
    )
    SetNPCPartEffects(Characters.c2320_0000, npc_part_id=2320, material_sfx_id=56, material_vfx_id=56)
    IfCharacterPartHealthLessThanOrEqual(0, Characters.c2320_0000, npc_part_id=2320, value=0)
    EzstateAIRequest(Characters.c2320_0000, command_id=1300, slot=0)
    IfHasTAEEvent(0, Characters.c2320_0000, tae_event_id=1204)
    EnableFlag(11505355)
    CreateNPCPart(
        Characters.c2320_0000,
        npc_part_id=2321,
        part_index=NPCPartType.Part2,
        part_health=100,
        damage_correction=1.0,
        body_damage_correction=1.0,
        is_invincible=False,
        start_in_stop_state=False,
    )
    SetNPCPartEffects(Characters.c2320_0000, npc_part_id=2321, material_sfx_id=56, material_vfx_id=56)
    DisableNetworkSync()
    Wait(15.0)
    EnableNetworkSync()
    DisableFlag(11505355)
    RestartEvent(11505352)
    SetNPCPartHealth(Characters.c2320_0000, npc_part_id=2321, desired_health=-1, overwrite_max=False)
    EzstateAIRequest(Characters.c2320_0000, command_id=1303, slot=0)
    Restart()


@UnknownRestart
def Event11505352():
    """ 11505352: Event 11505352 """
    EndIfFlagOn(11)
    EnableNetworkSync()
    IfFlagOn(0, 11505355)
    IfFlagOn(1, 11505355)
    IfCharacterPartHealthLessThanOrEqual(1, Characters.c2320_0000, npc_part_id=2321, value=0)
    IfConditionTrue(0, input_condition=1)
    RestartEvent(11505351)
    EzstateAIRequest(Characters.c2320_0000, command_id=1301, slot=0)
    IfHasTAEEvent(0, Characters.c2320_0000, tae_event_id=1203)
    DisableNetworkSync()
    Wait(15.0)
    EnableNetworkSync()
    EzstateAIRequest(Characters.c2320_0000, command_id=1304, slot=0)
    DisableFlag(11505355)
    Restart()


def Event11505353():
    """ 11505353: Event 11505353 """
    IfHasTAEEvent(1, Characters.c2320_0000, tae_event_id=400)
    IfHasTAEEvent(2, Characters.c2320_0000, tae_event_id=300)
    IfHealthLessThanOrEqual(3, Characters.c2320_0000, 0.0)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionFalse(2, 1)
    DisableCollision(Collisions.h1100B0_0000)
    SkipLines(1)
    EnableCollision(Collisions.h1100B0_0000)
    EndIfFinishedConditionTrue(3)
    IfDoesNotHaveTAEEvent(4, Characters.c2320_0000, tae_event_id=400)
    IfDoesNotHaveTAEEvent(4, Characters.c2320_0000, tae_event_id=300)
    IfConditionTrue(0, input_condition=4)
    Restart()


def Event11500201():
    """ 11500201: Event 11500201 """
    SkipLinesIfFlagOff(1, 11500200)
    EndOfAnimation(Objects.o5100_0000, 0)
    IfCharacterInsideRegion(0, PLAYER, region=Boxes.GateInitialization)
    IfCharacterOutsideRegion(0, PLAYER, region=Boxes.GateInitialization)
    Restart()


def Event11500790():
    """ 11500790: Event 11500790 """
    IfFlagOn(0, 11500791)
    IfFlagOff(1, 11505050)
    IfCharacterAlive(1, Characters.c2860_0000)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(11505052)
    Wait(5.0)
    EnableObject(Objects.o5010_0000)
    ForceAnimation(Objects.o5010_0000, 0)
    Wait(1.5)
    EnableCollision(Collisions.h0110B0_0000)
    Wait(3.5)
    WaitForNetworkApproval(max_seconds=10.0)
    SkipLinesIfFlagOn(2, 11505210)
    EnableFlag(11505220)
    Restart()
    SkipLinesIfFlagOn(2, 11505211)
    EnableFlag(11505221)
    Restart()
    SkipLinesIfFlagOn(2, 11505212)
    EnableFlag(11505222)
    Restart()
    SkipLinesIfFlagOn(1, 11505213)
    EnableFlag(11505223)
    Restart()


@RestartOnRest
def Event11500791():
    """ 11500791: Event 11500791 """
    SkipLinesIfThisEventOff(2)
    DisableCharacter(Characters.c2690_0004)
    End()
    DisableAI(Characters.c2690_0004)
    IfCharacterInsideRegion(0, PLAYER, region=Boxes.BoulderCrushesSerpentTrigger)
    EnableFlag(11500791)
    EnableObject(Objects.o5010_0000)
    ForceAnimation(Characters.c2690_0004, 500, wait_for_completion=True)
    ForceAnimation(Characters.c2690_0004, 603, wait_for_completion=True)
    EnableAI(Characters.c2690_0004)
    CreateHazard(
        11505200,
        Objects.o5010_0000,
        model_point=101,
        behavior_param_id=5050,
        target_type=DamageTargetType.Character,
        radius=1.7000000476837158,
        life=1.0,
        repetition_time=0.0,
    )
    ForceAnimation(Objects.o5010_0000, 12, wait_for_completion=True)
    DisableObject(Objects.o5010_0000)


def Event11500795():
    """ 11500795: Event 11500795 """
    IfFlagOn(0, 11505220)
    DisableFlag(11505220)
    EnableFlag(11505210)
    DisableObject(Objects.o5010_0000)
    EnableObject(Objects.o5010_0004)
    SkipLinesIfFlagOff(3, 11500812)
    RunEvent(
        11500700,
        slot=0,
        args=(11505200, Objects.o5010_0004, 1, 2.5, Objects.o5210_0002, 11505210),
        arg_types="iiifii",
    )
    IfFlagOff(0, 11505210)
    Restart()
    SkipLinesIfFlagOn(3, 11500803)
    RunEvent(
        11500700,
        slot=10,
        args=(11505200, Objects.o5010_0004, 2, 7.5, Objects.o5210_0003, 11505210),
        arg_types="iiifii",
    )
    IfFlagOff(0, 11505210)
    Restart()
    SkipLinesIfFlagOff(3, 11500806)
    RunEvent(
        11500700,
        slot=20,
        args=(11505200, Objects.o5010_0004, 3, 7.5, Objects.o5210_0000, 11505210),
        arg_types="iiifii",
    )
    IfFlagOff(0, 11505210)
    Restart()
    SkipLinesIfFlagOn(3, 11500830)
    RunEvent(
        11500700,
        slot=30,
        args=(11505200, Objects.o5010_0004, 4, 12.5, Objects.o5210_0001, 11505210),
        arg_types="iiifii",
    )
    IfFlagOff(0, 11505210)
    Restart()
    SkipLinesIfFlagOn(3, 11500821)
    RunEvent(
        11500750,
        slot=0,
        args=(
            11505200,
            Objects.o5010_0001,
            5,
            Collisions.h0081B0_0000,
            Objects.o5210_0001,
            11505210,
            11500821,
            Objects.o5010_0004,
        ),
    )
    IfFlagOff(0, 11505210)
    Restart()
    SkipLinesIfFlagOn(3, 11500822)
    RunEvent(
        11500750,
        slot=1,
        args=(
            11505200,
            Objects.o5010_0002,
            6,
            Collisions.h0081B0_0001,
            Objects.o5210_0001,
            11505210,
            11500822,
            Objects.o5010_0004,
        ),
    )
    IfFlagOff(0, 11505210)
    Restart()
    SkipLinesIfFlagOn(3, 11500823)
    RunEvent(
        11500750,
        slot=2,
        args=(
            11505200,
            Objects.o5010_0003,
            7,
            Collisions.h0081B0_0002,
            Objects.o5210_0001,
            11505210,
            11500823,
            Objects.o5010_0004,
        ),
    )
    IfFlagOff(0, 11505210)
    Restart()
    RunEvent(
        11500700,
        slot=40,
        args=(11505200, Objects.o5010_0004, 8, 18.5, Objects.o5210_0001, 11505210),
        arg_types="iiifii",
    )
    IfFlagOff(0, 11505210)
    Restart()


def Event11500796():
    """ 11500796: Event 11500796 """
    IfFlagOn(0, 11505221)
    DisableFlag(11505221)
    EnableFlag(11505211)
    DisableObject(Objects.o5010_0000)
    EnableObject(Objects.o5010_0005)
    SkipLinesIfFlagOff(3, 11500812)
    RunEvent(
        11500700,
        slot=1,
        args=(11505201, Objects.o5010_0005, 1, 2.5, Objects.o5210_0002, 11505211),
        arg_types="iiifii",
    )
    IfFlagOff(0, 11505211)
    Restart()
    SkipLinesIfFlagOn(3, 11500803)
    RunEvent(
        11500700,
        slot=11,
        args=(11505201, Objects.o5010_0005, 2, 7.5, Objects.o5210_0003, 11505211),
        arg_types="iiifii",
    )
    IfFlagOff(0, 11505211)
    Restart()
    SkipLinesIfFlagOff(3, 11500806)
    RunEvent(
        11500700,
        slot=21,
        args=(11505201, Objects.o5010_0005, 3, 7.5, Objects.o5210_0000, 11505211),
        arg_types="iiifii",
    )
    IfFlagOff(0, 11505211)
    Restart()
    SkipLinesIfFlagOn(3, 11500830)
    RunEvent(
        11500700,
        slot=31,
        args=(11505201, Objects.o5010_0005, 4, 12.5, Objects.o5210_0001, 11505211),
        arg_types="iiifii",
    )
    IfFlagOff(0, 11505211)
    Restart()
    SkipLinesIfFlagOn(3, 11500821)
    RunEvent(
        11500750,
        slot=0,
        args=(
            11505201,
            Objects.o5010_0001,
            5,
            Collisions.h0081B0_0000,
            Objects.o5210_0001,
            11505211,
            11500821,
            Objects.o5010_0005,
        ),
    )
    IfFlagOff(0, 11505211)
    Restart()
    SkipLinesIfFlagOn(3, 11500822)
    RunEvent(
        11500750,
        slot=1,
        args=(
            11505201,
            Objects.o5010_0002,
            6,
            Collisions.h0081B0_0001,
            Objects.o5210_0001,
            11505211,
            11500822,
            Objects.o5010_0005,
        ),
    )
    IfFlagOff(0, 11505211)
    Restart()
    SkipLinesIfFlagOn(3, 11500823)
    RunEvent(
        11500750,
        slot=2,
        args=(
            11505201,
            Objects.o5010_0003,
            7,
            Collisions.h0081B0_0002,
            Objects.o5210_0001,
            11505211,
            11500823,
            Objects.o5010_0005,
        ),
    )
    IfFlagOff(0, 11505211)
    Restart()
    RunEvent(
        11500700,
        slot=41,
        args=(11505201, Objects.o5010_0005, 8, 18.5, Objects.o5210_0001, 11505211),
        arg_types="iiifii",
    )
    IfFlagOff(0, 11505211)
    Restart()


def Event11500797():
    """ 11500797: Event 11500797 """
    IfFlagOn(0, 11505222)
    DisableFlag(11505222)
    EnableFlag(11505212)
    DisableObject(Objects.o5010_0000)
    EnableObject(Objects.o5010_0006)
    SkipLinesIfFlagOff(3, 11500812)
    RunEvent(
        11500700,
        slot=2,
        args=(11505202, Objects.o5010_0006, 1, 2.5, Objects.o5210_0002, 11505212),
        arg_types="iiifii",
    )
    IfFlagOff(0, 11505212)
    Restart()
    SkipLinesIfFlagOn(3, 11500803)
    RunEvent(
        11500700,
        slot=12,
        args=(11505202, Objects.o5010_0006, 2, 7.5, Objects.o5210_0003, 11505212),
        arg_types="iiifii",
    )
    IfFlagOff(0, 11505212)
    Restart()
    SkipLinesIfFlagOff(3, 11500806)
    RunEvent(
        11500700,
        slot=22,
        args=(11505202, Objects.o5010_0006, 3, 7.5, Objects.o5210_0000, 11505212),
        arg_types="iiifii",
    )
    IfFlagOff(0, 11505212)
    Restart()
    SkipLinesIfFlagOn(3, 11500830)
    RunEvent(
        11500700,
        slot=32,
        args=(11505202, Objects.o5010_0006, 4, 12.5, Objects.o5210_0001, 11505212),
        arg_types="iiifii",
    )
    IfFlagOff(0, 11505212)
    Restart()
    SkipLinesIfFlagOn(3, 11500821)
    RunEvent(
        11500750,
        slot=0,
        args=(
            11505202,
            Objects.o5010_0001,
            5,
            Collisions.h0081B0_0000,
            Objects.o5210_0001,
            11505212,
            11500821,
            Objects.o5010_0006,
        ),
    )
    IfFlagOff(0, 11505212)
    Restart()
    SkipLinesIfFlagOn(3, 11500822)
    RunEvent(
        11500750,
        slot=1,
        args=(
            11505202,
            Objects.o5010_0002,
            6,
            Collisions.h0081B0_0001,
            Objects.o5210_0001,
            11505212,
            11500822,
            Objects.o5010_0006,
        ),
    )
    IfFlagOff(0, 11505212)
    Restart()
    SkipLinesIfFlagOn(3, 11500823)
    RunEvent(
        11500750,
        slot=2,
        args=(
            11505202,
            Objects.o5010_0003,
            7,
            Collisions.h0081B0_0002,
            Objects.o5210_0001,
            11505212,
            11500823,
            Objects.o5010_0006,
        ),
    )
    IfFlagOff(0, 11505212)
    Restart()
    RunEvent(
        11500700,
        slot=42,
        args=(11505202, Objects.o5010_0006, 8, 18.5, Objects.o5210_0001, 11505212),
        arg_types="iiifii",
    )
    IfFlagOff(0, 11505212)
    Restart()


def Event11500798():
    """ 11500798: Event 11500798 """
    IfFlagOn(0, 11505223)
    DisableFlag(11505223)
    EnableFlag(11505213)
    DisableObject(Objects.o5010_0000)
    EnableObject(Objects.o5010_0007)
    SkipLinesIfFlagOff(3, 11500812)
    RunEvent(
        11500700,
        slot=3,
        args=(11505203, Objects.o5010_0007, 1, 2.5, Objects.o5210_0002, 11505213),
        arg_types="iiifii",
    )
    IfFlagOff(0, 11505213)
    Restart()
    SkipLinesIfFlagOn(3, 11500803)
    RunEvent(
        11500700,
        slot=13,
        args=(11505203, Objects.o5010_0007, 2, 7.5, Objects.o5210_0003, 11505213),
        arg_types="iiifii",
    )
    IfFlagOff(0, 11505213)
    Restart()
    SkipLinesIfFlagOff(3, 11500806)
    RunEvent(
        11500700,
        slot=23,
        args=(11505203, Objects.o5010_0007, 3, 7.5, Objects.o5210_0000, 11505213),
        arg_types="iiifii",
    )
    IfFlagOff(0, 11505213)
    Restart()
    SkipLinesIfFlagOn(3, 11500830)
    RunEvent(
        11500700,
        slot=33,
        args=(11505203, Objects.o5010_0007, 4, 12.5, Objects.o5210_0001, 11505213),
        arg_types="iiifii",
    )
    IfFlagOff(0, 11505213)
    Restart()
    SkipLinesIfFlagOn(3, 11500821)
    RunEvent(
        11500750,
        slot=0,
        args=(
            11505203,
            Objects.o5010_0001,
            5,
            Collisions.h0081B0_0000,
            Objects.o5210_0001,
            11505213,
            11500821,
            Objects.o5010_0007,
        ),
    )
    IfFlagOff(0, 11505213)
    Restart()
    SkipLinesIfFlagOn(3, 11500822)
    RunEvent(
        11500750,
        slot=1,
        args=(
            11505203,
            Objects.o5010_0002,
            6,
            Collisions.h0081B0_0001,
            Objects.o5210_0001,
            11505213,
            11500822,
            Objects.o5010_0007,
        ),
    )
    IfFlagOff(0, 11505213)
    Restart()
    SkipLinesIfFlagOn(3, 11500823)
    RunEvent(
        11500750,
        slot=2,
        args=(
            11505203,
            Objects.o5010_0003,
            7,
            Collisions.h0081B0_0002,
            Objects.o5210_0001,
            11505213,
            11500823,
            Objects.o5010_0007,
        ),
    )
    IfFlagOff(0, 11505213)
    Restart()
    RunEvent(
        11500700,
        slot=43,
        args=(11505203, Objects.o5010_0007, 8, 18.5, Objects.o5210_0001, 11505213),
        arg_types="iiifii",
    )
    IfFlagOff(0, 11505213)
    Restart()


def Event11500700(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: float, arg_16_19: int, arg_20_23: int):
    """ 11500700: Event 11500700 """
    DisableCollision(Collisions.h0110B0_0000)
    ForceAnimation(arg_16_19, 1)
    CreateHazard(
        arg_0_3,
        arg_4_7,
        model_point=101,
        behavior_param_id=5050,
        target_type=DamageTargetType.Character,
        radius=1.7000000476837158,
        life=arg_12_15,
        repetition_time=0.20000000298023224,
    )
    ForceAnimation(arg_4_7, arg_8_11, wait_for_completion=True)
    RemoveObjectFlag(arg_0_3)
    DisableObject(arg_4_7)
    EndOfAnimation(arg_4_7, 0)
    DisableFlag(arg_20_23)


def Event11500750(
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
    """ 11500750: Event 11500750 """
    DisableCollision(Collisions.h0110B0_0000)
    EnableFlag(arg_24_27)
    EnableObject(arg_4_7)
    DisableObject(arg_28_31)
    ForceAnimation(arg_16_19, 1)
    CreateHazard(
        arg_0_3,
        arg_4_7,
        model_point=101,
        behavior_param_id=5050,
        target_type=DamageTargetType.Character,
        radius=1.7000000476837158,
        life=12.5,
        repetition_time=0.20000000298023224,
    )
    ForceAnimation(arg_4_7, arg_8_11, wait_for_completion=True)
    EnableCollision(arg_12_15)
    RemoveObjectFlag(arg_0_3)
    DisableFlag(arg_20_23)


def Event11500830():
    """ 11500830: Event 11500830 """
    IfCharacterInsideRegion(0, PLAYER, region=Boxes.BoulderPitStackingTrigger)
    EnableFlag(11500830)


def Event11500831():
    """ 11500831: Event 11500831 """
    DisableNetworkSync()
    IfFlagOn(1, 11500751)
    IfCharacterInsideRegion(1, PLAYER, region=Boxes.BoulderPitCrushed1)
    IfFlagOn(2, 11500752)
    IfCharacterInsideRegion(2, PLAYER, region=Boxes.BoulderPitCrushed2)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    Kill(PLAYER, award_souls=False)


def Event11500850():
    """ 11500850: Event 11500850 """
    DisableFlag(11505250)
    IfFlagOff(1, 11505250)
    IfActionButton(
        1,
        prompt_text=10010502,
        anchor_entity=Objects.o5200_0000,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        model_point=104,
        trigger_attribute=TriggerAttribute.All,
    )
    IfFlagOff(2, 11505250)
    IfActionButton(
        2,
        prompt_text=10010502,
        anchor_entity=Objects.o5200_0000,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        model_point=102,
        trigger_attribute=TriggerAttribute.All,
    )
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    WaitForNetworkApproval(max_seconds=3.0)
    EnableFlag(11505250)
    DisableFlag(11505251)
    DisableFlag(11505252)
    SkipLinesIfFinishedConditionFalse(23, 1)
    Move(
        PLAYER,
        destination=Objects.o5200_0000,
        destination_type=CoordEntityType.Object,
        model_point=101,
        short_move=True,
    )
    ForceAnimation(PLAYER, 8020)
    CreateTemporaryVFX(150001, anchor_entity=Objects.o5200_0000, anchor_type=CoordEntityType.Object, model_point=-1)
    SkipLinesIfFlagOff(4, 11500812)
    DisableFlag(11500812)
    DisableFlag(11500803)
    ForceAnimation(Objects.o5200_0000, 3, wait_for_completion=True)
    Restart()
    SkipLinesIfFlagOff(4, 11500809)
    DisableFlag(11500809)
    EnableFlag(11500812)
    ForceAnimation(Objects.o5200_0000, 2, wait_for_completion=True)
    Restart()
    SkipLinesIfFlagOff(4, 11500806)
    DisableFlag(11500806)
    EnableFlag(11500809)
    ForceAnimation(Objects.o5200_0000, 1, wait_for_completion=True)
    Restart()
    SkipLinesIfFlagOn(4, 11500803)
    EnableFlag(11500803)
    EnableFlag(11500806)
    ForceAnimation(Objects.o5200_0000, 0, wait_for_completion=True)
    Restart()
    RestartIfFinishedConditionFalse(2)
    Move(
        PLAYER,
        destination=Objects.o5200_0000,
        destination_type=CoordEntityType.Object,
        model_point=103,
        short_move=True,
    )
    ForceAnimation(PLAYER, 8021)
    CreateTemporaryVFX(150001, anchor_entity=Objects.o5200_0000, anchor_type=CoordEntityType.Object, model_point=-1)
    SkipLinesIfFlagOff(4, 11500812)
    DisableFlag(11500812)
    EnableFlag(11500809)
    ForceAnimation(Objects.o5200_0000, 5, wait_for_completion=True)
    Restart()
    SkipLinesIfFlagOn(4, 11500803)
    EnableFlag(11500803)
    EnableFlag(11500812)
    ForceAnimation(Objects.o5200_0000, 4, wait_for_completion=True)
    Restart()
    SkipLinesIfFlagOff(4, 11500806)
    DisableFlag(11500806)
    DisableFlag(11500803)
    ForceAnimation(Objects.o5200_0000, 7, wait_for_completion=True)
    Restart()
    SkipLinesIfFlagOff(4, 11500809)
    DisableFlag(11500809)
    EnableFlag(11500806)
    ForceAnimation(Objects.o5200_0000, 6, wait_for_completion=True)
    Restart()
    EnableFlag(11500802)
    Restart()


def Event11505255():
    """ 11505255: Event 11505255 """
    IfFlagOff(1, 11505250)
    IfFlagOff(1, 11505251)
    IfFlagOff(1, 11500809)
    IfTimeElapsed(1, 2.0)
    IfCharacterInsideRegion(1, PLAYER, region=Boxes.AutoBouldersInside)
    IfFlagOff(2, 11505250)
    IfFlagOff(2, 11505252)
    IfFlagOn(2, 11500803)
    IfTimeElapsed(2, 2.0)
    IfCharacterInsideRegion(2, PLAYER, region=Boxes.AutoBouldersOutside)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    WaitForNetworkApproval(max_seconds=3.0)
    EnableFlag(11505250)
    SkipLinesIfFinishedConditionTrue(19, 2)
    EnableFlag(11505251)
    DisableFlag(11505252)
    SkipLinesIfFlagOn(5, 11500803)
    CreateTemporaryVFX(150001, anchor_entity=Objects.o5200_0000, anchor_type=CoordEntityType.Object, model_point=-1)
    EnableFlag(11500803)
    EnableFlag(11500809)
    ForceAnimation(Objects.o5200_0000, 0, wait_for_completion=True)
    ForceAnimation(Objects.o5200_0000, 1, wait_for_completion=True)
    SkipLinesIfFlagOff(4, 11500806)
    CreateTemporaryVFX(150001, anchor_entity=Objects.o5200_0000, anchor_type=CoordEntityType.Object, model_point=-1)
    DisableFlag(11500806)
    EnableFlag(11500809)
    ForceAnimation(Objects.o5200_0000, 1, wait_for_completion=True)
    SkipLinesIfFlagOff(4, 11500812)
    CreateTemporaryVFX(150001, anchor_entity=Objects.o5200_0000, anchor_type=CoordEntityType.Object, model_point=-1)
    DisableFlag(11500812)
    EnableFlag(11500809)
    ForceAnimation(Objects.o5200_0000, 5, wait_for_completion=True)
    SkipLines(18)
    DisableFlag(11505251)
    EnableFlag(11505252)
    SkipLinesIfFlagOff(5, 11500809)
    CreateTemporaryVFX(150001, anchor_entity=Objects.o5200_0000, anchor_type=CoordEntityType.Object, model_point=-1)
    DisableFlag(11500809)
    DisableFlag(11500803)
    ForceAnimation(Objects.o5200_0000, 6, wait_for_completion=True)
    ForceAnimation(Objects.o5200_0000, 7, wait_for_completion=True)
    SkipLinesIfFlagOff(4, 11500806)
    CreateTemporaryVFX(150001, anchor_entity=Objects.o5200_0000, anchor_type=CoordEntityType.Object, model_point=-1)
    DisableFlag(11500806)
    DisableFlag(11500803)
    ForceAnimation(Objects.o5200_0000, 7, wait_for_completion=True)
    SkipLinesIfFlagOff(4, 11500812)
    CreateTemporaryVFX(150001, anchor_entity=Objects.o5200_0000, anchor_type=CoordEntityType.Object, model_point=-1)
    DisableFlag(11500812)
    DisableFlag(11500803)
    ForceAnimation(Objects.o5200_0000, 3, wait_for_completion=True)
    DisableFlag(11505250)
    Restart()


def Event11500840():
    """ 11500840: Event 11500840 """
    IfFlagOn(0, 11505240)
    EnableFlag(11505240)
    IfFlagOff(0, 11505240)
    Restart()


def Event11500841(_, arg_0_3: int):
    """ 11500841: Event 11500841 """
    IfHost(1)
    IfFlagOn(1, 11505240)
    IfFlagOff(1, arg_0_3)
    IfHost(2)
    IfFlagOn(2, 11505240)
    IfFlagOn(2, arg_0_3)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    DisableFlag(11505240)
    SkipLinesIfFinishedConditionTrue(2, 2)
    DisableFlag(arg_0_3)
    SkipLines(1)
    EnableFlag(arg_0_3)
    Restart()


def Event11500835():
    """ 11500835: Event 11500835 """
    EndIfHost()
    WaitFrames(10)
    EnableFlag(11505360)
    IfFlagOn(1, 11505250)
    IfFlagOff(2, 11505250)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionTrue(1, 2)
    Wait(3.0)
    SkipLinesIfFlagOn(1, 11500803)
    EndOfAnimation(Objects.o5200_0000, 3)
    SkipLinesIfFlagOff(1, 11500806)
    EndOfAnimation(Objects.o5200_0000, 0)
    SkipLinesIfFlagOff(1, 11500809)
    EndOfAnimation(Objects.o5200_0000, 1)
    SkipLinesIfFlagOff(1, 11500812)
    EndOfAnimation(Objects.o5200_0000, 2)


def Event11500100():
    """ 11500100: Event 11500100 """
    IfThisEventOff(1)
    IfCharacterInsideRegion(1, PLAYER, region=Spheres.CageElevatorStart_UpperLeft)
    IfThisEventOn(2)
    IfFlagOff(2, 11500101)
    IfCharacterInsideRegion(2, PLAYER, region=Spheres.CageElevatorStart_UpperRight)
    IfThisEventOn(3)
    IfFlagOff(3, 11500101)
    IfCharacterInsideRegion(3, PLAYER, region=Spheres.CageElevatorStart_LowerLeft)
    IfThisEventOn(4)
    IfFlagOn(4, 11500101)
    IfCharacterInsideRegion(4, PLAYER, region=Spheres.CageElevatorStart_UpperLeft)
    IfThisEventOn(5)
    IfFlagOn(5, 11500101)
    IfCharacterInsideRegion(5, PLAYER, region=Spheres.CageElevatorStart_LowerRight)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(-1, input_condition=4)
    IfConditionTrue(-1, input_condition=5)
    IfConditionTrue(0, input_condition=-1)
    WaitForNetworkApproval(max_seconds=3.0)
    EnableNavmeshType(Navigation.Navmesh_CageElevator_0_0, NavmeshType.Solid)
    EnableNavmeshType(Navigation.Navmesh_CageElevator_1_0, NavmeshType.Solid)
    EnableNavmeshType(Navigation.Navmesh_CageElevator_2_0, NavmeshType.Solid)
    EnableNavmeshType(Navigation.Navmesh_CageElevator_3_0, NavmeshType.Solid)
    SkipLinesIfFinishedConditionFalse(16, 1)
    EnableFlag(11500100)
    ForceAnimation(Objects.o5301_0000, 0, wait_for_completion=True)
    DisableNavmeshType(Navigation.Navmesh_CageElevator_0_0, NavmeshType.Solid)
    DisableNavmeshType(Navigation.Navmesh_CageElevator_1_0, NavmeshType.Solid)
    DisableNavmeshType(Navigation.Navmesh_CageElevator_2_0, NavmeshType.Solid)
    DisableNavmeshType(Navigation.Navmesh_CageElevator_3_0, NavmeshType.Solid)
    EnableNavmeshType(Navigation.Navmesh_CageElevator_0_0, NavmeshType.Wall)
    EnableNavmeshType(Navigation.Navmesh_CageElevator_0_1, NavmeshType.WallTouchingFloor)
    EnableNavmeshType(Navigation.Navmesh_CageElevator_1_0, NavmeshType.WallTouchingFloor)
    EnableNavmeshType(Navigation.Navmesh_CageElevator_1_1, NavmeshType.Wall)
    EnableNavmeshType(Navigation.Navmesh_CageElevator_2_0, NavmeshType.WallTouchingFloor)
    EnableNavmeshType(Navigation.Navmesh_CageElevator_2_1, NavmeshType.Wall)
    EnableNavmeshType(Navigation.Navmesh_CageElevator_3_0, NavmeshType.Wall)
    EnableNavmeshType(Navigation.Navmesh_CageElevator_3_1, NavmeshType.WallTouchingFloor)
    IfAllPlayersOutsideRegion(0, region=Spheres.CageElevatorStart_LowerLeft)
    Restart()
    SkipLinesIfFinishedConditionTrue(27, 4)
    SkipLinesIfFinishedConditionTrue(26, 5)
    EnableFlag(11500101)
    DisableNavmeshType(Navigation.Navmesh_CageElevator_0_0, NavmeshType.Wall)
    DisableNavmeshType(Navigation.Navmesh_CageElevator_0_1, NavmeshType.WallTouchingFloor)
    DisableNavmeshType(Navigation.Navmesh_CageElevator_1_0, NavmeshType.WallTouchingFloor)
    DisableNavmeshType(Navigation.Navmesh_CageElevator_1_1, NavmeshType.Wall)
    DisableNavmeshType(Navigation.Navmesh_CageElevator_2_0, NavmeshType.WallTouchingFloor)
    DisableNavmeshType(Navigation.Navmesh_CageElevator_2_1, NavmeshType.Wall)
    DisableNavmeshType(Navigation.Navmesh_CageElevator_3_0, NavmeshType.Wall)
    DisableNavmeshType(Navigation.Navmesh_CageElevator_3_1, NavmeshType.WallTouchingFloor)
    ForceAnimation(Objects.o5301_0000, 1, wait_for_completion=True)
    DisableNavmeshType(Navigation.Navmesh_CageElevator_0_0, NavmeshType.Solid)
    DisableNavmeshType(Navigation.Navmesh_CageElevator_1_0, NavmeshType.Solid)
    DisableNavmeshType(Navigation.Navmesh_CageElevator_2_0, NavmeshType.Solid)
    DisableNavmeshType(Navigation.Navmesh_CageElevator_3_0, NavmeshType.Solid)
    EnableNavmeshType(Navigation.Navmesh_CageElevator_0_0, NavmeshType.WallTouchingFloor)
    EnableNavmeshType(Navigation.Navmesh_CageElevator_0_1, NavmeshType.Wall)
    EnableNavmeshType(Navigation.Navmesh_CageElevator_1_0, NavmeshType.Wall)
    EnableNavmeshType(Navigation.Navmesh_CageElevator_1_1, NavmeshType.WallTouchingFloor)
    EnableNavmeshType(Navigation.Navmesh_CageElevator_2_0, NavmeshType.Wall)
    EnableNavmeshType(Navigation.Navmesh_CageElevator_2_1, NavmeshType.WallTouchingFloor)
    EnableNavmeshType(Navigation.Navmesh_CageElevator_3_0, NavmeshType.WallTouchingFloor)
    EnableNavmeshType(Navigation.Navmesh_CageElevator_3_1, NavmeshType.Wall)
    IfAllPlayersOutsideRegion(6, region=Spheres.CageElevatorStart_UpperLeft)
    IfAllPlayersOutsideRegion(6, region=Spheres.CageElevatorStart_LowerRight)
    IfConditionTrue(0, input_condition=6)
    Restart()
    DisableFlag(11500101)
    DisableNavmeshType(Navigation.Navmesh_CageElevator_0_0, NavmeshType.WallTouchingFloor)
    DisableNavmeshType(Navigation.Navmesh_CageElevator_0_1, NavmeshType.Wall)
    DisableNavmeshType(Navigation.Navmesh_CageElevator_1_0, NavmeshType.Wall)
    DisableNavmeshType(Navigation.Navmesh_CageElevator_1_1, NavmeshType.WallTouchingFloor)
    DisableNavmeshType(Navigation.Navmesh_CageElevator_2_0, NavmeshType.Wall)
    DisableNavmeshType(Navigation.Navmesh_CageElevator_2_1, NavmeshType.WallTouchingFloor)
    DisableNavmeshType(Navigation.Navmesh_CageElevator_3_0, NavmeshType.WallTouchingFloor)
    DisableNavmeshType(Navigation.Navmesh_CageElevator_3_1, NavmeshType.Wall)
    ForceAnimation(Objects.o5301_0000, 2, wait_for_completion=True)
    DisableNavmeshType(Navigation.Navmesh_CageElevator_0_0, NavmeshType.Solid)
    DisableNavmeshType(Navigation.Navmesh_CageElevator_1_0, NavmeshType.Solid)
    DisableNavmeshType(Navigation.Navmesh_CageElevator_2_0, NavmeshType.Solid)
    DisableNavmeshType(Navigation.Navmesh_CageElevator_3_0, NavmeshType.Solid)
    EnableNavmeshType(Navigation.Navmesh_CageElevator_0_0, NavmeshType.Wall)
    EnableNavmeshType(Navigation.Navmesh_CageElevator_0_1, NavmeshType.WallTouchingFloor)
    EnableNavmeshType(Navigation.Navmesh_CageElevator_1_0, NavmeshType.WallTouchingFloor)
    EnableNavmeshType(Navigation.Navmesh_CageElevator_1_1, NavmeshType.Wall)
    EnableNavmeshType(Navigation.Navmesh_CageElevator_2_0, NavmeshType.WallTouchingFloor)
    EnableNavmeshType(Navigation.Navmesh_CageElevator_2_1, NavmeshType.Wall)
    EnableNavmeshType(Navigation.Navmesh_CageElevator_3_0, NavmeshType.Wall)
    EnableNavmeshType(Navigation.Navmesh_CageElevator_3_1, NavmeshType.WallTouchingFloor)
    IfAllPlayersOutsideRegion(7, region=Spheres.CageElevatorStart_UpperRight)
    IfAllPlayersOutsideRegion(7, region=Spheres.CageElevatorStart_LowerLeft)
    IfConditionTrue(0, input_condition=7)
    Restart()


def Event11500102():
    """ 11500102: Event 11500102 """
    SkipLinesIfThisEventOff(4)
    SkipLinesIfFlagOn(1, 11500100)
    EndOfAnimation(Objects.o5301_0000, 20)
    End()
    IfThisEventOff(1)
    IfPlayerHasGood(1, 2003, including_box=False)
    IfActionButton(
        1,
        prompt_text=10010400,
        anchor_entity=Objects.o5301_0000,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        model_point=105,
    )
    IfConditionTrue(0, input_condition=1)
    Move(
        PLAYER,
        destination=Objects.o5301_0000,
        destination_type=CoordEntityType.Object,
        model_point=120,
        short_move=True,
    )
    ForceAnimation(PLAYER, 7111)
    ForceAnimation(Objects.o5301_0000, 10)
    EndIfClient()
    DisplayDialog(
        10010862,
        anchor_entity=-1,
        display_distance=3.0,
        button_type=ButtonType.Yes_or_No,
        number_buttons=NumberButtons.NoButton,
    )


def Event11500103():
    """ 11500103: Event 11500103 """
    DisableNetworkSync()
    IfFlagOff(1, 11500102)
    IfPlayerDoesNotHaveGood(1, 2003, including_box=False)
    IfActionButton(
        1,
        prompt_text=10010400,
        anchor_entity=Objects.o5301_0000,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        model_point=105,
        trigger_attribute=TriggerAttribute.All,
    )
    IfConditionTrue(0, input_condition=1)
    DisplayDialog(
        10010163,
        anchor_entity=-1,
        display_distance=3.0,
        button_type=ButtonType.Yes_or_No,
        number_buttons=NumberButtons.NoButton,
    )
    Restart()


def Event11500106():
    """ 11500106: Event 11500106 """
    DisableNetworkSync()
    IfFlagOff(1, 11500105)
    IfActionButton(
        1,
        prompt_text=10010400,
        anchor_entity=Objects.o5140_0000,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        model_point=101,
        trigger_attribute=TriggerAttribute.All,
    )
    IfConditionTrue(0, input_condition=1)
    DisplayDialog(
        10010161,
        anchor_entity=Objects.o5140_0000,
        display_distance=3.0,
        button_type=ButtonType.OK_or_Cancel,
        number_buttons=NumberButtons.NoButton,
    )
    Restart()


def Event11500107():
    """ 11500107: Event 11500107 """
    SkipLinesIfThisEventOff(2)
    EndOfAnimation(Objects.o5140_0000, 0)
    End()
    IfFlagOff(1, 11500105)
    IfActionButton(
        1,
        prompt_text=10010400,
        anchor_entity=Objects.o5140_0000,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        model_point=100,
        trigger_attribute=TriggerAttribute.All,
    )
    IfConditionTrue(0, input_condition=1)
    EnableFlag(11500105)
    Move(
        PLAYER,
        destination=Objects.o5140_0000,
        destination_type=CoordEntityType.Object,
        model_point=120,
        short_move=True,
    )
    ForceAnimation(PLAYER, 7112)
    ForceAnimation(Objects.o5140_0000, 0)


def Event11500110(_, arg_0_3: int, arg_4_7: int):
    """ 11500110: Event 11500110 """
    SkipLinesIfThisEventSlotOff(3)
    EndOfAnimation(arg_0_3, 0)
    DisableObjectActivation(arg_0_3, obj_act_id=-1)
    End()
    IfObjectActivated(0, obj_act_id=arg_4_7)
    EnableFlag(arg_4_7)
    EndIfClient()
    IfPlayerHasGood(1, 2003, including_box=False)
    SkipLinesIfConditionTrue(2, 1)
    DisplayDialog(
        10010883,
        anchor_entity=arg_0_3,
        display_distance=3.0,
        button_type=ButtonType.Yes_or_No,
        number_buttons=NumberButtons.NoButton,
    )
    SkipLines(1)
    DisplayDialog(
        10010862,
        anchor_entity=arg_0_3,
        display_distance=3.0,
        button_type=ButtonType.Yes_or_No,
        number_buttons=NumberButtons.NoButton,
    )


def Event11505270(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int, arg_20_23: int):
    """ 11505270: Event 11505270 """
    SkipLinesIfFlagOff(2, arg_20_23)
    EndOfAnimation(arg_4_7, 0)
    SkipLines(12)
    IfCharacterInsideRegion(-1, PLAYER, region=arg_0_3)
    IfObjectDamagedBy(-1, arg_4_7, attacker=-1)
    IfConditionTrue(0, input_condition=-1)
    EnableFlag(arg_20_23)
    CreateTemporaryVFX(150005, anchor_entity=arg_4_7, anchor_type=CoordEntityType.Object, model_point=101)
    DeleteVFX(arg_8_11, erase_root_only=False)
    ForceAnimation(arg_4_7, 0, wait_for_completion=True)
    SkipLinesIfEqual(5, left=arg_20_23, right=11505284)
    ShootProjectile(
        owner_entity=Characters.c2690_0000,
        projectile_id=arg_12_15,
        model_point=101,
        behavior_id=5070,
        launch_angle_x=0,
        launch_angle_y=arg_16_19,
        launch_angle_z=0,
    )
    Wait(0.699999988079071)
    ShootProjectile(
        owner_entity=Characters.c2690_0000,
        projectile_id=arg_12_15,
        model_point=101,
        behavior_id=5070,
        launch_angle_x=0,
        launch_angle_y=arg_16_19,
        launch_angle_z=0,
    )
    Wait(0.699999988079071)
    ShootProjectile(
        owner_entity=Characters.c2690_0000,
        projectile_id=arg_12_15,
        model_point=101,
        behavior_id=5070,
        launch_angle_x=0,
        launch_angle_y=arg_16_19,
        launch_angle_z=0,
    )
    IfTrueFlagCountGreaterThanOrEqual(0, 2, (11505280, 11505285))
    DisableFlag(arg_20_23)
    ForceAnimation(arg_4_7, 1, wait_for_completion=True)
    Restart()


def Event11505260():
    """ 11505260: Event 11505260 """
    IfFlagOn(0, 11505284)
    Wait(0.699999988079071)
    ShootProjectile(
        owner_entity=Characters.c2690_0000,
        projectile_id=1501214,
        model_point=101,
        behavior_id=5070,
        launch_angle_x=0,
        launch_angle_y=180,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=Characters.c2690_0000,
        projectile_id=1501215,
        model_point=101,
        behavior_id=5070,
        launch_angle_x=0,
        launch_angle_y=180,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=Characters.c2690_0000,
        projectile_id=1501216,
        model_point=101,
        behavior_id=5070,
        launch_angle_x=0,
        launch_angle_y=180,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=Characters.c2690_0000,
        projectile_id=1501217,
        model_point=101,
        behavior_id=5070,
        launch_angle_x=0,
        launch_angle_y=180,
        launch_angle_z=0,
    )
    Wait(0.699999988079071)
    ShootProjectile(
        owner_entity=Characters.c2690_0000,
        projectile_id=1501214,
        model_point=101,
        behavior_id=5070,
        launch_angle_x=0,
        launch_angle_y=180,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=Characters.c2690_0000,
        projectile_id=1501215,
        model_point=101,
        behavior_id=5070,
        launch_angle_x=0,
        launch_angle_y=180,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=Characters.c2690_0000,
        projectile_id=1501216,
        model_point=101,
        behavior_id=5070,
        launch_angle_x=0,
        launch_angle_y=180,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=Characters.c2690_0000,
        projectile_id=1501217,
        model_point=101,
        behavior_id=5070,
        launch_angle_x=0,
        launch_angle_y=180,
        launch_angle_z=0,
    )
    Wait(0.699999988079071)
    ShootProjectile(
        owner_entity=Characters.c2690_0000,
        projectile_id=1501214,
        model_point=101,
        behavior_id=5070,
        launch_angle_x=0,
        launch_angle_y=180,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=Characters.c2690_0000,
        projectile_id=1501215,
        model_point=101,
        behavior_id=5070,
        launch_angle_x=0,
        launch_angle_y=180,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=Characters.c2690_0000,
        projectile_id=1501216,
        model_point=101,
        behavior_id=5070,
        launch_angle_x=0,
        launch_angle_y=180,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=Characters.c2690_0000,
        projectile_id=1501217,
        model_point=101,
        behavior_id=5070,
        launch_angle_x=0,
        launch_angle_y=180,
        launch_angle_z=0,
    )
    IfFlagOff(0, 11505284)
    Restart()


@RestartOnRest
def Event11505050():
    """ 11505050: Event 11505050 """
    EndIfThisEventOn()
    DisableAI(Characters.c2860_0000)
    IfCharacterInsideRegion(-1, PLAYER, region=Boxes.BoulderGiantAlertTrigger)
    IfAttacked(-1, Characters.c2860_0000, attacker=PLAYER)
    IfConditionTrue(0, input_condition=-1)
    EnableFlag(11505050)
    IfFlagOff(0, 11505052)
    EnableAI(Characters.c2860_0000)


@RestartOnRest
def Event11505051():
    """ 11505051: Event 11505051 """
    IfFlagOn(1, 11505050)
    IfFlagOn(2, 11505052)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(1)
    Move(
        Characters.c2860_0000,
        destination=Boxes.BoulderGiantAnimationSnap,
        destination_type=CoordEntityType.Region,
        short_move=True,
    )
    ForceAnimation(Characters.c2860_0000, 9001, wait_for_completion=True)
    DisableFlag(11505052)
    Restart()


@RestartOnRest
def Event11505055():
    """ 11505055: Event 11505055 """
    SkipLinesIfClient(1)
    SetNetworkUpdateAuthority(Characters.c2860_0001, UpdateAuthority.Forced)
    IfObjectDestroyed(1, Objects.o5560_0001)
    IfObjectDestroyed(1, Objects.o5560_0002)
    IfObjectDestroyed(1, Objects.o5560_0003)
    IfObjectDestroyed(1, Objects.o5560_0004)
    IfObjectDestroyed(1, Objects.o5560_0006)
    IfObjectDestroyed(1, Objects.o5560_0007)
    IfObjectDestroyed(1, Objects.o5560_0009)
    IfObjectDestroyed(1, Objects.o5561_0000)
    IfObjectDestroyed(1, Objects.o5561_0001)
    IfConditionTrue(0, input_condition=1)
    AICommand(Characters.c2860_0001, command_id=20, slot=1)
    ReplanAI(Characters.c2860_0001)


def Event11505110():
    """ 11505110: Event 11505110 """
    IfFlagOn(1, 11505100)
    IfFlagOn(2, 11505100)
    IfFlagOn(3, 11505100)
    IfFlagOn(4, 11505100)
    IfFlagOn(5, 11505100)
    IfFlagOn(6, 11505100)
    IfFlagOn(7, 11505100)
    IfFlagOn(1, 11505111)
    IfFlagOn(2, 11505112)
    IfFlagOn(3, 11505113)
    IfFlagOn(4, 11505114)
    IfFlagOn(5, 11505115)
    IfFlagOn(6, 11505116)
    IfFlagRangeAllOff(7, (11505111, 11505116))
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(-1, input_condition=4)
    IfConditionTrue(-1, input_condition=5)
    IfConditionTrue(-1, input_condition=6)
    IfConditionTrue(-1, input_condition=7)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionFalse(8, 6)
    ShootProjectile(
        owner_entity=Characters.c2690_0000,
        projectile_id=1500100,
        model_point=50,
        behavior_id=5305,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    DisableFlagRange((11505111, 11505116))
    AICommand(Characters.c2860_0001, command_id=-1, slot=2)
    DisableFlag(11505105)
    RestartEvent(11505102)
    Wait(1.0)
    DisableFlag(11505100)
    Restart()
    SkipLinesIfFinishedConditionFalse(8, 5)
    ShootProjectile(
        owner_entity=Characters.c2690_0000,
        projectile_id=1500100,
        model_point=50,
        behavior_id=5304,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    DisableFlagRange((11505111, 11505116))
    AICommand(Characters.c2860_0001, command_id=-1, slot=2)
    DisableFlag(11505105)
    RestartEvent(11505102)
    Wait(1.0)
    DisableFlag(11505100)
    Restart()
    SkipLinesIfFinishedConditionFalse(8, 4)
    ShootProjectile(
        owner_entity=Characters.c2690_0000,
        projectile_id=1500100,
        model_point=50,
        behavior_id=5303,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    DisableFlagRange((11505111, 11505116))
    AICommand(Characters.c2860_0001, command_id=-1, slot=2)
    DisableFlag(11505105)
    RestartEvent(11505102)
    Wait(1.0)
    DisableFlag(11505100)
    Restart()
    SkipLinesIfFinishedConditionFalse(8, 3)
    ShootProjectile(
        owner_entity=Characters.c2690_0000,
        projectile_id=1500100,
        model_point=50,
        behavior_id=5302,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    DisableFlagRange((11505111, 11505116))
    AICommand(Characters.c2860_0001, command_id=-1, slot=2)
    DisableFlag(11505105)
    RestartEvent(11505102)
    Wait(1.0)
    DisableFlag(11505100)
    Restart()
    SkipLinesIfFinishedConditionFalse(8, 2)
    ShootProjectile(
        owner_entity=Characters.c2690_0000,
        projectile_id=1500100,
        model_point=50,
        behavior_id=5301,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    DisableFlagRange((11505111, 11505116))
    AICommand(Characters.c2860_0001, command_id=-1, slot=2)
    DisableFlag(11505105)
    RestartEvent(11505102)
    Wait(1.0)
    DisableFlag(11505100)
    Restart()
    SkipLinesIfFinishedConditionFalse(8, 1)
    ShootProjectile(
        owner_entity=Characters.c2690_0000,
        projectile_id=1500100,
        model_point=50,
        behavior_id=5300,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    DisableFlagRange((11505111, 11505116))
    AICommand(Characters.c2860_0001, command_id=-1, slot=2)
    DisableFlag(11505105)
    RestartEvent(11505102)
    Wait(1.0)
    DisableFlag(11505100)
    Restart()
    ShootProjectile(
        owner_entity=Characters.c2690_0000,
        projectile_id=1500100,
        model_point=50,
        behavior_id=5304,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    DisableFlagRange((11505111, 11505116))
    AICommand(Characters.c2860_0001, command_id=-1, slot=2)
    DisableFlag(11505105)
    RestartEvent(11505102)
    Wait(1.0)
    DisableFlag(11505100)
    Restart()


def Event11505111(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 11505111: Event 11505111 """
    IfFlagOff(1, 11505100)
    IfFlagOff(1, 11505105)
    IfTimeElapsed(1, 2.0)
    IfFlagOff(1, arg_0_3)
    IfCharacterInsideRegion(1, PLAYER, region=arg_4_7)
    SkipLinesIfGreaterThanOrEqual(1, left=arg_0_3, right=11505112)
    IfAllPlayersOutsideRegion(1, region=Boxes.BombTargetB)
    SkipLinesIfGreaterThanOrEqual(1, left=arg_0_3, right=11505113)
    IfAllPlayersOutsideRegion(1, region=Boxes.BombTargetC)
    SkipLinesIfGreaterThanOrEqual(1, left=arg_0_3, right=11505114)
    IfAllPlayersOutsideRegion(1, region=Boxes.BombTargetD)
    SkipLinesIfGreaterThanOrEqual(1, left=arg_0_3, right=11505115)
    IfAllPlayersOutsideRegion(1, region=Boxes.BombTargetE)
    SkipLinesIfGreaterThanOrEqual(1, left=arg_0_3, right=11505116)
    IfAllPlayersOutsideRegion(1, region=Boxes.BombTargetF)
    SkipLinesIfGreaterThanOrEqual(1, left=arg_0_3, right=11505117)
    IfAllPlayersOutsideRegion(1, region=Boxes.BombGiantCombatArea)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((11505111, 11505116))
    EnableFlag(arg_0_3)
    AICommand(Characters.c2860_0001, command_id=arg_8_11, slot=2)
    Restart()


def Event11505101():
    """ 11505101: Event 11505101 """
    IfFlagOn(0, 11505105)
    EnableFlag(11505105)
    IfFlagOff(0, 11505105)
    DisableFlag(11505105)
    DisableFlag(11505100)
    Restart()


def Event11505102():
    """ 11505102: Event 11505102 """
    DisableNetworkSync()
    IfFlagOn(0, 11505105)
    Wait(30.0)
    DisableFlag(11505105)
    DisableFlag(11505100)
    Restart()


@RestartOnRest
def Event11505060(_, arg_0_3: int):
    """ 11505060: Event 11505060 """
    IfHasTAEEvent(0, arg_0_3, tae_event_id=500)
    EzstateAIRequest(arg_0_3, command_id=1500, slot=0)
    IfDoesNotHaveTAEEvent(0, arg_0_3, tae_event_id=500)
    Restart()


@RestartOnRest
def Event11505070(_, arg_0_3: int):
    """ 11505070: Event 11505070 """
    DisableNetworkSync()
    IfHasTAEEvent(0, arg_0_3, tae_event_id=1400)
    Wait(10.0)
    EzstateAIRequest(arg_0_3, command_id=1501, slot=0)
    Restart()


@RestartOnRest
def Event11505080():
    """ 11505080: Event 11505080 """
    SkipLinesIfThisEventOff(2)
    ResetStandbyAnimationSettings(Characters.c2690_0005)
    End()
    IfAttacked(-1, Characters.c2690_0005, attacker=PLAYER)
    IfHealthNotEqual(-1, Characters.c2690_0005, 1.0)
    IfConditionTrue(0, input_condition=-1)
    ResetStandbyAnimationSettings(Characters.c2690_0005)
    ForceAnimation(Characters.c2690_0005, 2000)


@RestartOnRest
def Event11505010():
    """ 11505010: Event 11505010 """
    IfCharacterAlive(1, Characters.c2780_0000)
    IfCharacterBackreadEnabled(1, Characters.c2780_0000)
    IfCharacterHasSpecialEffect(1, Characters.c2780_0000, 5421)
    IfCharacterType(2, PLAYER, CharacterType.BlackPhantom)
    IfConditionFalse(1, input_condition=2)
    IfActionButton(
        1,
        prompt_text=10010400,
        anchor_entity=Characters.c2780_0000,
        anchor_type=CoordEntityType.Character,
        facing_angle=45.0,
        max_distance=1.2000000476837158,
        model_point=7,
        trigger_attribute=TriggerAttribute.All,
    )
    IfConditionTrue(0, input_condition=1)
    Move(
        PLAYER,
        destination=Characters.c2780_0000,
        destination_type=CoordEntityType.Character,
        model_point=100,
        copy_draw_parent=Characters.c2780_0000,
    )
    ForceAnimation(PLAYER, 7521)
    AICommand(Characters.c2780_0000, command_id=10, slot=0)
    ReplanAI(Characters.c2780_0000)
    Wait(0.10000000149011612)
    AICommand(Characters.c2780_0000, command_id=-1, slot=0)
    Restart()


@RestartOnRest
def Event11505011():
    """ 11505011: Event 11505011 """
    IfCharacterDoesNotHaveSpecialEffect(1, Characters.c2780_0000, 5420)
    IfAttacked(1, Characters.c2780_0000, attacker=PLAYER)
    IfConditionTrue(0, input_condition=1)
    CancelSpecialEffect(Characters.c2780_0000, 3150)
    CancelSpecialEffect(Characters.c2780_0000, 3151)
    IfCharacterBackreadDisabled(7, Characters.c2780_0000)
    RestartIfConditionTrue(7)
    IfCharacterHasSpecialEffect(2, Characters.c2780_0000, 5421)
    SkipLinesIfConditionFalse(1, 2)
    ForceAnimation(Characters.c2780_0000, 3001, wait_for_completion=True)
    IfCharacterHasSpecialEffect(3, Characters.c2780_0000, 5422)
    SkipLinesIfConditionFalse(1, 3)
    ForceAnimation(Characters.c2780_0000, 3001, wait_for_completion=True)
    IfCharacterHasSpecialEffect(4, Characters.c2780_0000, 5423)
    SkipLinesIfConditionFalse(1, 4)
    ForceAnimation(Characters.c2780_0000, 3001, wait_for_completion=True)
    IfCharacterHasSpecialEffect(5, Characters.c2780_0000, 5424)
    SkipLinesIfConditionFalse(1, 5)
    ForceAnimation(Characters.c2780_0000, 3006, wait_for_completion=True)
    ReplanAI(Characters.c2780_0000)
    CancelSpecialEffect(Characters.c2780_0000, 3150)
    CancelSpecialEffect(Characters.c2780_0000, 3151)
    Restart()


@RestartOnRest
def Event11505012():
    """ 11505012: Event 11505012 """
    IfCharacterHasSpecialEffect(1, Characters.c2780_0000, 5421)
    IfCharacterHasSpecialEffect(1, Characters.c2780_0000, 3150)
    IfCharacterHasSpecialEffect(2, Characters.c2780_0000, 5420)
    IfCharacterHasSpecialEffect(2, Characters.c2780_0000, 3150)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionTrue(5, 2)
    AICommand(Characters.c2780_0000, command_id=200, slot=0)
    ReplanAI(Characters.c2780_0000)
    Wait(0.10000000149011612)
    AICommand(Characters.c2780_0000, command_id=-1, slot=0)
    SkipLines(4)
    AICommand(Characters.c2780_0000, command_id=210, slot=0)
    ReplanAI(Characters.c2780_0000)
    Wait(0.10000000149011612)
    AICommand(Characters.c2780_0000, command_id=-1, slot=0)
    IfCharacterHasSpecialEffect(-2, Characters.c2780_0000, 5420)
    IfCharacterHasSpecialEffect(-2, Characters.c2780_0000, 5421)
    IfConditionTrue(0, input_condition=-2)
    Restart()


@RestartOnRest
def Event11505013():
    """ 11505013: Event 11505013 """
    IfCharacterHasSpecialEffect(1, Characters.c2780_0000, 5422)
    IfCharacterDoesNotHaveSpecialEffect(1, Characters.c2780_0000, 3150)
    IfCharacterHasSpecialEffect(2, Characters.c2780_0000, 5423)
    IfCharacterDoesNotHaveSpecialEffect(2, Characters.c2780_0000, 3150)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    CancelSpecialEffect(Characters.c2780_0000, 3150)
    CancelSpecialEffect(Characters.c2780_0000, 3151)
    SkipLinesIfFinishedConditionTrue(5, 2)
    AICommand(Characters.c2780_0000, command_id=201, slot=0)
    ReplanAI(Characters.c2780_0000)
    Wait(0.10000000149011612)
    AICommand(Characters.c2780_0000, command_id=-1, slot=0)
    SkipLines(4)
    AICommand(Characters.c2780_0000, command_id=211, slot=0)
    ReplanAI(Characters.c2780_0000)
    Wait(0.10000000149011612)
    AICommand(Characters.c2780_0000, command_id=-1, slot=0)
    IfCharacterHasSpecialEffect(-2, Characters.c2780_0000, 5420)
    IfCharacterHasSpecialEffect(-2, Characters.c2780_0000, 5421)
    IfConditionTrue(0, input_condition=-2)
    Restart()


@RestartOnRest
def Event11505014():
    """ 11505014: Event 11505014 """
    IfSingleplayer(1)
    IfCharacterInsideRegion(1, Characters.c2780_0000, region=Boxes.MimicNest)
    IfCharacterBackreadDisabled(1, Characters.c2780_0000)
    IfConditionTrue(0, input_condition=1)
    AddSpecialEffect(Characters.c2780_0000, 5421)
    ClearTargetList(Characters.c2780_0000)
    ReplanAI(Characters.c2780_0000)
    Move(Characters.c2780_0000, destination=Boxes.MimicNest, destination_type=CoordEntityType.Region, short_move=True)
    IfCharacterBackreadEnabled(0, Characters.c2780_0000)
    Restart()


@RestartOnRest
def Event11505015():
    """ 11505015: Event 11505015 """
    EndIfHost()
    IfCharacterBackreadDisabled(1, Characters.c2780_0000)
    EndIfConditionTrue(1)
    ResetAnimation(Characters.c2780_0000, disable_interpolation=True)
    ForceAnimation(Characters.c2780_0000, 0)
    ReplanAI(Characters.c2780_0000)


@RestartOnRest
def Event11500900():
    """ 11500900: Event 11500900 """
    SkipLinesIfThisEventSlotOff(2)
    DisableCharacter(Characters.c2780_0000)
    End()
    IfCharacterDead(0, Characters.c2780_0000)
    End()


def Event11500210():
    """ 11500210: Event 11500210 """
    EndIfClient()
    IfInsideMap(0, game_map=SENS_FORTRESS)
    IfTimeElapsed(0, 5.0)
    IfFlagOn(0, 11)
    IfActionButton(
        0,
        prompt_text=10010120,
        anchor_entity=Spheres.AnorLondoWarpPrompt,
        anchor_type=CoordEntityType.Region,
    )
    DisableBackread(Characters.c2570_0000)
    WaitFrames(1)
    SkipLinesIfFlagOn(2, 11510400)
    PlayCutscene(
        150000,
        skippable=True,
        fade_out=False,
        player_id=PLAYER,
        move_to_region=Boxes.AnorLondoArrivalPoint,
        move_to_map=ANOR_LONDO,
    )
    SkipLines(2)
    SetMapDrawParamSlot(15, slot=2)
    PlayCutscene(
        150002,
        skippable=True,
        fade_out=False,
        player_id=PLAYER,
        move_to_region=Boxes.AnorLondoArrivalPoint,
        move_to_map=ANOR_LONDO,
    )
    WaitFrames(1)
    AwardAchievement(33)
    Restart()


@RestartOnRest
def Event11500860(_, arg_0_3: int):
    """ 11500860: Event 11500860 """
    SkipLinesIfThisEventSlotOff(3)
    DisableCharacter(arg_0_3)
    Kill(arg_0_3, award_souls=False)
    End()
    IfCharacterDead(0, arg_0_3)
    End()


def Event11500600(_, arg_0_3: int, arg_4_7: int):
    """ 11500600: Event 11500600 """
    SkipLinesIfThisEventSlotOff(4)
    EndOfAnimation(arg_0_3, 0)
    DisableObjectActivation(arg_0_3, obj_act_id=-1)
    EnableTreasure(arg_0_3)
    End()
    DisableTreasure(arg_0_3)
    IfObjectActivated(0, obj_act_id=arg_4_7)
    WaitFrames(10)
    EnableTreasure(arg_0_3)


def Event11500510(_, arg_0_3: int, arg_4_7: int):
    """ 11500510: Event 11500510 """
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


def Event11500520(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11500520: Event 11500520 """
    SkipLinesIfThisEventSlotOff(2)
    DropMandatoryTreasure(arg_0_3)
    End()
    IfHealthLessThanOrEqual(0, arg_0_3, 0.0)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)


def Event11500530():
    """ 11500530: Event 11500530 """
    SkipLinesIfFlagOn(3, 11500593)
    DisableObjectActivation(Objects.o5310_0004, obj_act_id=-1)
    IfFlagOn(0, 11500593)
    EnableObjectActivation(Objects.o5310_0004, obj_act_id=-1)
    EndIfThisEventOn()
    IfFlagOn(0, 11500112)
    DisableFlag(71500021)


def Event11500531(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11500531: Event 11500531 """
    IfFlagOff(1, 1096)
    IfFlagOn(1, 1090)
    IfFlagOn(1, 11500112)
    IfCharacterAlive(1, arg_0_3)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)


def Event11500532(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11500532: Event 11500532 """
    IfFlagOff(1, 1096)
    IfFlagOn(1, 1092)
    IfFlagOn(1, 11500594)
    IfConditionTrue(0, input_condition=1)
    SkipLinesIfFinishedConditionTrue(2, 1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)
    DisableCharacter(arg_0_3)


def Event11500533(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11500533: Event 11500533 """
    IfFlagOff(1, 1114)
    IfFlagOn(1, 1113)
    IfFlagOn(1, 723)
    IfInsideMap(1, game_map=SENS_FORTRESS)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)
    EnableCharacter(arg_0_3)


def Event11500534(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11500534: Event 11500534 """
    IfFlagOff(1, 1512)
    IfFlagOn(1, 1490)
    IfFlagOn(1, 11500591)
    IfFlagOn(1, 11500200)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)
    Move(
        arg_0_3,
        destination=Boxes.SiegmeyerMovement,
        destination_type=CoordEntityType.Region,
        set_draw_parent=Collisions.h0060B0_0000,
    )
    SetNest(arg_0_3, Boxes.SiegmeyerMovement)
    Kill(Characters.c2690_0006, award_souls=False)
    Kill(Characters.c2690_0007, award_souls=False)


def Event11500535(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11500535: Event 11500535 """
    IfFlagOff(1, 1512)
    IfFlagOn(1, 1490)
    IfFlagOff(1, 11500591)
    IfFlagOn(1, 11500200)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)
    Move(
        arg_0_3,
        destination=Boxes.SiegmeyerMovement,
        destination_type=CoordEntityType.Region,
        set_draw_parent=Collisions.h0060B0_0000,
    )
    SetNest(arg_0_3, Boxes.SiegmeyerMovement)
    Kill(Characters.c2690_0006, award_souls=False)
    Kill(Characters.c2690_0007, award_souls=False)


def Event11500536(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11500536: Event 11500536 """
    IfHost(1)
    IfFlagOff(1, 1512)
    IfFlagOn(1, 1491)
    IfFlagOn(1, 11500850)
    IfCharacterBackreadDisabled(1, arg_0_3)
    IfHost(2)
    IfFlagOff(2, 1512)
    IfFlagOn(2, 1492)
    IfFlagOn(2, 11500592)
    IfFlagOn(2, 11500850)
    IfCharacterBackreadDisabled(2, arg_0_3)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)
    DisableCharacter(arg_0_3)


def Event11505030():
    """ 11505030: Event 11505030 """
    SkipLinesIfClient(1)
    SetNetworkUpdateAuthority(Characters.c0000_0007, UpdateAuthority.Forced)
    SkipLinesIfFlagOn(3, 11505033)
    IfClient(2)
    IfFlagOn(2, 11505031)
    SkipLinesIfConditionTrue(1, 2)
    DisableCharacter(Characters.c0000_0007)
    EndIfFlagOn(11)
    IfHost(1)
    IfCharacterHuman(1, PLAYER)
    IfCharacterBackreadEnabled(1, Characters.c0000_0007)
    IfEntityWithinDistance(1, Characters.c0000_0007, PLAYER, radius=10.0)
    IfConditionTrue(0, input_condition=1)
    PlaceSummonSign(
        SummonSignType.BlueEyeSign,
        Characters.c0000_0007,
        region=Points.TarkusSummonSign,
        summon_flag=11505031,
        dismissal_flag=11505033,
    )


def Event11505990(_, arg_0_3: int, arg_4_7: int):
    """ 11505990: Event 11505990 """
    IfFlagOn(0, arg_0_3)
    EraseNPCSummonSign(summoned_character=arg_4_7)
    IfFlagOff(0, arg_0_3)
    Restart()


def Event11505029():
    """ 11505029: Event 11505029 """
    SkipLinesIfClient(1)
    SetNetworkUpdateAuthority(Characters.c0000_0007, UpdateAuthority.Forced)
    SkipLinesIfFlagOn(3, 11505033)
    IfClient(2)
    IfFlagOn(2, 11505031)
    SkipLinesIfConditionTrue(1, 2)
    DisableCharacter(Characters.c0000_0007)
    EndIfFlagOn(11)
    IfMultiplayerCount(1, arg1=4, arg2=3)
    IfHost(1)
    IfFlagOff(1, 11505031)
    IfFlagOff(1, 11505033)
    IfCharacterHuman(1, PLAYER)
    IfCharacterBackreadEnabled(1, Characters.c0000_0007)
    IfEntityWithinDistance(1, Characters.c0000_0007, PLAYER, radius=10.0)
    IfCharacterHasSpecialEffect(1, PLAYER, 28)
    IfConditionTrue(0, input_condition=1)
    PlaceSummonSign(
        SummonSignType.BlueEyeSign,
        Characters.c0000_0007,
        region=Points.TarkusSummonSign,
        summon_flag=11505031,
        dismissal_flag=11505033,
    )


def Event11505032():
    """ 11505032: Event 11505032 """
    EndIfThisEventOn()
    IfFlagOn(1, 11505031)
    IfFlagOn(1, 11505393)
    IfConditionTrue(0, input_condition=1)
    AICommand(Characters.c0000_0007, command_id=10, slot=0)
    ReplanAI(Characters.c0000_0007)
    IfCharacterInsideRegion(0, Characters.c0000_0007, region=Boxes.IronGolemFogPrompt)
    RotateToFaceEntity(Characters.c0000_0007, Boxes.IronGolemFogRotationTarget)
    ForceAnimation(Characters.c0000_0007, 7410)
    AICommand(Characters.c0000_0007, command_id=-1, slot=0)
    ReplanAI(Characters.c0000_0007)


def Event11505843(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11505843: Event 11505843 """
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


def Event11505846(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 11505846: Event 11505846 """
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
    """ 11502000: Patches teleports behind the player and attacks. """
    DisableCharacter(Characters.c0000_PatchesAmbush)

    Await(InsideMap(SENS_FORTRESS) and TriggerFlags.PatchesAmbush and IsAlive(Characters.c0000_PatchesAmbush))
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
    """ 11502001: Channeler teleports above the player (no gravity) and uses its buff dance. """
    DisableCharacter(Characters.c2370_TrollChanneler)

    Await(InsideMap(SENS_FORTRESS) and TriggerFlags.ChannelerAmbush and IsAlive(Characters.c2370_TrollChanneler))
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

    AddSpecialEffect(6030, 5470)
    AddSpecialEffect(6250, 5470)
    AddSpecialEffect(6280, 5470)
    AddSpecialEffect(6510, 5470)
    AddSpecialEffect(6043, 5470)
    AddSpecialEffect(6600, 5470)
    AddSpecialEffect(1500961, 5470)
    AddSpecialEffect(1500300, 5470)
    AddSpecialEffect(1500301, 5470)
    AddSpecialEffect(1500302, 5470)
    AddSpecialEffect(1500303, 5470)
    AddSpecialEffect(1500800, 5470)
    AddSpecialEffect(1500202, 5470)
    AddSpecialEffect(1500203, 5470)
    AddSpecialEffect(1500204, 5470)
    AddSpecialEffect(1500205, 5470)
    AddSpecialEffect(1500201, 5470)
    AddSpecialEffect(1500200, 5470)
    AddSpecialEffect(1500206, 5470)
    AddSpecialEffect(1500207, 5470)
    AddSpecialEffect(1500208, 5470)
    AddSpecialEffect(1500110, 5470)
    AddSpecialEffect(1500122, 5470)
    AddSpecialEffect(1500120, 5470)
    AddSpecialEffect(1500121, 5470)
    AddSpecialEffect(1500209, 5470)
    AddSpecialEffect(1500210, 5470)
    AddSpecialEffect(1500211, 5470)
    AddSpecialEffect(1500212, 5470)
    AddSpecialEffect(1500900, 5470)
    AddSpecialEffect(1500901, 5470)
    AddSpecialEffect(1500902, 5470)
    AddSpecialEffect(1500903, 5470)
    AddSpecialEffect(1500904, 5470)
    AddSpecialEffect(1500905, 5470)
    AddSpecialEffect(1500906, 5470)
    AddSpecialEffect(1500213, 5470)
    AddSpecialEffect(1500214, 5470)
    AddSpecialEffect(1500215, 5470)
    AddSpecialEffect(1500216, 5470)
    AddSpecialEffect(1500217, 5470)
    AddSpecialEffect(1500218, 5470)
    AddSpecialEffect(1500219, 5470)
    AddSpecialEffect(1500220, 5470)
    AddSpecialEffect(1500907, 5470)
    AddSpecialEffect(1500908, 5470)
    AddSpecialEffect(1500909, 5470)
    AddSpecialEffect(1500221, 5470)
    AddSpecialEffect(1500010, 5470)
    AddSpecialEffect(1500101, 5470)
    AddSpecialEffect(1500100, 5470)
    AddSpecialEffect(1500102, 5470)
    AddSpecialEffect(1503900, 5470)
    AddSpecialEffect(1503910, 5470)
    AddSpecialEffect(1503920, 5470)
    AddSpecialEffect(1503901, 5470)
    AddSpecialEffect(1503911, 5470)
    AddSpecialEffect(1503921, 5470)
    AddSpecialEffect(1503902, 5470)
    AddSpecialEffect(1503912, 5470)
    AddSpecialEffect(1503922, 5470)

    return RESTART


@RestartOnRest
def RedPhantomAmbush():
    """ 11502002: Random red phantom ambushes the player. """
    DisableCharacter(Characters.c2690_0012)
    DisableCharacter(Characters.c2690_0013)
    DisableCharacter(Characters.c2690_0014)
    DisableCharacter(Characters.c2690_0015)
    DisableCharacter(Characters.c2690_0016)
    DisableCharacter(Characters.c2690_0017)
    DisableCharacter(Characters.c2690_0018)
    DisableCharacter(Characters.c2700_0008)
    DisableCharacter(Characters.c2700_0009)
    DisableCharacter(Characters.c2700_0010)

    Await(InsideMap(SENS_FORTRESS) and TriggerFlags.EnemyAmbush)
    DisableFlag(TriggerFlags.EnemyAmbush)

    DisableFlagRange((11812900, 11812999))
    EnableRandomFlagInRange((11812900, 11812909))

    if FlagEnabled(11812900):
        ControlRedPhantom(0, Characters.c2690_0012)
    elif FlagEnabled(11812901):
        ControlRedPhantom(0, Characters.c2690_0013)
    elif FlagEnabled(11812902):
        ControlRedPhantom(0, Characters.c2690_0014)
    elif FlagEnabled(11812903):
        ControlRedPhantom(0, Characters.c2690_0015)
    elif FlagEnabled(11812904):
        ControlRedPhantom(0, Characters.c2690_0016)
    elif FlagEnabled(11812905):
        ControlRedPhantom(0, Characters.c2690_0017)
    elif FlagEnabled(11812906):
        ControlRedPhantom(0, Characters.c2690_0018)
    elif FlagEnabled(11812907):
        ControlRedPhantom(0, Characters.c2700_0008)
    elif FlagEnabled(11812908):
        ControlRedPhantom(0, Characters.c2700_0009)
    elif FlagEnabled(11812909):
        ControlRedPhantom(0, Characters.c2700_0010)
    
    Await(FlagEnabled(11505082))

    return RESTART


@RestartOnRest
def ControlRedPhantom(_, enemy: int):
    """ 11505081: `enemy` moves to player and appears. """
    DisableFlag(11505082)
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
    EnableFlag(11505082)


def MakeWorldInvisible():
    """ 11502003: Disable all map pieces. Undone only by reload. """
    Await(TriggerFlags.InvisibleWorld)   # note you don't need to be standing in the map
    DisableFlag(TriggerFlags.InvisibleWorld)
    for map_piece in range(1508500, 1508551):
        DisableMapPiece(map_piece)
    # No need to restart.


@RestartOnRest
def OopsAllGwyns():
    """ 11502004: Enable Gwyns and warp them to their paired normal characters. """
    DisableCharacter(1500600)
    DisableCharacter(1500601)
    DisableCharacter(1500602)
    DisableCharacter(1500603)
    DisableCharacter(1500604)
    DisableCharacter(1500605)
    DisableCharacter(1500606)
    Await(TriggerFlags.OopsAllGwyns)  # note you don't need to be standing in the map
    DisableCharacter(6030)
    EnableCharacter(1500600)
    DisableCharacter(6600)
    EnableCharacter(1500601)
    DisableCharacter(1500303)
    EnableCharacter(1500602)
    DisableCharacter(1500205)
    EnableCharacter(1500603)
    DisableCharacter(1500208)
    EnableCharacter(1500604)
    DisableCharacter(1500209)
    EnableCharacter(1500605)
    DisableCharacter(1500217)
    EnableCharacter(1500606)
    WaitFrames(30)  # enough time for other maps to trigger too
    DisableFlag(TriggerFlags.OopsAllGwyns)
    # No need to restart.


@RestartOnRest
def OopsAllBonewheels():
    """ 11502005: Enable Bonewheels and warp them to their paired normal characters. """
    DisableCharacter(1500400)
    DisableCharacter(1500401)
    DisableCharacter(1500402)
    DisableCharacter(1500403)
    DisableCharacter(1500404)
    DisableCharacter(1500405)
    DisableCharacter(1500406)
    DisableCharacter(1500407)
    DisableCharacter(1500408)
    DisableCharacter(1500409)
    DisableCharacter(1500410)
    DisableCharacter(1500411)
    DisableCharacter(1500412)
    DisableCharacter(1500413)
    DisableCharacter(1500414)
    DisableCharacter(1500415)
    DisableCharacter(1500416)
    DisableCharacter(1500417)
    DisableCharacter(1500418)
    DisableCharacter(1500419)
    DisableCharacter(1500420)
    DisableCharacter(1500421)
    DisableCharacter(1500422)
    DisableCharacter(1500423)
    DisableCharacter(1500424)
    DisableCharacter(1500425)
    DisableCharacter(1500426)
    DisableCharacter(1500427)
    DisableCharacter(1500428)
    DisableCharacter(1500429)
    DisableCharacter(1500430)
    DisableCharacter(1500431)
    DisableCharacter(1500432)
    DisableCharacter(1500433)
    DisableCharacter(1500434)
    DisableCharacter(1500435)
    DisableCharacter(1500436)
    DisableCharacter(1500437)
    Await(TriggerFlags.OopsAllBonewheels)  # note you don't need to be standing in the map
    DisableCharacter(6030)
    EnableCharacter(1500400)
    DisableCharacter(6250)
    EnableCharacter(1500401)
    DisableCharacter(6280)
    EnableCharacter(1500402)
    DisableCharacter(6510)
    EnableCharacter(1500403)
    DisableCharacter(6043)
    EnableCharacter(1500404)
    DisableCharacter(6600)
    EnableCharacter(1500405)
    DisableCharacter(1500300)
    EnableCharacter(1500406)
    DisableCharacter(1500301)
    EnableCharacter(1500407)
    DisableCharacter(1500302)
    EnableCharacter(1500408)
    DisableCharacter(1500303)
    EnableCharacter(1500409)
    DisableCharacter(1500202)
    EnableCharacter(1500410)
    DisableCharacter(1500203)
    EnableCharacter(1500411)
    DisableCharacter(1500204)
    EnableCharacter(1500412)
    DisableCharacter(1500205)
    EnableCharacter(1500413)
    DisableCharacter(1500201)
    EnableCharacter(1500414)
    DisableCharacter(1500200)
    EnableCharacter(1500415)
    DisableCharacter(1500206)
    EnableCharacter(1500416)
    DisableCharacter(1500207)
    EnableCharacter(1500417)
    DisableCharacter(1500208)
    EnableCharacter(1500418)
    DisableCharacter(1500110)
    EnableCharacter(1500419)
    DisableCharacter(1500122)
    EnableCharacter(1500420)
    DisableCharacter(1500120)
    EnableCharacter(1500421)
    DisableCharacter(1500121)
    EnableCharacter(1500422)
    DisableCharacter(1500209)
    EnableCharacter(1500423)
    DisableCharacter(1500210)
    EnableCharacter(1500424)
    DisableCharacter(1500211)
    EnableCharacter(1500425)
    DisableCharacter(1500212)
    EnableCharacter(1500426)
    DisableCharacter(1500213)
    EnableCharacter(1500427)
    DisableCharacter(1500214)
    EnableCharacter(1500428)
    DisableCharacter(1500215)
    EnableCharacter(1500429)
    DisableCharacter(1500216)
    EnableCharacter(1500430)
    DisableCharacter(1500217)
    EnableCharacter(1500431)
    DisableCharacter(1500218)
    EnableCharacter(1500432)
    DisableCharacter(1500219)
    EnableCharacter(1500433)
    DisableCharacter(1500220)
    EnableCharacter(1500434)
    DisableCharacter(1500221)
    EnableCharacter(1500435)
    DisableCharacter(1500010)
    EnableCharacter(1500436)
    DisableCharacter(1500102)
    EnableCharacter(1500437)
    WaitFrames(30)  # enough time for other maps to trigger too
    DisableFlag(TriggerFlags.OopsAllBonewheels)
    # No need to restart.


@RestartOnRest
def HyperAggression():
    """ 11502006: Switch AI param of every enemy to its aggressive version. """
    Await(TriggerFlags.HyperAggression or TriggerFlags.HyperAggressionReTrigger)
    
    SetAIParamID(1500300, 230052)
    SetAIParamID(1500301, 230052)
    SetAIParamID(1500302, 230051)
    SetAIParamID(1500303, 230051)
    SetAIParamID(1500800, 232050)
    SetAIParamID(1500202, 256051)
    SetAIParamID(1500203, 256054)
    SetAIParamID(1500204, 256055)
    SetAIParamID(1500205, 256056)
    SetAIParamID(1500201, 257062)
    SetAIParamID(1500200, 269050)
    SetAIParamID(1500206, 269050)
    SetAIParamID(1500207, 269050)
    SetAIParamID(1500208, 269051)
    SetAIParamID(1500110, 269050)
    SetAIParamID(1500122, 269050)
    SetAIParamID(1500120, 269050)
    SetAIParamID(1500121, 269050)
    SetAIParamID(1500209, 269050)
    SetAIParamID(1500210, 269050)
    SetAIParamID(1500211, 269050)
    SetAIParamID(1500212, 269050)
    SetAIParamID(1500900, 269050)
    SetAIParamID(1500901, 269050)
    SetAIParamID(1500902, 269051)
    SetAIParamID(1500903, 269051)
    SetAIParamID(1500904, 269051)
    SetAIParamID(1500905, 269050)
    SetAIParamID(1500906, 269050)
    SetAIParamID(1500213, 270050)
    SetAIParamID(1500214, 270052)
    SetAIParamID(1500215, 270052)
    SetAIParamID(1500216, 270052)
    SetAIParamID(1500217, 270052)
    SetAIParamID(1500218, 270052)
    SetAIParamID(1500219, 270051)
    SetAIParamID(1500220, 270052)
    SetAIParamID(1500907, 270052)
    SetAIParamID(1500908, 270051)
    SetAIParamID(1500909, 270052)
    SetAIParamID(1500221, 270050)
    SetAIParamID(1500010, 278050)
    SetAIParamID(1500101, 286050)
    SetAIParamID(1500100, 286051)
    SetAIParamID(1500102, 286050)
    SetAIParamID(1503900, 349050)
    SetAIParamID(1503910, 349050)
    SetAIParamID(1503920, 349050)
    SetAIParamID(1503901, 349150)
    SetAIParamID(1503911, 349150)
    SetAIParamID(1503921, 349150)
    SetAIParamID(1503902, 349150)
    SetAIParamID(1503912, 349150)
    SetAIParamID(1503922, 349150)
    SetAIParamID(1500600, 537050)
    SetAIParamID(1500601, 537050)
    SetAIParamID(1500602, 537050)
    SetAIParamID(1500603, 537050)
    SetAIParamID(1500604, 537050)
    SetAIParamID(1500605, 537050)
    SetAIParamID(1500606, 537050)
    SetAIParamID(1500400, 293050)
    SetAIParamID(1500401, 293050)
    SetAIParamID(1500402, 293050)
    SetAIParamID(1500403, 293050)
    SetAIParamID(1500404, 293050)
    SetAIParamID(1500405, 293050)
    SetAIParamID(1500406, 293050)
    SetAIParamID(1500407, 293050)
    SetAIParamID(1500408, 293050)
    SetAIParamID(1500409, 293050)
    SetAIParamID(1500410, 293050)
    SetAIParamID(1500411, 293050)
    SetAIParamID(1500412, 293050)
    SetAIParamID(1500413, 293050)
    SetAIParamID(1500414, 293050)
    SetAIParamID(1500415, 293050)
    SetAIParamID(1500416, 293050)
    SetAIParamID(1500417, 293050)
    SetAIParamID(1500418, 293050)
    SetAIParamID(1500419, 293050)
    SetAIParamID(1500420, 293050)
    SetAIParamID(1500421, 293050)
    SetAIParamID(1500422, 293050)
    SetAIParamID(1500423, 293050)
    SetAIParamID(1500424, 293050)
    SetAIParamID(1500425, 293050)
    SetAIParamID(1500426, 293050)
    SetAIParamID(1500427, 293050)
    SetAIParamID(1500428, 293050)
    SetAIParamID(1500429, 293050)
    SetAIParamID(1500430, 293050)
    SetAIParamID(1500431, 293050)
    SetAIParamID(1500432, 293050)
    SetAIParamID(1500433, 293050)
    SetAIParamID(1500434, 293050)
    SetAIParamID(1500435, 293050)
    SetAIParamID(1500436, 293050)
    SetAIParamID(1500437, 293050)
        
    # Common EMEVD manages the flags that control this event.
    Await(not TriggerFlags.HyperAggressionReTrigger)
    
    SetAIParamID(1500300, 230002)
    SetAIParamID(1500301, 230002)
    SetAIParamID(1500302, 230001)
    SetAIParamID(1500303, 230001)
    SetAIParamID(1500800, 232000)
    SetAIParamID(1500202, 256001)
    SetAIParamID(1500203, 256004)
    SetAIParamID(1500204, 256005)
    SetAIParamID(1500205, 256006)
    SetAIParamID(1500201, 257012)
    SetAIParamID(1500200, 269000)
    SetAIParamID(1500206, 269000)
    SetAIParamID(1500207, 269000)
    SetAIParamID(1500208, 269001)
    SetAIParamID(1500110, 269000)
    SetAIParamID(1500122, 269000)
    SetAIParamID(1500120, 269000)
    SetAIParamID(1500121, 269000)
    SetAIParamID(1500209, 269000)
    SetAIParamID(1500210, 269000)
    SetAIParamID(1500211, 269000)
    SetAIParamID(1500212, 269000)
    SetAIParamID(1500900, 269000)
    SetAIParamID(1500901, 269000)
    SetAIParamID(1500902, 269001)
    SetAIParamID(1500903, 269001)
    SetAIParamID(1500904, 269001)
    SetAIParamID(1500905, 269000)
    SetAIParamID(1500906, 269000)
    SetAIParamID(1500213, 270000)
    SetAIParamID(1500214, 270002)
    SetAIParamID(1500215, 270002)
    SetAIParamID(1500216, 270002)
    SetAIParamID(1500217, 270002)
    SetAIParamID(1500218, 270002)
    SetAIParamID(1500219, 270001)
    SetAIParamID(1500220, 270002)
    SetAIParamID(1500907, 270002)
    SetAIParamID(1500908, 270001)
    SetAIParamID(1500909, 270002)
    SetAIParamID(1500221, 270000)
    SetAIParamID(1500010, 278000)
    SetAIParamID(1500101, 286000)
    SetAIParamID(1500100, 286001)
    SetAIParamID(1500102, 286000)
    SetAIParamID(1503900, 349000)
    SetAIParamID(1503910, 349000)
    SetAIParamID(1503920, 349000)
    SetAIParamID(1503901, 349100)
    SetAIParamID(1503911, 349100)
    SetAIParamID(1503921, 349100)
    SetAIParamID(1503902, 349100)
    SetAIParamID(1503912, 349100)
    SetAIParamID(1503922, 349100)
    SetAIParamID(1500600, 537000)
    SetAIParamID(1500601, 537000)
    SetAIParamID(1500602, 537000)
    SetAIParamID(1500603, 537000)
    SetAIParamID(1500604, 537000)
    SetAIParamID(1500605, 537000)
    SetAIParamID(1500606, 537000)
    SetAIParamID(1500400, 293000)
    SetAIParamID(1500401, 293000)
    SetAIParamID(1500402, 293000)
    SetAIParamID(1500403, 293000)
    SetAIParamID(1500404, 293000)
    SetAIParamID(1500405, 293000)
    SetAIParamID(1500406, 293000)
    SetAIParamID(1500407, 293000)
    SetAIParamID(1500408, 293000)
    SetAIParamID(1500409, 293000)
    SetAIParamID(1500410, 293000)
    SetAIParamID(1500411, 293000)
    SetAIParamID(1500412, 293000)
    SetAIParamID(1500413, 293000)
    SetAIParamID(1500414, 293000)
    SetAIParamID(1500415, 293000)
    SetAIParamID(1500416, 293000)
    SetAIParamID(1500417, 293000)
    SetAIParamID(1500418, 293000)
    SetAIParamID(1500419, 293000)
    SetAIParamID(1500420, 293000)
    SetAIParamID(1500421, 293000)
    SetAIParamID(1500422, 293000)
    SetAIParamID(1500423, 293000)
    SetAIParamID(1500424, 293000)
    SetAIParamID(1500425, 293000)
    SetAIParamID(1500426, 293000)
    SetAIParamID(1500427, 293000)
    SetAIParamID(1500428, 293000)
    SetAIParamID(1500429, 293000)
    SetAIParamID(1500430, 293000)
    SetAIParamID(1500431, 293000)
    SetAIParamID(1500432, 293000)
    SetAIParamID(1500433, 293000)
    SetAIParamID(1500434, 293000)
    SetAIParamID(1500435, 293000)
    SetAIParamID(1500436, 293000)
    SetAIParamID(1500437, 293000)
    
    return RESTART


@RestartOnRest
def EnemySpeedUp():
    """ 11502200: Temporary enemy effect. """
    Await(TriggerFlags.EnemySpeedUp)
    AddSpecialEffect(6030, 200000)
    AddSpecialEffect(6250, 200000)
    AddSpecialEffect(6280, 200000)
    AddSpecialEffect(6510, 200000)
    AddSpecialEffect(6043, 200000)
    AddSpecialEffect(6600, 200000)
    AddSpecialEffect(1500961, 200000)
    AddSpecialEffect(1500300, 200000)
    AddSpecialEffect(1500301, 200000)
    AddSpecialEffect(1500302, 200000)
    AddSpecialEffect(1500303, 200000)
    AddSpecialEffect(1500800, 200000)
    AddSpecialEffect(1500202, 200000)
    AddSpecialEffect(1500203, 200000)
    AddSpecialEffect(1500204, 200000)
    AddSpecialEffect(1500205, 200000)
    AddSpecialEffect(1500201, 200000)
    AddSpecialEffect(1500200, 200000)
    AddSpecialEffect(1500206, 200000)
    AddSpecialEffect(1500207, 200000)
    AddSpecialEffect(1500208, 200000)
    AddSpecialEffect(1500110, 200000)
    AddSpecialEffect(1500122, 200000)
    AddSpecialEffect(1500120, 200000)
    AddSpecialEffect(1500121, 200000)
    AddSpecialEffect(1500209, 200000)
    AddSpecialEffect(1500210, 200000)
    AddSpecialEffect(1500211, 200000)
    AddSpecialEffect(1500212, 200000)
    AddSpecialEffect(1500900, 200000)
    AddSpecialEffect(1500901, 200000)
    AddSpecialEffect(1500902, 200000)
    AddSpecialEffect(1500903, 200000)
    AddSpecialEffect(1500904, 200000)
    AddSpecialEffect(1500905, 200000)
    AddSpecialEffect(1500906, 200000)
    AddSpecialEffect(1500213, 200000)
    AddSpecialEffect(1500214, 200000)
    AddSpecialEffect(1500215, 200000)
    AddSpecialEffect(1500216, 200000)
    AddSpecialEffect(1500217, 200000)
    AddSpecialEffect(1500218, 200000)
    AddSpecialEffect(1500219, 200000)
    AddSpecialEffect(1500220, 200000)
    AddSpecialEffect(1500907, 200000)
    AddSpecialEffect(1500908, 200000)
    AddSpecialEffect(1500909, 200000)
    AddSpecialEffect(1500221, 200000)
    AddSpecialEffect(1500010, 200000)
    AddSpecialEffect(1500101, 200000)
    AddSpecialEffect(1500100, 200000)
    AddSpecialEffect(1500102, 200000)
    AddSpecialEffect(1503900, 200000)
    AddSpecialEffect(1503910, 200000)
    AddSpecialEffect(1503920, 200000)
    AddSpecialEffect(1503901, 200000)
    AddSpecialEffect(1503911, 200000)
    AddSpecialEffect(1503921, 200000)
    AddSpecialEffect(1503902, 200000)
    AddSpecialEffect(1503912, 200000)
    AddSpecialEffect(1503922, 200000)
    WaitFrames(10)  # give other loaded maps time to trigger
    DisableFlag(TriggerFlags.EnemySpeedUp)
    return RESTART


@RestartOnRest
def EnemyExtremeSpeedUp():
    """ 11502201: Temporary enemy effect. """
    Await(TriggerFlags.EnemyExtremeSpeedUp)
    AddSpecialEffect(6030, 200001)
    AddSpecialEffect(6250, 200001)
    AddSpecialEffect(6280, 200001)
    AddSpecialEffect(6510, 200001)
    AddSpecialEffect(6043, 200001)
    AddSpecialEffect(6600, 200001)
    AddSpecialEffect(1500961, 200001)
    AddSpecialEffect(1500300, 200001)
    AddSpecialEffect(1500301, 200001)
    AddSpecialEffect(1500302, 200001)
    AddSpecialEffect(1500303, 200001)
    AddSpecialEffect(1500800, 200001)
    AddSpecialEffect(1500202, 200001)
    AddSpecialEffect(1500203, 200001)
    AddSpecialEffect(1500204, 200001)
    AddSpecialEffect(1500205, 200001)
    AddSpecialEffect(1500201, 200001)
    AddSpecialEffect(1500200, 200001)
    AddSpecialEffect(1500206, 200001)
    AddSpecialEffect(1500207, 200001)
    AddSpecialEffect(1500208, 200001)
    AddSpecialEffect(1500110, 200001)
    AddSpecialEffect(1500122, 200001)
    AddSpecialEffect(1500120, 200001)
    AddSpecialEffect(1500121, 200001)
    AddSpecialEffect(1500209, 200001)
    AddSpecialEffect(1500210, 200001)
    AddSpecialEffect(1500211, 200001)
    AddSpecialEffect(1500212, 200001)
    AddSpecialEffect(1500900, 200001)
    AddSpecialEffect(1500901, 200001)
    AddSpecialEffect(1500902, 200001)
    AddSpecialEffect(1500903, 200001)
    AddSpecialEffect(1500904, 200001)
    AddSpecialEffect(1500905, 200001)
    AddSpecialEffect(1500906, 200001)
    AddSpecialEffect(1500213, 200001)
    AddSpecialEffect(1500214, 200001)
    AddSpecialEffect(1500215, 200001)
    AddSpecialEffect(1500216, 200001)
    AddSpecialEffect(1500217, 200001)
    AddSpecialEffect(1500218, 200001)
    AddSpecialEffect(1500219, 200001)
    AddSpecialEffect(1500220, 200001)
    AddSpecialEffect(1500907, 200001)
    AddSpecialEffect(1500908, 200001)
    AddSpecialEffect(1500909, 200001)
    AddSpecialEffect(1500221, 200001)
    AddSpecialEffect(1500010, 200001)
    AddSpecialEffect(1500101, 200001)
    AddSpecialEffect(1500100, 200001)
    AddSpecialEffect(1500102, 200001)
    AddSpecialEffect(1503900, 200001)
    AddSpecialEffect(1503910, 200001)
    AddSpecialEffect(1503920, 200001)
    AddSpecialEffect(1503901, 200001)
    AddSpecialEffect(1503911, 200001)
    AddSpecialEffect(1503921, 200001)
    AddSpecialEffect(1503902, 200001)
    AddSpecialEffect(1503912, 200001)
    AddSpecialEffect(1503922, 200001)
    WaitFrames(10)  # give other loaded maps time to trigger
    DisableFlag(TriggerFlags.EnemyExtremeSpeedUp)
    return RESTART


@RestartOnRest
def EnemySpeedDown():
    """ 11502202: Temporary enemy effect. """
    Await(TriggerFlags.EnemySpeedDown)
    AddSpecialEffect(6030, 200002)
    AddSpecialEffect(6250, 200002)
    AddSpecialEffect(6280, 200002)
    AddSpecialEffect(6510, 200002)
    AddSpecialEffect(6043, 200002)
    AddSpecialEffect(6600, 200002)
    AddSpecialEffect(1500961, 200002)
    AddSpecialEffect(1500300, 200002)
    AddSpecialEffect(1500301, 200002)
    AddSpecialEffect(1500302, 200002)
    AddSpecialEffect(1500303, 200002)
    AddSpecialEffect(1500800, 200002)
    AddSpecialEffect(1500202, 200002)
    AddSpecialEffect(1500203, 200002)
    AddSpecialEffect(1500204, 200002)
    AddSpecialEffect(1500205, 200002)
    AddSpecialEffect(1500201, 200002)
    AddSpecialEffect(1500200, 200002)
    AddSpecialEffect(1500206, 200002)
    AddSpecialEffect(1500207, 200002)
    AddSpecialEffect(1500208, 200002)
    AddSpecialEffect(1500110, 200002)
    AddSpecialEffect(1500122, 200002)
    AddSpecialEffect(1500120, 200002)
    AddSpecialEffect(1500121, 200002)
    AddSpecialEffect(1500209, 200002)
    AddSpecialEffect(1500210, 200002)
    AddSpecialEffect(1500211, 200002)
    AddSpecialEffect(1500212, 200002)
    AddSpecialEffect(1500900, 200002)
    AddSpecialEffect(1500901, 200002)
    AddSpecialEffect(1500902, 200002)
    AddSpecialEffect(1500903, 200002)
    AddSpecialEffect(1500904, 200002)
    AddSpecialEffect(1500905, 200002)
    AddSpecialEffect(1500906, 200002)
    AddSpecialEffect(1500213, 200002)
    AddSpecialEffect(1500214, 200002)
    AddSpecialEffect(1500215, 200002)
    AddSpecialEffect(1500216, 200002)
    AddSpecialEffect(1500217, 200002)
    AddSpecialEffect(1500218, 200002)
    AddSpecialEffect(1500219, 200002)
    AddSpecialEffect(1500220, 200002)
    AddSpecialEffect(1500907, 200002)
    AddSpecialEffect(1500908, 200002)
    AddSpecialEffect(1500909, 200002)
    AddSpecialEffect(1500221, 200002)
    AddSpecialEffect(1500010, 200002)
    AddSpecialEffect(1500101, 200002)
    AddSpecialEffect(1500100, 200002)
    AddSpecialEffect(1500102, 200002)
    AddSpecialEffect(1503900, 200002)
    AddSpecialEffect(1503910, 200002)
    AddSpecialEffect(1503920, 200002)
    AddSpecialEffect(1503901, 200002)
    AddSpecialEffect(1503911, 200002)
    AddSpecialEffect(1503921, 200002)
    AddSpecialEffect(1503902, 200002)
    AddSpecialEffect(1503912, 200002)
    AddSpecialEffect(1503922, 200002)
    WaitFrames(10)  # give other loaded maps time to trigger
    DisableFlag(TriggerFlags.EnemySpeedDown)
    return RESTART


@RestartOnRest
def EnemyExtremeSpeedDown():
    """ 11502203: Temporary enemy effect. """
    Await(TriggerFlags.EnemyExtremeSpeedDown)
    AddSpecialEffect(6030, 200003)
    AddSpecialEffect(6250, 200003)
    AddSpecialEffect(6280, 200003)
    AddSpecialEffect(6510, 200003)
    AddSpecialEffect(6043, 200003)
    AddSpecialEffect(6600, 200003)
    AddSpecialEffect(1500961, 200003)
    AddSpecialEffect(1500300, 200003)
    AddSpecialEffect(1500301, 200003)
    AddSpecialEffect(1500302, 200003)
    AddSpecialEffect(1500303, 200003)
    AddSpecialEffect(1500800, 200003)
    AddSpecialEffect(1500202, 200003)
    AddSpecialEffect(1500203, 200003)
    AddSpecialEffect(1500204, 200003)
    AddSpecialEffect(1500205, 200003)
    AddSpecialEffect(1500201, 200003)
    AddSpecialEffect(1500200, 200003)
    AddSpecialEffect(1500206, 200003)
    AddSpecialEffect(1500207, 200003)
    AddSpecialEffect(1500208, 200003)
    AddSpecialEffect(1500110, 200003)
    AddSpecialEffect(1500122, 200003)
    AddSpecialEffect(1500120, 200003)
    AddSpecialEffect(1500121, 200003)
    AddSpecialEffect(1500209, 200003)
    AddSpecialEffect(1500210, 200003)
    AddSpecialEffect(1500211, 200003)
    AddSpecialEffect(1500212, 200003)
    AddSpecialEffect(1500900, 200003)
    AddSpecialEffect(1500901, 200003)
    AddSpecialEffect(1500902, 200003)
    AddSpecialEffect(1500903, 200003)
    AddSpecialEffect(1500904, 200003)
    AddSpecialEffect(1500905, 200003)
    AddSpecialEffect(1500906, 200003)
    AddSpecialEffect(1500213, 200003)
    AddSpecialEffect(1500214, 200003)
    AddSpecialEffect(1500215, 200003)
    AddSpecialEffect(1500216, 200003)
    AddSpecialEffect(1500217, 200003)
    AddSpecialEffect(1500218, 200003)
    AddSpecialEffect(1500219, 200003)
    AddSpecialEffect(1500220, 200003)
    AddSpecialEffect(1500907, 200003)
    AddSpecialEffect(1500908, 200003)
    AddSpecialEffect(1500909, 200003)
    AddSpecialEffect(1500221, 200003)
    AddSpecialEffect(1500010, 200003)
    AddSpecialEffect(1500101, 200003)
    AddSpecialEffect(1500100, 200003)
    AddSpecialEffect(1500102, 200003)
    AddSpecialEffect(1503900, 200003)
    AddSpecialEffect(1503910, 200003)
    AddSpecialEffect(1503920, 200003)
    AddSpecialEffect(1503901, 200003)
    AddSpecialEffect(1503911, 200003)
    AddSpecialEffect(1503921, 200003)
    AddSpecialEffect(1503902, 200003)
    AddSpecialEffect(1503912, 200003)
    AddSpecialEffect(1503922, 200003)
    WaitFrames(10)  # give other loaded maps time to trigger
    DisableFlag(TriggerFlags.EnemyExtremeSpeedDown)
    return RESTART


@RestartOnRest
def EnemyHealthRegain():
    """ 11502204: Temporary enemy effect. """
    Await(TriggerFlags.EnemyHealthRegain)
    AddSpecialEffect(6030, 200004)
    AddSpecialEffect(6250, 200004)
    AddSpecialEffect(6280, 200004)
    AddSpecialEffect(6510, 200004)
    AddSpecialEffect(6043, 200004)
    AddSpecialEffect(6600, 200004)
    AddSpecialEffect(1500961, 200004)
    AddSpecialEffect(1500300, 200004)
    AddSpecialEffect(1500301, 200004)
    AddSpecialEffect(1500302, 200004)
    AddSpecialEffect(1500303, 200004)
    AddSpecialEffect(1500800, 200004)
    AddSpecialEffect(1500202, 200004)
    AddSpecialEffect(1500203, 200004)
    AddSpecialEffect(1500204, 200004)
    AddSpecialEffect(1500205, 200004)
    AddSpecialEffect(1500201, 200004)
    AddSpecialEffect(1500200, 200004)
    AddSpecialEffect(1500206, 200004)
    AddSpecialEffect(1500207, 200004)
    AddSpecialEffect(1500208, 200004)
    AddSpecialEffect(1500110, 200004)
    AddSpecialEffect(1500122, 200004)
    AddSpecialEffect(1500120, 200004)
    AddSpecialEffect(1500121, 200004)
    AddSpecialEffect(1500209, 200004)
    AddSpecialEffect(1500210, 200004)
    AddSpecialEffect(1500211, 200004)
    AddSpecialEffect(1500212, 200004)
    AddSpecialEffect(1500900, 200004)
    AddSpecialEffect(1500901, 200004)
    AddSpecialEffect(1500902, 200004)
    AddSpecialEffect(1500903, 200004)
    AddSpecialEffect(1500904, 200004)
    AddSpecialEffect(1500905, 200004)
    AddSpecialEffect(1500906, 200004)
    AddSpecialEffect(1500213, 200004)
    AddSpecialEffect(1500214, 200004)
    AddSpecialEffect(1500215, 200004)
    AddSpecialEffect(1500216, 200004)
    AddSpecialEffect(1500217, 200004)
    AddSpecialEffect(1500218, 200004)
    AddSpecialEffect(1500219, 200004)
    AddSpecialEffect(1500220, 200004)
    AddSpecialEffect(1500907, 200004)
    AddSpecialEffect(1500908, 200004)
    AddSpecialEffect(1500909, 200004)
    AddSpecialEffect(1500221, 200004)
    AddSpecialEffect(1500010, 200004)
    AddSpecialEffect(1500101, 200004)
    AddSpecialEffect(1500100, 200004)
    AddSpecialEffect(1500102, 200004)
    AddSpecialEffect(1503900, 200004)
    AddSpecialEffect(1503910, 200004)
    AddSpecialEffect(1503920, 200004)
    AddSpecialEffect(1503901, 200004)
    AddSpecialEffect(1503911, 200004)
    AddSpecialEffect(1503921, 200004)
    AddSpecialEffect(1503902, 200004)
    AddSpecialEffect(1503912, 200004)
    AddSpecialEffect(1503922, 200004)
    WaitFrames(10)  # give other loaded maps time to trigger
    DisableFlag(TriggerFlags.EnemyHealthRegain)
    return RESTART


@RestartOnRest
def EnemyMaxHealthUp():
    """ 11502205: Temporary enemy effect. """
    Await(TriggerFlags.EnemyMaxHealthUp)
    AddSpecialEffect(6030, 200005)
    AddSpecialEffect(6250, 200005)
    AddSpecialEffect(6280, 200005)
    AddSpecialEffect(6510, 200005)
    AddSpecialEffect(6043, 200005)
    AddSpecialEffect(6600, 200005)
    AddSpecialEffect(1500961, 200005)
    AddSpecialEffect(1500300, 200005)
    AddSpecialEffect(1500301, 200005)
    AddSpecialEffect(1500302, 200005)
    AddSpecialEffect(1500303, 200005)
    AddSpecialEffect(1500800, 200005)
    AddSpecialEffect(1500202, 200005)
    AddSpecialEffect(1500203, 200005)
    AddSpecialEffect(1500204, 200005)
    AddSpecialEffect(1500205, 200005)
    AddSpecialEffect(1500201, 200005)
    AddSpecialEffect(1500200, 200005)
    AddSpecialEffect(1500206, 200005)
    AddSpecialEffect(1500207, 200005)
    AddSpecialEffect(1500208, 200005)
    AddSpecialEffect(1500110, 200005)
    AddSpecialEffect(1500122, 200005)
    AddSpecialEffect(1500120, 200005)
    AddSpecialEffect(1500121, 200005)
    AddSpecialEffect(1500209, 200005)
    AddSpecialEffect(1500210, 200005)
    AddSpecialEffect(1500211, 200005)
    AddSpecialEffect(1500212, 200005)
    AddSpecialEffect(1500900, 200005)
    AddSpecialEffect(1500901, 200005)
    AddSpecialEffect(1500902, 200005)
    AddSpecialEffect(1500903, 200005)
    AddSpecialEffect(1500904, 200005)
    AddSpecialEffect(1500905, 200005)
    AddSpecialEffect(1500906, 200005)
    AddSpecialEffect(1500213, 200005)
    AddSpecialEffect(1500214, 200005)
    AddSpecialEffect(1500215, 200005)
    AddSpecialEffect(1500216, 200005)
    AddSpecialEffect(1500217, 200005)
    AddSpecialEffect(1500218, 200005)
    AddSpecialEffect(1500219, 200005)
    AddSpecialEffect(1500220, 200005)
    AddSpecialEffect(1500907, 200005)
    AddSpecialEffect(1500908, 200005)
    AddSpecialEffect(1500909, 200005)
    AddSpecialEffect(1500221, 200005)
    AddSpecialEffect(1500010, 200005)
    AddSpecialEffect(1500101, 200005)
    AddSpecialEffect(1500100, 200005)
    AddSpecialEffect(1500102, 200005)
    AddSpecialEffect(1503900, 200005)
    AddSpecialEffect(1503910, 200005)
    AddSpecialEffect(1503920, 200005)
    AddSpecialEffect(1503901, 200005)
    AddSpecialEffect(1503911, 200005)
    AddSpecialEffect(1503921, 200005)
    AddSpecialEffect(1503902, 200005)
    AddSpecialEffect(1503912, 200005)
    AddSpecialEffect(1503922, 200005)
    WaitFrames(10)  # give other loaded maps time to trigger
    DisableFlag(TriggerFlags.EnemyMaxHealthUp)
    return RESTART


@RestartOnRest
def EnemyMaxHealthDown():
    """ 11502206: Temporary enemy effect. """
    Await(TriggerFlags.EnemyMaxHealthDown)
    AddSpecialEffect(6030, 200006)
    AddSpecialEffect(6250, 200006)
    AddSpecialEffect(6280, 200006)
    AddSpecialEffect(6510, 200006)
    AddSpecialEffect(6043, 200006)
    AddSpecialEffect(6600, 200006)
    AddSpecialEffect(1500961, 200006)
    AddSpecialEffect(1500300, 200006)
    AddSpecialEffect(1500301, 200006)
    AddSpecialEffect(1500302, 200006)
    AddSpecialEffect(1500303, 200006)
    AddSpecialEffect(1500800, 200006)
    AddSpecialEffect(1500202, 200006)
    AddSpecialEffect(1500203, 200006)
    AddSpecialEffect(1500204, 200006)
    AddSpecialEffect(1500205, 200006)
    AddSpecialEffect(1500201, 200006)
    AddSpecialEffect(1500200, 200006)
    AddSpecialEffect(1500206, 200006)
    AddSpecialEffect(1500207, 200006)
    AddSpecialEffect(1500208, 200006)
    AddSpecialEffect(1500110, 200006)
    AddSpecialEffect(1500122, 200006)
    AddSpecialEffect(1500120, 200006)
    AddSpecialEffect(1500121, 200006)
    AddSpecialEffect(1500209, 200006)
    AddSpecialEffect(1500210, 200006)
    AddSpecialEffect(1500211, 200006)
    AddSpecialEffect(1500212, 200006)
    AddSpecialEffect(1500900, 200006)
    AddSpecialEffect(1500901, 200006)
    AddSpecialEffect(1500902, 200006)
    AddSpecialEffect(1500903, 200006)
    AddSpecialEffect(1500904, 200006)
    AddSpecialEffect(1500905, 200006)
    AddSpecialEffect(1500906, 200006)
    AddSpecialEffect(1500213, 200006)
    AddSpecialEffect(1500214, 200006)
    AddSpecialEffect(1500215, 200006)
    AddSpecialEffect(1500216, 200006)
    AddSpecialEffect(1500217, 200006)
    AddSpecialEffect(1500218, 200006)
    AddSpecialEffect(1500219, 200006)
    AddSpecialEffect(1500220, 200006)
    AddSpecialEffect(1500907, 200006)
    AddSpecialEffect(1500908, 200006)
    AddSpecialEffect(1500909, 200006)
    AddSpecialEffect(1500221, 200006)
    AddSpecialEffect(1500010, 200006)
    AddSpecialEffect(1500101, 200006)
    AddSpecialEffect(1500100, 200006)
    AddSpecialEffect(1500102, 200006)
    AddSpecialEffect(1503900, 200006)
    AddSpecialEffect(1503910, 200006)
    AddSpecialEffect(1503920, 200006)
    AddSpecialEffect(1503901, 200006)
    AddSpecialEffect(1503911, 200006)
    AddSpecialEffect(1503921, 200006)
    AddSpecialEffect(1503902, 200006)
    AddSpecialEffect(1503912, 200006)
    AddSpecialEffect(1503922, 200006)
    WaitFrames(10)  # give other loaded maps time to trigger
    DisableFlag(TriggerFlags.EnemyMaxHealthDown)
    return RESTART


@RestartOnRest
def EnemyDefenseUp():
    """ 11502207: Temporary enemy effect. """
    Await(TriggerFlags.EnemyDefenseUp)
    AddSpecialEffect(6030, 200007)
    AddSpecialEffect(6250, 200007)
    AddSpecialEffect(6280, 200007)
    AddSpecialEffect(6510, 200007)
    AddSpecialEffect(6043, 200007)
    AddSpecialEffect(6600, 200007)
    AddSpecialEffect(1500961, 200007)
    AddSpecialEffect(1500300, 200007)
    AddSpecialEffect(1500301, 200007)
    AddSpecialEffect(1500302, 200007)
    AddSpecialEffect(1500303, 200007)
    AddSpecialEffect(1500800, 200007)
    AddSpecialEffect(1500202, 200007)
    AddSpecialEffect(1500203, 200007)
    AddSpecialEffect(1500204, 200007)
    AddSpecialEffect(1500205, 200007)
    AddSpecialEffect(1500201, 200007)
    AddSpecialEffect(1500200, 200007)
    AddSpecialEffect(1500206, 200007)
    AddSpecialEffect(1500207, 200007)
    AddSpecialEffect(1500208, 200007)
    AddSpecialEffect(1500110, 200007)
    AddSpecialEffect(1500122, 200007)
    AddSpecialEffect(1500120, 200007)
    AddSpecialEffect(1500121, 200007)
    AddSpecialEffect(1500209, 200007)
    AddSpecialEffect(1500210, 200007)
    AddSpecialEffect(1500211, 200007)
    AddSpecialEffect(1500212, 200007)
    AddSpecialEffect(1500900, 200007)
    AddSpecialEffect(1500901, 200007)
    AddSpecialEffect(1500902, 200007)
    AddSpecialEffect(1500903, 200007)
    AddSpecialEffect(1500904, 200007)
    AddSpecialEffect(1500905, 200007)
    AddSpecialEffect(1500906, 200007)
    AddSpecialEffect(1500213, 200007)
    AddSpecialEffect(1500214, 200007)
    AddSpecialEffect(1500215, 200007)
    AddSpecialEffect(1500216, 200007)
    AddSpecialEffect(1500217, 200007)
    AddSpecialEffect(1500218, 200007)
    AddSpecialEffect(1500219, 200007)
    AddSpecialEffect(1500220, 200007)
    AddSpecialEffect(1500907, 200007)
    AddSpecialEffect(1500908, 200007)
    AddSpecialEffect(1500909, 200007)
    AddSpecialEffect(1500221, 200007)
    AddSpecialEffect(1500010, 200007)
    AddSpecialEffect(1500101, 200007)
    AddSpecialEffect(1500100, 200007)
    AddSpecialEffect(1500102, 200007)
    AddSpecialEffect(1503900, 200007)
    AddSpecialEffect(1503910, 200007)
    AddSpecialEffect(1503920, 200007)
    AddSpecialEffect(1503901, 200007)
    AddSpecialEffect(1503911, 200007)
    AddSpecialEffect(1503921, 200007)
    AddSpecialEffect(1503902, 200007)
    AddSpecialEffect(1503912, 200007)
    AddSpecialEffect(1503922, 200007)
    WaitFrames(10)  # give other loaded maps time to trigger
    DisableFlag(TriggerFlags.EnemyDefenseUp)
    return RESTART
