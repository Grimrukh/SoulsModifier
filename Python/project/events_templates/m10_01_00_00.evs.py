"""
linked:


strings:

"""
from soulstruct.darksouls1r.events import *
from ..entities.m10_01_00_00_entities import *
from ..entities.common_entities import *


def Constructor():
    """ 0: Event 0 """
    RunEvent(11010008)
    DisableFlag(11010580)
    SkipLinesIfFlagOff(2, 61010610)
    EndOfAnimation(Objects.o1201_1000, 2)
    EnableNavmeshType(Navigation.Navmesh_GateLever, NavmeshType.Solid)
    SkipLinesIfClient(24)
    DisableObject(Objects.o1407_0000)
    DeleteVFX(VFX.MultiplayerFog1, erase_root_only=False)
    DisableObject(Objects.o1408_0000)
    DeleteVFX(VFX.MultiplayerFog2, erase_root_only=False)
    DisableObject(Objects.o1409_0000)
    DeleteVFX(VFX.MultiplayerFog3, erase_root_only=False)
    DisableObject(Objects.o1410_0000)
    DeleteVFX(VFX.MultiplayerFog4, erase_root_only=False)
    DisableObject(Objects.o1411_0000)
    DeleteVFX(VFX.MultiplayerFog5, erase_root_only=False)
    DisableObject(Objects.o1412_0000)
    DeleteVFX(VFX.MultiplayerFog6, erase_root_only=False)
    DisableObject(Objects.o1415_0000)
    DeleteVFX(VFX.MultiplayerFog7, erase_root_only=False)
    DisableObject(Objects.o1417_0000)
    DeleteVFX(VFX.MultiplayerFog8, erase_root_only=False)
    DisableObject(Objects.o1418_0000)
    DeleteVFX(VFX.MultiplayerFog9, erase_root_only=False)
    DisableObject(Objects.o1414_0000)
    DeleteVFX(VFX.MultiplayerFog10, erase_root_only=False)
    DisableObject(Objects.o1421_0000)
    DeleteVFX(VFX.MultiplayerFog11, erase_root_only=False)
    DisableObject(Objects.o1421_0001)
    DeleteVFX(VFX.MultiplayerFog12, erase_root_only=False)
    RunEvent(
        11010090,
        slot=0,
        args=(Objects.o1419_0000, VFX.CheckpointFog1, Boxes.CheckpointFog1FrontSide, Boxes.CheckpointFog1BackSide),
    )
    RunEvent(
        11010090,
        slot=1,
        args=(Objects.o1416_0000, VFX.CheckpointFog2, Boxes.CheckpointFog2FrontSide, Boxes.CheckpointFog2BackSide),
    )
    RunEvent(11010903)
    RunEvent(11015110)
    RunEvent(11015113)
    RunEvent(11015112)
    RunEvent(11015130)
    RunEvent(11010710)
    RunEvent(11010111)
    RunEvent(11010120)
    RunEvent(11010150, slot=0, args=(11010160, Boxes.LowerBurgShortcutUnlockedSide, Boxes.LowerBurgShortcutLockedSide))
    RunEvent(11010160, slot=0, args=(11010160, Objects.o1314_0000))
    RunEvent(11010170, slot=1, args=(11010171, 10010873, Objects.o1306))
    RunEvent(11010170, slot=2, args=(11010172, 10010860, Objects.o1312_01))
    RunEvent(11010180, slot=1, args=(11010181, 10010881, Objects.o1317_04))
    RunEvent(11010140, slot=0, args=(11010140, 10010881, Objects.o1310_0000, 10010883, 2021))
    RunEvent(11010190, slot=0, args=(11010190, 10010876, Objects.o1308_02, 10010883, 2017))
    RunEvent(11010190, slot=1, args=(11010191, 10010878, Objects.o1305_01, 10010883, 2019))
    RunEvent(11010190, slot=2, args=(11010192, 10010878, Objects.o1305_02, 10010883, 2019))
    RunEvent(11010101, slot=0, args=(Objects.o1308, 1, 101, 121, 7110), arg_types="iihii")
    RunEvent(11010102, slot=0, args=(11010142, Objects.o1308, 100), arg_types="iih")
    RunEvent(11015185)
    RunEvent(11010611)
    RunEvent(11010600)
    RunEvent(11010601)
    RunEvent(11015116)
    RunEvent(11010609)
    RunEvent(11010607)
    RunEvent(11010608)
    RunEvent(11010621)
    RunEvent(11010700)
    RunEvent(11015170)
    RunEvent(11010100)
    RunEvent(11010780)
    RunEvent(11010580)
    RunEvent(11010585)
    DisableSoundEvent(1013800)
    SkipLinesIfFlagOn(1, 3)
    DisableSoundEvent(1013801)
    SkipLinesIfFlagOff(6, 3)
    RunEvent(11015392)
    DisableObject(Objects.o1403_0000)
    DeleteVFX(VFX.BellGargoylesEntranceFog, erase_root_only=False)
    DisableObject(Objects.o1404_0000)
    DeleteVFX(VFX.BellGargoylesExitFog, erase_root_only=False)
    SkipLines(11)
    RunEvent(11010000)
    RunEvent(11015390)
    RunEvent(11015391)
    RunEvent(11015393)
    RunEvent(11015392)
    RunEvent(11010001)
    RunEvent(11015394)
    RunEvent(11015395)
    RunEvent(11015396)
    RunEvent(11010750, slot=0, args=(Characters.c5350_0000, 53500000))
    RunEvent(11010750, slot=1, args=(Characters.c5350_0001, 53500100))
    RunEvent(11015397, slot=0, args=(Characters.c5350_0000, 5350, 5350, Characters.c5352_0000), arg_types="ihii")
    RunEvent(11015398, slot=0, args=(Characters.c5350_0001, Characters.c5352_0001))
    DisableSoundEvent(1013802)
    SkipLinesIfFlagOff(6, 11010901)
    RunEvent(11010901)
    DisableObject(Objects.o1405_0000)
    DeleteVFX(VFX.TaurusDemonEntranceFog, erase_root_only=False)
    DisableObject(Objects.o1406_0000)
    DeleteVFX(VFX.TaurusDemonExitFog, erase_root_only=False)
    SkipLines(8)
    RunEvent(11015380)
    RunEvent(11015381)
    RunEvent(11015383)
    RunEvent(11015382)
    RunEvent(11015384)
    RunEvent(11015385)
    RunEvent(11015386)
    RunEvent(11010901)
    DisableSoundEvent(1013803)
    SkipLinesIfFlagOff(4, 11010902)
    RunEvent(11010902)
    DisableObject(Objects.o1413_0000)
    DeleteVFX(VFX.CapraDemonEntranceFog, erase_root_only=False)
    SkipLines(7)
    RunEvent(11015370)
    RunEvent(11015371)
    RunEvent(11015373)
    RunEvent(11015372)
    RunEvent(11015374)
    RunEvent(11015375)
    RunEvent(11010902)
    SkipLinesIfFlagOff(2, 11010900)
    RunEvent(11010900)
    SkipLines(29)
    RunEvent(11010899)
    RunEvent(11010900)
    RunEvent(11010782)
    RunEvent(11010783)
    RunEvent(11010790)
    RunEvent(11010791)
    RunEvent(11015301)
    RunEvent(11010784)
    RunEvent(11015302)
    RunEvent(11015303)
    RunEvent(11015304)
    RunEvent(11010851)
    RunEvent(11010852)
    RunEvent(11010890, slot=0, args=(11015320, 11015321, 11015322, 11015323, 11015324, 11015325, 11015326))
    RunEvent(11010890, slot=1, args=(11015327, 11015328, 11015329, 11015330, 11015331, 11015332, 11015333))
    RunEvent(11010890, slot=2, args=(11015334, 11015335, 11015336, 11015337, 11015338, 11015339, 11015340))
    RunEvent(11010850)
    RunEvent(11015307)
    RunEvent(11015308)
    RunEvent(11010200, slot=0, args=(10, 3000))
    RunEvent(11010200, slot=1, args=(20, 3001))
    RunEvent(11010200, slot=2, args=(30, 3002))
    RunEvent(11010200, slot=3, args=(40, 3009))
    RunEvent(11010200, slot=4, args=(50, 3010))
    RunEvent(11010200, slot=5, args=(60, 7004))
    RunEvent(11010200, slot=6, args=(70, 7005))
    RunEvent(11010200, slot=7, args=(80, 7008))
    RunEvent(11010200, slot=8, args=(90, 7009))
    RunEvent(11010200, slot=9, args=(100, 7011))
    RunEvent(11015250, slot=0, args=(Characters.c2500_0001, Characters.c2500_0001, 5.0, 0.0), arg_types="iiff")
    RunEvent(11015250, slot=1, args=(Characters.c2500_0008, Characters.c2500_0001, 5.5, 0.0), arg_types="iiff")
    RunEvent(11015250, slot=2, args=(Characters.c2500_0025, Characters.c2500_0025, 5.0, 0.0), arg_types="iiff")
    RunEvent(11015250, slot=3, args=(Characters.c2500_0026, Characters.c2500_0025, 4.0, 0.0), arg_types="iiff")
    RunEvent(11015250, slot=4, args=(Characters.c2500_0027, Characters.c2500_0025, 3.0, 0.0), arg_types="iiff")
    RunEvent(11015250, slot=5, args=(Characters.c2500_0021, Characters.c2500_0025, 3.0, 0.0), arg_types="iiff")
    RunEvent(11010130, slot=0, args=(Objects.o1316_0000, Characters.c2520_0004, Boxes.AssassinAmbush0))
    RunEvent(11010130, slot=1, args=(Objects.o1318_0000, Characters.c2520_0005, Boxes.AssassinAmbush0))
    RunEvent(11010130, slot=2, args=(Objects.o1317_0000, Characters.c2520_0006, Boxes.AssassinAmbush0))
    RunEvent(11010130, slot=3, args=(Objects.o1317_0001, Characters.c2520_0007, Boxes.AssassinAmbush1))
    RunEvent(11010130, slot=4, args=(Objects.o1317_0003, Characters.c2520_0008, Boxes.AssassinAmbush1))
    RunEvent(11010130, slot=5, args=(Objects.o1317_0002, Characters.c2520_0009, Boxes.AssassinAmbush1))
    RunEvent(11010860, slot=0, args=(Characters.c0000_0010, 0, 0))
    RunEvent(11010860, slot=1, args=(Characters.c2792_0000, 1, 27900000))
    RunEvent(11010860, slot=2, args=(Characters.c2793_0000, 1, 27900100))
    RunEvent(11010860, slot=3, args=(Characters.c2570_0000, 0, 0))
    RunEvent(11010860, slot=4, args=(Characters.c2300_0000, 0, 0))
    RunEvent(11010860, slot=5, args=(Characters.c2370_0001, 0, 0))
    RunEvent(11010860, slot=6, args=(Characters.c2550_0016, 0, 0))
    RunEvent(11010400, slot=2, args=(Objects.o0500_0004, Objects.o1155_0001))
    RunEvent(11010400, slot=3, args=(Objects.o0500_0027, Objects.o1155_0002))
    RunEvent(11010400, slot=4, args=(Objects.o0500_0034, Objects.o1154_47))
    RunEvent(11010650, slot=0, args=(Objects.o0110_0000, 11010650))
    RunEvent(11010650, slot=1, args=(Objects.o0110_0001, 11010651))
    RunEvent(11015846, slot=0, args=(11010901, Objects.o1405_0000, VFX.TaurusDemonEntranceFog))
    RunEvent(
        11015843,
        slot=0,
        args=(11010901, Objects.o1405_0000, Boxes.TaurusDemonFogPrompt, Boxes.TaurusDemonFogRotationTarget),
    )
    RunEvent(11015846, slot=1, args=(11010902, Objects.o1413_0000, VFX.CapraDemonEntranceFog))
    RunEvent(
        11015843,
        slot=1,
        args=(11010902, Objects.o1413_0000, Boxes.CapraDemonFogPrompt, Boxes.CapraDemonFogRotationTarget),
    )
    RunEvent(11015846, slot=2, args=(3, Objects.o1403_0000, VFX.BellGargoylesEntranceFog))
    RunEvent(
        11015843,
        slot=2,
        args=(3, Objects.o1403_0000, Boxes.BellGargoylesFogPrompt, Cylinders.BellGargoylesFogRotationTarget),
    )
    # <!--!>


