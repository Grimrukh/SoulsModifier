"""
linked:


strings:

"""
from soulstruct.darksouls1r.events import *
from ..entities.m18_00_00_00_entities import *
from ..entities.m10_02_00_00_entities import Boxes as m10_02_Boxes
from ..entities.m16_00_00_00_entities import Boxes as m16_00_Boxes
from ..entities.common_entities import *


def Constructor():
    """ 0: Event 0 """
    SkipLinesIfFlagOff(1, 11800100)
    RegisterBonfire(11800992, obj=Objects.o8310, reaction_distance=2.0, reaction_angle=180.0, initial_kindle_level=10)
    SkipLinesIfFlagOff(1, 11800210)
    RegisterBonfire(11800992, obj=Objects.o8310, reaction_distance=2.0, reaction_angle=180.0, initial_kindle_level=30)
    SkipLinesIfClient(2)
    DisableObject(Objects.o8051_0000)
    DeleteVFX(VFX.MultiplayerFog1, erase_root_only=False)
    SkipLinesIfFlagOff(3, 15)
    DisableObject(Objects.o8310)
    DisableObject(Objects.o8311)
    EnableObject(Objects.o8312)
    RunEvent(20)
    RunEvent(21)
    RunEvent(11800100)
    RunEvent(11800101)
    RunEvent(11800200)
    RunEvent(11800230, slot=0, args=(1, 180005, Objects.o8310))
    RunEvent(11800230, slot=1, args=(2, 180006, Objects.o8310))
    RunEvent(11800230, slot=2, args=(3, 180007, Objects.o8310))
    RunEvent(11800230, slot=3, args=(4, 180008, Objects.o8310))
    RunEvent(11800210)
    RunEvent(11800220)
    RunEvent(11806100, slot=0, args=(Characters.c2791_0000, Boxes.GhostKnightMovement1))
    RunEvent(11806100, slot=1, args=(Characters.c2791_0001, Boxes.GhostKnightMovement2))
    RunEvent(11806100, slot=2, args=(Characters.c2791_0002, Boxes.GhostKnightMovement3))
    RunEvent(11806100, slot=3, args=(Characters.c2791_0003, Boxes.GhostKnightMovement4))
    RunEvent(11806100, slot=4, args=(Characters.c2791_0004, Boxes.GhostKnightMovement5))
    RunEvent(11806100, slot=5, args=(Characters.c2791_0005, Boxes.GhostKnightMovement6))
    
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
    RunEvent(11800002)
    DisableSoundEvent(1803800)
    SkipLinesIfFlagOff(4, 15)
    RunEvent(11805392)
    DisableObject(Objects.o8050_0000)
    DeleteVFX(VFX.GwynEntranceFog, erase_root_only=False)
    SkipLines(7)
    RunEvent(11805390)
    RunEvent(11805391)
    RunEvent(11805393)
    RunEvent(11805392)
    RunEvent(11800001)
    RunEvent(11805394)
    RunEvent(11805395)
    HumanityRegistration(Characters.c0000_0002, 8310)
    RunEvent(11805030)
    RunEvent(11805029)
    RunEvent(11805032)
    RunEvent(11805990, slot=0, args=(11805031, Characters.c0000_0002))
    RunEvent(11800550, slot=0, args=(1000, 1029, 1012))
    EnableImmortality(Characters.c5330_0016)
    SkipLinesIfFlagOn(1, 830)
    DisableCharacter(Characters.c5330_0016)
    SkipLinesIfFlagOn(6, 15)
    RunEvent(11800539, slot=0, args=(Characters.c5330_0016, 1640, 1647, 1647))
    RunEvent(11800530, slot=0, args=(Characters.c5330_0016, 1640, 1647, 1644))
    RunEvent(11800531, slot=0, args=(Characters.c5330_0016, 1640, 1647, 1645))
    RunEvent(11800537, slot=0, args=(Characters.c5330_0016, 1640, 1647, 1649))
    RunEvent(11800541, slot=0, args=(Characters.c5330_0016,))
    RunEvent(11806200)
    EnableImmortality(Characters.c5330_0017)
    SkipLinesIfFlagOn(1, 831)
    DisableCharacter(Characters.c5330_0017)
    SkipLinesIfFlagOn(6, 15)
    RunEvent(11800540, slot=0, args=(Characters.c5330_0017, 1670, 1677, 1677))
    RunEvent(11800533, slot=0, args=(Characters.c5330_0017, 1670, 1677, 1673))
    RunEvent(11800534, slot=0, args=(Characters.c5330_0017, 1670, 1677, 1674))
    RunEvent(11800538, slot=0, args=(Characters.c5330_0017, 1670, 1677, 1678))
    RunEvent(11800542, slot=0, args=(Characters.c5330_0017,))
    RunEvent(11806201)


def Event11805390():
    """ 11805390: Event 11805390 """
    IfFlagOff(1, 15)
    IfActionButton(
        1,
        prompt_text=10010403,
        anchor_entity=Boxes.GwynFogPrompt,
        anchor_type=CoordEntityType.Region,
        line_intersects=Objects.o8050_0000,
        boss_version=True,
    )
    IfConditionTrue(0, input_condition=1)
    RotateToFaceEntity(PLAYER, Boxes.GwynFogRotationTarget)
    ForceAnimation(PLAYER, 7410)
    Restart()


def Event11805391():
    """ 11805391: Event 11805391 """
    IfFlagOff(1, 15)
    IfFlagOn(1, 11805393)
    IfCharacterType(1, PLAYER, CharacterType.WhitePhantom)
    IfActionButton(
        1,
        prompt_text=10010403,
        anchor_entity=Boxes.GwynFogPrompt,
        anchor_type=CoordEntityType.Region,
        trigger_attribute=TriggerAttribute.All,
        line_intersects=Objects.o8050_0000,
    )
    IfConditionTrue(0, input_condition=1)
    RotateToFaceEntity(PLAYER, Boxes.GwynFogRotationTarget)
    ForceAnimation(PLAYER, 7410)
    Restart()


def Event11805393():
    """ 11805393: Event 11805393 """
    SkipLinesIfThisEventOn(3)
    IfFlagOff(1, 15)
    IfCharacterInsideRegion(1, PLAYER, region=Boxes.GwynCombatStart)
    IfConditionTrue(0, input_condition=1)
    SkipLinesIfClient(1)
    NotifyBossBattleStart()
    ActivateMultiplayerBuffs(Characters.c5370_0000)


