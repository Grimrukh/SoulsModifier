"""
linked:


strings:

"""
from soulstruct.darksouls1r.events import *
from ..entities.m10_00_00_00_entities import *
from ..entities.common_entities import *


def Constructor():
    """ 0: Event 0 """
    RegisterBonfire(
        11000992,
        obj=Objects.o0200_0000,
        reaction_distance=2.0,
        reaction_angle=180.0,
        initial_kindle_level=0,
    )
    RegisterLadder(start_climbing_flag=11000010, stop_climbing_flag=11000011, obj=Objects.o1205)
    RegisterStatue(Objects.o0100_0000, game_map=DEPTHS, statue_type=StatueType.Stone)
    RegisterStatue(Objects.o0100_0001, game_map=DEPTHS, statue_type=StatueType.Stone)
    RegisterStatue(Objects.o0100_0002, game_map=DEPTHS, statue_type=StatueType.Stone)
    RegisterStatue(Objects.o0100_0003, game_map=DEPTHS, statue_type=StatueType.Stone)
    RegisterStatue(Objects.o0100_0004, game_map=DEPTHS, statue_type=StatueType.Stone)
    RegisterStatue(Objects.o0100_0005, game_map=DEPTHS, statue_type=StatueType.Stone)
    RegisterStatue(Objects.o0100_0006, game_map=DEPTHS, statue_type=StatueType.Stone)
    RegisterStatue(Objects.o0100_0007, game_map=DEPTHS, statue_type=StatueType.Stone)
    SkipLinesIfClient(5)
    DisableFlag(11000000)
    DisableObject(Objects.o1401_0000)
    DeleteVFX(VFX.MultiplayerFog1, erase_root_only=False)
    DisableObject(Objects.o1402_0000)
    DeleteVFX(VFX.MultiplayerFog2, erase_root_only=False)
    SkipLinesIfFlagOff(1, 11000100)
    EndOfAnimation(Objects.o1319_0000, 0)
    RunEvent(
        11000090,
        slot=0,
        args=(Objects.o1420_0000, VFX.CheckpointFog1, Boxes.CheckpointFog1FrontSide, Boxes.CheckpointFog1BackSide),
    )
    RunEvent(11000100)
    RunEvent(11000101)
    RunEvent(11000120, slot=0, args=(11000120, 10010877, Objects.o1315_0000, 10010883, 2018))
    RunEvent(11000200)
    RunEvent(11000800)
    RunEvent(11005050)
    RunEvent(11005060)
    RunEvent(11005070)
    RunEvent(11000110)
    RunEvent(11000111)
    RunEvent(11000600, slot=0, args=(Objects.o0110_0000, 11000600))
    DisableSoundEvent(1003800)
    SkipLinesIfFlagOff(4, 2)
    RunEvent(11005392)
    DisableObject(Objects.o1400_0000)
    DeleteVFX(VFX.BossEntranceFog, erase_root_only=False)
    SkipLines(10)
    RunEvent(11005390)
    RunEvent(11005391)
    RunEvent(11005393)
    RunEvent(11005392)
    RunEvent(11000001)
    RunEvent(11005394)
    RunEvent(11005395)
    RunEvent(11005396)
    RunEvent(11005397)
    RunEvent(11005398)
    RunEvent(11005000, slot=0, args=(Objects.o1340_0000, Objects.o1340_0000, 1))
    RunEvent(11005000, slot=1, args=(Objects.o1340_0001, Objects.o1340_0001, 1))
    RunEvent(11005000, slot=2, args=(Objects.o1340_0002, Objects.o1340_0002, 3))
    RunEvent(11005200, slot=0, args=(Characters.c2500_0003, Boxes.HierarchyA))
    RunEvent(11005200, slot=1, args=(Characters.c2500_0004, Boxes.HierarchyA))
    RunEvent(11005200, slot=2, args=(Characters.c2500_0005, Boxes.HierarchyA))
    RunEvent(11005200, slot=3, args=(Characters.c2500_0006, Boxes.HierarchyA))
    RunEvent(11005200, slot=4, args=(Characters.c2500_0007, Boxes.HierarchyA))
    RunEvent(11005200, slot=5, args=(Characters.c2500_0008, Boxes.HierarchyA))
    RunEvent(11005200, slot=6, args=(Characters.c3340_0002, Boxes.HierarchyB))
    RunEvent(11005200, slot=7, args=(Characters.c3340_0000, Boxes.HierarchyB))
    RunEvent(11005200, slot=8, args=(Characters.c3340_0001, Boxes.HierarchyC))
    RunEvent(11005200, slot=9, args=(Characters.c3340_0003, Boxes.HierarchyC))
    RunEvent(11005200, slot=10, args=(Characters.c2500_0009, Boxes.HierarchyC))
    RunEvent(11005100, slot=0, args=(Boxes.Slime0AmbushTrigger, Characters.c3200_0000, 0.0), arg_types="iif")
    RunEvent(11005100, slot=1, args=(Boxes.Slime1AmbushTrigger, Characters.c3200_0001, 0.0), arg_types="iif")
    RunEvent(11005100, slot=2, args=(Boxes.Slime2_3AmbushTrigger, Characters.c3200_0002, 0.0), arg_types="iif")
    RunEvent(
        11005100,
        slot=3,
        args=(Boxes.Slime2_3AmbushTrigger, Characters.c3200_0003, 0.6000000238418579),
        arg_types="iif",
    )
    RunEvent(11005100, slot=4, args=(Boxes.Slime4_5_6AmbushTrigger, Characters.c3200_0004, 0.0), arg_types="iif")
    RunEvent(
        11005100,
        slot=5,
        args=(Boxes.Slime4_5_6AmbushTrigger, Characters.c3200_0005, 0.20000000298023224),
        arg_types="iif",
    )
    RunEvent(
        11005100,
        slot=6,
        args=(Boxes.Slime4_5_6AmbushTrigger, Characters.c3200_0006, 0.8999999761581421),
        arg_types="iif",
    )
    RunEvent(11005100, slot=7, args=(Boxes.Slime7AmbushTrigger, Characters.c3200_0007, 0.0), arg_types="iif")
    RunEvent(11005150, slot=0, args=(Characters.c1201_0000, Objects.o1322_0002, 11009000, 11009010))
    RunEvent(11005150, slot=1, args=(Characters.c1201_0001, Objects.o1322_0005, 11009001, 11009011))
    RunEvent(11005150, slot=2, args=(Characters.c1201_0002, Objects.o1322_0006, 11009002, 11009012))
    RunEvent(11000850, slot=0, args=(Characters.c3340_0002,))
    RunEvent(11000850, slot=1, args=(Characters.c2660_0000,))
    RunEvent(11000850, slot=2, args=(Characters.c2660_0001,))
    RunEvent(11000850, slot=3, args=(Characters.c2370_0000,))
    RunEvent(
        11005843,
        slot=0,
        args=(2, Objects.o1400_0000, Boxes.GapingDragonFogPrompt, Boxes.GapingDragonFogRotationTarget),
    )
    RunEvent(11005844, slot=0, args=(2, Objects.o1400_0000, VFX.BossEntranceFog))
    
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

    DisableCharacter(Characters.c0000_PatchesAmbush)

    HumanityRegistration(Characters.c0000_0005, 8310)
    HumanityRegistration(Characters.c0000_0007, 8462)
    HumanityRegistration(Characters.c0000_0006, 8956)
    RunEvent(11005030)
    RunEvent(11005029)
    RunEvent(11005031)
    RunEvent(11005033)
    RunEvent(11005036)
    RunEvent(11005034)
    RunEvent(11005039)
    RunEvent(11000810)
    RunEvent(11005333)
    RunEvent(11005990, slot=0, args=(11005032, Characters.c0000_0005))
    RunEvent(11005990, slot=1, args=(11005035, Characters.c0000_0007))
    HumanityRegistration(Characters.c0000_0002, 8390)
    SkipLinesIfClient(1)
    DisableFlag(11000580)
    SkipLinesIfFlagOn(3, 11000580)
    SkipLinesIfFlagOn(2, 1250)
    SkipLinesIfFlagOn(1, 1253)
    DisableCharacter(Characters.c0000_0002)
    SkipLinesIfFlagOff(2, 1250)
    DisableGravity(Characters.c0000_0002)
    DisableCharacterCollision(Characters.c0000_0002)
    RunEvent(11000530, slot=0, args=(Characters.c0000_0002, 1250, 1255, 1251))
    RunEvent(11000531, slot=0, args=(Characters.c0000_0002,))
    RunEvent(11000510, slot=0, args=(Characters.c0000_0002, 1253))
    RunEvent(11000520, slot=0, args=(Characters.c0000_0002, 1250, 1255, 1254))
    RunEvent(11000534, slot=0, args=(Characters.c0000_0002,))
    HumanityRegistration(Characters.c0000_0004, 8430)
    SkipLinesIfFlagOn(2, 1434)
    SkipLinesIfFlagOn(1, 1430)
    DisableCharacter(Characters.c0000_0004)
    RunEvent(11000532, slot=0, args=(Characters.c0000_0004, 1430, 1459, 1431))
    RunEvent(11000510, slot=1, args=(Characters.c0000_0004, 1434))
    RunEvent(11000533, slot=0, args=(Characters.c0000_0004, 1435))