def Preconstructor():
    """ 50: Event 50 """

    DisableCharacter(Characters.c0000_PatchesAmbush)

    RunEvent(11010583)
    HumanityRegistration(Characters.c0000_0010, 8972)
    HumanityRegistration(Characters.c0000_0004, 8310)
    HumanityRegistration(Characters.c0000_0011, 8462)
    RunEvent(11015100)
    RunEvent(11015900)
    RunEvent(11015101)
    RunEvent(11015103)
    RunEvent(11015901)
    RunEvent(11015104)
    RunEvent(11015990, slot=0, args=(11015102, Characters.c0000_0004))
    RunEvent(11015990, slot=1, args=(11015105, Characters.c0000_0011))
    RunEvent(11015203)
    HumanityRegistration(Characters.c0000_0002, 8310)
    SkipLinesIfFlagOn(4, 1007)
    SkipLinesIfFlagOn(3, 1004)
    SkipLinesIfFlagOn(2, 1001)
    SkipLinesIfFlagOn(1, 1000)
    DisableCharacter(Characters.c0000_0002)
    SkipLinesIfFlagOn(1, 11510594)
    SkipLines(1)
    Move(
        Characters.c0000_0002,
        destination=Boxes.SolaireAtSunlightAltar,
        destination_type=CoordEntityType.Region,
        set_draw_parent=1013050,
    )
    RunEvent(11010510, slot=0, args=(Characters.c0000_0002, 1004))
    RunEvent(11010520, slot=0, args=(Characters.c0000_0002, 1000, 1029, 1005))
    RunEvent(11010530, slot=0, args=(Characters.c0000_0002, 1000, 1029, 1001))
    RunEvent(11010531, slot=0, args=(Characters.c0000_0002, 1000, 1029, 1007))
    HumanityRegistration(Characters.c0000_0003, 8342)
    SkipLinesIfFlagRangeAllOff(1, (1112, 1113))
    DisableCharacter(Characters.c0000_0003)
    RunEvent(11010510, slot=1, args=(Characters.c0000_0003, 1114))
    RunEvent(11010520, slot=1, args=(Characters.c0000_0003, 1110, 1119, 1115))
    RunEvent(11010532, slot=0, args=(Characters.c0000_0003, 1110, 1119, 1111))
    HumanityRegistration(Characters.c0000_0005, 8358)
    SkipLinesIfFlagOn(1, 1175)
    DisableCharacter(Characters.c0000_0005)
    RunEvent(11010533, slot=0, args=(Characters.c0000_0005, 1170, 1189, 1175))
    RunEvent(11010501, slot=0, args=(Characters.c0000_0005, 1179))
    RunEvent(11010535, slot=0, args=(Characters.c0000_0005, 1170, 1189, 1180))
    RunEvent(11010534, slot=0, args=(Characters.c0000_0005, 1170, 1189, 1181))
    RunEvent(11010537, slot=0, args=(Characters.c0000_0005, 1170, 1189, 1177))
    RunEvent(11010538)
    RunEvent(11010539)
    RunEvent(11010582)
    RunEvent(11010510, slot=3, args=(Characters.c2640_0000, 1321))
    RunEvent(11010520, slot=3, args=(Characters.c2640_0000, 1320, 1339, 1322))
    RunEvent(11015090, slot=0, args=(1321, 1322, Objects.o1252))
    RunEvent(11010510, slot=4, args=(Characters.c2510_0000, 1401))
    RunEvent(11010520, slot=4, args=(Characters.c2510_0000, 1400, 1409, 1402))
    HumanityRegistration(Characters.c0000_0006, 8462)
    SkipLinesIfClient(1)
    DisableFlag(11010584)
    SkipLinesIfFlagOn(3, 11010584)
    SkipLinesIfFlagOn(2, 1574)
    SkipLinesIfFlagOn(1, 1570)
    DisableCharacter(Characters.c0000_0006)
    RunEvent(11010510, slot=6, args=(Characters.c0000_0006, 1574))
    RunEvent(11010520, slot=6, args=(Characters.c0000_0006, 1570, 1599, 1575))
    RunEvent(11010550, slot=0, args=(Characters.c0000_0006, 1570, 1599, 1571))
    RunEvent(11010552, slot=0, args=(Characters.c0000_0006, 1570, 1599, 1577))
    RunEvent(11010551)
    HumanityRegistration(Characters.c0000_0012, 8486)
    SkipLinesIfFlagOn(1, 11010581)
    DisableCharacter(Characters.c0000_0012)
    RunEvent(11010510, slot=7, args=(Characters.c0000_0012, 1701))
    RunEvent(11010520, slot=7, args=(Characters.c0000_0012, 1700, 1709, 1702))
    RunEvent(11010581, slot=0, args=(Characters.c0000_0012,))


def Event11010008():
    """ 11010008: Event 11010008 """
    RegisterBonfire(
        11010984,
        obj=Objects.o0200_0001,
        reaction_distance=2.0,
        reaction_angle=180.0,
        initial_kindle_level=0,
    )
    RegisterBonfire(
        11010976,
        obj=Objects.o0200_0002,
        reaction_distance=2.0,
        reaction_angle=180.0,
        initial_kindle_level=0,
    )
    RegisterBonfire(
        11010960,
        obj=Objects.o0200_0005,
        reaction_distance=2.0,
        reaction_angle=180.0,
        initial_kindle_level=0,
    )
    RegisterLadder(start_climbing_flag=11010010, stop_climbing_flag=11010011, obj=Objects.o1215)
    RegisterLadder(start_climbing_flag=11010012, stop_climbing_flag=11010013, obj=Objects.o1209)
    RegisterLadder(start_climbing_flag=11010014, stop_climbing_flag=11010015, obj=Objects.o1210_1000)
    RegisterLadder(start_climbing_flag=11010016, stop_climbing_flag=11010017, obj=Objects.o1211_1000)
    RegisterLadder(start_climbing_flag=11010018, stop_climbing_flag=11010019, obj=Objects.o1212_1000)
    RegisterLadder(start_climbing_flag=11010020, stop_climbing_flag=11010021, obj=Objects.o1213_1000)
    RegisterLadder(start_climbing_flag=11010022, stop_climbing_flag=11010023, obj=Objects.o1214_1000)
    RegisterLadder(start_climbing_flag=11010024, stop_climbing_flag=11010025, obj=Objects.o1219)
    RegisterLadder(start_climbing_flag=11010026, stop_climbing_flag=11010027, obj=Objects.o1207)
    RegisterLadder(start_climbing_flag=11010030, stop_climbing_flag=11010031, obj=Objects.o1216_1000)
    RegisterLadder(start_climbing_flag=11010032, stop_climbing_flag=11010033, obj=Objects.o1206)
    RegisterLadder(start_climbing_flag=11010034, stop_climbing_flag=11010035, obj=Objects.o1218_0000)
    CreateHazard(
        11010300,
        Objects.o1110,
        model_point=200,
        behavior_param_id=5000,
        target_type=DamageTargetType.Character,
        radius=1.2000000476837158,
        life=0.0,
        repetition_time=1.0,
    )
    CreateHazard(
        11010308,
        Objects.o1111_07,
        model_point=100,
        behavior_param_id=5000,
        target_type=DamageTargetType.Character,
        radius=0.699999988079071,
        life=0.0,
        repetition_time=1.0,
    )
    CreateHazard(
        11010309,
        Objects.o1111_08,
        model_point=100,
        behavior_param_id=5000,
        target_type=DamageTargetType.Character,
        radius=0.699999988079071,
        life=0.0,
        repetition_time=1.0,
    )