@RestartOnRest
def Event11805392():
    """ 11805392: Event 11805392 """
    SkipLinesIfFlagOff(3, 15)
    DisableCharacter(Characters.c5370_0000)
    Kill(Characters.c5370_0000, award_souls=False)
    End()
    DisableAI(Characters.c5370_0000)
    IfFlagOn(1, 11805393)
    IfCharacterInsideRegion(1, PLAYER, region=Boxes.GwynCombatStart)
    IfConditionTrue(0, input_condition=1)
    EnableAI(Characters.c5370_0000)
    EnableBossHealthBar(Characters.c5370_0000, name=5370, slot=0)


def Event11800001():
    """ 11800001: Event 11800001 """
    DisableObject(Objects.o8312)
    DisableObject(Objects.o0200_0001)
    IfCharacterDead(0, Characters.c5370_0000)
    EnableFlag(15)
    KillBoss(1800800)
    DisableObject(Objects.o8050_0000)
    DeleteVFX(VFX.GwynEntranceFog, erase_root_only=True)
    SkipLinesIfClient(2)
    SetRespawnPoint(SpawnPoints.SpawnPointAtBoss)
    SaveRequest()
    DisableFlag(11807200)
    DisableFlag(11807210)
    DisableFlag(11807220)
    DisableFlag(11807240)
    DisableObject(Objects.o8310)
    DisableObject(Objects.o8311)
    EnableObject(Objects.o8312)
    DeleteObjectVFX(Objects.o8310, erase_root=True)
    CreateTemporaryVFX(90014, anchor_entity=Objects.o0200_0001, anchor_type=CoordEntityType.Object, model_point=-1)
    Wait(2.0)
    EnableObject(Objects.o0200_0001)


def Event20():
    """ 20: Event 20 """
    EndIfClient()
    IfFlagOn(1, 15)
    IfActionButton(
        1,
        prompt_text=10010108,
        anchor_entity=Objects.o0200_0001,
        anchor_type=CoordEntityType.Object,
        max_distance=1.5,
        model_point=-1,
    )
    IfConditionTrue(0, input_condition=1)
    IncrementNewGameCycle(1)
    PlayCutscene(180000, skippable=True, fade_out=False, player_id=PLAYER)
    WaitFrames(1)
    AwardAchievement(1)
    EnableFlag(20)


def Event21():
    """ 21: Event 21 """
    EndIfClient()
    IfFlagOn(1, 15)
    IfCharacterOutsideRegion(1, PLAYER, region=Spheres.GwynMusic)
    IfInsideMap(1, game_map=KILN_OF_THE_FIRST_FLAME)
    IfConditionTrue(0, input_condition=1)
    PlayCutscene(180001, skippable=True, fade_out=False, player_id=PLAYER)
    WaitFrames(1)
    IncrementNewGameCycle(1)
    AwardAchievement(2)
    EnableFlag(21)


def Event11805394():
    """ 11805394: Event 11805394 """
    DisableNetworkSync()
    IfFlagOff(1, 15)
    IfFlagOn(1, 11805392)
    SkipLinesIfHost(1)
    IfFlagOn(1, 11805391)
    IfCharacterInsideRegion(1, PLAYER, region=Spheres.GwynMusic)
    IfConditionTrue(0, input_condition=1)
    EnableSoundEvent(1803800)


def Event11805395():
    """ 11805395: Event 11805395 """
    DisableNetworkSync()
    IfFlagOn(1, 15)
    IfFlagOn(1, 11805394)
    IfConditionTrue(0, input_condition=1)
    DisableSoundEvent(1803800)


@RestartOnRest
def Event11800002():
    """ 11800002: Event 11800002 """
    IfFlagOn(0, 15)
    DisableCharacter(Characters.c2790_0001)
    DisableCharacter(Characters.c2790_0002)
    DisableCharacter(Characters.c2790_0003)
    DisableCharacter(Characters.c2790_0004)
    DisableCharacter(Characters.c2790_0005)
    DisableCharacter(Characters.c2790_0006)
    DisableCharacter(Characters.c2790_0007)
    DisableCharacter(Characters.c2790_0008)
    DisableCharacter(Characters.c2790_0009)
    DisableCharacter(Characters.c2790_0010)
    DisableCharacter(Characters.c3490_0000)
    DisableCharacter(Characters.c3491_0000)
    DisableCharacter(Characters.c3491_0001)
    Kill(Characters.c2790_0001, award_souls=False)
    Kill(Characters.c2790_0002, award_souls=False)
    Kill(Characters.c2790_0003, award_souls=False)
    Kill(Characters.c2790_0004, award_souls=False)
    Kill(Characters.c2790_0005, award_souls=False)
    Kill(Characters.c2790_0006, award_souls=False)
    Kill(Characters.c2790_0007, award_souls=False)
    Kill(Characters.c2790_0008, award_souls=False)
    Kill(Characters.c2790_0009, award_souls=False)
    Kill(Characters.c2790_0010, award_souls=False)
    Kill(Characters.c3490_0000, award_souls=False)
    Kill(Characters.c3491_0000, award_souls=False)
    Kill(Characters.c3491_0001, award_souls=False)


def Event11800100():
    """ 11800100: Event 11800100 """
    EndIfThisEventOn()
    DisableObject(Objects.o8311)
    IfHost(1)
    IfPlayerHasGood(1, 2510, including_box=False)
    IfActionButton(
        1,
        prompt_text=10010105,
        anchor_entity=Objects.o8310,
        anchor_type=CoordEntityType.Object,
        model_point=150,
    )
    IfConditionTrue(0, input_condition=1)
    PlayCutscene(180015, skippable=True, fade_out=False, player_id=PLAYER)
    WaitFrames(1)
    EnableObject(Objects.o8311)
    RegisterBonfire(11800992, obj=Objects.o8310, reaction_distance=2.0, reaction_angle=180.0, initial_kindle_level=10)
    RemoveGoodFromPlayer(2510)


def Event11800101():
    """ 11800101: Event 11800101 """
    DisableNetworkSync()
    IfFlagOff(1, 11800100)
    IfPlayerDoesNotHaveGood(1, 2510, including_box=False)
    IfActionButton(
        1,
        prompt_text=10010105,
        anchor_entity=Objects.o8310,
        anchor_type=CoordEntityType.Object,
        model_point=150,
        trigger_attribute=TriggerAttribute.All,
    )
    IfFlagOn(2, 11800100)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(2)
    DisplayDialog(
        10010174,
        anchor_entity=Objects.o8310,
        display_distance=3.0,
        button_type=ButtonType.OK_or_Cancel,
        number_buttons=NumberButtons.NoButton,
    )
    Restart()


