"""
linked:


strings:

"""
from soulstruct.darksouls1r.events import *
from ..entities.m15_01_00_00_entities import *
from ..entities.m11_00_00_00_entities import Boxes as m11_00_Boxes, SpawnPoints as m11_00_SpawnPoints
from ..entities.m15_00_00_00_entities import Boxes as m15_00_Boxes
from ..entities.common_entities import *


def Constructor():
    """ 0: Event 0 """
    SkipLinesIfFlagOff(1, 12)
    RegisterBonfire(
        11510920,
        obj=Objects.o0200_0002,
        reaction_distance=2.0,
        reaction_angle=180.0,
        initial_kindle_level=0,
    )
    RegisterBonfire(
        11510992,
        obj=Objects.o0200_0000,
        reaction_distance=2.0,
        reaction_angle=180.0,
        initial_kindle_level=10,
    )
    RegisterBonfire(
        11510984,
        obj=Objects.o0200_0001,
        reaction_distance=2.0,
        reaction_angle=180.0,
        initial_kindle_level=0,
    )
    RegisterBonfire(
        11510976,
        obj=Objects.o0200_0003,
        reaction_distance=2.0,
        reaction_angle=180.0,
        initial_kindle_level=0,
    )
    RegisterLadder(start_climbing_flag=11510010, stop_climbing_flag=11510011, obj=Objects.o5410_0000)
    RegisterLadder(start_climbing_flag=11510012, stop_climbing_flag=11510013, obj=Objects.o5410_0001)
    DisableFlag(11510304)
    SkipLinesIfClient(2)
    DisableObject(Objects.o5863_0000)
    DeleteVFX(VFX.MultiplayerFog1, erase_root_only=False)
    DisableObject(Objects.o5611_0000)
    DisableCollision(Collisions.h0010B1_0002)
    DisableCollision(Collisions.h0010B1_0001)
    DisableCollision(Collisions.h0010B1_0000)
    SkipLinesIfFlagOff(1, 11510300)
    SkipLinesIfFlagOff(6, 11510303)
    DisableFlag(11510301)
    DisableFlag(11510302)
    EnableFlag(11510303)
    EndOfAnimation(Objects.o5610_0000, 53)
    EnableCollision(Collisions.h0010B1_0000)
    SkipLines(13)
    SkipLinesIfFlagOff(6, 11510302)
    DisableFlag(11510301)
    EnableFlag(11510302)
    DisableFlag(11510303)
    EndOfAnimation(Objects.o5610_0000, 50)
    EnableCollision(Collisions.h0010B1_0001)
    SkipLines(6)
    SkipLinesIfFlagOff(5, 11510301)
    EnableFlag(11510301)
    DisableFlag(11510302)
    DisableFlag(11510303)
    EndOfAnimation(Objects.o5610_0000, 51)
    EnableCollision(Collisions.h0010B1_0002)
    DisableObject(Objects.o5905_0000)
    DisableFlag(11510460)
    RunEvent(
        11510090,
        slot=0,
        args=(Objects.o5864_0000, VFX.CheckpointFog1, Boxes.CheckpointFog1FrontSide, Boxes.CheckpointFog1BackSide),
    )
    RunEvent(
        11510090,
        slot=1,
        args=(Objects.o5865_0000, VFX.CheckpointFog2, Boxes.CheckpointFog2FrontSide, Boxes.CheckpointFog2BackSide),
    )
    RunEvent(11510200)
    RunEvent(11510201)
    RunEvent(11510100)
    RunEvent(11510210)
    RunEvent(11510211)
    RunEvent(11510220)
    RunEvent(11510300)
    RunEvent(11510319)
    RunEvent(11510340)
    RunEvent(11510350)
    RunEvent(11510310)
    RunEvent(11515250)
    RunEvent(11515251)
    RunEvent(11510110)
    RunEvent(11510400)
    RunEvent(11510401)
    RunEvent(11510230)
    RunEvent(11510240)
    RunEvent(11515050)
    RunEvent(11510120)
    RunEvent(11510130)
    RunEvent(11510131)
    RunEvent(11510460)
    RunEvent(11510462)
    RunEvent(11510461)
    RunEvent(11510140)
    RunEvent(11510150)
    RunEvent(151)
    RunEvent(11510215)
    RunEvent(11515060, slot=0, args=(Characters.c2870_0000,))
    RunEvent(11515060, slot=1, args=(Characters.c2870_0001,))
    RunEvent(11515060, slot=2, args=(Characters.c2870_0002,))
    RunEvent(11515060, slot=3, args=(Characters.c2870_0003,))
    RunEvent(11515060, slot=4, args=(Characters.c2870_0004,))
    RunEvent(11515060, slot=5, args=(Characters.c2870_0005,))
    RunEvent(11515060, slot=6, args=(1510406,))
    RunEvent(11515060, slot=7, args=(1510407,))
    RunEvent(11515060, slot=8, args=(Characters.c2870_0008,))
    RunEvent(11515060, slot=9, args=(Characters.c2870_0009,))
    RunEvent(11515060, slot=10, args=(1510410,))
    RunEvent(11515060, slot=11, args=(1510411,))
    RunEvent(11515060, slot=12, args=(Characters.c2870_0012,))
    RunEvent(11515060, slot=13, args=(Characters.c2870_0013,))
    RunEvent(11515080, slot=0, args=(Characters.c5351_0000, Characters.c5353_0000))
    RunEvent(11515080, slot=1, args=(Characters.c5351_0001, Characters.c5353_0001))
    RunEvent(11510260, slot=0, args=(11510251, Boxes.Door01_Inside, Boxes.Door01_Outside))
    RunEvent(11510260, slot=1, args=(11510257, Boxes.Door07_Inside, Boxes.Door07_Outside))
    RunEvent(11510260, slot=2, args=(11510258, Boxes.Door08_Inside, Boxes.Door08_Outside))
    DisableSoundEvent(1513800)
    SkipLinesIfFlagOff(10, 12)
    ForceAnimation(Objects.o5630_0000, 0, loop=True)
    ForceAnimation(Objects.o5620_0000, 0, loop=True)
    RunEvent(11515392)
    DisableObject(Objects.o5860_0000)
    DeleteVFX(VFX.OrnsteinSmoughEntranceFog1, erase_root_only=False)
    DisableObject(Objects.o5861_0000)
    DeleteVFX(VFX.OrnsteinSmoughExitFog1, erase_root_only=False)
    DisableObject(Objects.o5862_0000)
    DeleteVFX(VFX.OrnsteinSmoughExitFog2, erase_root_only=False)
    SkipLines(11)
    RunEvent(11515390)
    RunEvent(11515391)
    RunEvent(11515393)
    RunEvent(11515392)
    RunEvent(11510001)
    RunEvent(11515394)
    RunEvent(11515395)
    RunEvent(11515396)
    RunEvent(11515397)
    RunEvent(11515398)
    RunEvent(11515399)
    DisableSoundEvent(1513802)
    SkipLinesIfFlagOff(6, 11510900)
    RunEvent(11515382)
    DisableObject(Objects.o5867_0000)
    DeleteVFX(VFX.GwyndolinEntranceFog1, erase_root_only=False)
    DisableObject(Objects.o5868_0000)
    DeleteVFX(VFX.GwyndolinEntranceFog2, erase_root_only=False)
    SkipLines(9)
    RunEvent(11515380)
    RunEvent(11515381)
    RunEvent(11516388)
    RunEvent(11515383)
    RunEvent(11515382)
    RunEvent(11510900)
    RunEvent(11515384)
    RunEvent(11515385)
    RunEvent(11515386)
    RunEvent(11510450)
    RunEvent(11510710, slot=0, args=(11510251, Characters.c2410_0009, Boxes.Door01_Inside, Boxes.Door01_Outside))
    RunEvent(11510710, slot=1, args=(11510251, Characters.c2410_0014, Boxes.Door01_Inside, Boxes.Door01_Outside))
    RunEvent(11510710, slot=2, args=(11510251, Characters.c2410_0015, Boxes.Door01_Inside, Boxes.Door01_Outside))
    RunEvent(11510710, slot=3, args=(11510251, Characters.c2410_0001, Boxes.Door01_Inside, Boxes.Door01_Outside))
    RunEvent(11510710, slot=4, args=(11510251, Characters.c2410_0000, Boxes.Door01_Inside, Boxes.Door01_Outside))
    RunEvent(11510710, slot=5, args=(11510251, Characters.c2410_0002, Boxes.Door01_Inside, Boxes.Door01_Outside))
    RunEvent(11510710, slot=6, args=(11510251, Characters.c2410_0003, Boxes.Door01_Inside, Boxes.Door01_Outside))
    RunEvent(11510710, slot=7, args=(11510251, Characters.c2410_0004, Boxes.Door01_Inside, Boxes.Door01_Outside))
    RunEvent(11510710, slot=8, args=(11510251, Characters.c2410_0006, Boxes.Door01_Inside, Boxes.Door01_Outside))
    RunEvent(11510710, slot=9, args=(11510251, Characters.c2410_0007, Boxes.Door01_Inside, Boxes.Door01_Outside))
    RunEvent(11510710, slot=10, args=(11510251, Characters.c2410_0010, Boxes.Door01_Inside, Boxes.Door01_Outside))
    RunEvent(11510710, slot=11, args=(11510251, Characters.c2410_0011, Boxes.Door01_Inside, Boxes.Door01_Outside))
    RunEvent(11510710, slot=12, args=(11510251, Characters.c2410_0012, Boxes.Door01_Inside, Boxes.Door01_Outside))
    RunEvent(11510710, slot=13, args=(11510251, Characters.c2410_0013, Boxes.Door01_Inside, Boxes.Door01_Outside))
    RunEvent(11510710, slot=20, args=(11510257, Characters.c2410_0009, Boxes.Door07_Inside, Boxes.Door07_Outside))
    RunEvent(11510710, slot=21, args=(11510257, Characters.c2410_0014, Boxes.Door07_Inside, Boxes.Door07_Outside))
    RunEvent(11510710, slot=22, args=(11510257, Characters.c2410_0015, Boxes.Door07_Inside, Boxes.Door07_Outside))
    RunEvent(11510710, slot=23, args=(11510257, Characters.c2410_0001, Boxes.Door07_Inside, Boxes.Door07_Outside))
    RunEvent(11510710, slot=24, args=(11510257, Characters.c2410_0000, Boxes.Door07_Inside, Boxes.Door07_Outside))
    RunEvent(11510710, slot=25, args=(11510257, Characters.c2410_0002, Boxes.Door07_Inside, Boxes.Door07_Outside))
    RunEvent(11510710, slot=26, args=(11510257, Characters.c2410_0003, Boxes.Door07_Inside, Boxes.Door07_Outside))
    RunEvent(11510710, slot=27, args=(11510257, Characters.c2410_0004, Boxes.Door07_Inside, Boxes.Door07_Outside))
    RunEvent(11510710, slot=28, args=(11510257, Characters.c2410_0006, Boxes.Door07_Inside, Boxes.Door07_Outside))
    RunEvent(11510710, slot=29, args=(11510257, Characters.c2410_0007, Boxes.Door07_Inside, Boxes.Door07_Outside))
    RunEvent(11510710, slot=30, args=(11510257, Characters.c2410_0010, Boxes.Door07_Inside, Boxes.Door07_Outside))
    RunEvent(11510710, slot=31, args=(11510257, Characters.c2410_0011, Boxes.Door07_Inside, Boxes.Door07_Outside))
    RunEvent(11510710, slot=32, args=(11510257, Characters.c2410_0012, Boxes.Door07_Inside, Boxes.Door07_Outside))
    RunEvent(11510710, slot=33, args=(11510257, Characters.c2410_0013, Boxes.Door07_Inside, Boxes.Door07_Outside))
    RunEvent(11510710, slot=40, args=(11510258, Characters.c2410_0009, Boxes.Door08_Inside, Boxes.Door08_Outside))
    RunEvent(11510710, slot=41, args=(11510258, Characters.c2410_0014, Boxes.Door08_Inside, Boxes.Door08_Outside))
    RunEvent(11510710, slot=42, args=(11510258, Characters.c2410_0015, Boxes.Door08_Inside, Boxes.Door08_Outside))
    RunEvent(11510710, slot=43, args=(11510258, Characters.c2410_0001, Boxes.Door08_Inside, Boxes.Door08_Outside))
    RunEvent(11510710, slot=44, args=(11510258, Characters.c2410_0000, Boxes.Door08_Inside, Boxes.Door08_Outside))
    RunEvent(11510710, slot=45, args=(11510258, Characters.c2410_0002, Boxes.Door08_Inside, Boxes.Door08_Outside))
    RunEvent(11510710, slot=46, args=(11510258, Characters.c2410_0003, Boxes.Door08_Inside, Boxes.Door08_Outside))
    RunEvent(11510710, slot=47, args=(11510258, Characters.c2410_0004, Boxes.Door08_Inside, Boxes.Door08_Outside))
    RunEvent(11510710, slot=48, args=(11510258, Characters.c2410_0006, Boxes.Door08_Inside, Boxes.Door08_Outside))
    RunEvent(11510710, slot=49, args=(11510258, Characters.c2410_0007, Boxes.Door08_Inside, Boxes.Door08_Outside))
    RunEvent(11510710, slot=50, args=(11510258, Characters.c2410_0010, Boxes.Door08_Inside, Boxes.Door08_Outside))
    RunEvent(11510710, slot=51, args=(11510258, Characters.c2410_0011, Boxes.Door08_Inside, Boxes.Door08_Outside))
    RunEvent(11510710, slot=52, args=(11510258, Characters.c2410_0012, Boxes.Door08_Inside, Boxes.Door08_Outside))
    RunEvent(11510710, slot=53, args=(11510258, Characters.c2410_0013, Boxes.Door08_Inside, Boxes.Door08_Outside))
    RunEvent(11515200, slot=0, args=(Characters.c2780_0000,))
    RunEvent(11515210, slot=0, args=(Characters.c2780_0000,))
    RunEvent(11515220, slot=0, args=(Characters.c2780_0000,))
    RunEvent(11515230, slot=0, args=(Characters.c2780_0000,))
    RunEvent(11515240, slot=0, args=(Characters.c2780_0000, Boxes.MimicNest1))
    RunEvent(11510850, slot=0, args=(Characters.c2780_0000,))
    RunEvent(11515190, slot=0, args=(Characters.c2780_0000,))
    RunEvent(11515200, slot=1, args=(Characters.c2780_0001,))
    RunEvent(11515210, slot=1, args=(Characters.c2780_0001,))
    RunEvent(11515220, slot=1, args=(Characters.c2780_0001,))
    RunEvent(11515230, slot=1, args=(Characters.c2780_0001,))
    RunEvent(11515240, slot=1, args=(Characters.c2780_0001, Boxes.MimicNest2))
    RunEvent(11510850, slot=1, args=(Characters.c2780_0001,))
    RunEvent(11515190, slot=1, args=(Characters.c2780_0001,))
    RunEvent(11515200, slot=2, args=(Characters.c2780_0002,))
    RunEvent(11515210, slot=2, args=(Characters.c2780_0002,))
    RunEvent(11515220, slot=2, args=(Characters.c2780_0002,))
    RunEvent(11515230, slot=2, args=(Characters.c2780_0002,))
    RunEvent(11515240, slot=2, args=(Characters.c2780_0002, Boxes.MimicNest3))
    RunEvent(11510850, slot=2, args=(Characters.c2780_0002,))
    RunEvent(11515190, slot=2, args=(Characters.c2780_0002,))
    RunEvent(11515200, slot=3, args=(Characters.c2780_0003,))
    RunEvent(11515210, slot=3, args=(Characters.c2780_0003,))
    RunEvent(11515220, slot=3, args=(Characters.c2780_0003,))
    RunEvent(11515230, slot=3, args=(Characters.c2780_0003,))
    RunEvent(11515240, slot=3, args=(Characters.c2780_0003, Boxes.MimicNest4))
    RunEvent(11510850, slot=3, args=(Characters.c2780_0003,))
    RunEvent(11515190, slot=3, args=(Characters.c2780_0003,))
    RunEvent(11510600, slot=1, args=(Objects.o0110_0001, 11510601))
    RunEvent(11510600, slot=2, args=(Objects.o0110_0002, 11510602))
    RunEvent(11510600, slot=3, args=(Objects.o0110_0003, 11510603))
    RunEvent(11510600, slot=4, args=(Objects.o0110_0004, 11510604))
    RunEvent(11510600, slot=6, args=(Objects.o0110_0006, 11510606))
    RunEvent(11510600, slot=7, args=(Objects.o0110_0007, 11510607))
    RunEvent(11510600, slot=8, args=(Objects.o0110_0008, 11510608))
    RunEvent(11510600, slot=9, args=(Objects.o0110_0009, 11510609))
    RunEvent(11510600, slot=10, args=(Objects.o0110_0010, 11510610))
    RunEvent(11510600, slot=11, args=(Objects.o0110_0011, 11510611))
    RunEvent(11510600, slot=12, args=(Objects.o0110_0012, 11510612))
    RunEvent(11510600, slot=15, args=(Objects.o0110_0015, 11510615))
    RunEvent(11510600, slot=16, args=(Objects.o0110_0016, 11510616))
    RunEvent(11510600, slot=17, args=(Objects.o0110_0017, 11510617))
    RunEvent(11510600, slot=18, args=(Objects.o0110_0018, 11510618))
    RunEvent(11510600, slot=19, args=(Objects.o0110_0019, 11510619))
    RunEvent(11510860, slot=0, args=(Characters.c2300_0000, 0))
    RunEvent(11510860, slot=1, args=(Characters.c5351_0000, 53500000))
    RunEvent(11510860, slot=2, args=(Characters.c5351_0001, 53500000))
    RunEvent(11510860, slot=3, args=(Characters.c0000_0012, 0))
    RunEvent(11510860, slot=4, args=(Characters.c0000_0013, 0))
    RunEvent(
        11515843,
        slot=0,
        args=(11510902, Objects.o5860_0000, Boxes.OrnsteinSmoughFogPrompt, Boxes.OrnsteinSmoughFogRotationTarget),
    )
    RunEvent(11515846, slot=0, args=(11510902, Objects.o5860_0000, VFX.OrnsteinSmoughEntranceFog1))
    RunEvent(
        11515843,
        slot=1,
        args=(11510903, Objects.o5860_0000, Boxes.OrnsteinSmoughFogPrompt, Boxes.OrnsteinSmoughFogRotationTarget),
    )
    RunEvent(11515846, slot=1, args=(11510903, Objects.o5860_0000, VFX.OrnsteinSmoughEntranceFog1))
    RunEvent(
        11515843,
        slot=2,
        args=(11510900, Objects.o5867_0000, Boxes.GwyndolinFogPrompt, Boxes.GwyndolinFogRotationTarget),
    )
    RunEvent(11515846, slot=2, args=(11510900, Objects.o5867_0000, VFX.GwyndolinEntranceFog1))
    # <!--!>