def Event11010090(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11010090: Event 11010090 """
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


@RestartOnRest
def Event11010000():
    """ 11010000: Event 11010000 """
    SkipLinesIfThisEventOff(2)
    DisableCharacter(Characters.c5350_0002)
    End()
    DisableAI(Characters.c5350_0002)
    SetStandbyAnimationSettings(Characters.c5350_0002, standby_animation=7000)
    EnableInvincibility(Characters.c5350_0002)
    DisableHealthBar(Characters.c5350_0002)
    DisableCharacter(Characters.c5350_0000)
    IfFlagOn(1, 11015390)
    IfHost(1)
    IfCharacterInsideRegion(1, PLAYER, region=Cylinders.BellGargoylesCutsceneTrigger)
    IfConditionTrue(0, input_condition=1)
    IfCharacterType(-1, PLAYER, CharacterType.BlackPhantom)
    IfCharacterType(-1, PLAYER, CharacterType.Intruder)
    EndIfConditionTrue(-1)
    SkipLinesIfMultiplayer(2)
    PlayCutscene(100110, skippable=True, fade_out=False, player_id=PLAYER)
    SkipLines(1)
    PlayCutscene(100110, skippable=False, fade_out=False, player_id=PLAYER)
    WaitFrames(1)
    DisableCharacter(Characters.c5350_0002)
    EnableCharacter(Characters.c5350_0000)


def Event11015390():
    """ 11015390: Event 11015390 """
    IfFlagOff(1, 3)
    IfActionButton(
        1,
        prompt_text=10010403,
        anchor_entity=Boxes.BellGargoylesFogPrompt,
        anchor_type=CoordEntityType.Region,
        line_intersects=Objects.o1403_0000,
        boss_version=True,
    )
    IfConditionTrue(0, input_condition=1)
    RotateToFaceEntity(PLAYER, Cylinders.BellGargoylesFogRotationTarget)
    ForceAnimation(PLAYER, 7410)
    Restart()


def Event11015391():
    """ 11015391: Event 11015391 """
    IfFlagOff(1, 3)
    IfFlagOn(1, 11015393)
    IfCharacterType(1, PLAYER, CharacterType.WhitePhantom)
    IfActionButton(
        1,
        prompt_text=10010403,
        anchor_entity=Boxes.BellGargoylesFogPrompt,
        anchor_type=CoordEntityType.Region,
        trigger_attribute=TriggerAttribute.All,
        line_intersects=Objects.o1403_0000,
    )
    IfConditionTrue(0, input_condition=1)
    RotateToFaceEntity(PLAYER, Cylinders.BellGargoylesFogRotationTarget)
    ForceAnimation(PLAYER, 7410)
    Restart()


def Event11015393():
    """ 11015393: Event 11015393 """
    SkipLinesIfThisEventOn(3)
    IfFlagOff(1, 3)
    IfCharacterInsideRegion(1, PLAYER, region=Boxes.BellGargoylesCombatStart)
    IfConditionTrue(0, input_condition=1)
    SkipLinesIfClient(1)
    NotifyBossBattleStart()
    ActivateMultiplayerBuffs(Characters.c5350_0000)


@RestartOnRest
def Event11015392():
    """ 11015392: Event 11015392 """
    SkipLinesIfFlagOff(11, 3)
    DisableCharacter(Characters.c5350_0000)
    DisableCharacter(Characters.c5350_0001)
    DisableCharacter(Characters.c5350_0002)
    DisableCharacter(Characters.c5352_0000)
    DisableCharacter(Characters.c5352_0001)
    Kill(Characters.c5350_0000, award_souls=False)
    Kill(Characters.c5350_0001, award_souls=False)
    Kill(Characters.c5350_0002, award_souls=False)
    Kill(Characters.c5352_0000, award_souls=False)
    Kill(Characters.c5352_0001, award_souls=False)
    End()
    DisableAI(Characters.c5350_0000)
    IfFlagOn(1, 11010000)
    IfFlagOn(1, 11015393)
    IfCharacterInsideRegion(1, PLAYER, region=Boxes.BellGargoylesMusic)
    IfConditionTrue(0, input_condition=1)
    EnableAI(Characters.c5350_0000)
    EnableBossHealthBar(Characters.c5350_0000, name=5350, slot=0)


def Event11010001():
    """ 11010001: Event 11010001 """
    IfCharacterDead(1, Characters.c5350_0000)
    IfCharacterDead(2, Characters.c5350_0001)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    IfCharacterDead(3, Characters.c5350_0000)
    IfCharacterDead(3, Characters.c5350_0001)
    IfConditionTrue(0, input_condition=3)
    EnableFlag(3)
    SkipLinesIfFinishedConditionTrue(2, 1)
    PlaySoundEffect(anchor_entity=Characters.c5350_0000, sound_type=SoundType.s_SFX, sound_id=777777777)
    SkipLines(1)
    PlaySoundEffect(anchor_entity=Characters.c5350_0001, sound_type=SoundType.s_SFX, sound_id=777777777)
    KillBoss(1010800)
    DisableObject(Objects.o1403_0000)
    DeleteVFX(VFX.BellGargoylesEntranceFog, erase_root_only=True)
    DisableObject(Objects.o1404_0000)
    DeleteVFX(VFX.BellGargoylesExitFog, erase_root_only=True)


def Event11015394():
    """ 11015394: Event 11015394 """
    DisableNetworkSync()
    IfFlagOff(1, 3)
    IfFlagOn(1, 11010000)
    IfFlagOn(1, 11015392)
    SkipLinesIfHost(1)
    IfFlagOn(1, 11015391)
    IfCharacterInsideRegion(1, PLAYER, region=Boxes.BellGargoylesMusic)
    IfConditionTrue(0, input_condition=1)
    DisableSoundEvent(1013801)
    EnableSoundEvent(1013800)


def Event11015395():
    """ 11015395: Event 11015395 """
    DisableNetworkSync()
    IfFlagOn(1, 11015394)
    IfFlagOn(1, 3)
    IfConditionTrue(0, input_condition=1)
    DisableSoundEvent(1013800)
    EnableSoundEvent(1013801)


@RestartOnRest
def Event11015396():
    """ 11015396: Event 11015396 """
    EndIfFlagOn(3)
    DisableAI(Characters.c5350_0001)
    SetStandbyAnimationSettings(Characters.c5350_0001, standby_animation=7000)
    EnableInvincibility(Characters.c5350_0001)
    DisableHealthBar(Characters.c5350_0001)
    IfHealthLessThanOrEqual(0, Characters.c5350_0000, 0.6000000238418579)
    ResetStandbyAnimationSettings(Characters.c5350_0001)
    Move(
        Characters.c5350_0001,
        destination=Boxes.SecondBellGargoyleSpawn,
        destination_type=CoordEntityType.Region,
        short_move=True,
    )
    ForceAnimation(Characters.c5350_0001, 7001, wait_for_completion=True)
    DisableInvincibility(Characters.c5350_0001)
    EnableAI(Characters.c5350_0001)
    EnableBossHealthBar(Characters.c5350_0001, name=5350, slot=1)


@RestartOnRest
def Event11015397(_, arg_0_3: int, arg_4_5: short, arg_8_11: int, arg_12_15: int):
    """ 11015397: Event 11015397 """
    DisableCharacter(arg_12_15)
    SkipLinesIfThisEventSlotOff(5)
    SetDisplayMask(arg_0_3, bit_index=0, switch_type=OnOffChange.On)
    SetCollisionMask(arg_0_3, bit_index=1, switch_type=OnOffChange.Off)
    AddSpecialEffect(arg_0_3, 5434)
    AICommand(arg_0_3, command_id=20, slot=0)
    End()
    IfFlagOn(1, 11015392)
    IfCharacterBackreadEnabled(1, arg_0_3)
    IfConditionTrue(0, input_condition=1)
    CreateNPCPart(
        arg_0_3,
        npc_part_id=arg_4_5,
        part_index=NPCPartType.Part1,
        part_health=65,
        damage_correction=1.0,
        body_damage_correction=1.0,
        is_invincible=False,
        start_in_stop_state=False,
    )
    IfCharacterPartHealthLessThanOrEqual(2, arg_0_3, npc_part_id=arg_8_11, value=0)
    IfHealthLessThanOrEqual(3, arg_0_3, 0.0)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(3)
    Move(
        arg_12_15,
        destination=arg_0_3,
        destination_type=CoordEntityType.Character,
        model_point=130,
        copy_draw_parent=arg_0_3,
    )
    EnableCharacter(arg_12_15)
    ResetAnimation(arg_0_3, disable_interpolation=False)
    ForceAnimation(arg_0_3, 8000)
    ForceAnimation(arg_12_15, 8100)
    SetDisplayMask(arg_0_3, bit_index=0, switch_type=OnOffChange.On)
    SetCollisionMask(arg_0_3, bit_index=1, switch_type=OnOffChange.Off)
    AddSpecialEffect(arg_0_3, 5434)
    AICommand(arg_0_3, command_id=20, slot=0)
    ReplanAI(arg_0_3)
    IfCharacterHuman(-7, PLAYER)
    IfCharacterHollow(-7, PLAYER)
    EndIfConditionFalse(-7)
    AwardItemLot(53520000, host_only=True)


@RestartOnRest
def Event11015398(_, arg_0_3: int, arg_4_7: int):
    """ 11015398: Event 11015398 """
    DisableCharacter(arg_4_7)
    IfCharacterBackreadEnabled(0, arg_0_3)
    SetCollisionMask(arg_0_3, bit_index=1, switch_type=OnOffChange.Off)
    SetCollisionMask(arg_0_3, bit_index=2, switch_type=OnOffChange.Off)


def Event11010750(_, arg_0_3: int, arg_4_7: int):
    """ 11010750: Event 11010750 """
    IfFlagOff(1, 3)
    IfCharacterAlive(1, arg_0_3)
    IfConditionTrue(0, input_condition=1)
    IfCharacterDead(0, arg_0_3)
    IfCharacterHuman(-7, PLAYER)
    IfCharacterHollow(-7, PLAYER)
    EndIfConditionFalse(-7)
    AwardItemLot(arg_4_7, host_only=True)


def Event11015380():
    """ 11015380: Event 11015380 """
    IfFlagOff(1, 11010901)
    IfActionButton(
        1,
        prompt_text=10010403,
        anchor_entity=Boxes.TaurusDemonFogPrompt,
        anchor_type=CoordEntityType.Region,
        line_intersects=Objects.o1405_0000,
        boss_version=True,
    )
    IfConditionTrue(0, input_condition=1)
    RotateToFaceEntity(PLAYER, Boxes.TaurusDemonFogRotationTarget)
    ForceAnimation(PLAYER, 7410)
    Restart()


def Event11015381():
    """ 11015381: Event 11015381 """
    IfFlagOff(1, 11010901)
    IfFlagOn(1, 11015383)
    IfCharacterType(1, PLAYER, CharacterType.WhitePhantom)
    IfActionButton(
        1,
        prompt_text=10010403,
        anchor_entity=Boxes.TaurusDemonFogPrompt,
        anchor_type=CoordEntityType.Region,
        trigger_attribute=TriggerAttribute.All,
        line_intersects=Objects.o1405_0000,
    )
    IfConditionTrue(0, input_condition=1)
    RotateToFaceEntity(PLAYER, Boxes.TaurusDemonFogRotationTarget)
    ForceAnimation(PLAYER, 7410)
    Restart()


def Event11015383():
    """ 11015383: Event 11015383 """
    SkipLinesIfThisEventOn(3)
    IfFlagOff(1, 11010901)
    IfCharacterInsideRegion(1, PLAYER, region=Boxes.TaurusDemonCombatStart)
    IfConditionTrue(0, input_condition=1)
    SkipLinesIfClient(2)
    NotifyBossBattleStart()
    SetNetworkUpdateAuthority(Characters.c2250_0000, UpdateAuthority.Forced)
    ActivateMultiplayerBuffs(Characters.c2250_0000)


@RestartOnRest
def Event11015382():
    """ 11015382: Event 11015382 """
    SkipLinesIfThisEventOff(2)
    ResetStandbyAnimationSettings(Characters.c2250_0000)
    End()
    DisableAI(Characters.c2250_0000)
    SetStandbyAnimationSettings(Characters.c2250_0000, standby_animation=9001)
    DisableHealthBar(Characters.c2250_0000)
    IfAttacked(1, Characters.c2250_0000, attacker=PLAYER)
    IfHost(2)
    IfCharacterInsideRegion(2, PLAYER, region=Boxes.TaurusDemonTrigger)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EnableFlag(11010005)
    ResetStandbyAnimationSettings(Characters.c2250_0000)
    ForceAnimation(Characters.c2250_0000, 9061, wait_for_completion=True)
    EnableAI(Characters.c2250_0000)


def Event11015384():
    """ 11015384: Event 11015384 """
    DisableNetworkSync()
    IfFlagOff(1, 11010901)
    IfFlagOn(1, 11015382)
    SkipLinesIfHost(1)
    IfFlagOn(1, 11015381)
    IfCharacterInsideRegion(1, PLAYER, region=Boxes.TaurusDemonMusic)
    IfConditionTrue(0, input_condition=1)
    EnableBossHealthBar(Characters.c2250_0000, name=2250, slot=0)
    EnableSoundEvent(1013802)


def Event11015385():
    """ 11015385: Event 11015385 """
    DisableNetworkSync()
    IfFlagOn(1, 11015384)
    IfFlagOn(1, 11010901)
    IfConditionTrue(0, input_condition=1)
    DisableBossHealthBar(Characters.c2250_0000, name=2250, slot=0)
    DisableSoundEvent(1013802)


def Event11015386():
    """ 11015386: Event 11015386 """
    EndIfClient()
    IfHasTAEEvent(1, Characters.c2250_0000, tae_event_id=700)
    IfHasTAEEvent(2, Characters.c2250_0000, tae_event_id=710)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionTrue(2, 2)
    Move(
        Characters.c2250_0000,
        destination=Boxes.TaurusDemonJumpUpSnap,
        destination_type=CoordEntityType.Region,
        short_move=True,
    )
    SkipLines(1)
    Move(
        Characters.c2250_0000,
        destination=Boxes.TaurusDemonJumpDownSnap,
        destination_type=CoordEntityType.Region,
        short_move=True,
    )
    Restart()


@RestartOnRest
def Event11010901():
    """ 11010901: Event 11010901 """
    SkipLinesIfThisEventOff(3)
    DisableCharacter(Characters.c2250_0000)
    Kill(Characters.c2250_0000, award_souls=False)
    End()
    IfHealthLessThanOrEqual(0, Characters.c2250_0000, 0.0)
    Wait(1.0)
    PlaySoundEffect(anchor_entity=Characters.c2250_0000, sound_type=SoundType.s_SFX, sound_id=777777777)
    IfCharacterDead(0, Characters.c2250_0000)
    EnableFlag(11010901)
    KillBoss(1010700)
    DisableObject(Objects.o1405_0000)
    DeleteVFX(VFX.TaurusDemonEntranceFog, erase_root_only=True)
    DisableObject(Objects.o1406_0000)
    DeleteVFX(VFX.TaurusDemonExitFog, erase_root_only=True)


def Event11015370():
    """ 11015370: Event 11015370 """
    IfFlagOff(1, 11010902)
    IfActionButton(
        1,
        prompt_text=10010403,
        anchor_entity=Boxes.CapraDemonFogPrompt,
        anchor_type=CoordEntityType.Region,
        line_intersects=Objects.o1413_0000,
        boss_version=True,
    )
    IfConditionTrue(0, input_condition=1)
    RotateToFaceEntity(PLAYER, Boxes.CapraDemonFogRotationTarget)
    ForceAnimation(PLAYER, 7410, wait_for_completion=True)
    Restart()


def Event11015371():
    """ 11015371: Event 11015371 """
    IfFlagOff(1, 11010902)
    IfFlagOn(1, 11015373)
    IfCharacterType(1, PLAYER, CharacterType.WhitePhantom)
    IfActionButton(
        1,
        prompt_text=10010403,
        anchor_entity=Boxes.CapraDemonFogPrompt,
        anchor_type=CoordEntityType.Region,
        trigger_attribute=TriggerAttribute.All,
        line_intersects=Objects.o1413_0000,
    )
    IfConditionTrue(0, input_condition=1)
    RotateToFaceEntity(PLAYER, Boxes.CapraDemonFogRotationTarget)
    ForceAnimation(PLAYER, 7410)
    Restart()


def Event11015373():
    """ 11015373: Event 11015373 """
    SkipLinesIfThisEventOn(3)
    IfFlagOff(1, 11010902)
    IfCharacterInsideRegion(1, PLAYER, region=Boxes.CapraDemonCombatStart)
    IfConditionTrue(0, input_condition=1)
    SkipLinesIfClient(1)
    NotifyBossBattleStart()
    ActivateMultiplayerBuffs(Characters.c2240_0000)
    EnableFlag(11010597)


@RestartOnRest
def Event11015372():
    """ 11015372: Event 11015372 """
    SkipLinesIfThisEventOn(5)
    DisableAI(Characters.c2240_0000)
    IfFlagOn(1, 11015373)
    IfCharacterInsideRegion(1, PLAYER, region=Boxes.CapraDemonMusic)
    IfConditionTrue(0, input_condition=1)
    EnableAI(Characters.c2240_0000)
    EnableBossHealthBar(Characters.c2240_0000, name=2240, slot=0)


def Event11015374():
    """ 11015374: Event 11015374 """
    DisableNetworkSync()
    IfFlagOff(1, 11010902)
    IfFlagOn(1, 11015372)
    SkipLinesIfHost(1)
    IfFlagOn(1, 11015371)
    IfCharacterInsideRegion(1, PLAYER, region=Boxes.CapraDemonMusic)
    IfConditionTrue(0, input_condition=1)
    EnableSoundEvent(1013803)


def Event11015375():
    """ 11015375: Event 11015375 """
    DisableNetworkSync()
    IfFlagOn(1, 11015374)
    IfFlagOn(1, 11010902)
    IfConditionTrue(0, input_condition=1)
    DisableSoundEvent(1013803)


@RestartOnRest
def Event11010902():
    """ 11010902: Event 11010902 """
    SkipLinesIfThisEventOff(7)
    DisableCharacter(Characters.c2240_0000)
    DisableCharacter(Characters.c3340_0003)
    DisableCharacter(Characters.c3340_0004)
    Kill(Characters.c2240_0000, award_souls=False)
    Kill(Characters.c3340_0003, award_souls=False)
    Kill(Characters.c3340_0004, award_souls=False)
    End()
    DisableCharacter(Characters.c3340_0007)
    DisableCharacter(Characters.c3340_0008)
    Kill(Characters.c3340_0007, award_souls=False)
    Kill(Characters.c3340_0008, award_souls=False)
    IfHealthLessThanOrEqual(0, Characters.c2240_0000, 0.0)
    Wait(1.0)
    PlaySoundEffect(anchor_entity=Characters.c2240_0000, sound_type=SoundType.s_SFX, sound_id=777777777)
    IfCharacterDead(0, Characters.c2240_0000)
    EnableFlag(11010902)
    KillBoss(1010750)
    DisableObject(Objects.o1413_0000)
    DeleteVFX(VFX.CapraDemonEntranceFog, erase_root_only=True)


@RestartOnRest
def Event11010903():
    """ 11010903: Event 11010903 """
    SkipLinesIfThisEventOff(2)
    DisableCharacter(Characters.c3460_0000)
    End()
    IfCharacterDead(0, Characters.c3460_0000)
    EnableFlag(11010903)


@RestartOnRest
def Event11015110():
    """ 11015110: Event 11015110 """
    SkipLinesIfThisEventOff(2)
    PostDestruction(Objects.o1132_16)
    End()
    DisableAI(Characters.c2540_0007)
    IfEntityWithinDistance(1, PLAYER, Characters.c2540_0007, radius=5.0)
    IfObjectDestroyed(2, Objects.o1132_16)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionTrue(1, 2)
    ForceAnimation(Characters.c2540_0007, 3000, wait_for_completion=True)
    EnableAI(Characters.c2540_0007)


@RestartOnRest
def Event11015111():
    """ 11015111: Event 11015111 """
    EndIfThisEventOn()
    DisableAI(1010110)
    IfCharacterInsideRegion(1, PLAYER, region=Boxes.WarriorAmbushTrigger)
    IfAttacked(2, 1010110, attacker=PLAYER)
    IfEntityWithinDistance(3, 1010110, PLAYER, radius=2.0)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionFalse(1, 1)
    ForceAnimation(1010110, 13005, wait_for_completion=True)
    EnableAI(1010110)


@RestartOnRest
def Event11015113():
    """ 11015113: Event 11015113 """
    EndIfThisEventOn()
    DisableAI(Characters.c2550_0042)
    IfCharacterInsideRegion(-1, PLAYER, region=Boxes.TowerArcherTrigger)
    IfAttacked(-1, Characters.c2550_0042, attacker=PLAYER)
    IfEntityWithinDistance(-1, Characters.c2550_0042, PLAYER, radius=5.0)
    IfConditionTrue(0, input_condition=-1)
    EnableAI(Characters.c2550_0042)


@RestartOnRest
def Event11015112():
    """ 11015112: Event 11015112 """
    EndIfThisEventOn()
    DisableAI(Characters.c2500_0006)
    IfAttacked(-3, Characters.c2500_0006, attacker=PLAYER)
    IfCharacterInsideRegion(-3, PLAYER, region=Boxes.FleeingHollowCombatTrigger)
    IfConditionTrue(1, input_condition=-3)
    IfCharacterInsideRegion(2, PLAYER, region=Boxes.FleeingHollowFleeTrigger)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EnableAI(Characters.c2500_0006)
    EndIfFinishedConditionTrue(1)
    SetNest(Characters.c2500_0006, Boxes.FleeingHollowNest)
    AICommand(Characters.c2500_0006, command_id=10, slot=0)
    ReplanAI(Characters.c2500_0006)
    IfCharacterInsideRegion(-2, PLAYER, region=Boxes.FleeingHollowCombatTrigger)
    IfAttacked(-2, Characters.c2500_0006, attacker=PLAYER)
    IfConditionTrue(0, input_condition=-2)
    AICommand(Characters.c2500_0006, command_id=-1, slot=0)
    ReplanAI(Characters.c2500_0006)


@RestartOnRest
def Event11015130():
    """ 11015130: Event 11015130 """
    DisableCharacter(Characters.c3300_0000)
    EndIfFlagOn(11010710)
    IfObjectDestroyed(0, Objects.o1154_31)
    EnableCharacter(Characters.c3300_0000)
    SkipLinesIfFlagOn(4, 11015130)
    ForceAnimation(Characters.c3300_0000, 500, wait_for_completion=True)
    ForceAnimation(Characters.c3300_0000, 500, wait_for_completion=True)
    ForceAnimation(Characters.c3300_0000, 500, wait_for_completion=True)
    ForceAnimation(Characters.c3300_0000, 500, wait_for_completion=True)
    SetNest(Characters.c3300_0000, Cylinders.CrystalLizardNest)
    AICommand(Characters.c3300_0000, command_id=10, slot=0)
    ReplanAI(Characters.c3300_0000)
    EnableFlag(11015130)
    IfCharacterInsideRegion(0, Characters.c3300_0000, region=Cylinders.CrystalLizardNest)
    AICommand(Characters.c3300_0000, command_id=-1, slot=0)
    ReplanAI(Characters.c3300_0000)


@RestartOnRest
def Event11010710():
    """ 11010710: Event 11010710 """
    DisableCharacter(Characters.c3300_0000)
    EndIfFlagOn(11010710)
    IfCharacterDead(0, Characters.c3300_0000)
    IfCharacterHuman(-7, PLAYER)
    IfCharacterHollow(-7, PLAYER)
    EndIfConditionFalse(-7)
    AwardItemLot(33006000, host_only=True)


@RestartOnRest
def Event11010111():
    """ 11010111: Event 11010111 """
    EndIfThisEventOn()
    DisableAI(Characters.c2550_0010)
    IfAttacked(1, Characters.c2550_0010, attacker=PLAYER)
    IfCharacterInsideRegion(2, PLAYER, region=Boxes.HollowDoorKickTrigger)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EnableFlag(11010111)
    EnableAI(Characters.c2550_0010)
    EndIfFinishedConditionTrue(1)
    DisableObjectActivation(Objects.o1318_01, obj_act_id=-1, relative_index=0)
    DisableObjectActivation(Objects.o1318_01, obj_act_id=-1, relative_index=1)
    DisableObjectActivation(Objects.o1318_01, obj_act_id=-1, relative_index=2)
    DisableObjectActivation(Objects.o1318_01, obj_act_id=-1, relative_index=3)
    Move(
        Characters.c2550_0010,
        destination=Boxes.HollowDoorKickSnap,
        destination_type=CoordEntityType.Region,
        short_move=True,
    )
    ForceAnimation(Characters.c2550_0010, 7000)
    Wait(0.20000000298023224)
    ForceAnimation(Objects.o1318_01, 2, wait_for_completion=True)
    EnableFlag(61010518)
    DisableNetworkSync()
    Wait(4.0)
    DisableObjectActivation(Objects.o1318_01, obj_act_id=1318, relative_index=0)
    DisableObjectActivation(Objects.o1318_01, obj_act_id=1318, relative_index=1)
    EnableObjectActivation(Objects.o1318_01, obj_act_id=1318, relative_index=2)
    EnableObjectActivation(Objects.o1318_01, obj_act_id=1318, relative_index=3)


@RestartOnRest
def Event11010120():
    """ 11010120: Event 11010120 """
    SkipLinesIfThisEventOff(2)
    EndOfAnimation(Objects.o1330_0000, 0)
    End()
    DisableAI(Characters.c2550_0020)
    IfAttacked(-1, Characters.c2550_0020, attacker=PLAYER)
    IfCharacterInsideRegion(-1, PLAYER, region=Boxes.BurningBarrelTrigger)
    IfConditionTrue(0, input_condition=-1)
    DisableNetworkSync()
    ResetAnimation(Characters.c2550_0020, disable_interpolation=False)
    ForceAnimation(Characters.c2550_0020, 3006)
    Wait(0.5)
    CreateObjectVFX(100100, obj=Objects.o1330_0000, model_point=1)
    ForceAnimation(Objects.o1330_0000, 0)
    Wait(0.5)
    EnableAI(Characters.c2550_0020)
    CreateHazard(
        11010121,
        Objects.o1330_0000,
        model_point=1,
        behavior_param_id=5020,
        target_type=DamageTargetType.Character,
        radius=0.6000000238418579,
        life=3.0,
        repetition_time=0.0,
    )
    Wait(3.0)
    DeleteObjectVFX(Objects.o1330_0000, erase_root=True)


def Event11010101(_, arg_0_3: int, arg_4_7: int, arg_8_9: short, arg_12_15: int, arg_16_19: int):
    """ 11010101: Event 11010101 """
    SkipLinesIfThisEventSlotOff(2)
    EndOfAnimation(arg_0_3, arg_4_7)
    End()
    IfActionButton(
        0,
        prompt_text=10010400,
        anchor_entity=arg_0_3,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        model_point=arg_8_9,
        trigger_attribute=TriggerAttribute.All,
    )
    Move(PLAYER, destination=arg_0_3, destination_type=CoordEntityType.Object, model_point=arg_12_15, short_move=True)
    ForceAnimation(PLAYER, arg_16_19)
    ForceAnimation(arg_0_3, arg_4_7)


def Event11010102(_, arg_0_3: int, arg_4_7: int, arg_8_9: short):
    """ 11010102: Event 11010102 """
    DisableNetworkSync()
    IfFlagOn(-1, arg_0_3)
    IfActionButton(
        -1,
        prompt_text=10010400,
        anchor_entity=arg_4_7,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        model_point=arg_8_9,
        trigger_attribute=TriggerAttribute.All,
    )
    IfConditionTrue(0, input_condition=-1)
    EndIfFlagOn(arg_0_3)
    DisplayDialog(
        10010161,
        anchor_entity=arg_4_7,
        display_distance=3.0,
        button_type=ButtonType.Yes_or_No,
        number_buttons=NumberButtons.NoButton,
    )
    Restart()


@RestartOnRest
def Event11010125():
    """ 11010125: Event 11010125 """
    EndIfThisEventOn()
    DisableCharacter(1010104)
    Move(
        1010104,
        destination=Boxes.UnusedUndeadAssassinAmbush,
        destination_type=CoordEntityType.Region,
        short_move=True,
    )
    IfThisEventOn(0)
    EnableCharacter(1010104)


@RestartOnRest
def Event11010126():
    """ 11010126: Event 11010126 """
    EndIfThisEventOn()
    IfFlagOn(0, 51010030)
    EnableFlag(11010125)


@RestartOnRest
def Event11010130(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 11010130: Event 11010130 """
    SkipLinesIfThisEventSlotOff(2)
    EndOfAnimation(arg_0_3, 2)
    End()
    DisableAI(arg_4_7)
    IfCharacterInsideRegion(0, PLAYER, region=arg_8_11)
    WaitRandomSeconds(min_seconds=0.0, max_seconds=1.0)
    ForceAnimation(arg_4_7, 7001)
    EnableAI(arg_4_7)
    Wait(0.10000000149011612)
    ForceAnimation(arg_0_3, 2)


def Event11010150(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 11010150: Event 11010150 """
    DisableNetworkSync()
    SkipLinesIfFlagOn(4, arg_0_3)
    IfCharacterInsideRegion(0, PLAYER, region=arg_4_7)
    AddSpecialEffect(PLAYER, 4150)
    Wait(3.0)
    Restart()
    IfCharacterInsideRegion(-1, PLAYER, region=arg_4_7)
    IfCharacterInsideRegion(-1, PLAYER, region=arg_8_11)
    IfConditionTrue(0, input_condition=-1)
    AddSpecialEffect(PLAYER, 4150)
    Wait(3.0)
    Restart()


def Event11010160(_, arg_0_3: int, arg_4_7: int):
    """ 11010160: Event 11010160 """
    SkipLinesIfThisEventSlotOff(5)
    DisableObjectActivation(arg_4_7, obj_act_id=-1, relative_index=0)
    DisableObjectActivation(arg_4_7, obj_act_id=-1, relative_index=1)
    DisableObjectActivation(arg_4_7, obj_act_id=-1, relative_index=2)
    DisableObjectActivation(arg_4_7, obj_act_id=-1, relative_index=3)
    End()
    IfObjectActivated(0, obj_act_id=arg_0_3)
    EnableFlag(arg_0_3)
    Wait(2.0)
    DisableObjectActivation(arg_4_7, obj_act_id=-1, relative_index=0)
    DisableObjectActivation(arg_4_7, obj_act_id=-1, relative_index=1)
    DisableObjectActivation(arg_4_7, obj_act_id=-1, relative_index=2)
    DisableObjectActivation(arg_4_7, obj_act_id=-1, relative_index=3)


def Event11010180(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 11010180: Event 11010180 """
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


def Event11010170(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 11010170: Event 11010170 """
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
    Wait(2.0)
    DisableObjectActivation(arg_8_11, obj_act_id=-1, relative_index=0)
    DisableObjectActivation(arg_8_11, obj_act_id=-1, relative_index=1)
    DisableObjectActivation(arg_8_11, obj_act_id=-1, relative_index=2)
    DisableObjectActivation(arg_8_11, obj_act_id=-1, relative_index=3)


def Event11010140(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int):
    """ 11010140: Event 11010140 """
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


def Event11010190(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int):
    """ 11010190: Event 11010190 """
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
    Wait(2.0)
    DisableObjectActivation(arg_8_11, obj_act_id=-1, relative_index=0)
    DisableObjectActivation(arg_8_11, obj_act_id=-1, relative_index=1)
    DisableObjectActivation(arg_8_11, obj_act_id=-1, relative_index=2)
    DisableObjectActivation(arg_8_11, obj_act_id=-1, relative_index=3)


def Event11010100():
    """ 11010100: Event 11010100 """
    SkipLinesIfThisEventOff(3)
    EndOfAnimation(Objects.o1208, 0)
    RegisterLadder(start_climbing_flag=11010028, stop_climbing_flag=11010029, obj=Objects.o1208)
    End()
    IfActionButton(
        0,
        prompt_text=10010500,
        anchor_entity=Objects.o1208,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        model_point=194,
        trigger_attribute=TriggerAttribute.All,
    )
    EnableFlag(11010100)
    Move(PLAYER, destination=Objects.o1208, destination_type=CoordEntityType.Object, model_point=192, short_move=True)
    ForceAnimation(PLAYER, 8005)
    Wait(0.5)
    ForceAnimation(Objects.o1208, 0, wait_for_completion=True)
    RegisterLadder(start_climbing_flag=11010028, stop_climbing_flag=11010029, obj=Objects.o1208)


def Event11010400(_, arg_0_3: int, arg_4_7: int):
    """ 11010400: Event 11010400 """
    SkipLinesIfThisEventSlotOff(3)
    EndOfAnimation(arg_0_3, 101)
    EnableTreasure(arg_0_3)
    End()
    DisableTreasure(arg_0_3)
    ForceAnimation(arg_0_3, 100, loop=True)
    IfObjectDestroyed(0, arg_4_7)
    ForceAnimation(arg_0_3, 101, wait_for_completion=True)
    EnableTreasure(arg_0_3)


@RestartOnRest
def Event11015250(_, arg_0_3: int, arg_4_7: int, arg_8_11: float, arg_12_15: float):
    """ 11015250: Event 11015250 """
    SkipLinesIfThisEventSlotOff(2)
    ResetStandbyAnimationSettings(arg_0_3)
    End()
    DisableCharacterCollision(arg_0_3)
    IfEntityWithinDistance(0, PLAYER, arg_4_7, radius=arg_8_11)
    DisableNetworkSync()
    Wait(arg_12_15)
    EnableCharacterCollision(arg_0_3)
    SetStandbyAnimationSettings(arg_0_3, cancel_animation=9060)


def Event11015185():
    """ 11015185: Event 11015185 """
    IfFlagOn(1, 61010610)
    IfObjectActivated(1, obj_act_id=11010600)
    IfFlagOff(2, 61010610)
    IfObjectActivated(2, obj_act_id=11010600)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EnableFlag(11015180)
    SkipLinesIfFinishedConditionTrue(2, 2)
    EnableFlag(11015181)
    Restart()
    EnableFlag(11015182)
    Restart()


def Event11010611():
    """ 11010611: Event 11010611 """
    DisableNetworkSync()
    IfFramesElapsed(1, 10)
    IfInsideMap(1, game_map=UNDEAD_BURG)
    IfConditionTrue(0, input_condition=1)
    EnableObjectActivation(Objects.o1200_1000, obj_act_id=-1)


def Event11010600():
    """ 11010600: Event 11010600 """
    IfFlagOn(1, 11015181)
    IfHost(1)
    IfFlagOn(2, 11015182)
    IfHost(2)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    DisableFlag(11015180)
    DisableFlag(11015181)
    DisableFlag(11015182)
    SkipLinesIfFinishedConditionTrue(9, 2)
    SkipLinesIfFlagOn(2, 61010610)
    RunEvent(11010611)
    Restart()
    EnableNavmeshType(Navigation.Navmesh_GateLever, NavmeshType.Solid)
    EnableFlag(11010605)
    ForceAnimation(Objects.o1201_1000, 2)
    WaitFrames(60)
    RunEvent(11010611)
    Restart()
    SkipLinesIfFlagOff(2, 61010610)
    RunEvent(11010611)
    Restart()
    DisableNavmeshType(Navigation.Navmesh_GateLever, NavmeshType.Solid)
    ForceAnimation(Objects.o1201_1000, 4)
    WaitFrames(200)
    RunEvent(11010611)
    Restart()


def Event11010601():
    """ 11010601: Event 11010601 """
    IfFlagOn(0, 11010605)
    DisableFlag(11010605)
    Wait(0.5)
    CreateHazard(
        11010602,
        Objects.o1201_1000,
        model_point=42,
        behavior_param_id=5010,
        target_type=DamageTargetType.Character,
        radius=0.6000000238418579,
        life=0.5,
        repetition_time=0.0,
    )
    CreateHazard(
        11010603,
        Objects.o1201_1000,
        model_point=43,
        behavior_param_id=5010,
        target_type=DamageTargetType.Character,
        radius=0.6000000238418579,
        life=0.5,
        repetition_time=0.0,
    )
    CreateHazard(
        11010604,
        Objects.o1201_1000,
        model_point=44,
        behavior_param_id=5010,
        target_type=DamageTargetType.Character,
        radius=0.6000000238418579,
        life=0.5,
        repetition_time=0.0,
    )
    Restart()


@RestartOnRest
def Event11015116():
    """ 11015116: Event 11015116 """
    IfFlagOff(1, 61010610)
    IfFlagOff(1, 11010607)
    IfFlagOff(1, 11010600)
    IfCharacterInsideRegion(1, PLAYER, region=Boxes.GateClosingHollowTrigger)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(11015115)
    IfFlagOn(-1, 11015181)
    IfFlagOn(-1, 61010610)
    IfConditionTrue(0, input_condition=-1)
    DisableFlag(11015115)


@RestartOnRest
def Event11010609():
    """ 11010609: Event 11010609 """
    DisableNetworkSync()
    IfFlagOn(1, 11015115)
    IfFlagOff(1, 61010610)
    IfConditionTrue(0, input_condition=1)
    ActivateObject(Objects.o1200_1000, obj_act_id=-1, relative_index=-1)
    Wait(1.0)
    Restart()


@RestartOnRest
def Event11010607():
    """ 11010607: Event 11010607 """
    SkipLinesIfThisEventOff(3)
    Move(
        Characters.c2550_0016,
        destination=Cylinders.GateClosingHollowNest,
        destination_type=CoordEntityType.Region,
        short_move=True,
    )
    SetNest(Characters.c2550_0016, Cylinders.GateClosingHollowNest)
    End()
    IfCharacterInsideRegion(1, Characters.c2550_0016, region=Boxes.ArmoredTuskAreaAfterGate)
    IfEntityWithinDistance(1, Characters.c2550_0016, Objects.o1200_1000, radius=3.0)
    IfFlagOn(1, 11015181)
    IfConditionTrue(0, input_condition=1)
    SetNest(Characters.c2550_0016, Cylinders.GateClosingHollowNest)
    ClearTargetList(Characters.c2550_0016)
    ReplanAI(Characters.c2550_0016)


@RestartOnRest
def Event11010608():
    """ 11010608: Event 11010608 """
    IfFlagOn(1, 61010610)
    IfCharacterBackreadEnabled(1, Characters.c3460_0000)
    IfCharacterInsideRegion(1, Characters.c3460_0000, region=Boxes.ArmoredTuskAreaAfterGate)
    IfConditionTrue(0, input_condition=1)
    AICommand(Characters.c3460_0000, command_id=1, slot=0)
    SetNest(Characters.c3460_0000, Boxes.ArmoredTuskPointAfterGate)
    IfFlagOff(0, 61010610)
    AICommand(Characters.c3460_0000, command_id=-1, slot=0)
    SetNest(Characters.c3460_0000, Boxes.ArmoredTuskPointBeforeGate)
    Restart()


def Event11010621():
    """ 11010621: Event 11010621 """
    SkipLinesIfThisEventOff(3)
    EndOfAnimation(Objects.o1201_1001, 4)
    DisableObjectActivation(Objects.o1200_1001, obj_act_id=-1)
    End()
    EndOfAnimation(Objects.o1201_1001, 3)
    IfObjectActivated(0, obj_act_id=11010620)
    ForceAnimation(Objects.o1201_1001, 4)


def Event11010700():
    """ 11010700: Event 11010700 """
    SkipLinesIfThisEventOff(2)
    DisableObjectActivation(Objects.o1202, obj_act_id=-1)
    End()
    IfObjectActivated(0, obj_act_id=11010700)
    TriggerMultiplayerEvent(10010)
    IfHealthGreaterThan(0, PLAYER, 0.0)
    SkipLinesIfFlagOn(2, 11400200)
    PlayCutscene(100100, skippable=True, fade_out=False, player_id=PLAYER)
    SkipLines(2)
    PlayCutscene(100105, skippable=True, fade_out=False, player_id=PLAYER)
    EnableFlag(11500200)
    WaitFrames(1)
    AwardAchievement(29)


def Event11015170():
    """ 11015170: Event 11015170 """
    IfMultiplayerEvent(0, 10010)
    DisableNetworkSync()
    PlaySoundEffect(anchor_entity=Objects.o1303, sound_type=SoundType.o_Object, sound_id=130300002)
    WaitRandomSeconds(min_seconds=0.5, max_seconds=2.0)
    PlaySoundEffect(anchor_entity=Objects.o1303, sound_type=SoundType.o_Object, sound_id=130300002)
    WaitRandomSeconds(min_seconds=0.5, max_seconds=2.0)
    PlaySoundEffect(anchor_entity=Objects.o1303, sound_type=SoundType.o_Object, sound_id=130300002)
    Restart()


@RestartOnRest
def Event11010860(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 11010860: Event 11010860 """
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


def Event11010650(_, arg_0_3: int, arg_4_7: int):
    """ 11010650: Event 11010650 """
    SkipLinesIfThisEventSlotOff(4)
    EndOfAnimation(arg_0_3, 0)
    DisableObjectActivation(arg_0_3, obj_act_id=-1)
    EnableTreasure(arg_0_3)
    End()
    IfObjectActivated(0, obj_act_id=arg_4_7)
    WaitFrames(10)
    EnableTreasure(arg_0_3)


def Event11010899():
    """ 11010899: Event 11010899 """
    EnableImmortality(Characters.c3430_0000)
    DisableCharacter(Characters.c3430_0000)
    SetNest(Characters.c3430_0000, Boxes.HellkitePointC)
    SkipLinesIfClient(2)
    SetNetworkUpdateAuthority(Characters.c3430_0000, UpdateAuthority.Forced)
    DisableFlag(11010782)
    IfFlagOn(1, 11010791)
    IfFlagOff(1, 11015311)
    SkipLinesIfConditionFalse(6, 1)
    DisableFlag(11015310)
    EnableCharacter(Characters.c3430_0000)
    Move(
        Characters.c3430_0000,
        destination=Boxes.HellkitePointB,
        destination_type=CoordEntityType.Region,
        set_draw_parent=Collisions.h1115B1,
    )
    SetStandbyAnimationSettings(Characters.c3430_0000, standby_animation=7006)
    DisableCharacterCollision(Characters.c3430_0000)
    DisableGravity(Characters.c3430_0000)
    IfFlagOn(2, 11010791)
    IfFlagOn(2, 11015311)
    SkipLinesIfConditionFalse(4, 2)
    EnableCharacter(Characters.c3430_0000)
    Move(
        Characters.c3430_0000,
        destination=Boxes.HellkitePointC,
        destination_type=CoordEntityType.Region,
        short_move=True,
    )
    ResetStandbyAnimationSettings(Characters.c3430_0000)
    SetNest(Characters.c3430_0000, Boxes.HellkiteControlHomecoming)
    RunEvent(11010805, slot=0, args=(11015320, 11015325, 7004, 11015350))
    RunEvent(11010805, slot=1, args=(11015326, 11015331, 7008, 11015350))
    RunEvent(11010805, slot=2, args=(11015332, 11015333, 7009, 11015350))
    RunEvent(11010805, slot=3, args=(11015334, 11015337, 7011, 11015350))
    RunEvent(11010805, slot=4, args=(11015338, 11015339, 7006, 11015350))
    RunEvent(11010805, slot=5, args=(11015320, 11015323, 7009, 11015351))
    RunEvent(11010805, slot=6, args=(11015324, 11015339, 7006, 11015351))
    RunEvent(11010805, slot=7, args=(11015320, 11015323, 7011, 11015352))
    RunEvent(11010805, slot=8, args=(11015324, 11015339, 7006, 11015352))
    RunEvent(11010805, slot=9, args=(11015320, 11015321, 7004, 11015353))
    RunEvent(11010805, slot=10, args=(11015322, 11015333, 7008, 11015353))
    RunEvent(11010805, slot=11, args=(11015334, 11015335, 7009, 11015353))
    RunEvent(11010805, slot=12, args=(11015336, 11015337, 7011, 11015353))
    RunEvent(11010800, slot=0, args=(11015338, 11015339, 7010, 11015353))
    RunEvent(11010800, slot=1, args=(11015320, 11015339, 7010, 11015354))


@RestartOnRest
def Event11010900():
    """ 11010900: Event 11010900 """
    SkipLinesIfThisEventOff(4)
    DisableCharacter(Characters.c3430_0000)
    DisableCharacter(Characters.c3431_0000)
    DisableCharacter(Characters.c3430_0001)
    End()
    IfHealthLessThan(7, Characters.c3430_0000, 0.10000000149011612)
    IfFlagOff(7, 11015312)
    IfFlagOff(7, 11015300)
    IfConditionTrue(1, input_condition=7)
    IfConditionTrue(2, input_condition=7)
    IfConditionTrue(3, input_condition=7)
    IfFlagOff(1, 11010791)
    IfFlagOff(1, 11015311)
    IfFlagOn(2, 11010791)
    IfFlagOff(2, 11015311)
    IfFlagOn(3, 11010791)
    IfFlagOn(3, 11015311)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EnableFlag(11015310)
    SkipLinesIfFinishedConditionFalse(3, 1)
    ForceAnimation(Characters.c3430_0000, 7001, wait_for_completion=True)
    DisableCharacter(Characters.c3430_0000)
    End()
    SkipLinesIfFinishedConditionFalse(3, 2)
    ForceAnimation(Characters.c3430_0000, 7007, wait_for_completion=True)
    DisableCharacter(Characters.c3430_0000)
    End()
    DisableImmortality(Characters.c3430_0000)
    Kill(Characters.c3430_0000, award_souls=True)


@RestartOnRest
def Event11010790():
    """ 11010790: Event 11010790 """
    DisableGravity(Characters.c3430_0001)
    EnableInvincibility(Characters.c3430_0001)
    DisableCharacter(Characters.c3430_0001)
    SkipLinesIfClient(1)
    SetNetworkUpdateAuthority(Characters.c3430_0001, UpdateAuthority.Forced)
    EndIfThisEventOn()
    IfCharacterInsideRegion(0, PLAYER, region=Boxes.HellkiteReactionA)
    EnableFlag(11010790)
    SetNetworkUpdateRate(Characters.c3430_0001, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    DisableCollision(Collisions.h7004B1)
    EnableCharacter(Characters.c3430_0001)
    Move(
        Characters.c3430_0001,
        destination=Boxes.HellkitePointA,
        destination_type=CoordEntityType.Region,
        short_move=True,
    )
    ForceAnimation(Characters.c3430_0001, 7012, wait_for_completion=True)
    DisableCharacter(Characters.c3430_0001)
    EnableCollision(Collisions.h7004B1)


def Event11010791():
    """ 11010791: Event 11010791 """
    EndIfThisEventOn()
    IfFlagOff(1, 11015310)
    IfFlagOn(1, 11010790)
    IfFlagOff(1, 11010782)
    IfHealthGreaterThanOrEqual(1, Characters.c3430_0000, 0.10000000149011612)
    IfCharacterInsideRegion(1, PLAYER, region=Boxes.HellkiteMovementArea)
    IfAllPlayersOutsideRegion(1, region=Boxes.HellkiteControlAreaG)
    IfCharacterType(2, PLAYER, CharacterType.BlackPhantom)
    IfConditionFalse(1, input_condition=2)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(11015310)
    EnableFlag(11010791)
    EnableFlag(11010780)
    EnableCharacter(Characters.c3430_0000)
    Move(
        Characters.c3430_0000,
        destination=Boxes.HellkitePointA2,
        destination_type=CoordEntityType.Region,
        short_move=True,
    )
    SetStandbyAnimationSettings(Characters.c3430_0000, standby_animation=7006)
    ForceAnimation(Characters.c3430_0000, 7005)
    WaitFrames(395)
    Move(
        Characters.c3430_0000,
        destination=Boxes.HellkitePointB,
        destination_type=CoordEntityType.Region,
        short_move=True,
    )
    DisableFlag(11015310)


def Event11010780():
    """ 11010780: Event 11010780 """
    SkipLinesIfThisEventOff(2)
    EndOfAnimation(Objects.o1290, 2)
    End()
    IfHasTAEEvent(0, Characters.c3430_0000, tae_event_id=1000)
    ForceAnimation(Objects.o1290, 1, wait_for_completion=True)
    ForceAnimation(Objects.o1290, 2, loop=True)


@RestartOnRest
def Event11010784():
    """ 11010784: Event 11010784 """
    IfHasTAEEvent(0, Characters.c3430_0000, tae_event_id=500)
    EnableFlag(11015300)
    IfHasTAEEvent(0, Characters.c3430_0000, tae_event_id=600)
    DisableFlag(11015300)
    Restart()


@RestartOnRest
def Event11015301():
    """ 11015301: Event 11015301 """
    DisableCharacter(Characters.c3431_0000)
    IfCharacterBackreadEnabled(0, Characters.c3430_0000)
    SkipLinesIfThisEventOff(4)
    SetDisplayMask(Characters.c3430_0000, bit_index=0, switch_type=OnOffChange.On)
    SetCollisionMask(Characters.c3430_0000, bit_index=1, switch_type=OnOffChange.Off)
    AICommand(Characters.c3430_0000, command_id=20, slot=0)
    End()
    CreateNPCPart(
        Characters.c3430_0000,
        npc_part_id=3430,
        part_index=NPCPartType.Part1,
        part_health=200,
        damage_correction=1.0,
        body_damage_correction=1.0,
        is_invincible=False,
        start_in_stop_state=False,
    )
    IfCharacterPartHealthLessThanOrEqual(1, Characters.c3430_0000, npc_part_id=3430, value=0)
    IfFlagOff(1, 11015300)
    IfAttacked(1, Characters.c3430_0000, attacker=PLAYER)
    IfHealthGreaterThanOrEqual(1, Characters.c3430_0000, 0.10000000149011612)
    IfCharacterDead(2, Characters.c3430_0000)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(2)
    SkipLinesIfFlagOn(2, 11015311)
    ForceAnimation(Characters.c3430_0000, 8000)
    SkipLines(1)
    ForceAnimation(Characters.c3430_0000, 8010)
    IfHasTAEEvent(0, Characters.c3430_0000, tae_event_id=400)
    SetDisplayMask(Characters.c3430_0000, bit_index=0, switch_type=OnOffChange.On)
    SetCollisionMask(Characters.c3430_0000, bit_index=1, switch_type=OnOffChange.Off)
    Move(
        Characters.c3431_0000,
        destination=Characters.c3430_0000,
        destination_type=CoordEntityType.Character,
        model_point=66,
        copy_draw_parent=Characters.c3430_0000,
    )
    EnableCharacter(Characters.c3431_0000)
    ForceAnimation(Characters.c3431_0000, 8100)
    AICommand(Characters.c3430_0000, command_id=20, slot=0)
    ReplanAI(Characters.c3430_0000)
    IfCharacterHuman(-7, PLAYER)
    IfCharacterHollow(-7, PLAYER)
    EndIfConditionFalse(-7)
    AwardItemLot(34310000, host_only=True)


def Event11015302():
    """ 11015302: Event 11015302 """
    IfHost(-7)
    IfCharacterType(-7, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(1, input_condition=-7)
    IfFlagOff(1, 11015310)
    IfFlagOn(1, 11010791)
    IfFlagOff(1, 11015311)
    IfHealthGreaterThanOrEqual(1, Characters.c3430_0000, 0.10000000149011612)
    IfConditionTrue(2, input_condition=1)
    IfConditionTrue(3, input_condition=1)
    IfConditionTrue(4, input_condition=1)
    IfConditionTrue(5, input_condition=1)
    IfConditionTrue(6, input_condition=1)
    IfConditionTrue(7, input_condition=1)
    IfFlagOn(2, 11010100)
    IfCharacterInsideRegion(2, PLAYER, region=Boxes.HellkiteControlAreaA)
    IfCharacterInsideRegion(3, PLAYER, region=Boxes.HellkiteControlAreaB)
    IfFlagOn(4, 11010100)
    IfCharacterInsideRegion(4, PLAYER, region=Boxes.HellkiteControlAreaC)
    IfCharacterInsideRegion(5, PLAYER, region=Boxes.HellkiteControlAreaD)
    IfFlagOn(6, 11015305)
    IfFlagOn(7, 11015317)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(-1, input_condition=4)
    IfConditionTrue(-1, input_condition=5)
    IfConditionTrue(-1, input_condition=6)
    IfConditionTrue(-1, input_condition=7)
    IfConditionTrue(0, input_condition=-1)
    EnableFlag(11015310)
    SkipLinesIfFinishedConditionFalse(1, 2)
    EnableFlag(11015350)
    SkipLinesIfFinishedConditionFalse(1, 3)
    EnableFlag(11015351)
    SkipLinesIfFinishedConditionFalse(1, 4)
    EnableFlag(11015352)
    SkipLinesIfFinishedConditionFalse(1, 5)
    EnableFlag(11015353)
    SkipLinesIfFinishedConditionTrue(2, 6)
    SkipLinesIfFinishedConditionTrue(1, 7)
    SkipLines(1)
    EnableFlag(11015354)
    DisableFlagRange((11015320, 11015339))
    SkipLinesIfClient(2)
    EnableRandomFlagInRange((11015320, 11015339))
    EnableFlag(11015313)
    Restart()


def Event11010805(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11010805: Event 11010805 """
    IfHost(1)
    IfFlagOn(1, 11015310)
    IfFlagOn(1, arg_12_15)
    IfFlagRangeAnyOn(1, (arg_0_3, arg_4_7))
    IfHealthGreaterThan(1, Characters.c3430_0000, 0.10000000149011612)
    IfConditionTrue(0, input_condition=1)
    RestartIfFlagOn(11015311)
    SkipLinesIfClient(1)
    Move(
        Characters.c3430_0000,
        destination=Boxes.HellkitePointB,
        destination_type=CoordEntityType.Region,
        short_move=True,
    )
    SkipLinesIfNotEqual(2, left=arg_8_11, right=7011)
    EnableFlag(11015312)
    AddSpecialEffect(Characters.c3430_0000, 4160)
    SkipLinesIfEqual(1, left=arg_8_11, right=7006)
    ForceAnimation(Characters.c3430_0000, arg_8_11)
    SkipLinesIfNotEqual(1, left=arg_8_11, right=7004)
    WaitFrames(190)
    SkipLinesIfNotEqual(1, left=arg_8_11, right=7006)
    WaitFrames(90)
    SkipLinesIfNotEqual(1, left=arg_8_11, right=7008)
    WaitFrames(200)
    SkipLinesIfNotEqual(1, left=arg_8_11, right=7009)
    WaitFrames(180)
    SkipLinesIfNotEqual(1, left=arg_8_11, right=7011)
    WaitFrames(192)
    CancelSpecialEffect(Characters.c3430_0000, 4160)
    Move(
        Characters.c3430_0000,
        destination=Boxes.HellkitePointB,
        destination_type=CoordEntityType.Region,
        short_move=True,
    )
    DisableFlagRange((11015350, 11015354))
    DisableFlagRange((11015320, 11015339))
    DisableFlag(arg_12_15)
    DisableFlag(11015312)
    DisableFlag(11015310)
    Restart()


def Event11010800(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11010800: Event 11010800 """
    IfHost(1)
    IfFlagOn(1, 11015310)
    IfFlagOn(1, arg_12_15)
    IfFlagRangeAnyOn(1, (arg_0_3, arg_4_7))
    IfHealthGreaterThan(1, Characters.c3430_0000, 0.10000000149011612)
    IfConditionTrue(0, input_condition=1)
    RestartIfFlagOn(11015311)
    EnableFlag(11015311)
    EnableCharacterCollision(Characters.c3430_0000)
    EnableGravity(Characters.c3430_0000)
    SkipLinesIfClient(1)
    Move(
        Characters.c3430_0000,
        destination=Boxes.HellkitePointB,
        destination_type=CoordEntityType.Region,
        short_move=True,
    )
    ResetStandbyAnimationSettings(Characters.c3430_0000)
    SetBackreadStateAlternate(Characters.c3430_0000, state=True)
    SetNetworkUpdateRate(Characters.c3430_0000, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    AddSpecialEffect(Characters.c3430_0000, 4160)
    ForceAnimation(Characters.c3430_0000, arg_8_11)
    WaitFrames(111)
    CancelSpecialEffect(Characters.c3430_0000, 4160)
    SetBackreadStateAlternate(Characters.c3430_0000, state=False)
    DisableFlagRange((11015350, 11015354))
    DisableFlagRange((11015320, 11015339))
    DisableFlag(arg_12_15)
    DisableFlag(11015317)
    DisableFlag(11015310)
    Restart()


def Event11010890(
    _,
    arg_0_3: int,
    arg_4_7: int,
    arg_8_11: int,
    arg_12_15: int,
    arg_16_19: int,
    arg_20_23: int,
    arg_24_27: int,
):
    """ 11010890: Event 11010890 """
    IfFlagOn(1, 11015313)
    IfFlagOn(2, 11015313)
    IfFlagOn(3, 11015313)
    IfFlagOn(4, 11015313)
    IfFlagOn(5, 11015313)
    IfFlagOn(6, 11015313)
    IfFlagOn(7, 11015313)
    IfFlagOn(1, arg_0_3)
    IfFlagOn(2, arg_4_7)
    IfFlagOn(3, arg_8_11)
    IfFlagOn(4, arg_12_15)
    IfFlagOn(5, arg_16_19)
    IfFlagOn(6, arg_20_23)
    IfFlagOn(7, arg_24_27)
    IfConditionTrue(-7, input_condition=1)
    IfConditionTrue(-7, input_condition=2)
    IfConditionTrue(-7, input_condition=3)
    IfConditionTrue(-7, input_condition=4)
    IfConditionTrue(-7, input_condition=5)
    IfConditionTrue(-7, input_condition=6)
    IfConditionTrue(-7, input_condition=7)
    IfConditionTrue(0, input_condition=-7)
    DisableFlag(11015313)
    SkipLinesIfFinishedConditionFalse(1, 1)
    EnableFlag(arg_0_3)
    SkipLinesIfFinishedConditionFalse(1, 2)
    EnableFlag(arg_4_7)
    SkipLinesIfFinishedConditionFalse(1, 3)
    EnableFlag(arg_8_11)
    SkipLinesIfFinishedConditionFalse(1, 4)
    EnableFlag(arg_12_15)
    SkipLinesIfFinishedConditionFalse(1, 5)
    EnableFlag(arg_16_19)
    SkipLinesIfFinishedConditionFalse(1, 6)
    EnableFlag(arg_20_23)
    SkipLinesIfFinishedConditionFalse(1, 7)
    EnableFlag(arg_24_27)
    Restart()


def Event11015303():
    """ 11015303: Event 11015303 """
    IfFlagOff(1, 11015306)
    IfFlagOff(1, 11015311)
    IfFlagOn(1, 11010791)
    IfFlagOn(1, 11010100)
    IfCharacterInsideRegion(-7, PLAYER, region=Boxes.HellkiteControlAreaC)
    IfCharacterInsideRegion(-7, PLAYER, region=Boxes.HellkiteControlAreaF1)
    IfCharacterInsideRegion(-7, PLAYER, region=Boxes.HellkiteControlAreaF2)
    IfConditionTrue(1, input_condition=-7)
    IfFlagOn(2, 11015306)
    IfFlagOff(2, 11015311)
    IfFlagOn(2, 11010791)
    IfAllPlayersOutsideRegion(2, region=Boxes.HellkiteControlAreaC)
    IfAllPlayersOutsideRegion(2, region=Boxes.HellkiteControlAreaF1)
    IfAllPlayersOutsideRegion(2, region=Boxes.HellkiteControlAreaF2)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionTrue(2, 2)
    EnableFlag(11015306)
    Restart()
    DisableFlag(11015306)
    RestartEvent(11015304)
    Restart()


def Event11015304():
    """ 11015304: Event 11015304 """
    DisableNetworkSync()
    IfFlagOff(1, 11015305)
    IfFlagOn(1, 11015306)
    IfConditionTrue(0, input_condition=1)
    Wait(20.0)
    EnableFlag(11015305)
    Restart()


def Event11010850():
    """ 11010850: Event 11010850 """
    IfFlagOn(1, 11010791)
    IfFlagOff(1, 11015311)
    IfHealthGreaterThanOrEqual(1, Characters.c3430_0000, 0.10000000149011612)
    IfAttacked(1, Characters.c3430_0000, attacker=PLAYER)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(11015317)
    Restart()


def Event11010851():
    """ 11010851: Event 11010851 """
    IfFlagOff(1, 11015316)
    IfFlagOn(1, 11010791)
    IfFlagOff(1, 11015311)
    IfAllPlayersOutsideRegion(1, region=Boxes.HellkiteControlAreaH)
    IfHealthLessThan(1, Characters.c3430_0000, 0.699999988079071)
    IfHealthGreaterThanOrEqual(1, Characters.c3430_0000, 0.10000000149011612)
    IfFlagOn(2, 11015316)
    IfFlagOn(2, 11010791)
    IfCharacterInsideRegion(2, PLAYER, region=Boxes.HellkiteControlAreaH)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionTrue(2, 2)
    EnableFlag(11015316)
    Restart()
    DisableFlag(11015316)
    RestartEvent(11010852)
    Restart()


def Event11010852():
    """ 11010852: Event 11010852 """
    DisableNetworkSync()
    IfFlagOff(1, 11015315)
    IfFlagOn(1, 11015316)
    IfConditionTrue(0, input_condition=1)
    Wait(60.0)
    EnableFlag(11015315)
    Restart()


@RestartOnRest
def Event11015307():
    """ 11015307: Event 11015307 """
    IfFlagOff(1, 11015310)
    IfFlagOn(1, 11010791)
    IfFlagOn(1, 11015311)
    IfHealthGreaterThanOrEqual(1, Characters.c3430_0000, 0.10000000149011612)
    IfConditionTrue(0, input_condition=1)
    EnableAI(Characters.c3430_0000)
    ClearTargetList(Characters.c3430_0000)
    ReplanAI(Characters.c3430_0000)
    SetNest(Characters.c3430_0000, Boxes.HellkitePointC)
    IfHasTAEEvent(0, Characters.c3430_0000, tae_event_id=700)
    Move(
        Characters.c3430_0000,
        destination=Boxes.HellkiteControlHomecoming,
        destination_type=CoordEntityType.Region,
        short_move=True,
    )
    SetStandbyAnimationSettings(Characters.c3430_0000, standby_animation=7006)
    ForceAnimation(Characters.c3430_0000, 7016)
    WaitFrames(110)
    Move(
        Characters.c3430_0000,
        destination=Boxes.HellkitePointB,
        destination_type=CoordEntityType.Region,
        short_move=True,
    )
    AICommand(Characters.c3430_0000, command_id=-1, slot=1)
    DisableAI(Characters.c3430_0000)
    ClearTargetList(Characters.c3430_0000)
    ReplanAI(Characters.c3430_0000)
    DisableFlag(11015305)
    DisableFlag(11015309)
    DisableFlag(11015311)
    Restart()


def Event11015308():
    """ 11015308: Event 11015308 """
    IfFlagOff(1, 11015309)
    IfFlagOff(1, 11015310)
    IfFlagOn(1, 11010791)
    IfHealthGreaterThanOrEqual(1, Characters.c3430_0000, 0.10000000149011612)
    IfAllPlayersOutsideRegion(1, region=Boxes.HellkiteControlAreaE_FormerDepth140)
    IfFlagOn(2, 11015309)
    IfFlagOff(2, 11015310)
    IfFlagOn(2, 11010791)
    IfHealthGreaterThanOrEqual(2, Characters.c3430_0000, 0.10000000149011612)
    IfCharacterInsideRegion(2, PLAYER, region=Boxes.HellkiteControlAreaE_FormerDepth140)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionTrue(5, 2)
    EnableFlag(11015309)
    AICommand(Characters.c3430_0000, command_id=1, slot=1)
    ClearTargetList(Characters.c3430_0000)
    ReplanAI(Characters.c3430_0000)
    Restart()
    DisableFlag(11015309)
    AICommand(Characters.c3430_0000, command_id=-1, slot=1)
    ClearTargetList(Characters.c3430_0000)
    ReplanAI(Characters.c3430_0000)
    Restart()


def Event11010782():
    """ 11010782: Event 11010782 """
    IfFlagOff(1, 11015310)
    IfFlagOn(1, 11010790)
    IfFlagOn(1, 11010791)
    IfFlagOff(1, 11015311)
    IfCharacterType(7, PLAYER, CharacterType.BlackPhantom)
    IfConditionFalse(1, input_condition=7)
    IfCharacterInsideRegion(1, PLAYER, region=Boxes.HellkiteControlAreaG)
    IfConditionTrue(0, input_condition=1)
    WaitFrames(10)
    RestartIfFlagOn(11015311)
    EnableFlag(11015310)
    EnableFlag(11015312)
    DisableFlag(11010791)
    SetNetworkUpdateRate(Characters.c3430_0000, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    ForceAnimation(Characters.c3430_0000, 7013, wait_for_completion=True)
    DisableCharacter(Characters.c3430_0000)
    Move(
        Characters.c3430_0000,
        destination=Boxes.HellkitePointB,
        destination_type=CoordEntityType.Region,
        set_draw_parent=Collisions.h1113B1,
    )


def Event11010783():
    """ 11010783: Event 11010783 """
    IfFlagOff(1, 11015310)
    IfFlagOn(1, 11010790)
    IfFlagOn(1, 11010791)
    IfFlagOff(1, 11015311)
    IfFlagOn(1, 11015315)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(11015310)
    SetStandbyAnimationSettings(Characters.c3430_0000, standby_animation=7018)
    ForceAnimation(Characters.c3430_0000, 7017, wait_for_completion=True)
    IfHealthGreaterThanOrEqual(0, Characters.c3430_0000, 0.699999988079071)
    SetStandbyAnimationSettings(Characters.c3430_0000, standby_animation=7006)
    ForceAnimation(Characters.c3430_0000, 7019)
    WaitFrames(50)
    DisableFlag(11015315)
    DisableFlag(11015316)
    DisableFlag(11015310)
    Restart()


def Event11010200(_, arg_0_3: int, arg_4_7: int):
    """ 11010200: Event 11010200 """
    IfCharacterBackreadEnabled(1, Characters.c3430_0000)
    IfHasTAEEvent(1, Characters.c3430_0000, tae_event_id=arg_0_3)
    IfConditionTrue(0, input_condition=1)
    HellkiteBreathControl(Characters.c3430_0000, obj=Objects.o1060, animation_id=arg_4_7)
    IfDoesNotHaveTAEEvent(0, Characters.c3430_0000, tae_event_id=arg_0_3)
    Restart()


def Event11010510(_, arg_0_3: int, arg_4_7: int):
    """ 11010510: Event 11010510 """
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
    RestartIfThisEventSlotOff()
    IfFlagOn(0, 744)
    EnableFlag(744)
    IfFlagOff(0, 744)
    Restart()


def Event11010520(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11010520: Event 11010520 """
    SkipLinesIfThisEventSlotOff(2)
    DropMandatoryTreasure(arg_0_3)
    End()
    IfHealthLessThanOrEqual(0, arg_0_3, 0.0)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)


def Event11010501(_, arg_0_3: int, arg_4_7: int):
    """ 11010501: Event 11010501 """
    IfFlagOff(1, 1176)
    IfFlagOff(1, 1179)
    IfFlagOn(1, 1175)
    IfHealthLessThanOrEqual(1, arg_0_3, 0.8999999761581421)
    IfHealthGreaterThan(1, arg_0_3, 0.0)
    IfAttacked(1, arg_0_3, attacker=PLAYER)
    IfFlagOn(2, arg_4_7)
    IfThisEventOn(2)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EnableFlag(arg_4_7)
    EnableCharacter(arg_0_3)
    SetTeamTypeAndExitStandbyAnimation(arg_0_3, TeamType.HostileAlly)
    SetAIParamID(arg_0_3, 1)
    SaveRequest()
    RestartIfThisEventOff()
    IfFlagOn(0, 744)
    IfFlagOff(0, 744)
    Restart()


def Event11010530(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11010530: Event 11010530 """
    IfFlagOff(1, 1004)
    IfFlagOn(1, 1000)
    IfFlagOn(1, 11010591)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)
    EnableCharacter(arg_0_3)


def Event11010531(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11010531: Event 11010531 """
    IfFlagOff(1, 1004)
    IfFlagOn(1, 1008)
    IfFlagOn(1, 11510594)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)
    Move(
        arg_0_3,
        destination=Boxes.SolaireAtSunlightAltar,
        destination_type=CoordEntityType.Region,
        set_draw_parent=1013050,
    )
    SetNest(arg_0_3, Boxes.SolaireAtSunlightAltar)
    EnableCharacter(arg_0_3)


def Event11010532(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11010532: Event 11010532 """
    IfFlagOff(1, 1114)
    IfFlagOn(1, 1110)
    IfFlagOn(1, 11010181)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)
    ResetStandbyAnimationSettings(arg_0_3)


def Event11010533(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11010533: Event 11010533 """
    IfFlagOff(1, 1176)
    IfFlagOff(1, 1179)
    IfFlagOn(1, 1174)
    IfFlagOn(1, 11310590)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)
    EnableCharacter(arg_0_3)
    ClearEventValue(600, bit_count=4)


def Event11010534(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11010534: Event 11010534 """
    IfFlagOff(1, 1176)
    IfFlagOff(1, 1179)
    IfFlagOn(1, 1175)
    IfFlagOn(1, 724)
    IfCharacterAlive(1, arg_0_3)
    IfThisEventOff(1)
    IfHost(2)
    IfFlagOff(2, 1176)
    IfFlagOff(2, 1177)
    IfFlagOff(2, 1179)
    IfFlagOff(2, 1180)
    IfThisEventOn(2)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)
    DisableCharacter(arg_0_3)


def Event11010535(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11010535: Event 11010535 """
    IfFlagOff(1, 1176)
    IfFlagOn(-7, 1175)
    IfFlagOn(-7, 1179)
    IfConditionTrue(1, input_condition=-7)
    IfHealthLessThanOrEqual(1, arg_0_3, 0.0)
    IfThisEventOff(1)
    IfFlagOn(2, 1180)
    IfThisEventOn(2)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)
    EndIfFinishedConditionTrue(1)
    DropMandatoryTreasure(arg_0_3)


def Event11010537(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11010537: Event 11010537 """
    IfFlagOff(1, 1176)
    IfFlagOff(1, 1179)
    IfFlagOn(1, 1175)
    IfFlagOff(1, 1196)
    IfFlagOff(1, 1198)
    IfEventValueComparison(1, 600, bit_count=4, comparison_type=ComparisonType.GreaterThanOrEqual, value=2)
    IfThisEventOff(1)
    IfFlagOn(2, 703)
    IfFlagOn(3, 11010599)
    IfFlagOn(3, arg_12_15)
    IfThisEventOn(3)
    IfFlagOff(4, 11010599)
    IfFlagOn(4, arg_12_15)
    IfThisEventOn(4)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(-1, input_condition=4)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionTrue(8, 3)
    SkipLinesIfFinishedConditionFalse(9, 1)
    EnableFlag(11010599)
    SkipLinesIfClient(3)
    EnableFlag(50006070)
    DisableFlag(50006071)
    DisableFlag(50006080)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)
    DropMandatoryTreasure(arg_0_3)
    End()
    SkipLinesIfFinishedConditionFalse(3, 2)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)
    End()
    DropMandatoryTreasure(arg_0_3)


def Event11010538():
    """ 11010538: Event 11010538 """
    IfFlagOff(1, 1176)
    IfFlagOff(1, 1179)
    IfFlagOn(1, 1175)
    IfFlagOn(1, 11010596)
    IfConditionTrue(0, input_condition=1)
    DisableFlag(11010596)
    ClearEventValue(600, bit_count=4)
    Restart()


def Event11010539():
    """ 11010539: Event 11010539 """
    EndIfClient()
    IfFlagOn(1, 1177)
    IfFlagOn(1, 50006071)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(815)


def Event11010550(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11010550: Event 11010550 """
    IfFlagOff(1, 1574)
    IfFlagOn(1, 1570)
    IfFlagOn(1, 11010190)
    IfCharacterAlive(1, arg_0_3)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)
    EnableFlag(11010584)


def Event11010551():
    """ 11010551: Event 11010551 """
    EndIfFlagOn(11010593)
    DisableObjectActivation(Objects.o1308_02, obj_act_id=-1, relative_index=0)
    DisableObjectActivation(Objects.o1308_02, obj_act_id=-1, relative_index=1)
    DisableObjectActivation(Objects.o1308_02, obj_act_id=-1, relative_index=2)
    DisableObjectActivation(Objects.o1308_02, obj_act_id=-1, relative_index=3)
    IfFlagOn(0, 11010593)
    EnableObjectActivation(Objects.o1308_02, obj_act_id=-1, relative_index=0)
    EnableObjectActivation(Objects.o1308_02, obj_act_id=-1, relative_index=1)


def Event11010552(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11010552: Event 11010552 """
    IfFlagOff(1, 1574)
    IfFlagOn(1, 1570)
    IfFlagOn(-1, 3)
    IfFlagOn(2, 812)
    IfFlagOn(2, 813)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)
    DisableCharacter(arg_0_3)


def Event11010581(_, arg_0_3: int):
    """ 11010581: Event 11010581 """
    EndIfThisEventOn()
    IfFlagOn(0, 11010700)
    EnableCharacter(arg_0_3)


@RestartOnRest
def Event11010582():
    """ 11010582: Event 11010582 """
    SkipLinesIfClient(1)
    DisableFlag(11010586)
    SkipLinesIfFlagOn(4, 11010586)
    IfFlagOn(-1, 1175)
    IfFlagOn(-1, 1179)
    IfFlagOn(-1, 1181)
    IfConditionTrue(0, input_condition=-1)
    EnableFlag(11010586)
    DisableCharacter(Characters.c2570_0000)


def Event11010583():
    """ 11010583: Event 11010583 """
    EndIfClient()
    IfFlagOn(0, 744)
    IfFlagOff(0, 744)
    Wait(1.0)
    Move(
        Characters.c0000_0002,
        destination=Boxes.AbsolutionReset_Solaire,
        destination_type=CoordEntityType.Region,
        short_move=True,
    )
    SetStandbyAnimationSettings(Characters.c0000_0002, standby_animation=7845)
    Move(
        Characters.c0000_0003,
        destination=Boxes.AbsolutionReset_Griggs,
        destination_type=CoordEntityType.Region,
        short_move=True,
    )
    Move(
        Characters.c0000_0005,
        destination=Boxes.AbsolutionReset_Rhea,
        destination_type=CoordEntityType.Region,
        short_move=True,
    )
    SetStandbyAnimationSettings(Characters.c0000_0005, standby_animation=7880)
    Move(
        Characters.c2640_0000,
        destination=Boxes.AbsolutionReset_Andre,
        destination_type=CoordEntityType.Region,
        short_move=True,
    )
    SetStandbyAnimationSettings(Characters.c2640_0000, standby_animation=9000)
    DisableFlag(11015090)
    RestoreObject(Objects.o1252)
    RestartEvent(11015090)
    Move(
        Characters.c2510_0000,
        destination=Boxes.AbsolutionReset_MaleUndeadMerchant,
        destination_type=CoordEntityType.Region,
        short_move=True,
    )
    SetStandbyAnimationSettings(Characters.c2510_0000, standby_animation=9000)
    Move(
        Characters.c0000_0006,
        destination=Boxes.AbsolutionReset_Lautrec,
        destination_type=CoordEntityType.Region,
        short_move=True,
    )
    SetStandbyAnimationSettings(Characters.c0000_0006, standby_animation=7825)
    Restart()


def Event11010580():
    """ 11010580: Event 11010580 """
    IfCharacterHuman(-7, PLAYER)
    IfCharacterHollow(-7, PLAYER)
    IfConditionTrue(1, input_condition=-7)
    IfFlagOn(1, 11015030)
    IfFlagOff(1, 11015031)
    IfConditionTrue(2, input_condition=-7)
    IfFlagOff(2, 11015030)
    IfFlagOn(2, 11015031)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    WaitForNetworkApproval(max_seconds=3.0)
    SkipLinesIfFinishedConditionFalse(9, 1)
    AddSpecialEffect(PLAYER, 4170)
    SkipLinesIfClient(1)
    RotateToFaceEntity(PLAYER, Characters.c1000_0008)
    SkipLinesIfHost(1)
    SkipLinesIfThisEventOff(1)
    ForceAnimation(PLAYER, 7895, wait_for_completion=True)
    ForceAnimation(PLAYER, 7896, loop=True)
    EnableFlag(11015031)
    Restart()
    CancelSpecialEffect(PLAYER, 4170)
    SkipLinesIfHost(1)
    SkipLinesIfThisEventOff(1)
    ForceAnimation(PLAYER, 7897, wait_for_completion=True)
    DisableFlag(11015031)
    Restart()


def Event11010585():
    """ 11010585: Event 11010585 """
    DisableNetworkSync()
    WaitFrames(2)
    EnableFlag(11010580)


@RestartOnRest
def Event11015090(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 11015090: Event 11015090 """
    EndIfFlagOn(arg_0_3)
    EndIfFlagOn(arg_4_7)
    EnableObjectInvulnerability(arg_8_11)
    IfFlagOn(-1, arg_0_3)
    IfFlagOn(-1, arg_4_7)
    IfConditionTrue(0, input_condition=-1)
    DisableObjectInvulnerability(arg_8_11)
    WaitFrames(1)
    DestroyObject(arg_8_11)
    PlaySoundEffect(anchor_entity=arg_8_11, sound_type=SoundType.o_Object, sound_id=125200000)
    EnableFlag(11015090)
    IfFlagOn(0, 703)
    End()


def Event11015100():
    """ 11015100: Event 11015100 """
    SkipLinesIfClient(1)
    SetNetworkUpdateAuthority(Characters.c0000_0004, UpdateAuthority.Forced)
    SkipLinesIfThisEventOff(1)
    DisableCharacter(Characters.c0000_0002)
    SkipLinesIfFlagOn(3, 11015106)
    IfClient(2)
    IfFlagOn(2, 11015102)
    SkipLinesIfConditionTrue(1, 2)
    DisableCharacter(Characters.c0000_0004)
    EndIfFlagOn(3)
    IfMultiplayerCount(1, arg1=5, arg2=2)
    IfHost(1)
    IfCharacterHuman(1, PLAYER)
    IfFlagOff(1, 11015102)
    IfFlagOff(1, 11015106)
    IfFlagOn(-1, 1004)
    IfFlagOn(-1, 1005)
    IfFlagOn(-1, 1006)
    IfFlagOn(-1, 1010)
    IfFlagOn(-1, 1011)
    IfConditionFalse(1, input_condition=-1)
    IfCharacterBackreadEnabled(1, Characters.c0000_0004)
    IfConditionTrue(0, input_condition=1)
    PlaceSummonSign(
        SummonSignType.BlueEyeSign,
        Characters.c0000_0004,
        region=Points.SolaireSummonSign,
        summon_flag=11015102,
        dismissal_flag=11015106,
    )
    DisableCharacter(Characters.c0000_0002)


def Event11015101():
    """ 11015101: Event 11015101 """
    EndIfThisEventOn()
    IfFlagOn(1, 11015102)
    IfFlagOn(1, 11015393)
    IfConditionTrue(0, input_condition=1)
    AICommand(Characters.c0000_0004, command_id=10, slot=0)
    ReplanAI(Characters.c0000_0004)
    IfCharacterInsideRegion(0, Characters.c0000_0004, region=Boxes.BellGargoylesFogPrompt)
    RotateToFaceEntity(Characters.c0000_0004, Cylinders.BellGargoylesFogRotationTarget)
    ForceAnimation(Characters.c0000_0004, 7410)
    AICommand(Characters.c0000_0004, command_id=-1, slot=0)
    ReplanAI(Characters.c0000_0004)


def Event11015103():
    """ 11015103: Event 11015103 """
    SkipLinesIfClient(1)
    SetNetworkUpdateAuthority(Characters.c0000_0011, UpdateAuthority.Forced)
    SkipLinesIfFlagOn(3, 11015107)
    IfClient(2)
    IfFlagOn(2, 11015105)
    SkipLinesIfConditionTrue(1, 2)
    DisableCharacter(Characters.c0000_0011)
    EndIfFlagOn(3)
    IfMultiplayerCount(1, arg1=5, arg2=2)
    IfHost(1)
    IfCharacterHuman(1, PLAYER)
    IfFlagOff(1, 11015105)
    IfFlagOff(1, 11015107)
    IfFlagOn(1, 11020607)
    IfFlagOn(-1, 1572)
    IfFlagOn(-1, 1573)
    IfConditionTrue(1, input_condition=-1)
    IfFlagOff(1, 1574)
    IfCharacterBackreadEnabled(1, Characters.c0000_0011)
    IfEntityWithinDistance(1, Characters.c0000_0011, PLAYER, radius=20.0)
    IfConditionTrue(0, input_condition=1)
    PlaceSummonSign(
        SummonSignType.BlueEyeSign,
        Characters.c0000_0011,
        region=Points.LautrecSummonSign,
        summon_flag=11015105,
        dismissal_flag=11015107,
    )


def Event11015203():
    """ 11015203: Event 11015203 """
    IfFlagOn(0, 11015105)
    AddSpecialEffect(Characters.c0000_0011, 5450)


def Event11015104():
    """ 11015104: Event 11015104 """
    EndIfThisEventOn()
    IfFlagOn(1, 11015105)
    IfFlagOn(1, 11015393)
    IfConditionTrue(0, input_condition=1)
    AICommand(Characters.c0000_0011, command_id=10, slot=0)
    ReplanAI(Characters.c0000_0011)
    IfCharacterInsideRegion(0, Characters.c0000_0011, region=Boxes.BellGargoylesFogPrompt)
    RotateToFaceEntity(Characters.c0000_0011, Cylinders.BellGargoylesFogRotationTarget)
    ForceAnimation(Characters.c0000_0011, 7410)
    AICommand(Characters.c0000_0011, command_id=-1, slot=0)
    ReplanAI(Characters.c0000_0011)


def Event11015900():
    """ 11015900: Event 11015900 """
    SkipLinesIfClient(1)
    SetNetworkUpdateAuthority(Characters.c0000_0004, UpdateAuthority.Forced)
    SkipLinesIfThisEventOff(1)
    DisableCharacter(Characters.c0000_0002)
    SkipLinesIfFlagOn(3, 11015106)
    IfClient(2)
    IfFlagOn(2, 11015102)
    SkipLinesIfConditionTrue(1, 2)
    DisableCharacter(Characters.c0000_0004)
    EndIfFlagOn(3)
    IfMultiplayerCount(1, arg1=4, arg2=3)
    IfHost(1)
    IfCharacterHuman(1, PLAYER)
    IfFlagOff(1, 11015102)
    IfFlagOff(1, 11015106)
    IfFlagOn(-1, 1004)
    IfFlagOn(-1, 1005)
    IfFlagOn(-1, 1006)
    IfFlagOn(-1, 1010)
    IfFlagOn(-1, 1011)
    IfConditionFalse(1, input_condition=-1)
    IfCharacterBackreadEnabled(1, Characters.c0000_0004)
    IfCharacterHasSpecialEffect(1, PLAYER, 28)
    IfConditionTrue(0, input_condition=1)
    PlaceSummonSign(
        SummonSignType.BlueEyeSign,
        Characters.c0000_0004,
        region=Points.SolaireSummonSign,
        summon_flag=11015102,
        dismissal_flag=11015106,
    )
    DisableCharacter(Characters.c0000_0002)


def Event11015901():
    """ 11015901: Event 11015901 """
    SkipLinesIfClient(1)
    SetNetworkUpdateAuthority(Characters.c0000_0011, UpdateAuthority.Forced)
    SkipLinesIfFlagOn(3, 11015107)
    IfClient(2)
    IfFlagOn(2, 11015105)
    SkipLinesIfConditionTrue(1, 2)
    DisableCharacter(Characters.c0000_0011)
    EndIfFlagOn(3)
    IfMultiplayerCount(1, arg1=4, arg2=3)
    IfHost(1)
    IfCharacterHuman(1, PLAYER)
    IfFlagOff(1, 11015105)
    IfFlagOff(1, 11015107)
    IfFlagOn(1, 11020607)
    IfFlagOn(-1, 1572)
    IfFlagOn(-1, 1573)
    IfConditionTrue(1, input_condition=-1)
    IfFlagOff(1, 1574)
    IfCharacterBackreadEnabled(1, Characters.c0000_0011)
    IfEntityWithinDistance(1, Characters.c0000_0011, PLAYER, radius=20.0)
    IfCharacterHasSpecialEffect(1, PLAYER, 28)
    IfConditionTrue(0, input_condition=1)
    PlaceSummonSign(
        SummonSignType.BlueEyeSign,
        Characters.c0000_0011,
        region=Points.LautrecSummonSign,
        summon_flag=11015105,
        dismissal_flag=11015107,
    )


def Event11015990(_, arg_0_3: int, arg_4_7: int):
    """ 11015990: Event 11015990 """
    IfFlagOn(0, arg_0_3)
    EraseNPCSummonSign(summoned_character=arg_4_7)
    IfFlagOff(0, arg_0_3)
    Restart()


def Event11015843(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11015843: Event 11015843 """
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


def Event11015846(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 11015846: Event 11015846 """
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