def Event11800200():
    """ 11800200: Event 11800200 """
    IfFlagOn(0, 756)
    ForceAnimation(PLAYER, 7697)
    WaitFrames(75)
    IfFlagOff(1, 11800201)
    IfPlayerHasGood(1, 2500, including_box=False)
    IfFlagOff(2, 11800202)
    IfPlayerHasGood(2, 2501, including_box=False)
    IfFlagOff(3, 11800203)
    IfPlayerHasGood(3, 2502, including_box=False)
    IfFlagOff(4, 11800204)
    IfPlayerHasGood(4, 2503, including_box=False)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(-1, input_condition=4)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionFalse(2, 1)
    EnableFlag(11800201)
    RemoveGoodFromPlayer(2500)
    SkipLinesIfFinishedConditionFalse(2, 2)
    EnableFlag(11800202)
    RemoveGoodFromPlayer(2501)
    SkipLinesIfFinishedConditionFalse(2, 3)
    EnableFlag(11800203)
    RemoveGoodFromPlayer(2502)
    SkipLinesIfFinishedConditionFalse(2, 4)
    EnableFlag(11800204)
    RemoveGoodFromPlayer(2503)
    EnableFlag(11805111)
    IfFlagOff(0, 11805111)
    WaitFrames(10)
    EndIfFlagOn(11800211)
    DisableFlag(756)
    Restart()


def Event11800230(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 11800230: Event 11800230 """
    IfFlagOn(1, 11805111)
    IfTrueFlagCountEqual(1, arg_0_3, (11800201, 11800204))
    IfConditionTrue(0, input_condition=1)
    DeleteObjectVFX(arg_8_11, erase_root=True)
    CreateObjectVFX(arg_4_7, obj=arg_8_11, model_point=100)
    WaitFrames(95)
    SkipLinesIfFlagRangeAllOn(1, (11800201, 11800204))
    ForceAnimation(PLAYER, 7701, loop=True)
    DisableFlag(11805111)


def Event11800210():
    """ 11800210: Event 11800210 """
    SkipLinesIfFlagOn(17, 15)
    IfTrueFlagCountEqual(2, 1, (11800201, 11800204))
    IfTrueFlagCountEqual(3, 2, (11800201, 11800204))
    IfTrueFlagCountEqual(4, 3, (11800201, 11800204))
    IfTrueFlagCountEqual(5, 4, (11800201, 11800204))
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(-1, input_condition=4)
    IfConditionTrue(-1, input_condition=5)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionFalse(1, 2)
    CreateObjectVFX(180005, obj=Objects.o8310, model_point=100)
    SkipLinesIfFinishedConditionFalse(1, 3)
    CreateObjectVFX(180006, obj=Objects.o8310, model_point=100)
    SkipLinesIfFinishedConditionFalse(1, 4)
    CreateObjectVFX(180007, obj=Objects.o8310, model_point=100)
    SkipLinesIfFinishedConditionFalse(1, 5)
    CreateObjectVFX(180008, obj=Objects.o8310, model_point=100)
    SkipLinesIfThisEventOff(2)
    EndOfAnimation(Objects.o8300, 1)
    End()
    IfFlagOn(1, 11800201)
    IfFlagOn(1, 11800202)
    IfFlagOn(1, 11800203)
    IfFlagOn(1, 11800204)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(11800211)
    DisableFlag(756)
    PlayCutscene(180010, skippable=True, fade_out=False, player_id=PLAYER)
    WaitFrames(1)
    EndOfAnimation(Objects.o8300, 1)
    RegisterBonfire(11800992, obj=Objects.o8310, reaction_distance=2.0, reaction_angle=180.0, initial_kindle_level=30)


def Event11800220():
    """ 11800220: Event 11800220 """
    DisableNetworkSync()
    IfFlagOff(1, 11800210)
    IfActionButton(
        1,
        prompt_text=10010400,
        anchor_entity=Boxes.FirelinkAltarLocked,
        anchor_type=CoordEntityType.Region,
        trigger_attribute=TriggerAttribute.All,
        line_intersects=Objects.o8300,
    )
    IfFlagOn(2, 11805110)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionTrue(2, 2)
    DisplayDialog(
        10010160,
        anchor_entity=Objects.o8300,
        display_distance=3.0,
        button_type=ButtonType.OK_or_Cancel,
        number_buttons=NumberButtons.NoButton,
    )
    SkipLines(2)
    DisableFlag(11805110)
    DisplayDialog(
        10010171,
        anchor_entity=Objects.o8310,
        display_distance=3.0,
        button_type=ButtonType.OK_or_Cancel,
        number_buttons=NumberButtons.NoButton,
    )
    Restart()


@RestartOnRest
def Event11806100(_, arg_0_3: int, arg_4_7: int):
    """ 11806100: Event 11806100 """
    DisableNetworkSync()
    SkipLinesIfThisEventSlotOn(3)
    Move(arg_0_3, destination=arg_4_7, destination_type=CoordEntityType.Region, short_move=True)
    DisableAI(arg_0_3)
    ForceAnimation(arg_0_3, 200, loop=True)
    IfCharacterInsideRegion(0, arg_0_3, region=Boxes.GhostKnightMovementGoal)
    Move(arg_0_3, destination=arg_4_7, destination_type=CoordEntityType.Region, short_move=True)
    Restart()


@RestartOnRest
def Event11805100(_, arg_0_3: int, arg_4_7: int):
    """ 11805100: Event 11805100 """
    IfCharacterAlive(0, arg_0_3)
    IfCharacterDead(0, arg_0_3)
    IfCharacterHuman(-7, PLAYER)
    IfCharacterHollow(-7, PLAYER)
    EndIfConditionFalse(-7)
    AwardItemLot(arg_4_7, host_only=True)


def Event11800510(_, arg_0_3: int, arg_4_7: int):
    """ 11800510: Event 11800510 """
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


def Event11800520(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11800520: Event 11800520 """
    SkipLinesIfThisEventSlotOff(2)
    DropMandatoryTreasure(arg_0_3)
    End()
    IfHealthLessThanOrEqual(0, arg_0_3, 0.0)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)