def Preconstructor():
    """ 50: Event 50 """
    HumanityRegistration(Characters.c0000_0012, 8258)
    HumanityRegistration(Characters.c0000_0013, 8266)
    HumanityRegistration(Characters.c0000_0011, 8310)
    RunEvent(11515030)
    RunEvent(11515029)
    RunEvent(11515032)
    RunEvent(11515033)
    RunEvent(11515990, slot=0, args=(11515031, Characters.c0000_0011))
    HumanityRegistration(Characters.c0000_0006, 8310)
    SkipLinesIfFlagOn(2, 1008)
    SkipLinesIfFlagOn(1, 1004)
    DisableCharacter(Characters.c0000_0006)
    RunEvent(11510510, slot=0, args=(Characters.c0000_0006, 1004))
    RunEvent(11510520, slot=0, args=(Characters.c0000_0006, 1000, 1029, 1005))
    RunEvent(11510530, slot=0, args=(Characters.c0000_0006, 1000, 1029, 1008))
    HumanityRegistration(Characters.c0000_0003, 8318)
    RunEvent(11510501, slot=0, args=(Characters.c0000_0003, 1033))
    RunEvent(11510520, slot=1, args=(Characters.c0000_0003, 1030, 1036, 1034))
    RunEvent(11510531, slot=0, args=(Characters.c0000_0003, 1030, 1036, 1036))
    RunEvent(11510532, slot=0, args=(Characters.c0000_0003, 1030, 1036, 1031))
    RunEvent(11510533, slot=0, args=(Characters.c0000_0003,))
    DisableCharacter(Characters.c5310_0000)
    RunEvent(11510520, slot=2, args=(Characters.c5310_0000, 1230, 1239, 1232))
    SetTeamType(Characters.c5320_0000, TeamType.Ally)
    SkipLinesIfFlagRangeAnyOn(1, (1240, 1249))
    EnableFlag(1240)
    RunEvent(11510520, slot=3, args=(Characters.c5320_0000, 1240, 1249, 1242))
    RunEvent(11510502, slot=0, args=(Characters.c5320_0000, 1241))
    RunEvent(11515090, slot=0, args=(Characters.c2860_0000,))
    RunEvent(11515091, slot=0, args=(Characters.c2860_0000,))
    RunEvent(11515092, slot=0, args=(Characters.c2860_0000, Objects.o5965_0000, 1361, 1362))
    RunEvent(11510510, slot=4, args=(Characters.c2860_0000, 1361))
    RunEvent(11510520, slot=4, args=(Characters.c2860_0000, 1360, 1363, 1362))
    HumanityRegistration(Characters.c0000_0005, 8446)
    SkipLinesIfFlagOn(3, 1512)
    SkipLinesIfFlagOn(2, 1494)
    SkipLinesIfFlagOn(1, 1493)
    DisableCharacter(Characters.c0000_0005)
    RunEvent(11510510, slot=5, args=(Characters.c0000_0005, 1512))
    RunEvent(11510520, slot=5, args=(Characters.c0000_0005, 1490, 1514, 1513))
    RunEvent(11510535, slot=0, args=(Characters.c0000_0005, 1490, 1514, 1494))
    RunEvent(11510536, slot=0, args=(Characters.c0000_0005,))
    HumanityRegistration(Characters.c0000_0004, 8462)
    HumanityRegistration(Characters.c0000_0009, 8908)
    HumanityRegistration(Characters.c0000_0010, 8916)
    DisableCharacter(Characters.c0000_0004)
    DisableCharacter(Characters.c0000_0009)
    DisableCharacter(Characters.c0000_0010)
    RunEvent(11510541, slot=0, args=(Characters.c0000_0004, 1570, 1599, 1578))
    RunEvent(11510542, slot=0, args=(Characters.c0000_0004, 1570, 1599, 1575))
    RunEvent(11510543, slot=0, args=(Characters.c0000_0004, 1570, 1599, 1572))
    RunEvent(11510544, slot=0, args=(Characters.c0000_0004, 1570, 1599, 1575))


