"""
linked:


strings:

"""
from soulstruct.darksouls1r.events import *
from ..entities.m17_00_00_00_entities import *
from ..entities.common_entities import *


def Constructor():
    """ 0: Event 0 """
    SkipLinesIfFlagOff(1, 14)
    RegisterBonfire(
        11700920,
        obj=Objects.o0200_0002,
        reaction_distance=2.0,
        reaction_angle=180.0,
        initial_kindle_level=0,
    )
    RegisterBonfire(
        11700992,
        obj=Objects.o0200_0000,
        reaction_distance=2.0,
        reaction_angle=180.0,
        initial_kindle_level=0,
    )
    RegisterBonfire(
        11700984,
        obj=Objects.o0200_0001,
        reaction_distance=2.0,
        reaction_angle=180.0,
        initial_kindle_level=0,
    )
    RegisterBonfire(
        11700976,
        obj=Objects.o0200_0003,
        reaction_distance=2.0,
        reaction_angle=180.0,
        initial_kindle_level=0,
    )
    RegisterLadder(start_climbing_flag=11700010, stop_climbing_flag=11700011, obj=Objects.o7300)
    RegisterLadder(start_climbing_flag=11700012, stop_climbing_flag=11700013, obj=Objects.o7301)
    RegisterLadder(start_climbing_flag=11700014, stop_climbing_flag=11700015, obj=Objects.o7302)
    RegisterLadder(start_climbing_flag=11700016, stop_climbing_flag=11700017, obj=Objects.o7303)
    RegisterStatue(Objects.o0101_0000, game_map=DUKES_ARCHIVES, statue_type=StatueType.Crystal)
    RegisterStatue(Objects.o0101_0001, game_map=DUKES_ARCHIVES, statue_type=StatueType.Crystal)
    RegisterStatue(Objects.o0101_0002, game_map=DUKES_ARCHIVES, statue_type=StatueType.Crystal)
    RegisterStatue(Objects.o0101_0003, game_map=DUKES_ARCHIVES, statue_type=StatueType.Crystal)
    RegisterStatue(Objects.o0101_0004, game_map=DUKES_ARCHIVES, statue_type=StatueType.Crystal)
    RegisterStatue(Objects.o0101_0005, game_map=DUKES_ARCHIVES, statue_type=StatueType.Crystal)
    RegisterStatue(Objects.o0101_0006, game_map=DUKES_ARCHIVES, statue_type=StatueType.Crystal)
    RegisterStatue(Objects.o0101_0007, game_map=DUKES_ARCHIVES, statue_type=StatueType.Crystal)
    SkipLinesIfClient(5)
    EnableFlag(405)
    DisableObject(Objects.o7902_0000)
    DeleteVFX(VFX.MultiplayerFog1, erase_root_only=False)
    DisableObject(Objects.o7908_0000)
    DeleteVFX(VFX.MultiplayerFog2, erase_root_only=False)
    SkipLinesIfFlagOff(1, 11700140)
    DisableFlag(405)
    SkipLinesIfClient(9)
    SkipLinesIfFlagOff(6, 61700105)
    IfCharacterInsideRegion(1, PLAYER, region=Boxes.PrisonDoorReplaceMediumTrigger)
    IfCharacterInsideRegion(-1, PLAYER, region=Boxes.PrisonCell1)
    IfCharacterInsideRegion(-1, PLAYER, region=Boxes.PrisonCell2)
    IfConditionTrue(1, input_condition=-1)
    SkipLinesIfConditionTrue(2, 1)
    EnableFlag(61700105)
    SkipLines(1)
    DisableFlag(61700105)
    SkipLinesIfFlagOff(1, 11700002)
    EndOfAnimation(Objects.o7402, 0)
    SkipLinesIfFlagOff(1, 61700105)
    ForceAnimation(Objects.o7404, 1)
    RunEvent(
        11700083,
        slot=0,
        args=(Objects.o7906_0000, VFX.CheckpointFog2, Boxes.CheckpointFog2FrontSide, Boxes.CheckpointFog2BackSide),
    )
    RunEvent(11700085)
    RunEvent(11705380)
    RunEvent(11705381)
    RunEvent(11705386)
    RunEvent(11705382)
    RunEvent(11705383)
    RunEvent(11705384)
    RunEvent(11705385)
    RunEvent(11700110)
    RunEvent(11700120, slot=0, args=(11700120, Objects.o7250, Objects.o7201_00, 0, 0))
    RunEvent(11700120, slot=5, args=(11700125, Objects.o7251, 1701126, 1, 1))
    RunEvent(11700160, slot=0, args=(11700100, Objects.o7240, 11700210, 11700211, 11705090, 11705180, 11705181))
    RunEvent(
        11700105,
        slot=0,
        args=(11700100, Objects.o7240, Objects.o7201_01, Objects.o7201_05, 11705090, 11705180, 11705181),
    )
    RunEvent(11700160, slot=1, args=(11700102, Objects.o7241, 11700220, 11700221, 11705091, 11705182, 11705183))
    RunEvent(
        11700105,
        slot=2,
        args=(11700102, Objects.o7241, Objects.o7201_03, Objects.o7201_06, 11705091, 11705182, 11705183),
    )
    RunEvent(11700090, slot=0, args=(11700100, 0, Objects.o7201_01, 11705090), arg_types="iBii")
    RunEvent(11700090, slot=1, args=(11700100, 1, Objects.o7201_05, 11705090), arg_types="iBii")
    RunEvent(11700090, slot=2, args=(11700102, 0, Objects.o7201_03, 11705091), arg_types="iBii")
    RunEvent(11700090, slot=3, args=(11700102, 1, Objects.o7201_06, 11705091), arg_types="iBii")
    RunEvent(11705150, slot=0, args=(11700205, Objects.o7230_00, Objects.o7230_01))
    RunEvent(
        11700200,
        slot=0,
        args=(
            11700205,
            Objects.o7230_00,
            Objects.o7231,
            Collisions.h0124B0,
            Collisions.h0124B0_0000,
            Navigation.Navmesh_BeforeRotatingStairs0,
            Navigation.Navmesh_BeforeRotatingStairs1,
            11705151,
        ),
    )
    RunEvent(
        11700200,
        slot=1,
        args=(
            11700205,
            Objects.o7230_01,
            Objects.o7231_01,
            Collisions.h0125B0,
            Collisions.h0125B0_0000,
            Navigation.Navmesh_AfterRotatingStairs0,
            Navigation.Navmesh_AfterRotatingStairs1,
            11705152,
        ),
    )
    RunEvent(11700150, slot=0, args=(Collisions.h7500B0, Boxes.ElevatorEnemyWallToggle1))
    RunEvent(11700150, slot=1, args=(Collisions.h7501B0, Boxes.ElevatorEnemyWallToggle2))
    RunEvent(11705100)
    RunEvent(11705103)
    RunEvent(11705108)
    RunEvent(11705101)
    RunEvent(11705102)
    RunEvent(11700130)
    RunEvent(11700132)
    RunEvent(11700300, slot=0, args=(11700300, 10010863, Objects.o7401_00))
    RunEvent(11700300, slot=1, args=(11700311, 10010879, Objects.o7401_01))
    RunEvent(11700300, slot=2, args=(11700302, 10010863, Objects.o7401_02))
    RunEvent(11700300, slot=3, args=(11700313, 10010879, Objects.o7401_03))
    RunEvent(11700300, slot=4, args=(11700304, 10010863, Objects.o7401_04))
    RunEvent(11700300, slot=5, args=(11700305, 10010863, Objects.o7401_05))
    RunEvent(11700300, slot=6, args=(11700320, 10010865, Objects.o7401_06))
    RunEvent(11700140)
    RunEvent(11700141)
    RunEvent(11705170)
    RunEvent(11700700)
    DisableSoundEvent(1703800)
    SkipLinesIfFlagOff(5, 14)
    RunEvent(11705392)
    DisableObject(Objects.o7500)
    DisableObject(Objects.o7900_0000)
    DeleteVFX(VFX.SeathCaveEntranceFog, erase_root_only=False)
    SkipLines(10)
    RunEvent(11700000)
    RunEvent(11705390)
    RunEvent(11705391)
    RunEvent(11705393)
    RunEvent(11705392)
    RunEvent(11700001)
    RunEvent(11705394)
    RunEvent(11705395)
    RunEvent(11705396)
    RunEvent(11705397)
    RunEvent(11705200)
    RunEvent(11705270, slot=0, args=(Characters.c3250_0000, 15.0), arg_types="if")
    RunEvent(11705270, slot=1, args=(Characters.c3250_0001, 15.0), arg_types="if")
    RunEvent(11705140, slot=0, args=(Characters.c2690_0015, Cylinders.SerpentNest1))
    RunEvent(11705140, slot=1, args=(Characters.c2690_0014, Cylinders.SerpentNest2))
    RunEvent(11705160, slot=0, args=(Characters.c3230_0000, 3.0), arg_types="if")
    RunEvent(11705160, slot=1, args=(Characters.c3230_0001, 3.0), arg_types="if")
    RunEvent(11705160, slot=2, args=(Characters.c3230_0002, 10.0), arg_types="if")
    RunEvent(11705010, slot=0, args=(Characters.c2780_0000,))
    RunEvent(11705020, slot=0, args=(Characters.c2780_0000,))
    RunEvent(11705030, slot=0, args=(Characters.c2780_0000,))
    RunEvent(11705040, slot=0, args=(Characters.c2780_0000,))
    RunEvent(11705050, slot=0, args=(Characters.c2780_0000, Boxes.MimicNest0))
    RunEvent(11700900, slot=0, args=(Characters.c2780_0000,))
    RunEvent(11705060, slot=0, args=(Characters.c2780_0000,))
    RunEvent(11705010, slot=1, args=(Characters.c2780_0001,))
    RunEvent(11705020, slot=1, args=(Characters.c2780_0001,))
    RunEvent(11705030, slot=1, args=(Characters.c2780_0001,))
    RunEvent(11705040, slot=1, args=(Characters.c2780_0001,))
    RunEvent(11705050, slot=1, args=(Characters.c2780_0001, Boxes.MimicNest1))
    RunEvent(11700900, slot=1, args=(Characters.c2780_0001,))
    RunEvent(11705060, slot=1, args=(Characters.c2780_0001,))
    RunEvent(11700810, slot=0, args=(Characters.c0000_0005, 0, 0))
    RunEvent(11700810, slot=1, args=(Characters.c3300_0000, 1, 33001000))
    RunEvent(11700810, slot=2, args=(Characters.c3300_0001, 1, 33001000))
    RunEvent(11700810, slot=3, args=(Characters.c3300_0002, 1, 33001000))
    RunEvent(11700810, slot=4, args=(Characters.c3300_0003, 1, 33001000))
    RunEvent(11700810, slot=5, args=(Characters.c3461_0000, 0, 0))
    RunEvent(11700810, slot=6, args=(Characters.c3461_0001, 0, 0))
    RunEvent(11700810, slot=10, args=(Characters.c2711_0001, 0, 0))
    RunEvent(11700810, slot=11, args=(Characters.c2711_0002, 0, 0))
    RunEvent(11700810, slot=12, args=(Characters.c3330_0003, 0, 0))
    RunEvent(11700810, slot=13, args=(Characters.c3330_0004, 0, 0))
    RunEvent(11705280, slot=0, args=(Characters.c3230_0000,))
    RunEvent(11705280, slot=1, args=(Characters.c3230_0001,))
    RunEvent(11700600, slot=1, args=(Objects.o0110_0001, 11700601))
    RunEvent(11700600, slot=2, args=(Objects.o0110_0002, 11700602))
    RunEvent(11700600, slot=3, args=(Objects.o0110_0003, 11700603))
    RunEvent(11700600, slot=4, args=(Objects.o0110_0004, 11700604))
    RunEvent(11700600, slot=5, args=(1701655, 11700605))
    RunEvent(11700600, slot=6, args=(Objects.o0110_0006, 11700606))
    RunEvent(11700600, slot=7, args=(1701657, 11700607))
    RunEvent(11700600, slot=8, args=(Objects.o0110_0008, 11700608))
    RunEvent(11700600, slot=9, args=(Objects.o0110_0009, 11700609))
    RunEvent(11700600, slot=10, args=(Objects.o0110_0010, 11700610))
    RunEvent(11700600, slot=11, args=(1701661, 11700611))
    RunEvent(11700600, slot=12, args=(1701662, 11700612))
    RunEvent(11700600, slot=13, args=(Objects.o0110_0013, 11700613))
    RunEvent(11700600, slot=14, args=(Objects.o0110_0014, 11700614))
    RunEvent(11700600, slot=15, args=(Objects.o0110_0015, 11700615))
    RunEvent(11700600, slot=16, args=(Objects.o0110_0016, 11700616))
    RunEvent(11705110, slot=0, args=(Characters.c3330_0000,))
    RunEvent(11705110, slot=1, args=(Characters.c3330_0001,))
    RunEvent(11705110, slot=2, args=(Characters.c3330_0002,))
    RunEvent(11705110, slot=3, args=(Characters.c3330_0009,))
    RunEvent(11705110, slot=4, args=(Characters.c3330_0010,))
    RunEvent(11705110, slot=5, args=(Characters.c3330_0012,))
    RunEvent(11705110, slot=6, args=(Characters.c3330_0006,))
    RunEvent(11705110, slot=7, args=(Characters.c3330_0007,))
    RunEvent(11705110, slot=8, args=(Characters.c3330_0008,))
    RunEvent(11705110, slot=9, args=(1700119,))
    RunEvent(11705110, slot=10, args=(Characters.c3330_0005,))
    RunEvent(11705110, slot=11, args=(1700121,))
    RunEvent(11705110, slot=12, args=(1700122,))
    RunEvent(11705110, slot=13, args=(1700123,))
    RunEvent(11705110, slot=14, args=(1700124,))
    RunEvent(11705110, slot=15, args=(1700125,))
    RunEvent(11705110, slot=16, args=(1700126,))
    RunEvent(11705110, slot=17, args=(1700127,))
    RunEvent(11705110, slot=18, args=(Characters.c3330_0020,))
    RunEvent(11705110, slot=19, args=(Characters.c3330_0021,))
    RunEvent(
        11705843,
        slot=0,
        args=(14, Objects.o7900_0000, Boxes.SeathCaveFogPrompt, Boxes.SeathCaveFogRotationTarget),
    )
    RunEvent(11705846, slot=0, args=(14, Objects.o7900_0000, VFX.SeathCaveEntranceFog))
    
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
    HumanityRegistration(Characters.c0000_0005, 8988)
    HumanityRegistration(Characters.c0000_0002, 8334)
    HumanityRegistration(Characters.c0000_0006, 8334)
    SkipLinesIfFlagRangeAnyOn(1, (1093, 1096))
    DisableCharacter(Characters.c0000_0002)
    SkipLinesIfFlagOn(1, 1099)
    DisableCharacter(Characters.c0000_0006)
    SetTeamTypeAndExitStandbyAnimation(Characters.c0000_0006, TeamType.HostileAlly)
    SkipLinesIfFlagOff(1, 11700594)
    Move(
        Characters.c0000_0002,
        destination=Boxes.LoganInLibraryPoint,
        destination_type=CoordEntityType.Region,
        set_draw_parent=Collisions.h0041B0,
    )
    RunEvent(11700510, slot=0, args=(Characters.c0000_0002, 1096))
    RunEvent(11700520, slot=0, args=(Characters.c0000_0002, 1090, 1109, 1097))
    RunEvent(11700520, slot=1, args=(Characters.c0000_0006, 1090, 1109, 1097))
    RunEvent(11700530, slot=0, args=(Characters.c0000_0002, 1090, 1109, 1093))
    RunEvent(11700531, slot=0, args=(Characters.c0000_0002, 1090, 1109, 1094))
    RunEvent(11700532, slot=0, args=(Characters.c0000_0002, 1090, 1109, 1095))
    RunEvent(11700533, slot=0, args=(Characters.c0000_0002, 1090, 1109, 1099, Characters.c0000_0006))
    HumanityRegistration(Characters.c0000_0004, 8454)
    SkipLinesIfFlagOn(2, 1547)
    SkipLinesIfFlagOn(1, 1542)
    DisableCharacter(Characters.c0000_0004)
    RunEvent(11700510, slot=2, args=(Characters.c0000_0004, 1547))
    RunEvent(11700520, slot=2, args=(Characters.c0000_0004, 1540, 1569, 1548))
    RunEvent(11700538, slot=0, args=(Characters.c0000_0004, 1540, 1569, 1541))
    RunEvent(11700539, slot=0, args=(Characters.c0000_0004, 1540, 1569, 1542))
    RunEvent(11700540, slot=0, args=(Characters.c0000_0004, 1540, 1569, 1543))
    SetTeamTypeAndExitStandbyAnimation(Characters.c0000_0003, TeamType.HostileAlly)
    SkipLinesIfFlagOn(1, 1181)
    DisableCharacter(Characters.c0000_0003)
    RunEvent(11700520, slot=3, args=(Characters.c0000_0003, 1170, 1189, 1177))
    RunEvent(11700545, slot=0, args=(Characters.c0000_0003, 1170, 1189, 1181))