def Event11800530(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11800530: Event 11800530 """
    IfFlagOn(1, 1643)
    IfFlagOn(1, 830)
    IfFlagOn(1, 11800100)
    IfCharacterAlive(1, arg_0_3)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)


def Event11800531(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11800531: Event 11800531 """
    IfFlagOn(1, 1644)
    IfFlagOn(1, 830)
    IfFlagOn(1, 11800210)
    IfCharacterAlive(1, arg_0_3)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)


def Event11800533(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11800533: Event 11800533 """
    IfFlagOn(1, 1672)
    IfFlagOn(1, 831)
    IfFlagOn(1, 11800100)
    IfCharacterAlive(1, arg_0_3)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)


def Event11800534(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11800534: Event 11800534 """
    IfFlagOn(1, 1673)
    IfFlagOn(1, 831)
    IfFlagOn(1, 11800210)
    IfCharacterAlive(1, arg_0_3)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)


def Event11800537(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11800537: Event 11800537 """
    IfFlagOn(-1, 1642)
    IfFlagOn(-1, 1643)
    IfConditionTrue(1, input_condition=-1)
    IfFlagOff(1, 830)
    IfFlagOn(1, 11800100)
    IfCharacterAlive(1, arg_0_3)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)


def Event11800538(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11800538: Event 11800538 """
    IfFlagOn(-1, 1671)
    IfFlagOn(-1, 1672)
    IfConditionTrue(1, input_condition=-1)
    IfFlagOff(1, 831)
    IfFlagOn(1, 11800100)
    IfCharacterAlive(1, arg_0_3)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)


def Event11800539(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11800539: Event 11800539 """
    IfInsideMap(1, game_map=KILN_OF_THE_FIRST_FLAME)
    IfFlagOn(-7, 11020598)
    IfHealthLessThanOrEqual(7, arg_0_3, 0.8999999761581421)
    IfHealthGreaterThan(7, arg_0_3, 0.0)
    IfAttacked(7, arg_0_3, attacker=PLAYER)
    IfEntityBeyondDistance(7, arg_0_3, PLAYER, radius=15.0)
    IfConditionTrue(-7, input_condition=7)
    IfConditionTrue(1, input_condition=-7)
    IfThisEventOff(1)
    IfFlagOn(2, arg_12_15)
    IfThisEventOn(2)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionTrue(3, 2)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)
    ForceAnimation(arg_0_3, 7009, wait_for_completion=True)
    DisableCharacter(arg_0_3)


def Event11800540(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11800540: Event 11800540 """
    IfInsideMap(1, game_map=KILN_OF_THE_FIRST_FLAME)
    IfFlagOn(-7, 11600590)
    IfHealthLessThanOrEqual(7, arg_0_3, 0.8999999761581421)
    IfHealthGreaterThan(7, arg_0_3, 0.0)
    IfAttacked(7, arg_0_3, attacker=PLAYER)
    IfEntityBeyondDistance(7, arg_0_3, PLAYER, radius=15.0)
    IfConditionTrue(-7, input_condition=7)
    IfConditionTrue(1, input_condition=-7)
    IfThisEventOff(1)
    IfFlagOn(2, arg_12_15)
    IfThisEventOn(2)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionTrue(3, 2)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)
    ForceAnimation(arg_0_3, 7005, wait_for_completion=True)
    DisableCharacter(arg_0_3)


def Event11800541(_, arg_0_3: int):
    """ 11800541: Event 11800541 """
    IfFlagOn(1, 830)
    IfFlagOff(1, 1647)
    IfConditionTrue(0, input_condition=1)
    EnableCharacter(arg_0_3)
    IfFlagOff(0, 830)
    DisableCharacter(arg_0_3)
    Restart()


def Event11800542(_, arg_0_3: int):
    """ 11800542: Event 11800542 """
    IfFlagOn(1, 831)
    IfFlagOff(1, 1676)
    IfConditionTrue(0, input_condition=1)
    EnableCharacter(arg_0_3)
    IfFlagOff(0, 831)
    DisableCharacter(arg_0_3)
    Restart()


