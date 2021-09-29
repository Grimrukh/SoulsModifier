"""
linked:


strings:

"""
from soulstruct.darksouls1r.events import *
from ..entities.m14_01_00_00_entities import *
from ..entities.m14_00_00_00_entities import Characters as m14_00_Characters
from ..entities.common_entities import *


def Constructor():
    """ 0: Event 0 """
    SkipLinesIfFlagOff(1, 10)
    RegisterBonfire(
        11410920,
        obj=Objects.o0200_0003,
        reaction_distance=2.0,
        reaction_angle=180.0,
        initial_kindle_level=0,
    )
    RegisterBonfire(
        11410992,
        obj=Objects.o0200_0004,
        reaction_distance=2.0,
        reaction_angle=180.0,
        initial_kindle_level=0,
    )
    RegisterBonfire(
        11410984,
        obj=Objects.o0200_0001,
        reaction_distance=2.0,
        reaction_angle=180.0,
        initial_kindle_level=0,
    )
    SkipLinesIfFlagOff(1, 11410900)
    RegisterBonfire(
        11410976,
        obj=Objects.o0200_0002,
        reaction_distance=2.0,
        reaction_angle=180.0,
        initial_kindle_level=0,
    )
    RegisterBonfire(
        11410968,
        obj=Objects.o0200_0005,
        reaction_distance=2.0,
        reaction_angle=180.0,
        initial_kindle_level=0,
    )
    RegisterBonfire(
        11410960,
        obj=Objects.o0200_0006,
        reaction_distance=2.0,
        reaction_angle=180.0,
        initial_kindle_level=0,
    )
    SkipLinesIfClient(14)
    DisableObject(Objects.o4966_0000)
    DeleteVFX(VFX.MultiplayerFog1, erase_root_only=False)
    DisableObject(Objects.o4967_0000)
    DeleteVFX(VFX.MultiplayerFog2, erase_root_only=False)
    DisableObject(Objects.o4968_0000)
    DeleteVFX(VFX.MultiplayerFog3, erase_root_only=False)
    DisableObject(Objects.o4969_0000)
    DeleteVFX(VFX.MultiplayerFog4, erase_root_only=False)
    DisableObject(Objects.o4970_0000)
    DeleteVFX(VFX.MultiplayerFog5, erase_root_only=False)
    DisableObject(Objects.o4971_0000)
    DeleteVFX(VFX.MultiplayerFog6, erase_root_only=False)
    DisableObject(Objects.o4973_0000)
    DeleteVFX(VFX.MultiplayerFog7, erase_root_only=False)
    SkipLinesIfFlagOff(3, 11410291)
    DisableObject(Objects.o4610_0000)
    DeleteVFX(VFX.BedSealRight, erase_root_only=True)
    DeleteVFX(VFX.BedSealRootLeft, erase_root_only=True)
    SkipLinesIfFlagOff(3, 11410292)
    DisableObject(Objects.o4610_0001)
    DeleteVFX(VFX.BedSealLeft, erase_root_only=True)
    DeleteVFX(VFX.BedSealRootRight, erase_root_only=True)
    RunEvent(11410095)
    RunEvent(11410800)
    RunEvent(11410400)
    RunEvent(11410340)
    RunEvent(11410341)
    RunEvent(11410350)
    RunEvent(11410360)
    RunEvent(11415399)
    RunEvent(11410260)
    RunEvent(11410200)
    RunEvent(11410201, slot=0, args=(Objects.o4620_0000, 462000000))
    RunEvent(11410201, slot=1, args=(Objects.o4621_0000, 462100000))
    RunEvent(11410201, slot=2, args=(Objects.o4622_0000, 462200000))
    RunEvent(11410201, slot=3, args=(Objects.o4623_0000, 462300000))
    RunEvent(11410201, slot=4, args=(Objects.o4624_0000, 462400000))
    RunEvent(11410201, slot=5, args=(Objects.o4625_0000, 462500000))
    RunEvent(11410201, slot=6, args=(Objects.o4626_0000, 462600000))
    RunEvent(11410201, slot=7, args=(Objects.o4627_0000, 462700000))
    RunEvent(11410201, slot=8, args=(Objects.o4628_0000, 462800000))
    RunEvent(11410201, slot=9, args=(Objects.o4629_0000, 462900000))
    RunEvent(11410201, slot=10, args=(Objects.o4630_0000, 463000000))
    RunEvent(11410201, slot=11, args=(Objects.o4631_0000, 463100000))
    RunEvent(11410201, slot=12, args=(Objects.o4632_0000, 463200000))
    RunEvent(11410250)
    DisableSoundEvent(1413801)
    SkipLinesIfFlagOff(4, 11410900)
    RunEvent(11415372)
    DisableObject(Objects.o4961_0000)
    DeleteVFX(VFX.CeaselessEntranceFog, erase_root_only=False)
    SkipLines(10)
    RunEvent(11415370)
    RunEvent(11415371)
    RunEvent(11415373)
    RunEvent(11415372)
    RunEvent(11415374)
    RunEvent(11415376)
    RunEvent(11415377)
    RunEvent(11415378)
    RunEvent(11415379)
    RunEvent(11410900)
    RunEvent(11415310, slot=0, args=(11415376,))
    RunEvent(11415310, slot=1, args=(11415310,))
    RunEvent(11415310, slot=2, args=(11415311,))
    RunEvent(11415310, slot=3, args=(11415312,))
    RunEvent(11415310, slot=4, args=(11415313,))
    DisableSoundEvent(1413803)
    SkipLinesIfFlagOff(6, 11410410)
    RunEvent(11415342)
    DisableObject(Objects.o4962_0000)
    DeleteVFX(VFX.FiresageEntranceFog, erase_root_only=False)
    DisableObject(Objects.o4963_0000)
    DeleteVFX(VFX.FiresageExitFog, erase_root_only=False)
    SkipLines(7)
    RunEvent(11415340)
    RunEvent(11415341)
    RunEvent(11415343)
    RunEvent(11415342)
    RunEvent(11415344)
    RunEvent(11410410)
    RunEvent(11415345)
    DisableSoundEvent(1413802)
    SkipLinesIfFlagOff(6, 11410901)
    RunEvent(11415382)
    DisableObject(Objects.o4964_0000)
    DeleteVFX(VFX.CentipedeEntranceFog, erase_root_only=False)
    DisableObject(Objects.o4965_0000)
    DeleteVFX(VFX.CentipedeExitFog, erase_root_only=False)
    SkipLines(7)
    RunEvent(11415380)
    RunEvent(11415381)
    RunEvent(11415383)
    RunEvent(11415382)
    RunEvent(11415384)
    RunEvent(11410901)
    RunEvent(11415386)
    DisableSoundEvent(1413800)
    SkipLinesIfFlagOff(4, 10)
    RunEvent(11415392)
    DisableObject(Objects.o4972_0000)
    DeleteVFX(VFX.BedOfChaosEntranceFog, erase_root_only=False)
    SkipLines(11)
    RunEvent(11415390)
    RunEvent(11415391)
    RunEvent(11415393)
    RunEvent(11415392)
    RunEvent(11410001)
    RunEvent(11415394)
    RunEvent(11415395)
    RunEvent(11415396)
    RunEvent(11415397)
    RunEvent(11415398)
    RunEvent(11415300)
    RunEvent(800, slot=0, args=(Characters.c3480_0000,))
    RunEvent(11410100, slot=4, args=(Characters.c3390_0007,))
    RunEvent(11410100, slot=6, args=(Characters.c0000_0010,))
    RunEvent(11410100, slot=7, args=(Characters.c3300_0000,))
    RunEvent(11410100, slot=8, args=(1410150,))
    RunEvent(11410100, slot=9, args=(Characters.c3421_0000,))
    RunEvent(11410100, slot=10, args=(Characters.c3421_0001,))
    RunEvent(11410100, slot=11, args=(Characters.c3421_0002,))
    RunEvent(11410100, slot=12, args=(Characters.c3421_0003,))
    RunEvent(11410100, slot=13, args=(Characters.c3421_0004,))
    RunEvent(11410100, slot=14, args=(Characters.c3421_0005,))
    RunEvent(11410100, slot=15, args=(Characters.c3421_0006,))
    RunEvent(11410100, slot=16, args=(Characters.c3421_0007,))
    RunEvent(11410100, slot=17, args=(Characters.c3421_0008,))
    RunEvent(11410100, slot=18, args=(Characters.c3421_0009,))
    RunEvent(11410100, slot=19, args=(Characters.c3421_0010,))
    RunEvent(11410100, slot=20, args=(Characters.c3421_0011,))
    RunEvent(11410100, slot=21, args=(Characters.c3421_0012,))
    RunEvent(11410100, slot=22, args=(Characters.c3421_0013,))
    RunEvent(11410100, slot=23, args=(Characters.c3421_0014,))
    RunEvent(11410100, slot=24, args=(Characters.c3421_0015,))
    RunEvent(11410100, slot=25, args=(Characters.c3421_0016,))
    RunEvent(11410100, slot=26, args=(Characters.c3421_0017,))
    RunEvent(11410100, slot=27, args=(Characters.c3421_0018,))
    RunEvent(11410100, slot=28, args=(Characters.c3421_0019,))
    RunEvent(11410100, slot=29, args=(Characters.c3421_0020,))
    RunEvent(11410100, slot=30, args=(Characters.c3421_0021,))
    RunEvent(11410100, slot=31, args=(Characters.c3421_0022,))
    RunEvent(11410100, slot=32, args=(Characters.c3421_0023,))
    RunEvent(11410100, slot=33, args=(Characters.c3421_0024,))
    RunEvent(11410100, slot=34, args=(Characters.c3421_0025,))
    RunEvent(11410100, slot=35, args=(Characters.c3421_0026,))
    RunEvent(11410100, slot=36, args=(Characters.c3421_0027,))
    RunEvent(11410100, slot=37, args=(Characters.c3421_0028,))
    RunEvent(11410100, slot=38, args=(Characters.c2250_0003,))
    RunEvent(11410100, slot=39, args=(Characters.c2250_0004,))
    RunEvent(11410100, slot=40, args=(Characters.c2250_0005,))
    RunEvent(11410100, slot=41, args=(Characters.c2250_0006,))
    RunEvent(11410100, slot=42, args=(Characters.c2250_0007,))
    RunEvent(11410100, slot=43, args=(Characters.c2250_0008,))
    RunEvent(11410100, slot=44, args=(Characters.c2250_0009,))
    RunEvent(11415210, slot=0, args=(11415250, 11415263, 11))
    RunEvent(
        11415250,
        slot=0,
        args=(
            Characters.c3210_0000,
            Characters.c3220_0000,
            Characters.c3220_0001,
            Characters.c3220_0002,
            Characters.c3220_0003,
            Characters.c3220_0004,
        ),
    )
    RunEvent(
        11415250,
        slot=1,
        args=(
            Characters.c3210_0001,
            Characters.c3220_0005,
            Characters.c3220_0006,
            Characters.c3220_0007,
            Characters.c3220_0008,
            Characters.c3220_0009,
        ),
    )
    RunEvent(
        11415250,
        slot=2,
        args=(
            Characters.c3210_0002,
            Characters.c3220_0010,
            Characters.c3220_0011,
            Characters.c3220_0012,
            Characters.c3220_0013,
            Characters.c3220_0014,
        ),
    )
    RunEvent(
        11415250,
        slot=3,
        args=(
            Characters.c3210_0003,
            Characters.c3220_0015,
            Characters.c3220_0016,
            Characters.c3220_0017,
            Characters.c3220_0018,
            Characters.c3220_0019,
        ),
    )
    RunEvent(
        11415250,
        slot=4,
        args=(
            Characters.c3210_0004,
            Characters.c3220_0020,
            Characters.c3220_0021,
            Characters.c3220_0022,
            Characters.c3220_0023,
            Characters.c3220_0024,
        ),
    )
    RunEvent(
        11415250,
        slot=5,
        args=(
            Characters.c3210_0005,
            Characters.c3220_0025,
            Characters.c3220_0026,
            Characters.c3220_0027,
            Characters.c3220_0028,
            Characters.c3220_0029,
        ),
    )
    RunEvent(
        11415250,
        slot=6,
        args=(
            Characters.c3210_0006,
            Characters.c3220_0030,
            Characters.c3220_0031,
            Characters.c3220_0032,
            Characters.c3220_0033,
            Characters.c3220_0034,
        ),
    )
    RunEvent(
        11415250,
        slot=7,
        args=(
            Characters.c3210_0007,
            Characters.c3220_0035,
            Characters.c3220_0036,
            Characters.c3220_0037,
            Characters.c3220_0038,
            Characters.c3220_0039,
        ),
    )
    RunEvent(
        11415250,
        slot=8,
        args=(
            Characters.c3210_0008,
            Characters.c3220_0040,
            Characters.c3220_0041,
            Characters.c3220_0042,
            Characters.c3220_0043,
            Characters.c3220_0044,
        ),
    )
    RunEvent(
        11415250,
        slot=9,
        args=(
            Characters.c3210_0009,
            Characters.c3220_0045,
            Characters.c3220_0046,
            Characters.c3220_0047,
            Characters.c3220_0048,
            Characters.c3220_0049,
        ),
    )
    RunEvent(
        11415250,
        slot=10,
        args=(
            Characters.c3210_0010,
            Characters.c3220_0050,
            Characters.c3220_0051,
            Characters.c3220_0052,
            Characters.c3220_0053,
            Characters.c3220_0054,
        ),
    )
    RunEvent(
        11415250,
        slot=11,
        args=(
            Characters.c3210_0011,
            Characters.c3220_0055,
            Characters.c3220_0056,
            Characters.c3220_0057,
            Characters.c3220_0058,
            Characters.c3220_0059,
        ),
    )
    RunEvent(
        11415250,
        slot=12,
        args=(
            Characters.c3210_0012,
            Characters.c3220_0060,
            Characters.c3220_0061,
            Characters.c3220_0062,
            Characters.c3220_0063,
            Characters.c3220_0064,
        ),
    )
    RunEvent(
        11415250,
        slot=13,
        args=(
            Characters.c3210_0013,
            Characters.c3220_0065,
            Characters.c3220_0066,
            Characters.c3220_0067,
            Characters.c3220_0068,
            Characters.c3220_0069,
        ),
    )
    RunEvent(11415100, slot=0, args=(Characters.c3390_0001, Characters.c3390_0001, 9060, 15.0, 0.0), arg_types="iiiff")
    RunEvent(11415100, slot=1, args=(Characters.c3390_0002, Characters.c3390_0002, 9060, 10.0, 0.0), arg_types="iiiff")
    RunEvent(11415100, slot=2, args=(Characters.c3390_0007, Characters.c3390_0007, 9060, 15.0, 0.0), arg_types="iiiff")
    RunEvent(
        11415120,
        slot=0,
        args=(10000, Characters.c3390_0003, 9060, Boxes.CeilingRockwormTrigger, 0.30000001192092896),
        arg_types="iiiif",
    )
    RunEvent(
        11415120,
        slot=1,
        args=(10000, Characters.c3390_0004, 9060, Boxes.CeilingRockwormTrigger, 0.10000000149011612),
        arg_types="iiiif",
    )
    RunEvent(
        11415120,
        slot=2,
        args=(10000, Characters.c3390_0005, 9060, Boxes.CeilingRockwormTrigger, 0.0),
        arg_types="iiiif",
    )
    RunEvent(
        11415120,
        slot=3,
        args=(10000, Characters.c3390_0006, 9060, Boxes.CeilingRockwormTrigger, 0.20000000298023224),
        arg_types="iiiif",
    )
    RunEvent(11410150, slot=1, args=(Characters.c3390_0001, 33900000))
    RunEvent(11410150, slot=2, args=(Characters.c3390_0002, 33900000))
    RunEvent(11410150, slot=3, args=(Characters.c3390_0003, 33900000))
    RunEvent(11410150, slot=4, args=(Characters.c3390_0004, 33900000))
    RunEvent(11410150, slot=5, args=(Characters.c3390_0005, 33900000))
    RunEvent(11410150, slot=6, args=(Characters.c3390_0006, 33900000))
    RunEvent(11410600, slot=0, args=(Objects.o0110_0000, 11410600))
    RunEvent(11410600, slot=1, args=(Objects.o0110_0001, 11410601))
    RunEvent(11410600, slot=2, args=(Objects.o0110_0002, 11410602))
    RunEvent(11410600, slot=3, args=(Objects.o0110_0003, 11410603))
    RunEvent(11415843, slot=0, args=(10, Objects.o4972_0000, Boxes.BedFogPrompt, Boxes.BedFogRotationTarget))
    RunEvent(11415846, slot=0, args=(10, Objects.o4972_0000, VFX.BedOfChaosEntranceFog))
    RunEvent(
        11415843,
        slot=1,
        args=(11410900, Objects.o4961_0000, Boxes.CeaselessFogPrompt, Boxes.CeaselessFogRotationTarget),
    )
    RunEvent(11415846, slot=1, args=(11410900, Objects.o4961_0000, VFX.CeaselessEntranceFog))
    RunEvent(
        11415843,
        slot=2,
        args=(11410901, Objects.o4964_0000, Boxes.CentipedeFogPrompt, Boxes.CentipedeFogRotationTarget),
    )
    RunEvent(11415846, slot=2, args=(11410901, Objects.o4964_0000, VFX.CentipedeEntranceFog))
    RunEvent(
        11415843,
        slot=3,
        args=(11410410, Objects.o4962_0000, Boxes.FiresageDemonFogPrompt, Boxes.FiresageDemonFogRotationTarget),
    )
    RunEvent(11415846, slot=3, args=(11410410, Objects.o4962_0000, VFX.FiresageEntranceFog))
    # <!--!>


