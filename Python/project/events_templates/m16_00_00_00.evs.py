"""
linked:


strings:

"""
from soulstruct.darksouls1r.events import *
from ..entities.m16_00_00_00_entities import *
from ..entities.m10_02_00_00_entities import Objects as m10_02_Objects
from ..entities.m18_00_00_00_entities import Boxes as m18_00_Boxes, Characters as m18_00_Characters
from ..entities.common_entities import *


def Constructor():
    """ 0: Event 0 """
    SkipLinesIfFlagOff(1, 13)
    RegisterBonfire(
        11600920,
        obj=Objects.o0200_0001,
        reaction_distance=2.0,
        reaction_angle=180.0,
        initial_kindle_level=0,
    )
    RegisterBonfire(
        11600984,
        obj=Objects.o0200_0002,
        reaction_distance=2.0,
        reaction_angle=180.0,
        initial_kindle_level=0,
    )
    RegisterLadder(start_climbing_flag=11600010, stop_climbing_flag=11600011, obj=Objects.o6400_0000)
    RegisterLadder(start_climbing_flag=11600012, stop_climbing_flag=11600013, obj=Objects.o6401_0000)
    EnableFlag(11600102)
    SkipLinesIfClient(7)
    EnableFlag(404)
    DisableObject(Objects.o6601_0000)
    DeleteVFX(VFX.MultiplayerFog1, erase_root_only=False)
    DisableObject(Objects.o6602_0000)
    DeleteVFX(VFX.MultiplayerFog2, erase_root_only=False)
    DisableObject(Objects.o6603_0000)
    DeleteVFX(VFX.MultiplayerFog3, erase_root_only=False)
    DisableSpawner(Spawners.FourKingsSpawner)
    RunEvent(
        11600090,
        slot=0,
        args=(Objects.o6604_0000, VFX.CheckpointFog1, Boxes.CheckpointFog1FrontSide, Boxes.CheckpointFog1BackSide),
    )
    RunEvent(
        11600090,
        slot=1,
        args=(Objects.o6605_0000, VFX.CheckpointFog2, Boxes.CheckpointFog2FrontSide, Boxes.CheckpointFog2BackSide),
    )
    RunEvent(11605100)
    RunEvent(11600150)
    RunEvent(11600100)
    RunEvent(11600101, slot=0, args=(Objects.o6110_0000, 11600102, 0))
    RunEvent(11600110, slot=0, args=(11600110, 10010872, Objects.o6010_0001))
    RunEvent(11600120, slot=0, args=(11600120, 10010867, Objects.o6010_0000, 10010883, 2008))
    RunEvent(11600160)
    RunEvent(11600200)
    RunEvent(11600250)
    RunEvent(11600199)
    RunEvent(11600210)
    RunEvent(11600251)
    RunEvent(11600220)
    RunEvent(11600252)
    RunEvent(11600230)
    RunEvent(11600253)
    RunEvent(11600810)
    RunEvent(11600400)
    RunEvent(11605397)
    RunEvent(11605398)
    RunEvent(11605360, slot=0, args=(10000,))
    RunEvent(11605360, slot=1, args=(10001,))
    RunEvent(11605360, slot=2, args=(10002,))
    RunEvent(11605360, slot=3, args=(10003,))
    RunEvent(11605360, slot=4, args=(10004,))
    RunEvent(11605360, slot=5, args=(10005,))
    DisableSoundEvent(1603800)
    SkipLinesIfFlagOff(4, 13)
    RunEvent(11605392)
    DisableObject(Objects.o6606_0000)
    DeleteVFX(VFX.FourKingsEntranceFog, erase_root_only=False)
    SkipLines(13)
    RunEvent(11605390)
    RunEvent(11605391)
    RunEvent(11605393)
    RunEvent(11605392)
    RunEvent(11600001)
    RunEvent(11605394)
    RunEvent(11605395)
    RunEvent(11605396)
    RunEvent(11605350, slot=0, args=(Characters.c5390_0001,))
    RunEvent(11605350, slot=1, args=(Characters.c5390_0002,))
    RunEvent(11605350, slot=2, args=(Characters.c5390_0003,))
    RunEvent(11605350, slot=3, args=(Characters.c5390_0004,))
    RunEvent(11605399)
    DisableSoundEvent(1603801)
    RunEvent(11605150, slot=0, args=(Characters.c2670_0004, Boxes.MaleGhostCombatArea1))
    RunEvent(11605150, slot=1, args=(Characters.c2670_0016, Boxes.MaleGhostCombatArea1))
    RunEvent(11605150, slot=2, args=(Characters.c2670_0003, Boxes.MaleGhostCombatArea1))
    RunEvent(11605150, slot=3, args=(Characters.c2670_0031, Boxes.MaleGhostCombatArea1))
    RunEvent(11605150, slot=4, args=(Characters.c2670_0002, Boxes.MaleGhostCombatArea1))
    RunEvent(11605150, slot=5, args=(Characters.c2670_0020, Boxes.MaleGhostCombatArea1))
    RunEvent(11605150, slot=6, args=(Characters.c2670_0021, Boxes.MaleGhostCombatArea1))
    RunEvent(11605150, slot=7, args=(Characters.c2670_0022, Boxes.MaleGhostCombatArea1))
    RunEvent(11605150, slot=8, args=(Characters.c2670_0012, Boxes.MaleGhostCombatArea2))
    RunEvent(11605150, slot=9, args=(Characters.c2670_0013, Boxes.MaleGhostCombatArea2))
    RunEvent(11605150, slot=10, args=(Characters.c2670_0014, Boxes.MaleGhostCombatArea2))
    RunEvent(11605150, slot=11, args=(Characters.c2670_0008, Boxes.MaleGhostCombatArea3))
    RunEvent(11605150, slot=12, args=(Characters.c2670_0007, Boxes.MaleGhostCombatArea3))
    RunEvent(11605150, slot=13, args=(Characters.c2670_0015, Boxes.MaleGhostCombatArea3))
    RunEvent(11605150, slot=14, args=(Characters.c2670_0026, Boxes.MaleGhostCombatArea3))
    RunEvent(11605150, slot=15, args=(Characters.c2670_0027, Boxes.MaleGhostCombatArea3))
    RunEvent(11605150, slot=16, args=(Characters.c2670_0010, Boxes.MaleGhostCombatArea3))
    RunEvent(11605150, slot=17, args=(Characters.c2670_0011, Boxes.MaleGhostCombatArea3))
    RunEvent(11605150, slot=18, args=(Characters.c2670_0005, Boxes.MaleGhostCombatArea3))
    RunEvent(11605150, slot=19, args=(Characters.c2670_0006, Boxes.MaleGhostCombatArea3))
    RunEvent(11605150, slot=20, args=(Characters.c2670_0009, Boxes.MaleGhostCombatArea3))
    RunEvent(11605150, slot=21, args=(Characters.c2670_0025, Boxes.MaleGhostCombatArea3))
    RunEvent(11605150, slot=22, args=(Characters.c2670_0000, Boxes.MaleGhostCombatArea4))
    RunEvent(11605150, slot=23, args=(Characters.c2670_0017, Boxes.MaleGhostCombatArea4))
    RunEvent(11605150, slot=24, args=(Characters.c2670_0001, Boxes.MaleGhostCombatArea4))
    RunEvent(11605150, slot=25, args=(Characters.c2670_0018, Boxes.MaleGhostCombatArea4))
    RunEvent(11605150, slot=26, args=(Characters.c2670_0019, Boxes.MaleGhostCombatArea4))
    RunEvent(11605150, slot=27, args=(Characters.c2670_0029, Boxes.MaleGhostCombatArea4))
    RunEvent(11605150, slot=28, args=(Characters.c2670_0030, Boxes.MaleGhostCombatArea4))
    RunEvent(11605150, slot=29, args=(Characters.c2670_0023, Boxes.MaleGhostCombatArea5))
    RunEvent(11605150, slot=30, args=(Characters.c2670_0024, Boxes.MaleGhostCombatArea5))
    RunEvent(11605150, slot=31, args=(Characters.c2670_0028, Boxes.MaleGhostCombatArea5))
    RunEvent(11605150, slot=32, args=(Characters.c2680_0001, Boxes.FemaleGhostCombatArea))
    RunEvent(11605150, slot=33, args=(Characters.c2680_0000, Boxes.FemaleGhostCombatArea))
    RunEvent(11605001, slot=0, args=(Characters.c2670_0008, 5.0, 9060), arg_types="ifi")
    RunEvent(11605001, slot=1, args=(Characters.c2670_0007, 5.0, 9060), arg_types="ifi")
    RunEvent(11605001, slot=2, args=(Characters.c2670_0004, 7.0, 9060), arg_types="ifi")
    RunEvent(11605001, slot=3, args=(Characters.c2670_0001, 7.0, 9060), arg_types="ifi")
    RunEvent(11605001, slot=4, args=(Characters.c2670_0016, 6.0, 9060), arg_types="ifi")
    RunEvent(11605001, slot=5, args=(Characters.c2670_0003, 6.0, 9060), arg_types="ifi")
    RunEvent(11605001, slot=6, args=(Characters.c2670_0015, 3.0, 9060), arg_types="ifi")
    RunEvent(11605001, slot=7, args=(Characters.c2670_0030, 5.0, 9060), arg_types="ifi")
    RunEvent(11605050, slot=0, args=(Characters.c2670_0022, Boxes.GhostAttackArea0, 3007, 0, 0.0), arg_types="iiiif")
    RunEvent(11605050, slot=1, args=(Characters.c2670_0026, Boxes.GhostAttackArea1, 3007, 0, 0.0), arg_types="iiiif")
    RunEvent(11605050, slot=2, args=(Characters.c2670_0012, Boxes.GhostAttackArea2, 3006, 1, 5.0), arg_types="iiiif")
    RunEvent(11605050, slot=3, args=(Characters.c2670_0013, Boxes.GhostAttackArea3, 3006, 1, 5.0), arg_types="iiiif")
    RunEvent(11605050, slot=4, args=(Characters.c2670_0027, Boxes.GhostAttackArea4, 3005, 0, 0.0), arg_types="iiiif")
    RunEvent(11605050, slot=5, args=(Characters.c2670_0014, Boxes.GhostAttackArea5, 3005, 0, 0.0), arg_types="iiiif")
    RunEvent(11605050, slot=6, args=(Characters.c2670_0018, Boxes.GhostAppearArea0, 9060, 0, 0.0), arg_types="iiiif")
    RunEvent(11605050, slot=7, args=(Characters.c2670_0019, Boxes.GhostAppearArea0, 9060, 0, 0.0), arg_types="iiiif")
    RunEvent(11605050, slot=8, args=(Characters.c2670_0029, Boxes.GhostAppearArea0, 9060, 0, 0.0), arg_types="iiiif")
    RunEvent(11605050, slot=9, args=(Characters.c2670_0031, Boxes.GhostAppearArea1, 9060, 0, 0.0), arg_types="iiiif")
    RunEvent(11605200, slot=0, args=(Characters.c3500_0000, Characters.c3501_0000, 1, 11600100))
    RunEvent(11605200, slot=1, args=(Characters.c3500_0000, Characters.c3501_0001, 2, 11605200))
    RunEvent(11605200, slot=2, args=(Characters.c3500_0000, Characters.c3501_0002, 3, 11605201))
    RunEvent(11605200, slot=3, args=(Characters.c3500_0000, Characters.c3501_0003, 4, 11605202))
    RunEvent(11605200, slot=4, args=(Characters.c3500_0000, Characters.c3501_0004, 5, 11605203))
    RunEvent(11605200, slot=5, args=(Characters.c3500_0000, Characters.c3501_0005, 6, 11605204))
    RunEvent(11605200, slot=10, args=(Characters.c3500_0001, Characters.c3501_0006, 1, 11600100))
    RunEvent(11605200, slot=11, args=(Characters.c3500_0001, Characters.c3501_0007, 2, 11605210))
    RunEvent(11605200, slot=12, args=(Characters.c3500_0001, Characters.c3501_0008, 3, 11605211))
    RunEvent(11605200, slot=13, args=(Characters.c3500_0001, Characters.c3501_0009, 4, 11605212))
    RunEvent(11605200, slot=14, args=(Characters.c3500_0001, Characters.c3501_0010, 5, 11605213))
    RunEvent(11605200, slot=15, args=(Characters.c3500_0001, Characters.c3501_0011, 6, 11605214))
    RunEvent(11605250, slot=0, args=(Characters.c3501_0000,))
    RunEvent(11605250, slot=1, args=(Characters.c3501_0001,))
    RunEvent(11605250, slot=2, args=(Characters.c3501_0002,))
    RunEvent(11605250, slot=3, args=(Characters.c3501_0003,))
    RunEvent(11605250, slot=4, args=(Characters.c3501_0004,))
    RunEvent(11605250, slot=5, args=(Characters.c3501_0005,))
    RunEvent(11605250, slot=6, args=(Characters.c3501_0006,))
    RunEvent(11605250, slot=7, args=(Characters.c3501_0007,))
    RunEvent(11605250, slot=8, args=(Characters.c3501_0008,))
    RunEvent(11605250, slot=9, args=(Characters.c3501_0009,))
    RunEvent(11605250, slot=10, args=(Characters.c3501_0010,))
    RunEvent(11605250, slot=11, args=(Characters.c3501_0011,))
    RunEvent(11600850, slot=0, args=(Characters.c3500_0000,))
    RunEvent(11600850, slot=1, args=(Characters.c3500_0001,))
    RunEvent(11600600, slot=0, args=(Objects.o0110_0000, 11600600))
    RunEvent(11600600, slot=1, args=(Objects.o0110_0001, 11600601))
    RunEvent(11600600, slot=2, args=(Objects.o0110_0002, 11600602))
    RunEvent(11600650, slot=0, args=(Objects.o0500_0003, Objects.o6450_0003))
    RunEvent(11600650, slot=1, args=(Objects.o0500_0004, Objects.o6450_0009))
    RunEvent(
        11605843,
        slot=0,
        args=(13, Objects.o6606_0000, Boxes.FourKingsFogPrompt, Boxes.FourKingsFogRotationTarget),
    )
    RunEvent(11605846, slot=0, args=(13, Objects.o6606_0000, VFX.FourKingsEntranceFog))
    # <!--!>