def Event11700080(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11700080: Event 11700080 """
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
    IfFlagOn(3, 11700080)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EnableFlag(11700080)
    SkipLinesIfFinishedConditionTrue(5, 3)
    SkipLinesIfFinishedConditionTrue(2, 2)
    Move(PLAYER, destination=arg_8_11, destination_type=CoordEntityType.Region, short_move=True)
    SkipLines(1)
    Move(PLAYER, destination=arg_12_15, destination_type=CoordEntityType.Region, short_move=True)
    ForceAnimation(PLAYER, 7410)
    DisableObject(arg_0_3)
    DeleteVFX(arg_4_7, erase_root_only=True)


def Event11700083(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11700083: Event 11700083 """
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


def Event11700085():
    """ 11700085: Event 11700085 """
    SkipLinesIfFlagOff(4, 11800100)
    EnableFlag(11700086)
    DisableObject(Objects.o7907_0000)
    DeleteVFX(VFX.GoldenFog, erase_root_only=False)
    End()
    SkipLinesIfFlagOff(3, 11700086)
    DisableObject(Objects.o7907_0000)
    DeleteVFX(VFX.GoldenFog, erase_root_only=False)
    End()
    EndIfClient()
    IfActionButton(
        0,
        prompt_text=10010410,
        anchor_entity=Boxes.AtGoldenFog,
        anchor_type=CoordEntityType.Region,
        model_point=0,
        line_intersects=Objects.o7907_0000,
    )
    DisplayStatus(10010630, pad_enabled=True)
    Restart()


@RestartOnRest
def Event11700000():
    """ 11700000: Event 11700000 """
    EndIfThisEventOn()
    DisableObject(Objects.o7900_0000)
    DeleteVFX(VFX.SeathCaveEntranceFog, erase_root_only=False)
    DisableCharacter(Characters.c5290_0001)
    EnableObjectInvulnerability(Objects.o7500)
    IfThisEventOff(1)
    IfHost(1)
    IfCharacterInsideRegion(1, PLAYER, region=Boxes.SeathCutsceneTrigger)
    IfConditionTrue(0, input_condition=1)
    SkipLinesIfClient(1)
    NotifyBossBattleStart()
    ActivateMultiplayerBuffs(Characters.c5290_0001)
    EnableFlag(11705390)
    EnableFlag(11705391)
    EnableFlag(11705393)
    IfCharacterType(2, PLAYER, CharacterType.BlackPhantom)
    SkipLinesIfConditionFalse(1, 2)
    IfFlagOn(0, 703)
    SkipLinesIfMultiplayer(2)
    PlayCutscene(
        170000,
        skippable=True,
        fade_out=False,
        player_id=PLAYER,
        move_to_region=Boxes.PlayerPointAfterSeathCutscene,
        move_to_map=DUKES_ARCHIVES,
    )
    SkipLines(4)
    SkipLinesIfClient(2)
    PlayCutscene(
        170000,
        skippable=False,
        fade_out=False,
        player_id=PLAYER,
        move_to_region=Boxes.PlayerPointAfterSeathCutscene,
        move_to_map=DUKES_ARCHIVES,
    )
    SkipLines(1)
    PlayCutscene(170000, skippable=False, fade_out=False, player_id=PLAYER)
    WaitFrames(1)
    DisableObjectInvulnerability(Objects.o7500)
    EnableObject(Objects.o7900_0000)
    CreateVFX(VFX.SeathCaveEntranceFog)
    Move(
        Characters.c5290_0001,
        destination=Boxes.SeathPointAfterSeathCutscene,
        destination_type=CoordEntityType.Region,
        short_move=True,
    )
    EnableCharacter(Characters.c5290_0001)


def Event11705380():
    """ 11705380: Event 11705380 """
    IfFlagOff(1, 11700000)
    IfActionButton(
        1,
        prompt_text=10010403,
        anchor_entity=Boxes.SeathTowerFogPrompt,
        anchor_type=CoordEntityType.Region,
        line_intersects=Objects.o7901_0000,
        boss_version=True,
    )
    IfConditionTrue(0, input_condition=1)
    RotateToFaceEntity(PLAYER, Boxes.SeathTowerFogRotationTarget)
    ForceAnimation(PLAYER, 7410)
    Restart()


def Event11705381():
    """ 11705381: Event 11705381 """
    IfFlagOff(1, 11700000)
    IfFlagOn(1, 11705386)
    IfCharacterType(1, PLAYER, CharacterType.WhitePhantom)
    IfActionButton(
        1,
        prompt_text=10010403,
        anchor_entity=Boxes.SeathTowerFogPrompt,
        anchor_type=CoordEntityType.Region,
        trigger_attribute=TriggerAttribute.All,
        line_intersects=Objects.o7901_0000,
    )
    IfConditionTrue(0, input_condition=1)
    RotateToFaceEntity(PLAYER, Boxes.SeathTowerFogRotationTarget)
    ForceAnimation(PLAYER, 7410)
    Restart()


def Event11705386():
    """ 11705386: Event 11705386 """
    SkipLinesIfThisEventOn(3)
    IfFlagOff(1, 11700000)
    IfCharacterInsideRegion(1, PLAYER, region=Boxes.SeathTowerCombatStart)
    IfConditionTrue(0, input_condition=1)
    SkipLinesIfClient(1)
    NotifyBossBattleStart()
    ActivateMultiplayerBuffs(Characters.c5290_0000)


def Event11705382():
    """ 11705382: Event 11705382 """
    DisableNetworkSync()
    IfFlagOff(1, 11700000)
    IfActionButton(
        1,
        prompt_text=10010404,
        anchor_entity=Boxes.SeathTowerFogExitPrompt,
        anchor_type=CoordEntityType.Region,
        trigger_attribute=TriggerAttribute.All,
        line_intersects=Objects.o7901_0000,
    )
    IfConditionTrue(0, input_condition=1)
    RotateToFaceEntity(PLAYER, Boxes.SeathTowerFogExitRotationTarget)
    ForceAnimation(PLAYER, 7410, wait_for_completion=True)
    DisableBossHealthBar(Characters.c5290_0000, name=5290, slot=0)
    Restart()


@RestartOnRest
def Event11705383():
    """ 11705383: Event 11705383 """
    DisableAI(Characters.c5290_0000)
    IfFlagOff(1, 11700000)
    IfFlagOn(1, 11705386)
    IfCharacterInsideRegion(1, PLAYER, region=Boxes.SeathTowerMusic)
    IfConditionTrue(0, input_condition=1)
    EnableAI(Characters.c5290_0000)
    EnableBossHealthBar(Characters.c5290_0000, name=5290, slot=0)
    IfAllPlayersOutsideRegion(0, region=Boxes.SeathTowerMusic)
    Restart()


def Event11705384():
    """ 11705384: Event 11705384 """
    DisableNetworkSync()
    DisableSoundEvent(1703801)
    IfFlagOff(1, 11700000)
    IfFlagOn(1, 11705386)
    IfCharacterInsideRegion(1, PLAYER, region=Boxes.SeathTowerMusic)
    IfConditionTrue(0, input_condition=1)
    EnableSoundEvent(1703801)
    IfFlagOn(-1, 11700000)
    IfCharacterOutsideRegion(-1, PLAYER, region=Boxes.SeathTowerMusic)
    IfConditionTrue(0, input_condition=-1)
    Restart()


@RestartOnRest
def Event11705385():
    """ 11705385: Event 11705385 """
    EnableImmortality(Characters.c5290_0000)
    AddSpecialEffect(Characters.c5290_0000, 5441)
    AddSpecialEffect(Characters.c5290_0000, 5442)
    AddSpecialEffect(Characters.c5290_0000, 5443)
    IfFlagOn(0, 11700000)
    DisableCharacter(Characters.c5290_0000)
    DisableObject(Objects.o7510)
    DisableObject(Objects.o7901_0000)
    DeleteVFX(VFX.SeathTowerEntranceFog, erase_root_only=True)


def Event11705390():
    """ 11705390: Event 11705390 """
    IfFlagOff(1, 14)
    IfFlagOn(1, 11700000)
    IfActionButton(
        1,
        prompt_text=10010403,
        anchor_entity=Boxes.SeathCaveFogPrompt,
        anchor_type=CoordEntityType.Region,
        line_intersects=Objects.o7900_0000,
        boss_version=True,
    )
    IfConditionTrue(0, input_condition=1)
    SkipLinesIfClient(1)
    NotifyBossBattleStart()
    RotateToFaceEntity(PLAYER, Boxes.SeathCaveFogRotationTarget)
    ForceAnimation(PLAYER, 7410, wait_for_completion=True)
    ActivateMultiplayerBuffs(Characters.c5290_0001)
    Restart()


def Event11705391():
    """ 11705391: Event 11705391 """
    IfFlagOff(1, 14)
    IfFlagOn(1, 11705393)
    IfCharacterType(1, PLAYER, CharacterType.WhitePhantom)
    IfCharacterAlive(1, Characters.c5290_0001)
    IfActionButton(
        1,
        prompt_text=10010403,
        anchor_entity=Boxes.SeathCaveFogPrompt,
        anchor_type=CoordEntityType.Region,
        trigger_attribute=TriggerAttribute.All,
        line_intersects=Objects.o7900_0000,
    )
    IfConditionTrue(0, input_condition=1)
    RotateToFaceEntity(PLAYER, Boxes.SeathCaveFogRotationTarget)
    ForceAnimation(PLAYER, 7410)
    Restart()


def Event11705393():
    """ 11705393: Event 11705393 """
    SkipLinesIfThisEventOn(8)
    IfFlagOn(1, 11700000)
    IfFlagOff(1, 14)
    IfCharacterInsideRegion(1, PLAYER, region=Boxes.SeathCaveCombatStart)
    IfThisEventOn(2)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(2)
    SkipLinesIfClient(1)
    NotifyBossBattleStart()
    ActivateMultiplayerBuffs(Characters.c5290_0001)


@RestartOnRest
def Event11705392():
    """ 11705392: Event 11705392 """
    SkipLinesIfFlagOff(5, 14)
    DisableCharacter(Characters.c5290_0001)
    Kill(Characters.c5290_0001, award_souls=False)
    DisableCharacter(Characters.c5291_0000)
    Kill(Characters.c5291_0000, award_souls=False)
    End()
    DisableAI(Characters.c5290_0001)
    IfFlagOn(1, 11705393)
    IfCharacterInsideRegion(1, PLAYER, region=Boxes.SeathCaveMusic)
    IfConditionTrue(0, input_condition=1)
    EnableAI(Characters.c5290_0001)
    EnableBossHealthBar(Characters.c5290_0001, name=5290, slot=0)


def Event11700001():
    """ 11700001: Event 11700001 """
    DisableObject(Objects.o0200_0002)
    IfCharacterDead(0, Characters.c5290_0001)
    EnableFlag(14)
    KillBoss(1700800)
    SkipLinesIfClient(1)
    AwardAchievement(38)
    DisableObject(Objects.o7900_0000)
    DeleteVFX(VFX.SeathCaveEntranceFog, erase_root_only=True)
    CreateTemporaryVFX(90014, anchor_entity=Objects.o0200_0002, anchor_type=CoordEntityType.Object, model_point=-1)
    Wait(2.0)
    EnableObject(Objects.o0200_0002)
    RegisterBonfire(
        11700920,
        obj=Objects.o0200_0002,
        reaction_distance=2.0,
        reaction_angle=180.0,
        initial_kindle_level=0,
    )


def Event11705394():
    """ 11705394: Event 11705394 """
    DisableNetworkSync()
    IfFlagOff(1, 14)
    IfFlagOn(1, 11705392)
    SkipLinesIfHost(1)
    IfFlagOn(1, 11705391)
    IfCharacterInsideRegion(1, PLAYER, region=Boxes.SeathCaveMusic)
    IfConditionTrue(0, input_condition=1)
    EnableSoundEvent(1703800)


def Event11705395():
    """ 11705395: Event 11705395 """
    DisableNetworkSync()
    IfFlagOn(1, 14)
    IfFlagOn(1, 11705394)
    IfConditionTrue(0, input_condition=1)
    DisableSoundEvent(1703800)


@RestartOnRest
def Event11705396():
    """ 11705396: Event 11705396 """
    AddSpecialEffect(Characters.c5290_0001, 5440)
    AddSpecialEffect(Characters.c5290_0001, 5441)
    AddSpecialEffect(Characters.c5290_0001, 5442)
    AddSpecialEffect(Characters.c5290_0001, 5443)
    EnableImmortality(Characters.c5290_0001)
    CreateObjectVFX(170004, obj=Objects.o7500, model_point=100)
    IfObjectDestroyed(0, Objects.o7500)
    DeleteObjectVFX(1703100, erase_root=True)
    ForceAnimation(Characters.c5290_0001, 7000)
    IfHasTAEEvent(0, Characters.c5290_0001, tae_event_id=500)
    CancelSpecialEffect(Characters.c5290_0001, 5440)
    CancelSpecialEffect(Characters.c5290_0001, 5441)
    CancelSpecialEffect(Characters.c5290_0001, 5442)
    CancelSpecialEffect(Characters.c5290_0001, 5443)
    DisableImmortality(Characters.c5290_0001)


@RestartOnRest
def Event11705397():
    """ 11705397: Event 11705397 """
    DisableCharacter(Characters.c5291_0000)
    EndIfFlagOn(14)
    SkipLinesIfThisEventOff(4)
    SetDisplayMask(Characters.c5290_0001, bit_index=1, switch_type=OnOffChange.On)
    SetCollisionMask(Characters.c5290_0001, bit_index=1, switch_type=OnOffChange.Off)
    AICommand(Characters.c5290_0001, command_id=20, slot=0)
    End()
    IfCharacterBackreadEnabled(0, Characters.c5290_0001)
    CreateNPCPart(
        Characters.c5290_0001,
        npc_part_id=5290,
        part_index=NPCPartType.Part1,
        part_health=330,
        damage_correction=1.0,
        body_damage_correction=1.0,
        is_invincible=False,
        start_in_stop_state=False,
    )
    IfHealthGreaterThan(1, Characters.c5290_0001, 0.0)
    IfCharacterPartHealthLessThanOrEqual(1, Characters.c5290_0001, npc_part_id=5290, value=0)
    IfHealthLessThanOrEqual(2, Characters.c5290_0001, 0.0)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(2)
    ForceAnimation(Characters.c5290_0001, 8000)
    IfHasTAEEvent(0, Characters.c5290_0001, tae_event_id=400)
    Move(
        Characters.c5291_0000,
        destination=Characters.c5290_0001,
        destination_type=CoordEntityType.Character,
        model_point=150,
        copy_draw_parent=Characters.c5290_0001,
    )
    EnableCharacter(Characters.c5291_0000)
    SetDisplayMask(Characters.c5290_0001, bit_index=1, switch_type=OnOffChange.On)
    SetCollisionMask(Characters.c5290_0001, bit_index=1, switch_type=OnOffChange.Off)
    ForceAnimation(Characters.c5291_0000, 8100)
    AICommand(Characters.c5290_0001, command_id=20, slot=0)
    ReplanAI(Characters.c5290_0001)
    IfCharacterHuman(-7, PLAYER)
    IfCharacterHollow(-7, PLAYER)
    EndIfConditionFalse(-7)
    AwardItemLot(52910000, host_only=True)


def Event11700160(
    _,
    arg_0_3: int,
    arg_4_7: int,
    arg_8_11: int,
    arg_12_15: int,
    arg_16_19: int,
    arg_20_23: int,
    arg_24_27: int,
):
    """ 11700160: Event 11700160 """
    IfFlagOff(1, arg_16_19)
    IfActionButton(
        1,
        prompt_text=10010501,
        anchor_entity=arg_4_7,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        model_point=192,
        trigger_attribute=TriggerAttribute.All,
    )
    IfObjectActivated(2, obj_act_id=arg_8_11)
    IfObjectActivated(3, obj_act_id=arg_12_15)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EnableFlag(arg_16_19)
    SkipLinesIfFinishedConditionTrue(2, 3)
    SkipLinesIfFinishedConditionTrue(9, 2)
    SkipLinesIfFlagOn(8, arg_0_3)
    SkipLinesIfFinishedConditionFalse(4, 1)
    Move(PLAYER, destination=arg_4_7, destination_type=CoordEntityType.Object, model_point=191, short_move=True)
    ForceAnimation(PLAYER, 8000)
    ForceAnimation(arg_4_7, 0)
    WaitFrames(105)
    EnableFlag(arg_20_23)
    IfFlagOff(0, arg_16_19)
    Restart()
    SkipLinesIfFinishedConditionFalse(4, 1)
    Move(PLAYER, destination=arg_4_7, destination_type=CoordEntityType.Object, model_point=191, short_move=True)
    ForceAnimation(PLAYER, 8000)
    ForceAnimation(arg_4_7, 2)
    WaitFrames(105)
    EnableFlag(arg_24_27)
    IfFlagOff(0, arg_16_19)
    Restart()


def Event11700105(
    _,
    arg_0_3: int,
    arg_4_7: int,
    arg_8_11: int,
    arg_12_15: int,
    arg_16_19: int,
    arg_20_23: int,
    arg_24_27: int,
):
    """ 11700105: Event 11700105 """
    SkipLinesIfFlagOff(4, arg_0_3)
    EndOfAnimation(arg_4_7, 11)
    EnableObjectActivation(arg_8_11, obj_act_id=-1)
    DisableObjectActivation(arg_12_15, obj_act_id=-1)
    SkipLines(2)
    DisableObjectActivation(arg_8_11, obj_act_id=-1)
    EnableObjectActivation(arg_12_15, obj_act_id=-1)
    IfHost(1)
    IfFlagOn(1, arg_20_23)
    IfHost(2)
    IfFlagOn(2, arg_24_27)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    DisableFlag(arg_20_23)
    DisableFlag(arg_24_27)
    DisableObjectActivation(arg_8_11, obj_act_id=-1)
    DisableObjectActivation(arg_12_15, obj_act_id=-1)
    SkipLinesIfFinishedConditionTrue(5, 2)
    EnableFlag(arg_0_3)
    ForceAnimation(arg_4_7, 1)
    WaitFrames(300)
    DisableFlag(arg_16_19)
    Restart()
    DisableFlag(arg_0_3)
    ForceAnimation(arg_4_7, 3)
    WaitFrames(344)
    DisableFlag(arg_16_19)
    Restart()


def Event11700090(_, arg_0_3: int, arg_4_4: uchar, arg_8_11: int, arg_12_15: int):
    """ 11700090: Event 11700090 """
    DisableNetworkSync()
    IfFlagState(1, state=arg_4_4, flag_type=FlagType.Absolute, flag=arg_0_3)
    IfFlagOff(1, arg_12_15)
    IfActionButton(
        1,
        prompt_text=10010501,
        anchor_entity=arg_8_11,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        model_point=195,
        trigger_attribute=TriggerAttribute.All,
    )
    IfConditionTrue(0, input_condition=1)
    DisplayDialog(
        10010170,
        anchor_entity=arg_8_11,
        display_distance=3.0,
        button_type=ButtonType.OK_or_Cancel,
        number_buttons=NumberButtons.NoButton,
    )
    Restart()


def Event11705150(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 11705150: Event 11705150 """
    IfActionButton(
        1,
        prompt_text=10010503,
        anchor_entity=arg_4_7,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        model_point=192,
        trigger_attribute=TriggerAttribute.All,
    )
    IfActionButton(
        2,
        prompt_text=10010503,
        anchor_entity=arg_8_11,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        model_point=192,
        trigger_attribute=TriggerAttribute.All,
    )
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionFalse(7, 1)
    Move(PLAYER, destination=arg_4_7, destination_type=CoordEntityType.Object, model_point=191, short_move=True)
    SkipLinesIfFlagOn(2, arg_0_3)
    ForceAnimation(arg_4_7, 0)
    SkipLines(1)
    ForceAnimation(arg_4_7, 2)
    ForceAnimation(PLAYER, 8010)
    WaitFrames(105)
    SkipLinesIfFinishedConditionFalse(7, 2)
    Move(PLAYER, destination=arg_8_11, destination_type=CoordEntityType.Object, model_point=191, short_move=True)
    SkipLinesIfFlagOn(2, arg_0_3)
    ForceAnimation(arg_8_11, 0)
    SkipLines(1)
    ForceAnimation(arg_8_11, 2)
    ForceAnimation(PLAYER, 8010)
    WaitFrames(105)
    EnableFlag(11705151)
    EnableFlag(11705152)
    IfFlagOff(3, 11705151)
    IfFlagOff(3, 11705152)
    IfConditionTrue(0, input_condition=3)
    Restart()


def Event11700200(
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
    """ 11700200: Event 11700200 """
    DisableObject(arg_8_11)
    SkipLinesIfFlagOn(5, arg_0_3)
    EndOfAnimation(arg_4_7, 3)
    DisableCollision(arg_16_19)
    DisableNavmeshType(arg_20_23, NavmeshType.Solid)
    EnableNavmeshType(arg_24_27, NavmeshType.Solid)
    SkipLines(4)
    EndOfAnimation(arg_4_7, 1)
    DisableCollision(arg_12_15)
    EnableNavmeshType(arg_20_23, NavmeshType.Solid)
    DisableNavmeshType(arg_24_27, NavmeshType.Solid)
    IfFlagOn(0, arg_28_31)
    SkipLinesIfFlagOn(11, arg_0_3)
    ForceAnimation(arg_4_7, 1)
    DisableCollision(arg_12_15)
    EnableObject(arg_8_11)
    EnableNavmeshType(arg_20_23, NavmeshType.Solid)
    ForceAnimation(arg_8_11, 1)
    WaitFrames(180)
    DisableObject(arg_8_11)
    EnableCollision(arg_16_19)
    EnableFlag(arg_0_3)
    DisableFlag(arg_28_31)
    Restart()
    ForceAnimation(arg_4_7, 3)
    DisableCollision(arg_16_19)
    EnableObject(arg_8_11)
    EnableNavmeshType(arg_24_27, NavmeshType.Solid)
    ForceAnimation(arg_8_11, 3)
    WaitFrames(180)
    DisableObject(arg_8_11)
    EnableCollision(arg_12_15)
    DisableFlag(arg_0_3)
    DisableFlag(arg_28_31)
    Restart()


def Event11700110():
    """ 11700110: Event 11700110 """
    SkipLinesIfThisEventOff(5)
    DisableObjectActivation(Objects.o7201_04, obj_act_id=-1)
    EndOfAnimation(Objects.o7200_00, 0)
    DisableObject(Objects.o7199)
    DisableCollision(Collisions.h0042B0)
    End()
    DisableObject(Objects.o7199)
    DisableCollision(Collisions.h0043B0)
    IfObjectActivated(0, obj_act_id=11700110)
    DisableCollision(Collisions.h0042B0)
    EnableObject(Objects.o7199)
    ForceAnimation(Objects.o7200_00, 0)
    ForceAnimation(Objects.o7199, 0, wait_for_completion=True)
    DisableObject(Objects.o7199)
    EnableCollision(Collisions.h0043B0)


def Event11700120(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int):
    """ 11700120: Event 11700120 """
    SkipLinesIfThisEventSlotOff(4)
    SkipLinesIfEqual(1, left=arg_16_19, right=1)
    DisableObjectActivation(arg_8_11, obj_act_id=-1)
    EndOfAnimation(arg_4_7, arg_12_15)
    End()
    SkipLinesIfEqual(1, left=arg_16_19, right=0)
    IfFlagOn(-1, 11700140)
    IfObjectActivated(-1, obj_act_id=arg_0_3)
    IfConditionTrue(0, input_condition=-1)
    EnableFlag(arg_0_3)
    ForceAnimation(arg_4_7, arg_12_15)


def Event11700150(_, arg_0_3: int, arg_4_7: int):
    """ 11700150: Event 11700150 """
    IfAllPlayersOutsideRegion(0, region=arg_4_7)
    EnableCollision(arg_0_3)
    IfCharacterInsideRegion(0, PLAYER, region=arg_4_7)
    DisableCollision(arg_0_3)
    Restart()


def Event11705100():
    """ 11705100: Event 11705100 """
    DisableNetworkSync()
    IfCharacterInsideRegion(1, PLAYER, region=Boxes.SeathTowerMusic)
    IfHost(1)
    IfCharacterDead(1, PLAYER)
    IfConditionTrue(0, input_condition=1)
    SetRespawnPoint(SpawnPoints.SpawnPointInPrison)
    SaveRequest()


def Event11705101():
    """ 11705101: Event 11705101 """
    IfHost(1)
    SkipLinesIfClient(1)
    IfFlagOn(1, 51700990)
    IfFlagOff(1, 11705101)
    IfFlagOff(1, 11700133)
    IfCharacterInsideRegion(1, PLAYER, region=Cylinders.PishacaAlertArea)
    IfHost(2)
    IfFlagOn(2, 11705106)
    IfHost(3)
    IfFlagOn(3, 11705107)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    DisableFlag(11705106)
    DisableFlag(11705107)
    SkipLinesIfFlagOn(9, 11700002)
    SkipLinesIfFinishedConditionFalse(8, 1)
    SkipLinesIfMultiplayer(2)
    PlayCutscene(170010, skippable=True, fade_out=False, player_id=PLAYER)
    SkipLines(1)
    PlayCutscene(170010, skippable=False, fade_out=False, player_id=PLAYER)
    WaitFrames(1)
    ForceAnimation(Objects.o7402, 0)
    EnableFlag(11700002)
    EnableFlag(61700105)
    SkipLinesIfFinishedConditionTrue(1, 1)
    SkipLinesIfFinishedConditionTrue(9, 3)
    SkipLinesIfFlagOn(2, 61700105)
    RunEvent(11705108)
    Restart()
    EnableSoundEvent(1703500)
    ForceAnimation(Objects.o7404, 0)
    WaitFrames(150)
    ForceAnimation(Objects.o7404, 1)
    RunEvent(11705108)
    Restart()
    SkipLinesIfFlagOff(2, 61700105)
    RunEvent(11705108)
    Restart()
    DisableSoundEvent(1703500)
    EnableFlag(11700133)
    ForceAnimation(Objects.o7404, 2)
    WaitFrames(50)
    RunEvent(11705108)
    Restart()


def Event11705102():
    """ 11705102: Event 11705102 """
    DisableNetworkSync()
    SkipLinesIfFlagOn(1, 61700105)
    DisableSoundEvent(1703500)


def Event11705103():
    """ 11705103: Event 11705103 """
    IfFlagOn(1, 61700105)
    IfObjectActivated(1, obj_act_id=11705105)
    IfFlagOff(2, 61700105)
    IfObjectActivated(2, obj_act_id=11705105)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    DisableFlag(11705106)
    DisableFlag(11705107)
    SkipLinesIfFinishedConditionTrue(2, 2)
    EnableFlag(11705106)
    Restart()
    EnableFlag(11705107)
    Restart()


def Event11705108():
    """ 11705108: Event 11705108 """
    DisableNetworkSync()
    IfFramesElapsed(1, 10)
    IfInsideMap(1, game_map=DUKES_ARCHIVES)
    IfConditionTrue(0, input_condition=1)
    EnableObjectActivation(Objects.o7202, obj_act_id=-1)


@RestartOnRest
def Event11705110(_, arg_0_3: int):
    """ 11705110: Event 11705110 """
    IfFlagOn(1, 61700105)
    IfCharacterInsideRegion(-7, PLAYER, region=Cylinders.PishacaAlertArea)
    IfCharacterInsideRegion(-7, PLAYER, region=Boxes.PisacaNestCombatArea)
    IfConditionTrue(1, input_condition=-7)
    IfFlagOn(2, 61700105)
    IfAllPlayersOutsideRegion(2, region=Cylinders.PishacaAlertArea)
    IfAllPlayersOutsideRegion(2, region=Boxes.PisacaNestCombatArea)
    IfFlagOff(3, 61700105)
    IfFlagOn(3, 11700002)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionFalse(8, 1)
    AICommand(arg_0_3, command_id=1, slot=0)
    ReplanAI(arg_0_3)
    IfAllPlayersOutsideRegion(7, region=Cylinders.PishacaAlertArea)
    IfAllPlayersOutsideRegion(7, region=Boxes.PisacaNestCombatArea)
    IfConditionTrue(-2, input_condition=7)
    IfFlagOff(-2, 61700105)
    IfConditionTrue(0, input_condition=-2)
    Restart()
    SkipLinesIfFinishedConditionFalse(7, 2)
    AICommand(arg_0_3, command_id=2, slot=0)
    ReplanAI(arg_0_3)
    IfCharacterInsideRegion(-3, PLAYER, region=Cylinders.PishacaAlertArea)
    IfCharacterInsideRegion(-3, PLAYER, region=Boxes.PisacaNestCombatArea)
    IfFlagOff(-3, 61700105)
    IfConditionTrue(0, input_condition=-3)
    Restart()
    AICommand(arg_0_3, command_id=3, slot=0)
    ReplanAI(arg_0_3)
    IfFlagOn(0, 61700105)
    Restart()


@RestartOnRest
def Event11700130():
    """ 11700130: Event 11700130 """
    EndIfClient()
    SkipLinesIfFlagOff(3, 51700990)
    DisableCharacter(Characters.c2690_0000)
    Kill(Characters.c2690_0000, award_souls=False)
    End()
    DisableCharacterCollision(Characters.c2690_0000)
    DisableGravity(Characters.c2690_0000)


@RestartOnRest
def Event11705140(_, arg_0_3: int, arg_4_7: int):
    """ 11705140: Event 11705140 """
    EndIfThisEventSlotOn()
    IfFlagOn(0, 11705101)
    SetNest(arg_0_3, arg_4_7)
    AICommand(arg_0_3, command_id=10, slot=0)
    ReplanAI(arg_0_3)
    IfThisEventSlotOn(-1)
    IfCharacterInsideRegion(-1, arg_0_3, region=arg_4_7)
    IfConditionTrue(0, input_condition=-1)
    ClearTargetList(arg_0_3)
    AICommand(arg_0_3, command_id=-1, slot=0)
    ReplanAI(arg_0_3)


def Event11700140():
    """ 11700140: Event 11700140 """
    SkipLinesIfThisEventOff(2)
    EndOfAnimation(Objects.o7400, 0)
    End()
    IfPlayerHasGood(1, 2005, including_box=False)
    IfActionButton(
        1,
        prompt_text=10010400,
        anchor_entity=Objects.o7400,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        model_point=100,
    )
    IfFlagOn(2, 14)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    DisableFlag(405)
    SkipLinesIfFinishedConditionTrue(2, 2)
    Move(PLAYER, destination=Objects.o7400, destination_type=CoordEntityType.Object, model_point=120, short_move=True)
    ForceAnimation(PLAYER, 7120)
    ForceAnimation(Objects.o7400, 0)
    EndIfClient()
    DisplayDialog(
        10010864,
        anchor_entity=Objects.o7400,
        display_distance=3.0,
        button_type=ButtonType.Yes_or_No,
        number_buttons=NumberButtons.NoButton,
    )
    End()


def Event11700141():
    """ 11700141: Event 11700141 """
    DisableNetworkSync()
    IfFlagOff(1, 11700140)
    IfPlayerDoesNotHaveGood(1, 2005, including_box=False)
    IfActionButton(
        1,
        prompt_text=10010400,
        anchor_entity=Objects.o7400,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        model_point=100,
        trigger_attribute=TriggerAttribute.All,
    )
    IfFlagOff(2, 11700140)
    IfActionButton(
        2,
        prompt_text=10010400,
        anchor_entity=Objects.o7400,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        model_point=101,
        trigger_attribute=TriggerAttribute.All,
    )
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    DisplayDialog(
        10010163,
        anchor_entity=Objects.o7400,
        display_distance=3.0,
        button_type=ButtonType.OK_or_Cancel,
        number_buttons=NumberButtons.NoButton,
    )
    Restart()


@RestartOnRest
def Event11705170():
    """ 11705170: Event 11705170 """
    DisableNetworkSync()
    EndIfClient()
    DisableFlag(11705170)
    IfCharacterInsideRegion(0, PLAYER, region=Boxes.PrisonCell1)
    EnableFlag(11705170)
    IfCharacterOutsideRegion(0, PLAYER, region=Boxes.PrisonCell1)
    Restart()


@RestartOnRest
def Event11705160(_, arg_0_3: int, arg_4_7: float):
    """ 11705160: Event 11705160 """
    SkipLinesIfThisEventSlotOff(2)
    ResetStandbyAnimationSettings(arg_0_3)
    End()
    IfEntityWithinDistance(0, arg_0_3, PLAYER, radius=arg_4_7)
    SetStandbyAnimationSettings(arg_0_3, cancel_animation=13000)


@RestartOnRest
def Event11705250(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 11705250: Event 11705250 """
    EndIfThisEventSlotOn()
    DisableAI(arg_4_7)
    IfCharacterInsideRegion(-1, PLAYER, region=arg_0_3)
    IfAttacked(-1, arg_4_7, attacker=PLAYER)
    IfConditionTrue(0, input_condition=-1)
    ForceAnimation(arg_4_7, arg_8_11, wait_for_completion=True)
    EnableAI(arg_4_7)


@RestartOnRest
def Event11705270(_, arg_0_3: int, arg_4_7: float):
    """ 11705270: Event 11705270 """
    EndIfThisEventSlotOn()
    SetStandbyAnimationSettings(arg_0_3, standby_animation=9000)
    IfEntityWithinDistance(-1, arg_0_3, PLAYER, radius=arg_4_7)
    IfAttacked(-1, arg_0_3, attacker=PLAYER)
    IfConditionTrue(0, input_condition=-1)
    SetStandbyAnimationSettings(arg_0_3, cancel_animation=9060)


def Event11700300(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 11700300: Event 11700300 """
    EndIfClient()
    EndIfThisEventSlotOn()
    IfObjectActivated(0, obj_act_id=arg_0_3)
    EnableFlag(arg_0_3)
    DisplayDialog(
        arg_4_7,
        anchor_entity=arg_8_11,
        display_distance=3.0,
        button_type=ButtonType.Yes_or_No,
        number_buttons=NumberButtons.NoButton,
    )


@RestartOnRest
def Event11705200():
    """ 11705200: Event 11705200 """
    RunEvent(11705240, slot=0, args=(Characters.c2370_0002,))
    RunEvent(11705240, slot=1, args=(Characters.c2370_0003,))
    RunEvent(11705240, slot=2, args=(Characters.c2370_0004,))
    RunEvent(11705240, slot=3, args=(Characters.c2370_0005,))
    RunEvent(11705201, slot=0, args=(11705200, Characters.c2370_0000, Boxes.ChannelerWarpPoint_00_00, 11705202))
    RunEvent(11705201, slot=1, args=(11705201, Characters.c2370_0000, Boxes.ChannelerWarpPoint_00_05, 11705202))
    RunEvent(11705201, slot=2, args=(11705202, Characters.c2370_0000, Boxes.ChannelerWarpPoint_00_04, 11705202))
    EnableFlag(11705210)
    RunEvent(11705201, slot=10, args=(11705210, Characters.c2370_0001, Boxes.ChannelerWarpPoint_01_00, 11705213))
    RunEvent(11705201, slot=11, args=(11705211, Characters.c2370_0001, Boxes.ChannelerWarpPoint_01_01, 11705213))
    RunEvent(11705201, slot=12, args=(11705212, Characters.c2370_0001, Boxes.ChannelerWarpPoint_01_02, 11705213))
    RunEvent(11705201, slot=13, args=(11705213, Characters.c2370_0001, Boxes.ChannelerWarpPoint_01_03, 11705213))
    EnableFlag(11705220)
    RunEvent(11705201, slot=20, args=(11705220, Characters.c2370_0006, Boxes.ChannelerWarpPoint_02_00, 11705221))
    RunEvent(11705201, slot=21, args=(11705221, Characters.c2370_0006, Boxes.ChannelerWarpPoint_02_01, 11705221))


@RestartOnRest
def Event11705240(_, arg_0_3: int):
    """ 11705240: Event 11705240 """
    DisableNetworkSync()
    IfCharacterBackreadEnabled(0, arg_0_3)
    AICommand(arg_0_3, command_id=1, slot=0)


@UnknownRestart
def Event11705201(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11705201: Event 11705201 """
    EndIfThisEventSlotOn()
    IfFlagOn(1, arg_0_3)
    IfHasTAEEvent(1, arg_4_7, tae_event_id=1000)
    IfConditionTrue(0, input_condition=1)
    Move(arg_4_7, destination=arg_8_11, destination_type=CoordEntityType.Region, short_move=True)
    SetNest(arg_4_7, arg_8_11)
    ForceAnimation(arg_4_7, 7000, wait_for_completion=True)
    SkipLinesIfFlagOff(1, arg_12_15)
    AICommand(arg_4_7, command_id=1, slot=0)
    ReplanAI(arg_4_7)


@RestartOnRest
def Event11700810(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 11700810: Event 11700810 """
    SkipLinesIfThisEventSlotOff(3)
    DisableCharacter(arg_0_3)
    Kill(arg_0_3, award_souls=False)
    End()
    IfCharacterDead(0, arg_0_3)
    SkipLinesIfEqual(4, left=arg_4_7, right=0)
    IfCharacterHuman(-7, PLAYER)
    IfCharacterHollow(-7, PLAYER)
    EndIfConditionFalse(-7)
    AwardItemLot(arg_8_11, host_only=True)
    End()


@RestartOnRest
def Event11705280(_, arg_0_3: int):
    """ 11705280: Event 11705280 """
    IfCharacterAlive(0, arg_0_3)
    IfCharacterDead(0, arg_0_3)
    IfCharacterHuman(-7, PLAYER)
    IfCharacterHollow(-7, PLAYER)
    EndIfConditionFalse(-7)
    AwardItemLot(32300100, host_only=True)


def Event11700600(_, arg_0_3: int, arg_4_7: int):
    """ 11700600: Event 11700600 """
    SkipLinesIfThisEventSlotOff(4)
    EndOfAnimation(arg_0_3, 0)
    DisableObjectActivation(arg_0_3, obj_act_id=-1)
    EnableTreasure(arg_0_3)
    End()
    DisableTreasure(arg_0_3)
    IfObjectActivated(0, obj_act_id=arg_4_7)
    WaitFrames(10)
    EnableTreasure(arg_0_3)


@RestartOnRest
def Event11705010(_, arg_0_3: int):
    """ 11705010: Event 11705010 """
    IfCharacterAlive(1, arg_0_3)
    IfCharacterBackreadEnabled(1, arg_0_3)
    IfCharacterHasSpecialEffect(1, arg_0_3, 5421)
    IfCharacterType(2, PLAYER, CharacterType.BlackPhantom)
    IfConditionFalse(1, input_condition=2)
    IfActionButton(
        1,
        prompt_text=10010400,
        anchor_entity=arg_0_3,
        anchor_type=CoordEntityType.Character,
        facing_angle=45.0,
        max_distance=1.2000000476837158,
        model_point=7,
        trigger_attribute=TriggerAttribute.All,
    )
    IfConditionTrue(0, input_condition=1)
    Move(
        PLAYER,
        destination=arg_0_3,
        destination_type=CoordEntityType.Character,
        model_point=100,
        copy_draw_parent=arg_0_3,
    )
    ForceAnimation(PLAYER, 7521)
    AICommand(arg_0_3, command_id=10, slot=0)
    ReplanAI(arg_0_3)
    Wait(0.10000000149011612)
    AICommand(arg_0_3, command_id=-1, slot=0)
    Restart()


@RestartOnRest
def Event11705020(_, arg_0_3: int):
    """ 11705020: Event 11705020 """
    IfCharacterDoesNotHaveSpecialEffect(1, arg_0_3, 5420)
    IfAttacked(1, arg_0_3, attacker=PLAYER)
    IfConditionTrue(0, input_condition=1)
    CancelSpecialEffect(arg_0_3, 3150)
    CancelSpecialEffect(arg_0_3, 3151)
    IfCharacterBackreadDisabled(7, arg_0_3)
    RestartIfConditionTrue(7)
    IfCharacterHasSpecialEffect(2, arg_0_3, 5421)
    SkipLinesIfConditionFalse(1, 2)
    ForceAnimation(arg_0_3, 3001, wait_for_completion=True)
    IfCharacterHasSpecialEffect(3, arg_0_3, 5422)
    SkipLinesIfConditionFalse(1, 3)
    ForceAnimation(arg_0_3, 3001, wait_for_completion=True)
    IfCharacterHasSpecialEffect(4, arg_0_3, 5423)
    SkipLinesIfConditionFalse(1, 4)
    ForceAnimation(arg_0_3, 3001, wait_for_completion=True)
    IfCharacterHasSpecialEffect(5, arg_0_3, 5424)
    SkipLinesIfConditionFalse(1, 5)
    ForceAnimation(arg_0_3, 3006, wait_for_completion=True)
    ReplanAI(arg_0_3)
    CancelSpecialEffect(arg_0_3, 3150)
    CancelSpecialEffect(arg_0_3, 3151)
    Restart()


@RestartOnRest
def Event11705030(_, arg_0_3: int):
    """ 11705030: Event 11705030 """
    IfCharacterHasSpecialEffect(1, arg_0_3, 5421)
    IfCharacterHasSpecialEffect(1, arg_0_3, 3150)
    IfCharacterHasSpecialEffect(2, arg_0_3, 5420)
    IfCharacterHasSpecialEffect(2, arg_0_3, 3150)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionTrue(5, 2)
    AICommand(arg_0_3, command_id=200, slot=0)
    ReplanAI(arg_0_3)
    Wait(0.10000000149011612)
    AICommand(arg_0_3, command_id=-1, slot=0)
    SkipLines(4)
    AICommand(arg_0_3, command_id=210, slot=0)
    ReplanAI(arg_0_3)
    Wait(0.10000000149011612)
    AICommand(arg_0_3, command_id=-1, slot=0)
    IfCharacterHasSpecialEffect(-2, arg_0_3, 5420)
    IfCharacterHasSpecialEffect(-2, arg_0_3, 5421)
    IfConditionTrue(0, input_condition=-2)
    Restart()


@RestartOnRest
def Event11705040(_, arg_0_3: int):
    """ 11705040: Event 11705040 """
    IfCharacterHasSpecialEffect(1, arg_0_3, 5422)
    IfCharacterDoesNotHaveSpecialEffect(1, arg_0_3, 3150)
    IfCharacterHasSpecialEffect(2, arg_0_3, 5423)
    IfCharacterDoesNotHaveSpecialEffect(2, arg_0_3, 3150)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    CancelSpecialEffect(arg_0_3, 3150)
    CancelSpecialEffect(arg_0_3, 3151)
    SkipLinesIfFinishedConditionTrue(5, 2)
    AICommand(arg_0_3, command_id=201, slot=0)
    ReplanAI(arg_0_3)
    Wait(0.10000000149011612)
    AICommand(arg_0_3, command_id=-1, slot=0)
    SkipLines(4)
    AICommand(arg_0_3, command_id=211, slot=0)
    ReplanAI(arg_0_3)
    Wait(0.10000000149011612)
    AICommand(arg_0_3, command_id=-1, slot=0)
    IfCharacterHasSpecialEffect(-2, arg_0_3, 5420)
    IfCharacterHasSpecialEffect(-2, arg_0_3, 5421)
    IfConditionTrue(0, input_condition=-2)
    Restart()


@RestartOnRest
def Event11705050(_, arg_0_3: int, arg_4_7: int):
    """ 11705050: Event 11705050 """
    IfSingleplayer(1)
    IfCharacterInsideRegion(1, arg_0_3, region=arg_4_7)
    IfCharacterBackreadDisabled(1, arg_0_3)
    IfConditionTrue(0, input_condition=1)
    AddSpecialEffect(arg_0_3, 5421)
    ClearTargetList(arg_0_3)
    ReplanAI(arg_0_3)
    Move(arg_0_3, destination=arg_4_7, destination_type=CoordEntityType.Region, short_move=True)
    IfCharacterBackreadEnabled(0, arg_0_3)
    Restart()


@RestartOnRest
def Event11700900(_, arg_0_3: int):
    """ 11700900: Event 11700900 """
    SkipLinesIfThisEventSlotOff(2)
    DisableCharacter(arg_0_3)
    End()
    IfCharacterDead(0, arg_0_3)
    End()


@RestartOnRest
def Event11705060(_, arg_0_3: int):
    """ 11705060: Event 11705060 """
    EndIfHost()
    IfCharacterBackreadDisabled(1, arg_0_3)
    EndIfConditionTrue(1)
    ResetAnimation(arg_0_3, disable_interpolation=True)
    ForceAnimation(arg_0_3, 0)
    ReplanAI(arg_0_3)


@RestartOnRest
def Event11700700():
    """ 11700700: Event 11700700 """
    IfCharacterAlive(0, Characters.c2710_0010)
    EndIfFlagOn(11700700)
    IfDLCOwned(1)
    IfCharacterDead(1, Characters.c2710_0010)
    IfFlagOn(1, 11200530)
    IfFlagOff(1, 1121)
    IfConditionTrue(0, input_condition=1)
    IfCharacterHuman(-7, PLAYER)
    IfCharacterHollow(-7, PLAYER)
    EndIfConditionFalse(-7)
    AwardItemLot(27100200, host_only=True)


def Event11700510(_, arg_0_3: int, arg_4_7: int):
    """ 11700510: Event 11700510 """
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


def Event11700520(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11700520: Event 11700520 """
    SkipLinesIfThisEventSlotOff(2)
    DropMandatoryTreasure(arg_0_3)
    End()
    IfHealthLessThanOrEqual(0, arg_0_3, 0.0)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)


def Event11700530(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11700530: Event 11700530 """
    IfFlagOff(1, 1096)
    IfFlagOn(1, 1092)
    IfCharacterInsideRegion(1, PLAYER, region=Boxes.PrisonDoorReplaceMediumTrigger)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)
    EnableFlag(11020694)
    EnableCharacter(arg_0_3)
    DisableFlag(61700320)
    EndOfAnimation(Objects.o7401_06, 1)
    EnableObjectActivation(Objects.o7401_06, obj_act_id=27401, relative_index=0)
    EnableObjectActivation(Objects.o7401_06, obj_act_id=27401, relative_index=1)
    DisableObjectActivation(Objects.o7401_06, obj_act_id=27401, relative_index=2)
    DisableObjectActivation(Objects.o7401_06, obj_act_id=27401, relative_index=3)


def Event11700531(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11700531: Event 11700531 """
    IfFlagOff(1, 1096)
    IfFlagOn(1, 1093)
    IfFlagOn(1, 61700320)
    IfCharacterAlive(1, arg_0_3)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)
    EnableFlag(11700594)


def Event11700532(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11700532: Event 11700532 """
    IfFlagOff(1, 1096)
    IfFlagOn(1, 1094)
    IfHost(1)
    IfCharacterOutsideRegion(1, PLAYER, region=Boxes.PrisonDoorReplaceMediumTrigger)
    IfFlagOff(2, 1096)
    IfFlagOn(2, 1093)
    IfFlagOn(2, 14)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)
    EnableFlag(11700594)
    EnableCharacter(arg_0_3)
    Move(
        arg_0_3,
        destination=Boxes.LoganInLibraryPoint,
        destination_type=CoordEntityType.Region,
        set_draw_parent=Collisions.h0041B0,
    )
    IfCharacterBackreadEnabled(0, arg_0_3)
    SetNest(arg_0_3, Boxes.LoganInLibraryPoint)


def Event11700533(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int):
    """ 11700533: Event 11700533 """
    SkipLinesIfFlagOn(2, 11700595)
    DisableObject(Objects.o0110_0014)
    DisableObjectActivation(Objects.o0110_0014, obj_act_id=-1)
    IfFlagOff(1, 1096)
    IfThisEventOff(1)
    IfFlagOn(1, 1095)
    IfFlagOn(1, 14)
    IfFlagOn(1, 728)
    IfFlagOn(1, 11700592)
    IfFlagOff(2, 1096)
    IfFlagOn(2, 1095)
    IfThisEventOn(2)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)
    DisableCharacter(arg_0_3)
    EnableCharacter(arg_16_19)
    EnableFlag(11700595)


def Event11700538(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11700538: Event 11700538 """
    DisableCharacter(Characters.c2711_0000)
    IfFlagOff(1, 1547)
    IfFlagOn(1, 1540)
    IfFlagOff(1, 1512)
    IfFlagOff(1, 1513)
    IfFlagRangeAnyOn(1, (1501, 1511))
    IfCharacterAlive(1, arg_0_3)
    IfFlagOn(2, 1541)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)
    EnableCharacter(Characters.c2711_0000)
    SetDisplayMask(Characters.c2711_0000, bit_index=1, switch_type=OnOffChange.Off)


def Event11700539(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11700539: Event 11700539 """
    IfFlagOff(1, 1547)
    IfFlagOn(1, 1541)
    IfCharacterDead(1, Characters.c2711_0000)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)
    Move(
        arg_0_3,
        destination=Characters.c2711_0000,
        destination_type=CoordEntityType.Character,
        model_point=101,
        copy_draw_parent=Characters.c2711_0000,
    )
    EnableCharacter(arg_0_3)


def Event11700540(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11700540: Event 11700540 """
    IfFlagOff(1, 1547)
    IfFlagOn(1, 1542)
    IfFlagOn(1, 11700593)
    IfThisEventOff(1)
    IfHost(2)
    IfFlagOff(2, 1547)
    IfFlagOn(2, 1542)
    IfThisEventOn(2)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(1)
    SkipLinesIfFinishedConditionTrue(2, 2)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)
    DisableCharacter(arg_0_3)


def Event11700545(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11700545: Event 11700545 """
    IfFlagOff(1, 1176)
    IfFlagOff(1, 1179)
    IfFlagOn(1, 1175)
    IfFlagOn(1, 724)
    IfFlagOn(2, 1181)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)
    EnableCharacter(arg_0_3)


def Event11705843(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11705843: Event 11705843 """
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


def Event11705846(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 11705846: Event 11705846 """
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
    """ 11702000: Patches teleports behind the player and attacks. """
    DisableCharacter(Characters.c0000_PatchesAmbush)

    Await(InsideMap(DUKES_ARCHIVES) and TriggerFlags.PatchesAmbush and IsAlive(Characters.c0000_PatchesAmbush))
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
    """ 11702001: Channeler teleports above the player (no gravity) and uses its buff dance. """
    DisableCharacter(Characters.c2370_TrollChanneler)

    Await(InsideMap(DUKES_ARCHIVES) and TriggerFlags.ChannelerAmbush and IsAlive(Characters.c2370_TrollChanneler))
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

    AddSpecialEffect(6032, 5470)
    AddSpecialEffect(6073, 5470)
    AddSpecialEffect(6291, 5470)
    AddSpecialEffect(6610, 5470)
    AddSpecialEffect(6033, 5470)
    AddSpecialEffect(1700960, 5470)
    AddSpecialEffect(1700961, 5470)
    AddSpecialEffect(1700950, 5470)
    AddSpecialEffect(1700962, 5470)
    AddSpecialEffect(1700300, 5470)
    AddSpecialEffect(1700301, 5470)
    AddSpecialEffect(1700900, 5470)
    AddSpecialEffect(1700901, 5470)
    AddSpecialEffect(1700902, 5470)
    AddSpecialEffect(1700903, 5470)
    AddSpecialEffect(1700302, 5470)
    AddSpecialEffect(1700100, 5470)
    AddSpecialEffect(1700202, 5470)
    AddSpecialEffect(1700203, 5470)
    AddSpecialEffect(1700103, 5470)
    AddSpecialEffect(1700102, 5470)
    AddSpecialEffect(1700101, 5470)
    AddSpecialEffect(1700204, 5470)
    AddSpecialEffect(1700205, 5470)
    AddSpecialEffect(1700206, 5470)
    AddSpecialEffect(1700207, 5470)
    AddSpecialEffect(1700208, 5470)
    AddSpecialEffect(1700209, 5470)
    AddSpecialEffect(1700210, 5470)
    AddSpecialEffect(1700211, 5470)
    AddSpecialEffect(1700510, 5470)
    AddSpecialEffect(1700212, 5470)
    AddSpecialEffect(1700213, 5470)
    AddSpecialEffect(1700214, 5470)
    AddSpecialEffect(1700215, 5470)
    AddSpecialEffect(1700904, 5470)
    AddSpecialEffect(1700905, 5470)
    AddSpecialEffect(1700906, 5470)
    AddSpecialEffect(1700907, 5470)
    AddSpecialEffect(1700500, 5470)
    AddSpecialEffect(1700501, 5470)
    AddSpecialEffect(1700502, 5470)
    AddSpecialEffect(1700400, 5470)
    AddSpecialEffect(1700401, 5470)
    AddSpecialEffect(1700200, 5470)
    AddSpecialEffect(1700216, 5470)
    AddSpecialEffect(1700217, 5470)
    AddSpecialEffect(1700218, 5470)
    AddSpecialEffect(1700219, 5470)
    AddSpecialEffect(1700220, 5470)
    AddSpecialEffect(1700221, 5470)
    AddSpecialEffect(1700222, 5470)
    AddSpecialEffect(1700223, 5470)
    AddSpecialEffect(1700224, 5470)
    AddSpecialEffect(1700225, 5470)
    AddSpecialEffect(1700226, 5470)
    AddSpecialEffect(1700227, 5470)
    AddSpecialEffect(1700228, 5470)
    AddSpecialEffect(1700229, 5470)
    AddSpecialEffect(1700230, 5470)
    AddSpecialEffect(1700231, 5470)
    AddSpecialEffect(1700232, 5470)
    AddSpecialEffect(1700233, 5470)
    AddSpecialEffect(1700234, 5470)
    AddSpecialEffect(1700235, 5470)
    AddSpecialEffect(1700236, 5470)
    AddSpecialEffect(1700237, 5470)
    AddSpecialEffect(1700238, 5470)
    AddSpecialEffect(1700239, 5470)
    AddSpecialEffect(1700240, 5470)
    AddSpecialEffect(1700241, 5470)
    AddSpecialEffect(1700242, 5470)
    AddSpecialEffect(1700243, 5470)
    AddSpecialEffect(1700244, 5470)
    AddSpecialEffect(1700245, 5470)
    AddSpecialEffect(1700246, 5470)
    AddSpecialEffect(1700247, 5470)
    AddSpecialEffect(1700248, 5470)
    AddSpecialEffect(1700249, 5470)
    AddSpecialEffect(1700256, 5470)
    AddSpecialEffect(1700257, 5470)
    AddSpecialEffect(1700258, 5470)
    AddSpecialEffect(1700259, 5470)
    AddSpecialEffect(1700260, 5470)
    AddSpecialEffect(1700261, 5470)
    AddSpecialEffect(1700262, 5470)
    AddSpecialEffect(1700263, 5470)
    AddSpecialEffect(1700350, 5470)
    AddSpecialEffect(1700351, 5470)
    AddSpecialEffect(1700352, 5470)
    AddSpecialEffect(1700250, 5470)
    AddSpecialEffect(1700251, 5470)
    AddSpecialEffect(1700252, 5470)
    AddSpecialEffect(1700253, 5470)
    AddSpecialEffect(1700254, 5470)
    AddSpecialEffect(1700255, 5470)
    AddSpecialEffect(1700450, 5470)
    AddSpecialEffect(1700451, 5470)
    AddSpecialEffect(1700452, 5470)
    AddSpecialEffect(1700453, 5470)
    AddSpecialEffect(1700110, 5470)
    AddSpecialEffect(1700111, 5470)
    AddSpecialEffect(1700112, 5470)
    AddSpecialEffect(1700150, 5470)
    AddSpecialEffect(1700151, 5470)
    AddSpecialEffect(1700120, 5470)
    AddSpecialEffect(1700116, 5470)
    AddSpecialEffect(1700117, 5470)
    AddSpecialEffect(1700118, 5470)
    AddSpecialEffect(1700113, 5470)
    AddSpecialEffect(1700114, 5470)
    AddSpecialEffect(1700115, 5470)
    AddSpecialEffect(1700908, 5470)
    AddSpecialEffect(1700909, 5470)
    AddSpecialEffect(1700190, 5470)
    AddSpecialEffect(1700191, 5470)
    AddSpecialEffect(1703900, 5470)
    AddSpecialEffect(1703910, 5470)
    AddSpecialEffect(1703902, 5470)
    AddSpecialEffect(1703901, 5470)
    AddSpecialEffect(1703911, 5470)
    AddSpecialEffect(1703912, 5470)
    AddSpecialEffect(1700700, 5470)
    AddSpecialEffect(1700800, 5470)
    AddSpecialEffect(1700801, 5470)

    return RESTART


@RestartOnRest
def RedPhantomAmbush():
    """ 11702002: Random red phantom ambushes the player. """
    DisableCharacter(Characters.c2370_0002)
    DisableCharacter(Characters.c2370_0003)
    DisableCharacter(Characters.c2370_0004)
    DisableCharacter(Characters.c2370_0005)
    DisableCharacter(Characters.c2710_0015)
    DisableCharacter(Characters.c2710_0016)
    DisableCharacter(Characters.c2710_0017)
    DisableCharacter(Characters.c2710_0018)
    DisableCharacter(Characters.c3330_0020)
    DisableCharacter(Characters.c3330_0021)

    Await(InsideMap(DUKES_ARCHIVES) and TriggerFlags.EnemyAmbush)
    DisableFlag(TriggerFlags.EnemyAmbush)

    DisableFlagRange((11812900, 11812999))
    EnableRandomFlagInRange((11812900, 11812909))

    if FlagEnabled(11812900):
        ControlRedPhantom(0, Characters.c2370_0002)
    elif FlagEnabled(11812901):
        ControlRedPhantom(0, Characters.c2370_0003)
    elif FlagEnabled(11812902):
        ControlRedPhantom(0, Characters.c2370_0004)
    elif FlagEnabled(11812903):
        ControlRedPhantom(0, Characters.c2370_0005)
    elif FlagEnabled(11812904):
        ControlRedPhantom(0, Characters.c2710_0015)
    elif FlagEnabled(11812905):
        ControlRedPhantom(0, Characters.c2710_0016)
    elif FlagEnabled(11812906):
        ControlRedPhantom(0, Characters.c2710_0017)
    elif FlagEnabled(11812907):
        ControlRedPhantom(0, Characters.c2710_0018)
    elif FlagEnabled(11812908):
        ControlRedPhantom(0, Characters.c3330_0020)
    elif FlagEnabled(11812909):
        ControlRedPhantom(0, Characters.c3330_0021)
    
    Await(FlagEnabled(11705082))

    return RESTART


@RestartOnRest
def ControlRedPhantom(_, enemy: int):
    """ 11705081: `enemy` moves to player and appears. """
    DisableFlag(11705082)
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
    EnableFlag(11705082)


def MakeWorldInvisible():
    """ 11702003: Disable all map pieces. Undone only by reload. """
    Await(TriggerFlags.InvisibleWorld)   # note you don't need to be standing in the map
    DisableFlag(TriggerFlags.InvisibleWorld)
    for map_piece in range(1708500, 1708590):
        DisableMapPiece(map_piece)
    # No need to restart.


@RestartOnRest
def OopsAllGwyns():
    """ 11702004: Enable Gwyns and warp them to their paired normal characters. """
    DisableCharacter(1700600)
    DisableCharacter(1700601)
    DisableCharacter(1700602)
    DisableCharacter(1700603)
    DisableCharacter(1700604)
    DisableCharacter(1700605)
    DisableCharacter(1700606)
    DisableCharacter(1700607)
    DisableCharacter(1700608)
    DisableCharacter(1700609)
    DisableCharacter(1700610)
    DisableCharacter(1700611)
    DisableCharacter(1700612)
    DisableCharacter(1700613)
    DisableCharacter(1700614)
    DisableCharacter(1700615)
    DisableCharacter(1700616)
    DisableCharacter(1700617)
    DisableCharacter(1700618)
    DisableCharacter(1700619)
    DisableCharacter(1700620)
    DisableCharacter(1700621)
    Await(TriggerFlags.OopsAllGwyns)  # note you don't need to be standing in the map
    DisableCharacter(6032)
    EnableCharacter(1700600)
    DisableCharacter(1700301)
    EnableCharacter(1700601)
    DisableCharacter(1700302)
    EnableCharacter(1700602)
    DisableCharacter(1700102)
    EnableCharacter(1700603)
    DisableCharacter(1700207)
    EnableCharacter(1700604)
    DisableCharacter(1700510)
    EnableCharacter(1700605)
    DisableCharacter(1700501)
    EnableCharacter(1700606)
    DisableCharacter(1700216)
    EnableCharacter(1700607)
    DisableCharacter(1700221)
    EnableCharacter(1700608)
    DisableCharacter(1700226)
    EnableCharacter(1700609)
    DisableCharacter(1700231)
    EnableCharacter(1700610)
    DisableCharacter(1700236)
    EnableCharacter(1700611)
    DisableCharacter(1700241)
    EnableCharacter(1700612)
    DisableCharacter(1700246)
    EnableCharacter(1700613)
    DisableCharacter(1700257)
    EnableCharacter(1700614)
    DisableCharacter(1700262)
    EnableCharacter(1700615)
    DisableCharacter(1700250)
    EnableCharacter(1700616)
    DisableCharacter(1700255)
    EnableCharacter(1700617)
    DisableCharacter(1700110)
    EnableCharacter(1700618)
    DisableCharacter(1700120)
    EnableCharacter(1700619)
    DisableCharacter(1700114)
    EnableCharacter(1700620)
    DisableCharacter(1700191)
    EnableCharacter(1700621)
    WaitFrames(30)  # enough time for other maps to trigger too
    DisableFlag(TriggerFlags.OopsAllGwyns)
    # No need to restart.


@RestartOnRest
def OopsAllBonewheels():
    """ 11702005: Enable Bonewheels and warp them to their paired normal characters. """
    DisableCharacter(1700402)
    DisableCharacter(1700403)
    DisableCharacter(1700404)
    DisableCharacter(1700405)
    DisableCharacter(1700406)
    DisableCharacter(1700407)
    DisableCharacter(1700408)
    DisableCharacter(1700409)
    DisableCharacter(1700410)
    DisableCharacter(1700411)
    DisableCharacter(1700412)
    DisableCharacter(1700413)
    DisableCharacter(1700414)
    DisableCharacter(1700415)
    DisableCharacter(1700416)
    DisableCharacter(1700417)
    DisableCharacter(1700418)
    DisableCharacter(1700419)
    DisableCharacter(1700420)
    DisableCharacter(1700421)
    DisableCharacter(1700422)
    DisableCharacter(1700423)
    DisableCharacter(1700424)
    DisableCharacter(1700425)
    DisableCharacter(1700426)
    DisableCharacter(1700427)
    DisableCharacter(1700428)
    DisableCharacter(1700429)
    DisableCharacter(1700430)
    DisableCharacter(1700431)
    DisableCharacter(1700432)
    DisableCharacter(1700433)
    DisableCharacter(1700434)
    DisableCharacter(1700435)
    DisableCharacter(1700436)
    DisableCharacter(1700437)
    DisableCharacter(1700438)
    DisableCharacter(1700439)
    DisableCharacter(1700440)
    DisableCharacter(1700441)
    DisableCharacter(1700442)
    DisableCharacter(1700443)
    DisableCharacter(1700444)
    DisableCharacter(1700445)
    DisableCharacter(1700446)
    DisableCharacter(1700447)
    DisableCharacter(1700448)
    DisableCharacter(1700449)
    DisableCharacter(1700454)
    DisableCharacter(1700455)
    DisableCharacter(1700456)
    DisableCharacter(1700457)
    DisableCharacter(1700458)
    DisableCharacter(1700459)
    DisableCharacter(1700460)
    DisableCharacter(1700461)
    DisableCharacter(1700462)
    DisableCharacter(1700463)
    DisableCharacter(1700464)
    DisableCharacter(1700465)
    DisableCharacter(1700466)
    DisableCharacter(1700467)
    DisableCharacter(1700468)
    DisableCharacter(1700469)
    DisableCharacter(1700470)
    DisableCharacter(1700471)
    DisableCharacter(1700472)
    DisableCharacter(1700473)
    DisableCharacter(1700474)
    DisableCharacter(1700475)
    DisableCharacter(1700476)
    DisableCharacter(1700477)
    DisableCharacter(1700478)
    DisableCharacter(1700479)
    DisableCharacter(1700480)
    DisableCharacter(1700481)
    DisableCharacter(1700482)
    DisableCharacter(1700483)
    DisableCharacter(1700484)
    DisableCharacter(1700485)
    DisableCharacter(1700486)
    DisableCharacter(1700487)
    DisableCharacter(1700488)
    DisableCharacter(1700489)
    DisableCharacter(1700490)
    DisableCharacter(1700491)
    DisableCharacter(1700492)
    DisableCharacter(1700493)
    DisableCharacter(1700494)
    DisableCharacter(1700495)
    DisableCharacter(1700496)
    DisableCharacter(1700497)
    DisableCharacter(1700498)
    DisableCharacter(1700499)
    DisableCharacter(1700503)
    DisableCharacter(1700504)
    DisableCharacter(1700505)
    DisableCharacter(1700506)
    DisableCharacter(1700507)
    Await(TriggerFlags.OopsAllBonewheels)  # note you don't need to be standing in the map
    DisableCharacter(6032)
    EnableCharacter(1700402)
    DisableCharacter(6073)
    EnableCharacter(1700403)
    DisableCharacter(6291)
    EnableCharacter(1700404)
    DisableCharacter(6610)
    EnableCharacter(1700405)
    DisableCharacter(6033)
    EnableCharacter(1700406)
    DisableCharacter(1700300)
    EnableCharacter(1700407)
    DisableCharacter(1700301)
    EnableCharacter(1700408)
    DisableCharacter(1700302)
    EnableCharacter(1700409)
    DisableCharacter(1700202)
    EnableCharacter(1700410)
    DisableCharacter(1700203)
    EnableCharacter(1700411)
    DisableCharacter(1700103)
    EnableCharacter(1700412)
    DisableCharacter(1700102)
    EnableCharacter(1700413)
    DisableCharacter(1700101)
    EnableCharacter(1700414)
    DisableCharacter(1700204)
    EnableCharacter(1700415)
    DisableCharacter(1700205)
    EnableCharacter(1700416)
    DisableCharacter(1700206)
    EnableCharacter(1700417)
    DisableCharacter(1700207)
    EnableCharacter(1700418)
    DisableCharacter(1700208)
    EnableCharacter(1700419)
    DisableCharacter(1700209)
    EnableCharacter(1700420)
    DisableCharacter(1700210)
    EnableCharacter(1700421)
    DisableCharacter(1700211)
    EnableCharacter(1700422)
    DisableCharacter(1700510)
    EnableCharacter(1700423)
    DisableCharacter(1700212)
    EnableCharacter(1700424)
    DisableCharacter(1700213)
    EnableCharacter(1700425)
    DisableCharacter(1700214)
    EnableCharacter(1700426)
    DisableCharacter(1700215)
    EnableCharacter(1700427)
    DisableCharacter(1700500)
    EnableCharacter(1700428)
    DisableCharacter(1700501)
    EnableCharacter(1700429)
    DisableCharacter(1700502)
    EnableCharacter(1700430)
    DisableCharacter(1700400)
    EnableCharacter(1700431)
    DisableCharacter(1700401)
    EnableCharacter(1700432)
    DisableCharacter(1700200)
    EnableCharacter(1700433)
    DisableCharacter(1700216)
    EnableCharacter(1700434)
    DisableCharacter(1700217)
    EnableCharacter(1700435)
    DisableCharacter(1700218)
    EnableCharacter(1700436)
    DisableCharacter(1700219)
    EnableCharacter(1700437)
    DisableCharacter(1700220)
    EnableCharacter(1700438)
    DisableCharacter(1700221)
    EnableCharacter(1700439)
    DisableCharacter(1700222)
    EnableCharacter(1700440)
    DisableCharacter(1700223)
    EnableCharacter(1700441)
    DisableCharacter(1700224)
    EnableCharacter(1700442)
    DisableCharacter(1700225)
    EnableCharacter(1700443)
    DisableCharacter(1700226)
    EnableCharacter(1700444)
    DisableCharacter(1700227)
    EnableCharacter(1700445)
    DisableCharacter(1700228)
    EnableCharacter(1700446)
    DisableCharacter(1700229)
    EnableCharacter(1700447)
    DisableCharacter(1700230)
    EnableCharacter(1700448)
    DisableCharacter(1700231)
    EnableCharacter(1700449)
    DisableCharacter(1700232)
    EnableCharacter(1700454)
    DisableCharacter(1700233)
    EnableCharacter(1700455)
    DisableCharacter(1700234)
    EnableCharacter(1700456)
    DisableCharacter(1700235)
    EnableCharacter(1700457)
    DisableCharacter(1700236)
    EnableCharacter(1700458)
    DisableCharacter(1700237)
    EnableCharacter(1700459)
    DisableCharacter(1700238)
    EnableCharacter(1700460)
    DisableCharacter(1700239)
    EnableCharacter(1700461)
    DisableCharacter(1700240)
    EnableCharacter(1700462)
    DisableCharacter(1700241)
    EnableCharacter(1700463)
    DisableCharacter(1700242)
    EnableCharacter(1700464)
    DisableCharacter(1700243)
    EnableCharacter(1700465)
    DisableCharacter(1700244)
    EnableCharacter(1700466)
    DisableCharacter(1700245)
    EnableCharacter(1700467)
    DisableCharacter(1700246)
    EnableCharacter(1700468)
    DisableCharacter(1700247)
    EnableCharacter(1700469)
    DisableCharacter(1700248)
    EnableCharacter(1700470)
    DisableCharacter(1700249)
    EnableCharacter(1700471)
    DisableCharacter(1700256)
    EnableCharacter(1700472)
    DisableCharacter(1700257)
    EnableCharacter(1700473)
    DisableCharacter(1700258)
    EnableCharacter(1700474)
    DisableCharacter(1700259)
    EnableCharacter(1700475)
    DisableCharacter(1700260)
    EnableCharacter(1700476)
    DisableCharacter(1700261)
    EnableCharacter(1700477)
    DisableCharacter(1700262)
    EnableCharacter(1700478)
    DisableCharacter(1700263)
    EnableCharacter(1700479)
    DisableCharacter(1700250)
    EnableCharacter(1700480)
    DisableCharacter(1700251)
    EnableCharacter(1700481)
    DisableCharacter(1700252)
    EnableCharacter(1700482)
    DisableCharacter(1700253)
    EnableCharacter(1700483)
    DisableCharacter(1700254)
    EnableCharacter(1700484)
    DisableCharacter(1700255)
    EnableCharacter(1700485)
    DisableCharacter(1700450)
    EnableCharacter(1700486)
    DisableCharacter(1700451)
    EnableCharacter(1700487)
    DisableCharacter(1700452)
    EnableCharacter(1700488)
    DisableCharacter(1700453)
    EnableCharacter(1700489)
    DisableCharacter(1700110)
    EnableCharacter(1700490)
    DisableCharacter(1700111)
    EnableCharacter(1700491)
    DisableCharacter(1700112)
    EnableCharacter(1700492)
    DisableCharacter(1700150)
    EnableCharacter(1700493)
    DisableCharacter(1700151)
    EnableCharacter(1700494)
    DisableCharacter(1700120)
    EnableCharacter(1700495)
    DisableCharacter(1700116)
    EnableCharacter(1700496)
    DisableCharacter(1700117)
    EnableCharacter(1700497)
    DisableCharacter(1700118)
    EnableCharacter(1700498)
    DisableCharacter(1700113)
    EnableCharacter(1700499)
    DisableCharacter(1700114)
    EnableCharacter(1700503)
    DisableCharacter(1700115)
    EnableCharacter(1700504)
    DisableCharacter(1700190)
    EnableCharacter(1700505)
    DisableCharacter(1700191)
    EnableCharacter(1700506)
    DisableCharacter(1700801)
    EnableCharacter(1700507)
    WaitFrames(30)  # enough time for other maps to trigger too
    DisableFlag(TriggerFlags.OopsAllBonewheels)
    # No need to restart.


@RestartOnRest
def HyperAggression():
    """ 11702006: Switch AI param of every enemy to its aggressive version. """
    Await(TriggerFlags.HyperAggression or TriggerFlags.HyperAggressionReTrigger)
    
    SetAIParamID(1700300, 237051)
    SetAIParamID(1700301, 237051)
    SetAIParamID(1700900, 237051)
    SetAIParamID(1700901, 237051)
    SetAIParamID(1700902, 237051)
    SetAIParamID(1700903, 237051)
    SetAIParamID(1700302, 237051)
    SetAIParamID(1700100, 269050)
    SetAIParamID(1700202, 269050)
    SetAIParamID(1700203, 269050)
    SetAIParamID(1700103, 269060)
    SetAIParamID(1700102, 269060)
    SetAIParamID(1700101, 270050)
    SetAIParamID(1700204, 271050)
    SetAIParamID(1700205, 271051)
    SetAIParamID(1700206, 271050)
    SetAIParamID(1700207, 271051)
    SetAIParamID(1700208, 271051)
    SetAIParamID(1700209, 271050)
    SetAIParamID(1700210, 271050)
    SetAIParamID(1700211, 271051)
    SetAIParamID(1700510, 271052)
    SetAIParamID(1700212, 271050)
    SetAIParamID(1700213, 271051)
    SetAIParamID(1700214, 271051)
    SetAIParamID(1700215, 271051)
    SetAIParamID(1700904, 271050)
    SetAIParamID(1700905, 271050)
    SetAIParamID(1700906, 271050)
    SetAIParamID(1700907, 271050)
    SetAIParamID(1700500, 271150)
    SetAIParamID(1700501, 271151)
    SetAIParamID(1700502, 271150)
    SetAIParamID(1700400, 278050)
    SetAIParamID(1700401, 278050)
    SetAIParamID(1700200, 280050)
    SetAIParamID(1700216, 280050)
    SetAIParamID(1700217, 280050)
    SetAIParamID(1700218, 280050)
    SetAIParamID(1700219, 280050)
    SetAIParamID(1700220, 280050)
    SetAIParamID(1700221, 280051)
    SetAIParamID(1700222, 280050)
    SetAIParamID(1700223, 280050)
    SetAIParamID(1700224, 280050)
    SetAIParamID(1700225, 280050)
    SetAIParamID(1700226, 280051)
    SetAIParamID(1700227, 280051)
    SetAIParamID(1700228, 280050)
    SetAIParamID(1700229, 280052)
    SetAIParamID(1700230, 280052)
    SetAIParamID(1700231, 280052)
    SetAIParamID(1700232, 280052)
    SetAIParamID(1700233, 280052)
    SetAIParamID(1700234, 280052)
    SetAIParamID(1700235, 280052)
    SetAIParamID(1700236, 280052)
    SetAIParamID(1700237, 280051)
    SetAIParamID(1700238, 280050)
    SetAIParamID(1700239, 280051)
    SetAIParamID(1700240, 280052)
    SetAIParamID(1700241, 280052)
    SetAIParamID(1700242, 280051)
    SetAIParamID(1700243, 280050)
    SetAIParamID(1700244, 280050)
    SetAIParamID(1700245, 280050)
    SetAIParamID(1700246, 280051)
    SetAIParamID(1700247, 280052)
    SetAIParamID(1700248, 280051)
    SetAIParamID(1700249, 280051)
    SetAIParamID(1700256, 280051)
    SetAIParamID(1700257, 280052)
    SetAIParamID(1700258, 280051)
    SetAIParamID(1700259, 280051)
    SetAIParamID(1700260, 280052)
    SetAIParamID(1700261, 280052)
    SetAIParamID(1700262, 280051)
    SetAIParamID(1700263, 280052)
    SetAIParamID(1700350, 323051)
    SetAIParamID(1700351, 323051)
    SetAIParamID(1700352, 323051)
    SetAIParamID(1700250, 325050)
    SetAIParamID(1700251, 325050)
    SetAIParamID(1700252, 325050)
    SetAIParamID(1700253, 325050)
    SetAIParamID(1700254, 325050)
    SetAIParamID(1700255, 325050)
    SetAIParamID(1700450, 330050)
    SetAIParamID(1700451, 330050)
    SetAIParamID(1700452, 330050)
    SetAIParamID(1700453, 330050)
    SetAIParamID(1700110, 333050)
    SetAIParamID(1700111, 333050)
    SetAIParamID(1700112, 333053)
    SetAIParamID(1700150, 333055)
    SetAIParamID(1700151, 333055)
    SetAIParamID(1700120, 333053)
    SetAIParamID(1700116, 333052)
    SetAIParamID(1700117, 333052)
    SetAIParamID(1700118, 333053)
    SetAIParamID(1700113, 333051)
    SetAIParamID(1700114, 333051)
    SetAIParamID(1700115, 333053)
    SetAIParamID(1700908, 333050)
    SetAIParamID(1700909, 333050)
    SetAIParamID(1700190, 346150)
    SetAIParamID(1700191, 346150)
    SetAIParamID(1703900, 349050)
    SetAIParamID(1703910, 349050)
    SetAIParamID(1703902, 349150)
    SetAIParamID(1703901, 349150)
    SetAIParamID(1703911, 349150)
    SetAIParamID(1703912, 349150)
    SetAIParamID(1700700, 529051)
    SetAIParamID(1700800, 529050)
    SetAIParamID(1700600, 537050)
    SetAIParamID(1700601, 537050)
    SetAIParamID(1700602, 537050)
    SetAIParamID(1700603, 537050)
    SetAIParamID(1700604, 537050)
    SetAIParamID(1700605, 537050)
    SetAIParamID(1700606, 537050)
    SetAIParamID(1700607, 537050)
    SetAIParamID(1700608, 537050)
    SetAIParamID(1700609, 537050)
    SetAIParamID(1700610, 537050)
    SetAIParamID(1700611, 537050)
    SetAIParamID(1700612, 537050)
    SetAIParamID(1700613, 537050)
    SetAIParamID(1700614, 537050)
    SetAIParamID(1700615, 537050)
    SetAIParamID(1700616, 537050)
    SetAIParamID(1700617, 537050)
    SetAIParamID(1700618, 537050)
    SetAIParamID(1700619, 537050)
    SetAIParamID(1700620, 537050)
    SetAIParamID(1700621, 537050)
    SetAIParamID(1700402, 293050)
    SetAIParamID(1700403, 293050)
    SetAIParamID(1700404, 293050)
    SetAIParamID(1700405, 293050)
    SetAIParamID(1700406, 293050)
    SetAIParamID(1700407, 293050)
    SetAIParamID(1700408, 293050)
    SetAIParamID(1700409, 293050)
    SetAIParamID(1700410, 293050)
    SetAIParamID(1700411, 293050)
    SetAIParamID(1700412, 293050)
    SetAIParamID(1700413, 293050)
    SetAIParamID(1700414, 293050)
    SetAIParamID(1700415, 293050)
    SetAIParamID(1700416, 293050)
    SetAIParamID(1700417, 293050)
    SetAIParamID(1700418, 293050)
    SetAIParamID(1700419, 293050)
    SetAIParamID(1700420, 293050)
    SetAIParamID(1700421, 293050)
    SetAIParamID(1700422, 293050)
    SetAIParamID(1700423, 293050)
    SetAIParamID(1700424, 293050)
    SetAIParamID(1700425, 293050)
    SetAIParamID(1700426, 293050)
    SetAIParamID(1700427, 293050)
    SetAIParamID(1700428, 293050)
    SetAIParamID(1700429, 293050)
    SetAIParamID(1700430, 293050)
    SetAIParamID(1700431, 293050)
    SetAIParamID(1700432, 293050)
    SetAIParamID(1700433, 293050)
    SetAIParamID(1700434, 293050)
    SetAIParamID(1700435, 293050)
    SetAIParamID(1700436, 293050)
    SetAIParamID(1700437, 293050)
    SetAIParamID(1700438, 293050)
    SetAIParamID(1700439, 293050)
    SetAIParamID(1700440, 293050)
    SetAIParamID(1700441, 293050)
    SetAIParamID(1700442, 293050)
    SetAIParamID(1700443, 293050)
    SetAIParamID(1700444, 293050)
    SetAIParamID(1700445, 293050)
    SetAIParamID(1700446, 293050)
    SetAIParamID(1700447, 293050)
    SetAIParamID(1700448, 293050)
    SetAIParamID(1700449, 293050)
    SetAIParamID(1700454, 293050)
    SetAIParamID(1700455, 293050)
    SetAIParamID(1700456, 293050)
    SetAIParamID(1700457, 293050)
    SetAIParamID(1700458, 293050)
    SetAIParamID(1700459, 293050)
    SetAIParamID(1700460, 293050)
    SetAIParamID(1700461, 293050)
    SetAIParamID(1700462, 293050)
    SetAIParamID(1700463, 293050)
    SetAIParamID(1700464, 293050)
    SetAIParamID(1700465, 293050)
    SetAIParamID(1700466, 293050)
    SetAIParamID(1700467, 293050)
    SetAIParamID(1700468, 293050)
    SetAIParamID(1700469, 293050)
    SetAIParamID(1700470, 293050)
    SetAIParamID(1700471, 293050)
    SetAIParamID(1700472, 293050)
    SetAIParamID(1700473, 293050)
    SetAIParamID(1700474, 293050)
    SetAIParamID(1700475, 293050)
    SetAIParamID(1700476, 293050)
    SetAIParamID(1700477, 293050)
    SetAIParamID(1700478, 293050)
    SetAIParamID(1700479, 293050)
    SetAIParamID(1700480, 293050)
    SetAIParamID(1700481, 293050)
    SetAIParamID(1700482, 293050)
    SetAIParamID(1700483, 293050)
    SetAIParamID(1700484, 293050)
    SetAIParamID(1700485, 293050)
    SetAIParamID(1700486, 293050)
    SetAIParamID(1700487, 293050)
    SetAIParamID(1700488, 293050)
    SetAIParamID(1700489, 293050)
    SetAIParamID(1700490, 293050)
    SetAIParamID(1700491, 293050)
    SetAIParamID(1700492, 293050)
    SetAIParamID(1700493, 293050)
    SetAIParamID(1700494, 293050)
    SetAIParamID(1700495, 293050)
    SetAIParamID(1700496, 293050)
    SetAIParamID(1700497, 293050)
    SetAIParamID(1700498, 293050)
    SetAIParamID(1700499, 293050)
    SetAIParamID(1700503, 293050)
    SetAIParamID(1700504, 293050)
    SetAIParamID(1700505, 293050)
    SetAIParamID(1700506, 293050)
    SetAIParamID(1700507, 293050)
        
    # Common EMEVD manages the flags that control this event.
    Await(not TriggerFlags.HyperAggressionReTrigger)
    
    SetAIParamID(1700300, 237001)
    SetAIParamID(1700301, 237001)
    SetAIParamID(1700900, 237001)
    SetAIParamID(1700901, 237001)
    SetAIParamID(1700902, 237001)
    SetAIParamID(1700903, 237001)
    SetAIParamID(1700302, 237001)
    SetAIParamID(1700100, 269000)
    SetAIParamID(1700202, 269000)
    SetAIParamID(1700203, 269000)
    SetAIParamID(1700103, 269010)
    SetAIParamID(1700102, 269010)
    SetAIParamID(1700101, 270000)
    SetAIParamID(1700204, 271000)
    SetAIParamID(1700205, 271001)
    SetAIParamID(1700206, 271000)
    SetAIParamID(1700207, 271001)
    SetAIParamID(1700208, 271001)
    SetAIParamID(1700209, 271000)
    SetAIParamID(1700210, 271000)
    SetAIParamID(1700211, 271001)
    SetAIParamID(1700510, 271002)
    SetAIParamID(1700212, 271000)
    SetAIParamID(1700213, 271001)
    SetAIParamID(1700214, 271001)
    SetAIParamID(1700215, 271001)
    SetAIParamID(1700904, 271000)
    SetAIParamID(1700905, 271000)
    SetAIParamID(1700906, 271000)
    SetAIParamID(1700907, 271000)
    SetAIParamID(1700500, 271100)
    SetAIParamID(1700501, 271101)
    SetAIParamID(1700502, 271100)
    SetAIParamID(1700400, 278000)
    SetAIParamID(1700401, 278000)
    SetAIParamID(1700200, 280000)
    SetAIParamID(1700216, 280000)
    SetAIParamID(1700217, 280000)
    SetAIParamID(1700218, 280000)
    SetAIParamID(1700219, 280000)
    SetAIParamID(1700220, 280000)
    SetAIParamID(1700221, 280001)
    SetAIParamID(1700222, 280000)
    SetAIParamID(1700223, 280000)
    SetAIParamID(1700224, 280000)
    SetAIParamID(1700225, 280000)
    SetAIParamID(1700226, 280001)
    SetAIParamID(1700227, 280001)
    SetAIParamID(1700228, 280000)
    SetAIParamID(1700229, 280002)
    SetAIParamID(1700230, 280002)
    SetAIParamID(1700231, 280002)
    SetAIParamID(1700232, 280002)
    SetAIParamID(1700233, 280002)
    SetAIParamID(1700234, 280002)
    SetAIParamID(1700235, 280002)
    SetAIParamID(1700236, 280002)
    SetAIParamID(1700237, 280001)
    SetAIParamID(1700238, 280000)
    SetAIParamID(1700239, 280001)
    SetAIParamID(1700240, 280002)
    SetAIParamID(1700241, 280002)
    SetAIParamID(1700242, 280001)
    SetAIParamID(1700243, 280000)
    SetAIParamID(1700244, 280000)
    SetAIParamID(1700245, 280000)
    SetAIParamID(1700246, 280001)
    SetAIParamID(1700247, 280002)
    SetAIParamID(1700248, 280001)
    SetAIParamID(1700249, 280001)
    SetAIParamID(1700256, 280001)
    SetAIParamID(1700257, 280002)
    SetAIParamID(1700258, 280001)
    SetAIParamID(1700259, 280001)
    SetAIParamID(1700260, 280002)
    SetAIParamID(1700261, 280002)
    SetAIParamID(1700262, 280001)
    SetAIParamID(1700263, 280002)
    SetAIParamID(1700350, 323001)
    SetAIParamID(1700351, 323001)
    SetAIParamID(1700352, 323001)
    SetAIParamID(1700250, 325000)
    SetAIParamID(1700251, 325000)
    SetAIParamID(1700252, 325000)
    SetAIParamID(1700253, 325000)
    SetAIParamID(1700254, 325000)
    SetAIParamID(1700255, 325000)
    SetAIParamID(1700450, 330000)
    SetAIParamID(1700451, 330000)
    SetAIParamID(1700452, 330000)
    SetAIParamID(1700453, 330000)
    SetAIParamID(1700110, 333000)
    SetAIParamID(1700111, 333000)
    SetAIParamID(1700112, 333003)
    SetAIParamID(1700150, 333005)
    SetAIParamID(1700151, 333005)
    SetAIParamID(1700120, 333003)
    SetAIParamID(1700116, 333002)
    SetAIParamID(1700117, 333002)
    SetAIParamID(1700118, 333003)
    SetAIParamID(1700113, 333001)
    SetAIParamID(1700114, 333001)
    SetAIParamID(1700115, 333003)
    SetAIParamID(1700908, 333000)
    SetAIParamID(1700909, 333000)
    SetAIParamID(1700190, 346100)
    SetAIParamID(1700191, 346100)
    SetAIParamID(1703900, 349000)
    SetAIParamID(1703910, 349000)
    SetAIParamID(1703902, 349100)
    SetAIParamID(1703901, 349100)
    SetAIParamID(1703911, 349100)
    SetAIParamID(1703912, 349100)
    SetAIParamID(1700700, 529001)
    SetAIParamID(1700800, 529000)
    SetAIParamID(1700600, 537000)
    SetAIParamID(1700601, 537000)
    SetAIParamID(1700602, 537000)
    SetAIParamID(1700603, 537000)
    SetAIParamID(1700604, 537000)
    SetAIParamID(1700605, 537000)
    SetAIParamID(1700606, 537000)
    SetAIParamID(1700607, 537000)
    SetAIParamID(1700608, 537000)
    SetAIParamID(1700609, 537000)
    SetAIParamID(1700610, 537000)
    SetAIParamID(1700611, 537000)
    SetAIParamID(1700612, 537000)
    SetAIParamID(1700613, 537000)
    SetAIParamID(1700614, 537000)
    SetAIParamID(1700615, 537000)
    SetAIParamID(1700616, 537000)
    SetAIParamID(1700617, 537000)
    SetAIParamID(1700618, 537000)
    SetAIParamID(1700619, 537000)
    SetAIParamID(1700620, 537000)
    SetAIParamID(1700621, 537000)
    SetAIParamID(1700402, 293000)
    SetAIParamID(1700403, 293000)
    SetAIParamID(1700404, 293000)
    SetAIParamID(1700405, 293000)
    SetAIParamID(1700406, 293000)
    SetAIParamID(1700407, 293000)
    SetAIParamID(1700408, 293000)
    SetAIParamID(1700409, 293000)
    SetAIParamID(1700410, 293000)
    SetAIParamID(1700411, 293000)
    SetAIParamID(1700412, 293000)
    SetAIParamID(1700413, 293000)
    SetAIParamID(1700414, 293000)
    SetAIParamID(1700415, 293000)
    SetAIParamID(1700416, 293000)
    SetAIParamID(1700417, 293000)
    SetAIParamID(1700418, 293000)
    SetAIParamID(1700419, 293000)
    SetAIParamID(1700420, 293000)
    SetAIParamID(1700421, 293000)
    SetAIParamID(1700422, 293000)
    SetAIParamID(1700423, 293000)
    SetAIParamID(1700424, 293000)
    SetAIParamID(1700425, 293000)
    SetAIParamID(1700426, 293000)
    SetAIParamID(1700427, 293000)
    SetAIParamID(1700428, 293000)
    SetAIParamID(1700429, 293000)
    SetAIParamID(1700430, 293000)
    SetAIParamID(1700431, 293000)
    SetAIParamID(1700432, 293000)
    SetAIParamID(1700433, 293000)
    SetAIParamID(1700434, 293000)
    SetAIParamID(1700435, 293000)
    SetAIParamID(1700436, 293000)
    SetAIParamID(1700437, 293000)
    SetAIParamID(1700438, 293000)
    SetAIParamID(1700439, 293000)
    SetAIParamID(1700440, 293000)
    SetAIParamID(1700441, 293000)
    SetAIParamID(1700442, 293000)
    SetAIParamID(1700443, 293000)
    SetAIParamID(1700444, 293000)
    SetAIParamID(1700445, 293000)
    SetAIParamID(1700446, 293000)
    SetAIParamID(1700447, 293000)
    SetAIParamID(1700448, 293000)
    SetAIParamID(1700449, 293000)
    SetAIParamID(1700454, 293000)
    SetAIParamID(1700455, 293000)
    SetAIParamID(1700456, 293000)
    SetAIParamID(1700457, 293000)
    SetAIParamID(1700458, 293000)
    SetAIParamID(1700459, 293000)
    SetAIParamID(1700460, 293000)
    SetAIParamID(1700461, 293000)
    SetAIParamID(1700462, 293000)
    SetAIParamID(1700463, 293000)
    SetAIParamID(1700464, 293000)
    SetAIParamID(1700465, 293000)
    SetAIParamID(1700466, 293000)
    SetAIParamID(1700467, 293000)
    SetAIParamID(1700468, 293000)
    SetAIParamID(1700469, 293000)
    SetAIParamID(1700470, 293000)
    SetAIParamID(1700471, 293000)
    SetAIParamID(1700472, 293000)
    SetAIParamID(1700473, 293000)
    SetAIParamID(1700474, 293000)
    SetAIParamID(1700475, 293000)
    SetAIParamID(1700476, 293000)
    SetAIParamID(1700477, 293000)
    SetAIParamID(1700478, 293000)
    SetAIParamID(1700479, 293000)
    SetAIParamID(1700480, 293000)
    SetAIParamID(1700481, 293000)
    SetAIParamID(1700482, 293000)
    SetAIParamID(1700483, 293000)
    SetAIParamID(1700484, 293000)
    SetAIParamID(1700485, 293000)
    SetAIParamID(1700486, 293000)
    SetAIParamID(1700487, 293000)
    SetAIParamID(1700488, 293000)
    SetAIParamID(1700489, 293000)
    SetAIParamID(1700490, 293000)
    SetAIParamID(1700491, 293000)
    SetAIParamID(1700492, 293000)
    SetAIParamID(1700493, 293000)
    SetAIParamID(1700494, 293000)
    SetAIParamID(1700495, 293000)
    SetAIParamID(1700496, 293000)
    SetAIParamID(1700497, 293000)
    SetAIParamID(1700498, 293000)
    SetAIParamID(1700499, 293000)
    SetAIParamID(1700503, 293000)
    SetAIParamID(1700504, 293000)
    SetAIParamID(1700505, 293000)
    SetAIParamID(1700506, 293000)
    SetAIParamID(1700507, 293000)
    
    return RESTART


@RestartOnRest
def EnemySpeedUp():
    """ 11702200: Temporary enemy effect. """
    Await(TriggerFlags.EnemySpeedUp)
    AddSpecialEffect(6032, 200000)
    AddSpecialEffect(6073, 200000)
    AddSpecialEffect(6291, 200000)
    AddSpecialEffect(6610, 200000)
    AddSpecialEffect(6033, 200000)
    AddSpecialEffect(1700960, 200000)
    AddSpecialEffect(1700961, 200000)
    AddSpecialEffect(1700950, 200000)
    AddSpecialEffect(1700962, 200000)
    AddSpecialEffect(1700300, 200000)
    AddSpecialEffect(1700301, 200000)
    AddSpecialEffect(1700900, 200000)
    AddSpecialEffect(1700901, 200000)
    AddSpecialEffect(1700902, 200000)
    AddSpecialEffect(1700903, 200000)
    AddSpecialEffect(1700302, 200000)
    AddSpecialEffect(1700100, 200000)
    AddSpecialEffect(1700202, 200000)
    AddSpecialEffect(1700203, 200000)
    AddSpecialEffect(1700103, 200000)
    AddSpecialEffect(1700102, 200000)
    AddSpecialEffect(1700101, 200000)
    AddSpecialEffect(1700204, 200000)
    AddSpecialEffect(1700205, 200000)
    AddSpecialEffect(1700206, 200000)
    AddSpecialEffect(1700207, 200000)
    AddSpecialEffect(1700208, 200000)
    AddSpecialEffect(1700209, 200000)
    AddSpecialEffect(1700210, 200000)
    AddSpecialEffect(1700211, 200000)
    AddSpecialEffect(1700510, 200000)
    AddSpecialEffect(1700212, 200000)
    AddSpecialEffect(1700213, 200000)
    AddSpecialEffect(1700214, 200000)
    AddSpecialEffect(1700215, 200000)
    AddSpecialEffect(1700904, 200000)
    AddSpecialEffect(1700905, 200000)
    AddSpecialEffect(1700906, 200000)
    AddSpecialEffect(1700907, 200000)
    AddSpecialEffect(1700500, 200000)
    AddSpecialEffect(1700501, 200000)
    AddSpecialEffect(1700502, 200000)
    AddSpecialEffect(1700400, 200000)
    AddSpecialEffect(1700401, 200000)
    AddSpecialEffect(1700200, 200000)
    AddSpecialEffect(1700216, 200000)
    AddSpecialEffect(1700217, 200000)
    AddSpecialEffect(1700218, 200000)
    AddSpecialEffect(1700219, 200000)
    AddSpecialEffect(1700220, 200000)
    AddSpecialEffect(1700221, 200000)
    AddSpecialEffect(1700222, 200000)
    AddSpecialEffect(1700223, 200000)
    AddSpecialEffect(1700224, 200000)
    AddSpecialEffect(1700225, 200000)
    AddSpecialEffect(1700226, 200000)
    AddSpecialEffect(1700227, 200000)
    AddSpecialEffect(1700228, 200000)
    AddSpecialEffect(1700229, 200000)
    AddSpecialEffect(1700230, 200000)
    AddSpecialEffect(1700231, 200000)
    AddSpecialEffect(1700232, 200000)
    AddSpecialEffect(1700233, 200000)
    AddSpecialEffect(1700234, 200000)
    AddSpecialEffect(1700235, 200000)
    AddSpecialEffect(1700236, 200000)
    AddSpecialEffect(1700237, 200000)
    AddSpecialEffect(1700238, 200000)
    AddSpecialEffect(1700239, 200000)
    AddSpecialEffect(1700240, 200000)
    AddSpecialEffect(1700241, 200000)
    AddSpecialEffect(1700242, 200000)
    AddSpecialEffect(1700243, 200000)
    AddSpecialEffect(1700244, 200000)
    AddSpecialEffect(1700245, 200000)
    AddSpecialEffect(1700246, 200000)
    AddSpecialEffect(1700247, 200000)
    AddSpecialEffect(1700248, 200000)
    AddSpecialEffect(1700249, 200000)
    AddSpecialEffect(1700256, 200000)
    AddSpecialEffect(1700257, 200000)
    AddSpecialEffect(1700258, 200000)
    AddSpecialEffect(1700259, 200000)
    AddSpecialEffect(1700260, 200000)
    AddSpecialEffect(1700261, 200000)
    AddSpecialEffect(1700262, 200000)
    AddSpecialEffect(1700263, 200000)
    AddSpecialEffect(1700350, 200000)
    AddSpecialEffect(1700351, 200000)
    AddSpecialEffect(1700352, 200000)
    AddSpecialEffect(1700250, 200000)
    AddSpecialEffect(1700251, 200000)
    AddSpecialEffect(1700252, 200000)
    AddSpecialEffect(1700253, 200000)
    AddSpecialEffect(1700254, 200000)
    AddSpecialEffect(1700255, 200000)
    AddSpecialEffect(1700450, 200000)
    AddSpecialEffect(1700451, 200000)
    AddSpecialEffect(1700452, 200000)
    AddSpecialEffect(1700453, 200000)
    AddSpecialEffect(1700110, 200000)
    AddSpecialEffect(1700111, 200000)
    AddSpecialEffect(1700112, 200000)
    AddSpecialEffect(1700150, 200000)
    AddSpecialEffect(1700151, 200000)
    AddSpecialEffect(1700120, 200000)
    AddSpecialEffect(1700116, 200000)
    AddSpecialEffect(1700117, 200000)
    AddSpecialEffect(1700118, 200000)
    AddSpecialEffect(1700113, 200000)
    AddSpecialEffect(1700114, 200000)
    AddSpecialEffect(1700115, 200000)
    AddSpecialEffect(1700908, 200000)
    AddSpecialEffect(1700909, 200000)
    AddSpecialEffect(1700190, 200000)
    AddSpecialEffect(1700191, 200000)
    AddSpecialEffect(1703900, 200000)
    AddSpecialEffect(1703910, 200000)
    AddSpecialEffect(1703902, 200000)
    AddSpecialEffect(1703901, 200000)
    AddSpecialEffect(1703911, 200000)
    AddSpecialEffect(1703912, 200000)
    AddSpecialEffect(1700700, 200000)
    AddSpecialEffect(1700800, 200000)
    AddSpecialEffect(1700801, 200000)
    WaitFrames(10)  # give other loaded maps time to trigger
    DisableFlag(TriggerFlags.EnemySpeedUp)
    return RESTART


@RestartOnRest
def EnemyExtremeSpeedUp():
    """ 11702201: Temporary enemy effect. """
    Await(TriggerFlags.EnemyExtremeSpeedUp)
    AddSpecialEffect(6032, 200001)
    AddSpecialEffect(6073, 200001)
    AddSpecialEffect(6291, 200001)
    AddSpecialEffect(6610, 200001)
    AddSpecialEffect(6033, 200001)
    AddSpecialEffect(1700960, 200001)
    AddSpecialEffect(1700961, 200001)
    AddSpecialEffect(1700950, 200001)
    AddSpecialEffect(1700962, 200001)
    AddSpecialEffect(1700300, 200001)
    AddSpecialEffect(1700301, 200001)
    AddSpecialEffect(1700900, 200001)
    AddSpecialEffect(1700901, 200001)
    AddSpecialEffect(1700902, 200001)
    AddSpecialEffect(1700903, 200001)
    AddSpecialEffect(1700302, 200001)
    AddSpecialEffect(1700100, 200001)
    AddSpecialEffect(1700202, 200001)
    AddSpecialEffect(1700203, 200001)
    AddSpecialEffect(1700103, 200001)
    AddSpecialEffect(1700102, 200001)
    AddSpecialEffect(1700101, 200001)
    AddSpecialEffect(1700204, 200001)
    AddSpecialEffect(1700205, 200001)
    AddSpecialEffect(1700206, 200001)
    AddSpecialEffect(1700207, 200001)
    AddSpecialEffect(1700208, 200001)
    AddSpecialEffect(1700209, 200001)
    AddSpecialEffect(1700210, 200001)
    AddSpecialEffect(1700211, 200001)
    AddSpecialEffect(1700510, 200001)
    AddSpecialEffect(1700212, 200001)
    AddSpecialEffect(1700213, 200001)
    AddSpecialEffect(1700214, 200001)
    AddSpecialEffect(1700215, 200001)
    AddSpecialEffect(1700904, 200001)
    AddSpecialEffect(1700905, 200001)
    AddSpecialEffect(1700906, 200001)
    AddSpecialEffect(1700907, 200001)
    AddSpecialEffect(1700500, 200001)
    AddSpecialEffect(1700501, 200001)
    AddSpecialEffect(1700502, 200001)
    AddSpecialEffect(1700400, 200001)
    AddSpecialEffect(1700401, 200001)
    AddSpecialEffect(1700200, 200001)
    AddSpecialEffect(1700216, 200001)
    AddSpecialEffect(1700217, 200001)
    AddSpecialEffect(1700218, 200001)
    AddSpecialEffect(1700219, 200001)
    AddSpecialEffect(1700220, 200001)
    AddSpecialEffect(1700221, 200001)
    AddSpecialEffect(1700222, 200001)
    AddSpecialEffect(1700223, 200001)
    AddSpecialEffect(1700224, 200001)
    AddSpecialEffect(1700225, 200001)
    AddSpecialEffect(1700226, 200001)
    AddSpecialEffect(1700227, 200001)
    AddSpecialEffect(1700228, 200001)
    AddSpecialEffect(1700229, 200001)
    AddSpecialEffect(1700230, 200001)
    AddSpecialEffect(1700231, 200001)
    AddSpecialEffect(1700232, 200001)
    AddSpecialEffect(1700233, 200001)
    AddSpecialEffect(1700234, 200001)
    AddSpecialEffect(1700235, 200001)
    AddSpecialEffect(1700236, 200001)
    AddSpecialEffect(1700237, 200001)
    AddSpecialEffect(1700238, 200001)
    AddSpecialEffect(1700239, 200001)
    AddSpecialEffect(1700240, 200001)
    AddSpecialEffect(1700241, 200001)
    AddSpecialEffect(1700242, 200001)
    AddSpecialEffect(1700243, 200001)
    AddSpecialEffect(1700244, 200001)
    AddSpecialEffect(1700245, 200001)
    AddSpecialEffect(1700246, 200001)
    AddSpecialEffect(1700247, 200001)
    AddSpecialEffect(1700248, 200001)
    AddSpecialEffect(1700249, 200001)
    AddSpecialEffect(1700256, 200001)
    AddSpecialEffect(1700257, 200001)
    AddSpecialEffect(1700258, 200001)
    AddSpecialEffect(1700259, 200001)
    AddSpecialEffect(1700260, 200001)
    AddSpecialEffect(1700261, 200001)
    AddSpecialEffect(1700262, 200001)
    AddSpecialEffect(1700263, 200001)
    AddSpecialEffect(1700350, 200001)
    AddSpecialEffect(1700351, 200001)
    AddSpecialEffect(1700352, 200001)
    AddSpecialEffect(1700250, 200001)
    AddSpecialEffect(1700251, 200001)
    AddSpecialEffect(1700252, 200001)
    AddSpecialEffect(1700253, 200001)
    AddSpecialEffect(1700254, 200001)
    AddSpecialEffect(1700255, 200001)
    AddSpecialEffect(1700450, 200001)
    AddSpecialEffect(1700451, 200001)
    AddSpecialEffect(1700452, 200001)
    AddSpecialEffect(1700453, 200001)
    AddSpecialEffect(1700110, 200001)
    AddSpecialEffect(1700111, 200001)
    AddSpecialEffect(1700112, 200001)
    AddSpecialEffect(1700150, 200001)
    AddSpecialEffect(1700151, 200001)
    AddSpecialEffect(1700120, 200001)
    AddSpecialEffect(1700116, 200001)
    AddSpecialEffect(1700117, 200001)
    AddSpecialEffect(1700118, 200001)
    AddSpecialEffect(1700113, 200001)
    AddSpecialEffect(1700114, 200001)
    AddSpecialEffect(1700115, 200001)
    AddSpecialEffect(1700908, 200001)
    AddSpecialEffect(1700909, 200001)
    AddSpecialEffect(1700190, 200001)
    AddSpecialEffect(1700191, 200001)
    AddSpecialEffect(1703900, 200001)
    AddSpecialEffect(1703910, 200001)
    AddSpecialEffect(1703902, 200001)
    AddSpecialEffect(1703901, 200001)
    AddSpecialEffect(1703911, 200001)
    AddSpecialEffect(1703912, 200001)
    AddSpecialEffect(1700700, 200001)
    AddSpecialEffect(1700800, 200001)
    AddSpecialEffect(1700801, 200001)
    WaitFrames(10)  # give other loaded maps time to trigger
    DisableFlag(TriggerFlags.EnemyExtremeSpeedUp)
    return RESTART


@RestartOnRest
def EnemySpeedDown():
    """ 11702202: Temporary enemy effect. """
    Await(TriggerFlags.EnemySpeedDown)
    AddSpecialEffect(6032, 200002)
    AddSpecialEffect(6073, 200002)
    AddSpecialEffect(6291, 200002)
    AddSpecialEffect(6610, 200002)
    AddSpecialEffect(6033, 200002)
    AddSpecialEffect(1700960, 200002)
    AddSpecialEffect(1700961, 200002)
    AddSpecialEffect(1700950, 200002)
    AddSpecialEffect(1700962, 200002)
    AddSpecialEffect(1700300, 200002)
    AddSpecialEffect(1700301, 200002)
    AddSpecialEffect(1700900, 200002)
    AddSpecialEffect(1700901, 200002)
    AddSpecialEffect(1700902, 200002)
    AddSpecialEffect(1700903, 200002)
    AddSpecialEffect(1700302, 200002)
    AddSpecialEffect(1700100, 200002)
    AddSpecialEffect(1700202, 200002)
    AddSpecialEffect(1700203, 200002)
    AddSpecialEffect(1700103, 200002)
    AddSpecialEffect(1700102, 200002)
    AddSpecialEffect(1700101, 200002)
    AddSpecialEffect(1700204, 200002)
    AddSpecialEffect(1700205, 200002)
    AddSpecialEffect(1700206, 200002)
    AddSpecialEffect(1700207, 200002)
    AddSpecialEffect(1700208, 200002)
    AddSpecialEffect(1700209, 200002)
    AddSpecialEffect(1700210, 200002)
    AddSpecialEffect(1700211, 200002)
    AddSpecialEffect(1700510, 200002)
    AddSpecialEffect(1700212, 200002)
    AddSpecialEffect(1700213, 200002)
    AddSpecialEffect(1700214, 200002)
    AddSpecialEffect(1700215, 200002)
    AddSpecialEffect(1700904, 200002)
    AddSpecialEffect(1700905, 200002)
    AddSpecialEffect(1700906, 200002)
    AddSpecialEffect(1700907, 200002)
    AddSpecialEffect(1700500, 200002)
    AddSpecialEffect(1700501, 200002)
    AddSpecialEffect(1700502, 200002)
    AddSpecialEffect(1700400, 200002)
    AddSpecialEffect(1700401, 200002)
    AddSpecialEffect(1700200, 200002)
    AddSpecialEffect(1700216, 200002)
    AddSpecialEffect(1700217, 200002)
    AddSpecialEffect(1700218, 200002)
    AddSpecialEffect(1700219, 200002)
    AddSpecialEffect(1700220, 200002)
    AddSpecialEffect(1700221, 200002)
    AddSpecialEffect(1700222, 200002)
    AddSpecialEffect(1700223, 200002)
    AddSpecialEffect(1700224, 200002)
    AddSpecialEffect(1700225, 200002)
    AddSpecialEffect(1700226, 200002)
    AddSpecialEffect(1700227, 200002)
    AddSpecialEffect(1700228, 200002)
    AddSpecialEffect(1700229, 200002)
    AddSpecialEffect(1700230, 200002)
    AddSpecialEffect(1700231, 200002)
    AddSpecialEffect(1700232, 200002)
    AddSpecialEffect(1700233, 200002)
    AddSpecialEffect(1700234, 200002)
    AddSpecialEffect(1700235, 200002)
    AddSpecialEffect(1700236, 200002)
    AddSpecialEffect(1700237, 200002)
    AddSpecialEffect(1700238, 200002)
    AddSpecialEffect(1700239, 200002)
    AddSpecialEffect(1700240, 200002)
    AddSpecialEffect(1700241, 200002)
    AddSpecialEffect(1700242, 200002)
    AddSpecialEffect(1700243, 200002)
    AddSpecialEffect(1700244, 200002)
    AddSpecialEffect(1700245, 200002)
    AddSpecialEffect(1700246, 200002)
    AddSpecialEffect(1700247, 200002)
    AddSpecialEffect(1700248, 200002)
    AddSpecialEffect(1700249, 200002)
    AddSpecialEffect(1700256, 200002)
    AddSpecialEffect(1700257, 200002)
    AddSpecialEffect(1700258, 200002)
    AddSpecialEffect(1700259, 200002)
    AddSpecialEffect(1700260, 200002)
    AddSpecialEffect(1700261, 200002)
    AddSpecialEffect(1700262, 200002)
    AddSpecialEffect(1700263, 200002)
    AddSpecialEffect(1700350, 200002)
    AddSpecialEffect(1700351, 200002)
    AddSpecialEffect(1700352, 200002)
    AddSpecialEffect(1700250, 200002)
    AddSpecialEffect(1700251, 200002)
    AddSpecialEffect(1700252, 200002)
    AddSpecialEffect(1700253, 200002)
    AddSpecialEffect(1700254, 200002)
    AddSpecialEffect(1700255, 200002)
    AddSpecialEffect(1700450, 200002)
    AddSpecialEffect(1700451, 200002)
    AddSpecialEffect(1700452, 200002)
    AddSpecialEffect(1700453, 200002)
    AddSpecialEffect(1700110, 200002)
    AddSpecialEffect(1700111, 200002)
    AddSpecialEffect(1700112, 200002)
    AddSpecialEffect(1700150, 200002)
    AddSpecialEffect(1700151, 200002)
    AddSpecialEffect(1700120, 200002)
    AddSpecialEffect(1700116, 200002)
    AddSpecialEffect(1700117, 200002)
    AddSpecialEffect(1700118, 200002)
    AddSpecialEffect(1700113, 200002)
    AddSpecialEffect(1700114, 200002)
    AddSpecialEffect(1700115, 200002)
    AddSpecialEffect(1700908, 200002)
    AddSpecialEffect(1700909, 200002)
    AddSpecialEffect(1700190, 200002)
    AddSpecialEffect(1700191, 200002)
    AddSpecialEffect(1703900, 200002)
    AddSpecialEffect(1703910, 200002)
    AddSpecialEffect(1703902, 200002)
    AddSpecialEffect(1703901, 200002)
    AddSpecialEffect(1703911, 200002)
    AddSpecialEffect(1703912, 200002)
    AddSpecialEffect(1700700, 200002)
    AddSpecialEffect(1700800, 200002)
    AddSpecialEffect(1700801, 200002)
    WaitFrames(10)  # give other loaded maps time to trigger
    DisableFlag(TriggerFlags.EnemySpeedDown)
    return RESTART


@RestartOnRest
def EnemyExtremeSpeedDown():
    """ 11702203: Temporary enemy effect. """
    Await(TriggerFlags.EnemyExtremeSpeedDown)
    AddSpecialEffect(6032, 200003)
    AddSpecialEffect(6073, 200003)
    AddSpecialEffect(6291, 200003)
    AddSpecialEffect(6610, 200003)
    AddSpecialEffect(6033, 200003)
    AddSpecialEffect(1700960, 200003)
    AddSpecialEffect(1700961, 200003)
    AddSpecialEffect(1700950, 200003)
    AddSpecialEffect(1700962, 200003)
    AddSpecialEffect(1700300, 200003)
    AddSpecialEffect(1700301, 200003)
    AddSpecialEffect(1700900, 200003)
    AddSpecialEffect(1700901, 200003)
    AddSpecialEffect(1700902, 200003)
    AddSpecialEffect(1700903, 200003)
    AddSpecialEffect(1700302, 200003)
    AddSpecialEffect(1700100, 200003)
    AddSpecialEffect(1700202, 200003)
    AddSpecialEffect(1700203, 200003)
    AddSpecialEffect(1700103, 200003)
    AddSpecialEffect(1700102, 200003)
    AddSpecialEffect(1700101, 200003)
    AddSpecialEffect(1700204, 200003)
    AddSpecialEffect(1700205, 200003)
    AddSpecialEffect(1700206, 200003)
    AddSpecialEffect(1700207, 200003)
    AddSpecialEffect(1700208, 200003)
    AddSpecialEffect(1700209, 200003)
    AddSpecialEffect(1700210, 200003)
    AddSpecialEffect(1700211, 200003)
    AddSpecialEffect(1700510, 200003)
    AddSpecialEffect(1700212, 200003)
    AddSpecialEffect(1700213, 200003)
    AddSpecialEffect(1700214, 200003)
    AddSpecialEffect(1700215, 200003)
    AddSpecialEffect(1700904, 200003)
    AddSpecialEffect(1700905, 200003)
    AddSpecialEffect(1700906, 200003)
    AddSpecialEffect(1700907, 200003)
    AddSpecialEffect(1700500, 200003)
    AddSpecialEffect(1700501, 200003)
    AddSpecialEffect(1700502, 200003)
    AddSpecialEffect(1700400, 200003)
    AddSpecialEffect(1700401, 200003)
    AddSpecialEffect(1700200, 200003)
    AddSpecialEffect(1700216, 200003)
    AddSpecialEffect(1700217, 200003)
    AddSpecialEffect(1700218, 200003)
    AddSpecialEffect(1700219, 200003)
    AddSpecialEffect(1700220, 200003)
    AddSpecialEffect(1700221, 200003)
    AddSpecialEffect(1700222, 200003)
    AddSpecialEffect(1700223, 200003)
    AddSpecialEffect(1700224, 200003)
    AddSpecialEffect(1700225, 200003)
    AddSpecialEffect(1700226, 200003)
    AddSpecialEffect(1700227, 200003)
    AddSpecialEffect(1700228, 200003)
    AddSpecialEffect(1700229, 200003)
    AddSpecialEffect(1700230, 200003)
    AddSpecialEffect(1700231, 200003)
    AddSpecialEffect(1700232, 200003)
    AddSpecialEffect(1700233, 200003)
    AddSpecialEffect(1700234, 200003)
    AddSpecialEffect(1700235, 200003)
    AddSpecialEffect(1700236, 200003)
    AddSpecialEffect(1700237, 200003)
    AddSpecialEffect(1700238, 200003)
    AddSpecialEffect(1700239, 200003)
    AddSpecialEffect(1700240, 200003)
    AddSpecialEffect(1700241, 200003)
    AddSpecialEffect(1700242, 200003)
    AddSpecialEffect(1700243, 200003)
    AddSpecialEffect(1700244, 200003)
    AddSpecialEffect(1700245, 200003)
    AddSpecialEffect(1700246, 200003)
    AddSpecialEffect(1700247, 200003)
    AddSpecialEffect(1700248, 200003)
    AddSpecialEffect(1700249, 200003)
    AddSpecialEffect(1700256, 200003)
    AddSpecialEffect(1700257, 200003)
    AddSpecialEffect(1700258, 200003)
    AddSpecialEffect(1700259, 200003)
    AddSpecialEffect(1700260, 200003)
    AddSpecialEffect(1700261, 200003)
    AddSpecialEffect(1700262, 200003)
    AddSpecialEffect(1700263, 200003)
    AddSpecialEffect(1700350, 200003)
    AddSpecialEffect(1700351, 200003)
    AddSpecialEffect(1700352, 200003)
    AddSpecialEffect(1700250, 200003)
    AddSpecialEffect(1700251, 200003)
    AddSpecialEffect(1700252, 200003)
    AddSpecialEffect(1700253, 200003)
    AddSpecialEffect(1700254, 200003)
    AddSpecialEffect(1700255, 200003)
    AddSpecialEffect(1700450, 200003)
    AddSpecialEffect(1700451, 200003)
    AddSpecialEffect(1700452, 200003)
    AddSpecialEffect(1700453, 200003)
    AddSpecialEffect(1700110, 200003)
    AddSpecialEffect(1700111, 200003)
    AddSpecialEffect(1700112, 200003)
    AddSpecialEffect(1700150, 200003)
    AddSpecialEffect(1700151, 200003)
    AddSpecialEffect(1700120, 200003)
    AddSpecialEffect(1700116, 200003)
    AddSpecialEffect(1700117, 200003)
    AddSpecialEffect(1700118, 200003)
    AddSpecialEffect(1700113, 200003)
    AddSpecialEffect(1700114, 200003)
    AddSpecialEffect(1700115, 200003)
    AddSpecialEffect(1700908, 200003)
    AddSpecialEffect(1700909, 200003)
    AddSpecialEffect(1700190, 200003)
    AddSpecialEffect(1700191, 200003)
    AddSpecialEffect(1703900, 200003)
    AddSpecialEffect(1703910, 200003)
    AddSpecialEffect(1703902, 200003)
    AddSpecialEffect(1703901, 200003)
    AddSpecialEffect(1703911, 200003)
    AddSpecialEffect(1703912, 200003)
    AddSpecialEffect(1700700, 200003)
    AddSpecialEffect(1700800, 200003)
    AddSpecialEffect(1700801, 200003)
    WaitFrames(10)  # give other loaded maps time to trigger
    DisableFlag(TriggerFlags.EnemyExtremeSpeedDown)
    return RESTART


@RestartOnRest
def EnemyHealthRegain():
    """ 11702204: Temporary enemy effect. """
    Await(TriggerFlags.EnemyHealthRegain)
    AddSpecialEffect(6032, 200004)
    AddSpecialEffect(6073, 200004)
    AddSpecialEffect(6291, 200004)
    AddSpecialEffect(6610, 200004)
    AddSpecialEffect(6033, 200004)
    AddSpecialEffect(1700960, 200004)
    AddSpecialEffect(1700961, 200004)
    AddSpecialEffect(1700950, 200004)
    AddSpecialEffect(1700962, 200004)
    AddSpecialEffect(1700300, 200004)
    AddSpecialEffect(1700301, 200004)
    AddSpecialEffect(1700900, 200004)
    AddSpecialEffect(1700901, 200004)
    AddSpecialEffect(1700902, 200004)
    AddSpecialEffect(1700903, 200004)
    AddSpecialEffect(1700302, 200004)
    AddSpecialEffect(1700100, 200004)
    AddSpecialEffect(1700202, 200004)
    AddSpecialEffect(1700203, 200004)
    AddSpecialEffect(1700103, 200004)
    AddSpecialEffect(1700102, 200004)
    AddSpecialEffect(1700101, 200004)
    AddSpecialEffect(1700204, 200004)
    AddSpecialEffect(1700205, 200004)
    AddSpecialEffect(1700206, 200004)
    AddSpecialEffect(1700207, 200004)
    AddSpecialEffect(1700208, 200004)
    AddSpecialEffect(1700209, 200004)
    AddSpecialEffect(1700210, 200004)
    AddSpecialEffect(1700211, 200004)
    AddSpecialEffect(1700510, 200004)
    AddSpecialEffect(1700212, 200004)
    AddSpecialEffect(1700213, 200004)
    AddSpecialEffect(1700214, 200004)
    AddSpecialEffect(1700215, 200004)
    AddSpecialEffect(1700904, 200004)
    AddSpecialEffect(1700905, 200004)
    AddSpecialEffect(1700906, 200004)
    AddSpecialEffect(1700907, 200004)
    AddSpecialEffect(1700500, 200004)
    AddSpecialEffect(1700501, 200004)
    AddSpecialEffect(1700502, 200004)
    AddSpecialEffect(1700400, 200004)
    AddSpecialEffect(1700401, 200004)
    AddSpecialEffect(1700200, 200004)
    AddSpecialEffect(1700216, 200004)
    AddSpecialEffect(1700217, 200004)
    AddSpecialEffect(1700218, 200004)
    AddSpecialEffect(1700219, 200004)
    AddSpecialEffect(1700220, 200004)
    AddSpecialEffect(1700221, 200004)
    AddSpecialEffect(1700222, 200004)
    AddSpecialEffect(1700223, 200004)
    AddSpecialEffect(1700224, 200004)
    AddSpecialEffect(1700225, 200004)
    AddSpecialEffect(1700226, 200004)
    AddSpecialEffect(1700227, 200004)
    AddSpecialEffect(1700228, 200004)
    AddSpecialEffect(1700229, 200004)
    AddSpecialEffect(1700230, 200004)
    AddSpecialEffect(1700231, 200004)
    AddSpecialEffect(1700232, 200004)
    AddSpecialEffect(1700233, 200004)
    AddSpecialEffect(1700234, 200004)
    AddSpecialEffect(1700235, 200004)
    AddSpecialEffect(1700236, 200004)
    AddSpecialEffect(1700237, 200004)
    AddSpecialEffect(1700238, 200004)
    AddSpecialEffect(1700239, 200004)
    AddSpecialEffect(1700240, 200004)
    AddSpecialEffect(1700241, 200004)
    AddSpecialEffect(1700242, 200004)
    AddSpecialEffect(1700243, 200004)
    AddSpecialEffect(1700244, 200004)
    AddSpecialEffect(1700245, 200004)
    AddSpecialEffect(1700246, 200004)
    AddSpecialEffect(1700247, 200004)
    AddSpecialEffect(1700248, 200004)
    AddSpecialEffect(1700249, 200004)
    AddSpecialEffect(1700256, 200004)
    AddSpecialEffect(1700257, 200004)
    AddSpecialEffect(1700258, 200004)
    AddSpecialEffect(1700259, 200004)
    AddSpecialEffect(1700260, 200004)
    AddSpecialEffect(1700261, 200004)
    AddSpecialEffect(1700262, 200004)
    AddSpecialEffect(1700263, 200004)
    AddSpecialEffect(1700350, 200004)
    AddSpecialEffect(1700351, 200004)
    AddSpecialEffect(1700352, 200004)
    AddSpecialEffect(1700250, 200004)
    AddSpecialEffect(1700251, 200004)
    AddSpecialEffect(1700252, 200004)
    AddSpecialEffect(1700253, 200004)
    AddSpecialEffect(1700254, 200004)
    AddSpecialEffect(1700255, 200004)
    AddSpecialEffect(1700450, 200004)
    AddSpecialEffect(1700451, 200004)
    AddSpecialEffect(1700452, 200004)
    AddSpecialEffect(1700453, 200004)
    AddSpecialEffect(1700110, 200004)
    AddSpecialEffect(1700111, 200004)
    AddSpecialEffect(1700112, 200004)
    AddSpecialEffect(1700150, 200004)
    AddSpecialEffect(1700151, 200004)
    AddSpecialEffect(1700120, 200004)
    AddSpecialEffect(1700116, 200004)
    AddSpecialEffect(1700117, 200004)
    AddSpecialEffect(1700118, 200004)
    AddSpecialEffect(1700113, 200004)
    AddSpecialEffect(1700114, 200004)
    AddSpecialEffect(1700115, 200004)
    AddSpecialEffect(1700908, 200004)
    AddSpecialEffect(1700909, 200004)
    AddSpecialEffect(1700190, 200004)
    AddSpecialEffect(1700191, 200004)
    AddSpecialEffect(1703900, 200004)
    AddSpecialEffect(1703910, 200004)
    AddSpecialEffect(1703902, 200004)
    AddSpecialEffect(1703901, 200004)
    AddSpecialEffect(1703911, 200004)
    AddSpecialEffect(1703912, 200004)
    AddSpecialEffect(1700700, 200004)
    AddSpecialEffect(1700800, 200004)
    AddSpecialEffect(1700801, 200004)
    WaitFrames(10)  # give other loaded maps time to trigger
    DisableFlag(TriggerFlags.EnemyHealthRegain)
    return RESTART


@RestartOnRest
def EnemyMaxHealthUp():
    """ 11702205: Temporary enemy effect. """
    Await(TriggerFlags.EnemyMaxHealthUp)
    AddSpecialEffect(6032, 200005)
    AddSpecialEffect(6073, 200005)
    AddSpecialEffect(6291, 200005)
    AddSpecialEffect(6610, 200005)
    AddSpecialEffect(6033, 200005)
    AddSpecialEffect(1700960, 200005)
    AddSpecialEffect(1700961, 200005)
    AddSpecialEffect(1700950, 200005)
    AddSpecialEffect(1700962, 200005)
    AddSpecialEffect(1700300, 200005)
    AddSpecialEffect(1700301, 200005)
    AddSpecialEffect(1700900, 200005)
    AddSpecialEffect(1700901, 200005)
    AddSpecialEffect(1700902, 200005)
    AddSpecialEffect(1700903, 200005)
    AddSpecialEffect(1700302, 200005)
    AddSpecialEffect(1700100, 200005)
    AddSpecialEffect(1700202, 200005)
    AddSpecialEffect(1700203, 200005)
    AddSpecialEffect(1700103, 200005)
    AddSpecialEffect(1700102, 200005)
    AddSpecialEffect(1700101, 200005)
    AddSpecialEffect(1700204, 200005)
    AddSpecialEffect(1700205, 200005)
    AddSpecialEffect(1700206, 200005)
    AddSpecialEffect(1700207, 200005)
    AddSpecialEffect(1700208, 200005)
    AddSpecialEffect(1700209, 200005)
    AddSpecialEffect(1700210, 200005)
    AddSpecialEffect(1700211, 200005)
    AddSpecialEffect(1700510, 200005)
    AddSpecialEffect(1700212, 200005)
    AddSpecialEffect(1700213, 200005)
    AddSpecialEffect(1700214, 200005)
    AddSpecialEffect(1700215, 200005)
    AddSpecialEffect(1700904, 200005)
    AddSpecialEffect(1700905, 200005)
    AddSpecialEffect(1700906, 200005)
    AddSpecialEffect(1700907, 200005)
    AddSpecialEffect(1700500, 200005)
    AddSpecialEffect(1700501, 200005)
    AddSpecialEffect(1700502, 200005)
    AddSpecialEffect(1700400, 200005)
    AddSpecialEffect(1700401, 200005)
    AddSpecialEffect(1700200, 200005)
    AddSpecialEffect(1700216, 200005)
    AddSpecialEffect(1700217, 200005)
    AddSpecialEffect(1700218, 200005)
    AddSpecialEffect(1700219, 200005)
    AddSpecialEffect(1700220, 200005)
    AddSpecialEffect(1700221, 200005)
    AddSpecialEffect(1700222, 200005)
    AddSpecialEffect(1700223, 200005)
    AddSpecialEffect(1700224, 200005)
    AddSpecialEffect(1700225, 200005)
    AddSpecialEffect(1700226, 200005)
    AddSpecialEffect(1700227, 200005)
    AddSpecialEffect(1700228, 200005)
    AddSpecialEffect(1700229, 200005)
    AddSpecialEffect(1700230, 200005)
    AddSpecialEffect(1700231, 200005)
    AddSpecialEffect(1700232, 200005)
    AddSpecialEffect(1700233, 200005)
    AddSpecialEffect(1700234, 200005)
    AddSpecialEffect(1700235, 200005)
    AddSpecialEffect(1700236, 200005)
    AddSpecialEffect(1700237, 200005)
    AddSpecialEffect(1700238, 200005)
    AddSpecialEffect(1700239, 200005)
    AddSpecialEffect(1700240, 200005)
    AddSpecialEffect(1700241, 200005)
    AddSpecialEffect(1700242, 200005)
    AddSpecialEffect(1700243, 200005)
    AddSpecialEffect(1700244, 200005)
    AddSpecialEffect(1700245, 200005)
    AddSpecialEffect(1700246, 200005)
    AddSpecialEffect(1700247, 200005)
    AddSpecialEffect(1700248, 200005)
    AddSpecialEffect(1700249, 200005)
    AddSpecialEffect(1700256, 200005)
    AddSpecialEffect(1700257, 200005)
    AddSpecialEffect(1700258, 200005)
    AddSpecialEffect(1700259, 200005)
    AddSpecialEffect(1700260, 200005)
    AddSpecialEffect(1700261, 200005)
    AddSpecialEffect(1700262, 200005)
    AddSpecialEffect(1700263, 200005)
    AddSpecialEffect(1700350, 200005)
    AddSpecialEffect(1700351, 200005)
    AddSpecialEffect(1700352, 200005)
    AddSpecialEffect(1700250, 200005)
    AddSpecialEffect(1700251, 200005)
    AddSpecialEffect(1700252, 200005)
    AddSpecialEffect(1700253, 200005)
    AddSpecialEffect(1700254, 200005)
    AddSpecialEffect(1700255, 200005)
    AddSpecialEffect(1700450, 200005)
    AddSpecialEffect(1700451, 200005)
    AddSpecialEffect(1700452, 200005)
    AddSpecialEffect(1700453, 200005)
    AddSpecialEffect(1700110, 200005)
    AddSpecialEffect(1700111, 200005)
    AddSpecialEffect(1700112, 200005)
    AddSpecialEffect(1700150, 200005)
    AddSpecialEffect(1700151, 200005)
    AddSpecialEffect(1700120, 200005)
    AddSpecialEffect(1700116, 200005)
    AddSpecialEffect(1700117, 200005)
    AddSpecialEffect(1700118, 200005)
    AddSpecialEffect(1700113, 200005)
    AddSpecialEffect(1700114, 200005)
    AddSpecialEffect(1700115, 200005)
    AddSpecialEffect(1700908, 200005)
    AddSpecialEffect(1700909, 200005)
    AddSpecialEffect(1700190, 200005)
    AddSpecialEffect(1700191, 200005)
    AddSpecialEffect(1703900, 200005)
    AddSpecialEffect(1703910, 200005)
    AddSpecialEffect(1703902, 200005)
    AddSpecialEffect(1703901, 200005)
    AddSpecialEffect(1703911, 200005)
    AddSpecialEffect(1703912, 200005)
    AddSpecialEffect(1700700, 200005)
    AddSpecialEffect(1700800, 200005)
    AddSpecialEffect(1700801, 200005)
    WaitFrames(10)  # give other loaded maps time to trigger
    DisableFlag(TriggerFlags.EnemyMaxHealthUp)
    return RESTART


@RestartOnRest
def EnemyMaxHealthDown():
    """ 11702206: Temporary enemy effect. """
    Await(TriggerFlags.EnemyMaxHealthDown)
    AddSpecialEffect(6032, 200006)
    AddSpecialEffect(6073, 200006)
    AddSpecialEffect(6291, 200006)
    AddSpecialEffect(6610, 200006)
    AddSpecialEffect(6033, 200006)
    AddSpecialEffect(1700960, 200006)
    AddSpecialEffect(1700961, 200006)
    AddSpecialEffect(1700950, 200006)
    AddSpecialEffect(1700962, 200006)
    AddSpecialEffect(1700300, 200006)
    AddSpecialEffect(1700301, 200006)
    AddSpecialEffect(1700900, 200006)
    AddSpecialEffect(1700901, 200006)
    AddSpecialEffect(1700902, 200006)
    AddSpecialEffect(1700903, 200006)
    AddSpecialEffect(1700302, 200006)
    AddSpecialEffect(1700100, 200006)
    AddSpecialEffect(1700202, 200006)
    AddSpecialEffect(1700203, 200006)
    AddSpecialEffect(1700103, 200006)
    AddSpecialEffect(1700102, 200006)
    AddSpecialEffect(1700101, 200006)
    AddSpecialEffect(1700204, 200006)
    AddSpecialEffect(1700205, 200006)
    AddSpecialEffect(1700206, 200006)
    AddSpecialEffect(1700207, 200006)
    AddSpecialEffect(1700208, 200006)
    AddSpecialEffect(1700209, 200006)
    AddSpecialEffect(1700210, 200006)
    AddSpecialEffect(1700211, 200006)
    AddSpecialEffect(1700510, 200006)
    AddSpecialEffect(1700212, 200006)
    AddSpecialEffect(1700213, 200006)
    AddSpecialEffect(1700214, 200006)
    AddSpecialEffect(1700215, 200006)
    AddSpecialEffect(1700904, 200006)
    AddSpecialEffect(1700905, 200006)
    AddSpecialEffect(1700906, 200006)
    AddSpecialEffect(1700907, 200006)
    AddSpecialEffect(1700500, 200006)
    AddSpecialEffect(1700501, 200006)
    AddSpecialEffect(1700502, 200006)
    AddSpecialEffect(1700400, 200006)
    AddSpecialEffect(1700401, 200006)
    AddSpecialEffect(1700200, 200006)
    AddSpecialEffect(1700216, 200006)
    AddSpecialEffect(1700217, 200006)
    AddSpecialEffect(1700218, 200006)
    AddSpecialEffect(1700219, 200006)
    AddSpecialEffect(1700220, 200006)
    AddSpecialEffect(1700221, 200006)
    AddSpecialEffect(1700222, 200006)
    AddSpecialEffect(1700223, 200006)
    AddSpecialEffect(1700224, 200006)
    AddSpecialEffect(1700225, 200006)
    AddSpecialEffect(1700226, 200006)
    AddSpecialEffect(1700227, 200006)
    AddSpecialEffect(1700228, 200006)
    AddSpecialEffect(1700229, 200006)
    AddSpecialEffect(1700230, 200006)
    AddSpecialEffect(1700231, 200006)
    AddSpecialEffect(1700232, 200006)
    AddSpecialEffect(1700233, 200006)
    AddSpecialEffect(1700234, 200006)
    AddSpecialEffect(1700235, 200006)
    AddSpecialEffect(1700236, 200006)
    AddSpecialEffect(1700237, 200006)
    AddSpecialEffect(1700238, 200006)
    AddSpecialEffect(1700239, 200006)
    AddSpecialEffect(1700240, 200006)
    AddSpecialEffect(1700241, 200006)
    AddSpecialEffect(1700242, 200006)
    AddSpecialEffect(1700243, 200006)
    AddSpecialEffect(1700244, 200006)
    AddSpecialEffect(1700245, 200006)
    AddSpecialEffect(1700246, 200006)
    AddSpecialEffect(1700247, 200006)
    AddSpecialEffect(1700248, 200006)
    AddSpecialEffect(1700249, 200006)
    AddSpecialEffect(1700256, 200006)
    AddSpecialEffect(1700257, 200006)
    AddSpecialEffect(1700258, 200006)
    AddSpecialEffect(1700259, 200006)
    AddSpecialEffect(1700260, 200006)
    AddSpecialEffect(1700261, 200006)
    AddSpecialEffect(1700262, 200006)
    AddSpecialEffect(1700263, 200006)
    AddSpecialEffect(1700350, 200006)
    AddSpecialEffect(1700351, 200006)
    AddSpecialEffect(1700352, 200006)
    AddSpecialEffect(1700250, 200006)
    AddSpecialEffect(1700251, 200006)
    AddSpecialEffect(1700252, 200006)
    AddSpecialEffect(1700253, 200006)
    AddSpecialEffect(1700254, 200006)
    AddSpecialEffect(1700255, 200006)
    AddSpecialEffect(1700450, 200006)
    AddSpecialEffect(1700451, 200006)
    AddSpecialEffect(1700452, 200006)
    AddSpecialEffect(1700453, 200006)
    AddSpecialEffect(1700110, 200006)
    AddSpecialEffect(1700111, 200006)
    AddSpecialEffect(1700112, 200006)
    AddSpecialEffect(1700150, 200006)
    AddSpecialEffect(1700151, 200006)
    AddSpecialEffect(1700120, 200006)
    AddSpecialEffect(1700116, 200006)
    AddSpecialEffect(1700117, 200006)
    AddSpecialEffect(1700118, 200006)
    AddSpecialEffect(1700113, 200006)
    AddSpecialEffect(1700114, 200006)
    AddSpecialEffect(1700115, 200006)
    AddSpecialEffect(1700908, 200006)
    AddSpecialEffect(1700909, 200006)
    AddSpecialEffect(1700190, 200006)
    AddSpecialEffect(1700191, 200006)
    AddSpecialEffect(1703900, 200006)
    AddSpecialEffect(1703910, 200006)
    AddSpecialEffect(1703902, 200006)
    AddSpecialEffect(1703901, 200006)
    AddSpecialEffect(1703911, 200006)
    AddSpecialEffect(1703912, 200006)
    AddSpecialEffect(1700700, 200006)
    AddSpecialEffect(1700800, 200006)
    AddSpecialEffect(1700801, 200006)
    WaitFrames(10)  # give other loaded maps time to trigger
    DisableFlag(TriggerFlags.EnemyMaxHealthDown)
    return RESTART


@RestartOnRest
def EnemyDefenseUp():
    """ 11702207: Temporary enemy effect. """
    Await(TriggerFlags.EnemyDefenseUp)
    AddSpecialEffect(6032, 200007)
    AddSpecialEffect(6073, 200007)
    AddSpecialEffect(6291, 200007)
    AddSpecialEffect(6610, 200007)
    AddSpecialEffect(6033, 200007)
    AddSpecialEffect(1700960, 200007)
    AddSpecialEffect(1700961, 200007)
    AddSpecialEffect(1700950, 200007)
    AddSpecialEffect(1700962, 200007)
    AddSpecialEffect(1700300, 200007)
    AddSpecialEffect(1700301, 200007)
    AddSpecialEffect(1700900, 200007)
    AddSpecialEffect(1700901, 200007)
    AddSpecialEffect(1700902, 200007)
    AddSpecialEffect(1700903, 200007)
    AddSpecialEffect(1700302, 200007)
    AddSpecialEffect(1700100, 200007)
    AddSpecialEffect(1700202, 200007)
    AddSpecialEffect(1700203, 200007)
    AddSpecialEffect(1700103, 200007)
    AddSpecialEffect(1700102, 200007)
    AddSpecialEffect(1700101, 200007)
    AddSpecialEffect(1700204, 200007)
    AddSpecialEffect(1700205, 200007)
    AddSpecialEffect(1700206, 200007)
    AddSpecialEffect(1700207, 200007)
    AddSpecialEffect(1700208, 200007)
    AddSpecialEffect(1700209, 200007)
    AddSpecialEffect(1700210, 200007)
    AddSpecialEffect(1700211, 200007)
    AddSpecialEffect(1700510, 200007)
    AddSpecialEffect(1700212, 200007)
    AddSpecialEffect(1700213, 200007)
    AddSpecialEffect(1700214, 200007)
    AddSpecialEffect(1700215, 200007)
    AddSpecialEffect(1700904, 200007)
    AddSpecialEffect(1700905, 200007)
    AddSpecialEffect(1700906, 200007)
    AddSpecialEffect(1700907, 200007)
    AddSpecialEffect(1700500, 200007)
    AddSpecialEffect(1700501, 200007)
    AddSpecialEffect(1700502, 200007)
    AddSpecialEffect(1700400, 200007)
    AddSpecialEffect(1700401, 200007)
    AddSpecialEffect(1700200, 200007)
    AddSpecialEffect(1700216, 200007)
    AddSpecialEffect(1700217, 200007)
    AddSpecialEffect(1700218, 200007)
    AddSpecialEffect(1700219, 200007)
    AddSpecialEffect(1700220, 200007)
    AddSpecialEffect(1700221, 200007)
    AddSpecialEffect(1700222, 200007)
    AddSpecialEffect(1700223, 200007)
    AddSpecialEffect(1700224, 200007)
    AddSpecialEffect(1700225, 200007)
    AddSpecialEffect(1700226, 200007)
    AddSpecialEffect(1700227, 200007)
    AddSpecialEffect(1700228, 200007)
    AddSpecialEffect(1700229, 200007)
    AddSpecialEffect(1700230, 200007)
    AddSpecialEffect(1700231, 200007)
    AddSpecialEffect(1700232, 200007)
    AddSpecialEffect(1700233, 200007)
    AddSpecialEffect(1700234, 200007)
    AddSpecialEffect(1700235, 200007)
    AddSpecialEffect(1700236, 200007)
    AddSpecialEffect(1700237, 200007)
    AddSpecialEffect(1700238, 200007)
    AddSpecialEffect(1700239, 200007)
    AddSpecialEffect(1700240, 200007)
    AddSpecialEffect(1700241, 200007)
    AddSpecialEffect(1700242, 200007)
    AddSpecialEffect(1700243, 200007)
    AddSpecialEffect(1700244, 200007)
    AddSpecialEffect(1700245, 200007)
    AddSpecialEffect(1700246, 200007)
    AddSpecialEffect(1700247, 200007)
    AddSpecialEffect(1700248, 200007)
    AddSpecialEffect(1700249, 200007)
    AddSpecialEffect(1700256, 200007)
    AddSpecialEffect(1700257, 200007)
    AddSpecialEffect(1700258, 200007)
    AddSpecialEffect(1700259, 200007)
    AddSpecialEffect(1700260, 200007)
    AddSpecialEffect(1700261, 200007)
    AddSpecialEffect(1700262, 200007)
    AddSpecialEffect(1700263, 200007)
    AddSpecialEffect(1700350, 200007)
    AddSpecialEffect(1700351, 200007)
    AddSpecialEffect(1700352, 200007)
    AddSpecialEffect(1700250, 200007)
    AddSpecialEffect(1700251, 200007)
    AddSpecialEffect(1700252, 200007)
    AddSpecialEffect(1700253, 200007)
    AddSpecialEffect(1700254, 200007)
    AddSpecialEffect(1700255, 200007)
    AddSpecialEffect(1700450, 200007)
    AddSpecialEffect(1700451, 200007)
    AddSpecialEffect(1700452, 200007)
    AddSpecialEffect(1700453, 200007)
    AddSpecialEffect(1700110, 200007)
    AddSpecialEffect(1700111, 200007)
    AddSpecialEffect(1700112, 200007)
    AddSpecialEffect(1700150, 200007)
    AddSpecialEffect(1700151, 200007)
    AddSpecialEffect(1700120, 200007)
    AddSpecialEffect(1700116, 200007)
    AddSpecialEffect(1700117, 200007)
    AddSpecialEffect(1700118, 200007)
    AddSpecialEffect(1700113, 200007)
    AddSpecialEffect(1700114, 200007)
    AddSpecialEffect(1700115, 200007)
    AddSpecialEffect(1700908, 200007)
    AddSpecialEffect(1700909, 200007)
    AddSpecialEffect(1700190, 200007)
    AddSpecialEffect(1700191, 200007)
    AddSpecialEffect(1703900, 200007)
    AddSpecialEffect(1703910, 200007)
    AddSpecialEffect(1703902, 200007)
    AddSpecialEffect(1703901, 200007)
    AddSpecialEffect(1703911, 200007)
    AddSpecialEffect(1703912, 200007)
    AddSpecialEffect(1700700, 200007)
    AddSpecialEffect(1700800, 200007)
    AddSpecialEffect(1700801, 200007)
    WaitFrames(10)  # give other loaded maps time to trigger
    DisableFlag(TriggerFlags.EnemyDefenseUp)
    return RESTART