def Preconstructor():
    """ 50: Event 50 """
    RunEvent(11410100, slot=0, args=(Characters.c3240_0002,))
    RunEvent(11410100, slot=1, args=(Characters.c3240_0003,))
    RunEvent(11410100, slot=2, args=(Characters.c3240_0004,))
    RunEvent(11410100, slot=3, args=(Characters.c3240_0005,))
    HumanityRegistration(Characters.c0000_0010, 8250)
    HumanityRegistration(Characters.c0000_0007, 8310)
    HumanityRegistration(Characters.c0000_0008, 8956)
    HumanityRegistration(Characters.c0000_0009, 8956)
    RunEvent(11415030)
    RunEvent(11415029)
    RunEvent(11415032)
    RunEvent(11415035)
    RunEvent(11415038)
    RunEvent(11410810, slot=0, args=(Characters.c0000_0008, 11415036, 11415037))
    RunEvent(11410810, slot=1, args=(Characters.c0000_0009, 11415039, 11415040))
    RunEvent(14015990, slot=0, args=(11415031, Characters.c0000_0007))
    HumanityRegistration(Characters.c0000_0002, 8310)
    HumanityRegistration(Characters.c0000_0003, 8310)
    SkipLinesIfFlagOn(3, 1009)
    SkipLinesIfFlagOn(2, 1004)
    SkipLinesIfFlagOn(1, 1003)
    DisableCharacter(Characters.c0000_0002)
    SkipLinesIfFlagOn(1, 11410580)
    SkipLines(1)
    Move(
        Characters.c0000_0002,
        destination=Boxes.SolaireSaved,
        destination_type=CoordEntityType.Region,
        set_draw_parent=Collisions.h0042B1,
    )
    SkipLinesIfFlagOn(1, 1002)
    DisableCharacter(Characters.c0000_0003)
    SetTeamTypeAndExitStandbyAnimation(Characters.c0000_0003, TeamType.HostileAlly)
    RunEvent(11410510, slot=0, args=(Characters.c0000_0002, 1004))
    RunEvent(11410520, slot=0, args=(Characters.c0000_0002, 1000, 1029, 1005))
    RunEvent(11410530, slot=0, args=(Characters.c0000_0002, 1000, 1029, 1009))
    RunEvent(11410531, slot=0, args=(Characters.c0000_0002, 1000, 1029, 1002))
    RunEvent(11410532, slot=0, args=(Characters.c0000_0002, 1000, 1029, 1003))
    RunEvent(11410533, slot=0, args=(6006, 1000, 1029, 1012))
    RunEvent(11410534, slot=0, args=(Characters.c0000_0003, 1000, 1029, 1011))
    HumanityRegistration(Characters.c0000_0005, 8446)
    SkipLinesIfFlagRangeAnyOn(1, (1503, 1507))
    DisableCharacter(Characters.c0000_0005)
    SkipLinesIfFlagOn(3, 1504)
    SkipLinesIfFlagOn(2, 1506)
    SkipLinesIfFlagOn(1, 1507)
    SkipLines(2)
    AddSpecialEffect(Characters.c0000_0005, 90111)
    Move(
        Characters.c0000_0005,
        destination=Boxes.SiegmeyerNestAfterBattle,
        destination_type=CoordEntityType.Region,
        short_move=True,
    )
    SkipLinesIfFlagOff(1, 11410593)
    SetStandbyAnimationSettings(Characters.c0000_0005, standby_animation=7855)
    RunEvent(11410501, slot=0, args=(Characters.c0000_0005, 1512))
    RunEvent(11410546, slot=0, args=(Characters.c0000_0005, 1490, 1514, 1513))
    RunEvent(11410540, slot=0, args=(Characters.c0000_0005, 1490, 1514, 1503))
    RunEvent(11410541, slot=0, args=(Characters.c0000_0005, 1490, 1514, 1504))
    RunEvent(11410542, slot=0, args=(Characters.c0000_0005, 1490, 1514, 1505))
    RunEvent(11410543, slot=0, args=(Characters.c0000_0005, 1490, 1514, 1506))
    RunEvent(11410544, slot=0, args=(Characters.c0000_0005, 1490, 1514, 1507))
    RunEvent(11410545, slot=0, args=(Characters.c0000_0005, 1490, 1514, 1513))
    RunEvent(11410549, slot=0, args=(Characters.c0000_0005,))
    RunEvent(11410550, slot=0, args=(Characters.c0000_0005, 1490, 1514, 1514))
    RunEvent(11410547, slot=0, args=(Characters.c0000_0005,))
    RunEvent(11410548, slot=0, args=(Characters.c0000_0005,))