def Preconstructor():
    """ 50: Event 50 """
    HumanityRegistration(Characters.c0000_0006, 8932)
    RunEvent(11605030)
    RunEvent(11605029)
    RunEvent(11605032)
    RunEvent(11605033)
    RunEvent(11605990, slot=0, args=(11605031, Characters.c0000_0006))
    HumanityRegistration(Characters.c0000_0003, 8406)
    SkipLinesIfFlagOn(2, 1315)
    SkipLinesIfFlagOn(1, 1313)
    SkipLines(1)
    DisableCharacter(Characters.c0000_0003)
    RunEvent(11600510, slot=0, args=(Characters.c0000_0003, 1314))
    RunEvent(11600520, slot=0, args=(Characters.c0000_0003, 1310, 1319, 1315))
    RunEvent(11600530, slot=0, args=(Characters.c0000_0003, 1310, 1319, 1311))
    RunEvent(11600531, slot=0, args=(Characters.c0000_0003, 1310, 1319, 1312))
    RunEvent(11600532, slot=0, args=(Characters.c0000_0003, 1310, 1319, 1313))
    HumanityRegistration(Characters.c0000_0004, 8414)
    RunEvent(11600510, slot=1, args=(Characters.c0000_0004, 1381))
    RunEvent(11600520, slot=1, args=(Characters.c0000_0004, 1380, 1399, 1382))
    SetTeamTypeAndExitStandbyAnimation(Characters.c0000_0007, TeamType.HostileAlly)
    SkipLinesIfFlagOn(1, 1464)
    DisableCharacter(Characters.c0000_0007)
    RunEvent(11600520, slot=5, args=(Characters.c0000_0007, 1460, 1489, 1462))
    RunEvent(11600545, slot=0, args=(Characters.c0000_0007,))
    SkipLinesIfFlagOff(2, 15)
    DisableCharacter(Characters.c5330_0000)
    SkipLinesIfFlagOn(11, 15)
    EnableImmortality(Characters.c5330_0000)
    SkipLinesIfFlagOn(2, 1677)
    SkipLinesIfFlagOn(1, 1676)
    SkipLines(1)
    DisableCharacter(Characters.c5330_0000)
    RunEvent(11600537, slot=0, args=(Characters.c5330_0000, 1670, 1678, 1671))
    RunEvent(11600538, slot=0, args=(Characters.c5330_0000, 1670, 1678, 1672))
    RunEvent(11600539, slot=0, args=(Characters.c5330_0000, 1670, 1678, 1673))
    RunEvent(11600540, slot=0, args=(Characters.c5330_0000, 1670, 1678, 1677))
    RunEvent(11600541, slot=0, args=(Characters.c5330_0000, 1670, 1678, 1677))
    RunEvent(11606200)


