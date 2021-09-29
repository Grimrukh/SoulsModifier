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
    # <!--!>


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