def Event11510090(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11510090: Event 11510090 """
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


def Event11515380():
    """ 11515380: Event 11515380 """
    IfFlagOff(1, 11510900)
    IfActionButton(
        1,
        prompt_text=10010403,
        anchor_entity=Boxes.GwyndolinFogPrompt,
        anchor_type=CoordEntityType.Region,
        line_intersects=Objects.o5867_0000,
        boss_version=True,
    )
    IfConditionTrue(0, input_condition=1)
    EnableFlag(743)
    RotateToFaceEntity(PLAYER, Boxes.GwyndolinFogRotationTarget)
    ForceAnimation(PLAYER, 7410, wait_for_completion=True)
    Restart()


def Event11515381():
    """ 11515381: Event 11515381 """
    DisableNetworkSync()
    IfFlagOff(1, 11510900)
    IfFlagOn(1, 11515383)
    IfCharacterType(1, PLAYER, CharacterType.WhitePhantom)
    IfActionButton(
        1,
        prompt_text=10010403,
        anchor_entity=Boxes.GwyndolinFogPrompt,
        anchor_type=CoordEntityType.Region,
        trigger_attribute=TriggerAttribute.All,
        line_intersects=Objects.o5867_0000,
        boss_version=True,
    )
    IfConditionTrue(0, input_condition=1)
    RotateToFaceEntity(PLAYER, Boxes.GwyndolinFogRotationTarget)
    SkipLinesIfFlagOn(2, 11510400)
    PlayCutscene(
        150151,
        skippable=False,
        fade_out=False,
        player_id=PLAYER,
        move_to_region=Boxes.GwyndolinFogPromptClient,
        move_to_map=ANOR_LONDO,
    )
    SkipLines(1)
    PlayCutscene(
        150156,
        skippable=False,
        fade_out=False,
        player_id=PLAYER,
        move_to_region=Boxes.GwyndolinFogPromptClient,
        move_to_map=ANOR_LONDO,
    )
    WaitFrames(1)
    EnableCharacter(Characters.c5320_0000)
    EnableFlag(11515388)
    Restart()


def Event11516388():
    """ 11516388: Event 11516388 """
    IfFlagOn(1, 11515388)
    IfCharacterType(1, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(0, input_condition=1)
    ForceAnimation(PLAYER, 7410)
    DisableFlag(11515388)
    Restart()


def Event11515383():
    """ 11515383: Event 11515383 """
    SkipLinesIfThisEventOn(3)
    IfFlagOff(1, 11510900)
    IfCharacterInsideRegion(1, PLAYER, region=Boxes.GwyndolinCombatStart)
    IfConditionTrue(0, input_condition=1)
    SkipLinesIfClient(2)
    NotifyBossBattleStart()
    SetNetworkUpdateAuthority(Characters.c5320_0000, UpdateAuthority.Forced)
    ActivateMultiplayerBuffs(Characters.c5320_0000)


@RestartOnRest
def Event11515382():
    """ 11515382: Event 11515382 """
    SkipLinesIfFlagOff(2, 11510900)
    DisableCharacter(Characters.c5320_0000)
    End()
    DisableAI(Characters.c5320_0000)
    IfFlagOn(1, 11515383)
    IfCharacterInsideRegion(1, PLAYER, region=Boxes.GwyndolinCombatStart)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(11515386)
    IfFlagOn(0, 11515387)
    SkipLinesIfClient(2)
    ForceAnimation(PLAYER, -1)
    ResetAnimation(PLAYER, disable_interpolation=True)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterHollow(-1, PLAYER)
    IfConditionTrue(2, input_condition=-1)
    IfPlayerCovenant(2, Covenant.DarkmoonBlade)
    SkipLinesIfConditionFalse(6, 2)
    BetrayCurrentCovenant()
    SkipLinesIfFlagOn(2, 9002)
    IncrementPvPSin()
    EnableFlag(9002)
    EnableFlag(742)
    SaveRequest()
    EnableAI(Characters.c5320_0000)
    SetTeamType(Characters.c5320_0000, TeamType.Boss)
    EnableBossHealthBar(Characters.c5320_0000, name=5320, slot=0)


def Event11510900():
    """ 11510900: Event 11510900 """
    IfHealthLessThanOrEqual(0, Characters.c5320_0000, 0.0)
    WaitFrames(1)
    SkipLinesIfClient(7)
    EnableFlag(11515389)
    IfFlagOn(0, 11515389)
    SkipLinesIfFlagOn(2, 11510400)
    PlayCutscene(
        150152,
        skippable=True,
        fade_out=False,
        player_id=PLAYER,
        move_to_region=Boxes.GwyndolinFogRotationTarget,
        move_to_map=ANOR_LONDO,
    )
    SkipLines(1)
    PlayCutscene(
        150157,
        skippable=True,
        fade_out=False,
        player_id=PLAYER,
        move_to_region=Boxes.GwyndolinFogRotationTarget,
        move_to_map=ANOR_LONDO,
    )
    EnableFlag(4047)
    WaitFrames(10)
    SkipLinesIfFlagOff(1, 12)
    EnableFlag(120)
    EnableFlag(11510900)
    KillBoss(1510650)
    DisableObject(Objects.o5867_0000)
    DeleteVFX(VFX.GwyndolinEntranceFog1, erase_root_only=True)
    EndIfClient()
    DisableFlag(11807170)
    DisableFlag(11807180)
    DisableFlag(11807190)
    DisableFlag(11807230)
    AwardAchievement(39)


def Event11515384():
    """ 11515384: Event 11515384 """
    DisableNetworkSync()
    IfFlagOff(1, 11510900)
    IfFlagOn(1, 11515382)
    IfCharacterInsideRegion(1, PLAYER, region=Boxes.GwyndolinMusic)
    IfConditionTrue(0, input_condition=1)
    EnableSoundEvent(1513802)


def Event11515385():
    """ 11515385: Event 11515385 """
    DisableNetworkSync()
    IfHealthLessThanOrEqual(1, Characters.c5320_0000, 0.0)
    IfFlagOn(1, 11515384)
    IfConditionTrue(0, input_condition=1)
    DisableSoundEvent(1513802)


@RestartOnRest
def Event11515386():
    """ 11515386: Event 11515386 """
    IfThisEventOn(1)
    IfFlagOn(1, 11510400)
    IfHost(1)
    IfThisEventOn(2)
    IfHost(2)
    IfPlayerCovenant(2, Covenant.DarkmoonBlade)
    IfThisEventOn(3)
    IfHost(3)
    IfConditionFalse(3, input_condition=1)
    IfConditionFalse(3, input_condition=2)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    IfCharacterType(-2, PLAYER, CharacterType.BlackPhantom)
    IfCharacterType(-2, PLAYER, CharacterType.Intruder)
    EndIfConditionTrue(-2)
    SkipLinesIfFinishedConditionFalse(10, 1)
    SkipLinesIfUnknownPlayerType4(2)
    PlayCutscene(
        150155,
        skippable=True,
        fade_out=False,
        player_id=PLAYER,
        move_to_region=Boxes.GwyndolinInfiniteCorridorWarpPoint,
        move_to_map=ANOR_LONDO,
    )
    SkipLines(4)
    SkipLinesIfClient(2)
    PlayCutscene(
        150155,
        skippable=False,
        fade_out=False,
        player_id=PLAYER,
        move_to_region=Boxes.GwyndolinInfiniteCorridorWarpPoint,
        move_to_map=ANOR_LONDO,
    )
    SkipLines(1)
    PlayCutscene(150155, skippable=False, fade_out=False, player_id=PLAYER)
    WaitFrames(1)
    EnableFlag(11515387)
    End()
    SkipLinesIfFinishedConditionFalse(10, 2)
    SkipLinesIfUnknownPlayerType4(2)
    PlayCutscene(
        150161,
        skippable=True,
        fade_out=False,
        player_id=PLAYER,
        move_to_region=Boxes.GwyndolinInfiniteCorridorWarpPoint,
        move_to_map=ANOR_LONDO,
    )
    SkipLines(4)
    SkipLinesIfClient(2)
    PlayCutscene(
        150161,
        skippable=False,
        fade_out=False,
        player_id=PLAYER,
        move_to_region=Boxes.GwyndolinInfiniteCorridorWarpPoint,
        move_to_map=ANOR_LONDO,
    )
    SkipLines(1)
    PlayCutscene(150161, skippable=False, fade_out=False, player_id=PLAYER)
    WaitFrames(1)
    EnableFlag(11515387)
    End()
    SkipLinesIfUnknownPlayerType4(2)
    PlayCutscene(
        150160,
        skippable=True,
        fade_out=False,
        player_id=PLAYER,
        move_to_region=Boxes.GwyndolinInfiniteCorridorWarpPoint,
        move_to_map=ANOR_LONDO,
    )
    SkipLines(4)
    SkipLinesIfClient(2)
    PlayCutscene(
        150160,
        skippable=False,
        fade_out=False,
        player_id=PLAYER,
        move_to_region=Boxes.GwyndolinInfiniteCorridorWarpPoint,
        move_to_map=ANOR_LONDO,
    )
    SkipLines(1)
    PlayCutscene(150160, skippable=False, fade_out=False, player_id=PLAYER)
    WaitFrames(1)
    EnableFlag(11515387)
    End()


def Event11515390():
    """ 11515390: Event 11515390 """
    IfFlagOff(1, 12)
    IfActionButton(
        1,
        prompt_text=10010403,
        anchor_entity=Boxes.OrnsteinSmoughFogPrompt,
        anchor_type=CoordEntityType.Region,
        line_intersects=Objects.o5860_0000,
        boss_version=True,
    )
    IfConditionTrue(0, input_condition=1)
    RotateToFaceEntity(PLAYER, Boxes.OrnsteinSmoughFogRotationTarget)
    ForceAnimation(PLAYER, 7410)
    Restart()


def Event11515391():
    """ 11515391: Event 11515391 """
    IfFlagOff(1, 12)
    IfFlagOn(1, 11515393)
    IfCharacterType(1, PLAYER, CharacterType.WhitePhantom)
    IfActionButton(
        1,
        prompt_text=10010403,
        anchor_entity=Boxes.OrnsteinSmoughFogPrompt,
        anchor_type=CoordEntityType.Region,
        trigger_attribute=TriggerAttribute.All,
        line_intersects=Objects.o5860_0000,
    )
    IfConditionTrue(0, input_condition=1)
    RotateToFaceEntity(PLAYER, Boxes.OrnsteinSmoughFogRotationTarget)
    ForceAnimation(PLAYER, 7410)
    Restart()


def Event11515393():
    """ 11515393: Event 11515393 """
    SkipLinesIfThisEventOn(3)
    IfFlagOff(1, 12)
    IfCharacterInsideRegion(1, PLAYER, region=Boxes.OrnsteinSmoughCombatStart)
    IfConditionTrue(0, input_condition=1)
    SkipLinesIfClient(1)
    NotifyBossBattleStart()
    ActivateMultiplayerBuffs(Characters.c5270_0000)
    ActivateMultiplayerBuffs(Characters.c5271_0000)
    ActivateMultiplayerBuffs(Characters.c2360_0000)
    ActivateMultiplayerBuffs(Characters.c2360_0001)


@RestartOnRest
def Event11515392():
    """ 11515392: Event 11515392 """
    SkipLinesIfFlagOff(9, 12)
    DisableCharacter(Characters.c5270_0000)
    DisableCharacter(Characters.c5271_0000)
    DisableCharacter(Characters.c2360_0000)
    DisableCharacter(Characters.c2360_0001)
    Kill(Characters.c5270_0000, award_souls=False)
    Kill(Characters.c5271_0000, award_souls=False)
    Kill(Characters.c2360_0000, award_souls=False)
    Kill(Characters.c2360_0001, award_souls=False)
    End()
    DisableCharacter(Characters.c5271_0000)
    DisableCharacter(Characters.c2360_0001)
    DisableBackread(Characters.c5271_0000)
    SkipLinesIfFlagOn(1, 11510000)
    DisableCharacter(Characters.c5270_0000)
    DisableAI(Characters.c5270_0000)
    DisableAI(Characters.c2360_0000)
    IfFlagOn(1, 11515393)
    IfCharacterInsideRegion(1, PLAYER, region=Boxes.OrnsteinSmoughMusic)
    IfConditionTrue(0, input_condition=1)
    IfCharacterType(-1, PLAYER, CharacterType.BlackPhantom)
    IfCharacterType(-1, PLAYER, CharacterType.Intruder)
    EndIfConditionTrue(-1)
    SkipLinesIfFlagOn(8, 11510000)
    SkipLinesIfMultiplayer(2)
    PlayCutscene(150140, skippable=True, fade_out=False, player_id=PLAYER)
    SkipLines(1)
    PlayCutscene(150140, skippable=False, fade_out=False, player_id=PLAYER)
    WaitFrames(1)
    EnableCharacter(Characters.c5270_0000)
    EnableCharacter(Characters.c2360_0000)
    EnableFlag(11510000)
    EnableAI(Characters.c5270_0000)
    EnableAI(Characters.c2360_0000)
    EnableBossHealthBar(Characters.c5270_0000, name=5270, slot=1)
    EnableBossHealthBar(Characters.c2360_0000, name=2360, slot=0)


def Event11510001():
    """ 11510001: Event 11510001 """
    DisableObject(Objects.o0200_0002)
    IfCharacterDead(1, Characters.c5270_0000)
    IfCharacterDead(2, Characters.c2360_0000)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionTrue(10, 1)
    IfCharacterDead(0, Characters.c5271_0000)
    EnableFlag(11510902)
    PlaySoundEffect(anchor_entity=Characters.c5271_0000, sound_type=SoundType.s_SFX, sound_id=777777777)
    Kill(Characters.c2360_0001, award_souls=False)
    KillBoss(1510801)
    DisableFlag(11807100)
    DisableFlag(11807110)
    DisableFlag(11807120)
    DisableFlag(11807130)
    SkipLines(9)
    IfCharacterDead(0, Characters.c2360_0001)
    EnableFlag(11510903)
    PlaySoundEffect(anchor_entity=Characters.c2360_0001, sound_type=SoundType.s_SFX, sound_id=777777777)
    Kill(Characters.c5271_0000, award_souls=False)
    KillBoss(1510811)
    DisableFlag(11807060)
    DisableFlag(11807070)
    DisableFlag(11807080)
    DisableFlag(11807090)
    EnableFlag(12)
    EnableFlag(120)
    DisableObject(Objects.o5860_0000)
    DeleteVFX(VFX.OrnsteinSmoughEntranceFog1, erase_root_only=True)
    DisableObject(Objects.o5861_0000)
    DeleteVFX(VFX.OrnsteinSmoughExitFog1, erase_root_only=True)
    DisableObject(Objects.o5862_0000)
    DeleteVFX(VFX.OrnsteinSmoughExitFog2, erase_root_only=True)
    EnableObject(Objects.o0200_0002)
    RegisterBonfire(
        11510920,
        obj=Objects.o0200_0002,
        reaction_distance=2.0,
        reaction_angle=180.0,
        initial_kindle_level=0,
    )
    DisableNetworkSync()
    Wait(3.0)
    ForceAnimation(Objects.o5630_0000, 0, loop=True)
    ForceAnimation(Objects.o5620_0000, 0, loop=True)


def Event11515394():
    """ 11515394: Event 11515394 """
    DisableNetworkSync()
    IfFlagOff(1, 12)
    IfFlagOn(1, 11515392)
    SkipLinesIfHost(1)
    IfFlagOn(1, 11515391)
    IfCharacterInsideRegion(1, PLAYER, region=Boxes.OrnsteinSmoughMusic)
    IfConditionTrue(0, input_condition=1)
    EnableSoundEvent(1513800)
    EnableBackread(Characters.c5271_0000)


def Event11515395():
    """ 11515395: Event 11515395 """
    DisableNetworkSync()
    IfFlagOn(1, 12)
    IfFlagOn(1, 11515394)
    IfConditionTrue(0, input_condition=1)
    DisableSoundEvent(1513800)


def Event11515396():
    """ 11515396: Event 11515396 """
    IfCharacterDead(1, Characters.c5270_0000)
    IfCharacterDead(2, Characters.c2360_0000)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionTrue(12, 2)
    SkipLinesIfMultiplayer(2)
    PlayCutscene(150121, skippable=True, fade_out=False, player_id=PLAYER)
    SkipLines(1)
    PlayCutscene(150121, skippable=False, fade_out=False, player_id=PLAYER)
    WaitFrames(1)
    DisableCharacter(Characters.c5270_0000)
    DisableCharacter(Characters.c2360_0000)
    DisableImmortality(Characters.c2360_0000)
    Kill(Characters.c2360_0000, award_souls=False)
    EnableCharacter(Characters.c2360_0001)
    EnableBossHealthBar(Characters.c2360_0001, name=2360, slot=0)
    End()
    SkipLinesIfMultiplayer(2)
    PlayCutscene(150120, skippable=True, fade_out=False, player_id=PLAYER)
    SkipLines(1)
    PlayCutscene(150120, skippable=False, fade_out=False, player_id=PLAYER)
    WaitFrames(1)
    DisableCharacter(Characters.c2360_0000)
    DisableCharacter(Characters.c5270_0000)
    DisableImmortality(Characters.c5270_0000)
    Kill(Characters.c5270_0000, award_souls=False)
    EnableCharacter(Characters.c5271_0000)
    EnableBossHealthBar(Characters.c5271_0000, name=5270, slot=1)


def Event11515397():
    """ 11515397: Event 11515397 """
    IfHealthLessThanOrEqual(1, Characters.c5270_0000, 0.0)
    IfHealthLessThanOrEqual(2, Characters.c2360_0000, 0.0)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionTrue(2, 2)
    EnableImmortality(Characters.c2360_0000)
    End()
    EnableImmortality(Characters.c5270_0000)


@RestartOnRest
def Event11515398():
    """ 11515398: Event 11515398 """
    IfCharacterDead(1, Characters.c2360_0000)
    EndIfConditionTrue(1)
    IfCharacterBackreadEnabled(0, Characters.c2360_0000)
    CreateNPCPart(
        Characters.c2360_0000,
        npc_part_id=2360,
        part_index=NPCPartType.Part1,
        part_health=100,
        damage_correction=0.0,
        body_damage_correction=0.0,
        is_invincible=True,
        start_in_stop_state=False,
    )
    SetNPCPartBulletDamageScaling(Characters.c2360_0000, npc_part_id=2360, desired_scaling=0.0)
    SetNPCPartEffects(Characters.c2360_0000, npc_part_id=2360, material_sfx_id=50, material_vfx_id=50)
    IfHealthLessThanOrEqual(0, Characters.c2360_0000, 0.0)
    SetNPCPartHealth(Characters.c2360_0000, npc_part_id=2360, desired_health=0, overwrite_max=False)


@RestartOnRest
def Event11515399():
    """ 11515399: Event 11515399 """
    IfCharacterDead(1, Characters.c2360_0001)
    EndIfConditionTrue(1)
    IfCharacterBackreadEnabled(0, Characters.c2360_0001)
    CreateNPCPart(
        Characters.c2360_0001,
        npc_part_id=2360,
        part_index=NPCPartType.Part1,
        part_health=100,
        damage_correction=0.0,
        body_damage_correction=0.0,
        is_invincible=True,
        start_in_stop_state=False,
    )
    SetNPCPartBulletDamageScaling(Characters.c2360_0001, npc_part_id=2360, desired_scaling=0.0)
    SetNPCPartEffects(Characters.c2360_0001, npc_part_id=2360, material_sfx_id=50, material_vfx_id=50)
    IfHealthLessThanOrEqual(0, Characters.c2360_0001, 0.0)
    SetNPCPartHealth(Characters.c2360_0001, npc_part_id=2360, desired_health=0, overwrite_max=False)


@RestartOnRest
def Event11515060(_, arg_0_3: int):
    """ 11515060: Event 11515060 """
    IfCharacterDead(1, arg_0_3)
    EndIfConditionTrue(1)
    IfCharacterBackreadEnabled(0, arg_0_3)
    CreateNPCPart(
        arg_0_3,
        npc_part_id=2870,
        part_index=NPCPartType.Part2,
        part_health=100,
        damage_correction=0.0,
        body_damage_correction=0.0,
        is_invincible=True,
        start_in_stop_state=False,
    )
    SetNPCPartBulletDamageScaling(arg_0_3, npc_part_id=2870, desired_scaling=0.0)
    SetNPCPartEffects(arg_0_3, npc_part_id=2870, material_sfx_id=50, material_vfx_id=50)
    IfHealthLessThanOrEqual(0, arg_0_3, 0.0)
    SetNPCPartHealth(arg_0_3, npc_part_id=2870, desired_health=0, overwrite_max=False)


@RestartOnRest
def Event11515080(_, arg_0_3: int, arg_4_7: int):
    """ 11515080: Event 11515080 """
    DisableCharacter(arg_4_7)
    SkipLinesIfThisEventSlotOff(5)
    SetDisplayMask(arg_0_3, bit_index=0, switch_type=OnOffChange.On)
    SetCollisionMask(arg_0_3, bit_index=1, switch_type=OnOffChange.Off)
    AddSpecialEffect(arg_0_3, 5434)
    AICommand(arg_0_3, command_id=20, slot=0)
    End()
    IfCharacterBackreadEnabled(0, arg_0_3)
    CreateNPCPart(
        arg_0_3,
        npc_part_id=5351,
        part_index=NPCPartType.Part1,
        part_health=65,
        damage_correction=1.0,
        body_damage_correction=1.0,
        is_invincible=False,
        start_in_stop_state=False,
    )
    IfCharacterPartHealthLessThanOrEqual(1, arg_0_3, npc_part_id=5351, value=0)
    IfHealthLessThanOrEqual(2, arg_0_3, 0.0)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(2)
    ResetAnimation(arg_0_3, disable_interpolation=False)
    Move(
        arg_4_7,
        destination=arg_0_3,
        destination_type=CoordEntityType.Character,
        model_point=110,
        copy_draw_parent=arg_0_3,
    )
    EnableCharacter(arg_4_7)
    ForceAnimation(arg_0_3, 8000)
    ForceAnimation(arg_4_7, 8100)
    SetDisplayMask(arg_0_3, bit_index=0, switch_type=OnOffChange.On)
    SetCollisionMask(arg_0_3, bit_index=1, switch_type=OnOffChange.Off)
    AddSpecialEffect(arg_0_3, 5434)
    AICommand(arg_0_3, command_id=20, slot=0)
    ReplanAI(arg_0_3)
    EndIfNotEqual(left=arg_0_3, right=1510450)
    IfCharacterHuman(-7, PLAYER)
    IfCharacterHollow(-7, PLAYER)
    EndIfConditionFalse(-7)
    AwardItemLot(53530000, host_only=True)


def Event11510100():
    """ 11510100: Event 11510100 """
    SkipLinesIfThisEventOff(8)
    PostDestruction(Objects.o5810_0000)
    PostDestruction(Objects.o5801_0000)
    EndOfAnimation(Objects.o0500_0000, 111)
    EndOfAnimation(Objects.o5800_0000, 0)
    EndOfAnimation(Objects.o5801_0000, 1)
    EnableObjectInvulnerability(Objects.o5800_0000)
    EnableTreasure(Objects.o0500_0000)
    End()
    DisableTreasure(Objects.o0500_0000)
    SkipLinesIfClient(1)
    CreateObjectVFX(99010, obj=Objects.o0500_0000, model_point=90)
    ForceAnimation(Objects.o0500_0000, 110, loop=True)
    IfObjectDestroyed(0, Objects.o5810_0000)
    ForceAnimation(Objects.o0500_0000, 111)
    ForceAnimation(Objects.o5800_0000, 0)
    ForceAnimation(Objects.o5801_0000, 0, wait_for_completion=True)
    SkipLinesIfClient(1)
    DeleteObjectVFX(Objects.o0500_0000, erase_root=True)
    EnableTreasure(Objects.o0500_0000)
    DestroyObject(Objects.o5801_0000)


def Event11510110():
    """ 11510110: Event 11510110 """
    SkipLinesIfThisEventOff(2)
    EndOfAnimation(Objects.o5730_0000, 0)
    End()
    IfActionButton(
        0,
        prompt_text=10010400,
        anchor_entity=Objects.o5730_0000,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        model_point=100,
        trigger_attribute=TriggerAttribute.All,
    )
    Move(
        PLAYER,
        destination=Objects.o5730_0000,
        destination_type=CoordEntityType.Object,
        model_point=120,
        short_move=True,
    )
    ForceAnimation(PLAYER, 7120)
    ForceAnimation(Objects.o5730_0000, 0)


def Event11510200():
    """ 11510200: Event 11510200 """
    SkipLinesIfThisEventOff(4)
    DisableObjectActivation(Objects.o5760_0000, obj_act_id=-1)
    EndOfAnimation(Objects.o5700_0000, 0)
    EndOfAnimation(Objects.o5760_0000, 0)
    End()
    IfFlagOff(1, 11510700)
    IfActionButton(
        1,
        prompt_text=10010502,
        anchor_entity=Objects.o5760_0000,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        model_point=102,
        trigger_attribute=TriggerAttribute.All,
    )
    IfConditionTrue(0, input_condition=1)
    Move(
        PLAYER,
        destination=Objects.o5760_0000,
        destination_type=CoordEntityType.Object,
        model_point=103,
        short_move=True,
    )
    ForceAnimation(PLAYER, 8021)
    ForceAnimation(Objects.o5760_0000, 0, wait_for_completion=True)
    ForceAnimation(Objects.o5700_0000, 0)


def Event11510201():
    """ 11510201: Event 11510201 """
    DisableNetworkSync()
    IfFlagOff(1, 11510200)
    IfActionButton(
        1,
        prompt_text=10010400,
        anchor_entity=Boxes.CannotOpenPalaceGate,
        anchor_type=CoordEntityType.Region,
        trigger_attribute=TriggerAttribute.All,
        line_intersects=Objects.o5700_0000,
    )
    IfConditionTrue(0, input_condition=1)
    DisplayDialog(
        10010160,
        anchor_entity=-1,
        display_distance=3.0,
        button_type=ButtonType.OK_or_Cancel,
        number_buttons=NumberButtons.NoButton,
    )
    Restart()


def Event11510210():
    """ 11510210: Event 11510210 """
    SkipLinesIfThisEventOff(2)
    EndOfAnimation(Objects.o5710_0000, 0)
    End()
    EnableNavmeshType(Navigation.Navmesh_GardenGate, NavmeshType.Solid)
    IfActionButton(
        0,
        prompt_text=10010400,
        anchor_entity=Objects.o5710_0000,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        model_point=101,
        trigger_attribute=TriggerAttribute.All,
    )
    Move(
        PLAYER,
        destination=Objects.o5710_0000,
        destination_type=CoordEntityType.Object,
        model_point=121,
        short_move=True,
    )
    ForceAnimation(PLAYER, 7110)
    ForceAnimation(Objects.o5710_0000, 0)
    DisableNavmeshType(Navigation.Navmesh_GardenGate, NavmeshType.Solid)


def Event11510211():
    """ 11510211: Event 11510211 """
    DisableNetworkSync()
    IfFlagOff(1, 11510210)
    IfActionButton(
        1,
        prompt_text=10010400,
        anchor_entity=Objects.o5710_0000,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        model_point=100,
        trigger_attribute=TriggerAttribute.All,
    )
    IfConditionTrue(0, input_condition=1)
    DisplayDialog(
        10010161,
        anchor_entity=Objects.o5710_0000,
        display_distance=3.0,
        button_type=ButtonType.OK_or_Cancel,
        number_buttons=NumberButtons.NoButton,
    )
    Restart()


def Event11510220():
    """ 11510220: Event 11510220 """
    SkipLinesIfThisEventOn(1)
    IfCharacterInsideRegion(0, PLAYER, region=Spheres.RotatingBridgeFirstUse)
    ForceAnimation(Objects.o5600_0000, 0)


def Event11510260(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 11510260: Event 11510260 """
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


def Event11510710(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11510710: Event 11510710 """
    SkipLinesIfThisEventSlotOn(2)
    IfObjectActivated(0, obj_act_id=arg_0_3)
    EnableFlag(arg_0_3)
    DisableNetworkSync()
    IfCharacterInsideRegion(-1, arg_4_7, region=arg_8_11)
    IfCharacterInsideRegion(-1, arg_4_7, region=arg_12_15)
    IfConditionTrue(0, input_condition=-1)
    AddSpecialEffect(arg_4_7, 4150)
    Wait(3.0)
    Restart()


def Event11510300():
    """ 11510300: Event 11510300 """
    IfFlagOff(1, 11510301)
    IfActionButton(
        1,
        prompt_text=10010502,
        anchor_entity=Objects.o5610_0000,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        model_point=102,
        trigger_attribute=TriggerAttribute.All,
    )
    IfFlagOff(2, 11510303)
    IfActionButton(
        2,
        prompt_text=10010502,
        anchor_entity=Objects.o5610_0000,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        model_point=104,
        trigger_attribute=TriggerAttribute.All,
    )
    IfFlagOn(3, 11510305)
    IfFlagOff(3, 11510303)
    IfActionButton(
        3,
        prompt_text=10010501,
        anchor_entity=Objects.o5750_0001,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        model_point=192,
        trigger_attribute=TriggerAttribute.All,
    )
    IfFlagOn(4, 11510305)
    IfFlagOn(4, 11510303)
    IfActionButton(
        4,
        prompt_text=10010501,
        anchor_entity=Objects.o5750_0002,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        model_point=192,
        trigger_attribute=TriggerAttribute.All,
    )
    IfFlagOn(5, 11510305)
    IfFlagOff(5, 11510301)
    IfActionButton(
        5,
        prompt_text=10010501,
        anchor_entity=Objects.o5750_0003,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        model_point=192,
        trigger_attribute=TriggerAttribute.All,
    )
    IfFlagOn(6, 11510305)
    IfFlagOff(6, 11510302)
    IfActionButton(
        6,
        prompt_text=10010501,
        anchor_entity=Objects.o5750_0004,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        model_point=192,
        trigger_attribute=TriggerAttribute.All,
    )
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(-1, input_condition=4)
    IfConditionTrue(-1, input_condition=5)
    IfConditionTrue(-1, input_condition=6)
    IfConditionTrue(0, input_condition=-1)
    WaitForNetworkApproval(max_seconds=3.0)
    EnableFlag(11515300)
    SkipLinesIfFlagOn(20, 11510305)
    Move(
        PLAYER,
        destination=Objects.o5610_0000,
        destination_type=CoordEntityType.Object,
        model_point=103,
        short_move=True,
    )
    ForceAnimation(PLAYER, 8021)
    ForceAnimation(Objects.o5610_0000, 10, wait_for_completion=True)
    SkipLinesIfMultiplayer(2)
    PlayCutscene(
        cutscene_id=150100,
        skippable=True,
        fade_out=False,
        player_id=PLAYER,
        rotation=-90,
        relative_rotation_axis_x=337.5,
        relative_rotation_axis_z=255.0,
        vertical_translation=-12.0,
    )
    SkipLines(4)
    SkipLinesIfFlagOff(2, 11510304)
    PlayCutscene(
        cutscene_id=150100,
        skippable=False,
        fade_out=False,
        player_id=PLAYER,
        rotation=-90,
        relative_rotation_axis_x=337.5,
        relative_rotation_axis_z=255.0,
        vertical_translation=-12.0,
    )
    SkipLines(1)
    PlayCutscene(150100, skippable=False, fade_out=False, player_id=PLAYER)
    WaitFrames(1)
    EndOfAnimation(Objects.o5610_0000, 0)
    DisableCollision(Collisions.h0010B1_0000)
    EnableCollision(Collisions.h0010B1_0001)
    DisableFlag(11510303)
    EnableFlag(11510302)
    DisableFlag(11510304)
    EnableFlag(11510305)
    DisableFlag(11515300)
    Restart()
    SkipLinesIfFlagOff(33, 11510303)
    SkipLinesIfFinishedConditionFalse(6, 1)
    Move(
        PLAYER,
        destination=Objects.o5610_0000,
        destination_type=CoordEntityType.Object,
        model_point=103,
        short_move=True,
    )
    ForceAnimation(PLAYER, 8021)
    ForceAnimation(Objects.o5610_0000, 10)
    WaitFrames(130)
    IfFramesElapsed(0, 0)
    RunEvent(11515320, slot=0, args=(0, Collisions.h0010B1_0000, Collisions.h0010B1_0001, 11510303, 11510302, 180))
    SkipLinesIfFinishedConditionFalse(7, 4)
    Move(
        PLAYER,
        destination=Objects.o5750_0002,
        destination_type=CoordEntityType.Object,
        model_point=191,
        short_move=True,
    )
    ForceAnimation(PLAYER, 8000)
    ForceAnimation(Objects.o5750_0002, 1)
    ForceAnimation(Objects.o5610_0000, 10)
    WaitFrames(130)
    IfFramesElapsed(0, 0)
    RunEvent(11515320, slot=1, args=(0, Collisions.h0010B1_0000, Collisions.h0010B1_0001, 11510303, 11510302, 180))
    SkipLinesIfFinishedConditionFalse(7, 5)
    Move(
        PLAYER,
        destination=Objects.o5750_0003,
        destination_type=CoordEntityType.Object,
        model_point=191,
        short_move=True,
    )
    ForceAnimation(PLAYER, 8000)
    ForceAnimation(Objects.o5750_0003, 1)
    ForceAnimation(Objects.o5610_0000, 10)
    WaitFrames(130)
    IfFramesElapsed(0, 0)
    RunEvent(11515330, slot=0, args=(0, 1, Collisions.h0010B1_0002, 11510303, 11510301, 11, 180, 360))
    SkipLinesIfFinishedConditionFalse(7, 6)
    Move(
        PLAYER,
        destination=Objects.o5750_0004,
        destination_type=CoordEntityType.Object,
        model_point=191,
        short_move=True,
    )
    ForceAnimation(PLAYER, 8000)
    ForceAnimation(Objects.o5750_0004, 1)
    ForceAnimation(Objects.o5610_0000, 10)
    WaitFrames(130)
    IfFramesElapsed(0, 0)
    RunEvent(11515320, slot=2, args=(0, Collisions.h0010B1_0000, Collisions.h0010B1_0001, 11510303, 11510302, 180))
    IfFlagOff(0, 11515300)
    Restart()
    SkipLinesIfFlagOff(32, 11510302)
    SkipLinesIfFinishedConditionFalse(6, 1)
    Move(
        PLAYER,
        destination=Objects.o5610_0000,
        destination_type=CoordEntityType.Object,
        model_point=103,
        short_move=True,
    )
    ForceAnimation(PLAYER, 8021)
    ForceAnimation(Objects.o5610_0000, 11)
    WaitFrames(130)
    IfFramesElapsed(0, 0)
    RunEvent(11515320, slot=3, args=(1, Collisions.h0010B1_0001, Collisions.h0010B1_0002, 11510302, 11510301, 360))
    SkipLinesIfFinishedConditionFalse(6, 2)
    Move(
        PLAYER,
        destination=Objects.o5610_0000,
        destination_type=CoordEntityType.Object,
        model_point=101,
        short_move=True,
    )
    ForceAnimation(PLAYER, 8020)
    ForceAnimation(Objects.o5610_0000, 13)
    WaitFrames(130)
    IfFramesElapsed(0, 0)
    RunEvent(11515320, slot=4, args=(3, Collisions.h0010B1_0001, Collisions.h0010B1_0000, 11510302, 11510303, 180))
    SkipLinesIfFinishedConditionFalse(7, 3)
    Move(
        PLAYER,
        destination=Objects.o5750_0001,
        destination_type=CoordEntityType.Object,
        model_point=191,
        short_move=True,
    )
    ForceAnimation(PLAYER, 8000)
    ForceAnimation(Objects.o5750_0001, 1)
    ForceAnimation(Objects.o5610_0000, 13)
    WaitFrames(130)
    IfFramesElapsed(0, 0)
    RunEvent(11515320, slot=5, args=(3, Collisions.h0010B1_0001, Collisions.h0010B1_0000, 11510302, 11510303, 180))
    SkipLinesIfFinishedConditionFalse(7, 5)
    Move(
        PLAYER,
        destination=Objects.o5750_0003,
        destination_type=CoordEntityType.Object,
        model_point=191,
        short_move=True,
    )
    ForceAnimation(PLAYER, 8000)
    ForceAnimation(Objects.o5750_0003, 1)
    ForceAnimation(Objects.o5610_0000, 11)
    WaitFrames(130)
    IfFramesElapsed(0, 0)
    RunEvent(11515320, slot=6, args=(1, Collisions.h0010B1_0001, Collisions.h0010B1_0002, 11510302, 11510301, 360))
    IfFlagOff(0, 11515300)
    Restart()
    SkipLinesIfFlagOff(25, 11510301)
    SkipLinesIfFinishedConditionFalse(6, 2)
    Move(
        PLAYER,
        destination=Objects.o5610_0000,
        destination_type=CoordEntityType.Object,
        model_point=101,
        short_move=True,
    )
    ForceAnimation(PLAYER, 8020)
    ForceAnimation(Objects.o5610_0000, 12)
    WaitFrames(130)
    IfFramesElapsed(0, 0)
    RunEvent(11515320, slot=7, args=(2, Collisions.h0010B1_0002, Collisions.h0010B1_0001, 11510301, 11510302, 360))
    SkipLinesIfFinishedConditionFalse(7, 3)
    Move(
        PLAYER,
        destination=Objects.o5750_0001,
        destination_type=CoordEntityType.Object,
        model_point=191,
        short_move=True,
    )
    ForceAnimation(PLAYER, 8000)
    ForceAnimation(Objects.o5750_0001, 1)
    ForceAnimation(Objects.o5610_0000, 12)
    WaitFrames(130)
    IfFramesElapsed(0, 0)
    RunEvent(11515330, slot=1, args=(2, 3, Collisions.h0010B1_0000, 11510301, 11510303, 13, 360, 180))
    SkipLinesIfFinishedConditionFalse(7, 6)
    Move(
        PLAYER,
        destination=Objects.o5750_0004,
        destination_type=CoordEntityType.Object,
        model_point=191,
        short_move=True,
    )
    ForceAnimation(PLAYER, 8000)
    ForceAnimation(Objects.o5750_0004, 1)
    ForceAnimation(Objects.o5610_0000, 12)
    WaitFrames(130)
    IfFramesElapsed(0, 0)
    RunEvent(11515320, slot=8, args=(2, Collisions.h0010B1_0002, Collisions.h0010B1_0001, 11510301, 11510302, 360))
    IfFlagOff(0, 11515300)
    Restart()
    DisplayDialog(
        10010170,
        anchor_entity=-1,
        display_distance=3.0,
        button_type=ButtonType.OK_or_Cancel,
        number_buttons=NumberButtons.NoButton,
    )
    Restart()


def Event11510319():
    """ 11510319: Event 11510319 """
    DisableNetworkSync()
    IfCharacterInsideRegion(0, PLAYER, region=Boxes.RotatingBridgeCutsceneTrigger)
    EnableFlag(11510304)
    IfCharacterOutsideRegion(0, PLAYER, region=Boxes.RotatingBridgeCutsceneTrigger)
    DisableFlag(11510304)
    Restart()


def Event11515320(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int, arg_20_23: int):
    """ 11515320: Event 11515320 """
    DisableCollision(arg_4_7)
    EnableObject(Objects.o5611_0000)
    ForceAnimation(Objects.o5610_0000, arg_0_3)
    ForceAnimation(Objects.o5611_0000, arg_0_3)
    WaitFrames(arg_20_23)
    IfTimeElapsed(0, 0.0)
    DisableObject(Objects.o5611_0000)
    EnableCollision(arg_8_11)
    DisableFlag(arg_12_15)
    EnableFlag(arg_16_19)
    EnableFlag(11515301)
    SkipLinesIfSingleplayer(1)
    Wait(2.0)
    DisableFlag(11515300)


def Event11515330(
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
    """ 11515330: Event 11515330 """
    DisableCollision(Collisions.h0010B1_0002)
    DisableCollision(Collisions.h0010B1_0001)
    DisableCollision(Collisions.h0010B1_0000)
    EnableObject(Objects.o5611_0000)
    ForceAnimation(Objects.o5610_0000, arg_0_3)
    ForceAnimation(Objects.o5611_0000, arg_0_3)
    WaitFrames(arg_24_27)
    IfTimeElapsed(0, 0.0)
    ForceAnimation(Objects.o5610_0000, arg_20_23)
    WaitFrames(130)
    IfTimeElapsed(0, 0.0)
    ForceAnimation(Objects.o5610_0000, arg_4_7)
    ForceAnimation(Objects.o5611_0000, arg_4_7)
    WaitFrames(arg_28_31)
    IfTimeElapsed(0, 0.0)
    DisableObject(Objects.o5611_0000)
    EnableCollision(arg_8_11)
    DisableFlag(arg_12_15)
    EnableFlag(arg_16_19)
    EnableFlag(11515301)
    SkipLinesIfSingleplayer(1)
    Wait(2.0)
    DisableFlag(11515300)


def Event11510340():
    """ 11510340: Event 11510340 """
    SkipLinesIfFlagOff(8, 11515300)
    EnableCollision(Collisions.h9000B1_0000)
    EnableNavmeshType(Navigation.Navmesh_RotatingBridge00, NavmeshType.Solid)
    EnableNavmeshType(Navigation.Navmesh_RotatingBridge01, NavmeshType.Solid)
    EnableNavmeshType(Navigation.Navmesh_RotatingBridge02, NavmeshType.Solid)
    EnableNavmeshType(Navigation.Navmesh_RotatingBridge03, NavmeshType.Solid)
    EnableNavmeshType(Navigation.Navmesh_RotatingBridge04, NavmeshType.Solid)
    IfFlagOff(0, 11515300)
    Restart()
    SkipLinesIfFlagOff(8, 11510303)
    EnableCollision(Collisions.h9000B1_0000)
    DisableNavmeshType(Navigation.Navmesh_RotatingBridge00, NavmeshType.Solid)
    EnableNavmeshType(Navigation.Navmesh_RotatingBridge01, NavmeshType.Solid)
    EnableNavmeshType(Navigation.Navmesh_RotatingBridge02, NavmeshType.Solid)
    EnableNavmeshType(Navigation.Navmesh_RotatingBridge03, NavmeshType.Solid)
    EnableNavmeshType(Navigation.Navmesh_RotatingBridge04, NavmeshType.Solid)
    IfFlagOn(0, 11515300)
    Restart()
    SkipLinesIfFlagOff(8, 11510302)
    DisableCollision(Collisions.h9000B1_0000)
    EnableNavmeshType(Navigation.Navmesh_RotatingBridge00, NavmeshType.Solid)
    DisableNavmeshType(Navigation.Navmesh_RotatingBridge01, NavmeshType.Solid)
    DisableNavmeshType(Navigation.Navmesh_RotatingBridge02, NavmeshType.Solid)
    DisableNavmeshType(Navigation.Navmesh_RotatingBridge03, NavmeshType.Solid)
    EnableNavmeshType(Navigation.Navmesh_RotatingBridge04, NavmeshType.Solid)
    IfFlagOn(0, 11515300)
    Restart()
    SkipLinesIfFlagOff(8, 11510301)
    EnableCollision(Collisions.h9000B1_0000)
    EnableNavmeshType(Navigation.Navmesh_RotatingBridge00, NavmeshType.Solid)
    EnableNavmeshType(Navigation.Navmesh_RotatingBridge01, NavmeshType.Solid)
    EnableNavmeshType(Navigation.Navmesh_RotatingBridge02, NavmeshType.Solid)
    DisableNavmeshType(Navigation.Navmesh_RotatingBridge03, NavmeshType.Solid)
    DisableNavmeshType(Navigation.Navmesh_RotatingBridge04, NavmeshType.Solid)
    IfFlagOn(0, 11515300)
    Restart()
    DisplayDialog(
        10010105,
        anchor_entity=-1,
        display_distance=3.0,
        button_type=ButtonType.OK_or_Cancel,
        number_buttons=NumberButtons.NoButton,
    )
    Restart()


def Event11510350():
    """ 11510350: Event 11510350 """
    IfHost(1)
    IfFlagOn(1, 11515301)
    IfFlagOn(1, 11510301)
    IfHost(2)
    IfFlagOn(2, 11515301)
    IfFlagOn(2, 11510302)
    IfHost(3)
    IfFlagOn(3, 11515301)
    IfFlagOn(3, 11510303)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    DisableFlag(11515301)
    RestartIfSingleplayer()
    SkipLinesIfFinishedConditionFalse(6, 1)
    EnableFlag(11510301)
    DisableFlag(11510302)
    DisableFlag(11510303)
    EndOfAnimation(Objects.o5610_0000, 51)
    EnableCollision(Collisions.h0010B1_0002)
    Restart()
    SkipLinesIfFinishedConditionFalse(6, 2)
    DisableFlag(11510301)
    EnableFlag(11510302)
    DisableFlag(11510303)
    EndOfAnimation(Objects.o5610_0000, 50)
    EnableCollision(Collisions.h0010B1_0001)
    Restart()
    DisableFlag(11510301)
    DisableFlag(11510302)
    EnableFlag(11510303)
    EndOfAnimation(Objects.o5610_0000, 53)
    EnableCollision(Collisions.h0010B1_0000)
    Restart()


def Event11510310():
    """ 11510310: Event 11510310 """
    DisableNetworkSync()
    IfFlagOn(1, 11510301)
    IfActionButton(
        1,
        prompt_text=10010502,
        anchor_entity=Objects.o5610_0000,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        model_point=102,
        trigger_attribute=TriggerAttribute.All,
    )
    IfFlagOn(2, 11510303)
    IfActionButton(
        2,
        prompt_text=10010502,
        anchor_entity=Objects.o5610_0000,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        model_point=104,
        trigger_attribute=TriggerAttribute.All,
    )
    IfFlagOff(-2, 11510305)
    IfFlagOn(-2, 11510303)
    IfConditionTrue(3, input_condition=-2)
    IfActionButton(
        3,
        prompt_text=10010501,
        anchor_entity=Objects.o5750_0001,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        model_point=192,
        trigger_attribute=TriggerAttribute.All,
    )
    IfFlagOff(-3, 11510305)
    IfFlagOff(-3, 11510303)
    IfConditionTrue(4, input_condition=-3)
    IfActionButton(
        4,
        prompt_text=10010501,
        anchor_entity=Objects.o5750_0002,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        model_point=192,
        trigger_attribute=TriggerAttribute.All,
    )
    IfFlagOff(-4, 11510305)
    IfFlagOn(-4, 11510301)
    IfConditionTrue(5, input_condition=-4)
    IfActionButton(
        5,
        prompt_text=10010501,
        anchor_entity=Objects.o5750_0003,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        model_point=192,
        trigger_attribute=TriggerAttribute.All,
    )
    IfFlagOff(-5, 11510305)
    IfFlagOn(-5, 11510302)
    IfConditionTrue(6, input_condition=-5)
    IfActionButton(
        6,
        prompt_text=10010501,
        anchor_entity=Objects.o5750_0004,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        model_point=192,
        trigger_attribute=TriggerAttribute.All,
    )
    IfFlagOn(7, 11515300)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(-1, input_condition=4)
    IfConditionTrue(-1, input_condition=5)
    IfConditionTrue(-1, input_condition=6)
    IfConditionTrue(-1, input_condition=7)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionTrue(2, 7)
    DisplayDialog(
        10010170,
        anchor_entity=-1,
        display_distance=3.0,
        button_type=ButtonType.OK_or_Cancel,
        number_buttons=NumberButtons.NoButton,
    )
    Restart()
    IfFlagOff(0, 11515300)
    Restart()


def Event11510400():
    """ 11510400: Event 11510400 """
    DisableMapPiece(1513401)
    SkipLinesIfThisEventOff(7)
    DisableSoundEvent(1513801)
    SetMapDrawParamSlot(15, slot=1)
    SetLockedCameraSlot(game_map=ANOR_LONDO, camera_slot=1)
    DisableMapPiece(1513400)
    EnableMapPiece(1513401)
    DisableObject(Objects.o5900_0000)
    End()
    EnableCharacter(Characters.c5310_0000)
    IfCharacterDead(1, Characters.c5310_0000)
    IfEntityWithinDistance(1, Characters.c5310_0000, PLAYER, radius=15.0)
    IfConditionTrue(0, input_condition=1)
    Wait(3.0)
    DisableSoundEvent(1513801)
    EnableFlag(743)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterHollow(-1, PLAYER)
    IfConditionTrue(1, input_condition=-1)
    IfPlayerCovenant(1, Covenant.PrincessGuard)
    SkipLinesIfConditionFalse(4, 1)
    BetrayCurrentCovenant()
    IncrementPvPSin()
    EnableFlag(742)
    SaveRequest()
    DisableFlag(120)
    SkipLinesIfFlagOn(2, 11510900)
    PlayCutscene(150110, skippable=True, fade_out=False, player_id=PLAYER)
    SkipLines(1)
    PlayCutscene(150111, skippable=True, fade_out=False, player_id=PLAYER)
    WaitFrames(1)
    SetMapDrawParamSlot(15, slot=1)
    SetLockedCameraSlot(game_map=ANOR_LONDO, camera_slot=1)
    DisableMapPiece(1513400)
    EnableMapPiece(1513401)
    DisableObject(Objects.o5900_0000)
    IfPlayerHasGood(2, 2510, including_box=False)
    EndIfConditionTrue(2)
    AwardItemLot(1090, host_only=True)


def Event11510401():
    """ 11510401: Event 11510401 """
    SkipLinesIfThisEventOff(2)
    DisableObject(Objects.o5900_0000)
    End()
    EnableObjectInvulnerability(Objects.o5900_0000)
    IfFlagOn(1, 11510400)
    IfEntityWithinDistance(1, Objects.o5900_0000, PLAYER, radius=15.0)
    IfHost(2)
    IfCharacterHasSpecialEffect(2, PLAYER, 2310)
    IfEntityWithinDistance(2, Objects.o5900_0000, PLAYER, radius=15.0)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    DisableObjectInvulnerability(Objects.o5900_0000)
    DestroyObject(Objects.o5900_0000)
    ForceAnimation(Objects.o5900_0000, 0)
    PlaySoundEffect(anchor_entity=Objects.o5900_0000, sound_type=SoundType.o_Object, sound_id=590000000)


@RestartOnRest
def Event11510450():
    """ 11510450: Event 11510450 """
    IfDoesNotHaveTAEEvent(0, Characters.c5320_0000, tae_event_id=600)
    IfHasTAEEvent(0, Characters.c5320_0000, tae_event_id=600)
    DisableCharacter(Characters.c5320_0000)
    Wait(1.0)
    SkipLinesIfFlagOn(2, 11515110)
    RunEvent(11515110, slot=0, args=(Spheres.GwyndolinWarpPoint00, 11515110))
    Restart()
    SkipLinesIfFlagOn(2, 11515111)
    RunEvent(11515110, slot=1, args=(Spheres.GwyndolinWarpPoint01, 11515111))
    Restart()
    SkipLinesIfFlagOn(2, 11515112)
    RunEvent(11515110, slot=2, args=(Spheres.GwyndolinWarpPoint02, 11515112))
    Restart()
    SkipLinesIfFlagOn(2, 11515113)
    RunEvent(11515110, slot=3, args=(Spheres.GwyndolinWarpPoint03, 11515113))
    Restart()
    SkipLinesIfFlagOn(2, 11515114)
    RunEvent(11515110, slot=4, args=(Spheres.GwyndolinWarpPoint04, 11515114))
    Restart()
    SkipLinesIfFlagOn(2, 11515115)
    RunEvent(11515110, slot=5, args=(Spheres.GwyndolinWarpPoint05, 11515115))
    Restart()
    SkipLinesIfFlagOn(2, 11515116)
    RunEvent(11515110, slot=6, args=(Spheres.GwyndolinWarpPoint06, 11515116))
    Restart()
    SkipLinesIfFlagOn(2, 11515117)
    RunEvent(11515110, slot=7, args=(Spheres.GwyndolinWarpPoint07, 11515117))
    Restart()
    SkipLinesIfFlagOn(2, 11515118)
    RunEvent(11515110, slot=8, args=(Spheres.GwyndolinWarpPoint08, 11515118))
    Restart()
    SkipLinesIfFlagOn(2, 11515119)
    RunEvent(11515110, slot=9, args=(Spheres.GwyndolinWarpPoint09, 11515119))
    Restart()
    SkipLinesIfFlagOn(2, 11515120)
    RunEvent(11515110, slot=10, args=(Spheres.GwyndolinWarpPoint10, 11515120))
    Restart()
    SkipLinesIfFlagOn(2, 11515121)
    RunEvent(11515110, slot=11, args=(Spheres.GwyndolinWarpPoint11, 11515121))
    Restart()
    SkipLinesIfFlagOn(2, 11515122)
    RunEvent(11515110, slot=12, args=(Spheres.GwyndolinWarpPoint12, 11515122))
    Restart()
    SkipLinesIfFlagOn(2, 11515123)
    RunEvent(11515110, slot=13, args=(Spheres.GwyndolinWarpPoint13, 11515123))
    Restart()
    SkipLinesIfFlagOn(2, 11515124)
    RunEvent(11515110, slot=14, args=(Spheres.GwyndolinWarpPoint14, 11515124))
    Restart()
    SkipLinesIfFlagOn(2, 11515125)
    RunEvent(11515110, slot=15, args=(Spheres.GwyndolinWarpPoint15, 11515125))
    Restart()
    SkipLinesIfFlagOn(2, 11515126)
    RunEvent(11515110, slot=16, args=(Spheres.GwyndolinWarpPoint16, 11515126))
    Restart()
    SkipLinesIfFlagOn(2, 11515127)
    RunEvent(11515110, slot=17, args=(Spheres.GwyndolinWarpPoint17, 11515127))
    Restart()
    SkipLinesIfFlagOn(2, 11515128)
    RunEvent(11515110, slot=18, args=(Spheres.GwyndolinWarpPoint18, 11515128))
    Restart()
    SkipLinesIfFlagOn(2, 11515129)
    RunEvent(11515110, slot=19, args=(Spheres.GwyndolinWarpPoint19, 11515129))
    Restart()
    SkipLinesIfFlagOn(2, 11515130)
    RunEvent(11515110, slot=20, args=(Spheres.GwyndolinWarpPoint20, 11515130))
    Restart()
    SkipLinesIfFlagOn(2, 11515131)
    RunEvent(11515110, slot=21, args=(Spheres.GwyndolinWarpPoint21, 11515131))
    Restart()
    SkipLinesIfFlagOn(2, 11515132)
    RunEvent(11515110, slot=22, args=(Spheres.GwyndolinWarpPoint22, 11515132))
    Restart()
    SkipLinesIfFlagOn(2, 11515133)
    RunEvent(11515110, slot=23, args=(Spheres.GwyndolinWarpPoint23, 11515133))
    Restart()
    SkipLinesIfFlagOn(2, 11515134)
    RunEvent(11515110, slot=24, args=(Spheres.GwyndolinWarpPoint24, 11515134))
    Restart()
    SkipLinesIfFlagOn(2, 11515135)
    RunEvent(11515110, slot=25, args=(Spheres.GwyndolinWarpPoint25, 11515135))
    Restart()
    SkipLinesIfFlagOn(2, 11515136)
    RunEvent(11515110, slot=26, args=(Spheres.GwyndolinWarpPoint26, 11515136))
    Restart()
    SkipLinesIfFlagOn(2, 11515137)
    RunEvent(11515110, slot=27, args=(Spheres.GwyndolinWarpPoint27, 11515137))
    Restart()
    SkipLinesIfFlagOn(2, 11515138)
    RunEvent(11515110, slot=28, args=(Spheres.GwyndolinWarpPoint28, 11515138))
    Restart()
    SkipLinesIfFlagOn(2, 11515139)
    RunEvent(11515110, slot=29, args=(Spheres.GwyndolinWarpPoint29, 11515139))
    Restart()


@UnknownRestart
def Event11515110(_, arg_0_3: int, arg_4_7: int):
    """ 11515110: Event 11515110 """
    Move(Characters.c5320_0000, destination=arg_0_3, destination_type=CoordEntityType.Region, short_move=True)
    EnableCharacter(Characters.c5320_0000)
    ReplanAI(Characters.c5320_0000)
    ForceAnimation(Characters.c5320_0000, 7000, wait_for_completion=True)
    EnableFlag(arg_4_7)
    SkipLinesIfFlagOff(2, 11515132)
    AICommand(Characters.c5320_0000, command_id=1, slot=0)
    ReplanAI(Characters.c5320_0000)


def Event11510230():
    """ 11510230: Event 11510230 """
    IfActionButton(0, prompt_text=10010100, anchor_entity=Boxes.PaintedWorldPrompt, anchor_type=CoordEntityType.Region)
    IfSingleplayer(1)
    IfHost(1)
    IfPlayerHasGood(1, 384, including_box=False)
    SkipLinesIfConditionTrue(3, 1)
    SkipLinesIfClient(1)
    DisplayDialog(
        10010170,
        anchor_entity=-1,
        display_distance=3.0,
        button_type=ButtonType.OK_or_Cancel,
        number_buttons=NumberButtons.NoButton,
    )
    Restart()
    PlayCutscene(
        150135,
        skippable=True,
        fade_out=False,
        player_id=PLAYER,
        move_to_region=m11_00_Boxes.ArrivalPointFromAnorLondo,
        move_to_map=PAINTED_WORLD,
    )
    WaitFrames(1)
    SetRespawnPoint(m11_00_SpawnPoints.SpawnPointArrival)
    SaveRequest()
    Restart()


def Event11510240():
    """ 11510240: Event 11510240 """
    EndIfClient()
    IfInsideMap(0, game_map=ANOR_LONDO)
    IfTimeElapsed(0, 5.0)
    IfFlagOff(2, 11515050)
    IfActionButton(
        2,
        prompt_text=10010200,
        anchor_entity=Characters.c2260_0000,
        anchor_type=CoordEntityType.Character,
        max_distance=7.0,
        model_point=-1,
    )
    IfConditionTrue(0, input_condition=2)
    SkipLinesIfSingleplayer(2)
    DisplayDialog(
        10010170,
        anchor_entity=-1,
        display_distance=3.0,
        button_type=ButtonType.OK_or_Cancel,
        number_buttons=NumberButtons.NoButton,
    )
    Restart()
    SkipLinesIfFlagOn(2, 11510400)
    PlayCutscene(
        150130,
        skippable=True,
        fade_out=False,
        player_id=PLAYER,
        move_to_region=m15_00_Boxes.ArrivalFromAnorLondo,
        move_to_map=SENS_FORTRESS,
    )
    SkipLines(1)
    PlayCutscene(
        150132,
        skippable=True,
        fade_out=False,
        player_id=PLAYER,
        move_to_region=m15_00_Boxes.ArrivalFromAnorLondo,
        move_to_map=SENS_FORTRESS,
    )
    WaitFrames(1)
    SetMapDrawParamSlot(15, slot=0)
    Restart()


def Event11515050():
    """ 11515050: Event 11515050 """
    SkipLinesIfThisEventOff(2)
    DisableCharacter(Characters.c2260_0000)
    End()
    DisableImmortality(Characters.c2260_0000)
    SetStandbyAnimationSettings(Characters.c2260_0000, standby_animation=9000)
    IfAttacked(-1, Characters.c2260_0000, attacker=PLAYER)
    IfFlagOn(-1, 11515050)
    IfConditionTrue(0, input_condition=-1)
    EnableFlag(11515050)
    ResetAnimation(Characters.c2260_0000, disable_interpolation=True)
    ForceAnimation(Characters.c2260_0000, 9060, wait_for_completion=True)
    DisableCharacter(Characters.c2260_0000)


def Event11510120():
    """ 11510120: Event 11510120 """
    DisableNetworkSync()
    EndIfClient()
    IfFlagOn(1, 743)
    IfFlagOn(1, 12)
    IfFlagOff(1, 11510900)
    IfFlagOn(1, 11510400)
    IfCharacterInsideRegion(-1, PLAYER, region=Boxes.AnorLondoPalaceArea)
    IfStandingOnCollision(-1, 1513405)
    IfStandingOnCollision(-1, 1513100)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    AddSpecialEffect(PLAYER, 4501)
    WaitFrames(10)
    Restart()


@RestartOnRest
def Event11510130():
    """ 11510130: Event 11510130 """
    SkipLinesIfFlagOn(5, 11510400)
    DisableCharacter(Characters.c0000_0012)
    DisableCharacter(Characters.c0000_0013)
    IfFlagOn(0, 11510400)
    EnableCharacter(Characters.c0000_0012)
    EnableCharacter(Characters.c0000_0013)
    DisableCharacter(Characters.c2410_0005)
    DisableCharacter(Characters.c5351_0000)
    DisableCharacter(Characters.c5351_0001)
    DisableCharacter(Characters.c2260_0003)
    DisableCharacter(Characters.c2260_0004)
    DisableCharacter(Characters.c2260_0005)
    DisableCharacter(Characters.c2260_0006)
    DisableCharacter(Characters.c2260_0007)
    DisableCharacter(Characters.c2260_0008)
    DisableCharacter(1510116)
    DisableCharacter(Characters.c2260_0010)
    DisableCharacter(Characters.c2260_0011)
    DisableCharacter(Characters.c2260_0012)
    DisableCharacter(Characters.c2870_0000)
    DisableCharacter(Characters.c2870_0001)
    DisableCharacter(Characters.c2870_0002)
    DisableCharacter(Characters.c2870_0003)
    DisableCharacter(Characters.c2870_0004)
    DisableCharacter(Characters.c2870_0005)
    DisableCharacter(1510406)
    DisableCharacter(1510407)
    DisableCharacter(Characters.c2870_0008)
    DisableCharacter(Characters.c2870_0009)
    DisableCharacter(1510410)
    DisableCharacter(1510411)
    DisableCharacter(Characters.c2870_0012)
    DisableCharacter(Characters.c2870_0013)
    EndIfFlagOn(1034)
    Move(
        Characters.c0000_0003,
        destination=Boxes.DarkmoonKnightArea,
        destination_type=CoordEntityType.Region,
        copy_draw_parent=Characters.c5351_0001,
    )
    SetNest(Characters.c0000_0003, Boxes.DarkmoonKnightArea)
    ResetStandbyAnimationSettings(Characters.c0000_0003)


def Event11510131():
    """ 11510131: Event 11510131 """
    EndIfClient()
    IfFlagOn(1, 11510400)
    IfInsideMap(1, game_map=ANOR_LONDO)
    IfHost(1)
    IfCharacterDead(1, PLAYER)
    IfConditionTrue(0, input_condition=1)
    SetRespawnPoint(SpawnPoints.SpawnPoint0)
    SaveRequest()


def Event11510140():
    """ 11510140: Event 11510140 """
    IfFlagOn(0, 11510900)
    MoveRemains(
        source_region=Boxes.GwyndolinBloodstainMoveSource,
        destination_region=Boxes.GwyndolinBloodstainMoveDestination,
    )


def Event11510150():
    """ 11510150: Event 11510150 """
    DisableNetworkSync()
    IfHost(1)
    IfPlayerHasGood(1, 115, including_box=False)
    IfCharacterInsideRegion(1, PLAYER, region=Boxes.LautrecBlackEyeOrbTrigger)
    IfConditionTrue(0, input_condition=1)
    End()


def Event11510460():
    """ 11510460: Event 11510460 """
    IfFlagOn(-7, 11510593)
    IfCharacterHuman(-7, PLAYER)
    IfCharacterHollow(-7, PLAYER)
    IfConditionTrue(1, input_condition=-7)
    IfFlagOff(1, 11515352)
    IfFlagOff(1, 11515350)
    IfFlagOff(1, 743)
    IfFlagOn(1, 1240)
    IfActionButton(
        1,
        prompt_text=10010210,
        anchor_entity=Boxes.GwyndolinKneelPrompt,
        anchor_type=CoordEntityType.Region,
    )
    IfConditionTrue(2, input_condition=-7)
    IfFlagOn(2, 11515352)
    IfFlagOff(2, 11515350)
    IfConditionTrue(3, input_condition=-7)
    IfFlagOn(3, 11515352)
    IfFlagOn(3, 11515350)
    IfHost(3)
    IfCharacterOutsideRegion(3, PLAYER, region=Boxes.GwynevereKneelPrompt)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionFalse(10, 1)
    AddSpecialEffect(PLAYER, 4170)
    SkipLinesIfClient(1)
    RotateToFaceEntity(PLAYER, Boxes.GwyndolinFogRotationTarget)
    EnableFlag(11515350)
    SkipLinesIfHost(1)
    SkipLinesIfThisEventOff(1)
    ForceAnimation(PLAYER, 7895, wait_for_completion=True)
    ForceAnimation(PLAYER, 7896, loop=True)
    EnableFlag(11515352)
    Restart()
    CancelSpecialEffect(PLAYER, 4170)
    DisableFlag(11515350)
    SkipLinesIfHost(1)
    SkipLinesIfThisEventOff(2)
    SkipLinesIfFinishedConditionTrue(1, 3)
    ForceAnimation(PLAYER, 7897, wait_for_completion=True)
    DisableFlag(11515352)
    Restart()


def Event11510462():
    """ 11510462: Event 11510462 """
    DisableNetworkSync()
    WaitFrames(2)
    EnableFlag(11510460)


@RestartOnRest
def Event11510860(_, arg_0_3: int, arg_4_7: int):
    """ 11510860: Event 11510860 """
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


def Event11510461():
    """ 11510461: Event 11510461 """
    IfFlagOn(0, 11515351)
    AddSpecialEffect(PLAYER, 4170)
    RotateToFaceEntity(PLAYER, Characters.c5310_0000)
    ForceAnimation(PLAYER, 7895, wait_for_completion=True)
    ForceAnimation(PLAYER, 7896, loop=True)
    IfFlagOff(0, 11515351)
    CancelSpecialEffect(PLAYER, 4170)
    ForceAnimation(PLAYER, 7897, wait_for_completion=True)
    Restart()


def Event11510600(_, arg_0_3: int, arg_4_7: int):
    """ 11510600: Event 11510600 """
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
def Event11515200(_, arg_0_3: int):
    """ 11515200: Event 11515200 """
    IfHealthGreaterThan(1, arg_0_3, 0.0)
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
def Event11515210(_, arg_0_3: int):
    """ 11515210: Event 11515210 """
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
def Event11515220(_, arg_0_3: int):
    """ 11515220: Event 11515220 """
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
def Event11515230(_, arg_0_3: int):
    """ 11515230: Event 11515230 """
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
def Event11515240(_, arg_0_3: int, arg_4_7: int):
    """ 11515240: Event 11515240 """
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
def Event11510850(_, arg_0_3: int):
    """ 11510850: Event 11510850 """
    SkipLinesIfThisEventSlotOff(2)
    DisableCharacter(arg_0_3)
    End()
    IfCharacterDead(0, arg_0_3)
    End()


@RestartOnRest
def Event11515190(_, arg_0_3: int):
    """ 11515190: Event 11515190 """
    EndIfHost()
    IfCharacterBackreadDisabled(1, arg_0_3)
    EndIfConditionTrue(1)
    ResetAnimation(arg_0_3, disable_interpolation=True)
    ForceAnimation(arg_0_3, 0)
    ReplanAI(arg_0_3)


@RestartOnRest
def Event11515250():
    """ 11515250: Event 11515250 """
    EndIfThisEventOn()
    DisableAI(Characters.c2400_0010)
    IfCharacterInsideRegion(1, PLAYER, region=Boxes.PaintingGuardianAmbushTrigger)
    IfAttacked(2, Characters.c2400_0010, attacker=PLAYER)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionTrue(1, 2)
    ForceAnimation(Characters.c2400_0010, 500)
    EnableAI(Characters.c2400_0010)


@RestartOnRest
def Event11515251():
    """ 11515251: Event 11515251 """
    EndIfThisEventOn()
    DisableAI(Characters.c2410_0001)
    IfCharacterInsideRegion(-1, PLAYER, region=Boxes.SilverKnightDriveReactionArea)
    IfAttacked(-1, Characters.c2410_0001, attacker=PLAYER)
    IfEntityWithinDistance(-1, Characters.c2410_0001, PLAYER, radius=4.0)
    IfConditionTrue(0, input_condition=-1)
    EnableAI(Characters.c2410_0001)


def Event11510215():
    """ 11510215: Event 11510215 """
    SkipLinesIfThisEventOff(2)
    DisableObject(Objects.o5740_0000)
    End()
    IfObjectDestroyed(0, Objects.o5740_0000)
    End()


def Event11510510(_, arg_0_3: int, arg_4_7: int):
    """ 11510510: Event 11510510 """
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


def Event11510520(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11510520: Event 11510520 """
    SkipLinesIfThisEventSlotOff(2)
    DropMandatoryTreasure(arg_0_3)
    End()
    IfHealthLessThanOrEqual(0, arg_0_3, 0.0)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)


def Event11510501(_, arg_0_3: int, arg_4_7: int):
    """ 11510501: Event 11510501 """
    IfFlagOn(-2, 1030)
    IfFlagOn(-2, 1031)
    IfFlagOn(-2, 1036)
    IfConditionTrue(1, input_condition=-2)
    IfHealthLessThanOrEqual(1, arg_0_3, 0.8999999761581421)
    IfHealthGreaterThan(1, arg_0_3, 0.0)
    IfAttacked(1, arg_0_3, attacker=PLAYER)
    IfThisEventOff(1)
    IfFlagOff(2, 1034)
    IfFlagOn(-3, 1232)
    IfFlagOn(-3, 1241)
    IfFlagOn(-3, 1242)
    IfConditionTrue(2, input_condition=-3)
    IfCharacterBackreadEnabled(2, arg_0_3)
    IfThisEventOff(2)
    IfFlagOn(3, arg_4_7)
    IfThisEventOn(3)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EnableFlag(arg_4_7)
    EnableCharacter(arg_0_3)
    SetTeamTypeAndExitStandbyAnimation(arg_0_3, TeamType.HostileAlly)
    SaveRequest()


def Event11510502(_, arg_0_3: int, arg_4_7: int):
    """ 11510502: Event 11510502 """
    IfFlagOn(1, 1240)
    IfFlagOn(-2, 1232)
    IfFlagOn(-2, 11515382)
    IfConditionTrue(1, input_condition=-2)
    IfCharacterAlive(1, arg_0_3)
    IfFlagOn(2, arg_4_7)
    IfThisEventOn(2)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EnableFlag(arg_4_7)
    SetTeamType(arg_0_3, TeamType.Boss)


def Event11510530(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11510530: Event 11510530 """
    IfFlagOff(1, 1004)
    IfFlagOn(1, 1001)
    IfFlagOn(1, 11010590)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)
    EnableCharacter(arg_0_3)


def Event11510531(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11510531: Event 11510531 """
    IfFlagOff(1, 1033)
    IfFlagOn(1, 1030)
    IfFlagOn(1, 710)
    IfCharacterAlive(1, arg_0_3)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)


def Event11510532(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11510532: Event 11510532 """
    IfFlagOff(1, 1033)
    IfFlagOn(-1, 1030)
    IfFlagOn(-1, 1036)
    IfConditionTrue(1, input_condition=-1)
    IfFlagOn(1, 711)
    IfFlagOn(1, 712)
    IfFlagOn(1, 713)
    IfFlagOn(1, 714)
    IfCharacterAlive(1, arg_0_3)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)


def Event11510533(_, arg_0_3: int):
    """ 11510533: Event 11510533 """
    EndIfThisEventOn()
    IfCharacterDead(0, arg_0_3)
    EnableFlag(151)


def Event11510535(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11510535: Event 11510535 """
    IfFlagOff(1, 1512)
    IfFlagOn(1, 1493)
    IfCharacterDead(1, Characters.c2410_0009)
    IfCharacterDead(1, Characters.c2410_0014)
    IfCharacterDead(1, Characters.c2410_0015)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)
    EnableCharacter(arg_0_3)


def Event11510536(_, arg_0_3: int):
    """ 11510536: Event 11510536 """
    IfHost(1)
    IfFlagOff(1, 1512)
    IfFlagOn(1, 1494)
    IfFlagOn(1, 11510590)
    SkipLinesIfThisEventOn(1)
    IfCharacterBackreadDisabled(1, arg_0_3)
    IfConditionTrue(0, input_condition=1)
    DisableCharacter(arg_0_3)


def Event11510541(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11510541: Event 11510541 """
    IfFlagOn(-1, 1572)
    IfFlagOn(-1, 1573)
    IfFlagOn(-1, 1577)
    IfConditionTrue(1, input_condition=-1)
    IfFlagOn(1, 11510700)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)
    SetTeamType(Characters.c0000_0009, TeamType.WhitePhantom)
    SetTeamType(Characters.c0000_0010, TeamType.WhitePhantom)
    DisableAI(arg_0_3)
    DisableAI(Characters.c0000_0009)
    DisableAI(Characters.c0000_0010)
    IfFlagOn(-1, 11510598)
    IfAttacked(-1, arg_0_3, attacker=PLAYER)
    IfAttacked(-1, Characters.c0000_0009, attacker=PLAYER)
    IfAttacked(-1, Characters.c0000_0010, attacker=PLAYER)
    IfConditionTrue(0, input_condition=-1)
    EnableAI(arg_0_3)
    EnableAI(Characters.c0000_0009)
    EnableAI(Characters.c0000_0010)


def Event11510542(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11510542: Event 11510542 """
    IfHealthLessThanOrEqual(0, arg_0_3, 0.0)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)
    EnableFlag(8102)


def Event11510543(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11510543: Event 11510543 """
    DisableObject(Objects.o5870_0000)
    DeleteVFX(VFX.LautrecInvasionFog1, erase_root_only=False)
    DisableObject(Objects.o5871_0000)
    DeleteVFX(VFX.LautrecInvasionFog2, erase_root_only=False)
    DisableObject(Objects.o5869_0000)
    DeleteVFX(VFX.LautrecInvasionFog3, erase_root_only=False)
    IfFlagOn(0, 11510700)
    EnableObject(Objects.o5870_0000)
    CreateVFX(VFX.LautrecInvasionFog1)
    EnableObject(Objects.o5871_0000)
    CreateVFX(VFX.LautrecInvasionFog2)
    EnableObject(Objects.o5869_0000)
    CreateVFX(VFX.LautrecInvasionFog3)
    DisableFlag(8104)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)
    DisableCharacter(Characters.c2870_0012)
    DisableCharacter(Characters.c2870_0013)
    DisableCharacter(Characters.c2410_0005)
    EnableCharacter(arg_0_3)
    EnableCharacter(Characters.c0000_0009)
    EnableCharacter(Characters.c0000_0010)
    SkipLinesIfFlagOn(2, 8101)
    EnableFlag(8101)
    End()
    EnableFlag(8100)


def Event11510544(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11510544: Event 11510544 """
    SkipLinesIfThisEventOff(2)
    EnableTreasure(Objects.o0500_0008)
    End()
    DisableObject(Objects.o0500_0008)
    DisableTreasure(Objects.o0500_0008)
    IfHost(1)
    IfFlagOff(1, 11510700)
    IfFlagOn(1, 8102)
    IfConditionTrue(0, input_condition=1)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterHollow(-1, PLAYER)
    SkipLinesIfConditionFalse(3, -1)
    AwardItemLot(2060, host_only=True)
    AwardItemLot(6300, host_only=True)
    RemoveGoodFromPlayer(115)
    EnableObject(Objects.o0500_0008)
    EnableTreasure(Objects.o0500_0008)
    DisableCharacter(arg_0_3)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)


def Event151():
    """ 151: Event 151 """
    DisableNetworkSync()
    IfThisEventOn(1)
    IfActionButton(
        1,
        prompt_text=10010182,
        anchor_entity=Objects.o0200_0000,
        anchor_type=CoordEntityType.Object,
        max_distance=3.4000000953674316,
        model_point=-1,
    )
    IfConditionTrue(0, input_condition=1)
    DisplayDialog(
        10010184,
        anchor_entity=Objects.o0200_0000,
        display_distance=3.4000000953674316,
        button_type=ButtonType.Yes_or_No,
        number_buttons=NumberButtons.NoButton,
    )
    Restart()


@RestartOnRest
def Event11515090(_, arg_0_3: int):
    """ 11515090: Event 11515090 """
    IfHasTAEEvent(0, arg_0_3, tae_event_id=500)
    EzstateAIRequest(arg_0_3, command_id=1500, slot=0)
    IfDoesNotHaveTAEEvent(0, arg_0_3, tae_event_id=500)
    Restart()


@RestartOnRest
def Event11515091(_, arg_0_3: int):
    """ 11515091: Event 11515091 """
    DisableNetworkSync()
    IfHasTAEEvent(0, arg_0_3, tae_event_id=1400)
    Wait(10.0)
    EzstateAIRequest(arg_0_3, command_id=1501, slot=0)
    Restart()


@RestartOnRest
def Event11515092(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11515092: Event 11515092 """
    EndIfFlagOn(arg_8_11)
    EndIfFlagOn(arg_12_15)
    DisableCharacterCollision(arg_0_3)
    DisableGravity(arg_0_3)
    EnableObjectInvulnerability(arg_4_7)
    IfFlagOn(-1, arg_8_11)
    IfFlagOn(-1, arg_12_15)
    IfConditionTrue(0, input_condition=-1)
    EnableCharacterCollision(arg_0_3)
    EnableGravity(arg_0_3)
    DisableObjectInvulnerability(arg_4_7)
    WaitFrames(1)
    DestroyObject(arg_4_7)
    PlaySoundEffect(anchor_entity=arg_4_7, sound_type=SoundType.o_Object, sound_id=596500000)


def Event11515030():
    """ 11515030: Event 11515030 """
    SkipLinesIfClient(1)
    SetNetworkUpdateAuthority(Characters.c0000_0011, UpdateAuthority.Forced)
    SkipLinesIfThisEventOff(1)
    DisableCharacter(Characters.c0000_0006)
    SkipLinesIfFlagOn(3, 11515034)
    IfClient(2)
    IfFlagOn(2, 11515031)
    SkipLinesIfConditionTrue(1, 2)
    DisableCharacter(Characters.c0000_0011)
    EndIfFlagOn(12)
    IfHost(1)
    IfCharacterHuman(1, PLAYER)
    IfFlagOn(-1, 1004)
    IfFlagOn(-1, 1005)
    IfFlagOn(-1, 1006)
    IfFlagOn(-1, 1010)
    IfFlagOn(-1, 1011)
    IfConditionFalse(1, input_condition=-1)
    IfCharacterBackreadEnabled(1, Characters.c0000_0011)
    IfEntityWithinDistance(1, Characters.c0000_0011, PLAYER, radius=30.0)
    IfConditionTrue(0, input_condition=1)
    PlaceSummonSign(
        SummonSignType.BlueEyeSign,
        Characters.c0000_0011,
        region=Points.SolaireSummonSign,
        summon_flag=11515031,
        dismissal_flag=11515034,
    )
    DisableCharacter(Characters.c0000_0006)
    IfFlagOn(0, 11515031)
    SetNest(Characters.c0000_0011, Boxes.SolaireSummonNest)


def Event11515990(_, arg_0_3: int, arg_4_7: int):
    """ 11515990: Event 11515990 """
    IfFlagOn(0, arg_0_3)
    EraseNPCSummonSign(summoned_character=arg_4_7)
    IfFlagOff(0, arg_0_3)
    Restart()


def Event11515029():
    """ 11515029: Event 11515029 """
    SkipLinesIfClient(1)
    SetNetworkUpdateAuthority(Characters.c0000_0011, UpdateAuthority.Forced)
    SkipLinesIfThisEventOff(1)
    DisableCharacter(Characters.c0000_0006)
    SkipLinesIfFlagOn(3, 11515034)
    IfClient(2)
    IfFlagOn(2, 11515031)
    SkipLinesIfConditionTrue(1, 2)
    DisableCharacter(Characters.c0000_0011)
    EndIfFlagOn(12)
    IfMultiplayerCount(1, arg1=4, arg2=3)
    IfHost(1)
    IfCharacterHuman(1, PLAYER)
    IfFlagOff(1, 11515031)
    IfFlagOff(1, 11515034)
    IfFlagOn(-1, 1004)
    IfFlagOn(-1, 1005)
    IfFlagOn(-1, 1006)
    IfFlagOn(-1, 1010)
    IfFlagOn(-1, 1011)
    IfConditionFalse(1, input_condition=-1)
    IfCharacterBackreadEnabled(1, Characters.c0000_0011)
    IfEntityWithinDistance(1, Characters.c0000_0011, PLAYER, radius=30.0)
    IfCharacterHasSpecialEffect(1, PLAYER, 28)
    IfConditionTrue(0, input_condition=1)
    PlaceSummonSign(
        SummonSignType.BlueEyeSign,
        Characters.c0000_0011,
        region=Points.SolaireSummonSign,
        summon_flag=11515031,
        dismissal_flag=11515034,
    )
    DisableCharacter(Characters.c0000_0006)
    IfFlagOn(0, 11515031)
    SetNest(Characters.c0000_0011, Boxes.SolaireSummonNest)


def Event11515032():
    """ 11515032: Event 11515032 """
    EndIfThisEventOn()
    IfFlagOn(1, 11515031)
    IfFlagOn(1, 11515393)
    IfConditionTrue(0, input_condition=1)
    AICommand(Characters.c0000_0011, command_id=10, slot=0)
    ReplanAI(Characters.c0000_0011)
    IfCharacterInsideRegion(0, Characters.c0000_0011, region=Boxes.OrnsteinSmoughFogPrompt)
    RotateToFaceEntity(Characters.c0000_0011, Boxes.OrnsteinSmoughFogRotationTarget)
    ForceAnimation(Characters.c0000_0011, 7410)
    AICommand(Characters.c0000_0011, command_id=-1, slot=0)
    ReplanAI(Characters.c0000_0011)


def Event11515033():
    """ 11515033: Event 11515033 """
    IfFlagOn(1, 11515031)
    IfFlagOff(1, 11515390)
    IfCharacterInsideRegion(1, PLAYER, region=Boxes.GwyndolinCorridor)
    IfConditionTrue(0, input_condition=1)
    AICommand(Characters.c0000_0011, command_id=8, slot=0)
    ReplanAI(Characters.c0000_0011)
    IfAllPlayersOutsideRegion(0, region=Boxes.GwyndolinCorridor)
    AICommand(Characters.c0000_0011, command_id=-1, slot=0)
    ReplanAI(Characters.c0000_0011)
    Restart()


def Event11515843(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11515843: Event 11515843 """
    IfFlagOn(1, 120)
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


def Event11515846(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 11515846: Event 11515846 """
    IfFlagOn(1, 120)
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