def Event11600090(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11600090: Event 11600090 """
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


def Event11605390():
    """ 11605390: Event 11605390 """
    IfFlagOff(1, 13)
    IfActionButton(
        1,
        prompt_text=10010403,
        anchor_entity=Boxes.FourKingsFogPrompt,
        anchor_type=CoordEntityType.Region,
        line_intersects=Objects.o6606_0000,
        boss_version=True,
    )
    IfConditionTrue(0, input_condition=1)
    RotateToFaceEntity(PLAYER, Boxes.FourKingsFogRotationTarget)
    ForceAnimation(PLAYER, 7410)
    Restart()


def Event11605391():
    """ 11605391: Event 11605391 """
    IfFlagOff(1, 13)
    IfFlagOn(1, 11605393)
    IfCharacterType(1, PLAYER, CharacterType.WhitePhantom)
    IfActionButton(
        1,
        prompt_text=10010403,
        anchor_entity=Boxes.FourKingsFogPrompt,
        anchor_type=CoordEntityType.Region,
        trigger_attribute=TriggerAttribute.All,
        line_intersects=Objects.o6606_0000,
    )
    IfConditionTrue(0, input_condition=1)
    RotateToFaceEntity(PLAYER, Boxes.FourKingsFogRotationTarget)
    ForceAnimation(PLAYER, 7410)
    Restart()


def Event11605393():
    """ 11605393: Event 11605393 """
    SkipLinesIfThisEventOn(3)
    IfFlagOff(1, 13)
    IfFlagOn(1, 11605390)
    IfCharacterInsideRegion(1, PLAYER, region=Boxes.FourKingsNotify)
    IfConditionTrue(0, input_condition=1)
    SkipLinesIfClient(1)
    NotifyBossBattleStart()
    ActivateMultiplayerBuffs(Characters.c5390_0000)
    ActivateMultiplayerBuffs(Characters.c5390_0001)
    ActivateMultiplayerBuffs(Characters.c5390_0002)
    ActivateMultiplayerBuffs(Characters.c5390_0003)
    ActivateMultiplayerBuffs(Characters.c5390_0004)


@RestartOnRest
def Event11605392():
    """ 11605392: Event 11605392 """
    SkipLinesIfFlagOff(12, 13)
    DisableCharacter(Characters.c5390_0000)
    DisableCharacter(Characters.c5390_0001)
    DisableCharacter(Characters.c5390_0002)
    DisableCharacter(Characters.c5390_0003)
    DisableCharacter(Characters.c5390_0004)
    Kill(Characters.c5390_0000, award_souls=False)
    Kill(Characters.c5390_0001, award_souls=False)
    Kill(Characters.c5390_0002, award_souls=False)
    Kill(Characters.c5390_0003, award_souls=False)
    Kill(Characters.c5390_0004, award_souls=False)
    EnableTreasure(Objects.o0504_0001)
    End()
    DisableAI(Characters.c5390_0000)
    DisableAI(Characters.c5390_0001)
    DisableAI(Characters.c5390_0002)
    DisableAI(Characters.c5390_0003)
    DisableAI(Characters.c5390_0004)
    DisableCharacter(Characters.c5390_0001)
    Kill(Characters.c5390_0002, award_souls=False)
    Kill(Characters.c5390_0003, award_souls=False)
    Kill(Characters.c5390_0004, award_souls=False)
    DisableGravity(Characters.c5390_0000)
    SkipLinesIfThisEventOn(5)
    IfFlagOn(1, 11605399)
    IfCharacterInsideRegion(1, PLAYER, region=Cylinders.FourKingsDeathCutsceneTrigger)
    IfConditionTrue(0, input_condition=1)
    DisableNetworkSync()
    Wait(7.0)
    EnableCharacter(Characters.c5390_0001)
    ForceAnimation(Characters.c5390_0001, 6200)
    EnableAI(Characters.c5390_0001)
    EnableAI(Characters.c5390_0002)
    EnableAI(Characters.c5390_0003)
    EnableAI(Characters.c5390_0004)
    EnableBossHealthBar(Characters.c5390_0000, name=5390, slot=0)
    ReferDamageToEntity(Characters.c5390_0001, Characters.c5390_0000)
    ReferDamageToEntity(Characters.c5390_0002, Characters.c5390_0000)
    ReferDamageToEntity(Characters.c5390_0003, Characters.c5390_0000)
    ReferDamageToEntity(Characters.c5390_0004, Characters.c5390_0000)


def Event11600001():
    """ 11600001: Event 11600001 """
    DisableTreasure(Objects.o0504_0001)
    DisableObject(Objects.o0504_0001)
    DisableObject(Objects.o0200_0001)
    IfHealthLessThanOrEqual(1, Characters.c5390_0000, 0.0)
    IfFlagOn(1, 11605395)
    IfConditionTrue(0, input_condition=1)
    FadeOutCharacter(Characters.c5390_0000, duration=3.0)
    FadeOutCharacter(Characters.c5390_0001, duration=3.0)
    FadeOutCharacter(Characters.c5390_0002, duration=3.0)
    FadeOutCharacter(Characters.c5390_0003, duration=3.0)
    FadeOutCharacter(Characters.c5390_0004, duration=3.0)
    SkipLinesIfMultiplayer(2)
    PlayCutscene(
        160010,
        skippable=True,
        fade_out=False,
        player_id=PLAYER,
        move_to_region=Boxes.PlayerPoinAfterFourKingsDeath,
        move_to_map=NEW_LONDO_RUINS,
    )
    SkipLines(4)
    SkipLinesIfClient(2)
    PlayCutscene(
        160010,
        skippable=False,
        fade_out=False,
        player_id=PLAYER,
        move_to_region=Boxes.PlayerPoinAfterFourKingsDeath,
        move_to_map=NEW_LONDO_RUINS,
    )
    SkipLines(1)
    PlayCutscene(160010, skippable=False, fade_out=False, player_id=PLAYER)
    EnableFlag(4047)
    WaitFrames(10)
    DisableCharacter(Characters.c5390_0000)
    DisableCharacter(Characters.c5390_0001)
    DisableCharacter(Characters.c5390_0002)
    DisableCharacter(Characters.c5390_0003)
    DisableCharacter(Characters.c5390_0004)
    Kill(Characters.c5390_0000, award_souls=True)
    Kill(Characters.c5390_0001, award_souls=True)
    Kill(Characters.c5390_0002, award_souls=True)
    Kill(Characters.c5390_0003, award_souls=True)
    Kill(Characters.c5390_0004, award_souls=True)
    IfCharacterDead(0, Characters.c5390_0000)
    EnableFlag(13)
    DisableSpawner(Spawners.FourKingsSpawner)
    KillBoss(1600800)
    DisableObject(Objects.o6606_0000)
    DeleteVFX(VFX.FourKingsEntranceFog, erase_root_only=True)
    EnableTreasure(Objects.o0504_0001)
    EnableObject(Objects.o0504_0001)
    EndIfClient()
    AwardAchievement(37)
    CreateTemporaryVFX(90014, anchor_entity=Objects.o0200_0001, anchor_type=CoordEntityType.Object, model_point=-1)
    Wait(2.0)
    EnableObject(Objects.o0200_0001)
    RegisterBonfire(
        11600920,
        obj=Objects.o0200_0001,
        reaction_distance=2.0,
        reaction_angle=180.0,
        initial_kindle_level=0,
    )


def Event11605394():
    """ 11605394: Event 11605394 """
    DisableNetworkSync()
    IfFlagOff(1, 13)
    IfFlagOn(1, 11605392)
    SkipLinesIfHost(1)
    IfFlagOn(1, 11605391)
    IfCharacterInsideRegion(1, PLAYER, region=Boxes.FourKingsMusic)
    IfConditionTrue(0, input_condition=1)
    EnableSoundEvent(1603800)


def Event11605395():
    """ 11605395: Event 11605395 """
    DisableNetworkSync()
    IfHealthLessThanOrEqual(1, Characters.c5390_0000, 0.0)
    IfFlagOn(1, 11605394)
    IfConditionTrue(0, input_condition=1)
    DisableSoundEvent(1603800)


def Event11605396():
    """ 11605396: Event 11605396 """
    IfFlagOn(0, 11605392)
    IfHealthLessThanOrEqual(7, Characters.c5390_0000, 0.0)
    EndIfConditionTrue(7)
    IfCharacterAlive(1, Characters.c5390_0001)
    SkipLinesIfConditionFalse(5, 1)
    AICommand(Characters.c5390_0001, command_id=1, slot=0)
    IfCharacterDead(-1, Characters.c5390_0001)
    IfHasTAEEvent(-1, Characters.c5390_0001, tae_event_id=500)
    IfConditionTrue(0, input_condition=-1)
    AICommand(Characters.c5390_0001, command_id=-1, slot=0)
    IfCharacterAlive(2, Characters.c5390_0002)
    SkipLinesIfConditionFalse(5, 2)
    AICommand(Characters.c5390_0002, command_id=1, slot=0)
    IfCharacterDead(-2, Characters.c5390_0002)
    IfHasTAEEvent(-2, Characters.c5390_0002, tae_event_id=500)
    IfConditionTrue(0, input_condition=-2)
    AICommand(Characters.c5390_0002, command_id=-1, slot=0)
    IfCharacterAlive(3, Characters.c5390_0003)
    SkipLinesIfConditionFalse(5, 3)
    AICommand(Characters.c5390_0003, command_id=1, slot=0)
    IfCharacterDead(-3, Characters.c5390_0003)
    IfHasTAEEvent(-3, Characters.c5390_0003, tae_event_id=500)
    IfConditionTrue(0, input_condition=-3)
    AICommand(Characters.c5390_0003, command_id=-1, slot=0)
    IfCharacterAlive(4, Characters.c5390_0004)
    SkipLinesIfConditionFalse(5, 4)
    AICommand(Characters.c5390_0004, command_id=1, slot=0)
    IfCharacterDead(-4, Characters.c5390_0004)
    IfHasTAEEvent(-4, Characters.c5390_0004, tae_event_id=500)
    IfConditionTrue(0, input_condition=-4)
    AICommand(Characters.c5390_0004, command_id=-1, slot=0)
    Restart()


def Event11605397():
    """ 11605397: Event 11605397 """
    DisableNetworkSync()
    IfCharacterHasSpecialEffect(-1, PLAYER, 2200)
    IfFlagOn(-1, 13)
    IfConditionTrue(0, input_condition=-1)
    DisableCollision(Collisions.h9000B0_0000)
    DisableCollision(Collisions.h9000B0_0001)
    EndIfFlagOn(13)
    IfCharacterDoesNotHaveSpecialEffect(0, PLAYER, 2200)
    EnableCollision(Collisions.h9000B0_0000)
    EnableCollision(Collisions.h9000B0_0001)
    Restart()


def Event11605398():
    """ 11605398: Event 11605398 """
    DisableNetworkSync()
    SkipLinesIfFlagOff(3, 13)
    IfCharacterInsideRegion(1, PLAYER, region=Cylinders.FourKingsDeathCutsceneTrigger)
    IfConditionTrue(0, input_condition=1)
    SkipLinesIfFlagOn(7, 13)
    IfCharacterHasSpecialEffect(1, PLAYER, 2200)
    IfCharacterInsideRegion(1, PLAYER, region=Cylinders.FourKingsDeathCutsceneTrigger)
    IfCharacterDoesNotHaveSpecialEffect(2, PLAYER, 2200)
    IfCharacterInsideRegion(2, PLAYER, region=Cylinders.AbyssArea)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionTrue(5, 1)
    DisableCharacterCollision(PLAYER)
    IfCharacterDead(0, PLAYER)
    EnableCharacterCollision(PLAYER)
    EnableFlag(8120)
    End()
    EnableInvincibility(PLAYER)
    Wait(2.0)
    DisableInvincibility(PLAYER)


def Event11605399():
    """ 11605399: Event 11605399 """
    DisableNetworkSync()
    IfHost(1)
    IfStandingOnCollision(1, 1603300)
    IfConditionTrue(0, input_condition=1)
    EnableSpawner(Spawners.FourKingsSpawner)
    End()


def Event11605360(_, arg_0_3: int):
    """ 11605360: Event 11605360 """
    DisableNetworkSync()
    IfFlagOff(1, 13)
    IfCharacterInsideRegion(1, arg_0_3, region=Boxes.FourKingsMusic)
    IfCharacterDoesNotHaveSpecialEffect(1, arg_0_3, 2200)
    IfConditionTrue(0, input_condition=1)
    ResetAnimation(arg_0_3, disable_interpolation=True)
    ForceAnimation(arg_0_3, 6084, wait_for_completion=True)
    DisableCharacter(arg_0_3)
    EndIfNotEqual(left=arg_0_3, right=10000)
    EnableFlag(8120)


def Event11605350(_, arg_0_3: int):
    """ 11605350: Event 11605350 """
    IfHost(7)
    IfHealthGreaterThan(7, arg_0_3, 0.0)
    IfConditionTrue(0, input_condition=7)
    EnableImmortality(arg_0_3)
    IfHost(1)
    IfTimeElapsed(1, 1.0)
    IfHealthGreaterThan(1, Characters.c5390_0000, 0.0)
    IfHealthLessThanOrEqual(1, arg_0_3, 0.009999999776482582)
    IfHealthLessThanOrEqual(2, Characters.c5390_0000, 0.0)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionTrue(3, 2)
    DisableImmortality(arg_0_3)
    Kill(arg_0_3, award_souls=False)
    Restart()
    ForceAnimation(arg_0_3, 7000, wait_for_completion=True)
    DisableCharacter(arg_0_3)
    DisableImmortality(arg_0_3)
    Kill(arg_0_3, award_souls=False)


def Event11605380():
    """ 11605380: Event 11605380 """
    IfFlagOff(1, 11600900)
    IfActionButton(
        1,
        prompt_text=10010403,
        anchor_entity=1602898,
        anchor_type=CoordEntityType.Region,
        boss_version=True,
    )
    IfConditionTrue(0, input_condition=1)
    SkipLinesIfClient(1)
    NotifyBossBattleStart()
    RotateToFaceEntity(PLAYER, 1602897)
    ForceAnimation(PLAYER, 7410, wait_for_completion=True)
    ActivateMultiplayerBuffs(1600810)
    Restart()


def Event11605381():
    """ 11605381: Event 11605381 """
    DisableNetworkSync()
    IfFlagOff(1, 11600900)
    IfFlagOn(1, 11605380)
    IfCharacterType(1, PLAYER, CharacterType.WhitePhantom)
    IfActionButton(
        1,
        prompt_text=10010403,
        anchor_entity=1602898,
        anchor_type=CoordEntityType.Region,
        trigger_attribute=TriggerAttribute.All,
    )
    IfConditionTrue(0, input_condition=1)
    RotateToFaceEntity(PLAYER, 1602897)
    ForceAnimation(PLAYER, 7410)
    Restart()


@RestartOnRest
def Event11605382():
    """ 11605382: Event 11605382 """
    SkipLinesIfFlagOff(3, 11600900)
    DisableCharacter(1600810)
    Kill(1600810, award_souls=False)
    End()
    DisableAI(1600810)
    IfHost(1)
    IfFlagOn(1, 11605380)
    IfCharacterInsideRegion(1, PLAYER, region=Boxes.JareelMusic)
    IfConditionTrue(0, input_condition=1)
    EnableAI(1600810)
    EnableBossHealthBar(1600810, name=2390, slot=0)


def Event11600900():
    """ 11600900: Event 11600900 """
    IfCharacterDead(0, 1600810)
    KillBoss(1600810)
    DisableObject(1601890)
    DeleteVFX(1601891, erase_root_only=True)
    EndIfClient()
    IfPlayerHasGood(1, 2013, including_box=False)
    EndIfConditionTrue(1)
    AwardItemLot(1100, host_only=False)


def Event11605384():
    """ 11605384: Event 11605384 """
    DisableNetworkSync()
    IfFlagOff(1, 11600900)
    IfFlagOn(1, 11605382)
    IfCharacterInsideRegion(1, PLAYER, region=Boxes.JareelMusic)
    SkipLinesIfHost(1)
    IfFlagOn(1, 11605381)
    IfConditionTrue(0, input_condition=1)
    EnableSoundEvent(1603801)


def Event11605385():
    """ 11605385: Event 11605385 """
    DisableNetworkSync()
    IfCharacterInsideRegion(1, PLAYER, region=Boxes.JareelMusic)
    IfCharacterDead(1, 1600810)
    IfConditionTrue(0, input_condition=1)
    DisableSoundEvent(1603801)


def Event11600150():
    """ 11600150: Event 11600150 """
    SkipLinesIfFlagOn(63, 11600100)
    DisableCollision(Collisions.h0000B0_0002)
    DisableCollision(Collisions.h0001B0_0001)
    DisableCollision(Collisions.h0002B0_0001)
    DisableCollision(Collisions.h0003B0_0001)
    DisableCollision(Collisions.h0004B0_0001)
    DisableCollision(Collisions.h0005B0_0001)
    DisableCollision(Collisions.h0106B0_0000)
    DisableCollision(Collisions.h0010B0_0001)
    DisableCollision(Collisions.h0011B0_0001)
    DisableCollision(Collisions.h0012B0_0001)
    DisableCollision(Collisions.h0020B0_0001)
    DisableCollision(Collisions.h0021B0_0001)
    DisableCollision(Collisions.h0022B0_0001)
    DisableCollision(Collisions.h0023B0_0001)
    DisableCollision(Collisions.h0024B0_0001)
    DisableCollision(Collisions.h0025B0_0001)
    DisableCollision(Collisions.h0026B0_0001)
    DisableCollision(Collisions.h0027B0_0001)
    DisableMapPiece(1603110)
    DisableMapPiece(1603111)
    DisableMapPiece(1603112)
    DisableMapPiece(1603113)
    DisableMapPiece(1603114)
    DisableMapPiece(1603115)
    DisableMapPiece(1603116)
    DisableMapPiece(1603117)
    DisableMapPiece(1603118)
    DisableMapPiece(1603119)
    DisableMapPiece(1603120)
    DisableCollision(Collisions.h0130B0_0000)
    DisableCollision(Collisions.h0154B0_0000)
    IfFlagOn(0, 11600100)
    EnableCollision(Collisions.h0000B0_0002)
    EnableCollision(Collisions.h0001B0_0001)
    EnableCollision(Collisions.h0002B0_0001)
    EnableCollision(Collisions.h0003B0_0001)
    EnableCollision(Collisions.h0004B0_0001)
    EnableCollision(Collisions.h0005B0_0001)
    EnableCollision(Collisions.h0106B0_0000)
    EnableCollision(Collisions.h0010B0_0001)
    EnableCollision(Collisions.h0011B0_0001)
    EnableCollision(Collisions.h0012B0_0001)
    EnableCollision(Collisions.h0020B0_0001)
    EnableCollision(Collisions.h0021B0_0001)
    EnableCollision(Collisions.h0022B0_0001)
    EnableCollision(Collisions.h0023B0_0001)
    EnableCollision(Collisions.h0024B0_0001)
    EnableCollision(Collisions.h0025B0_0001)
    EnableCollision(Collisions.h0026B0_0001)
    EnableCollision(Collisions.h0027B0_0001)
    EnableMapPiece(1603110)
    EnableMapPiece(1603111)
    EnableMapPiece(1603112)
    EnableMapPiece(1603113)
    EnableMapPiece(1603114)
    EnableMapPiece(1603115)
    EnableMapPiece(1603116)
    EnableMapPiece(1603117)
    EnableMapPiece(1603118)
    EnableMapPiece(1603119)
    EnableMapPiece(1603120)
    EnableCollision(Collisions.h0130B0_0000)
    EnableCollision(Collisions.h0154B0_0000)
    DisableSoundEvent(1603850)
    DisableCollision(Collisions.h0000B0_0000)
    DisableCollision(Collisions.h0001B0_0000)
    DisableCollision(Collisions.h0002B0_0000)
    DisableCollision(Collisions.h0003B0_0000)
    DisableCollision(Collisions.h0004B0_0000)
    DisableCollision(Collisions.h0005B0_0000)
    DisableCollision(Collisions.h0006B0_0000)
    DisableCollision(Collisions.h0010B0_0000)
    DisableCollision(Collisions.h0011B0_0000)
    DisableCollision(Collisions.h0012B0_0000)
    DisableCollision(Collisions.h0020B0_0000)
    DisableCollision(Collisions.h0021B0_0000)
    DisableCollision(Collisions.h0022B0_0000)
    DisableCollision(Collisions.h0023B0_0000)
    DisableCollision(Collisions.h0024B0_0000)
    DisableCollision(Collisions.h0025B0_0000)
    DisableCollision(Collisions.h0026B0_0000)
    DisableCollision(Collisions.h0027B0_0000)


@RestartOnRest
def Event11605100():
    """ 11605100: Event 11605100 """
    EndIfFlagOn(11600100)
    DisableBackread(Characters.c2390_0011)
    DisableBackread(Characters.c2390_0001)
    DisableBackread(Characters.c2390_0002)
    DisableBackread(Characters.c2390_0003)
    DisableBackread(Characters.c2390_0004)
    DisableBackread(Characters.c2390_0005)
    DisableBackread(Characters.c2390_0006)
    DisableBackread(Characters.c2390_0007)
    DisableBackread(Characters.c2390_0008)
    DisableBackread(Characters.c2390_0009)
    DisableBackread(Characters.c2390_0010)
    DisableBackread(Characters.c3500_0000)
    DisableBackread(Characters.c3500_0001)
    DisableBackread(Characters.c2390_0012)
    DisableBackread(Characters.c2390_0013)
    DisableBackread(Characters.c2390_0014)
    DisableBackread(Characters.c2390_0015)
    DisableBackread(Characters.c2390_0016)
    DisableBackread(Characters.c2390_0017)
    IfFlagOn(0, 11600100)
    EnableBackread(Characters.c2390_0011)
    EnableBackread(Characters.c2390_0001)
    EnableBackread(Characters.c2390_0002)
    EnableBackread(Characters.c2390_0003)
    EnableBackread(Characters.c2390_0004)
    EnableBackread(Characters.c2390_0005)
    EnableBackread(Characters.c2390_0006)
    EnableBackread(Characters.c2390_0007)
    EnableBackread(Characters.c2390_0008)
    EnableBackread(Characters.c2390_0009)
    EnableBackread(Characters.c2390_0010)
    EnableBackread(Characters.c3500_0000)
    EnableBackread(Characters.c3500_0001)
    EnableBackread(Characters.c2390_0012)
    EnableBackread(Characters.c2390_0013)
    EnableBackread(Characters.c2390_0014)
    EnableBackread(Characters.c2390_0015)
    EnableBackread(Characters.c2390_0016)
    EnableBackread(Characters.c2390_0017)


def Event11600100():
    """ 11600100: Event 11600100 """
    SkipLinesIfFlagOn(1, 11600101)
    SkipLinesIfThisEventOff(8)
    EndOfAnimation(Objects.o6000_0000, 10)
    DisableCollision(Collisions.h7000B0_0000)
    DisableCollision(Collisions.h7000B0_0001)
    DisableCollision(Collisions.h8000B0_0000)
    DisableCollision(Collisions.h8000B0_0001)
    DisableObject(Objects.o6500_0000)
    DisableFlag(404)
    End()
    EnableCollision(Collisions.h8000B0_0000)
    EnableCollision(Collisions.h8000B0_0001)
    IfFlagOn(0, 11600101)
    SkipLinesIfMultiplayer(2)
    PlayCutscene(160000, skippable=True, fade_out=False, player_id=PLAYER)
    SkipLines(1)
    PlayCutscene(160000, skippable=False, fade_out=False, player_id=PLAYER)
    WaitFrames(1)
    EnableFlag(11600100)
    Restart()


def Event11600101(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 11600101: Event 11600101 """
    SkipLinesIfThisEventSlotOff(3)
    EndOfAnimation(Objects.o6000_0000, arg_8_11)
    EndOfAnimation(arg_0_3, 0)
    End()
    IfActionButton(
        0,
        prompt_text=10010502,
        anchor_entity=arg_0_3,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        model_point=104,
        trigger_attribute=TriggerAttribute.All,
    )
    Move(PLAYER, destination=arg_0_3, destination_type=CoordEntityType.Object, model_point=101, short_move=True)
    ForceAnimation(PLAYER, 8020)
    ForceAnimation(arg_0_3, 0, wait_for_completion=True)
    EndIfFlagOn(arg_4_7)
    ForceAnimation(Objects.o6000_0000, arg_8_11, wait_for_completion=True)


def Event11600110(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 11600110: Event 11600110 """
    SkipLinesIfThisEventSlotOff(5)
    DisableObjectActivation(arg_8_11, obj_act_id=-1, relative_index=0)
    DisableObjectActivation(arg_8_11, obj_act_id=-1, relative_index=1)
    DisableObjectActivation(arg_8_11, obj_act_id=-1, relative_index=2)
    DisableObjectActivation(arg_8_11, obj_act_id=-1, relative_index=3)
    End()
    IfObjectActivated(0, obj_act_id=arg_0_3)
    EnableFlag(arg_0_3)
    EndIfClient()
    DisplayDialog(
        arg_4_7,
        anchor_entity=arg_8_11,
        display_distance=3.0,
        button_type=ButtonType.Yes_or_No,
        number_buttons=NumberButtons.NoButton,
    )
    DisableNetworkSync()
    Wait(2.0)
    DisableObjectActivation(arg_8_11, obj_act_id=-1, relative_index=0)
    DisableObjectActivation(arg_8_11, obj_act_id=-1, relative_index=1)
    DisableObjectActivation(arg_8_11, obj_act_id=-1, relative_index=2)
    DisableObjectActivation(arg_8_11, obj_act_id=-1, relative_index=3)


def Event11600120(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int):
    """ 11600120: Event 11600120 """
    SkipLinesIfThisEventSlotOff(5)
    DisableObjectActivation(arg_8_11, obj_act_id=-1, relative_index=0)
    DisableObjectActivation(arg_8_11, obj_act_id=-1, relative_index=1)
    DisableObjectActivation(arg_8_11, obj_act_id=-1, relative_index=2)
    DisableObjectActivation(arg_8_11, obj_act_id=-1, relative_index=3)
    End()
    IfObjectActivated(0, obj_act_id=arg_0_3)
    EnableFlag(arg_0_3)
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
    DisableNetworkSync()
    Wait(2.0)
    DisableObjectActivation(arg_8_11, obj_act_id=-1, relative_index=0)
    DisableObjectActivation(arg_8_11, obj_act_id=-1, relative_index=1)
    DisableObjectActivation(arg_8_11, obj_act_id=-1, relative_index=2)
    DisableObjectActivation(arg_8_11, obj_act_id=-1, relative_index=3)


def Event11600160():
    """ 11600160: Event 11600160 """
    SkipLinesIfThisEventOff(3)
    EndOfAnimation(Objects.o6410_0000, 0)
    RegisterLadder(start_climbing_flag=11600014, stop_climbing_flag=11600015, obj=Objects.o6410_0000)
    End()
    IfActionButton(
        0,
        prompt_text=10010500,
        anchor_entity=Objects.o6410_0000,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        model_point=194,
        trigger_attribute=TriggerAttribute.All,
    )
    EnableFlag(11600160)
    Move(
        PLAYER,
        destination=Objects.o6410_0000,
        destination_type=CoordEntityType.Object,
        model_point=192,
        short_move=True,
    )
    ForceAnimation(PLAYER, 8005)
    Wait(0.5)
    ForceAnimation(Objects.o6410_0000, 0, wait_for_completion=True)
    RegisterLadder(start_climbing_flag=11600014, stop_climbing_flag=11600015, obj=Objects.o6410_0000)


def Event11600200():
    """ 11600200: Event 11600200 """
    SkipLinesIfFlagOff(3, 11600201)
    EndOfAnimation(Objects.o6200_0000, 21)
    DisableObjectActivation(Objects.o6100_0006, obj_act_id=6101)
    SkipLines(2)
    EndOfAnimation(Objects.o6200_0000, 20)
    DisableObjectActivation(m10_02_Objects.o6100_0000, obj_act_id=6101)
    IfSingleplayer(1)
    IfFlagOff(1, 11600201)
    IfCharacterInsideRegion(1, PLAYER, region=Spheres.FirelinkElevatorStartFromTop)
    IfSingleplayer(2)
    IfFlagOn(2, 11600201)
    IfCharacterInsideRegion(2, PLAYER, region=Spheres.FirelinkElevatorStartFromBottom)
    IfSingleplayer(3)
    IfObjectActivated(3, obj_act_id=11020202)
    IfSingleplayer(4)
    IfObjectActivated(4, obj_act_id=11600203)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(-1, input_condition=4)
    IfConditionTrue(0, input_condition=-1)
    WaitForNetworkApproval(max_seconds=3.0)
    EnableFlag(11605120)
    SkipLinesIfFinishedConditionTrue(10, 2)
    SkipLinesIfFinishedConditionTrue(9, 3)
    EnableFlag(11600201)
    DisableObjectActivation(Objects.o6100_0006, obj_act_id=6101)
    ForceAnimation(Objects.o6200_0000, 11, wait_for_completion=True)
    ForceAnimation(Objects.o6200_0000, 1, wait_for_completion=True)
    IfAllPlayersOutsideRegion(0, region=Spheres.FirelinkElevatorStartFromBottom)
    ForceAnimation(Objects.o6200_0000, 21, wait_for_completion=True)
    EnableObjectActivation(m10_02_Objects.o6100_0000, obj_act_id=6101)
    DisableFlag(11605120)
    Restart()
    DisableFlag(11600201)
    DisableObjectActivation(m10_02_Objects.o6100_0000, obj_act_id=6101)
    ForceAnimation(Objects.o6200_0000, 10, wait_for_completion=True)
    ForceAnimation(Objects.o6200_0000, 0, wait_for_completion=True)
    IfAllPlayersOutsideRegion(0, region=Spheres.FirelinkElevatorStartFromTop)
    ForceAnimation(Objects.o6200_0000, 20, wait_for_completion=True)
    EnableObjectActivation(Objects.o6100_0006, obj_act_id=6101)
    DisableFlag(11605120)
    Restart()


def Event11600250():
    """ 11600250: Event 11600250 """
    DisableNetworkSync()
    IfFlagOff(1, 11605120)
    IfFlagOff(1, 11600201)
    IfActionButton(
        1,
        prompt_text=10010501,
        anchor_entity=m10_02_Objects.o6100_0000,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        model_point=192,
        trigger_attribute=TriggerAttribute.All,
    )
    IfFlagOff(2, 11605120)
    IfFlagOn(2, 11600201)
    IfActionButton(
        2,
        prompt_text=10010501,
        anchor_entity=Objects.o6100_0006,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        model_point=192,
        trigger_attribute=TriggerAttribute.All,
    )
    IfMultiplayer(3)
    IfFlagOff(3, 11600201)
    IfCharacterInsideRegion(3, PLAYER, region=Spheres.FirelinkElevatorStartFromTop)
    IfMultiplayer(4)
    IfFlagOn(4, 11600201)
    IfCharacterInsideRegion(4, PLAYER, region=Spheres.FirelinkElevatorStartFromBottom)
    IfMultiplayer(5)
    IfObjectActivated(5, obj_act_id=11020202)
    IfMultiplayer(6)
    IfObjectActivated(6, obj_act_id=11600203)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(-1, input_condition=4)
    IfConditionTrue(-1, input_condition=5)
    IfConditionTrue(-1, input_condition=6)
    IfConditionTrue(0, input_condition=-1)
    DisplayDialog(
        10010170,
        anchor_entity=-1,
        display_distance=3.0,
        button_type=ButtonType.OK_or_Cancel,
        number_buttons=NumberButtons.NoButton,
    )
    Restart()


def Event11600199():
    """ 11600199: Event 11600199 """
    EndIfThisEventOn()
    IfFlagOn(0, 11600100)
    EnableObjectActivation(Objects.o6100_0002, obj_act_id=6101)
    EnableObjectActivation(Objects.o6100_0004, obj_act_id=6101)


def Event11600210():
    """ 11600210: Event 11600210 """
    SkipLinesIfFlagOff(3, 11600211)
    EndOfAnimation(Objects.o6200_0001, 22)
    DisableObjectActivation(Objects.o6100_0002, obj_act_id=6101)
    SkipLines(2)
    EndOfAnimation(Objects.o6200_0001, 21)
    DisableObjectActivation(Objects.o6100_0003, obj_act_id=6101)
    SkipLinesIfFlagOn(1, 11600100)
    DisableObjectActivation(Objects.o6100_0002, obj_act_id=6101)
    IfFlagOn(1, 11600100)
    IfFlagOff(1, 11600211)
    IfCharacterInsideRegion(1, PLAYER, region=Spheres.ChurchelevatorStartFromBottom)
    IfFlagOn(2, 11600100)
    IfFlagOn(2, 11600211)
    IfCharacterInsideRegion(2, PLAYER, region=Spheres.ChurchelevatorStartFromTop)
    IfObjectActivated(3, obj_act_id=11600212)
    IfObjectActivated(4, obj_act_id=11600213)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(-1, input_condition=4)
    IfConditionTrue(0, input_condition=-1)
    WaitForNetworkApproval(max_seconds=3.0)
    EnableFlag(11605121)
    SkipLinesIfFinishedConditionTrue(10, 2)
    SkipLinesIfFinishedConditionTrue(9, 4)
    EnableFlag(11600211)
    DisableObjectActivation(Objects.o6100_0002, obj_act_id=6101)
    ForceAnimation(Objects.o6200_0001, 10, wait_for_completion=True)
    ForceAnimation(Objects.o6200_0001, 2, wait_for_completion=True)
    IfAllPlayersOutsideRegion(0, region=Spheres.ChurchelevatorStartFromTop)
    ForceAnimation(Objects.o6200_0001, 22, wait_for_completion=True)
    EnableObjectActivation(Objects.o6100_0003, obj_act_id=6101)
    DisableFlag(11605121)
    Restart()
    DisableFlag(11600211)
    DisableObjectActivation(Objects.o6100_0003, obj_act_id=6101)
    ForceAnimation(Objects.o6200_0001, 13, wait_for_completion=True)
    ForceAnimation(Objects.o6200_0001, 3, wait_for_completion=True)
    IfAllPlayersOutsideRegion(0, region=Spheres.ChurchelevatorStartFromBottom)
    ForceAnimation(Objects.o6200_0001, 21, wait_for_completion=True)
    EnableObjectActivation(Objects.o6100_0002, obj_act_id=6101)
    DisableFlag(11605121)
    Restart()


def Event11600251():
    """ 11600251: Event 11600251 """
    DisableNetworkSync()
    IfFlagOff(1, 11605121)
    IfFlagOn(1, 11600211)
    IfActionButton(
        1,
        prompt_text=10010501,
        anchor_entity=Objects.o6100_0002,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        model_point=192,
        trigger_attribute=TriggerAttribute.All,
    )
    IfFlagOff(2, 11605121)
    IfFlagOff(2, 11600211)
    IfActionButton(
        2,
        prompt_text=10010501,
        anchor_entity=Objects.o6100_0003,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        model_point=192,
        trigger_attribute=TriggerAttribute.All,
    )
    IfFlagOff(3, 11600100)
    IfActionButton(
        3,
        prompt_text=10010501,
        anchor_entity=Objects.o6100_0002,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        model_point=192,
        trigger_attribute=TriggerAttribute.All,
    )
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    DisplayDialog(
        10010170,
        anchor_entity=-1,
        display_distance=3.0,
        button_type=ButtonType.OK_or_Cancel,
        number_buttons=NumberButtons.NoButton,
    )
    Restart()


def Event11600220():
    """ 11600220: Event 11600220 """
    SkipLinesIfFlagOff(3, 11600221)
    EndOfAnimation(Objects.o6200_0002, 24)
    DisableObjectActivation(Objects.o6100_0004, obj_act_id=6101)
    SkipLines(2)
    EndOfAnimation(Objects.o6200_0002, 21)
    DisableObjectActivation(Objects.o6100_0005, obj_act_id=6101)
    SkipLinesIfFlagOn(1, 11600100)
    DisableObjectActivation(Objects.o6100_0004, obj_act_id=6101)
    IfFlagOn(1, 11600100)
    IfFlagOff(1, 11600221)
    IfCharacterInsideRegion(1, PLAYER, region=Spheres.SluiceElevatorStartFromBottom)
    IfFlagOn(2, 11600100)
    IfFlagOn(2, 11600221)
    IfCharacterInsideRegion(2, PLAYER, region=Spheres.SluiceElevatorStartFromTop)
    IfObjectActivated(3, obj_act_id=11600222)
    IfObjectActivated(4, obj_act_id=11600223)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(-1, input_condition=4)
    IfConditionTrue(0, input_condition=-1)
    WaitForNetworkApproval(max_seconds=3.0)
    EnableFlag(11605122)
    SkipLinesIfFinishedConditionTrue(10, 2)
    SkipLinesIfFinishedConditionTrue(9, 4)
    EnableFlag(11600221)
    DisableObjectActivation(Objects.o6100_0004, obj_act_id=6101)
    ForceAnimation(Objects.o6200_0002, 10, wait_for_completion=True)
    ForceAnimation(Objects.o6200_0002, 4, wait_for_completion=True)
    IfAllPlayersOutsideRegion(0, region=Spheres.SluiceElevatorStartFromTop)
    ForceAnimation(Objects.o6200_0002, 24, wait_for_completion=True)
    EnableObjectActivation(Objects.o6100_0005, obj_act_id=6101)
    DisableFlag(11605122)
    Restart()
    DisableFlag(11600221)
    DisableObjectActivation(Objects.o6100_0005, obj_act_id=6101)
    ForceAnimation(Objects.o6200_0002, 15, wait_for_completion=True)
    ForceAnimation(Objects.o6200_0002, 5, wait_for_completion=True)
    IfAllPlayersOutsideRegion(0, region=Spheres.SluiceElevatorStartFromBottom)
    ForceAnimation(Objects.o6200_0002, 21, wait_for_completion=True)
    EnableObjectActivation(Objects.o6100_0004, obj_act_id=6101)
    DisableFlag(11605122)
    Restart()


def Event11600252():
    """ 11600252: Event 11600252 """
    DisableNetworkSync()
    IfFlagOff(1, 11605122)
    IfFlagOn(1, 11600221)
    IfActionButton(
        1,
        prompt_text=10010501,
        anchor_entity=Objects.o6100_0004,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        model_point=192,
        trigger_attribute=TriggerAttribute.All,
    )
    IfFlagOff(2, 11605122)
    IfFlagOff(2, 11600221)
    IfActionButton(
        2,
        prompt_text=10010501,
        anchor_entity=Objects.o6100_0005,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        model_point=192,
        trigger_attribute=TriggerAttribute.All,
    )
    IfFlagOff(3, 11600100)
    IfActionButton(
        3,
        prompt_text=10010501,
        anchor_entity=Objects.o6100_0004,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        model_point=192,
        trigger_attribute=TriggerAttribute.All,
    )
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    DisplayDialog(
        10010170,
        anchor_entity=-1,
        display_distance=3.0,
        button_type=ButtonType.OK_or_Cancel,
        number_buttons=NumberButtons.NoButton,
    )
    Restart()


def Event11600230():
    """ 11600230: Event 11600230 """
    SkipLinesIfFlagOff(3, 11600231)
    EndOfAnimation(Objects.o6200_0003, 26)
    DisableObjectActivation(Objects.o6100_0007, obj_act_id=6101)
    SkipLines(2)
    EndOfAnimation(Objects.o6200_0003, 21)
    DisableObjectActivation(Objects.o6100_0008, obj_act_id=6101)
    IfFlagOff(1, 11600231)
    IfCharacterInsideRegion(1, PLAYER, region=Spheres.DarkrootElevatorStartFromBottom)
    IfFlagOn(2, 11600231)
    IfCharacterInsideRegion(2, PLAYER, region=Spheres.DarkrootElevatorStartFromTop)
    IfObjectActivated(3, obj_act_id=11600232)
    IfObjectActivated(4, obj_act_id=11600233)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(-1, input_condition=4)
    IfConditionTrue(0, input_condition=-1)
    WaitForNetworkApproval(max_seconds=3.0)
    EnableFlag(11605123)
    SkipLinesIfFinishedConditionTrue(10, 2)
    SkipLinesIfFinishedConditionTrue(9, 4)
    EnableFlag(11600231)
    DisableObjectActivation(Objects.o6100_0007, obj_act_id=6101)
    ForceAnimation(Objects.o6200_0003, 10, wait_for_completion=True)
    ForceAnimation(Objects.o6200_0003, 6, wait_for_completion=True)
    IfAllPlayersOutsideRegion(0, region=Spheres.DarkrootElevatorStartFromTop)
    ForceAnimation(Objects.o6200_0003, 26, wait_for_completion=True)
    EnableObjectActivation(Objects.o6100_0008, obj_act_id=6101)
    DisableFlag(11605123)
    Restart()
    DisableFlag(11600231)
    DisableObjectActivation(Objects.o6100_0008, obj_act_id=6101)
    ForceAnimation(Objects.o6200_0003, 17, wait_for_completion=True)
    ForceAnimation(Objects.o6200_0003, 7, wait_for_completion=True)
    IfAllPlayersOutsideRegion(0, region=Spheres.DarkrootElevatorStartFromBottom)
    ForceAnimation(Objects.o6200_0003, 21, wait_for_completion=True)
    EnableObjectActivation(Objects.o6100_0007, obj_act_id=6101)
    DisableFlag(11605123)
    Restart()


def Event11600253():
    """ 11600253: Event 11600253 """
    DisableNetworkSync()
    IfFlagOff(1, 11605123)
    IfFlagOn(1, 11600231)
    IfActionButton(
        1,
        prompt_text=10010501,
        anchor_entity=Objects.o6100_0007,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        model_point=192,
        trigger_attribute=TriggerAttribute.All,
    )
    IfFlagOff(2, 11605123)
    IfFlagOff(2, 11600231)
    IfActionButton(
        2,
        prompt_text=10010501,
        anchor_entity=Objects.o6100_0008,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        model_point=192,
        trigger_attribute=TriggerAttribute.All,
    )
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    DisplayDialog(
        10010170,
        anchor_entity=-1,
        display_distance=3.0,
        button_type=ButtonType.OK_or_Cancel,
        number_buttons=NumberButtons.NoButton,
    )
    Restart()


@RestartOnRest
def Event11605150(_, arg_0_3: int, arg_4_7: int):
    """ 11605150: Event 11605150 """
    DisableNetworkSync()
    IfCharacterDead(1, arg_0_3)
    EndIfConditionTrue(1)
    IfCharacterOutsideRegion(0, arg_0_3, region=arg_4_7)
    ReplanAI(arg_0_3)
    Wait(5.0)
    Restart()


@RestartOnRest
def Event11605001(_, arg_0_3: int, arg_4_7: float, arg_8_11: int):
    """ 11605001: Event 11605001 """
    SkipLinesIfThisEventSlotOff(2)
    ResetStandbyAnimationSettings(arg_0_3)
    End()
    DisableAI(arg_0_3)
    IfEntityWithinDistance(1, arg_0_3, PLAYER, radius=arg_4_7)
    IfAttacked(2, arg_0_3, attacker=PLAYER)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionTrue(2, 1)
    ResetStandbyAnimationSettings(arg_0_3)
    SkipLines(1)
    SetStandbyAnimationSettings(arg_0_3, cancel_animation=arg_8_11)
    EnableAI(arg_0_3)


@RestartOnRest
def Event11605050(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: float):
    """ 11605050: Event 11605050 """
    SkipLinesIfThisEventSlotOff(2)
    ResetStandbyAnimationSettings(arg_0_3)
    End()
    DisableAI(arg_0_3)
    IfCharacterInsideRegion(1, PLAYER, region=arg_4_7)
    IfAttacked(2, arg_0_3, attacker=PLAYER)
    SkipLinesIfEqual(1, left=arg_12_15, right=0)
    IfEntityWithinDistance(3, arg_0_3, PLAYER, radius=arg_16_19)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    SkipLinesIfEqual(1, left=arg_12_15, right=0)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionTrue(2, 1)
    ResetStandbyAnimationSettings(arg_0_3)
    SkipLines(1)
    SetStandbyAnimationSettings(arg_0_3, cancel_animation=arg_8_11)
    EnableAI(arg_0_3)


@RestartOnRest
def Event11605101():
    """ 11605101: Event 11605101 """
    SkipLinesIfThisEventOff(2)
    AICommand(Characters.c2680_0001, command_id=1, slot=0)
    End()
    IfHasTAEEvent(0, Characters.c2680_0001, tae_event_id=700)
    SetNest(Characters.c2680_0001, Boxes.FemaleGhostNestChange)
    AICommand(Characters.c2680_0001, command_id=0, slot=0)
    ReplanAI(Characters.c2680_0001)
    IfCharacterInsideRegion(0, Characters.c2680_0001, region=Boxes.FemaleGhostNestChangeTrigger)
    AICommand(Characters.c2680_0001, command_id=1, slot=0)


@RestartOnRest
def Event11600810():
    """ 11600810: Event 11600810 """
    SkipLinesIfThisEventOff(2)
    DisableCharacter(Characters.c3420_0000)
    End()
    IfCharacterDead(0, Characters.c3420_0000)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterHollow(-1, PLAYER)
    EndIfConditionFalse(-1)
    AwardItemLot(34200200, host_only=True)


@RestartOnRest
def Event11600400():
    """ 11600400: Event 11600400 """
    DisableCharacterCollision(Characters.c3420_0000)
    DisableGravity(Characters.c3420_0000)
    SkipLinesIfThisEventOff(2)
    SetStandbyAnimationSettings(Characters.c3420_0000, cancel_animation=29060)
    End()
    IfEntityWithinDistance(-1, Characters.c3420_0000, PLAYER, radius=10.0)
    IfAttacked(-1, Characters.c3420_0000, attacker=PLAYER)
    IfConditionTrue(0, input_condition=-1)
    ResetStandbyAnimationSettings(Characters.c3420_0000)
    ForceAnimation(Characters.c3420_0000, 29060)


@RestartOnRest
def Event11605200(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11605200: Event 11605200 """
    SkipLinesIfThisEventSlotOff(3)
    IfCharacterBackreadEnabled(0, arg_0_3)
    AICommand(arg_0_3, command_id=arg_8_11, slot=0)
    End()
    DisableCharacter(arg_4_7)
    IfCharacterBackreadEnabled(1, arg_0_3)
    IfHasTAEEvent(1, arg_0_3, tae_event_id=300)
    IfFlagOn(1, arg_12_15)
    IfConditionTrue(0, input_condition=1)
    AICommand(arg_0_3, command_id=arg_8_11, slot=0)
    EnableCharacter(arg_4_7)
    Move(
        arg_4_7,
        destination=arg_0_3,
        destination_type=CoordEntityType.Character,
        model_point=100,
        copy_draw_parent=arg_0_3,
    )
    ForceAnimation(arg_4_7, 8300, wait_for_completion=True)
    IfDoesNotHaveTAEEvent(1, arg_0_3, tae_event_id=300)
    End()


@RestartOnRest
def Event11605250(_, arg_0_3: int):
    """ 11605250: Event 11605250 """
    DisableNetworkSync()
    SkipLinesIfThisEventSlotOn(1)
    IfHasTAEEvent(0, arg_0_3, tae_event_id=400)
    DisableCharacter(arg_0_3)


@RestartOnRest
def Event11600850(_, arg_0_3: int):
    """ 11600850: Event 11600850 """
    SkipLinesIfThisEventSlotOff(3)
    DisableCharacter(arg_0_3)
    Kill(arg_0_3, award_souls=False)
    End()
    IfCharacterDead(0, arg_0_3)
    End()


def Event11600600(_, arg_0_3: int, arg_4_7: int):
    """ 11600600: Event 11600600 """
    SkipLinesIfThisEventSlotOff(4)
    EndOfAnimation(arg_0_3, 0)
    DisableObjectActivation(arg_0_3, obj_act_id=-1)
    EnableTreasure(arg_0_3)
    End()
    DisableTreasure(arg_0_3)
    IfObjectActivated(0, obj_act_id=arg_4_7)
    WaitFrames(10)
    EnableTreasure(arg_0_3)


def Event11600650(_, arg_0_3: int, arg_4_7: int):
    """ 11600650: Event 11600650 """
    SkipLinesIfThisEventSlotOff(3)
    EndOfAnimation(arg_0_3, 101)
    EnableTreasure(arg_0_3)
    End()
    DisableTreasure(arg_0_3)
    ForceAnimation(arg_0_3, 100, loop=True)
    IfObjectDestroyed(0, arg_4_7)
    ForceAnimation(arg_0_3, 101, wait_for_completion=True)
    EnableTreasure(arg_0_3)


def Event11600510(_, arg_0_3: int, arg_4_7: int):
    """ 11600510: Event 11600510 """
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


def Event11600520(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11600520: Event 11600520 """
    SkipLinesIfThisEventSlotOff(2)
    DropMandatoryTreasure(arg_0_3)
    End()
    IfHealthLessThanOrEqual(0, arg_0_3, 0.0)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)


def Event11600530(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11600530: Event 11600530 """
    IfFlagOff(1, 1314)
    IfFlagOn(1, 1310)
    IfFlagOn(1, 710)
    IfCharacterAlive(1, arg_0_3)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)


def Event11600531(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11600531: Event 11600531 """
    IfFlagOff(1, 1314)
    IfFlagOn(1, 1311)
    IfFlagOn(1, 11600100)
    IfCharacterAlive(1, arg_0_3)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)


def Event11600532(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11600532: Event 11600532 """
    IfFlagOff(1, 1314)
    IfFlagOn(1, 1312)
    IfFlagOn(1, 13)
    IfFlagOn(1, 11600593)
    IfOutsideMap(1, game_map=NEW_LONDO_RUINS)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)
    DisableCharacter(arg_0_3)


def Event11600537(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11600537: Event 11600537 """
    EndIfFlagOff(1670)
    DisableCharacter(arg_0_3)
    IfHost(1)
    IfFlagOn(1, 1670)
    IfFlagOff(1, 11800100)
    IfFlagOn(1, 13)
    IfConditionTrue(0, input_condition=1)
    EnableCharacter(arg_0_3)
    ForceAnimation(arg_0_3, 9060, wait_for_completion=True)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)


def Event11600538(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11600538: Event 11600538 """
    IfFlagOn(1, 1671)
    IfFlagOn(1, 710)
    IfCharacterAlive(1, arg_0_3)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)


def Event11600539(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11600539: Event 11600539 """
    IfFlagOn(1, 1672)
    IfFlagOn(1, 11800100)
    IfCharacterAlive(1, arg_0_3)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)


def Event11600540(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11600540: Event 11600540 """
    IfFlagOn(-1, 1672)
    IfFlagOn(-1, 1678)
    IfConditionTrue(1, input_condition=-1)
    IfFlagOn(1, 11600590)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)
    ForceAnimation(arg_0_3, 7005, wait_for_completion=True)
    DisableCharacter(arg_0_3)


def Event11600541(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11600541: Event 11600541 """
    IfInsideMap(1, game_map=NEW_LONDO_RUINS)
    IfFlagOn(-1, 11600590)
    IfHealthLessThanOrEqual(2, arg_0_3, 0.8999999761581421)
    IfHealthGreaterThan(2, arg_0_3, 0.0)
    IfAttacked(2, arg_0_3, attacker=PLAYER)
    IfEntityBeyondDistance(2, arg_0_3, PLAYER, radius=15.0)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)
    ForceAnimation(arg_0_3, 7005, wait_for_completion=True)
    DisableCharacter(arg_0_3)


def Event11600545(_, arg_0_3: int):
    """ 11600545: Event 11600545 """
    IfFlagOn(0, 1464)
    EnableCharacter(arg_0_3)
    SetTeamTypeAndExitStandbyAnimation(arg_0_3, TeamType.HostileAlly)


def Event11606200():
    """ 11606200: Event 11606200 """
    IfFlagOn(-1, 1672)
    IfFlagOn(-1, 1673)
    IfFlagOn(-1, 1674)
    IfConditionTrue(1, input_condition=-1)
    IfInsideMap(1, game_map=NEW_LONDO_RUINS)
    IfFlagOn(1, 821)
    IfConditionTrue(0, input_condition=1)
    DisableFlag(821)
    EnableFlag(831)
    EnableCharacter(m18_00_Characters.c5330_0017)
    PlayCutscene(
        160040,
        skippable=True,
        fade_out=False,
        player_id=PLAYER,
        move_to_region=m18_00_Boxes.ArrivalFromFirelinkOrAbyss,
        move_to_map=KILN_OF_THE_FIRST_FLAME,
    )
    PlayCutscene(180041, skippable=True, fade_out=False, player_id=PLAYER)
    WaitFrames(1)
    EnableFlag(823)
    Restart()


def Event11605029():
    """ 11605029: Event 11605029 """
    SkipLinesIfClient(1)
    SetNetworkUpdateAuthority(Characters.c0000_0006, UpdateAuthority.Forced)
    SkipLinesIfFlagOn(3, 11605034)
    IfClient(2)
    IfFlagOn(2, 11605031)
    SkipLinesIfConditionTrue(1, 2)
    DisableCharacter(Characters.c0000_0006)
    EndIfFlagOn(13)
    IfMultiplayerCount(1, arg1=4, arg2=3)
    IfHost(1)
    IfFlagOff(1, 11605031)
    IfFlagOff(1, 11605034)
    IfCharacterHuman(1, PLAYER)
    IfFlagOn(1, 11200300)
    IfCharacterBackreadEnabled(1, Characters.c0000_0006)
    IfEntityWithinDistance(1, Characters.c0000_0006, PLAYER, radius=5.0)
    IfCharacterHasSpecialEffect(1, PLAYER, 28)
    IfConditionTrue(0, input_condition=1)
    PlaceSummonSign(
        SummonSignType.BlueEyeSign,
        Characters.c0000_0006,
        region=Points.WitchBeatriceSummonSign,
        summon_flag=11605031,
        dismissal_flag=11605034,
    )


def Event11605030():
    """ 11605030: Event 11605030 """
    SkipLinesIfClient(1)
    SetNetworkUpdateAuthority(Characters.c0000_0006, UpdateAuthority.Forced)
    SkipLinesIfFlagOn(3, 11605034)
    IfClient(2)
    IfFlagOn(2, 11605031)
    SkipLinesIfConditionTrue(1, 2)
    DisableCharacter(Characters.c0000_0006)
    EndIfFlagOn(13)
    IfHost(1)
    IfCharacterHuman(1, PLAYER)
    IfFlagOn(1, 11200300)
    IfCharacterBackreadEnabled(1, Characters.c0000_0006)
    IfEntityWithinDistance(1, Characters.c0000_0006, PLAYER, radius=5.0)
    IfConditionTrue(0, input_condition=1)
    PlaceSummonSign(
        SummonSignType.BlueEyeSign,
        Characters.c0000_0006,
        region=Points.WitchBeatriceSummonSign,
        summon_flag=11605031,
        dismissal_flag=11605034,
    )


def Event11605990(_, arg_0_3: int, arg_4_7: int):
    """ 11605990: Event 11605990 """
    IfFlagOn(0, arg_0_3)
    EraseNPCSummonSign(summoned_character=arg_4_7)
    IfFlagOff(0, arg_0_3)
    Restart()


def Event11605032():
    """ 11605032: Event 11605032 """
    EndIfThisEventOn()
    IfFlagOn(1, 11605031)
    IfFlagOn(1, 11605393)
    IfConditionTrue(0, input_condition=1)
    AICommand(Characters.c0000_0006, command_id=10, slot=0)
    ReplanAI(Characters.c0000_0006)
    IfCharacterInsideRegion(0, Characters.c0000_0006, region=Boxes.FourKingsFogPrompt)
    RotateToFaceEntity(Characters.c0000_0006, Boxes.FourKingsFogRotationTarget)
    ForceAnimation(Characters.c0000_0006, 7410)
    AICommand(Characters.c0000_0006, command_id=-1, slot=0)
    ReplanAI(Characters.c0000_0006)


def Event11605033():
    """ 11605033: Event 11605033 """
    IfFlagOn(1, 11605031)
    IfCharacterHasSpecialEffect(1, Characters.c0000_0006, 2200)
    IfCharacterInsideRegion(1, Characters.c0000_0006, region=Cylinders.FourKingsDeathCutsceneTrigger)
    IfConditionTrue(0, input_condition=1)
    EnableInvincibility(Characters.c0000_0006)
    Wait(2.0)
    DisableInvincibility(Characters.c0000_0006)


def Event11605843(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11605843: Event 11605843 """
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


def Event11605846(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 11605846: Event 11605846 """
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