def Event11800550(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 11800550: Event 11800550 """
    IfFlagOff(1, 1004)
    IfFlagOn(1, 1003)
    IfFlagOn(1, 11410595)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_0_3, arg_4_7))
    EnableFlag(arg_8_11)


def Event11806200():
    """ 11806200: Event 11806200 """
    IfFlagOn(-1, 1643)
    IfFlagOn(-1, 1644)
    IfFlagOn(-1, 1645)
    IfConditionTrue(1, input_condition=-1)
    IfInsideMap(1, game_map=KILN_OF_THE_FIRST_FLAME)
    IfFlagOn(1, 824)
    IfConditionTrue(0, input_condition=1)
    DisableFlag(824)
    PlayCutscene(
        180050,
        skippable=True,
        fade_out=False,
        player_id=PLAYER,
        move_to_region=m10_02_Boxes.ArriveFromKiln,
        move_to_map=FIRELINK_SHRINE,
    )
    PlayCutscene(100250, skippable=True, fade_out=False, player_id=PLAYER)
    WaitFrames(1)
    DisableCharacter(Characters.c5330_0016)
    DisableFlag(830)
    Restart()


def Event11806201():
    """ 11806201: Event 11806201 """
    IfFlagOn(-1, 1672)
    IfFlagOn(-1, 1673)
    IfFlagOn(-1, 1674)
    IfConditionTrue(1, input_condition=-1)
    IfInsideMap(1, game_map=KILN_OF_THE_FIRST_FLAME)
    IfFlagOn(1, 825)
    IfConditionTrue(0, input_condition=1)
    DisableFlag(825)
    PlayCutscene(
        180051,
        skippable=True,
        fade_out=False,
        player_id=PLAYER,
        move_to_region=m16_00_Boxes.ArrivalFromKiln,
        move_to_map=NEW_LONDO_RUINS,
    )
    PlayCutscene(160050, skippable=True, fade_out=False, player_id=PLAYER)
    WaitFrames(1)
    DisableCharacter(Characters.c5330_0017)
    DisableFlag(831)
    Restart()


def Event11805029():
    """ 11805029: Event 11805029 """
    SkipLinesIfClient(1)
    SetNetworkUpdateAuthority(Characters.c0000_0002, UpdateAuthority.Forced)
    SkipLinesIfFlagOn(3, 11805033)
    IfClient(2)
    IfFlagOn(2, 11805031)
    SkipLinesIfConditionTrue(1, 2)
    DisableCharacter(Characters.c0000_0002)
    EndIfFlagOn(15)
    IfMultiplayerCount(1, arg1=4, arg2=3)
    IfHost(1)
    IfCharacterHuman(1, PLAYER)
    IfFlagOff(1, 11805031)
    IfFlagOff(1, 11805033)
    IfFlagOn(1, 1012)
    IfCharacterBackreadEnabled(1, Characters.c0000_0002)
    IfEntityWithinDistance(1, Characters.c0000_0002, PLAYER, radius=30.0)
    IfCharacterHasSpecialEffect(1, PLAYER, 28)
    IfConditionTrue(0, input_condition=1)
    PlaceSummonSign(
        SummonSignType.BlueEyeSign,
        Characters.c0000_0002,
        region=Points.SolaireSummonSign,
        summon_flag=11805031,
        dismissal_flag=11805033,
    )


def Event11805990(_, arg_0_3: int, arg_4_7: int):
    """ 11805990: Event 11805990 """
    IfFlagOn(0, arg_0_3)
    EraseNPCSummonSign(summoned_character=arg_4_7)
    IfFlagOff(0, arg_0_3)
    Restart()


def Event11805030():
    """ 11805030: Event 11805030 """
    SkipLinesIfClient(1)
    SetNetworkUpdateAuthority(Characters.c0000_0002, UpdateAuthority.Forced)
    SkipLinesIfFlagOn(3, 11805033)
    IfClient(2)
    IfFlagOn(2, 11805031)
    SkipLinesIfConditionTrue(1, 2)
    DisableCharacter(Characters.c0000_0002)
    EndIfFlagOn(15)
    IfHost(1)
    IfCharacterHuman(1, PLAYER)
    IfFlagOn(1, 1012)
    IfCharacterBackreadEnabled(1, Characters.c0000_0002)
    IfEntityWithinDistance(1, Characters.c0000_0002, PLAYER, radius=30.0)
    IfConditionTrue(0, input_condition=1)
    PlaceSummonSign(
        SummonSignType.BlueEyeSign,
        Characters.c0000_0002,
        region=Points.SolaireSummonSign,
        summon_flag=11805031,
        dismissal_flag=11805033,
    )


def Event11805032():
    """ 11805032: Event 11805032 """
    EndIfThisEventOn()
    IfFlagOn(1, 11805031)
    IfFlagOn(1, 11805393)
    IfConditionTrue(0, input_condition=1)
    AICommand(Characters.c0000_0002, command_id=10, slot=0)
    ReplanAI(Characters.c0000_0002)
    IfEntityWithinDistance(0, Characters.c0000_0002, Objects.o8050_0000, radius=1.5)
    RotateToFaceEntity(Characters.c0000_0002, Boxes.GwynFogRotationTarget)
    ForceAnimation(Characters.c0000_0002, 7410)
    AICommand(Characters.c0000_0002, command_id=-1, slot=0)
    ReplanAI(Characters.c0000_0002)


@RestartOnRest
def Event11805200():
    """ 11805200: Event 11805200 """
    DisableAI(1800999)
    IfMovingOnCollision(1, 1803000)
    IfRunningOnCollision(2, 1803000)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionTrue(2, 2)
    RequestAnimation(1800999, 1750, loop=False, wait_for_completion=True)
    Restart()
    RequestAnimation(1800999, 2000, loop=False, wait_for_completion=True)
    Restart()


@RestartOnRest
def PatchesAmbush():
    """ 11802000: Patches teleports behind the player and attacks. """
    DisableCharacter(Characters.c0000_PatchesAmbush)

    Await(InsideMap(KILN_OF_THE_FIRST_FLAME) and TriggerFlags.PatchesAmbush and IsAlive(Characters.c0000_PatchesAmbush))
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
    """ 11802001: Channeler teleports above the player (no gravity) and uses its buff dance. """
    DisableCharacter(Characters.c2370_TrollChanneler)

    Await(InsideMap(KILN_OF_THE_FIRST_FLAME) and TriggerFlags.ChannelerAmbush and IsAlive(Characters.c2370_TrollChanneler))
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

    AddSpecialEffect(6544, 5470)
    AddSpecialEffect(1800960, 5470)
    AddSpecialEffect(1800200, 5470)
    AddSpecialEffect(1800201, 5470)
    AddSpecialEffect(1800202, 5470)
    AddSpecialEffect(1800203, 5470)
    AddSpecialEffect(1800204, 5470)
    AddSpecialEffect(1800900, 5470)
    AddSpecialEffect(1800901, 5470)
    AddSpecialEffect(1800902, 5470)
    AddSpecialEffect(1800903, 5470)
    AddSpecialEffect(1800904, 5470)
    AddSpecialEffect(1800100, 5470)
    AddSpecialEffect(1800101, 5470)
    AddSpecialEffect(1800102, 5470)
    AddSpecialEffect(1800103, 5470)
    AddSpecialEffect(1800104, 5470)
    AddSpecialEffect(1800105, 5470)
    AddSpecialEffect(1803900, 5470)
    AddSpecialEffect(1803901, 5470)
    AddSpecialEffect(1803902, 5470)
    AddSpecialEffect(6331, 5470)
    AddSpecialEffect(6341, 5470)
    AddSpecialEffect(1800800, 5470)

    return RESTART


@RestartOnRest
def RedPhantomAmbush():
    """ 11802002: Random red phantom ambushes the player. """
    DisableCharacter(Characters.c2790_0006)
    DisableCharacter(Characters.c2790_0007)
    DisableCharacter(Characters.c2790_0008)
    DisableCharacter(Characters.c2790_0009)
    DisableCharacter(Characters.c2790_0010)

    Await(InsideMap(KILN_OF_THE_FIRST_FLAME) and TriggerFlags.EnemyAmbush)
    DisableFlag(TriggerFlags.EnemyAmbush)

    DisableFlagRange((11812900, 11812999))
    EnableRandomFlagInRange((11812900, 11812904))

    if FlagEnabled(11812900):
        ControlRedPhantom(0, Characters.c2790_0006)
    elif FlagEnabled(11812901):
        ControlRedPhantom(0, Characters.c2790_0007)
    elif FlagEnabled(11812902):
        ControlRedPhantom(0, Characters.c2790_0008)
    elif FlagEnabled(11812903):
        ControlRedPhantom(0, Characters.c2790_0009)
    elif FlagEnabled(11812904):
        ControlRedPhantom(0, Characters.c2790_0010)
    
    Await(FlagEnabled(11805082))

    return RESTART


@RestartOnRest
def ControlRedPhantom(_, enemy: int):
    """ 11805081: `enemy` moves to player and appears. """
    DisableFlag(11805082)
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
    EnableFlag(11805082)


def MakeWorldInvisible():
    """ 11802003: Disable all map pieces. Undone only by reload. """
    Await(TriggerFlags.InvisibleWorld)   # note you don't need to be standing in the map
    DisableFlag(TriggerFlags.InvisibleWorld)
    for map_piece in range(1808500, 1808514):
        DisableMapPiece(map_piece)
    # No need to restart.


@RestartOnRest
def OopsAllGwyns():
    """ 11802004: Enable Gwyns and warp them to their paired normal characters. """
    DisableCharacter(1800600)
    DisableCharacter(1800601)
    DisableCharacter(1800602)
    Await(TriggerFlags.OopsAllGwyns)  # note you don't need to be standing in the map
    DisableCharacter(6544)
    EnableCharacter(1800600)
    DisableCharacter(1800203)
    EnableCharacter(1800601)
    DisableCharacter(1800103)
    EnableCharacter(1800602)
    WaitFrames(30)  # enough time for other maps to trigger too
    DisableFlag(TriggerFlags.OopsAllGwyns)
    # No need to restart.


@RestartOnRest
def OopsAllBonewheels():
    """ 11802005: Enable Bonewheels and warp them to their paired normal characters. """
    DisableCharacter(1800400)
    DisableCharacter(1800401)
    DisableCharacter(1800402)
    DisableCharacter(1800403)
    DisableCharacter(1800404)
    DisableCharacter(1800405)
    DisableCharacter(1800406)
    DisableCharacter(1800407)
    DisableCharacter(1800408)
    DisableCharacter(1800409)
    DisableCharacter(1800410)
    DisableCharacter(1800411)
    DisableCharacter(1800412)
    DisableCharacter(1800413)
    Await(TriggerFlags.OopsAllBonewheels)  # note you don't need to be standing in the map
    DisableCharacter(6544)
    EnableCharacter(1800400)
    DisableCharacter(1800200)
    EnableCharacter(1800401)
    DisableCharacter(1800201)
    EnableCharacter(1800402)
    DisableCharacter(1800202)
    EnableCharacter(1800403)
    DisableCharacter(1800203)
    EnableCharacter(1800404)
    DisableCharacter(1800204)
    EnableCharacter(1800405)
    DisableCharacter(1800100)
    EnableCharacter(1800406)
    DisableCharacter(1800101)
    EnableCharacter(1800407)
    DisableCharacter(1800102)
    EnableCharacter(1800408)
    DisableCharacter(1800103)
    EnableCharacter(1800409)
    DisableCharacter(1800104)
    EnableCharacter(1800410)
    DisableCharacter(1800105)
    EnableCharacter(1800411)
    DisableCharacter(6331)
    EnableCharacter(1800412)
    DisableCharacter(6341)
    EnableCharacter(1800413)
    WaitFrames(30)  # enough time for other maps to trigger too
    DisableFlag(TriggerFlags.OopsAllBonewheels)
    # No need to restart.


@RestartOnRest
def HyperAggression():
    """ 11802006: Switch AI param of every enemy to its aggressive version. """
    Await(TriggerFlags.HyperAggression or TriggerFlags.HyperAggressionReTrigger)
    
    SetAIParamID(1800200, 279050)
    SetAIParamID(1800201, 279051)
    SetAIParamID(1800202, 279050)
    SetAIParamID(1800203, 279052)
    SetAIParamID(1800204, 279054)
    SetAIParamID(1800900, 279051)
    SetAIParamID(1800901, 279052)
    SetAIParamID(1800902, 279053)
    SetAIParamID(1800903, 279050)
    SetAIParamID(1800904, 279051)
    SetAIParamID(1800100, 279150)
    SetAIParamID(1800101, 279150)
    SetAIParamID(1800102, 279150)
    SetAIParamID(1800103, 279150)
    SetAIParamID(1800104, 279150)
    SetAIParamID(1800105, 279150)
    SetAIParamID(1803900, 349050)
    SetAIParamID(1803901, 349150)
    SetAIParamID(1803902, 349150)
    SetAIParamID(1800800, 537050)
    SetAIParamID(1800600, 537050)
    SetAIParamID(1800601, 537050)
    SetAIParamID(1800602, 537050)
    SetAIParamID(1800400, 293050)
    SetAIParamID(1800401, 293050)
    SetAIParamID(1800402, 293050)
    SetAIParamID(1800403, 293050)
    SetAIParamID(1800404, 293050)
    SetAIParamID(1800405, 293050)
    SetAIParamID(1800406, 293050)
    SetAIParamID(1800407, 293050)
    SetAIParamID(1800408, 293050)
    SetAIParamID(1800409, 293050)
    SetAIParamID(1800410, 293050)
    SetAIParamID(1800411, 293050)
    SetAIParamID(1800412, 293050)
    SetAIParamID(1800413, 293050)
        
    # Common EMEVD manages the flags that control this event.
    Await(not TriggerFlags.HyperAggressionReTrigger)
    
    SetAIParamID(1800200, 279000)
    SetAIParamID(1800201, 279001)
    SetAIParamID(1800202, 279000)
    SetAIParamID(1800203, 279002)
    SetAIParamID(1800204, 279004)
    SetAIParamID(1800900, 279001)
    SetAIParamID(1800901, 279002)
    SetAIParamID(1800902, 279003)
    SetAIParamID(1800903, 279000)
    SetAIParamID(1800904, 279001)
    SetAIParamID(1800100, 279100)
    SetAIParamID(1800101, 279100)
    SetAIParamID(1800102, 279100)
    SetAIParamID(1800103, 279100)
    SetAIParamID(1800104, 279100)
    SetAIParamID(1800105, 279100)
    SetAIParamID(1803900, 349000)
    SetAIParamID(1803901, 349100)
    SetAIParamID(1803902, 349100)
    SetAIParamID(1800800, 537000)
    SetAIParamID(1800600, 537000)
    SetAIParamID(1800601, 537000)
    SetAIParamID(1800602, 537000)
    SetAIParamID(1800400, 293000)
    SetAIParamID(1800401, 293000)
    SetAIParamID(1800402, 293000)
    SetAIParamID(1800403, 293000)
    SetAIParamID(1800404, 293000)
    SetAIParamID(1800405, 293000)
    SetAIParamID(1800406, 293000)
    SetAIParamID(1800407, 293000)
    SetAIParamID(1800408, 293000)
    SetAIParamID(1800409, 293000)
    SetAIParamID(1800410, 293000)
    SetAIParamID(1800411, 293000)
    SetAIParamID(1800412, 293000)
    SetAIParamID(1800413, 293000)
    
    return RESTART


@RestartOnRest
def EnemySpeedUp():
    """ 11802200: Temporary enemy effect. """
    Await(TriggerFlags.EnemySpeedUp)
    AddSpecialEffect(6544, 200000)
    AddSpecialEffect(1800960, 200000)
    AddSpecialEffect(1800200, 200000)
    AddSpecialEffect(1800201, 200000)
    AddSpecialEffect(1800202, 200000)
    AddSpecialEffect(1800203, 200000)
    AddSpecialEffect(1800204, 200000)
    AddSpecialEffect(1800900, 200000)
    AddSpecialEffect(1800901, 200000)
    AddSpecialEffect(1800902, 200000)
    AddSpecialEffect(1800903, 200000)
    AddSpecialEffect(1800904, 200000)
    AddSpecialEffect(1800100, 200000)
    AddSpecialEffect(1800101, 200000)
    AddSpecialEffect(1800102, 200000)
    AddSpecialEffect(1800103, 200000)
    AddSpecialEffect(1800104, 200000)
    AddSpecialEffect(1800105, 200000)
    AddSpecialEffect(1803900, 200000)
    AddSpecialEffect(1803901, 200000)
    AddSpecialEffect(1803902, 200000)
    AddSpecialEffect(6331, 200000)
    AddSpecialEffect(6341, 200000)
    AddSpecialEffect(1800800, 200000)
    WaitFrames(10)  # give other loaded maps time to trigger
    DisableFlag(TriggerFlags.EnemySpeedUp)
    return RESTART


@RestartOnRest
def EnemyExtremeSpeedUp():
    """ 11802201: Temporary enemy effect. """
    Await(TriggerFlags.EnemyExtremeSpeedUp)
    AddSpecialEffect(6544, 200001)
    AddSpecialEffect(1800960, 200001)
    AddSpecialEffect(1800200, 200001)
    AddSpecialEffect(1800201, 200001)
    AddSpecialEffect(1800202, 200001)
    AddSpecialEffect(1800203, 200001)
    AddSpecialEffect(1800204, 200001)
    AddSpecialEffect(1800900, 200001)
    AddSpecialEffect(1800901, 200001)
    AddSpecialEffect(1800902, 200001)
    AddSpecialEffect(1800903, 200001)
    AddSpecialEffect(1800904, 200001)
    AddSpecialEffect(1800100, 200001)
    AddSpecialEffect(1800101, 200001)
    AddSpecialEffect(1800102, 200001)
    AddSpecialEffect(1800103, 200001)
    AddSpecialEffect(1800104, 200001)
    AddSpecialEffect(1800105, 200001)
    AddSpecialEffect(1803900, 200001)
    AddSpecialEffect(1803901, 200001)
    AddSpecialEffect(1803902, 200001)
    AddSpecialEffect(6331, 200001)
    AddSpecialEffect(6341, 200001)
    AddSpecialEffect(1800800, 200001)
    WaitFrames(10)  # give other loaded maps time to trigger
    DisableFlag(TriggerFlags.EnemyExtremeSpeedUp)
    return RESTART


@RestartOnRest
def EnemySpeedDown():
    """ 11802202: Temporary enemy effect. """
    Await(TriggerFlags.EnemySpeedDown)
    AddSpecialEffect(6544, 200002)
    AddSpecialEffect(1800960, 200002)
    AddSpecialEffect(1800200, 200002)
    AddSpecialEffect(1800201, 200002)
    AddSpecialEffect(1800202, 200002)
    AddSpecialEffect(1800203, 200002)
    AddSpecialEffect(1800204, 200002)
    AddSpecialEffect(1800900, 200002)
    AddSpecialEffect(1800901, 200002)
    AddSpecialEffect(1800902, 200002)
    AddSpecialEffect(1800903, 200002)
    AddSpecialEffect(1800904, 200002)
    AddSpecialEffect(1800100, 200002)
    AddSpecialEffect(1800101, 200002)
    AddSpecialEffect(1800102, 200002)
    AddSpecialEffect(1800103, 200002)
    AddSpecialEffect(1800104, 200002)
    AddSpecialEffect(1800105, 200002)
    AddSpecialEffect(1803900, 200002)
    AddSpecialEffect(1803901, 200002)
    AddSpecialEffect(1803902, 200002)
    AddSpecialEffect(6331, 200002)
    AddSpecialEffect(6341, 200002)
    AddSpecialEffect(1800800, 200002)
    WaitFrames(10)  # give other loaded maps time to trigger
    DisableFlag(TriggerFlags.EnemySpeedDown)
    return RESTART


@RestartOnRest
def EnemyExtremeSpeedDown():
    """ 11802203: Temporary enemy effect. """
    Await(TriggerFlags.EnemyExtremeSpeedDown)
    AddSpecialEffect(6544, 200003)
    AddSpecialEffect(1800960, 200003)
    AddSpecialEffect(1800200, 200003)
    AddSpecialEffect(1800201, 200003)
    AddSpecialEffect(1800202, 200003)
    AddSpecialEffect(1800203, 200003)
    AddSpecialEffect(1800204, 200003)
    AddSpecialEffect(1800900, 200003)
    AddSpecialEffect(1800901, 200003)
    AddSpecialEffect(1800902, 200003)
    AddSpecialEffect(1800903, 200003)
    AddSpecialEffect(1800904, 200003)
    AddSpecialEffect(1800100, 200003)
    AddSpecialEffect(1800101, 200003)
    AddSpecialEffect(1800102, 200003)
    AddSpecialEffect(1800103, 200003)
    AddSpecialEffect(1800104, 200003)
    AddSpecialEffect(1800105, 200003)
    AddSpecialEffect(1803900, 200003)
    AddSpecialEffect(1803901, 200003)
    AddSpecialEffect(1803902, 200003)
    AddSpecialEffect(6331, 200003)
    AddSpecialEffect(6341, 200003)
    AddSpecialEffect(1800800, 200003)
    WaitFrames(10)  # give other loaded maps time to trigger
    DisableFlag(TriggerFlags.EnemyExtremeSpeedDown)
    return RESTART


@RestartOnRest
def EnemyHealthRegain():
    """ 11802204: Temporary enemy effect. """
    Await(TriggerFlags.EnemyHealthRegain)
    AddSpecialEffect(6544, 200004)
    AddSpecialEffect(1800960, 200004)
    AddSpecialEffect(1800200, 200004)
    AddSpecialEffect(1800201, 200004)
    AddSpecialEffect(1800202, 200004)
    AddSpecialEffect(1800203, 200004)
    AddSpecialEffect(1800204, 200004)
    AddSpecialEffect(1800900, 200004)
    AddSpecialEffect(1800901, 200004)
    AddSpecialEffect(1800902, 200004)
    AddSpecialEffect(1800903, 200004)
    AddSpecialEffect(1800904, 200004)
    AddSpecialEffect(1800100, 200004)
    AddSpecialEffect(1800101, 200004)
    AddSpecialEffect(1800102, 200004)
    AddSpecialEffect(1800103, 200004)
    AddSpecialEffect(1800104, 200004)
    AddSpecialEffect(1800105, 200004)
    AddSpecialEffect(1803900, 200004)
    AddSpecialEffect(1803901, 200004)
    AddSpecialEffect(1803902, 200004)
    AddSpecialEffect(6331, 200004)
    AddSpecialEffect(6341, 200004)
    AddSpecialEffect(1800800, 200004)
    WaitFrames(10)  # give other loaded maps time to trigger
    DisableFlag(TriggerFlags.EnemyHealthRegain)
    return RESTART


@RestartOnRest
def EnemyMaxHealthUp():
    """ 11802205: Temporary enemy effect. """
    Await(TriggerFlags.EnemyMaxHealthUp)
    AddSpecialEffect(6544, 200005)
    AddSpecialEffect(1800960, 200005)
    AddSpecialEffect(1800200, 200005)
    AddSpecialEffect(1800201, 200005)
    AddSpecialEffect(1800202, 200005)
    AddSpecialEffect(1800203, 200005)
    AddSpecialEffect(1800204, 200005)
    AddSpecialEffect(1800900, 200005)
    AddSpecialEffect(1800901, 200005)
    AddSpecialEffect(1800902, 200005)
    AddSpecialEffect(1800903, 200005)
    AddSpecialEffect(1800904, 200005)
    AddSpecialEffect(1800100, 200005)
    AddSpecialEffect(1800101, 200005)
    AddSpecialEffect(1800102, 200005)
    AddSpecialEffect(1800103, 200005)
    AddSpecialEffect(1800104, 200005)
    AddSpecialEffect(1800105, 200005)
    AddSpecialEffect(1803900, 200005)
    AddSpecialEffect(1803901, 200005)
    AddSpecialEffect(1803902, 200005)
    AddSpecialEffect(6331, 200005)
    AddSpecialEffect(6341, 200005)
    AddSpecialEffect(1800800, 200005)
    WaitFrames(10)  # give other loaded maps time to trigger
    DisableFlag(TriggerFlags.EnemyMaxHealthUp)
    return RESTART


@RestartOnRest
def EnemyMaxHealthDown():
    """ 11802206: Temporary enemy effect. """
    Await(TriggerFlags.EnemyMaxHealthDown)
    AddSpecialEffect(6544, 200006)
    AddSpecialEffect(1800960, 200006)
    AddSpecialEffect(1800200, 200006)
    AddSpecialEffect(1800201, 200006)
    AddSpecialEffect(1800202, 200006)
    AddSpecialEffect(1800203, 200006)
    AddSpecialEffect(1800204, 200006)
    AddSpecialEffect(1800900, 200006)
    AddSpecialEffect(1800901, 200006)
    AddSpecialEffect(1800902, 200006)
    AddSpecialEffect(1800903, 200006)
    AddSpecialEffect(1800904, 200006)
    AddSpecialEffect(1800100, 200006)
    AddSpecialEffect(1800101, 200006)
    AddSpecialEffect(1800102, 200006)
    AddSpecialEffect(1800103, 200006)
    AddSpecialEffect(1800104, 200006)
    AddSpecialEffect(1800105, 200006)
    AddSpecialEffect(1803900, 200006)
    AddSpecialEffect(1803901, 200006)
    AddSpecialEffect(1803902, 200006)
    AddSpecialEffect(6331, 200006)
    AddSpecialEffect(6341, 200006)
    AddSpecialEffect(1800800, 200006)
    WaitFrames(10)  # give other loaded maps time to trigger
    DisableFlag(TriggerFlags.EnemyMaxHealthDown)
    return RESTART


@RestartOnRest
def EnemyDefenseUp():
    """ 11802207: Temporary enemy effect. """
    Await(TriggerFlags.EnemyDefenseUp)
    AddSpecialEffect(6544, 200007)
    AddSpecialEffect(1800960, 200007)
    AddSpecialEffect(1800200, 200007)
    AddSpecialEffect(1800201, 200007)
    AddSpecialEffect(1800202, 200007)
    AddSpecialEffect(1800203, 200007)
    AddSpecialEffect(1800204, 200007)
    AddSpecialEffect(1800900, 200007)
    AddSpecialEffect(1800901, 200007)
    AddSpecialEffect(1800902, 200007)
    AddSpecialEffect(1800903, 200007)
    AddSpecialEffect(1800904, 200007)
    AddSpecialEffect(1800100, 200007)
    AddSpecialEffect(1800101, 200007)
    AddSpecialEffect(1800102, 200007)
    AddSpecialEffect(1800103, 200007)
    AddSpecialEffect(1800104, 200007)
    AddSpecialEffect(1800105, 200007)
    AddSpecialEffect(1803900, 200007)
    AddSpecialEffect(1803901, 200007)
    AddSpecialEffect(1803902, 200007)
    AddSpecialEffect(6331, 200007)
    AddSpecialEffect(6341, 200007)
    AddSpecialEffect(1800800, 200007)
    WaitFrames(10)  # give other loaded maps time to trigger
    DisableFlag(TriggerFlags.EnemyDefenseUp)
    return RESTART