def Event11410090(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11410090: Event 11410090 """
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


def Event11410095():
    """ 11410095: Event 11410095 """
    SkipLinesIfFlagOff(5, 11800100)
    EnableFlag(11410096)
    DisableObject(Objects.o4960_0000)
    DeleteVFX(VFX.GoldenFog, erase_root_only=False)
    DisableFlag(402)
    End()
    SkipLinesIfFlagOff(3, 11410096)
    DisableObject(Objects.o4960_0000)
    DeleteVFX(VFX.GoldenFog, erase_root_only=False)
    End()
    EndIfClient()
    IfActionButton(
        0,
        prompt_text=10010410,
        anchor_entity=Boxes.AtGoldenFog,
        anchor_type=CoordEntityType.Region,
        model_point=0,
        line_intersects=Objects.o4960_0000,
    )
    DisplayStatus(10010630, pad_enabled=True)
    Restart()


def Event11415390():
    """ 11415390: Event 11415390 """
    IfFlagOff(1, 10)
    IfActionButton(
        1,
        prompt_text=10010403,
        anchor_entity=Boxes.BedFogPrompt,
        anchor_type=CoordEntityType.Region,
        line_intersects=Objects.o4972_0000,
        boss_version=True,
    )
    IfConditionTrue(0, input_condition=1)
    RotateToFaceEntity(PLAYER, Boxes.BedFogRotationTarget)
    ForceAnimation(PLAYER, 7410)
    Restart()


def Event11415391():
    """ 11415391: Event 11415391 """
    DisableNetworkSync()
    IfFlagOff(1, 10)
    IfFlagOn(1, 11415393)
    IfCharacterType(1, PLAYER, CharacterType.WhitePhantom)
    IfActionButton(
        1,
        prompt_text=10010403,
        anchor_entity=Boxes.BedFogPrompt,
        anchor_type=CoordEntityType.Region,
        trigger_attribute=TriggerAttribute.All,
        line_intersects=Objects.o4972_0000,
    )
    IfConditionTrue(0, input_condition=1)
    RotateToFaceEntity(PLAYER, Boxes.BedFogRotationTarget)
    ForceAnimation(PLAYER, 7410)
    Restart()


def Event11415393():
    """ 11415393: Event 11415393 """
    SkipLinesIfThisEventOn(3)
    IfFlagOff(1, 10)
    IfCharacterInsideRegion(1, PLAYER, region=Boxes.BedOfChaosNotify)
    IfConditionTrue(0, input_condition=1)
    SkipLinesIfClient(1)
    NotifyBossBattleStart()
    ActivateMultiplayerBuffs(Characters.c5400_0000)


@RestartOnRest
def Event11415392():
    """ 11415392: Event 11415392 """
    SkipLinesIfFlagOff(7, 10)
    DisableCharacter(Characters.c5400_0000)
    DisableCharacter(Characters.c5230_0000)
    DisableCharacter(Characters.c5401_0000)
    Kill(Characters.c5400_0000, award_souls=False)
    Kill(Characters.c5230_0000, award_souls=False)
    Kill(Characters.c5401_0000, award_souls=False)
    End()
    SkipLinesIfFlagRangeAnyOn(1, (11410291, 11410292))
    DisableCharacter(Characters.c5400_0000)
    SkipLinesIfFlagRangeAllOff(1, (11410291, 11410292))
    ResetStandbyAnimationSettings(Characters.c5230_0000)
    EnableInvincibility(Characters.c5400_0000)
    EnableInvincibility(Characters.c5230_0000)
    DisableHealthBar(Characters.c5400_0000)
    DisableHealthBar(Characters.c5230_0000)
    DisableAI(Characters.c5230_0000)
    SetLockedCameraSlot(game_map=LOST_IZALITH, camera_slot=1)
    IfHost(1)
    IfCharacterInsideRegion(1, PLAYER, region=Boxes.BedOfChaosNotify)
    IfConditionTrue(0, input_condition=1)
    SkipLinesIfFlagRangeAnyOn(2, (11410291, 11410292))
    ResetStandbyAnimationSettings(Characters.c5230_0000)
    ForceAnimation(Characters.c5230_0000, 9060)
    EnableAI(Characters.c5230_0000)
    EnableBossHealthBar(Characters.c5401_0000, name=5400, slot=0)


def Event11410001():
    """ 11410001: Event 11410001 """
    DisableObject(Objects.o0200_0003)
    IfCharacterDead(0, Characters.c5401_0000)
    EnableFlag(10)
    KillBoss(1410800)
    SkipLinesIfClient(1)
    AwardAchievement(36)
    SetLockedCameraSlot(game_map=LOST_IZALITH, camera_slot=0)
    DisableObject(Objects.o4972_0000)
    DeleteVFX(VFX.BedOfChaosEntranceFog, erase_root_only=True)
    DisableNetworkSync()
    CreateTemporaryVFX(90014, anchor_entity=Objects.o0200_0003, anchor_type=CoordEntityType.Object, model_point=-1)
    Wait(2.0)
    EnableObject(Objects.o0200_0003)
    RegisterBonfire(
        11410920,
        obj=Objects.o0200_0003,
        reaction_distance=2.0,
        reaction_angle=180.0,
        initial_kindle_level=0,
    )


def Event11415394():
    """ 11415394: Event 11415394 """
    DisableNetworkSync()
    IfFlagOff(1, 10)
    IfFlagOn(1, 11415392)
    SkipLinesIfHost(1)
    IfFlagOn(1, 11415391)
    IfCharacterInsideRegion(1, PLAYER, region=Spheres.BedOfChaosMusic)
    IfConditionTrue(0, input_condition=1)
    EnableSoundEvent(1413800)


def Event11415395():
    """ 11415395: Event 11415395 """
    DisableNetworkSync()
    IfFlagOn(1, 10)
    IfFlagOn(1, 11415394)
    IfConditionTrue(0, input_condition=1)
    DisableSoundEvent(1413800)


@RestartOnRest
def Event11415396():
    """ 11415396: Event 11415396 """
    SkipLinesIfFlagRangeAnyOn(15, (11410291, 11410292))
    IfFlagOn(-1, 11410291)
    IfFlagOn(-1, 11410292)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFlagOn(6, 11410292)
    EnableFlag(11410005)
    SkipLinesIfMultiplayer(2)
    PlayCutscene(140116, skippable=True, fade_out=False, player_id=PLAYER)
    SkipLines(1)
    PlayCutscene(140116, skippable=False, fade_out=False, player_id=PLAYER)
    SkipLines(4)
    SkipLinesIfMultiplayer(2)
    PlayCutscene(140115, skippable=True, fade_out=False, player_id=PLAYER)
    SkipLines(1)
    PlayCutscene(140115, skippable=False, fade_out=False, player_id=PLAYER)
    WaitFrames(1)
    EnableCharacter(Characters.c5400_0000)
    IfFlagOn(1, 11410291)
    IfFlagOn(1, 11410292)
    IfConditionTrue(0, input_condition=1)
    AddSpecialEffect(Characters.c5400_0000, 5130)
    SkipLinesIfFlagOn(12, 11410000)
    SkipLinesIfFlagOff(5, 11410005)
    SkipLinesIfMultiplayer(2)
    PlayCutscene(140117, skippable=True, fade_out=False, player_id=PLAYER)
    SkipLines(1)
    PlayCutscene(140117, skippable=False, fade_out=False, player_id=PLAYER)
    SkipLines(4)
    SkipLinesIfMultiplayer(2)
    PlayCutscene(140118, skippable=True, fade_out=False, player_id=PLAYER)
    SkipLines(1)
    PlayCutscene(140118, skippable=False, fade_out=False, player_id=PLAYER)
    SetStandbyAnimationSettings(Characters.c5400_0000, standby_animation=10000)
    WaitFrames(1)
    EnableFlag(11410000)
    ResetStandbyAnimationSettings(Characters.c5400_0000)
    WaitFrames(1)
    ResetAnimation(Characters.c5400_0000, disable_interpolation=True)


@RestartOnRest
def Event11415397():
    """ 11415397: Event 11415397 """
    EnableInvincibility(Characters.c5401_0000)
    IfFlagOn(1, 11410291)
    IfFlagOn(1, 11410292)
    IfConditionTrue(0, input_condition=1)
    DisableInvincibility(Characters.c5401_0000)
    IfHealthLessThanOrEqual(0, Characters.c5401_0000, 0.0)
    DisableInvincibility(Characters.c5400_0000)
    DisableInvincibility(Characters.c5230_0000)
    Kill(Characters.c5400_0000, award_souls=True)
    Kill(Characters.c5230_0000, award_souls=False)


@RestartOnRest
def Event11415398():
    """ 11415398: Event 11415398 """
    IfFlagOn(-1, 11410291)
    IfFlagOn(-1, 11410292)
    IfConditionTrue(0, input_condition=-1)
    IfCharacterBackreadEnabled(0, Characters.c5400_0000)
    AICommand(Characters.c5400_0000, command_id=2, slot=0)
    ReplanAI(Characters.c5400_0000)
    AICommand(Characters.c5230_0000, command_id=2, slot=0)
    ReplanAI(Characters.c5230_0000)
    IfFlagOn(1, 11410291)
    IfFlagOn(1, 11410292)
    SkipLinesIfFlagOn(1, 11410000)
    IfFlagOn(1, 11415396)
    IfConditionTrue(0, input_condition=1)
    IfCharacterBackreadEnabled(0, Characters.c5400_0000)
    AICommand(Characters.c5400_0000, command_id=3, slot=0)
    ReplanAI(Characters.c5400_0000)
    AICommand(Characters.c5230_0000, command_id=3, slot=0)
    ReplanAI(Characters.c5230_0000)


def Event11415399():
    """ 11415399: Event 11415399 """
    DisableNetworkSync()
    IfCharacterInsideRegion(0, PLAYER, region=Boxes.BedSlideInvincibility)
    EnableInvincibility(PLAYER)
    IfCharacterOutsideRegion(0, PLAYER, region=Boxes.BedSlideInvincibility)
    Wait(3.0)
    DisableInvincibility(PLAYER)


def Event11415300():
    """ 11415300: Event 11415300 """
    EndIfFlagOn(10)
    SkipLinesIfThisEventOn(2)
    EnableFlag(11415300)
    EnableObjectInvulnerability(1411120)
    IfFlagOff(1, 11410291)
    IfObjectDestroyed(1, Objects.o4610_0000)
    IfFlagOff(2, 11410292)
    IfObjectDestroyed(2, Objects.o4610_0001)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfFlagOn(-1, 10)
    IfConditionTrue(0, input_condition=-1)
    EndIfFlagOn(10)
    SkipLinesIfFinishedConditionFalse(4, 1)
    EnableFlag(11410291)
    DeleteVFX(VFX.BedSealRight, erase_root_only=True)
    DeleteVFX(VFX.BedSealRootLeft, erase_root_only=True)
    Restart()
    EnableFlag(11410292)
    DeleteVFX(VFX.BedSealLeft, erase_root_only=True)
    DeleteVFX(VFX.BedSealRootRight, erase_root_only=True)
    Restart()


def Event11410200():
    """ 11410200: Event 11410200 """
    SkipLinesIfThisEventOff(6)
    DisableObject(Objects.o4633_0000)
    DisableObject(Objects.o4634_0000)
    DisableObject(Objects.o4635_0000)
    DisableObject(Objects.o4636_0000)
    DisableObject(Objects.o4637_0000)
    End()
    RestoreObject(Objects.o4633_0000)
    RestoreObject(Objects.o4634_0000)
    RestoreObject(Objects.o4635_0000)
    RestoreObject(Objects.o4636_0000)
    RestoreObject(Objects.o4637_0000)
    EnableObjectInvulnerability(Objects.o4633_0000)
    EnableObjectInvulnerability(Objects.o4634_0000)
    EnableObjectInvulnerability(Objects.o4635_0000)
    EnableObjectInvulnerability(Objects.o4636_0000)
    EnableObjectInvulnerability(Objects.o4637_0000)
    IfFlagOn(1, 11410291)
    IfFlagOn(1, 11410292)
    IfCharacterInsideRegion(1, PLAYER, region=Spheres.BedCentralFloorBreakTrigger)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(11410200)
    DisableObjectInvulnerability(Objects.o4633_0000)
    DisableObjectInvulnerability(Objects.o4634_0000)
    DisableObjectInvulnerability(Objects.o4635_0000)
    DisableObjectInvulnerability(Objects.o4636_0000)
    DisableObjectInvulnerability(Objects.o4637_0000)
    CreateTemporaryVFX(140009, anchor_entity=Objects.o4635_0000, anchor_type=CoordEntityType.Object, model_point=-1)
    DestroyObject(Objects.o4633_0000)
    PlaySoundEffect(anchor_entity=Objects.o4633_0000, sound_type=SoundType.o_Object, sound_id=463300000)
    WaitFrames(4)
    DestroyObject(Objects.o4634_0000)
    PlaySoundEffect(anchor_entity=Objects.o4634_0000, sound_type=SoundType.o_Object, sound_id=463400000)
    WaitFrames(3)
    DestroyObject(Objects.o4635_0000)
    PlaySoundEffect(anchor_entity=Objects.o4635_0000, sound_type=SoundType.o_Object, sound_id=463500000)
    WaitFrames(2)
    DestroyObject(Objects.o4636_0000)
    PlaySoundEffect(anchor_entity=Objects.o4636_0000, sound_type=SoundType.o_Object, sound_id=463600000)
    WaitFrames(1)
    DestroyObject(Objects.o4637_0000)
    PlaySoundEffect(anchor_entity=Objects.o4637_0000, sound_type=SoundType.o_Object, sound_id=463700000)
    DisableNetworkSync()
    Wait(10.0)
    DisableObject(Objects.o4633_0000)
    DisableObject(Objects.o4636_0000)
    DisableObject(Objects.o4637_0000)


def Event11410201(_, arg_0_3: int, arg_4_7: int):
    """ 11410201: Event 11410201 """
    SkipLinesIfThisEventSlotOff(2)
    DisableObject(arg_0_3)
    End()
    RestoreObject(arg_0_3)
    EnableObjectInvulnerability(arg_0_3)
    IfFlagOn(-1, 11410291)
    IfFlagOn(-1, 11410292)
    IfConditionTrue(0, input_condition=-1)
    IfEntityWithinDistance(0, arg_0_3, PLAYER, radius=8.0)
    DisableObjectInvulnerability(arg_0_3)
    DestroyObject(arg_0_3)
    CreateTemporaryVFX(140008, anchor_entity=arg_0_3, anchor_type=CoordEntityType.Object, model_point=-1)
    PlaySoundEffect(anchor_entity=arg_0_3, sound_type=SoundType.o_Object, sound_id=arg_4_7)
    DisableNetworkSync()
    Wait(10.0)
    DisableObject(arg_0_3)


def Event11410250():
    """ 11410250: Event 11410250 """
    EndIfFlagRangeAllOn((11410291, 11410292))
    EnableObjectInvulnerability(Objects.o4840_0000)
    EnableObjectInvulnerability(Objects.o4840_0001)
    EnableObjectInvulnerability(Objects.o4840_0002)
    EnableObjectInvulnerability(Objects.o4840_0003)
    EnableObjectInvulnerability(Objects.o4840_0004)
    EnableObjectInvulnerability(Objects.o4840_0005)
    EnableObjectInvulnerability(Objects.o4840_0006)
    EnableObjectInvulnerability(Objects.o4840_0007)
    EnableObjectInvulnerability(Objects.o4840_0008)
    EnableObjectInvulnerability(Objects.o4840_0009)
    EnableObjectInvulnerability(Objects.o4840_0010)
    EnableObjectInvulnerability(Objects.o4840_0011)
    EnableObjectInvulnerability(Objects.o4840_0012)
    EnableObjectInvulnerability(Objects.o4840_0013)
    EnableObjectInvulnerability(Objects.o4840_0014)
    EnableObjectInvulnerability(Objects.o4840_0015)
    EnableObjectInvulnerability(Objects.o4840_0016)
    EnableObjectInvulnerability(Objects.o4840_0017)
    EnableObjectInvulnerability(Objects.o4840_0018)
    EnableObjectInvulnerability(Objects.o4840_0019)
    EnableObjectInvulnerability(Objects.o4840_0020)
    EnableObjectInvulnerability(Objects.o4840_0021)
    EnableObjectInvulnerability(Objects.o4840_0022)
    EnableObjectInvulnerability(Objects.o4840_0023)
    EnableObjectInvulnerability(Objects.o4840_0024)
    EnableObjectInvulnerability(Objects.o4840_0025)
    EnableObjectInvulnerability(Objects.o4840_0026)
    EnableObjectInvulnerability(Objects.o4840_0027)
    EnableObjectInvulnerability(Objects.o4840_0028)
    EnableObjectInvulnerability(Objects.o4840_0029)
    EnableObjectInvulnerability(Objects.o4840_0030)
    EnableObjectInvulnerability(Objects.o4840_0031)
    EnableObjectInvulnerability(Objects.o4840_0032)
    EnableObjectInvulnerability(Objects.o4840_0033)
    EnableObjectInvulnerability(Objects.o4840_0034)
    EnableObjectInvulnerability(Objects.o4840_0035)
    EnableObjectInvulnerability(Objects.o4840_0036)
    EnableObjectInvulnerability(Objects.o4840_0037)
    EnableObjectInvulnerability(Objects.o4840_0038)
    EnableObjectInvulnerability(Objects.o4840_0039)
    EnableObjectInvulnerability(Objects.o4840_0040)
    EnableObjectInvulnerability(Objects.o4840_0041)
    EnableObjectInvulnerability(Objects.o4840_0042)
    EnableObjectInvulnerability(Objects.o4840_0043)
    EnableObjectInvulnerability(Objects.o4840_0044)
    EnableObjectInvulnerability(Objects.o4840_0045)
    EnableObjectInvulnerability(Objects.o4840_0046)
    EnableObjectInvulnerability(Objects.o4840_0047)
    IfFlagOn(1, 11410291)
    IfFlagOn(1, 11410292)
    IfConditionTrue(0, input_condition=1)
    DisableObjectInvulnerability(Objects.o4840_0000)
    DisableObjectInvulnerability(Objects.o4840_0001)
    DisableObjectInvulnerability(Objects.o4840_0002)
    DisableObjectInvulnerability(Objects.o4840_0003)
    DisableObjectInvulnerability(Objects.o4840_0004)
    DisableObjectInvulnerability(Objects.o4840_0005)
    DisableObjectInvulnerability(Objects.o4840_0006)
    DisableObjectInvulnerability(Objects.o4840_0007)
    DisableObjectInvulnerability(Objects.o4840_0008)
    DisableObjectInvulnerability(Objects.o4840_0009)
    DisableObjectInvulnerability(Objects.o4840_0010)
    DisableObjectInvulnerability(Objects.o4840_0011)
    DisableObjectInvulnerability(Objects.o4840_0012)
    DisableObjectInvulnerability(Objects.o4840_0013)
    DisableObjectInvulnerability(Objects.o4840_0014)
    DisableObjectInvulnerability(Objects.o4840_0015)
    DisableObjectInvulnerability(Objects.o4840_0016)
    DisableObjectInvulnerability(Objects.o4840_0017)
    DisableObjectInvulnerability(Objects.o4840_0018)
    DisableObjectInvulnerability(Objects.o4840_0019)
    DisableObjectInvulnerability(Objects.o4840_0020)
    DisableObjectInvulnerability(Objects.o4840_0021)
    DisableObjectInvulnerability(Objects.o4840_0022)
    DisableObjectInvulnerability(Objects.o4840_0023)
    DisableObjectInvulnerability(Objects.o4840_0024)
    DisableObjectInvulnerability(Objects.o4840_0025)
    DisableObjectInvulnerability(Objects.o4840_0026)
    DisableObjectInvulnerability(Objects.o4840_0027)
    DisableObjectInvulnerability(Objects.o4840_0028)
    DisableObjectInvulnerability(Objects.o4840_0029)
    DisableObjectInvulnerability(Objects.o4840_0030)
    DisableObjectInvulnerability(Objects.o4840_0031)
    DisableObjectInvulnerability(Objects.o4840_0032)
    DisableObjectInvulnerability(Objects.o4840_0033)
    DisableObjectInvulnerability(Objects.o4840_0034)
    DisableObjectInvulnerability(Objects.o4840_0035)
    DisableObjectInvulnerability(Objects.o4840_0036)
    DisableObjectInvulnerability(Objects.o4840_0037)
    DisableObjectInvulnerability(Objects.o4840_0038)
    DisableObjectInvulnerability(Objects.o4840_0039)
    DisableObjectInvulnerability(Objects.o4840_0040)
    DisableObjectInvulnerability(Objects.o4840_0041)
    DisableObjectInvulnerability(Objects.o4840_0042)
    DisableObjectInvulnerability(Objects.o4840_0043)
    DisableObjectInvulnerability(Objects.o4840_0044)
    DisableObjectInvulnerability(Objects.o4840_0045)
    DisableObjectInvulnerability(Objects.o4840_0046)
    DisableObjectInvulnerability(Objects.o4840_0047)


def Event11415370():
    """ 11415370: Event 11415370 """
    IfFlagOff(1, 11410900)
    IfActionButton(
        1,
        prompt_text=10010403,
        anchor_entity=Boxes.CeaselessFogPrompt,
        anchor_type=CoordEntityType.Region,
        line_intersects=Objects.o4961_0000,
        boss_version=True,
    )
    IfConditionTrue(0, input_condition=1)
    RotateToFaceEntity(PLAYER, Boxes.CeaselessFogRotationTarget)
    ForceAnimation(PLAYER, 7410)
    Restart()


def Event11415371():
    """ 11415371: Event 11415371 """
    IfFlagOff(1, 11410900)
    IfFlagOn(1, 11415373)
    IfCharacterType(1, PLAYER, CharacterType.WhitePhantom)
    IfActionButton(
        1,
        prompt_text=10010403,
        anchor_entity=Boxes.CeaselessFogPrompt,
        anchor_type=CoordEntityType.Region,
        trigger_attribute=TriggerAttribute.All,
        line_intersects=Objects.o4961_0000,
    )
    IfConditionTrue(0, input_condition=1)
    RotateToFaceEntity(PLAYER, Boxes.CeaselessFogRotationTarget)
    ForceAnimation(PLAYER, 7410)
    Restart()


def Event11415373():
    """ 11415373: Event 11415373 """
    SkipLinesIfThisEventOn(3)
    IfFlagOff(1, 11410900)
    IfCharacterInsideRegion(1, PLAYER, region=Boxes.CeaselessNotify)
    IfConditionTrue(0, input_condition=1)
    SkipLinesIfClient(2)
    NotifyBossBattleStart()
    SetNetworkUpdateAuthority(Characters.c5250_0000, UpdateAuthority.Forced)
    ActivateMultiplayerBuffs(Characters.c5250_0000)
    SetNetworkUpdateRate(Characters.c5250_0000, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    DisableInvincibility(Characters.c5250_0000)


@RestartOnRest
def Event11415372():
    """ 11415372: Event 11415372 """
    SkipLinesIfFlagOff(3, 11410900)
    DisableBackread(Characters.c5250_0000)
    Kill(Characters.c5250_0000, award_souls=False)
    End()
    DisableAI(Characters.c5250_0000)
    DisableHealthBar(Characters.c5250_0000)
    EnableInvincibility(Characters.c5250_0000)
    IfFlagOn(1, 11415373)
    IfHost(1)
    SkipLinesIfClient(1)
    IfFlagOn(1, 51410180)
    IfFlagOn(2, 11415373)
    IfAttacked(2, Characters.c5250_0000, attacker=PLAYER)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EnableAI(Characters.c5250_0000)
    EnableBossHealthBar(Characters.c5250_0000, name=5250, slot=0)


def Event11410900():
    """ 11410900: Event 11410900 """
    DisableObject(Objects.o0200_0002)
    IfCharacterDead(0, Characters.c5250_0000)
    EnableFlag(11410900)
    KillBoss(1410600)
    DisableBackread(Characters.c5250_0000)
    EnableFlag(11410800)
    DisableObject(Objects.o4961_0000)
    DeleteVFX(VFX.CeaselessEntranceFog, erase_root_only=True)
    EnableObject(Objects.o0200_0002)
    RegisterBonfire(
        11410976,
        obj=Objects.o0200_0002,
        reaction_distance=2.0,
        reaction_angle=180.0,
        initial_kindle_level=0,
    )
    EndIfFlagOn(11800100)
    EnableFlag(402)


def Event11415374():
    """ 11415374: Event 11415374 """
    DisableNetworkSync()
    IfFlagOff(1, 11410900)
    IfFlagOn(1, 11415372)
    SkipLinesIfHost(1)
    IfFlagOn(1, 11415371)
    IfCharacterInsideRegion(1, PLAYER, region=Boxes.CeaselessDischargeMusic)
    IfConditionTrue(0, input_condition=1)
    EnableSoundEvent(1413801)
    IfFlagOn(0, 11410900)
    DisableSoundEvent(1413801)


@RestartOnRest
def Event11415376():
    """ 11415376: Event 11415376 """
    IfCharacterAlive(1, Characters.c5250_0000)
    IfCharacterInsideRegion(1, Characters.c5250_0000, region=Boxes.CeaselessClings)
    IfConditionTrue(0, input_condition=1)
    Move(
        Characters.c5250_0000,
        destination=Spheres.CeaselessPreClingSnap,
        destination_type=CoordEntityType.Region,
        short_move=True,
    )
    ForceAnimation(Characters.c5250_0000, 17006, wait_for_completion=True)
    Move(
        Characters.c5250_0000,
        destination=Spheres.CeaselessPostClingSnap,
        destination_type=CoordEntityType.Region,
        short_move=True,
    )


@RestartOnRest
def Event11415377():
    """ 11415377: Event 11415377 """
    SkipLinesIfThisEventOff(4)
    CancelSpecialEffect(Characters.c5250_0000, 5132)
    AddSpecialEffect(Characters.c5250_0000, 5133)
    AICommand(Characters.c5250_0000, command_id=-1, slot=1)
    End()
    IfHasTAEEvent(0, Characters.c5250_0000, tae_event_id=300)
    CancelSpecialEffect(Characters.c5250_0000, 5132)
    AddSpecialEffect(Characters.c5250_0000, 5133)
    AICommand(Characters.c5250_0000, command_id=-1, slot=1)
    ReplanAI(Characters.c5250_0000)


@RestartOnRest
def Event11415378():
    """ 11415378: Event 11415378 """
    SkipLinesIfFlagOn(4, 0)
    IfHost(1)
    SkipLinesIfClient(1)
    IfFlagOn(1, 51410180)
    IfCharacterInsideRegion(1, PLAYER, region=Boxes.CeaselessAltarArea)
    IfConditionTrue(0, input_condition=1)
    AICommand(Characters.c5250_0000, command_id=1, slot=1)
    ReplanAI(Characters.c5250_0000)


@RestartOnRest
def Event11415379():
    """ 11415379: Event 11415379 """
    EndIfFlagOn(11410900)
    IfFlagRangeAllOn(1, (11415310, 11415314))
    IfHealthLessThanOrEqual(2, Characters.c5250_0000, 0.0)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(2)
    Kill(Characters.c5250_0000, award_souls=True)


@RestartOnRest
def Event11415310(_, arg_0_3: int):
    """ 11415310: Event 11415310 """
    IfFlagOn(1, 11415376)
    IfFlagOn(1, arg_0_3)
    IfAttacked(1, Characters.c5250_0000, attacker=PLAYER)
    IfConditionTrue(0, input_condition=1)
    End()


def Event11410800():
    """ 11410800: Event 11410800 """
    SkipLinesIfFlagOff(5, 11410801)
    DisableObject(Objects.o4500_0000)
    DisableCollision(Collisions.h0008B1)
    DisableSoundEvent(1413805)
    EnableTreasure(Objects.o0500_0005)
    End()
    DisableObject(Objects.o0500_0005)
    DisableTreasure(Objects.o0500_0005)
    DisableCollision(Collisions.h1008B1)
    DisableCharacter(Characters.c2250_0003)
    DisableCharacter(Characters.c2250_0004)
    DisableCharacter(Characters.c2250_0005)
    DisableCharacter(Characters.c2250_0006)
    DisableCharacter(Characters.c2250_0007)
    DisableCharacter(Characters.c2250_0008)
    DisableCharacter(Characters.c2250_0009)
    DisableNetworkSync()
    IfThisEventOn(0)
    Wait(5.0)
    IfHost(1)
    IfHealthLessThanOrEqual(1, PLAYER, 0.0)
    EndIfConditionTrue(1)
    EndIfClient()
    IfCharacterInsideRegion(0, PLAYER, region=Boxes.PlayerInLavaField)
    PlayCutscene(140100, skippable=True, fade_out=False, player_id=PLAYER)
    WaitFrames(1)
    EnableFlag(11410801)
    DisableObject(Objects.o4500_0000)
    DisableSoundEvent(1413805)
    DisableCollision(Collisions.h0008B1)
    EnableCollision(Collisions.h1008B1)
    EnableObject(Objects.o0500_0005)
    EnableTreasure(Objects.o0500_0005)
    EnableCharacter(Characters.c2250_0003)
    EnableCharacter(Characters.c2250_0004)
    EnableCharacter(Characters.c2250_0005)
    EnableCharacter(Characters.c2250_0006)
    EnableCharacter(Characters.c2250_0007)
    EnableCharacter(Characters.c2250_0008)
    EnableCharacter(Characters.c2250_0009)


def Event11415380():
    """ 11415380: Event 11415380 """
    IfFlagOff(1, 11410901)
    IfActionButton(
        1,
        prompt_text=10010403,
        anchor_entity=Boxes.CentipedeFogPrompt,
        anchor_type=CoordEntityType.Region,
        line_intersects=Objects.o4964_0000,
        boss_version=True,
    )
    IfConditionTrue(0, input_condition=1)
    RotateToFaceEntity(PLAYER, Boxes.CentipedeFogRotationTarget)
    ForceAnimation(PLAYER, 7410)
    Restart()


def Event11415381():
    """ 11415381: Event 11415381 """
    IfFlagOff(1, 11410901)
    IfFlagOn(1, 11415383)
    IfCharacterType(1, PLAYER, CharacterType.WhitePhantom)
    IfActionButton(
        1,
        prompt_text=10010403,
        anchor_entity=Boxes.CentipedeFogPrompt,
        anchor_type=CoordEntityType.Region,
        trigger_attribute=TriggerAttribute.All,
        line_intersects=Objects.o4964_0000,
    )
    IfConditionTrue(0, input_condition=1)
    RotateToFaceEntity(PLAYER, Boxes.CentipedeFogRotationTarget)
    ForceAnimation(PLAYER, 7410)
    Restart()


def Event11415383():
    """ 11415383: Event 11415383 """
    SkipLinesIfThisEventOn(3)
    IfFlagOff(1, 11410901)
    IfCharacterInsideRegion(1, PLAYER, region=Boxes.CentipedeCombatStart)
    IfConditionTrue(0, input_condition=1)
    SkipLinesIfClient(1)
    NotifyBossBattleStart()
    ActivateMultiplayerBuffs(Characters.c5200_0000)


@RestartOnRest
def Event11415382():
    """ 11415382: Event 11415382 """
    DisableObject(Objects.o4450_0000)
    RunEvent(11415385)
    SkipLinesIfFlagOff(2, 11410901)
    DisableBackread(Characters.c5200_0000)
    End()
    SkipLinesIfFlagOn(2, 11410002)
    EnableObject(Objects.o4450_0000)
    DisableCharacter(Characters.c5200_0000)
    DisableAI(Characters.c5200_0000)
    IfFlagOn(1, 11415383)
    IfCharacterInsideRegion(1, PLAYER, region=Boxes.CentipedeCombatStart)
    IfConditionTrue(0, input_condition=1)
    IfCharacterType(-1, PLAYER, CharacterType.BlackPhantom)
    IfCharacterType(-1, PLAYER, CharacterType.Intruder)
    EndIfConditionTrue(-1)
    SkipLinesIfFlagOn(8, 11410002)
    SkipLinesIfMultiplayer(2)
    PlayCutscene(140120, skippable=True, fade_out=False, player_id=PLAYER)
    SkipLines(1)
    PlayCutscene(140120, skippable=False, fade_out=False, player_id=PLAYER)
    WaitFrames(1)
    EnableCharacter(Characters.c5200_0000)
    DisableObject(Objects.o4450_0000)
    EnableFlag(11410002)
    EnableAI(Characters.c5200_0000)
    EnableBossHealthBar(Characters.c5200_0000, name=5200, slot=0)


def Event11410901():
    """ 11410901: Event 11410901 """
    IfCharacterDead(0, Characters.c5200_0000)
    EnableFlag(11410901)
    KillBoss(1410700)
    EnableFlag(11410901)
    DisableObject(Objects.o4964_0000)
    DeleteVFX(VFX.CentipedeEntranceFog, erase_root_only=True)
    DisableObject(Objects.o4965_0000)
    DeleteVFX(VFX.CentipedeExitFog, erase_root_only=True)
    DisableNetworkSync()
    Wait(10.0)
    DisableCharacter(Characters.c5200_0000)
    DisableBackread(Characters.c5200_0000)


def Event11415384():
    """ 11415384: Event 11415384 """
    DisableNetworkSync()
    IfFlagOff(1, 11410901)
    IfFlagOn(1, 11410002)
    IfFlagOn(1, 11415382)
    SkipLinesIfHost(1)
    IfFlagOn(1, 11415381)
    IfCharacterInsideRegion(1, PLAYER, region=Boxes.CentipedeDemonMusic)
    IfConditionTrue(0, input_condition=1)
    EnableSoundEvent(1413802)
    IfFlagOn(0, 11410901)
    DisableSoundEvent(1413802)


@UnknownRestart
def Event11415385():
    """ 11415385: Event 11415385 """
    DisableCharacter(Characters.c5201_0000)
    DisableCharacter(Characters.c5201_0001)
    DisableCharacter(Characters.c5201_0002)
    DisableCharacter(Characters.c5201_0003)
    DisableCharacter(Characters.c5201_0004)
    DisableCharacter(Characters.c5202_0000)
    DisableCharacter(Characters.c5202_0001)
    DisableCharacter(Characters.c5202_0002)
    DisableCharacter(Characters.c5202_0003)
    DisableCharacter(Characters.c5202_0004)
    EndIfFlagOn(11410901)
    RunEvent(11415350, slot=0, args=(11415380, 5200, 5200, 125, Characters.c5201_0000), arg_types="ihiii")
    RunEvent(11415350, slot=1, args=(11415350, 5201, 5201, 125, Characters.c5201_0001), arg_types="ihiii")
    RunEvent(11415350, slot=2, args=(11415351, 5202, 5202, 125, Characters.c5201_0002), arg_types="ihiii")
    RunEvent(11415350, slot=3, args=(11415352, 5203, 5203, 125, Characters.c5201_0003), arg_types="ihiii")
    RunEvent(11415350, slot=4, args=(11415353, 5204, 5204, 125, Characters.c5201_0004), arg_types="ihiii")
    RunEvent(11415360, slot=0, args=(11415380, 5205, 5205, 95, Characters.c5202_0000), arg_types="ihiii")
    RunEvent(11415360, slot=1, args=(11415360, 5206, 5206, 95, Characters.c5202_0001), arg_types="ihiii")
    RunEvent(11415360, slot=2, args=(11415361, 5207, 5207, 95, Characters.c5202_0002), arg_types="ihiii")
    RunEvent(11415360, slot=3, args=(11415362, 5208, 5208, 95, Characters.c5202_0003), arg_types="ihiii")
    RunEvent(11415360, slot=4, args=(11415363, 5209, 5209, 95, Characters.c5202_0004), arg_types="ihiii")
    RunEvent(11415320, slot=0, args=(11415380, Characters.c5201_0000))
    RunEvent(11415320, slot=1, args=(11415350, Characters.c5201_0001))
    RunEvent(11415320, slot=2, args=(11415351, Characters.c5201_0002))
    RunEvent(11415320, slot=3, args=(11415352, Characters.c5201_0003))
    RunEvent(11415320, slot=4, args=(11415353, Characters.c5201_0004))
    RunEvent(11415320, slot=5, args=(11415380, Characters.c5202_0000))
    RunEvent(11415320, slot=6, args=(11415360, Characters.c5202_0001))
    RunEvent(11415320, slot=7, args=(11415361, Characters.c5202_0002))
    RunEvent(11415320, slot=8, args=(11415362, Characters.c5202_0003))
    RunEvent(11415320, slot=9, args=(11415363, Characters.c5202_0004))


def Event11415386():
    """ 11415386: Event 11415386 """
    EndIfClient()
    IfCharacterDead(-1, Characters.c5200_0000)
    IfCharacterDead(-1, Characters.c5201_0000)
    IfCharacterDead(-1, Characters.c5201_0001)
    IfCharacterDead(-1, Characters.c5201_0002)
    IfCharacterDead(-1, Characters.c5201_0003)
    IfCharacterDead(-1, Characters.c5201_0004)
    IfCharacterDead(-1, Characters.c5202_0000)
    IfCharacterDead(-1, Characters.c5202_0001)
    IfCharacterDead(-1, Characters.c5202_0002)
    IfCharacterDead(-1, Characters.c5202_0003)
    IfCharacterDead(-1, Characters.c5202_0004)
    IfConditionTrue(0, input_condition=-1)
    IfCharacterHuman(-7, PLAYER)
    IfCharacterHollow(-7, PLAYER)
    EndIfConditionFalse(-7)
    AwardItemLot(2670, host_only=True)


@UnknownRestart
def Event11415320(_, arg_0_3: int, arg_4_7: int):
    """ 11415320: Event 11415320 """
    IfFlagOn(1, arg_0_3)
    IfHasTAEEvent(1, Characters.c5200_0000, tae_event_id=400)
    IfHealthGreaterThan(1, Characters.c5200_0000, 0.0)
    IfConditionTrue(0, input_condition=1)
    IfHealthLessThanOrEqual(0, Characters.c5200_0000, 0.0)
    Kill(arg_4_7, award_souls=True)


@UnknownRestart
def Event11415350(_, arg_0_3: int, arg_4_5: short, arg_8_11: int, arg_12_15: int, arg_16_19: int):
    """ 11415350: Event 11415350 """
    SkipLinesIfThisEventSlotOff(1)
    EnableCharacter(arg_16_19)
    SkipLinesIfFlagOff(4, 11415354)
    SetDisplayMask(Characters.c5200_0000, bit_index=0, switch_type=OnOffChange.On)
    SetCollisionMask(Characters.c5200_0000, bit_index=1, switch_type=OnOffChange.Off)
    AICommand(Characters.c5200_0000, command_id=20, slot=0)
    End()
    IfFlagOn(0, arg_0_3)
    CreateNPCPart(
        Characters.c5200_0000,
        npc_part_id=arg_4_5,
        part_index=NPCPartType.Part1,
        part_health=arg_12_15,
        damage_correction=1.0,
        body_damage_correction=1.0,
        is_invincible=False,
        start_in_stop_state=False,
    )
    IfCharacterPartHealthLessThanOrEqual(1, Characters.c5200_0000, npc_part_id=arg_8_11, value=0)
    IfHealthLessThanOrEqual(2, Characters.c5200_0000, 0.0)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(2)
    EzstateAIRequest(Characters.c5200_0000, command_id=1001, slot=0)
    IfHasTAEEvent(0, Characters.c5200_0000, tae_event_id=400)
    EnableCharacter(arg_16_19)
    Move(
        arg_16_19,
        destination=Characters.c5200_0000,
        destination_type=CoordEntityType.Character,
        model_point=140,
        copy_draw_parent=Characters.c5200_0000,
    )
    ForceAnimation(arg_16_19, 8100)
    SetDisplayMask(Characters.c5200_0000, bit_index=0, switch_type=OnOffChange.On)
    SetCollisionMask(Characters.c5200_0000, bit_index=1, switch_type=OnOffChange.Off)
    AICommand(Characters.c5200_0000, command_id=10, slot=0)
    SkipLinesIfFlagOff(2, 11415353)
    AICommand(Characters.c5200_0000, command_id=20, slot=0)
    End()
    IfHasTAEEvent(0, Characters.c5200_0000, tae_event_id=300)
    SetDisplayMask(Characters.c5200_0000, bit_index=0, switch_type=OnOffChange.Off)
    SetCollisionMask(Characters.c5200_0000, bit_index=1, switch_type=OnOffChange.On)
    AICommand(Characters.c5200_0000, command_id=-1, slot=0)


@UnknownRestart
def Event11415360(_, arg_0_3: int, arg_4_5: short, arg_8_11: int, arg_12_15: int, arg_16_19: int):
    """ 11415360: Event 11415360 """
    SkipLinesIfThisEventSlotOff(1)
    EnableCharacter(arg_16_19)
    SkipLinesIfFlagOff(4, 11415364)
    SetDisplayMask(Characters.c5200_0000, bit_index=1, switch_type=OnOffChange.On)
    SetCollisionMask(Characters.c5200_0000, bit_index=2, switch_type=OnOffChange.Off)
    AICommand(Characters.c5200_0000, command_id=20, slot=1)
    End()
    IfFlagOn(0, arg_0_3)
    CreateNPCPart(
        Characters.c5200_0000,
        npc_part_id=arg_4_5,
        part_index=NPCPartType.Part2,
        part_health=arg_12_15,
        damage_correction=1.0,
        body_damage_correction=1.0,
        is_invincible=False,
        start_in_stop_state=False,
    )
    IfCharacterPartHealthLessThanOrEqual(1, Characters.c5200_0000, npc_part_id=arg_8_11, value=0)
    IfHealthLessThanOrEqual(2, Characters.c5200_0000, 0.0)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(2)
    EzstateAIRequest(Characters.c5200_0000, command_id=1002, slot=0)
    IfHasTAEEvent(0, Characters.c5200_0000, tae_event_id=400)
    EnableCharacter(arg_16_19)
    Move(
        arg_16_19,
        destination=Characters.c5200_0000,
        destination_type=CoordEntityType.Character,
        model_point=141,
        copy_draw_parent=Characters.c5200_0000,
    )
    ForceAnimation(arg_16_19, 8100)
    SetDisplayMask(Characters.c5200_0000, bit_index=1, switch_type=OnOffChange.On)
    SetCollisionMask(Characters.c5200_0000, bit_index=2, switch_type=OnOffChange.Off)
    AICommand(Characters.c5200_0000, command_id=10, slot=1)
    SkipLinesIfFlagOff(2, 11415363)
    AICommand(Characters.c5200_0000, command_id=20, slot=1)
    End()
    IfHasTAEEvent(0, Characters.c5200_0000, tae_event_id=600)
    SetDisplayMask(Characters.c5200_0000, bit_index=1, switch_type=OnOffChange.Off)
    SetCollisionMask(Characters.c5200_0000, bit_index=2, switch_type=OnOffChange.On)
    AICommand(Characters.c5200_0000, command_id=-1, slot=1)


def Event11410340():
    """ 11410340: Event 11410340 """
    SkipLinesIfThisEventOff(2)
    EndOfAnimation(Objects.o4700_0000, 1)
    End()
    IfHost(1)
    IfPlayerCovenant(1, Covenant.ChaosServant)
    IfFlagOn(1, 11400598)
    IfActionButton(
        1,
        prompt_text=10010510,
        anchor_entity=Boxes.IzalithShortcutGateFrontPrompt,
        anchor_type=CoordEntityType.Region,
        line_intersects=Objects.o4700_0000,
    )
    IfActionButton(
        2,
        prompt_text=10010510,
        anchor_entity=Boxes.IzalithShortcutGateBackPrompt,
        anchor_type=CoordEntityType.Region,
        line_intersects=Objects.o4700_0000,
    )
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EnableFlag(11410340)
    RotateToFaceEntity(PLAYER, Objects.o4700_0000)
    ForceAnimation(PLAYER, 7114, wait_for_completion=True)
    ForceAnimation(Objects.o4700_0000, 1)
    CreateTemporaryVFX(140000, anchor_entity=Objects.o4700_0000, anchor_type=CoordEntityType.Object, model_point=-1)


def Event11410341():
    """ 11410341: Event 11410341 """
    DisableNetworkSync()
    IfFlagOff(1, 11410340)
    IfHost(6)
    IfPlayerCovenant(7, Covenant.ChaosServant)
    IfConditionFalse(6, input_condition=7)
    IfConditionTrue(-7, input_condition=6)
    IfFlagOff(-7, 11400598)
    IfConditionTrue(1, input_condition=-7)
    IfActionButton(
        -2,
        prompt_text=10010510,
        anchor_entity=Boxes.IzalithShortcutGateFrontPrompt,
        anchor_type=CoordEntityType.Region,
        line_intersects=Objects.o4700_0000,
    )
    IfConditionTrue(1, input_condition=-2)
    IfFlagOff(2, 11410340)
    IfClient(2)
    IfActionButton(
        -3,
        prompt_text=10010510,
        anchor_entity=Boxes.IzalithShortcutGateBackPrompt,
        anchor_type=CoordEntityType.Region,
        trigger_attribute=TriggerAttribute.All,
        line_intersects=Objects.o4700_0000,
    )
    IfActionButton(
        -3,
        prompt_text=10010510,
        anchor_entity=Boxes.IzalithShortcutGateFrontPrompt,
        anchor_type=CoordEntityType.Region,
        trigger_attribute=TriggerAttribute.All,
        line_intersects=Objects.o4700_0000,
    )
    IfConditionTrue(2, input_condition=-3)
    IfFlagOn(3, 11410340)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfFlagOn(11410340)
    DisplayDialog(
        10010160,
        anchor_entity=Objects.o4700_0000,
        display_distance=5.0,
        button_type=ButtonType.Yes_or_No,
        number_buttons=NumberButtons.NoButton,
    )
    Restart()


def Event11410360():
    """ 11410360: Event 11410360 """
    SkipLinesIfThisEventOff(2)
    DisableObject(Objects.o4510_0000)
    End()
    IfObjectDestroyed(0, Objects.o4510_0000)
    EnableFlag(11410360)


def Event11410400():
    """ 11410400: Event 11410400 """
    SkipLinesIfFlagOff(1, 11410401)
    EndOfAnimation(Objects.o4600_0000, 0)
    IfFlagOn(0, 11410410)
    IfFlagOn(1, 11410401)
    IfCharacterInsideRegion(1, PLAYER, region=Spheres.ShortcutElevatorStartFromBottom)
    IfFlagOff(2, 11410401)
    IfCharacterInsideRegion(2, PLAYER, region=Spheres.ShortcutElevatorStartFromTop)
    IfFlagOff(3, 11410401)
    IfCharacterInsideRegion(3, PLAYER, region=Spheres.ShortcutElevatorSummonFromBottom)
    IfFlagOn(4, 11410401)
    IfCharacterInsideRegion(4, PLAYER, region=Spheres.ShortcutElevatorSummonFromTop)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(-1, input_condition=4)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionTrue(2, 3)
    SkipLinesIfFinishedConditionTrue(8, 4)
    SkipLinesIfFlagOn(7, 11410401)
    EnableFlag(11410401)
    CreateObjectVFX(140002, obj=Objects.o4600_0000, model_point=100)
    ForceAnimation(Objects.o4600_0000, 3, wait_for_completion=True)
    DeleteObjectVFX(Objects.o4600_0000, erase_root=True)
    IfAllPlayersOutsideRegion(0, region=Spheres.ShortcutElevatorStartFromBottom)
    ForceAnimation(Objects.o4600_0000, 4, wait_for_completion=True)
    Restart()
    DisableFlag(11410401)
    CreateObjectVFX(140002, obj=Objects.o4600_0000, model_point=100)
    ForceAnimation(Objects.o4600_0000, 1, wait_for_completion=True)
    DeleteObjectVFX(Objects.o4600_0000, erase_root=True)
    IfAllPlayersOutsideRegion(0, region=Spheres.ShortcutElevatorStartFromTop)
    ForceAnimation(Objects.o4600_0000, 5, wait_for_completion=True)
    Restart()


def Event11410402():
    """ 11410402: Event 11410402 """
    DisableNetworkSync()
    IfFlagOff(-2, 11410410)
    IfMultiplayer(-2)
    IfConditionTrue(1, input_condition=-2)
    IfActionButton(
        1,
        prompt_text=10010510,
        anchor_entity=Objects.o4600_0000,
        anchor_type=CoordEntityType.Object,
        max_distance=1.5,
        model_point=100,
        trigger_attribute=TriggerAttribute.All,
    )
    IfConditionTrue(0, input_condition=1)
    DisplayDialog(
        10010170,
        anchor_entity=Objects.o4600_0000,
        display_distance=3.0,
        button_type=ButtonType.Yes_or_No,
        number_buttons=NumberButtons.NoButton,
    )
    Restart()


def Event11415340():
    """ 11415340: Event 11415340 """
    IfFlagOff(1, 11410410)
    IfActionButton(
        1,
        prompt_text=10010403,
        anchor_entity=Boxes.FiresageDemonFogPrompt,
        anchor_type=CoordEntityType.Region,
        line_intersects=Objects.o4962_0000,
        boss_version=True,
    )
    IfConditionTrue(0, input_condition=1)
    RotateToFaceEntity(PLAYER, Boxes.FiresageDemonFogRotationTarget)
    ForceAnimation(PLAYER, 7410)
    Restart()


def Event11415341():
    """ 11415341: Event 11415341 """
    IfFlagOff(1, 11410410)
    IfFlagOn(1, 11415343)
    IfCharacterType(1, PLAYER, CharacterType.WhitePhantom)
    IfActionButton(
        1,
        prompt_text=10010403,
        anchor_entity=Boxes.FiresageDemonFogPrompt,
        anchor_type=CoordEntityType.Region,
        trigger_attribute=TriggerAttribute.All,
        line_intersects=Objects.o4962_0000,
    )
    IfConditionTrue(0, input_condition=1)
    RotateToFaceEntity(PLAYER, Boxes.FiresageDemonFogRotationTarget)
    ForceAnimation(PLAYER, 7410)
    Restart()


def Event11415343():
    """ 11415343: Event 11415343 """
    SkipLinesIfThisEventOn(3)
    IfFlagOff(1, 11410410)
    IfCharacterInsideRegion(1, PLAYER, region=Boxes.FiresageDemonCombatStart)
    IfConditionTrue(0, input_condition=1)
    SkipLinesIfClient(1)
    NotifyBossBattleStart()
    ActivateMultiplayerBuffs(Characters.c2231_0000)


@RestartOnRest
def Event11415342():
    """ 11415342: Event 11415342 """
    SkipLinesIfFlagOff(8, 11410410)
    SkipLinesIfClient(4)
    DisableObject(Objects.o4962_0000)
    DeleteVFX(VFX.FiresageEntranceFog, erase_root_only=False)
    DisableObject(Objects.o4963_0000)
    DeleteVFX(VFX.FiresageExitFog, erase_root_only=False)
    DisableCharacter(Characters.c2231_0000)
    DisableBackread(Characters.c2231_0000)
    End()
    DisableAI(Characters.c2231_0000)
    IfFlagOn(1, 11415343)
    IfCharacterInsideRegion(1, PLAYER, region=Boxes.FiresageDemonCombatStart)
    IfConditionTrue(0, input_condition=1)
    EnableAI(Characters.c2231_0000)
    EnableBossHealthBar(Characters.c2231_0000, name=2230, slot=0)


def Event11415344():
    """ 11415344: Event 11415344 """
    DisableNetworkSync()
    IfFlagOff(1, 11410410)
    IfFlagOn(1, 11415342)
    SkipLinesIfHost(1)
    IfFlagOn(1, 11415341)
    IfCharacterInsideRegion(1, PLAYER, region=Boxes.FiresageDemonMusic)
    IfConditionTrue(0, input_condition=1)
    EnableSoundEvent(1413803)
    IfFlagOn(0, 11410410)
    DisableSoundEvent(1413803)


def Event11415345():
    """ 11415345: Event 11415345 """
    DisableNetworkSync()
    IfFlagOn(1, 11415340)
    IfCharacterInsideRegion(1, PLAYER, region=Boxes.FiresageDemonMusic)
    IfCharacterBackreadEnabled(-1, m14_00_Characters.c5340_0000)
    IfCharacterBackreadEnabled(-1, m14_00_Characters.c3210_0000)
    IfCharacterBackreadEnabled(-1, m14_00_Characters.c3220_0000)
    IfCharacterBackreadEnabled(-1, m14_00_Characters.c3220_0001)
    IfCharacterBackreadEnabled(-1, m14_00_Characters.c3220_0002)
    IfCharacterBackreadEnabled(-1, m14_00_Characters.c3220_0003)
    IfCharacterBackreadEnabled(-1, m14_00_Characters.c3220_0004)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    DisableBackread(m14_00_Characters.c5340_0000)
    DisableBackread(m14_00_Characters.c3210_0000)
    DisableBackread(m14_00_Characters.c3220_0000)
    DisableBackread(m14_00_Characters.c3220_0001)
    DisableBackread(m14_00_Characters.c3220_0002)
    DisableBackread(m14_00_Characters.c3220_0003)
    DisableBackread(m14_00_Characters.c3220_0004)
    IfFlagOn(0, 11410410)
    Wait(5.0)
    EnableBackread(m14_00_Characters.c5340_0000)
    EnableBackread(m14_00_Characters.c3210_0000)
    EnableBackread(m14_00_Characters.c3220_0000)
    EnableBackread(m14_00_Characters.c3220_0001)
    EnableBackread(m14_00_Characters.c3220_0002)
    EnableBackread(m14_00_Characters.c3220_0003)
    EnableBackread(m14_00_Characters.c3220_0004)


def Event11410410():
    """ 11410410: Event 11410410 """
    IfCharacterDead(0, Characters.c2231_0000)
    EnableFlag(11410410)
    KillBoss(1410400)
    EnableFlag(11410410)
    DisableObject(Objects.o4962_0000)
    DeleteVFX(VFX.FiresageEntranceFog, erase_root_only=True)
    DisableObject(Objects.o4963_0000)
    DeleteVFX(VFX.FiresageExitFog, erase_root_only=True)
    DisableNetworkSync()
    Wait(3.0)
    DisableCharacter(Characters.c2231_0000)
    DisableBackread(Characters.c2231_0000)


@RestartOnRest
def Event11415100(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: float, arg_16_19: float):
    """ 11415100: Event 11415100 """
    SkipLinesIfThisEventSlotOff(2)
    SetStandbyAnimationSettings(arg_4_7, cancel_animation=arg_8_11)
    End()
    IfEntityWithinDistance(0, arg_0_3, PLAYER, radius=arg_12_15)
    Wait(arg_16_19)
    SetStandbyAnimationSettings(arg_4_7, cancel_animation=arg_8_11)


@RestartOnRest
def Event11415120(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: float):
    """ 11415120: Event 11415120 """
    SkipLinesIfThisEventSlotOff(2)
    SetStandbyAnimationSettings(arg_4_7, cancel_animation=arg_8_11)
    End()
    IfCharacterInsideRegion(0, arg_0_3, region=arg_12_15)
    Wait(arg_16_19)
    SetStandbyAnimationSettings(arg_4_7, cancel_animation=arg_8_11)


@RestartOnRest
def Event11415200():
    """ 11415200: Event 11415200 """
    RunEvent(11415201, slot=0, args=(1410500, 1, 0, 3290, 3290), arg_types="ihhii")
    RunEvent(5200, slot=-1, args=(1410500, 11415201, 0, 0), arg_types="iiBB")
    RunEvent(5200, slot=-1, args=(1410500, 11415201, 2, 0), arg_types="iiBB")
    RunEvent(5201, slot=-1, args=(1410500, 11415201, 1411500, 1411501, 120, 0), arg_types="iiiihh")
    RunEvent(5201, slot=-1, args=(1410500, 11415201, 1411502, 1411503, 126, 0), arg_types="iiiihh")
    RunEvent(5202, slot=-1, args=(1410500, 11415201, 1410550, 1410551, 120, 123))
    RunEvent(5202, slot=-1, args=(1410500, 11415201, 1410552, 1410553, 126, 129))
    RunEvent(11415201, slot=1, args=(1410500, 2, 0, 3291, 3291), arg_types="ihhii")
    RunEvent(5200, slot=-1, args=(1410500, 11415202, 5, 0), arg_types="iiBB")
    RunEvent(5201, slot=-1, args=(1410500, 11415202, 1411504, 1411505, 135, 0), arg_types="iiiihh")
    RunEvent(5202, slot=-1, args=(1410500, 11415202, 1410554, 1410555, 135, 137))
    RunEvent(5202, slot=-1, args=(1410500, 11415202, 1410556, 1410557, 153, 155))
    RunEvent(11415201, slot=2, args=(1410500, 3, 0, 3292, 3292), arg_types="ihhii")
    RunEvent(5200, slot=-1, args=(1410500, 11415203, 6, 0), arg_types="iiBB")
    RunEvent(5200, slot=-1, args=(1410500, 11415203, 8, 0), arg_types="iiBB")
    RunEvent(5201, slot=-1, args=(1410500, 11415203, 1411506, 1411507, 138, 0), arg_types="iiiihh")
    RunEvent(5201, slot=-1, args=(1410500, 11415203, 1411508, 1411509, 144, 0), arg_types="iiiihh")
    RunEvent(5202, slot=-1, args=(1410500, 11415203, 1410558, 1410559, 138, 141))
    RunEvent(5202, slot=-1, args=(1410500, 11415203, 1410560, 1410561, 144, 150))
    RunEvent(11415201, slot=3, args=(1410500, 4, 0, 3293, 3293), arg_types="ihhii")
    RunEvent(5200, slot=-1, args=(1410500, 11415204, 4, 0), arg_types="iiBB")
    RunEvent(5201, slot=-1, args=(1410500, 11415204, 1411510, 1411511, 132, 0), arg_types="iiiihh")
    RunEvent(5202, slot=-1, args=(1410500, 11415204, 1410562, 1410563, 132, 134))
    RunEvent(5202, slot=-1, args=(1410500, 11415204, 1410564, 1410565, 150, 152))


@UnknownRestart
def Event11415201(_, arg_0_3: int, arg_4_5: short, arg_6_7: short, arg_8_11: int, arg_12_15: int):
    """ 11415201: Event 11415201 """
    EndIfThisEventSlotOn()
    IfCharacterBackreadEnabled(0, arg_0_3)
    CreateNPCPart(
        arg_0_3,
        npc_part_id=arg_6_7,
        part_index=arg_4_5,
        part_health=100,
        damage_correction=1.0,
        body_damage_correction=1.0,
        is_invincible=False,
        start_in_stop_state=False,
    )
    IfCharacterPartHealthLessThanOrEqual(0, arg_0_3, npc_part_id=arg_8_11, value=0)
    DisableFlag(11415290)
    DisableFlag(11415291)
    SkipLinesIfClient(1)
    EnableRandomFlagInRange((11415290, 11415291))
    EnableFlag(arg_12_15)
    SkipLinesIfFlagOff(2, 11415290)
    ForceAnimation(arg_0_3, 8000)
    SkipLines(1)
    ForceAnimation(arg_0_3, 8010)


@UnknownRestart
def Event5200(_, arg_0_3: int, arg_4_7: int, arg_8_8: uchar, arg_9_9: uchar):
    """ 5200: Event 5200 """
    SkipLinesIfFlagOn(6, arg_4_7)
    IfFlagOn(1, arg_4_7)
    IfCharacterDead(2, arg_0_3)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(2)
    SetDisplayMask(arg_0_3, bit_index=arg_8_8, switch_type=OnOffChange.On)
    SetDisplayMask(arg_0_3, bit_index=arg_9_9, switch_type=OnOffChange.On)


@UnknownRestart
def Event5201(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_17: short, arg_18_19: short):
    """ 5201: Event 5201 """
    DisableObject(arg_8_11)
    DisableObject(arg_12_15)
    EndIfFlagOn(arg_4_7)
    IfFlagOn(1, arg_4_7)
    IfCharacterDead(2, arg_0_3)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(2)
    EnableObject(arg_8_11)
    EnableObject(arg_12_15)
    MoveObjectToCharacter(arg_8_11, character=arg_0_3, model_point=arg_16_17)
    MoveObjectToCharacter(arg_12_15, character=arg_0_3, model_point=arg_18_19)
    DestroyObject(arg_8_11)
    DestroyObject(arg_12_15)


@UnknownRestart
def Event5202(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int, arg_20_23: int):
    """ 5202: Event 5202 """
    EndIfFlagOn(arg_4_7)
    DisableCharacter(arg_8_11)
    DisableCharacter(arg_12_15)
    IfFlagOn(1, arg_4_7)
    IfCharacterDead(2, arg_0_3)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(2)
    ResetAnimation(arg_0_3, disable_interpolation=False)
    Move(
        arg_8_11,
        destination=arg_0_3,
        destination_type=CoordEntityType.Character,
        model_point=arg_16_19,
        copy_draw_parent=arg_0_3,
    )
    Move(
        arg_12_15,
        destination=arg_0_3,
        destination_type=CoordEntityType.Character,
        model_point=arg_20_23,
        copy_draw_parent=arg_0_3,
    )
    EnableCharacter(arg_8_11)
    EnableCharacter(arg_12_15)
    ForceAnimation(arg_8_11, 7000)
    ForceAnimation(arg_12_15, 7000)


@RestartOnRest
def Event11415210(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 11415210: Event 11415210 """
    IfTrueFlagCountGreaterThanOrEqual(0, arg_8_11, (arg_0_3, arg_4_7))
    DisableSoundEvent(1413806)


@RestartOnRest
def Event11415250(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int, arg_20_23: int):
    """ 11415250: Event 11415250 """
    SkipLinesIfThisEventSlotOff(2)
    SetDisplayMask(arg_0_3, bit_index=2, switch_type=OnOffChange.On)
    End()
    DisableCharacter(arg_4_7)
    DisableCharacter(arg_8_11)
    DisableCharacter(arg_12_15)
    DisableCharacter(arg_16_19)
    DisableCharacter(arg_20_23)
    IfCharacterDead(0, arg_0_3)
    SetDisplayMask(arg_0_3, bit_index=2, switch_type=OnOffChange.On)
    EnableCharacter(arg_4_7)
    EnableCharacter(arg_8_11)
    EnableCharacter(arg_12_15)
    EnableCharacter(arg_16_19)
    EnableCharacter(arg_20_23)
    Move(
        arg_4_7,
        destination=arg_0_3,
        destination_type=CoordEntityType.Character,
        model_point=100,
        copy_draw_parent=arg_0_3,
    )
    Move(
        arg_8_11,
        destination=arg_0_3,
        destination_type=CoordEntityType.Character,
        model_point=101,
        copy_draw_parent=arg_0_3,
    )
    Move(
        arg_12_15,
        destination=arg_0_3,
        destination_type=CoordEntityType.Character,
        model_point=102,
        copy_draw_parent=arg_0_3,
    )
    Move(
        arg_16_19,
        destination=arg_0_3,
        destination_type=CoordEntityType.Character,
        model_point=103,
        copy_draw_parent=arg_0_3,
    )
    Move(
        arg_20_23,
        destination=arg_0_3,
        destination_type=CoordEntityType.Character,
        model_point=104,
        copy_draw_parent=arg_0_3,
    )
    ForceAnimation(arg_4_7, 7000)
    ForceAnimation(arg_8_11, 7000)
    ForceAnimation(arg_12_15, 7000)
    ForceAnimation(arg_16_19, 7000)
    ForceAnimation(arg_20_23, 7000)


def Event11410350():
    """ 11410350: Event 11410350 """
    SkipLinesIfThisEventOff(5)
    DisableObject(Objects.o4810_0000)
    PostDestruction(Objects.o4810_0001)
    EndOfAnimation(Objects.o0500_0000, 116)
    EnableTreasure(Objects.o0500_0000)
    End()
    DisableObject(Objects.o4810_0001)
    DisableTreasure(Objects.o0500_0000)
    CreateObjectVFX(99010, obj=Objects.o0500_0000, model_point=90)
    ForceAnimation(Objects.o0500_0000, 115, loop=True)
    IfCharacterInsideRegion(-1, PLAYER, region=Boxes.SewerFloorBreakTrigger)
    IfObjectDestroyed(-1, Objects.o4810_0000)
    IfConditionTrue(0, input_condition=-1)
    DisableObject(Objects.o4810_0000)
    EnableObject(Objects.o4810_0001)
    CreateTemporaryVFX(140001, anchor_entity=Objects.o4810_0001, anchor_type=CoordEntityType.Object, model_point=-1)
    PlaySoundEffect(anchor_entity=Objects.o4810_0001, sound_type=SoundType.o_Object, sound_id=481000001)
    DestroyObject(Objects.o4810_0001)
    ForceAnimation(Objects.o0500_0000, 116, wait_for_completion=True)
    EnableTreasure(Objects.o0500_0000)
    DeleteObjectVFX(Objects.o0500_0000, erase_root=True)


@RestartOnRest
def Event11410100(_, arg_0_3: int):
    """ 11410100: Event 11410100 """
    SkipLinesIfThisEventSlotOff(3)
    DisableCharacter(arg_0_3)
    Kill(arg_0_3, award_souls=False)
    End()
    IfCharacterDead(0, arg_0_3)
    EndIfNotEqual(left=arg_0_3, right=1410110)
    IfCharacterHuman(-7, PLAYER)
    IfCharacterHollow(-7, PLAYER)
    EndIfConditionFalse(-7)
    AwardItemLot(33002000, host_only=True)


@RestartOnRest
def Event11410150(_, arg_0_3: int, arg_4_7: int):
    """ 11410150: Event 11410150 """
    EndIfThisEventSlotOn()
    IfCharacterDead(0, arg_0_3)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterHollow(-1, PLAYER)
    EndIfConditionFalse(-1)
    AwardItemLot(arg_4_7, host_only=True)


@RestartOnRest
def Event800(_, arg_0_3: int):
    """ 800: Event 800 """
    SkipLinesIfThisEventSlotOff(3)
    DropMandatoryTreasure(arg_0_3)
    DisableCharacter(arg_0_3)
    End()
    IfCharacterDead(0, arg_0_3)
    End()


def Event11410600(_, arg_0_3: int, arg_4_7: int):
    """ 11410600: Event 11410600 """
    SkipLinesIfThisEventSlotOff(4)
    EndOfAnimation(arg_0_3, 0)
    DisableObjectActivation(arg_0_3, obj_act_id=-1)
    EnableTreasure(arg_0_3)
    End()
    DisableTreasure(arg_0_3)
    IfObjectActivated(0, obj_act_id=arg_4_7)
    WaitFrames(10)
    EnableTreasure(arg_0_3)


def Event11410260():
    """ 11410260: Event 11410260 """
    DisableNetworkSync()
    IfInsideMap(1, game_map=LOST_IZALITH)
    IfCharacterInsideRegion(1, PLAYER, region=Spheres.PlayerHasEnteredIzalith)
    IfTimeElapsed(1, 3.0)
    IfConditionTrue(0, input_condition=1)
    ActivateKillplaneForModel(game_map=LOST_IZALITH, y_threshold=-400.0, target_model_id=3240)
    Restart()


def Event11410510(_, arg_0_3: int, arg_4_7: int):
    """ 11410510: Event 11410510 """
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


def Event11410520(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11410520: Event 11410520 """
    SkipLinesIfThisEventSlotOff(2)
    DropMandatoryTreasure(arg_0_3)
    End()
    IfHealthLessThanOrEqual(0, arg_0_3, 0.0)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)


def Event11410501(_, arg_0_3: int, arg_4_7: int):
    """ 11410501: Event 11410501 """
    IfFlagOn(-2, 1503)
    IfFlagOn(-2, 1505)
    IfFlagOn(-2, 1506)
    IfFlagOn(-2, 1507)
    IfConditionTrue(1, input_condition=-2)
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


def Event11410530(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11410530: Event 11410530 """
    IfFlagOff(1, 1004)
    IfFlagOn(1, 1007)
    IfFlagOn(1, 11410901)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)
    EnableCharacter(arg_0_3)


def Event11410531(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11410531: Event 11410531 """
    IfFlagOff(1, 1004)
    IfFlagOn(1, 1009)
    IfFlagOff(1, 800)
    IfHost(1)
    IfCharacterInsideRegion(1, PLAYER, region=Spheres.PlayerHasEnteredIzalith)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)
    DisableCharacter(arg_0_3)
    EnableCharacter(Characters.c0000_0003)
    SetTeamTypeAndExitStandbyAnimation(Characters.c0000_0003, TeamType.HostileAlly)
    SaveRequest()


def Event11410532(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11410532: Event 11410532 """
    IfFlagOff(1, 1004)
    IfFlagOn(1, 1009)
    IfFlagOn(1, 800)
    IfHost(1)
    IfCharacterInsideRegion(1, PLAYER, region=Spheres.PlayerHasEnteredIzalith)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)
    Move(
        arg_0_3,
        destination=Boxes.SolaireSaved,
        destination_type=CoordEntityType.Region,
        set_draw_parent=Collisions.h0042B1,
    )
    EnableFlag(11410580)
    IfCharacterBackreadEnabled(0, arg_0_3)
    SetNest(arg_0_3, Boxes.SolaireSaved)


def Event11410533(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11410533: Event 11410533 """
    IfFlagOff(1, 1004)
    IfFlagOn(1, 1003)
    IfFlagOn(1, 11410595)
    IfCharacterAlive(1, arg_0_3)
    IfThisEventOff(1)
    IfHost(2)
    IfFlagOff(2, 1004)
    IfFlagOn(2, arg_12_15)
    IfThisEventOn(2)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)
    DisableCharacter(arg_0_3)


def Event11410534(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11410534: Event 11410534 """
    IfFlagOff(1, 1004)
    IfFlagOn(1, 1002)
    IfHealthLessThanOrEqual(1, arg_0_3, 0.0)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)


def Event11410540(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11410540: Event 11410540 """
    IfFlagOff(1, 1512)
    IfFlagOn(1, 1502)
    IfFlagOn(1, 11400590)
    IfInsideMap(1, game_map=LOST_IZALITH)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)
    EnableCharacter(arg_0_3)
    EnableFlag(814)


def Event11410541(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11410541: Event 11410541 """
    IfFlagOff(1, 1512)
    IfFlagOn(1, 1503)
    IfCharacterAlive(-1, Characters.c3240_0002)
    IfCharacterAlive(-1, Characters.c3240_0003)
    IfCharacterAlive(-1, Characters.c3240_0004)
    IfCharacterAlive(-1, Characters.c3240_0005)
    IfConditionTrue(1, input_condition=-1)
    IfFlagOn(1, 11410590)
    IfFlagOff(2, 1512)
    IfFlagOn(2, 1504)
    IfThisEventOn(2)
    IfConditionTrue(-2, input_condition=1)
    IfConditionTrue(-2, input_condition=2)
    IfConditionTrue(0, input_condition=-2)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)
    ResetStandbyAnimationSettings(arg_0_3)
    EnableCharacter(arg_0_3)
    SetTeamTypeAndExitStandbyAnimation(arg_0_3, TeamType.FightingAlly)
    AddSpecialEffect(arg_0_3, 90111)


def Event11410542(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11410542: Event 11410542 """
    IfFlagOff(1, 1512)
    IfFlagOn(1, 1503)
    IfCharacterDead(1, Characters.c3240_0002)
    IfCharacterDead(1, Characters.c3240_0003)
    IfCharacterDead(1, Characters.c3240_0004)
    IfCharacterDead(1, Characters.c3240_0005)
    IfCharacterAlive(1, arg_0_3)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)


def Event11410543(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11410543: Event 11410543 """
    IfFlagOff(1, 1512)
    IfFlagOn(1, 1504)
    IfHealthLessThan(1, arg_0_3, 0.5)
    IfHealthGreaterThan(1, arg_0_3, 0.0)
    IfCharacterDead(1, Characters.c3240_0002)
    IfCharacterDead(1, Characters.c3240_0003)
    IfCharacterDead(1, Characters.c3240_0004)
    IfCharacterDead(1, Characters.c3240_0005)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)
    SetNest(arg_0_3, Boxes.SiegmeyerNestAfterBattle)


def Event11410544(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11410544: Event 11410544 """
    IfFlagOff(1, 1512)
    IfFlagOn(1, 1504)
    IfHealthGreaterThanOrEqual(1, arg_0_3, 0.5)
    IfCharacterDead(1, Characters.c3240_0002)
    IfCharacterDead(1, Characters.c3240_0003)
    IfCharacterDead(1, Characters.c3240_0004)
    IfCharacterDead(1, Characters.c3240_0005)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)
    SetNest(arg_0_3, Boxes.SiegmeyerNestAfterBattle)


def Event11410545(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11410545: Event 11410545 """
    IfFlagOff(1, 1512)
    IfFlagOn(1, 1506)
    IfFlagOn(1, 11410591)
    IfThisEventOff(1)
    IfFlagOff(2, 1512)
    IfFlagOn(2, arg_12_15)
    IfThisEventOn(2)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)
    SkipLinesIfFinishedConditionTrue(3, 2)
    Kill(arg_0_3, award_souls=True)
    CancelSpecialEffect(arg_0_3, 90111)
    End()
    DropMandatoryTreasure(arg_0_3)


def Event11410546(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11410546: Event 11410546 """
    SkipLinesIfThisEventSlotOff(2)
    DropMandatoryTreasure(arg_0_3)
    End()
    IfFlagOff(1, 1506)
    IfFlagOff(1, 1508)
    IfHealthLessThanOrEqual(1, arg_0_3, 0.0)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)


def Event11410547(_, arg_0_3: int):
    """ 11410547: Event 11410547 """
    EndIfFlagOn(1512)
    SkipLinesIfThisEventSlotOff(3)
    SkipLinesIfFlagOn(1, 11410593)
    ResetStandbyAnimationSettings(arg_0_3)
    End()
    IfThisEventOn(-1)
    IfFlagOn(-1, 1503)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfThisEventOn(1)
    IfFlagOff(0, 814)
    SetStandbyAnimationSettings(arg_0_3, cancel_animation=7856)


def Event11410548(_, arg_0_3: int):
    """ 11410548: Event 11410548 """
    EndIfFlagOn(1512)
    SkipLinesIfThisEventSlotOff(2)
    SetStandbyAnimationSettings(arg_0_3, standby_animation=7855)
    End()
    IfFlagOff(1, 1512)
    IfFlagOn(1, 1507)
    IfFlagOn(1, 11410593)
    IfThisEventOn(2)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    SetStandbyAnimationSettings(arg_0_3, standby_animation=7855)


def Event11410549(_, arg_0_3: int):
    """ 11410549: Event 11410549 """
    IfFlagOff(1, 1512)
    IfFlagOn(1, 1507)
    IfFlagOn(1, 11410594)
    SkipLinesIfThisEventOn(1)
    IfCharacterBackreadDisabled(1, arg_0_3)
    IfConditionTrue(0, input_condition=1)
    DisableCharacter(arg_0_3)


def Event11410550(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11410550: Event 11410550 """
    IfHost(1)
    IfFlagOff(1, 1512)
    IfFlagOn(1, 1505)
    IfFlagOn(1, 11410594)
    SkipLinesIfThisEventOn(1)
    IfCharacterBackreadDisabled(1, arg_0_3)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)
    DisableCharacter(arg_0_3)


def Event11415030():
    """ 11415030: Event 11415030 """
    SkipLinesIfClient(1)
    SetNetworkUpdateAuthority(Characters.c0000_0007, UpdateAuthority.Forced)
    SkipLinesIfFlagOn(3, 11415033)
    IfClient(2)
    IfFlagOn(2, 11415031)
    SkipLinesIfConditionTrue(1, 2)
    DisableCharacter(Characters.c0000_0007)
    EndIfFlagOn(10)
    IfHost(1)
    IfCharacterHuman(1, PLAYER)
    IfFlagOff(1, 1004)
    IfFlagOn(1, 1007)
    IfCharacterBackreadEnabled(1, Characters.c0000_0007)
    IfEntityWithinDistance(1, Characters.c0000_0007, PLAYER, radius=20.0)
    IfConditionTrue(0, input_condition=1)
    PlaceSummonSign(
        SummonSignType.BlueEyeSign,
        Characters.c0000_0007,
        region=Points.SolaireSummonSign,
        summon_flag=11415031,
        dismissal_flag=11415033,
    )


def Event11415029():
    """ 11415029: Event 11415029 """
    SkipLinesIfClient(1)
    SetNetworkUpdateAuthority(Characters.c0000_0007, UpdateAuthority.Forced)
    SkipLinesIfFlagOn(3, 11415033)
    IfClient(2)
    IfFlagOn(2, 11415031)
    SkipLinesIfConditionTrue(1, 2)
    DisableCharacter(Characters.c0000_0007)
    EndIfFlagOn(10)
    IfMultiplayerCount(1, arg1=4, arg2=3)
    IfHost(1)
    IfCharacterHuman(1, PLAYER)
    IfFlagOff(1, 11415031)
    IfFlagOff(1, 11415033)
    IfFlagOff(1, 1004)
    IfFlagOn(1, 1007)
    IfCharacterBackreadEnabled(1, Characters.c0000_0007)
    IfEntityWithinDistance(1, Characters.c0000_0007, PLAYER, radius=20.0)
    IfCharacterHasSpecialEffect(1, PLAYER, 28)
    IfConditionTrue(0, input_condition=1)
    PlaceSummonSign(
        SummonSignType.BlueEyeSign,
        Characters.c0000_0007,
        region=Points.SolaireSummonSign,
        summon_flag=11415031,
        dismissal_flag=11415033,
    )


def Event14015990(_, arg_0_3: int, arg_4_7: int):
    """ 14015990: Event 14015990 """
    IfFlagOn(0, arg_0_3)
    EraseNPCSummonSign(summoned_character=arg_4_7)
    IfFlagOff(0, arg_0_3)
    Restart()


def Event11415032():
    """ 11415032: Event 11415032 """
    EndIfThisEventOn()
    IfFlagOn(1, 11415031)
    IfFlagOn(1, 11415383)
    IfConditionTrue(0, input_condition=1)
    AICommand(Characters.c0000_0007, command_id=10, slot=0)
    ReplanAI(Characters.c0000_0007)
    IfCharacterInsideRegion(0, Characters.c0000_0007, region=Boxes.CentipedeFogPrompt)
    RotateToFaceEntity(Characters.c0000_0007, Boxes.CentipedeFogRotationTarget)
    ForceAnimation(Characters.c0000_0007, 7410)
    AICommand(Characters.c0000_0007, command_id=-1, slot=0)
    ReplanAI(Characters.c0000_0007)


def Event11415035():
    """ 11415035: Event 11415035 """
    DisableNetworkSync()
    EndIfClient()
    EndIfFlagOn(11415036)
    EndIfFlagOn(11410410)
    IfHost(1)
    IfCharacterHuman(1, PLAYER)
    IfFlagOff(1, 11410810)
    SkipLinesIfThisEventOn(1)
    IfCharacterInsideRegion(1, PLAYER, region=Boxes.KirkInvaderTrigger1)
    IfConditionTrue(0, input_condition=1)
    PlaceSummonSign(
        SummonSignType.BlackEyeSign,
        Characters.c0000_0008,
        region=Points.KirkInvaderSpawn1,
        summon_flag=11415036,
        dismissal_flag=11415037,
    )
    Wait(20.0)
    Restart()


def Event11415038():
    """ 11415038: Event 11415038 """
    DisableNetworkSync()
    EndIfClient()
    EndIfFlagOn(11415039)
    EndIfFlagOn(10)
    IfHost(1)
    IfCharacterHuman(1, PLAYER)
    IfFlagOff(1, 11410811)
    SkipLinesIfThisEventOn(1)
    IfCharacterInsideRegion(1, PLAYER, region=Boxes.KirkInvaderTrigger2)
    IfConditionTrue(0, input_condition=1)
    PlaceSummonSign(
        SummonSignType.BlackEyeSign,
        Characters.c0000_0009,
        region=Points.KirkInvaderSpawn2,
        summon_flag=11415039,
        dismissal_flag=11415040,
    )
    Wait(20.0)
    Restart()


def Event11410810(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 11410810: Event 11410810 """
    SkipLinesIfHost(3)
    IfFlagOn(1, arg_4_7)
    IfFlagOff(1, arg_8_11)
    SkipLinesIfConditionTrue(1, 1)
    DisableCharacter(arg_0_3)
    EndIfThisEventSlotOn()
    IfCharacterDead(0, arg_0_3)
    End()


def Event11415843(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11415843: Event 11415843 """
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


def Event11415846(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 11415846: Event 11415846 """
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