def Event11000090(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11000090: Event 11000090 """
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


def Event11005390():
    """ 11005390: Event 11005390 """
    IfFlagOff(1, 2)
    IfActionButton(
        1,
        prompt_text=10010403,
        anchor_entity=Boxes.GapingDragonFogPrompt,
        anchor_type=CoordEntityType.Region,
        line_intersects=Objects.o1400_0000,
        boss_version=True,
    )
    IfConditionTrue(0, input_condition=1)
    RotateToFaceEntity(PLAYER, Boxes.GapingDragonFogRotationTarget)
    ForceAnimation(PLAYER, 7410)
    Restart()


def Event11005391():
    """ 11005391: Event 11005391 """
    IfFlagOff(1, 2)
    IfFlagOn(1, 11005393)
    IfCharacterType(1, PLAYER, CharacterType.WhitePhantom)
    IfActionButton(
        1,
        prompt_text=10010403,
        anchor_entity=Boxes.GapingDragonFogPrompt,
        anchor_type=CoordEntityType.Region,
        trigger_attribute=TriggerAttribute.All,
        line_intersects=Objects.o1400_0000,
        boss_version=True,
    )
    IfConditionTrue(0, input_condition=1)
    RotateToFaceEntity(PLAYER, Boxes.GapingDragonFogRotationTarget)
    ForceAnimation(PLAYER, 7410)
    Restart()


def Event11005393():
    """ 11005393: Event 11005393 """
    SkipLinesIfThisEventOn(3)
    IfFlagOff(1, 2)
    IfCharacterInsideRegion(1, PLAYER, region=Boxes.GapingDragonCutsceneTrigger)
    IfConditionTrue(0, input_condition=1)
    SkipLinesIfClient(1)
    NotifyBossBattleStart()
    ActivateMultiplayerBuffs(Characters.c5260_0000)


@RestartOnRest
def Event11005392():
    """ 11005392: Event 11005392 """
    SkipLinesIfFlagOff(5, 2)
    DisableCharacter(Characters.c5260_0000)
    DisableCharacter(Characters.c5261_0000)
    Kill(Characters.c5260_0000, award_souls=False)
    Kill(Characters.c5261_0000, award_souls=False)
    End()
    SkipLinesIfFlagOn(1, 11000000)
    DisableCharacter(Characters.c5260_0000)
    DisableAI(Characters.c5260_0000)
    IfFlagOn(1, 11005393)
    IfHost(1)
    IfCharacterInsideRegion(1, PLAYER, region=Boxes.GapingDragonCutsceneTrigger)
    IfConditionTrue(0, input_condition=1)
    IfCharacterType(-1, PLAYER, CharacterType.Intruder)
    IfCharacterType(-1, PLAYER, CharacterType.BlackPhantom)
    EndIfConditionTrue(-1)
    SkipLinesIfFlagOn(7, 11000000)
    SkipLinesIfMultiplayer(2)
    PlayCutscene(100000, skippable=True, fade_out=False, player_id=PLAYER)
    SkipLines(1)
    PlayCutscene(100000, skippable=False, fade_out=False, player_id=PLAYER)
    WaitFrames(1)
    EnableCharacter(Characters.c5260_0000)
    EnableFlag(11000000)
    EnableAI(Characters.c5260_0000)
    EnableBossHealthBar(Characters.c5260_0000, name=5260, slot=0)


def Event11000001():
    """ 11000001: Event 11000001 """
    IfCharacterDead(0, Characters.c5260_0000)
    EnableFlag(2)
    Kill(Characters.c5261_0000, award_souls=False)
    KillBoss(1000800)
    DisableObject(Objects.o1400_0000)
    DeleteVFX(VFX.BossEntranceFog, erase_root_only=True)


def Event11005394():
    """ 11005394: Event 11005394 """
    DisableNetworkSync()
    IfFlagOff(1, 2)
    IfFlagOn(1, 11005392)
    IfCharacterInsideRegion(1, PLAYER, region=Boxes.GapingDragonCutsceneTrigger)
    IfConditionTrue(0, input_condition=1)
    EnableSoundEvent(1003800)


def Event11005395():
    """ 11005395: Event 11005395 """
    DisableNetworkSync()
    IfFlagOn(1, 2)
    IfFlagOn(1, 11005394)
    IfConditionTrue(0, input_condition=1)
    DisableSoundEvent(1003800)


@RestartOnRest
def Event11005396():
    """ 11005396: Event 11005396 """
    DisableCharacter(Characters.c5261_0000)
    EndIfThisEventOn()
    IfFlagOn(0, 11005390)
    CreateNPCPart(
        Characters.c5260_0000,
        npc_part_id=5260,
        part_index=NPCPartType.Part1,
        part_health=300,
        damage_correction=1.0,
        body_damage_correction=1.0,
        is_invincible=False,
        start_in_stop_state=False,
    )
    IfCharacterPartHealthLessThanOrEqual(0, Characters.c5260_0000, npc_part_id=5260, value=0)
    EzstateAIRequest(Characters.c5260_0000, command_id=1001, slot=0)
    IfHasTAEEvent(0, Characters.c5260_0000, tae_event_id=400)
    EnableCharacter(Characters.c5261_0000)
    Move(
        Characters.c5261_0000,
        destination=Characters.c5260_0000,
        destination_type=CoordEntityType.Character,
        model_point=100,
        copy_draw_parent=Characters.c5260_0000,
    )
    ForceAnimation(Characters.c5261_0000, 8100)
    SetDisplayMask(Characters.c5260_0000, bit_index=0, switch_type=OnOffChange.On)
    SetCollisionMask(Characters.c5260_0000, bit_index=1, switch_type=OnOffChange.Off)
    AICommand(Characters.c5260_0000, command_id=20, slot=0)
    IfCharacterHuman(-7, PLAYER)
    IfCharacterHollow(-7, PLAYER)
    EndIfConditionFalse(-7)
    AwardItemLot(52610000, host_only=True)


@RestartOnRest
def Event11005397():
    """ 11005397: Event 11005397 """
    IfFlagOn(1, 11005390)
    IfCharacterBackreadEnabled(1, Characters.c5260_0000)
    IfConditionTrue(0, input_condition=1)
    CreateNPCPart(
        Characters.c5260_0000,
        npc_part_id=5261,
        part_index=NPCPartType.Part2,
        part_health=100,
        damage_correction=0.0,
        body_damage_correction=1.0,
        is_invincible=False,
        start_in_stop_state=False,
    )
    SetNPCPartEffects(Characters.c5260_0000, npc_part_id=5261, material_sfx_id=60, material_vfx_id=60)


@RestartOnRest
def Event11005398():
    """ 11005398: Event 11005398 """
    IfFlagOn(0, 11005390)
    CreateNPCPart(
        Characters.c5260_0000,
        npc_part_id=5262,
        part_index=NPCPartType.Part3,
        part_health=1,
        damage_correction=1.0,
        body_damage_correction=1.0,
        is_invincible=False,
        start_in_stop_state=False,
    )
    IfCharacterPartHealthLessThanOrEqual(0, Characters.c5260_0000, npc_part_id=5262, value=0)
    AICommand(Characters.c5260_0000, command_id=1, slot=0)
    DisableNetworkSync()
    Wait(1.0)
    EnableNetworkSync()
    SkipLinesIfFlagOn(2, 11005396)
    AICommand(Characters.c5260_0000, command_id=0, slot=0)
    SkipLines(1)
    AICommand(Characters.c5260_0000, command_id=20, slot=0)
    Restart()


def Event11005000(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 11005000: Event 11005000 """
    SkipLinesIfThisEventSlotOff(2)
    DisableObject(arg_4_7)
    End()
    IfEntityWithinDistance(0, PLAYER, arg_0_3, radius=3.0)
    ForceAnimation(arg_4_7, arg_8_11, wait_for_completion=True)
    DisableObject(arg_4_7)


def Event11000100():
    """ 11000100: Event 11000100 """
    IfFlagOff(1, 11000100)
    IfActionButton(
        1,
        prompt_text=10010400,
        anchor_entity=Objects.o1319_0000,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        model_point=101,
        trigger_attribute=TriggerAttribute.All,
    )
    IfConditionTrue(0, input_condition=1)
    Move(
        PLAYER,
        destination=Objects.o1319_0000,
        destination_type=CoordEntityType.Object,
        model_point=121,
        short_move=True,
    )
    ForceAnimation(PLAYER, 7110)
    ForceAnimation(Objects.o1319_0000, 0)


def Event11000101():
    """ 11000101: Event 11000101 """
    DisableNetworkSync()
    IfFlagOff(1, 11000100)
    IfActionButton(
        1,
        prompt_text=10010400,
        anchor_entity=Objects.o1319_0000,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        model_point=100,
        trigger_attribute=TriggerAttribute.All,
    )
    IfConditionTrue(0, input_condition=1)
    DisplayDialog(
        10010161,
        anchor_entity=Objects.o1319_0000,
        display_distance=3.0,
        button_type=ButtonType.Yes_or_No,
        number_buttons=NumberButtons.NoButton,
    )
    Restart()


def Event11000110():
    """ 11000110: Event 11000110 """
    SkipLinesIfFlagOn(1, 590)
    SkipLinesIfThisEventOff(2)
    EndOfAnimation(Objects.o1309, 1)
    End()
    IfPlayerHasGood(1, 2007, including_box=False)
    IfActionButton(
        1,
        prompt_text=10010400,
        anchor_entity=Objects.o1309,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        model_point=100,
    )
    IfConditionTrue(0, input_condition=1)
    EnableFlag(11000111)
    Move(PLAYER, destination=Objects.o1309, destination_type=CoordEntityType.Object, model_point=120, short_move=True)
    ForceAnimation(PLAYER, 7120)
    ForceAnimation(Objects.o1309, 1)
    EndIfClient()
    DisplayDialog(
        10010866,
        anchor_entity=Objects.o1309,
        display_distance=3.0,
        button_type=ButtonType.OK_or_Cancel,
        number_buttons=NumberButtons.NoButton,
    )
    EnableFlag(590)


def Event11000111():
    """ 11000111: Event 11000111 """
    DisableNetworkSync()
    IfFlagOn(-1, 11000110)
    IfPlayerDoesNotHaveGood(1, 2007, including_box=False)
    IfActionButton(
        1,
        prompt_text=10010400,
        anchor_entity=Objects.o1309,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        model_point=100,
    )
    IfClient(2)
    IfActionButton(
        2,
        prompt_text=10010400,
        anchor_entity=Objects.o1309,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        model_point=100,
        trigger_attribute=TriggerAttribute.All,
    )
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EndIfFlagOn(11000110)
    DisplayDialog(
        10010163,
        anchor_entity=Objects.o1309,
        display_distance=3.0,
        button_type=ButtonType.OK_or_Cancel,
        number_buttons=NumberButtons.NoButton,
    )
    Restart()


def Event11000120(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int):
    """ 11000120: Event 11000120 """
    EndIfThisEventSlotOn()
    IfObjectActivated(0, obj_act_id=arg_0_3)
    EndIfClient()
    IfPlayerHasGood(1, arg_16_19, including_box=False)
    SkipLinesIfConditionTrue(2, 1)
    DisplayDialog(
        arg_12_15,
        anchor_entity=arg_8_11,
        display_distance=3.0,
        button_type=ButtonType.Yes_or_No,
        number_buttons=NumberButtons.NoButton,
    )
    SkipLines(1)
    DisplayDialog(
        arg_4_7,
        anchor_entity=arg_8_11,
        display_distance=3.0,
        button_type=ButtonType.Yes_or_No,
        number_buttons=NumberButtons.NoButton,
    )


@RestartOnRest
def Event11000200():
    """ 11000200: Event 11000200 """
    EndIfThisEventOn()
    DisableAI(Characters.c3270_0000)
    IfFlagOff(1, 11000200)
    IfEntityWithinDistance(1, Characters.c3270_0000, PLAYER, radius=9.0)
    IfConditionTrue(0, input_condition=1)
    ForceAnimation(Characters.c3270_0000, 500, wait_for_completion=True)
    ForceAnimation(Characters.c3270_0000, 500, wait_for_completion=True)
    ForceAnimation(Characters.c3270_0000, 500, wait_for_completion=True)
    ForceAnimation(Characters.c3270_0000, 500, wait_for_completion=True)
    ForceAnimation(Characters.c3270_0000, 500, wait_for_completion=True)
    ForceAnimation(Characters.c3270_0000, 500, wait_for_completion=True)
    ForceAnimation(Characters.c3270_0000, 500, wait_for_completion=True)
    EnableAI(Characters.c3270_0000)


@RestartOnRest
def Event11000800():
    """ 11000800: Event 11000800 """
    SkipLinesIfThisEventOff(2)
    DisableCharacter(Characters.c1202_0000)
    End()
    IfCharacterDead(0, Characters.c1202_0000)
    EnableFlag(11000800)


@RestartOnRest
def Event11005050():
    """ 11005050: Event 11005050 """
    IfEntityWithinDistance(-1, PLAYER, Characters.c2660_0000, radius=7.0)
    IfAttacked(-1, Characters.c2660_0000, attacker=PLAYER)
    IfObjectDestroyed(-1, Objects.o1002_01)
    IfHasAIStatus(-1, Characters.c3340_0002, ai_status=AIStatusType.Battle)
    IfConditionTrue(0, input_condition=-1)
    SetStandbyAnimationSettings(Characters.c2660_0000, cancel_animation=9060)


def Event11005060():
    """ 11005060: Event 11005060 """
    EndIfThisEventOn()
    CreateObjectVFX(100013, obj=Objects.o1002_01, model_point=10)
    IfObjectDestroyed(0, Objects.o1002_01)
    DeleteObjectVFX(Objects.o1002_01, erase_root=True)


@RestartOnRest
def Event11005070():
    """ 11005070: Event 11005070 """
    IfCharacterDead(7, Characters.c2660_0001)
    SkipLinesIfConditionFalse(2, 7)
    DisableCharacter(Characters.c2660_0001)
    End()
    EndIfThisEventOn()
    DisableAI(Characters.c2660_0001)
    IfCharacterInsideRegion(1, PLAYER, region=Boxes.ButcherAmbushTrigger)
    IfAttacked(2, Characters.c2660_0001, attacker=PLAYER)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionFalse(1, 1)
    ForceAnimation(Characters.c2660_0001, 500)
    EnableAI(Characters.c2660_0001)


@RestartOnRest
def Event11005100(_, arg_0_3: int, arg_4_7: int, arg_8_11: float):
    """ 11005100: Event 11005100 """
    SkipLinesIfThisEventSlotOn(6)
    DisableGravity(arg_4_7)
    DisableCharacterCollision(arg_4_7)
    IfCharacterInsideRegion(-1, PLAYER, region=arg_0_3)
    IfAttacked(-1, arg_4_7, attacker=PLAYER)
    IfConditionTrue(0, input_condition=-1)
    Wait(arg_8_11)
    EnableGravity(arg_4_7)
    EnableCharacterCollision(arg_4_7)
    ResetStandbyAnimationSettings(arg_4_7)


@RestartOnRest
def Event11005200(_, arg_0_3: int, arg_4_7: int):
    """ 11005200: Event 11005200 """
    EndIfThisEventSlotOn()
    DisableAI(arg_0_3)
    IfCharacterInsideRegion(-1, PLAYER, region=arg_4_7)
    IfAttacked(-1, arg_0_3, attacker=PLAYER)
    IfConditionTrue(0, input_condition=-1)
    EnableAI(arg_0_3)


@RestartOnRest
def Event11005150(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11005150: Event 11005150 """
    IfCharacterDead(4, arg_0_3)
    SkipLinesIfConditionTrue(2, 4)
    DisableFlag(arg_8_11)
    DisableFlag(arg_12_15)
    IfCharacterAlive(5, arg_0_3)
    SkipLinesIfConditionTrue(1, 5)
    SkipLinesIfFlagOn(1, arg_8_11)
    SkipLinesIfThisEventSlotOff(9)
    IfCharacterDead(3, arg_0_3)
    IfHost(3)
    SkipLinesIfConditionFalse(2, 3)
    DisableCharacter(arg_0_3)
    EnableFlag(arg_12_15)
    SkipLinesIfFlagOff(1, arg_12_15)
    DisableCharacter(arg_0_3)
    PostDestruction(arg_4_7)
    End()
    RestoreObject(arg_4_7)
    DisableCharacter(arg_0_3)
    IfEntityWithinDistance(1, PLAYER, arg_0_3, radius=3.0)
    IfObjectDestroyed(2, arg_4_7)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionFalse(5, 1)
    DestroyObject(arg_4_7)
    PlaySoundEffect(anchor_entity=arg_4_7, sound_type=SoundType.o_Object, sound_id=132200000)
    EnableCharacter(arg_0_3)
    ForceAnimation(arg_0_3, 3002)
    EnableFlag(arg_8_11)
    End()
    EnableCharacter(arg_0_3)
    EnableFlag(arg_8_11)


@RestartOnRest
def Event11000850(_, arg_0_3: int):
    """ 11000850: Event 11000850 """
    SkipLinesIfThisEventSlotOff(3)
    DisableCharacter(arg_0_3)
    Kill(arg_0_3, award_souls=False)
    End()
    IfCharacterDead(0, arg_0_3)
    End()


def Event11000600(_, arg_0_3: int, arg_4_7: int):
    """ 11000600: Event 11000600 """
    SkipLinesIfThisEventSlotOff(4)
    EndOfAnimation(arg_0_3, 0)
    DisableObjectActivation(arg_0_3, obj_act_id=-1)
    EnableTreasure(arg_0_3)
    End()
    DisableTreasure(arg_0_3)
    IfObjectActivated(0, obj_act_id=arg_4_7)
    WaitFrames(10)
    EnableTreasure(arg_0_3)


def Event11000510(_, arg_0_3: int, arg_4_7: int):
    """ 11000510: Event 11000510 """
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


def Event11000520(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11000520: Event 11000520 """
    SkipLinesIfThisEventSlotOff(2)
    DropMandatoryTreasure(arg_0_3)
    End()
    IfHealthLessThanOrEqual(0, arg_0_3, 0.0)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)


def Event11000530(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11000530: Event 11000530 """
    SkipLinesIfFlagOn(9, 11000580)
    IfFlagOff(1, 1253)
    IfFlagOn(1, 1250)
    IfHealthGreaterThan(1, arg_0_3, 0.0)
    IfObjectDestroyed(-1, Objects.o1155)
    IfAttacked(-1, arg_0_3, attacker=PLAYER)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)
    SkipLinesIfObjectDestroyed(1, Objects.o1155)
    DestroyObject(Objects.o1155)
    EnableGravity(arg_0_3)
    EnableCharacterCollision(arg_0_3)
    SetStandbyAnimationSettings(arg_0_3, cancel_animation=7821)
    EnableFlag(11000580)


def Event11000531(_, arg_0_3: int):
    """ 11000531: Event 11000531 """
    IfFlagOff(1, 1253)
    IfFlagOn(1, 1252)
    IfConditionTrue(0, input_condition=1)
    DisableCharacter(arg_0_3)


def Event11000532(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11000532: Event 11000532 """
    IfFlagOff(1, 1434)
    IfFlagOff(1, 1435)
    IfFlagOn(1, 1430)
    IfFlagOn(1, 11010700)
    IfFlagOn(1, 11400200)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)
    DisableCharacter(arg_0_3)


def Event11000533(_, arg_0_3: int, arg_4_7: int):
    """ 11000533: Event 11000533 """
    SkipLinesIfThisEventSlotOff(2)
    DropMandatoryTreasure(arg_0_3)
    End()
    IfHealthLessThanOrEqual(0, arg_0_3, 0.0)
    DisableFlag(1434)
    EnableFlag(arg_4_7)


def Event11000534(_, arg_0_3: int):
    """ 11000534: Event 11000534 """
    IfFlagOn(1, 1250)
    IfFlagOff(1, 1253)
    IfConditionTrue(0, input_condition=1)
    EnableInvincibility(arg_0_3)
    IfObjectDestroyed(0, Objects.o1155)
    DisableNetworkSync()
    Wait(2.0)
    DisableInvincibility(arg_0_3)


def Event11005030():
    """ 11005030: Event 11005030 """
    SkipLinesIfClient(1)
    SetNetworkUpdateAuthority(Characters.c0000_0005, UpdateAuthority.Forced)
    SkipLinesIfFlagOn(3, 11005037)
    IfClient(2)
    IfFlagOn(2, 11005032)
    SkipLinesIfConditionTrue(1, 2)
    DisableCharacter(Characters.c0000_0005)
    EndIfFlagOn(2)
    IfMultiplayerCount(1, arg1=5, arg2=2)
    IfHost(1)
    IfCharacterHuman(1, PLAYER)
    IfFlagOff(1, 11005032)
    IfFlagOff(1, 11005037)
    IfFlagOn(-1, 1004)
    IfFlagOn(-1, 1005)
    IfFlagOn(-1, 1006)
    IfFlagOn(-1, 1010)
    IfFlagOn(-1, 1011)
    IfConditionFalse(1, input_condition=-1)
    IfCharacterBackreadEnabled(1, Characters.c0000_0005)
    IfConditionTrue(0, input_condition=1)
    PlaceSummonSign(
        SummonSignType.BlueEyeSign,
        Characters.c0000_0005,
        region=Points.SolaireSummonSign,
        summon_flag=11005032,
        dismissal_flag=11005037,
    )


def Event11005029():
    """ 11005029: Event 11005029 """
    SkipLinesIfClient(1)
    SetNetworkUpdateAuthority(Characters.c0000_0005, UpdateAuthority.Forced)
    SkipLinesIfFlagOn(3, 11005037)
    IfClient(2)
    IfFlagOn(2, 11005032)
    SkipLinesIfConditionTrue(1, 2)
    DisableCharacter(Characters.c0000_0005)
    EndIfFlagOn(2)
    IfMultiplayerCount(1, arg1=4, arg2=3)
    IfHost(1)
    IfCharacterHuman(1, PLAYER)
    IfFlagOff(1, 11005032)
    IfFlagOff(1, 11005037)
    IfFlagOn(-1, 1004)
    IfFlagOn(-1, 1005)
    IfFlagOn(-1, 1006)
    IfFlagOn(-1, 1010)
    IfFlagOn(-1, 1011)
    IfConditionFalse(1, input_condition=-1)
    IfCharacterBackreadEnabled(1, Characters.c0000_0005)
    IfCharacterHasSpecialEffect(1, PLAYER, 28)
    IfConditionTrue(0, input_condition=1)
    PlaceSummonSign(
        SummonSignType.BlueEyeSign,
        Characters.c0000_0005,
        region=Points.SolaireSummonSign,
        summon_flag=11005032,
        dismissal_flag=11005037,
    )


def Event11005031():
    """ 11005031: Event 11005031 """
    EndIfThisEventOn()
    IfFlagOn(1, 11005032)
    IfFlagOn(1, 11005393)
    IfConditionTrue(0, input_condition=1)
    AICommand(Characters.c0000_0005, command_id=10, slot=0)
    ReplanAI(Characters.c0000_0005)
    IfCharacterInsideRegion(0, Characters.c0000_0005, region=Boxes.GapingDragonFogPrompt)
    RotateToFaceEntity(Characters.c0000_0005, Boxes.GapingDragonFogRotationTarget)
    ForceAnimation(Characters.c0000_0005, 7410)
    AICommand(Characters.c0000_0005, command_id=-1, slot=0)
    ReplanAI(Characters.c0000_0005)


def Event11005033():
    """ 11005033: Event 11005033 """
    SkipLinesIfClient(1)
    SetNetworkUpdateAuthority(Characters.c0000_0007, UpdateAuthority.Forced)
    SkipLinesIfFlagOn(3, 11005038)
    IfClient(2)
    IfFlagOn(2, 11005035)
    SkipLinesIfConditionTrue(1, 2)
    DisableCharacter(Characters.c0000_0007)
    EndIfFlagOn(2)
    IfMultiplayerCount(1, arg1=5, arg2=2)
    IfHost(1)
    IfCharacterHuman(1, PLAYER)
    IfFlagOn(1, 11020607)
    IfFlagOff(1, 11005035)
    IfFlagOff(1, 11005038)
    IfFlagOn(-1, 1572)
    IfFlagOn(-1, 1573)
    IfConditionTrue(1, input_condition=-1)
    IfFlagOff(1, 1574)
    IfCharacterBackreadEnabled(1, Characters.c0000_0007)
    IfConditionTrue(0, input_condition=1)
    PlaceSummonSign(
        SummonSignType.BlueEyeSign,
        Characters.c0000_0007,
        region=Points.LautrecSummonSign,
        summon_flag=11005035,
        dismissal_flag=11005038,
    )


def Event11005333():
    """ 11005333: Event 11005333 """
    IfFlagOn(0, 11005035)
    AddSpecialEffect(Characters.c0000_0007, 5450)


def Event11005990(_, arg_0_3: int, arg_4_7: int):
    """ 11005990: Event 11005990 """
    IfFlagOn(0, arg_0_3)
    EraseNPCSummonSign(summoned_character=arg_4_7)
    IfFlagOff(0, arg_0_3)
    Restart()


def Event11005036():
    """ 11005036: Event 11005036 """
    SkipLinesIfClient(1)
    SetNetworkUpdateAuthority(Characters.c0000_0007, UpdateAuthority.Forced)
    SkipLinesIfFlagOn(3, 11005038)
    IfClient(2)
    IfFlagOn(2, 11005035)
    SkipLinesIfConditionTrue(1, 2)
    DisableCharacter(Characters.c0000_0007)
    EndIfFlagOn(2)
    IfMultiplayerCount(1, arg1=4, arg2=3)
    IfHost(1)
    IfCharacterHuman(1, PLAYER)
    IfFlagOff(1, 11005035)
    IfFlagOff(1, 11005038)
    IfFlagOn(1, 11020607)
    IfFlagOn(-1, 1572)
    IfFlagOn(-1, 1573)
    IfConditionTrue(1, input_condition=-1)
    IfFlagOff(1, 1574)
    IfCharacterBackreadEnabled(1, Characters.c0000_0007)
    IfCharacterHasSpecialEffect(1, PLAYER, 28)
    IfConditionTrue(0, input_condition=1)
    PlaceSummonSign(
        SummonSignType.BlueEyeSign,
        Characters.c0000_0007,
        region=Points.LautrecSummonSign,
        summon_flag=11005035,
        dismissal_flag=11005038,
    )


def Event11005034():
    """ 11005034: Event 11005034 """
    EndIfThisEventOn()
    IfFlagOn(1, 11005035)
    IfFlagOn(1, 11005393)
    IfConditionTrue(0, input_condition=1)
    AICommand(Characters.c0000_0007, command_id=10, slot=0)
    ReplanAI(Characters.c0000_0007)
    IfCharacterInsideRegion(0, Characters.c0000_0007, region=Boxes.GapingDragonFogPrompt)
    RotateToFaceEntity(Characters.c0000_0007, Boxes.GapingDragonFogRotationTarget)
    ForceAnimation(Characters.c0000_0007, 7410)
    AICommand(Characters.c0000_0007, command_id=-1, slot=0)
    ReplanAI(Characters.c0000_0007)


def Event11005039():
    """ 11005039: Event 11005039 """
    DisableNetworkSync()
    EndIfClient()
    EndIfFlagOn(11005040)
    EndIfFlagOn(2)
    IfHost(1)
    IfCharacterHuman(1, PLAYER)
    IfFlagOff(1, 11000810)
    SkipLinesIfThisEventOn(1)
    IfCharacterInsideRegion(1, PLAYER, region=Boxes.KirkInvaderTrigger)
    IfConditionTrue(0, input_condition=1)
    PlaceSummonSign(
        SummonSignType.BlackEyeSign,
        Characters.c0000_0006,
        region=Points.KirkInvaderSpawn,
        summon_flag=11005040,
        dismissal_flag=11005041,
    )
    Wait(20.0)
    Restart()


def Event11000810():
    """ 11000810: Event 11000810 """
    SkipLinesIfHost(3)
    IfFlagOn(1, 11005040)
    IfFlagOff(1, 11005041)
    SkipLinesIfConditionTrue(1, 1)
    DisableCharacter(Characters.c0000_0006)
    EndIfThisEventOn()
    IfCharacterDead(0, Characters.c0000_0006)
    EnableFlag(11000810)


def Event11005843(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11005843: Event 11005843 """
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


def Event11005844(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 11005844: Event 11005844 """
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
    """ 11002000: Patches teleports behind the player and attacks. """
    DisableCharacter(Characters.c0000_PatchesAmbush)

    Await(InsideMap(DEPTHS) and TriggerFlags.PatchesAmbush and IsAlive(Characters.c0000_PatchesAmbush))
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
    """ 11002001: Channeler teleports above the player (no gravity) and uses its buff dance. """
    DisableCharacter(Characters.c2370_TrollChanneler)

    Await(InsideMap(DEPTHS) and TriggerFlags.ChannelerAmbush and IsAlive(Characters.c2370_TrollChanneler))
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

    AddSpecialEffect(6130, 5470)
    AddSpecialEffect(6260, 5470)
    AddSpecialEffect(6541, 5470)
    AddSpecialEffect(6562, 5470)
    AddSpecialEffect(6591, 5470)
    AddSpecialEffect(1000960, 5470)
    AddSpecialEffect(1000201, 5470)
    AddSpecialEffect(1000202, 5470)
    AddSpecialEffect(1000203, 5470)
    AddSpecialEffect(1000204, 5470)
    AddSpecialEffect(1000205, 5470)
    AddSpecialEffect(1000206, 5470)
    AddSpecialEffect(1000150, 5470)
    AddSpecialEffect(1000151, 5470)
    AddSpecialEffect(1000152, 5470)
    AddSpecialEffect(1000207, 5470)
    AddSpecialEffect(1000208, 5470)
    AddSpecialEffect(1000209, 5470)
    AddSpecialEffect(1000211, 5470)
    AddSpecialEffect(1000212, 5470)
    AddSpecialEffect(1000213, 5470)
    AddSpecialEffect(1000214, 5470)
    AddSpecialEffect(1000215, 5470)
    AddSpecialEffect(1000216, 5470)
    AddSpecialEffect(1000217, 5470)
    AddSpecialEffect(1000218, 5470)
    AddSpecialEffect(1000219, 5470)
    AddSpecialEffect(1000220, 5470)
    AddSpecialEffect(1000221, 5470)
    AddSpecialEffect(1000222, 5470)
    AddSpecialEffect(1000906, 5470)
    AddSpecialEffect(1000907, 5470)
    AddSpecialEffect(1000908, 5470)
    AddSpecialEffect(1000909, 5470)
    AddSpecialEffect(1000910, 5470)
    AddSpecialEffect(1000911, 5470)
    AddSpecialEffect(1000912, 5470)
    AddSpecialEffect(1000913, 5470)
    AddSpecialEffect(1000500, 5470)
    AddSpecialEffect(1000300, 5470)
    AddSpecialEffect(1000223, 5470)
    AddSpecialEffect(1000224, 5470)
    AddSpecialEffect(1000225, 5470)
    AddSpecialEffect(1000120, 5470)
    AddSpecialEffect(1000121, 5470)
    AddSpecialEffect(1000122, 5470)
    AddSpecialEffect(1000123, 5470)
    AddSpecialEffect(1000124, 5470)
    AddSpecialEffect(1000125, 5470)
    AddSpecialEffect(1000126, 5470)
    AddSpecialEffect(1000226, 5470)
    AddSpecialEffect(1000227, 5470)
    AddSpecialEffect(1000900, 5470)
    AddSpecialEffect(1000901, 5470)
    AddSpecialEffect(1000902, 5470)
    AddSpecialEffect(1000903, 5470)
    AddSpecialEffect(1000904, 5470)
    AddSpecialEffect(1000099, 5470)
    AddSpecialEffect(1000090, 5470)
    AddSpecialEffect(1000905, 5470)
    AddSpecialEffect(1000100, 5470)
    AddSpecialEffect(1000101, 5470)
    AddSpecialEffect(1000102, 5470)
    AddSpecialEffect(1000103, 5470)
    AddSpecialEffect(1000104, 5470)
    AddSpecialEffect(1000105, 5470)
    AddSpecialEffect(1000106, 5470)
    AddSpecialEffect(1000107, 5470)
    AddSpecialEffect(1000228, 5470)
    AddSpecialEffect(1000229, 5470)
    AddSpecialEffect(1000230, 5470)
    AddSpecialEffect(1000200, 5470)
    AddSpecialEffect(1000231, 5470)
    AddSpecialEffect(1000232, 5470)
    AddSpecialEffect(1000233, 5470)
    AddSpecialEffect(1000234, 5470)
    AddSpecialEffect(1000235, 5470)
    AddSpecialEffect(1000210, 5470)
    AddSpecialEffect(1000236, 5470)
    AddSpecialEffect(1000237, 5470)
    AddSpecialEffect(1000238, 5470)
    AddSpecialEffect(1000111, 5470)
    AddSpecialEffect(1000112, 5470)
    AddSpecialEffect(1000110, 5470)
    AddSpecialEffect(1000113, 5470)
    AddSpecialEffect(1003900, 5470)
    AddSpecialEffect(1003910, 5470)
    AddSpecialEffect(1003901, 5470)
    AddSpecialEffect(1003911, 5470)
    AddSpecialEffect(1003902, 5470)
    AddSpecialEffect(1003912, 5470)
    AddSpecialEffect(1000800, 5470)
    AddSpecialEffect(1000801, 5470)

    return RESTART


@RestartOnRest
def RedPhantomAmbush():
    """ 11002002: Random red phantom ambushes the player. """
    DisableCharacter(Characters.c2500_0012)
    DisableCharacter(Characters.c2500_0013)
    DisableCharacter(Characters.c2500_0014)
    DisableCharacter(Characters.c2500_0015)
    DisableCharacter(Characters.c2500_0016)
    DisableCharacter(Characters.c2660_0002)
    DisableCharacter(Characters.c1201_0018)
    DisableCharacter(Characters.c1201_0019)
    DisableCharacter(Characters.c1201_0020)
    DisableCharacter(Characters.c1201_0021)
    DisableCharacter(Characters.c1201_0022)
    DisableCharacter(Characters.c1201_0023)
    DisableCharacter(Characters.c1201_0024)
    DisableCharacter(Characters.c1201_0025)

    Await(InsideMap(DEPTHS) and TriggerFlags.EnemyAmbush)
    DisableFlag(TriggerFlags.EnemyAmbush)

    DisableFlagRange((11812900, 11812999))
    EnableRandomFlagInRange((11812900, 11812913))

    if FlagEnabled(11812900):
        ControlRedPhantom(0, Characters.c2500_0012)
    elif FlagEnabled(11812901):
        ControlRedPhantom(0, Characters.c2500_0013)
    elif FlagEnabled(11812902):
        ControlRedPhantom(0, Characters.c2500_0014)
    elif FlagEnabled(11812903):
        ControlRedPhantom(0, Characters.c2500_0015)
    elif FlagEnabled(11812904):
        ControlRedPhantom(0, Characters.c2500_0016)
    elif FlagEnabled(11812905):
        ControlRedPhantom(0, Characters.c2660_0002)
    elif FlagEnabled(11812906):
        ControlRedPhantom(0, Characters.c1201_0018)
    elif FlagEnabled(11812907):
        ControlRedPhantom(0, Characters.c1201_0019)
    elif FlagEnabled(11812908):
        ControlRedPhantom(0, Characters.c1201_0020)
    elif FlagEnabled(11812909):
        ControlRedPhantom(0, Characters.c1201_0021)
    elif FlagEnabled(11812910):
        ControlRedPhantom(0, Characters.c1201_0022)
    elif FlagEnabled(11812911):
        ControlRedPhantom(0, Characters.c1201_0023)
    elif FlagEnabled(11812912):
        ControlRedPhantom(0, Characters.c1201_0024)
    elif FlagEnabled(11812913):
        ControlRedPhantom(0, Characters.c1201_0025)
    
    Await(FlagEnabled(11005082))

    return RESTART


@RestartOnRest
def ControlRedPhantom(_, enemy: int):
    """ 11005081: `enemy` moves to player and appears. """
    DisableFlag(11005082)
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
    EnableFlag(11005082)


def MakeWorldInvisible():
    """ 11002003: Disable all map pieces. Undone only by reload. """
    Await(TriggerFlags.InvisibleWorld)   # note you don't need to be standing in the map
    DisableFlag(TriggerFlags.InvisibleWorld)
    for map_piece in range(1008500, 1008569):
        DisableMapPiece(map_piece)
    # No need to restart.


@RestartOnRest
def OopsAllGwyns():
    """ 11002004: Enable Gwyns and warp them to their paired normal characters. """
    DisableCharacter(1000600)
    DisableCharacter(1000601)
    DisableCharacter(1000602)
    DisableCharacter(1000603)
    DisableCharacter(1000604)
    DisableCharacter(1000605)
    DisableCharacter(1000606)
    DisableCharacter(1000607)
    DisableCharacter(1000608)
    DisableCharacter(1000609)
    DisableCharacter(1000610)
    DisableCharacter(1000611)
    DisableCharacter(1000612)
    Await(TriggerFlags.OopsAllGwyns)  # note you don't need to be standing in the map
    DisableCharacter(6130)
    EnableCharacter(1000600)
    DisableCharacter(1000205)
    EnableCharacter(1000601)
    DisableCharacter(1000207)
    EnableCharacter(1000602)
    DisableCharacter(1000213)
    EnableCharacter(1000603)
    DisableCharacter(1000218)
    EnableCharacter(1000604)
    DisableCharacter(1000223)
    EnableCharacter(1000605)
    DisableCharacter(1000122)
    EnableCharacter(1000606)
    DisableCharacter(1000226)
    EnableCharacter(1000607)
    DisableCharacter(1000100)
    EnableCharacter(1000608)
    DisableCharacter(1000105)
    EnableCharacter(1000609)
    DisableCharacter(1000230)
    EnableCharacter(1000610)
    DisableCharacter(1000234)
    EnableCharacter(1000611)
    DisableCharacter(1000238)
    EnableCharacter(1000612)
    WaitFrames(30)  # enough time for other maps to trigger too
    DisableFlag(TriggerFlags.OopsAllGwyns)
    # No need to restart.


@RestartOnRest
def OopsAllBonewheels():
    """ 11002005: Enable Bonewheels and warp them to their paired normal characters. """
    DisableCharacter(1000400)
    DisableCharacter(1000401)
    DisableCharacter(1000402)
    DisableCharacter(1000403)
    DisableCharacter(1000404)
    DisableCharacter(1000405)
    DisableCharacter(1000406)
    DisableCharacter(1000407)
    DisableCharacter(1000408)
    DisableCharacter(1000409)
    DisableCharacter(1000410)
    DisableCharacter(1000411)
    DisableCharacter(1000412)
    DisableCharacter(1000413)
    DisableCharacter(1000414)
    DisableCharacter(1000415)
    DisableCharacter(1000416)
    DisableCharacter(1000417)
    DisableCharacter(1000418)
    DisableCharacter(1000419)
    DisableCharacter(1000420)
    DisableCharacter(1000421)
    DisableCharacter(1000422)
    DisableCharacter(1000423)
    DisableCharacter(1000424)
    DisableCharacter(1000425)
    DisableCharacter(1000426)
    DisableCharacter(1000427)
    DisableCharacter(1000428)
    DisableCharacter(1000429)
    DisableCharacter(1000430)
    DisableCharacter(1000431)
    DisableCharacter(1000432)
    DisableCharacter(1000433)
    DisableCharacter(1000434)
    DisableCharacter(1000435)
    DisableCharacter(1000436)
    DisableCharacter(1000437)
    DisableCharacter(1000438)
    DisableCharacter(1000439)
    DisableCharacter(1000440)
    DisableCharacter(1000441)
    DisableCharacter(1000442)
    DisableCharacter(1000443)
    DisableCharacter(1000444)
    DisableCharacter(1000445)
    DisableCharacter(1000446)
    DisableCharacter(1000447)
    DisableCharacter(1000448)
    DisableCharacter(1000449)
    DisableCharacter(1000450)
    DisableCharacter(1000451)
    DisableCharacter(1000452)
    DisableCharacter(1000453)
    DisableCharacter(1000454)
    DisableCharacter(1000455)
    DisableCharacter(1000456)
    DisableCharacter(1000457)
    DisableCharacter(1000458)
    DisableCharacter(1000459)
    DisableCharacter(1000460)
    DisableCharacter(1000461)
    DisableCharacter(1000462)
    DisableCharacter(1000463)
    DisableCharacter(1000464)
    DisableCharacter(1000465)
    DisableCharacter(1000466)
    DisableCharacter(1000467)
    DisableCharacter(1000468)
    DisableCharacter(1000469)
    DisableCharacter(1000470)
    Await(TriggerFlags.OopsAllBonewheels)  # note you don't need to be standing in the map
    DisableCharacter(6130)
    EnableCharacter(1000400)
    DisableCharacter(6260)
    EnableCharacter(1000401)
    DisableCharacter(6541)
    EnableCharacter(1000402)
    DisableCharacter(6562)
    EnableCharacter(1000403)
    DisableCharacter(6591)
    EnableCharacter(1000404)
    DisableCharacter(1000201)
    EnableCharacter(1000405)
    DisableCharacter(1000202)
    EnableCharacter(1000406)
    DisableCharacter(1000203)
    EnableCharacter(1000407)
    DisableCharacter(1000204)
    EnableCharacter(1000408)
    DisableCharacter(1000205)
    EnableCharacter(1000409)
    DisableCharacter(1000206)
    EnableCharacter(1000410)
    DisableCharacter(1000150)
    EnableCharacter(1000411)
    DisableCharacter(1000151)
    EnableCharacter(1000412)
    DisableCharacter(1000152)
    EnableCharacter(1000413)
    DisableCharacter(1000207)
    EnableCharacter(1000414)
    DisableCharacter(1000208)
    EnableCharacter(1000415)
    DisableCharacter(1000209)
    EnableCharacter(1000416)
    DisableCharacter(1000211)
    EnableCharacter(1000417)
    DisableCharacter(1000212)
    EnableCharacter(1000418)
    DisableCharacter(1000213)
    EnableCharacter(1000419)
    DisableCharacter(1000214)
    EnableCharacter(1000420)
    DisableCharacter(1000215)
    EnableCharacter(1000421)
    DisableCharacter(1000216)
    EnableCharacter(1000422)
    DisableCharacter(1000217)
    EnableCharacter(1000423)
    DisableCharacter(1000218)
    EnableCharacter(1000424)
    DisableCharacter(1000219)
    EnableCharacter(1000425)
    DisableCharacter(1000220)
    EnableCharacter(1000426)
    DisableCharacter(1000221)
    EnableCharacter(1000427)
    DisableCharacter(1000222)
    EnableCharacter(1000428)
    DisableCharacter(1000500)
    EnableCharacter(1000429)
    DisableCharacter(1000300)
    EnableCharacter(1000430)
    DisableCharacter(1000223)
    EnableCharacter(1000431)
    DisableCharacter(1000224)
    EnableCharacter(1000432)
    DisableCharacter(1000225)
    EnableCharacter(1000433)
    DisableCharacter(1000120)
    EnableCharacter(1000434)
    DisableCharacter(1000121)
    EnableCharacter(1000435)
    DisableCharacter(1000122)
    EnableCharacter(1000436)
    DisableCharacter(1000123)
    EnableCharacter(1000437)
    DisableCharacter(1000124)
    EnableCharacter(1000438)
    DisableCharacter(1000125)
    EnableCharacter(1000439)
    DisableCharacter(1000126)
    EnableCharacter(1000440)
    DisableCharacter(1000226)
    EnableCharacter(1000441)
    DisableCharacter(1000227)
    EnableCharacter(1000442)
    DisableCharacter(1000099)
    EnableCharacter(1000443)
    DisableCharacter(1000090)
    EnableCharacter(1000444)
    DisableCharacter(1000100)
    EnableCharacter(1000445)
    DisableCharacter(1000101)
    EnableCharacter(1000446)
    DisableCharacter(1000102)
    EnableCharacter(1000447)
    DisableCharacter(1000103)
    EnableCharacter(1000448)
    DisableCharacter(1000104)
    EnableCharacter(1000449)
    DisableCharacter(1000105)
    EnableCharacter(1000450)
    DisableCharacter(1000106)
    EnableCharacter(1000451)
    DisableCharacter(1000107)
    EnableCharacter(1000452)
    DisableCharacter(1000228)
    EnableCharacter(1000453)
    DisableCharacter(1000229)
    EnableCharacter(1000454)
    DisableCharacter(1000230)
    EnableCharacter(1000455)
    DisableCharacter(1000200)
    EnableCharacter(1000456)
    DisableCharacter(1000231)
    EnableCharacter(1000457)
    DisableCharacter(1000232)
    EnableCharacter(1000458)
    DisableCharacter(1000233)
    EnableCharacter(1000459)
    DisableCharacter(1000234)
    EnableCharacter(1000460)
    DisableCharacter(1000235)
    EnableCharacter(1000461)
    DisableCharacter(1000210)
    EnableCharacter(1000462)
    DisableCharacter(1000236)
    EnableCharacter(1000463)
    DisableCharacter(1000237)
    EnableCharacter(1000464)
    DisableCharacter(1000238)
    EnableCharacter(1000465)
    DisableCharacter(1000111)
    EnableCharacter(1000466)
    DisableCharacter(1000112)
    EnableCharacter(1000467)
    DisableCharacter(1000110)
    EnableCharacter(1000468)
    DisableCharacter(1000113)
    EnableCharacter(1000469)
    DisableCharacter(1000801)
    EnableCharacter(1000470)
    WaitFrames(30)  # enough time for other maps to trigger too
    DisableFlag(TriggerFlags.OopsAllBonewheels)
    # No need to restart.


@RestartOnRest
def HyperAggression():
    """ 11002006: Switch AI param of every enemy to its aggressive version. """
    Await(TriggerFlags.HyperAggression or TriggerFlags.HyperAggressionReTrigger)
    
    SetAIParamID(1000201, 120050)
    SetAIParamID(1000202, 120050)
    SetAIParamID(1000203, 120050)
    SetAIParamID(1000204, 120060)
    SetAIParamID(1000205, 120060)
    SetAIParamID(1000206, 120060)
    SetAIParamID(1000150, 120150)
    SetAIParamID(1000151, 120150)
    SetAIParamID(1000152, 120150)
    SetAIParamID(1000207, 120150)
    SetAIParamID(1000208, 120150)
    SetAIParamID(1000209, 120150)
    SetAIParamID(1000211, 120150)
    SetAIParamID(1000212, 120150)
    SetAIParamID(1000213, 120150)
    SetAIParamID(1000214, 120150)
    SetAIParamID(1000215, 120150)
    SetAIParamID(1000216, 120150)
    SetAIParamID(1000217, 120150)
    SetAIParamID(1000218, 120150)
    SetAIParamID(1000219, 120150)
    SetAIParamID(1000220, 120150)
    SetAIParamID(1000221, 120150)
    SetAIParamID(1000222, 120150)
    SetAIParamID(1000906, 120151)
    SetAIParamID(1000907, 120151)
    SetAIParamID(1000908, 120151)
    SetAIParamID(1000909, 120151)
    SetAIParamID(1000910, 120151)
    SetAIParamID(1000911, 120151)
    SetAIParamID(1000912, 120151)
    SetAIParamID(1000913, 120151)
    SetAIParamID(1000500, 120250)
    SetAIParamID(1000300, 237052)
    SetAIParamID(1000223, 250080)
    SetAIParamID(1000224, 250051)
    SetAIParamID(1000225, 250051)
    SetAIParamID(1000120, 250062)
    SetAIParamID(1000121, 250062)
    SetAIParamID(1000122, 250061)
    SetAIParamID(1000123, 250052)
    SetAIParamID(1000124, 250052)
    SetAIParamID(1000125, 250052)
    SetAIParamID(1000126, 250052)
    SetAIParamID(1000226, 250061)
    SetAIParamID(1000227, 250063)
    SetAIParamID(1000900, 250062)
    SetAIParamID(1000901, 250062)
    SetAIParamID(1000902, 250061)
    SetAIParamID(1000903, 250061)
    SetAIParamID(1000904, 250063)
    SetAIParamID(1000099, 266050)
    SetAIParamID(1000090, 266050)
    SetAIParamID(1000905, 266050)
    SetAIParamID(1000100, 320050)
    SetAIParamID(1000101, 320050)
    SetAIParamID(1000102, 320050)
    SetAIParamID(1000103, 320050)
    SetAIParamID(1000104, 320050)
    SetAIParamID(1000105, 320050)
    SetAIParamID(1000106, 320050)
    SetAIParamID(1000107, 320050)
    SetAIParamID(1000228, 320050)
    SetAIParamID(1000229, 320050)
    SetAIParamID(1000230, 320050)
    SetAIParamID(1000200, 327050)
    SetAIParamID(1000231, 327050)
    SetAIParamID(1000232, 327051)
    SetAIParamID(1000233, 327051)
    SetAIParamID(1000234, 327051)
    SetAIParamID(1000235, 327050)
    SetAIParamID(1000210, 327051)
    SetAIParamID(1000236, 327051)
    SetAIParamID(1000237, 327050)
    SetAIParamID(1000238, 327050)
    SetAIParamID(1000111, 334061)
    SetAIParamID(1000112, 334061)
    SetAIParamID(1000110, 334061)
    SetAIParamID(1000113, 334061)
    SetAIParamID(1003900, 349050)
    SetAIParamID(1003910, 349050)
    SetAIParamID(1003901, 349150)
    SetAIParamID(1003911, 349150)
    SetAIParamID(1003902, 349150)
    SetAIParamID(1003912, 349150)
    SetAIParamID(1000800, 526050)
    SetAIParamID(1000600, 537050)
    SetAIParamID(1000601, 537050)
    SetAIParamID(1000602, 537050)
    SetAIParamID(1000603, 537050)
    SetAIParamID(1000604, 537050)
    SetAIParamID(1000605, 537050)
    SetAIParamID(1000606, 537050)
    SetAIParamID(1000607, 537050)
    SetAIParamID(1000608, 537050)
    SetAIParamID(1000609, 537050)
    SetAIParamID(1000610, 537050)
    SetAIParamID(1000611, 537050)
    SetAIParamID(1000612, 537050)
    SetAIParamID(1000400, 293050)
    SetAIParamID(1000401, 293050)
    SetAIParamID(1000402, 293050)
    SetAIParamID(1000403, 293050)
    SetAIParamID(1000404, 293050)
    SetAIParamID(1000405, 293050)
    SetAIParamID(1000406, 293050)
    SetAIParamID(1000407, 293050)
    SetAIParamID(1000408, 293050)
    SetAIParamID(1000409, 293050)
    SetAIParamID(1000410, 293050)
    SetAIParamID(1000411, 293050)
    SetAIParamID(1000412, 293050)
    SetAIParamID(1000413, 293050)
    SetAIParamID(1000414, 293050)
    SetAIParamID(1000415, 293050)
    SetAIParamID(1000416, 293050)
    SetAIParamID(1000417, 293050)
    SetAIParamID(1000418, 293050)
    SetAIParamID(1000419, 293050)
    SetAIParamID(1000420, 293050)
    SetAIParamID(1000421, 293050)
    SetAIParamID(1000422, 293050)
    SetAIParamID(1000423, 293050)
    SetAIParamID(1000424, 293050)
    SetAIParamID(1000425, 293050)
    SetAIParamID(1000426, 293050)
    SetAIParamID(1000427, 293050)
    SetAIParamID(1000428, 293050)
    SetAIParamID(1000429, 293050)
    SetAIParamID(1000430, 293050)
    SetAIParamID(1000431, 293050)
    SetAIParamID(1000432, 293050)
    SetAIParamID(1000433, 293050)
    SetAIParamID(1000434, 293050)
    SetAIParamID(1000435, 293050)
    SetAIParamID(1000436, 293050)
    SetAIParamID(1000437, 293050)
    SetAIParamID(1000438, 293050)
    SetAIParamID(1000439, 293050)
    SetAIParamID(1000440, 293050)
    SetAIParamID(1000441, 293050)
    SetAIParamID(1000442, 293050)
    SetAIParamID(1000443, 293050)
    SetAIParamID(1000444, 293050)
    SetAIParamID(1000445, 293050)
    SetAIParamID(1000446, 293050)
    SetAIParamID(1000447, 293050)
    SetAIParamID(1000448, 293050)
    SetAIParamID(1000449, 293050)
    SetAIParamID(1000450, 293050)
    SetAIParamID(1000451, 293050)
    SetAIParamID(1000452, 293050)
    SetAIParamID(1000453, 293050)
    SetAIParamID(1000454, 293050)
    SetAIParamID(1000455, 293050)
    SetAIParamID(1000456, 293050)
    SetAIParamID(1000457, 293050)
    SetAIParamID(1000458, 293050)
    SetAIParamID(1000459, 293050)
    SetAIParamID(1000460, 293050)
    SetAIParamID(1000461, 293050)
    SetAIParamID(1000462, 293050)
    SetAIParamID(1000463, 293050)
    SetAIParamID(1000464, 293050)
    SetAIParamID(1000465, 293050)
    SetAIParamID(1000466, 293050)
    SetAIParamID(1000467, 293050)
    SetAIParamID(1000468, 293050)
    SetAIParamID(1000469, 293050)
    SetAIParamID(1000470, 293050)
        
    # Common EMEVD manages the flags that control this event.
    Await(not TriggerFlags.HyperAggressionReTrigger)
    
    SetAIParamID(1000201, 120000)
    SetAIParamID(1000202, 120000)
    SetAIParamID(1000203, 120000)
    SetAIParamID(1000204, 120010)
    SetAIParamID(1000205, 120010)
    SetAIParamID(1000206, 120010)
    SetAIParamID(1000150, 120100)
    SetAIParamID(1000151, 120100)
    SetAIParamID(1000152, 120100)
    SetAIParamID(1000207, 120100)
    SetAIParamID(1000208, 120100)
    SetAIParamID(1000209, 120100)
    SetAIParamID(1000211, 120100)
    SetAIParamID(1000212, 120100)
    SetAIParamID(1000213, 120100)
    SetAIParamID(1000214, 120100)
    SetAIParamID(1000215, 120100)
    SetAIParamID(1000216, 120100)
    SetAIParamID(1000217, 120100)
    SetAIParamID(1000218, 120100)
    SetAIParamID(1000219, 120100)
    SetAIParamID(1000220, 120100)
    SetAIParamID(1000221, 120100)
    SetAIParamID(1000222, 120100)
    SetAIParamID(1000906, 120101)
    SetAIParamID(1000907, 120101)
    SetAIParamID(1000908, 120101)
    SetAIParamID(1000909, 120101)
    SetAIParamID(1000910, 120101)
    SetAIParamID(1000911, 120101)
    SetAIParamID(1000912, 120101)
    SetAIParamID(1000913, 120101)
    SetAIParamID(1000500, 120200)
    SetAIParamID(1000300, 237002)
    SetAIParamID(1000223, 250030)
    SetAIParamID(1000224, 250001)
    SetAIParamID(1000225, 250001)
    SetAIParamID(1000120, 250012)
    SetAIParamID(1000121, 250012)
    SetAIParamID(1000122, 250011)
    SetAIParamID(1000123, 250002)
    SetAIParamID(1000124, 250002)
    SetAIParamID(1000125, 250002)
    SetAIParamID(1000126, 250002)
    SetAIParamID(1000226, 250011)
    SetAIParamID(1000227, 250013)
    SetAIParamID(1000900, 250012)
    SetAIParamID(1000901, 250012)
    SetAIParamID(1000902, 250011)
    SetAIParamID(1000903, 250011)
    SetAIParamID(1000904, 250013)
    SetAIParamID(1000099, 266000)
    SetAIParamID(1000090, 266000)
    SetAIParamID(1000905, 266000)
    SetAIParamID(1000100, 320000)
    SetAIParamID(1000101, 320000)
    SetAIParamID(1000102, 320000)
    SetAIParamID(1000103, 320000)
    SetAIParamID(1000104, 320000)
    SetAIParamID(1000105, 320000)
    SetAIParamID(1000106, 320000)
    SetAIParamID(1000107, 320000)
    SetAIParamID(1000228, 320000)
    SetAIParamID(1000229, 320000)
    SetAIParamID(1000230, 320000)
    SetAIParamID(1000200, 327000)
    SetAIParamID(1000231, 327000)
    SetAIParamID(1000232, 327001)
    SetAIParamID(1000233, 327001)
    SetAIParamID(1000234, 327001)
    SetAIParamID(1000235, 327000)
    SetAIParamID(1000210, 327001)
    SetAIParamID(1000236, 327001)
    SetAIParamID(1000237, 327000)
    SetAIParamID(1000238, 327000)
    SetAIParamID(1000111, 334011)
    SetAIParamID(1000112, 334011)
    SetAIParamID(1000110, 334011)
    SetAIParamID(1000113, 334011)
    SetAIParamID(1003900, 349000)
    SetAIParamID(1003910, 349000)
    SetAIParamID(1003901, 349100)
    SetAIParamID(1003911, 349100)
    SetAIParamID(1003902, 349100)
    SetAIParamID(1003912, 349100)
    SetAIParamID(1000800, 526000)
    SetAIParamID(1000600, 537000)
    SetAIParamID(1000601, 537000)
    SetAIParamID(1000602, 537000)
    SetAIParamID(1000603, 537000)
    SetAIParamID(1000604, 537000)
    SetAIParamID(1000605, 537000)
    SetAIParamID(1000606, 537000)
    SetAIParamID(1000607, 537000)
    SetAIParamID(1000608, 537000)
    SetAIParamID(1000609, 537000)
    SetAIParamID(1000610, 537000)
    SetAIParamID(1000611, 537000)
    SetAIParamID(1000612, 537000)
    SetAIParamID(1000400, 293000)
    SetAIParamID(1000401, 293000)
    SetAIParamID(1000402, 293000)
    SetAIParamID(1000403, 293000)
    SetAIParamID(1000404, 293000)
    SetAIParamID(1000405, 293000)
    SetAIParamID(1000406, 293000)
    SetAIParamID(1000407, 293000)
    SetAIParamID(1000408, 293000)
    SetAIParamID(1000409, 293000)
    SetAIParamID(1000410, 293000)
    SetAIParamID(1000411, 293000)
    SetAIParamID(1000412, 293000)
    SetAIParamID(1000413, 293000)
    SetAIParamID(1000414, 293000)
    SetAIParamID(1000415, 293000)
    SetAIParamID(1000416, 293000)
    SetAIParamID(1000417, 293000)
    SetAIParamID(1000418, 293000)
    SetAIParamID(1000419, 293000)
    SetAIParamID(1000420, 293000)
    SetAIParamID(1000421, 293000)
    SetAIParamID(1000422, 293000)
    SetAIParamID(1000423, 293000)
    SetAIParamID(1000424, 293000)
    SetAIParamID(1000425, 293000)
    SetAIParamID(1000426, 293000)
    SetAIParamID(1000427, 293000)
    SetAIParamID(1000428, 293000)
    SetAIParamID(1000429, 293000)
    SetAIParamID(1000430, 293000)
    SetAIParamID(1000431, 293000)
    SetAIParamID(1000432, 293000)
    SetAIParamID(1000433, 293000)
    SetAIParamID(1000434, 293000)
    SetAIParamID(1000435, 293000)
    SetAIParamID(1000436, 293000)
    SetAIParamID(1000437, 293000)
    SetAIParamID(1000438, 293000)
    SetAIParamID(1000439, 293000)
    SetAIParamID(1000440, 293000)
    SetAIParamID(1000441, 293000)
    SetAIParamID(1000442, 293000)
    SetAIParamID(1000443, 293000)
    SetAIParamID(1000444, 293000)
    SetAIParamID(1000445, 293000)
    SetAIParamID(1000446, 293000)
    SetAIParamID(1000447, 293000)
    SetAIParamID(1000448, 293000)
    SetAIParamID(1000449, 293000)
    SetAIParamID(1000450, 293000)
    SetAIParamID(1000451, 293000)
    SetAIParamID(1000452, 293000)
    SetAIParamID(1000453, 293000)
    SetAIParamID(1000454, 293000)
    SetAIParamID(1000455, 293000)
    SetAIParamID(1000456, 293000)
    SetAIParamID(1000457, 293000)
    SetAIParamID(1000458, 293000)
    SetAIParamID(1000459, 293000)
    SetAIParamID(1000460, 293000)
    SetAIParamID(1000461, 293000)
    SetAIParamID(1000462, 293000)
    SetAIParamID(1000463, 293000)
    SetAIParamID(1000464, 293000)
    SetAIParamID(1000465, 293000)
    SetAIParamID(1000466, 293000)
    SetAIParamID(1000467, 293000)
    SetAIParamID(1000468, 293000)
    SetAIParamID(1000469, 293000)
    SetAIParamID(1000470, 293000)
    
    return RESTART


@RestartOnRest
def EnemySpeedUp():
    """ 11002200: Temporary enemy effect. """
    Await(TriggerFlags.EnemySpeedUp)
    AddSpecialEffect(6130, 200000)
    AddSpecialEffect(6260, 200000)
    AddSpecialEffect(6541, 200000)
    AddSpecialEffect(6562, 200000)
    AddSpecialEffect(6591, 200000)
    AddSpecialEffect(1000960, 200000)
    AddSpecialEffect(1000201, 200000)
    AddSpecialEffect(1000202, 200000)
    AddSpecialEffect(1000203, 200000)
    AddSpecialEffect(1000204, 200000)
    AddSpecialEffect(1000205, 200000)
    AddSpecialEffect(1000206, 200000)
    AddSpecialEffect(1000150, 200000)
    AddSpecialEffect(1000151, 200000)
    AddSpecialEffect(1000152, 200000)
    AddSpecialEffect(1000207, 200000)
    AddSpecialEffect(1000208, 200000)
    AddSpecialEffect(1000209, 200000)
    AddSpecialEffect(1000211, 200000)
    AddSpecialEffect(1000212, 200000)
    AddSpecialEffect(1000213, 200000)
    AddSpecialEffect(1000214, 200000)
    AddSpecialEffect(1000215, 200000)
    AddSpecialEffect(1000216, 200000)
    AddSpecialEffect(1000217, 200000)
    AddSpecialEffect(1000218, 200000)
    AddSpecialEffect(1000219, 200000)
    AddSpecialEffect(1000220, 200000)
    AddSpecialEffect(1000221, 200000)
    AddSpecialEffect(1000222, 200000)
    AddSpecialEffect(1000906, 200000)
    AddSpecialEffect(1000907, 200000)
    AddSpecialEffect(1000908, 200000)
    AddSpecialEffect(1000909, 200000)
    AddSpecialEffect(1000910, 200000)
    AddSpecialEffect(1000911, 200000)
    AddSpecialEffect(1000912, 200000)
    AddSpecialEffect(1000913, 200000)
    AddSpecialEffect(1000500, 200000)
    AddSpecialEffect(1000300, 200000)
    AddSpecialEffect(1000223, 200000)
    AddSpecialEffect(1000224, 200000)
    AddSpecialEffect(1000225, 200000)
    AddSpecialEffect(1000120, 200000)
    AddSpecialEffect(1000121, 200000)
    AddSpecialEffect(1000122, 200000)
    AddSpecialEffect(1000123, 200000)
    AddSpecialEffect(1000124, 200000)
    AddSpecialEffect(1000125, 200000)
    AddSpecialEffect(1000126, 200000)
    AddSpecialEffect(1000226, 200000)
    AddSpecialEffect(1000227, 200000)
    AddSpecialEffect(1000900, 200000)
    AddSpecialEffect(1000901, 200000)
    AddSpecialEffect(1000902, 200000)
    AddSpecialEffect(1000903, 200000)
    AddSpecialEffect(1000904, 200000)
    AddSpecialEffect(1000099, 200000)
    AddSpecialEffect(1000090, 200000)
    AddSpecialEffect(1000905, 200000)
    AddSpecialEffect(1000100, 200000)
    AddSpecialEffect(1000101, 200000)
    AddSpecialEffect(1000102, 200000)
    AddSpecialEffect(1000103, 200000)
    AddSpecialEffect(1000104, 200000)
    AddSpecialEffect(1000105, 200000)
    AddSpecialEffect(1000106, 200000)
    AddSpecialEffect(1000107, 200000)
    AddSpecialEffect(1000228, 200000)
    AddSpecialEffect(1000229, 200000)
    AddSpecialEffect(1000230, 200000)
    AddSpecialEffect(1000200, 200000)
    AddSpecialEffect(1000231, 200000)
    AddSpecialEffect(1000232, 200000)
    AddSpecialEffect(1000233, 200000)
    AddSpecialEffect(1000234, 200000)
    AddSpecialEffect(1000235, 200000)
    AddSpecialEffect(1000210, 200000)
    AddSpecialEffect(1000236, 200000)
    AddSpecialEffect(1000237, 200000)
    AddSpecialEffect(1000238, 200000)
    AddSpecialEffect(1000111, 200000)
    AddSpecialEffect(1000112, 200000)
    AddSpecialEffect(1000110, 200000)
    AddSpecialEffect(1000113, 200000)
    AddSpecialEffect(1003900, 200000)
    AddSpecialEffect(1003910, 200000)
    AddSpecialEffect(1003901, 200000)
    AddSpecialEffect(1003911, 200000)
    AddSpecialEffect(1003902, 200000)
    AddSpecialEffect(1003912, 200000)
    AddSpecialEffect(1000800, 200000)
    AddSpecialEffect(1000801, 200000)
    WaitFrames(10)  # give other loaded maps time to trigger
    DisableFlag(TriggerFlags.EnemySpeedUp)
    return RESTART


@RestartOnRest
def EnemyExtremeSpeedUp():
    """ 11002201: Temporary enemy effect. """
    Await(TriggerFlags.EnemyExtremeSpeedUp)
    AddSpecialEffect(6130, 200001)
    AddSpecialEffect(6260, 200001)
    AddSpecialEffect(6541, 200001)
    AddSpecialEffect(6562, 200001)
    AddSpecialEffect(6591, 200001)
    AddSpecialEffect(1000960, 200001)
    AddSpecialEffect(1000201, 200001)
    AddSpecialEffect(1000202, 200001)
    AddSpecialEffect(1000203, 200001)
    AddSpecialEffect(1000204, 200001)
    AddSpecialEffect(1000205, 200001)
    AddSpecialEffect(1000206, 200001)
    AddSpecialEffect(1000150, 200001)
    AddSpecialEffect(1000151, 200001)
    AddSpecialEffect(1000152, 200001)
    AddSpecialEffect(1000207, 200001)
    AddSpecialEffect(1000208, 200001)
    AddSpecialEffect(1000209, 200001)
    AddSpecialEffect(1000211, 200001)
    AddSpecialEffect(1000212, 200001)
    AddSpecialEffect(1000213, 200001)
    AddSpecialEffect(1000214, 200001)
    AddSpecialEffect(1000215, 200001)
    AddSpecialEffect(1000216, 200001)
    AddSpecialEffect(1000217, 200001)
    AddSpecialEffect(1000218, 200001)
    AddSpecialEffect(1000219, 200001)
    AddSpecialEffect(1000220, 200001)
    AddSpecialEffect(1000221, 200001)
    AddSpecialEffect(1000222, 200001)
    AddSpecialEffect(1000906, 200001)
    AddSpecialEffect(1000907, 200001)
    AddSpecialEffect(1000908, 200001)
    AddSpecialEffect(1000909, 200001)
    AddSpecialEffect(1000910, 200001)
    AddSpecialEffect(1000911, 200001)
    AddSpecialEffect(1000912, 200001)
    AddSpecialEffect(1000913, 200001)
    AddSpecialEffect(1000500, 200001)
    AddSpecialEffect(1000300, 200001)
    AddSpecialEffect(1000223, 200001)
    AddSpecialEffect(1000224, 200001)
    AddSpecialEffect(1000225, 200001)
    AddSpecialEffect(1000120, 200001)
    AddSpecialEffect(1000121, 200001)
    AddSpecialEffect(1000122, 200001)
    AddSpecialEffect(1000123, 200001)
    AddSpecialEffect(1000124, 200001)
    AddSpecialEffect(1000125, 200001)
    AddSpecialEffect(1000126, 200001)
    AddSpecialEffect(1000226, 200001)
    AddSpecialEffect(1000227, 200001)
    AddSpecialEffect(1000900, 200001)
    AddSpecialEffect(1000901, 200001)
    AddSpecialEffect(1000902, 200001)
    AddSpecialEffect(1000903, 200001)
    AddSpecialEffect(1000904, 200001)
    AddSpecialEffect(1000099, 200001)
    AddSpecialEffect(1000090, 200001)
    AddSpecialEffect(1000905, 200001)
    AddSpecialEffect(1000100, 200001)
    AddSpecialEffect(1000101, 200001)
    AddSpecialEffect(1000102, 200001)
    AddSpecialEffect(1000103, 200001)
    AddSpecialEffect(1000104, 200001)
    AddSpecialEffect(1000105, 200001)
    AddSpecialEffect(1000106, 200001)
    AddSpecialEffect(1000107, 200001)
    AddSpecialEffect(1000228, 200001)
    AddSpecialEffect(1000229, 200001)
    AddSpecialEffect(1000230, 200001)
    AddSpecialEffect(1000200, 200001)
    AddSpecialEffect(1000231, 200001)
    AddSpecialEffect(1000232, 200001)
    AddSpecialEffect(1000233, 200001)
    AddSpecialEffect(1000234, 200001)
    AddSpecialEffect(1000235, 200001)
    AddSpecialEffect(1000210, 200001)
    AddSpecialEffect(1000236, 200001)
    AddSpecialEffect(1000237, 200001)
    AddSpecialEffect(1000238, 200001)
    AddSpecialEffect(1000111, 200001)
    AddSpecialEffect(1000112, 200001)
    AddSpecialEffect(1000110, 200001)
    AddSpecialEffect(1000113, 200001)
    AddSpecialEffect(1003900, 200001)
    AddSpecialEffect(1003910, 200001)
    AddSpecialEffect(1003901, 200001)
    AddSpecialEffect(1003911, 200001)
    AddSpecialEffect(1003902, 200001)
    AddSpecialEffect(1003912, 200001)
    AddSpecialEffect(1000800, 200001)
    AddSpecialEffect(1000801, 200001)
    WaitFrames(10)  # give other loaded maps time to trigger
    DisableFlag(TriggerFlags.EnemyExtremeSpeedUp)
    return RESTART


@RestartOnRest
def EnemySpeedDown():
    """ 11002202: Temporary enemy effect. """
    Await(TriggerFlags.EnemySpeedDown)
    AddSpecialEffect(6130, 200002)
    AddSpecialEffect(6260, 200002)
    AddSpecialEffect(6541, 200002)
    AddSpecialEffect(6562, 200002)
    AddSpecialEffect(6591, 200002)
    AddSpecialEffect(1000960, 200002)
    AddSpecialEffect(1000201, 200002)
    AddSpecialEffect(1000202, 200002)
    AddSpecialEffect(1000203, 200002)
    AddSpecialEffect(1000204, 200002)
    AddSpecialEffect(1000205, 200002)
    AddSpecialEffect(1000206, 200002)
    AddSpecialEffect(1000150, 200002)
    AddSpecialEffect(1000151, 200002)
    AddSpecialEffect(1000152, 200002)
    AddSpecialEffect(1000207, 200002)
    AddSpecialEffect(1000208, 200002)
    AddSpecialEffect(1000209, 200002)
    AddSpecialEffect(1000211, 200002)
    AddSpecialEffect(1000212, 200002)
    AddSpecialEffect(1000213, 200002)
    AddSpecialEffect(1000214, 200002)
    AddSpecialEffect(1000215, 200002)
    AddSpecialEffect(1000216, 200002)
    AddSpecialEffect(1000217, 200002)
    AddSpecialEffect(1000218, 200002)
    AddSpecialEffect(1000219, 200002)
    AddSpecialEffect(1000220, 200002)
    AddSpecialEffect(1000221, 200002)
    AddSpecialEffect(1000222, 200002)
    AddSpecialEffect(1000906, 200002)
    AddSpecialEffect(1000907, 200002)
    AddSpecialEffect(1000908, 200002)
    AddSpecialEffect(1000909, 200002)
    AddSpecialEffect(1000910, 200002)
    AddSpecialEffect(1000911, 200002)
    AddSpecialEffect(1000912, 200002)
    AddSpecialEffect(1000913, 200002)
    AddSpecialEffect(1000500, 200002)
    AddSpecialEffect(1000300, 200002)
    AddSpecialEffect(1000223, 200002)
    AddSpecialEffect(1000224, 200002)
    AddSpecialEffect(1000225, 200002)
    AddSpecialEffect(1000120, 200002)
    AddSpecialEffect(1000121, 200002)
    AddSpecialEffect(1000122, 200002)
    AddSpecialEffect(1000123, 200002)
    AddSpecialEffect(1000124, 200002)
    AddSpecialEffect(1000125, 200002)
    AddSpecialEffect(1000126, 200002)
    AddSpecialEffect(1000226, 200002)
    AddSpecialEffect(1000227, 200002)
    AddSpecialEffect(1000900, 200002)
    AddSpecialEffect(1000901, 200002)
    AddSpecialEffect(1000902, 200002)
    AddSpecialEffect(1000903, 200002)
    AddSpecialEffect(1000904, 200002)
    AddSpecialEffect(1000099, 200002)
    AddSpecialEffect(1000090, 200002)
    AddSpecialEffect(1000905, 200002)
    AddSpecialEffect(1000100, 200002)
    AddSpecialEffect(1000101, 200002)
    AddSpecialEffect(1000102, 200002)
    AddSpecialEffect(1000103, 200002)
    AddSpecialEffect(1000104, 200002)
    AddSpecialEffect(1000105, 200002)
    AddSpecialEffect(1000106, 200002)
    AddSpecialEffect(1000107, 200002)
    AddSpecialEffect(1000228, 200002)
    AddSpecialEffect(1000229, 200002)
    AddSpecialEffect(1000230, 200002)
    AddSpecialEffect(1000200, 200002)
    AddSpecialEffect(1000231, 200002)
    AddSpecialEffect(1000232, 200002)
    AddSpecialEffect(1000233, 200002)
    AddSpecialEffect(1000234, 200002)
    AddSpecialEffect(1000235, 200002)
    AddSpecialEffect(1000210, 200002)
    AddSpecialEffect(1000236, 200002)
    AddSpecialEffect(1000237, 200002)
    AddSpecialEffect(1000238, 200002)
    AddSpecialEffect(1000111, 200002)
    AddSpecialEffect(1000112, 200002)
    AddSpecialEffect(1000110, 200002)
    AddSpecialEffect(1000113, 200002)
    AddSpecialEffect(1003900, 200002)
    AddSpecialEffect(1003910, 200002)
    AddSpecialEffect(1003901, 200002)
    AddSpecialEffect(1003911, 200002)
    AddSpecialEffect(1003902, 200002)
    AddSpecialEffect(1003912, 200002)
    AddSpecialEffect(1000800, 200002)
    AddSpecialEffect(1000801, 200002)
    WaitFrames(10)  # give other loaded maps time to trigger
    DisableFlag(TriggerFlags.EnemySpeedDown)
    return RESTART


@RestartOnRest
def EnemyExtremeSpeedDown():
    """ 11002203: Temporary enemy effect. """
    Await(TriggerFlags.EnemyExtremeSpeedDown)
    AddSpecialEffect(6130, 200003)
    AddSpecialEffect(6260, 200003)
    AddSpecialEffect(6541, 200003)
    AddSpecialEffect(6562, 200003)
    AddSpecialEffect(6591, 200003)
    AddSpecialEffect(1000960, 200003)
    AddSpecialEffect(1000201, 200003)
    AddSpecialEffect(1000202, 200003)
    AddSpecialEffect(1000203, 200003)
    AddSpecialEffect(1000204, 200003)
    AddSpecialEffect(1000205, 200003)
    AddSpecialEffect(1000206, 200003)
    AddSpecialEffect(1000150, 200003)
    AddSpecialEffect(1000151, 200003)
    AddSpecialEffect(1000152, 200003)
    AddSpecialEffect(1000207, 200003)
    AddSpecialEffect(1000208, 200003)
    AddSpecialEffect(1000209, 200003)
    AddSpecialEffect(1000211, 200003)
    AddSpecialEffect(1000212, 200003)
    AddSpecialEffect(1000213, 200003)
    AddSpecialEffect(1000214, 200003)
    AddSpecialEffect(1000215, 200003)
    AddSpecialEffect(1000216, 200003)
    AddSpecialEffect(1000217, 200003)
    AddSpecialEffect(1000218, 200003)
    AddSpecialEffect(1000219, 200003)
    AddSpecialEffect(1000220, 200003)
    AddSpecialEffect(1000221, 200003)
    AddSpecialEffect(1000222, 200003)
    AddSpecialEffect(1000906, 200003)
    AddSpecialEffect(1000907, 200003)
    AddSpecialEffect(1000908, 200003)
    AddSpecialEffect(1000909, 200003)
    AddSpecialEffect(1000910, 200003)
    AddSpecialEffect(1000911, 200003)
    AddSpecialEffect(1000912, 200003)
    AddSpecialEffect(1000913, 200003)
    AddSpecialEffect(1000500, 200003)
    AddSpecialEffect(1000300, 200003)
    AddSpecialEffect(1000223, 200003)
    AddSpecialEffect(1000224, 200003)
    AddSpecialEffect(1000225, 200003)
    AddSpecialEffect(1000120, 200003)
    AddSpecialEffect(1000121, 200003)
    AddSpecialEffect(1000122, 200003)
    AddSpecialEffect(1000123, 200003)
    AddSpecialEffect(1000124, 200003)
    AddSpecialEffect(1000125, 200003)
    AddSpecialEffect(1000126, 200003)
    AddSpecialEffect(1000226, 200003)
    AddSpecialEffect(1000227, 200003)
    AddSpecialEffect(1000900, 200003)
    AddSpecialEffect(1000901, 200003)
    AddSpecialEffect(1000902, 200003)
    AddSpecialEffect(1000903, 200003)
    AddSpecialEffect(1000904, 200003)
    AddSpecialEffect(1000099, 200003)
    AddSpecialEffect(1000090, 200003)
    AddSpecialEffect(1000905, 200003)
    AddSpecialEffect(1000100, 200003)
    AddSpecialEffect(1000101, 200003)
    AddSpecialEffect(1000102, 200003)
    AddSpecialEffect(1000103, 200003)
    AddSpecialEffect(1000104, 200003)
    AddSpecialEffect(1000105, 200003)
    AddSpecialEffect(1000106, 200003)
    AddSpecialEffect(1000107, 200003)
    AddSpecialEffect(1000228, 200003)
    AddSpecialEffect(1000229, 200003)
    AddSpecialEffect(1000230, 200003)
    AddSpecialEffect(1000200, 200003)
    AddSpecialEffect(1000231, 200003)
    AddSpecialEffect(1000232, 200003)
    AddSpecialEffect(1000233, 200003)
    AddSpecialEffect(1000234, 200003)
    AddSpecialEffect(1000235, 200003)
    AddSpecialEffect(1000210, 200003)
    AddSpecialEffect(1000236, 200003)
    AddSpecialEffect(1000237, 200003)
    AddSpecialEffect(1000238, 200003)
    AddSpecialEffect(1000111, 200003)
    AddSpecialEffect(1000112, 200003)
    AddSpecialEffect(1000110, 200003)
    AddSpecialEffect(1000113, 200003)
    AddSpecialEffect(1003900, 200003)
    AddSpecialEffect(1003910, 200003)
    AddSpecialEffect(1003901, 200003)
    AddSpecialEffect(1003911, 200003)
    AddSpecialEffect(1003902, 200003)
    AddSpecialEffect(1003912, 200003)
    AddSpecialEffect(1000800, 200003)
    AddSpecialEffect(1000801, 200003)
    WaitFrames(10)  # give other loaded maps time to trigger
    DisableFlag(TriggerFlags.EnemyExtremeSpeedDown)
    return RESTART


@RestartOnRest
def EnemyHealthRegain():
    """ 11002204: Temporary enemy effect. """
    Await(TriggerFlags.EnemyHealthRegain)
    AddSpecialEffect(6130, 200004)
    AddSpecialEffect(6260, 200004)
    AddSpecialEffect(6541, 200004)
    AddSpecialEffect(6562, 200004)
    AddSpecialEffect(6591, 200004)
    AddSpecialEffect(1000960, 200004)
    AddSpecialEffect(1000201, 200004)
    AddSpecialEffect(1000202, 200004)
    AddSpecialEffect(1000203, 200004)
    AddSpecialEffect(1000204, 200004)
    AddSpecialEffect(1000205, 200004)
    AddSpecialEffect(1000206, 200004)
    AddSpecialEffect(1000150, 200004)
    AddSpecialEffect(1000151, 200004)
    AddSpecialEffect(1000152, 200004)
    AddSpecialEffect(1000207, 200004)
    AddSpecialEffect(1000208, 200004)
    AddSpecialEffect(1000209, 200004)
    AddSpecialEffect(1000211, 200004)
    AddSpecialEffect(1000212, 200004)
    AddSpecialEffect(1000213, 200004)
    AddSpecialEffect(1000214, 200004)
    AddSpecialEffect(1000215, 200004)
    AddSpecialEffect(1000216, 200004)
    AddSpecialEffect(1000217, 200004)
    AddSpecialEffect(1000218, 200004)
    AddSpecialEffect(1000219, 200004)
    AddSpecialEffect(1000220, 200004)
    AddSpecialEffect(1000221, 200004)
    AddSpecialEffect(1000222, 200004)
    AddSpecialEffect(1000906, 200004)
    AddSpecialEffect(1000907, 200004)
    AddSpecialEffect(1000908, 200004)
    AddSpecialEffect(1000909, 200004)
    AddSpecialEffect(1000910, 200004)
    AddSpecialEffect(1000911, 200004)
    AddSpecialEffect(1000912, 200004)
    AddSpecialEffect(1000913, 200004)
    AddSpecialEffect(1000500, 200004)
    AddSpecialEffect(1000300, 200004)
    AddSpecialEffect(1000223, 200004)
    AddSpecialEffect(1000224, 200004)
    AddSpecialEffect(1000225, 200004)
    AddSpecialEffect(1000120, 200004)
    AddSpecialEffect(1000121, 200004)
    AddSpecialEffect(1000122, 200004)
    AddSpecialEffect(1000123, 200004)
    AddSpecialEffect(1000124, 200004)
    AddSpecialEffect(1000125, 200004)
    AddSpecialEffect(1000126, 200004)
    AddSpecialEffect(1000226, 200004)
    AddSpecialEffect(1000227, 200004)
    AddSpecialEffect(1000900, 200004)
    AddSpecialEffect(1000901, 200004)
    AddSpecialEffect(1000902, 200004)
    AddSpecialEffect(1000903, 200004)
    AddSpecialEffect(1000904, 200004)
    AddSpecialEffect(1000099, 200004)
    AddSpecialEffect(1000090, 200004)
    AddSpecialEffect(1000905, 200004)
    AddSpecialEffect(1000100, 200004)
    AddSpecialEffect(1000101, 200004)
    AddSpecialEffect(1000102, 200004)
    AddSpecialEffect(1000103, 200004)
    AddSpecialEffect(1000104, 200004)
    AddSpecialEffect(1000105, 200004)
    AddSpecialEffect(1000106, 200004)
    AddSpecialEffect(1000107, 200004)
    AddSpecialEffect(1000228, 200004)
    AddSpecialEffect(1000229, 200004)
    AddSpecialEffect(1000230, 200004)
    AddSpecialEffect(1000200, 200004)
    AddSpecialEffect(1000231, 200004)
    AddSpecialEffect(1000232, 200004)
    AddSpecialEffect(1000233, 200004)
    AddSpecialEffect(1000234, 200004)
    AddSpecialEffect(1000235, 200004)
    AddSpecialEffect(1000210, 200004)
    AddSpecialEffect(1000236, 200004)
    AddSpecialEffect(1000237, 200004)
    AddSpecialEffect(1000238, 200004)
    AddSpecialEffect(1000111, 200004)
    AddSpecialEffect(1000112, 200004)
    AddSpecialEffect(1000110, 200004)
    AddSpecialEffect(1000113, 200004)
    AddSpecialEffect(1003900, 200004)
    AddSpecialEffect(1003910, 200004)
    AddSpecialEffect(1003901, 200004)
    AddSpecialEffect(1003911, 200004)
    AddSpecialEffect(1003902, 200004)
    AddSpecialEffect(1003912, 200004)
    AddSpecialEffect(1000800, 200004)
    AddSpecialEffect(1000801, 200004)
    WaitFrames(10)  # give other loaded maps time to trigger
    DisableFlag(TriggerFlags.EnemyHealthRegain)
    return RESTART


@RestartOnRest
def EnemyMaxHealthUp():
    """ 11002205: Temporary enemy effect. """
    Await(TriggerFlags.EnemyMaxHealthUp)
    AddSpecialEffect(6130, 200005)
    AddSpecialEffect(6260, 200005)
    AddSpecialEffect(6541, 200005)
    AddSpecialEffect(6562, 200005)
    AddSpecialEffect(6591, 200005)
    AddSpecialEffect(1000960, 200005)
    AddSpecialEffect(1000201, 200005)
    AddSpecialEffect(1000202, 200005)
    AddSpecialEffect(1000203, 200005)
    AddSpecialEffect(1000204, 200005)
    AddSpecialEffect(1000205, 200005)
    AddSpecialEffect(1000206, 200005)
    AddSpecialEffect(1000150, 200005)
    AddSpecialEffect(1000151, 200005)
    AddSpecialEffect(1000152, 200005)
    AddSpecialEffect(1000207, 200005)
    AddSpecialEffect(1000208, 200005)
    AddSpecialEffect(1000209, 200005)
    AddSpecialEffect(1000211, 200005)
    AddSpecialEffect(1000212, 200005)
    AddSpecialEffect(1000213, 200005)
    AddSpecialEffect(1000214, 200005)
    AddSpecialEffect(1000215, 200005)
    AddSpecialEffect(1000216, 200005)
    AddSpecialEffect(1000217, 200005)
    AddSpecialEffect(1000218, 200005)
    AddSpecialEffect(1000219, 200005)
    AddSpecialEffect(1000220, 200005)
    AddSpecialEffect(1000221, 200005)
    AddSpecialEffect(1000222, 200005)
    AddSpecialEffect(1000906, 200005)
    AddSpecialEffect(1000907, 200005)
    AddSpecialEffect(1000908, 200005)
    AddSpecialEffect(1000909, 200005)
    AddSpecialEffect(1000910, 200005)
    AddSpecialEffect(1000911, 200005)
    AddSpecialEffect(1000912, 200005)
    AddSpecialEffect(1000913, 200005)
    AddSpecialEffect(1000500, 200005)
    AddSpecialEffect(1000300, 200005)
    AddSpecialEffect(1000223, 200005)
    AddSpecialEffect(1000224, 200005)
    AddSpecialEffect(1000225, 200005)
    AddSpecialEffect(1000120, 200005)
    AddSpecialEffect(1000121, 200005)
    AddSpecialEffect(1000122, 200005)
    AddSpecialEffect(1000123, 200005)
    AddSpecialEffect(1000124, 200005)
    AddSpecialEffect(1000125, 200005)
    AddSpecialEffect(1000126, 200005)
    AddSpecialEffect(1000226, 200005)
    AddSpecialEffect(1000227, 200005)
    AddSpecialEffect(1000900, 200005)
    AddSpecialEffect(1000901, 200005)
    AddSpecialEffect(1000902, 200005)
    AddSpecialEffect(1000903, 200005)
    AddSpecialEffect(1000904, 200005)
    AddSpecialEffect(1000099, 200005)
    AddSpecialEffect(1000090, 200005)
    AddSpecialEffect(1000905, 200005)
    AddSpecialEffect(1000100, 200005)
    AddSpecialEffect(1000101, 200005)
    AddSpecialEffect(1000102, 200005)
    AddSpecialEffect(1000103, 200005)
    AddSpecialEffect(1000104, 200005)
    AddSpecialEffect(1000105, 200005)
    AddSpecialEffect(1000106, 200005)
    AddSpecialEffect(1000107, 200005)
    AddSpecialEffect(1000228, 200005)
    AddSpecialEffect(1000229, 200005)
    AddSpecialEffect(1000230, 200005)
    AddSpecialEffect(1000200, 200005)
    AddSpecialEffect(1000231, 200005)
    AddSpecialEffect(1000232, 200005)
    AddSpecialEffect(1000233, 200005)
    AddSpecialEffect(1000234, 200005)
    AddSpecialEffect(1000235, 200005)
    AddSpecialEffect(1000210, 200005)
    AddSpecialEffect(1000236, 200005)
    AddSpecialEffect(1000237, 200005)
    AddSpecialEffect(1000238, 200005)
    AddSpecialEffect(1000111, 200005)
    AddSpecialEffect(1000112, 200005)
    AddSpecialEffect(1000110, 200005)
    AddSpecialEffect(1000113, 200005)
    AddSpecialEffect(1003900, 200005)
    AddSpecialEffect(1003910, 200005)
    AddSpecialEffect(1003901, 200005)
    AddSpecialEffect(1003911, 200005)
    AddSpecialEffect(1003902, 200005)
    AddSpecialEffect(1003912, 200005)
    AddSpecialEffect(1000800, 200005)
    AddSpecialEffect(1000801, 200005)
    WaitFrames(10)  # give other loaded maps time to trigger
    DisableFlag(TriggerFlags.EnemyMaxHealthUp)
    return RESTART


@RestartOnRest
def EnemyMaxHealthDown():
    """ 11002206: Temporary enemy effect. """
    Await(TriggerFlags.EnemyMaxHealthDown)
    AddSpecialEffect(6130, 200006)
    AddSpecialEffect(6260, 200006)
    AddSpecialEffect(6541, 200006)
    AddSpecialEffect(6562, 200006)
    AddSpecialEffect(6591, 200006)
    AddSpecialEffect(1000960, 200006)
    AddSpecialEffect(1000201, 200006)
    AddSpecialEffect(1000202, 200006)
    AddSpecialEffect(1000203, 200006)
    AddSpecialEffect(1000204, 200006)
    AddSpecialEffect(1000205, 200006)
    AddSpecialEffect(1000206, 200006)
    AddSpecialEffect(1000150, 200006)
    AddSpecialEffect(1000151, 200006)
    AddSpecialEffect(1000152, 200006)
    AddSpecialEffect(1000207, 200006)
    AddSpecialEffect(1000208, 200006)
    AddSpecialEffect(1000209, 200006)
    AddSpecialEffect(1000211, 200006)
    AddSpecialEffect(1000212, 200006)
    AddSpecialEffect(1000213, 200006)
    AddSpecialEffect(1000214, 200006)
    AddSpecialEffect(1000215, 200006)
    AddSpecialEffect(1000216, 200006)
    AddSpecialEffect(1000217, 200006)
    AddSpecialEffect(1000218, 200006)
    AddSpecialEffect(1000219, 200006)
    AddSpecialEffect(1000220, 200006)
    AddSpecialEffect(1000221, 200006)
    AddSpecialEffect(1000222, 200006)
    AddSpecialEffect(1000906, 200006)
    AddSpecialEffect(1000907, 200006)
    AddSpecialEffect(1000908, 200006)
    AddSpecialEffect(1000909, 200006)
    AddSpecialEffect(1000910, 200006)
    AddSpecialEffect(1000911, 200006)
    AddSpecialEffect(1000912, 200006)
    AddSpecialEffect(1000913, 200006)
    AddSpecialEffect(1000500, 200006)
    AddSpecialEffect(1000300, 200006)
    AddSpecialEffect(1000223, 200006)
    AddSpecialEffect(1000224, 200006)
    AddSpecialEffect(1000225, 200006)
    AddSpecialEffect(1000120, 200006)
    AddSpecialEffect(1000121, 200006)
    AddSpecialEffect(1000122, 200006)
    AddSpecialEffect(1000123, 200006)
    AddSpecialEffect(1000124, 200006)
    AddSpecialEffect(1000125, 200006)
    AddSpecialEffect(1000126, 200006)
    AddSpecialEffect(1000226, 200006)
    AddSpecialEffect(1000227, 200006)
    AddSpecialEffect(1000900, 200006)
    AddSpecialEffect(1000901, 200006)
    AddSpecialEffect(1000902, 200006)
    AddSpecialEffect(1000903, 200006)
    AddSpecialEffect(1000904, 200006)
    AddSpecialEffect(1000099, 200006)
    AddSpecialEffect(1000090, 200006)
    AddSpecialEffect(1000905, 200006)
    AddSpecialEffect(1000100, 200006)
    AddSpecialEffect(1000101, 200006)
    AddSpecialEffect(1000102, 200006)
    AddSpecialEffect(1000103, 200006)
    AddSpecialEffect(1000104, 200006)
    AddSpecialEffect(1000105, 200006)
    AddSpecialEffect(1000106, 200006)
    AddSpecialEffect(1000107, 200006)
    AddSpecialEffect(1000228, 200006)
    AddSpecialEffect(1000229, 200006)
    AddSpecialEffect(1000230, 200006)
    AddSpecialEffect(1000200, 200006)
    AddSpecialEffect(1000231, 200006)
    AddSpecialEffect(1000232, 200006)
    AddSpecialEffect(1000233, 200006)
    AddSpecialEffect(1000234, 200006)
    AddSpecialEffect(1000235, 200006)
    AddSpecialEffect(1000210, 200006)
    AddSpecialEffect(1000236, 200006)
    AddSpecialEffect(1000237, 200006)
    AddSpecialEffect(1000238, 200006)
    AddSpecialEffect(1000111, 200006)
    AddSpecialEffect(1000112, 200006)
    AddSpecialEffect(1000110, 200006)
    AddSpecialEffect(1000113, 200006)
    AddSpecialEffect(1003900, 200006)
    AddSpecialEffect(1003910, 200006)
    AddSpecialEffect(1003901, 200006)
    AddSpecialEffect(1003911, 200006)
    AddSpecialEffect(1003902, 200006)
    AddSpecialEffect(1003912, 200006)
    AddSpecialEffect(1000800, 200006)
    AddSpecialEffect(1000801, 200006)
    WaitFrames(10)  # give other loaded maps time to trigger
    DisableFlag(TriggerFlags.EnemyMaxHealthDown)
    return RESTART


@RestartOnRest
def EnemyDefenseUp():
    """ 11002207: Temporary enemy effect. """
    Await(TriggerFlags.EnemyDefenseUp)
    AddSpecialEffect(6130, 200007)
    AddSpecialEffect(6260, 200007)
    AddSpecialEffect(6541, 200007)
    AddSpecialEffect(6562, 200007)
    AddSpecialEffect(6591, 200007)
    AddSpecialEffect(1000960, 200007)
    AddSpecialEffect(1000201, 200007)
    AddSpecialEffect(1000202, 200007)
    AddSpecialEffect(1000203, 200007)
    AddSpecialEffect(1000204, 200007)
    AddSpecialEffect(1000205, 200007)
    AddSpecialEffect(1000206, 200007)
    AddSpecialEffect(1000150, 200007)
    AddSpecialEffect(1000151, 200007)
    AddSpecialEffect(1000152, 200007)
    AddSpecialEffect(1000207, 200007)
    AddSpecialEffect(1000208, 200007)
    AddSpecialEffect(1000209, 200007)
    AddSpecialEffect(1000211, 200007)
    AddSpecialEffect(1000212, 200007)
    AddSpecialEffect(1000213, 200007)
    AddSpecialEffect(1000214, 200007)
    AddSpecialEffect(1000215, 200007)
    AddSpecialEffect(1000216, 200007)
    AddSpecialEffect(1000217, 200007)
    AddSpecialEffect(1000218, 200007)
    AddSpecialEffect(1000219, 200007)
    AddSpecialEffect(1000220, 200007)
    AddSpecialEffect(1000221, 200007)
    AddSpecialEffect(1000222, 200007)
    AddSpecialEffect(1000906, 200007)
    AddSpecialEffect(1000907, 200007)
    AddSpecialEffect(1000908, 200007)
    AddSpecialEffect(1000909, 200007)
    AddSpecialEffect(1000910, 200007)
    AddSpecialEffect(1000911, 200007)
    AddSpecialEffect(1000912, 200007)
    AddSpecialEffect(1000913, 200007)
    AddSpecialEffect(1000500, 200007)
    AddSpecialEffect(1000300, 200007)
    AddSpecialEffect(1000223, 200007)
    AddSpecialEffect(1000224, 200007)
    AddSpecialEffect(1000225, 200007)
    AddSpecialEffect(1000120, 200007)
    AddSpecialEffect(1000121, 200007)
    AddSpecialEffect(1000122, 200007)
    AddSpecialEffect(1000123, 200007)
    AddSpecialEffect(1000124, 200007)
    AddSpecialEffect(1000125, 200007)
    AddSpecialEffect(1000126, 200007)
    AddSpecialEffect(1000226, 200007)
    AddSpecialEffect(1000227, 200007)
    AddSpecialEffect(1000900, 200007)
    AddSpecialEffect(1000901, 200007)
    AddSpecialEffect(1000902, 200007)
    AddSpecialEffect(1000903, 200007)
    AddSpecialEffect(1000904, 200007)
    AddSpecialEffect(1000099, 200007)
    AddSpecialEffect(1000090, 200007)
    AddSpecialEffect(1000905, 200007)
    AddSpecialEffect(1000100, 200007)
    AddSpecialEffect(1000101, 200007)
    AddSpecialEffect(1000102, 200007)
    AddSpecialEffect(1000103, 200007)
    AddSpecialEffect(1000104, 200007)
    AddSpecialEffect(1000105, 200007)
    AddSpecialEffect(1000106, 200007)
    AddSpecialEffect(1000107, 200007)
    AddSpecialEffect(1000228, 200007)
    AddSpecialEffect(1000229, 200007)
    AddSpecialEffect(1000230, 200007)
    AddSpecialEffect(1000200, 200007)
    AddSpecialEffect(1000231, 200007)
    AddSpecialEffect(1000232, 200007)
    AddSpecialEffect(1000233, 200007)
    AddSpecialEffect(1000234, 200007)
    AddSpecialEffect(1000235, 200007)
    AddSpecialEffect(1000210, 200007)
    AddSpecialEffect(1000236, 200007)
    AddSpecialEffect(1000237, 200007)
    AddSpecialEffect(1000238, 200007)
    AddSpecialEffect(1000111, 200007)
    AddSpecialEffect(1000112, 200007)
    AddSpecialEffect(1000110, 200007)
    AddSpecialEffect(1000113, 200007)
    AddSpecialEffect(1003900, 200007)
    AddSpecialEffect(1003910, 200007)
    AddSpecialEffect(1003901, 200007)
    AddSpecialEffect(1003911, 200007)
    AddSpecialEffect(1003902, 200007)
    AddSpecialEffect(1003912, 200007)
    AddSpecialEffect(1000800, 200007)
    AddSpecialEffect(1000801, 200007)
    WaitFrames(10)  # give other loaded maps time to trigger
    DisableFlag(TriggerFlags.EnemyDefenseUp)
    return RESTART
