"""
linked:


strings:

"""
from soulstruct.darksouls1r.events import *
from ..entities.m13_00_00_00_entities import *
from ..entities.m13_01_00_00_entities import Objects as m13_01_Objects, Boxes as m13_01_Boxes
from ..entities.common_entities import *


def Constructor():
    """ 0: Event 0 """
    RegisterBonfire(
        11300992,
        obj=Objects.o0200_0000,
        reaction_distance=2.0,
        reaction_angle=180.0,
        initial_kindle_level=0,
    )
    RegisterBonfire(
        11300984,
        obj=Objects.o0200_0001,
        reaction_distance=2.0,
        reaction_angle=180.0,
        initial_kindle_level=0,
    )
    RegisterBonfire(
        11300976,
        obj=Objects.o0200_0003,
        reaction_distance=2.0,
        reaction_angle=180.0,
        initial_kindle_level=0,
    )
    RegisterLadder(start_climbing_flag=11300010, stop_climbing_flag=11300011, obj=Objects.o3040_0000)
    RegisterLadder(start_climbing_flag=11300012, stop_climbing_flag=11300013, obj=Objects.o3041_0000)
    RegisterLadder(start_climbing_flag=11300014, stop_climbing_flag=11300015, obj=Objects.o3042_0000)
    SkipLinesIfFlagOff(1, 6)
    RegisterLadder(start_climbing_flag=11300016, stop_climbing_flag=11300017, obj=Objects.o3043_0000)
    RegisterLadder(start_climbing_flag=11300018, stop_climbing_flag=11300019, obj=Objects.o3044_0000)
    RegisterLadder(start_climbing_flag=11300020, stop_climbing_flag=11300021, obj=Objects.o3045_0000)
    RegisterLadder(start_climbing_flag=11300022, stop_climbing_flag=11300023, obj=Objects.o3046_0000)
    RegisterLadder(start_climbing_flag=11300024, stop_climbing_flag=11300025, obj=Objects.o3046_0001)
    RegisterLadder(start_climbing_flag=11300026, stop_climbing_flag=11300027, obj=Objects.o3047_0000)
    RegisterLadder(start_climbing_flag=11300028, stop_climbing_flag=11300029, obj=Objects.o3048_0000)
    SkipLinesIfClient(3)
    DisableFlag(11300000)
    DisableObject(Objects.o3951_0000)
    DeleteVFX(VFX.MultiplayerFog1, erase_root_only=False)
    RunEvent(
        11300090,
        slot=0,
        args=(Objects.o3952_0000, VFX.CheckpointFog1, Boxes.CheckpointFog1FrontSide, Boxes.CheckpoingFog1BackSide),
    )
    RunEvent(11300800)
    RunEvent(11300300)
    RunEvent(11300350)
    RunEvent(11300900, slot=0, args=(11300900, Objects.o3011_0000, Objects.o3020_0000, Navigation.InvaderSpawn00))
    RunEvent(11300900, slot=1, args=(11300901, Objects.o3011_0003, Objects.o3021_0000, Navigation.Navmesh_MiddleGate))
    RunEvent(11305032, slot=0, args=(11300902, 11300903, 11305035, 11305036))
    RunEvent(
        11305030,
        slot=0,
        args=(11300402, 11305035, 11305036, Objects.o3011_0001, Objects.o3000_0000, Navigation.Navmesh_BridgeA),
    )
    RunEvent(11305032, slot=1, args=(11300904, 11300905, 11305037, 11305038))
    RunEvent(
        11305030,
        slot=1,
        args=(11300403, 11305037, 11305038, Objects.o3011_0002, Objects.o3001_0000, Navigation.Navmesh_BridgeB),
    )
    RunEvent(11305000)
    RunEvent(11305001)
    RunEvent(11305002)
    RunEvent(11305003)
    RunEvent(11305004)
    RunEvent(11305009)
    RunEvent(11300420, slot=0, args=(10000,))
    RunEvent(11300420, slot=1, args=(10001,))
    RunEvent(11300420, slot=2, args=(10002,))
    RunEvent(11300420, slot=3, args=(10003,))
    RunEvent(11300420, slot=4, args=(10004,))
    RunEvent(11300420, slot=5, args=(10005,))
    RunEvent(11300420, slot=6, args=(10006,))
    RunEvent(11300420, slot=7, args=(10007,))
    RunEvent(11300420, slot=8, args=(10008,))
    RunEvent(11300420, slot=9, args=(10009,))
    RunEvent(11300420, slot=10, args=(10010,))
    RunEvent(11300420, slot=11, args=(10011,))
    RunEvent(11300420, slot=12, args=(10012,))
    RunEvent(11300420, slot=13, args=(10013,))
    RunEvent(11300420, slot=14, args=(10014,))
    RunEvent(11300420, slot=15, args=(10015,))
    RunEvent(11300420, slot=16, args=(10016,))
    RunEvent(11300420, slot=17, args=(10017,))
    RunEvent(11300210)
    RunEvent(11305060)
    RunEvent(11300200)
    RunEvent(11305045)
    RunEvent(11300100, slot=0, args=(11300100, Cylinders.FloorBreakTriggerA, Objects.o3030_0000, 303000000))
    RunEvent(11300100, slot=1, args=(11300101, Cylinders.FloorBreakTriggerB, Objects.o3031_0000, 303100000))
    RunEvent(11300100, slot=2, args=(11300102, Cylinders.FloorBreakTriggerC, Objects.o3032_0000, 303200000))
    RunEvent(11300100, slot=3, args=(11300103, Cylinders.FloorBreakTriggerD, Objects.o3033_0000, 303300000))
    RunEvent(11300100, slot=4, args=(11300104, Cylinders.FloorBreakTriggerE, Objects.o3034_0000, 303400000))
    RunEvent(11300100, slot=5, args=(11300105, Cylinders.FloorBreakTriggerF, Objects.o3035_0000, 303500000))
    RunEvent(11300150)
    RunEvent(11300160)
    RunEvent(11300700, slot=0, args=(Objects.o3321_0000, 11300750))
    RunEvent(11300700, slot=1, args=(Objects.o3321_0001, 11300751))
    RunEvent(11300700, slot=2, args=(Objects.o3321_0002, 11300752))
    RunEvent(11300700, slot=3, args=(Objects.o3321_0003, 11300753))
    RunEvent(11300700, slot=4, args=(Objects.o3321_0004, 11300754))
    RunEvent(11300700, slot=5, args=(Objects.o3321_0005, 11300755))
    RunEvent(11300700, slot=6, args=(Objects.o3321_0006, 11300756))
    RunEvent(11300700, slot=7, args=(Objects.o3321_0007, 11300757))
    RunEvent(11300700, slot=8, args=(Objects.o3321_0008, 11300758))
    RunEvent(11300700, slot=9, args=(Objects.o3321_0009, 11300759))
    RunEvent(11300700, slot=10, args=(Objects.o3321_0010, 11300760))
    RunEvent(11300700, slot=12, args=(Objects.o3321_0011, 11300762))
    RunEvent(11300700, slot=13, args=(Objects.o3321_1004, 11300763))
    RunEvent(11300700, slot=14, args=(Objects.o3321_1005, 11300764))
    RunEvent(11300700, slot=15, args=(Objects.o3321_1006, 11300765))
    RunEvent(11300700, slot=16, args=(Objects.o3321_1007, 11300766))
    RunEvent(11300700, slot=17, args=(Objects.o3321_1008, 11300767))
    RunEvent(11300700, slot=18, args=(Objects.o3321_1009, 11300768))
    RunEvent(11300700, slot=19, args=(Objects.o3321_1010, 11300769))
    RunEvent(11300880)
    DisableSoundEvent(1303800)
    SkipLinesIfFlagOff(4, 6)
    DisableObject(Objects.o3954_0000)
    DeleteVFX(VFX.PinwheelEntranceFog, erase_root_only=False)
    RunEvent(11305392)
    SkipLines(32)
    RunEvent(11305390)
    RunEvent(11305391)
    RunEvent(11305393)
    RunEvent(11305392)
    RunEvent(11300001)
    RunEvent(11305394)
    RunEvent(11305395)
    RunEvent(11300882)
    RunEvent(11305396)
    RunEvent(11305397)
    RunEvent(11305398)
    RunEvent(11305250)
    RunEvent(
        11305350,
        slot=0,
        args=(
            11305251,
            11305252,
            Characters.c3320_0001,
            Characters.c3320_0002,
            Boxes.PinwheelWarpPoint00,
            Boxes.PinwheelWarpPoint12,
            11305300,
        ),
    )
    RunEvent(
        11305350,
        slot=1,
        args=(
            11305253,
            11305254,
            Characters.c3320_0003,
            Characters.c3320_0004,
            Boxes.PinwheelWarpPoint01,
            Boxes.PinwheelWarpPoint11,
            11305301,
        ),
    )
    RunEvent(
        11305350,
        slot=2,
        args=(
            11305255,
            11305256,
            Characters.c3320_0005,
            Characters.c3320_0006,
            Boxes.PinwheelWarpPoint02,
            Boxes.PinwheelWarpPoint10,
            11305302,
        ),
    )
    RunEvent(
        11305350,
        slot=3,
        args=(
            11305257,
            11305258,
            Characters.c3320_0007,
            Characters.c3320_0008,
            Boxes.PinwheelWarpPoint03,
            Boxes.PinwheelWarpPoint09,
            11305303,
        ),
    )
    RunEvent(
        11305350,
        slot=4,
        args=(
            11305259,
            11305260,
            Characters.c3320_0009,
            Characters.c3320_0010,
            Boxes.PinwheelWarpPoint04,
            Boxes.PinwheelWarpPoint08,
            11305304,
        ),
    )
    RunEvent(
        11305350,
        slot=5,
        args=(
            11305261,
            11305262,
            Characters.c3320_0011,
            Characters.c3320_0012,
            Boxes.PinwheelWarpPoint05,
            Boxes.PinwheelWarpPoint07,
            11305305,
        ),
    )
    RunEvent(
        11305350,
        slot=6,
        args=(
            11305263,
            11305264,
            Characters.c3320_0013,
            Characters.c3320_0014,
            Boxes.PinwheelWarpPoint06,
            Boxes.PinwheelWarpPoint06,
            11305306,
        ),
    )
    RunEvent(11305370, slot=0, args=(Characters.c3320_0001, 11305251))
    RunEvent(11305370, slot=1, args=(Characters.c3320_0002, 11305252))
    RunEvent(11305370, slot=2, args=(Characters.c3320_0003, 11305253))
    RunEvent(11305370, slot=3, args=(Characters.c3320_0004, 11305254))
    RunEvent(11305370, slot=4, args=(Characters.c3320_0005, 11305255))
    RunEvent(11305370, slot=5, args=(Characters.c3320_0006, 11305256))
    RunEvent(11305370, slot=6, args=(Characters.c3320_0007, 11305257))
    RunEvent(11305370, slot=7, args=(Characters.c3320_0008, 11305258))
    RunEvent(11305370, slot=8, args=(Characters.c3320_0009, 11305259))
    RunEvent(11305370, slot=9, args=(Characters.c3320_0010, 11305260))
    RunEvent(11305370, slot=10, args=(Characters.c3320_0011, 11305261))
    RunEvent(11305370, slot=11, args=(Characters.c3320_0012, 11305262))
    RunEvent(11305370, slot=12, args=(Characters.c3320_0013, 11305263))
    RunEvent(11305370, slot=13, args=(Characters.c3320_0014, 11305264))
    RunEvent(11300850, slot=0, args=(Characters.c2650_0000, 0))
    RunEvent(11300850, slot=1, args=(Characters.c2650_0001, 0))
    RunEvent(11300850, slot=2, args=(Characters.c2650_0002, 0))
    RunEvent(11300850, slot=3, args=(Characters.c2650_0003, 0))
    RunEvent(11300850, slot=4, args=(Characters.c2650_0004, 0))
    RunEvent(11300850, slot=5, args=(Characters.c2650_0005, 0))
    RunEvent(11300850, slot=6, args=(Characters.c3300_0000, 33003000))
    RunEvent(11300850, slot=7, args=(Characters.c3300_0001, 33003000))
    RunEvent(11300850, slot=8, args=(Characters.c2300_0000, 0))
    RunEvent(11300850, slot=9, args=(Characters.c2794_0000, 27902000))
    RunEvent(11305846, slot=0, args=(6, Objects.o3954_0000, VFX.PinwheelEntranceFog))
    RunEvent(11305843, slot=0, args=(6, Objects.o3954_0000, Boxes.PinwheelFogPrompt, Boxes.PinwheelFogRotationTarget))
    # <!--!>


def Preconstructor():
    """ 50: Event 50 """
    HumanityRegistration(Characters.c0000_0004, 8948)
    RunEvent(11305025)
    RunEvent(11305029)
    RunEvent(11305027)
    RunEvent(11305990, slot=0, args=(11305026, Characters.c0000_0004))
    RunEvent(11300510, slot=0, args=(Characters.c2920_0000, 1341))
    RunEvent(11300520, slot=0, args=(Characters.c2920_0000, 1340, 1343, 1342))
    RunEvent(11305061, slot=0, args=(Characters.c2920_0000,))
    HumanityRegistration(Characters.c0000_0002, 8478)
    SkipLinesIfFlagOn(2, 1627)
    SkipLinesIfFlagRangeAnyOn(1, (1620, 1621))
    DisableCharacter(Characters.c0000_0002)
    RunEvent(11300510, slot=1, args=(Characters.c0000_0002, 1627))
    RunEvent(11300531, slot=0, args=(Characters.c0000_0002, 1628))
    RunEvent(11300530, slot=0, args=(Characters.c0000_0002, 1620, 1631, 1621))
    RunEvent(11300533, slot=0, args=(Characters.c0000_0002, 1620, 1631, 1623))
    RunEvent(11300592)
    RunEvent(11300593)


def Event11300090(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11300090: Event 11300090 """
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


def Event11305390():
    """ 11305390: Event 11305390 """
    IfFlagOff(1, 6)
    IfCharacterAlive(1, Characters.c3320_0000)
    IfActionButton(
        1,
        prompt_text=10010403,
        anchor_entity=Boxes.PinwheelFogPrompt,
        anchor_type=CoordEntityType.Region,
        line_intersects=Objects.o3954_0000,
        boss_version=True,
    )
    IfConditionTrue(0, input_condition=1)
    RotateToFaceEntity(PLAYER, Boxes.PinwheelFogRotationTarget)
    ForceAnimation(PLAYER, 7410)
    Restart()


def Event11305391():
    """ 11305391: Event 11305391 """
    IfFlagOff(1, 6)
    IfFlagOn(1, 11305393)
    IfCharacterType(1, PLAYER, CharacterType.WhitePhantom)
    IfActionButton(
        1,
        prompt_text=10010403,
        anchor_entity=Boxes.PinwheelFogPrompt,
        anchor_type=CoordEntityType.Region,
        trigger_attribute=TriggerAttribute.All,
        line_intersects=Objects.o3954_0000,
    )
    IfConditionTrue(0, input_condition=1)
    RotateToFaceEntity(PLAYER, Boxes.PinwheelFogRotationTarget)
    ForceAnimation(PLAYER, 7410)
    Restart()


def Event11305393():
    """ 11305393: Event 11305393 """
    SkipLinesIfThisEventOn(3)
    IfFlagOff(1, 6)
    IfFlagOn(1, 11305390)
    IfCharacterInsideRegion(1, PLAYER, region=Boxes.PinwheelNotify)
    IfConditionTrue(0, input_condition=1)
    SkipLinesIfClient(1)
    NotifyBossBattleStart()
    ActivateMultiplayerBuffs(Characters.c3320_0000)


@RestartOnRest
def Event11305392():
    """ 11305392: Event 11305392 """
    SkipLinesIfFlagOff(3, 6)
    DisableCharacter(Characters.c3320_0000)
    Kill(Characters.c3320_0000, award_souls=False)
    End()
    SkipLinesIfFlagOn(1, 11300000)
    DisableCharacter(Characters.c3320_0000)
    DisableAI(Characters.c3320_0000)
    IfFlagOff(1, 6)
    IfHost(1)
    IfCharacterInsideRegion(1, PLAYER, region=Boxes.PinwheelCutsceneTrigger)
    IfConditionTrue(0, input_condition=1)
    SkipLinesIfFlagOn(8, 11300000)
    SkipLinesIfMultiplayer(2)
    PlayCutscene(130000, skippable=True, fade_out=False, player_id=PLAYER)
    SkipLines(1)
    PlayCutscene(130000, skippable=False, fade_out=False, player_id=PLAYER)
    WaitFrames(1)
    EnableCharacter(Characters.c3320_0000)
    EnableFlag(11300000)
    EnableFlag(11300005)
    SkipLinesIfClient(1)
    SetNetworkUpdateAuthority(Characters.c3320_0000, UpdateAuthority.Forced)
    EnableAI(Characters.c3320_0000)
    EnableBossHealthBar(Characters.c3320_0000, name=3320, slot=0)


def Event11300001():
    """ 11300001: Event 11300001 """
    IfHealthLessThanOrEqual(0, Characters.c3320_0000, 0.0)
    Wait(1.0)
    PlaySoundEffect(anchor_entity=Characters.c3320_0000, sound_type=SoundType.s_SFX, sound_id=777777777)
    IfCharacterDead(0, Characters.c3320_0000)
    EnableFlag(6)
    KillBoss(1300800)
    DisableObject(Objects.o3954_0000)
    DeleteVFX(VFX.PinwheelEntranceFog, erase_root_only=True)
    RegisterLadder(start_climbing_flag=11300016, stop_climbing_flag=11300017, obj=Objects.o3043_0000)
    RunEvent(11300880)


def Event11305394():
    """ 11305394: Event 11305394 """
    DisableNetworkSync()
    IfFlagOff(1, 6)
    IfFlagOn(1, 11305392)
    SkipLinesIfHost(1)
    IfFlagOn(1, 11305391)
    IfConditionTrue(0, input_condition=1)
    EnableSoundEvent(1303800)


def Event11305395():
    """ 11305395: Event 11305395 """
    DisableNetworkSync()
    IfFlagOn(1, 6)
    IfFlagOn(1, 11305394)
    IfConditionTrue(0, input_condition=1)
    DisableSoundEvent(1303800)


def Event11305396():
    """ 11305396: Event 11305396 """
    IfHasTAEEvent(0, Characters.c3320_0000, tae_event_id=600)
    DisableCharacter(Characters.c3320_0000)
    DisableFlagRange((11305320, 11305326))
    SkipLinesIfClient(2)
    SetNetworkUpdateAuthority(Characters.c3320_0000, UpdateAuthority.Forced)
    EnableRandomFlagInRange((11305320, 11305326))
    EnableFlag(11305329)
    IfFlagOff(-1, 11305329)
    IfTimeElapsed(-1, 5.0)
    IfConditionTrue(0, input_condition=-1)
    Wait(3.0)
    EnableCharacter(Characters.c3320_0000)
    SkipLinesIfFlagOff(1, 11305320)
    Move(
        Characters.c3320_0000,
        destination=Boxes.PinwheelWarpPoint00,
        destination_type=CoordEntityType.Region,
        short_move=True,
    )
    SkipLinesIfFlagOff(1, 11305321)
    Move(
        Characters.c3320_0000,
        destination=Boxes.PinwheelWarpPoint02,
        destination_type=CoordEntityType.Region,
        short_move=True,
    )
    SkipLinesIfFlagOff(1, 11305322)
    Move(
        Characters.c3320_0000,
        destination=Boxes.PinwheelWarpPoint04,
        destination_type=CoordEntityType.Region,
        short_move=True,
    )
    SkipLinesIfFlagOff(1, 11305323)
    Move(
        Characters.c3320_0000,
        destination=Boxes.PinwheelWarpPoint05,
        destination_type=CoordEntityType.Region,
        short_move=True,
    )
    SkipLinesIfFlagOff(1, 11305324)
    Move(
        Characters.c3320_0000,
        destination=Boxes.PinwheelWarpPoint06,
        destination_type=CoordEntityType.Region,
        short_move=True,
    )
    SkipLinesIfFlagOff(1, 11305325)
    Move(
        Characters.c3320_0000,
        destination=Boxes.PinwheelWarpPoint08,
        destination_type=CoordEntityType.Region,
        short_move=True,
    )
    SkipLinesIfFlagOff(1, 11305326)
    Move(
        Characters.c3320_0000,
        destination=Boxes.PinwheelWarpPoint12,
        destination_type=CoordEntityType.Region,
        short_move=True,
    )
    WaitFrames(1)
    EnableCharacter(Characters.c3320_0000)
    ForceAnimation(Characters.c3320_0000, 7000, wait_for_completion=True)
    Restart()


def Event11300882():
    """ 11300882: Event 11300882 """
    IfFlagOn(1, 11305329)
    IfFlagOn(2, 11305329)
    IfFlagOn(3, 11305329)
    IfFlagOn(4, 11305329)
    IfFlagOn(5, 11305329)
    IfFlagOn(6, 11305329)
    IfFlagOn(7, 11305329)
    IfFlagOn(1, 11305320)
    IfFlagOn(2, 11305321)
    IfFlagOn(3, 11305322)
    IfFlagOn(4, 11305323)
    IfFlagOn(5, 11305324)
    IfFlagOn(6, 11305325)
    IfFlagOn(7, 11305326)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(-1, input_condition=4)
    IfConditionTrue(-1, input_condition=5)
    IfConditionTrue(-1, input_condition=6)
    IfConditionTrue(-1, input_condition=7)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionFalse(1, 1)
    EnableFlag(11305320)
    SkipLinesIfFinishedConditionFalse(1, 2)
    EnableFlag(11305321)
    SkipLinesIfFinishedConditionFalse(1, 3)
    EnableFlag(11305322)
    SkipLinesIfFinishedConditionFalse(1, 4)
    EnableFlag(11305323)
    SkipLinesIfFinishedConditionFalse(1, 5)
    EnableFlag(11305324)
    SkipLinesIfFinishedConditionFalse(1, 6)
    EnableFlag(11305325)
    SkipLinesIfFinishedConditionFalse(1, 7)
    EnableFlag(11305326)
    DisableFlag(11305329)
    Restart()


def Event11305397():
    """ 11305397: Event 11305397 """
    EndIfClient()
    SkipLinesIfFlagOn(4, 11305310)
    IfFlagOff(1, 11305399)
    IfHasTAEEvent(1, Characters.c3320_0000, tae_event_id=700)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(11305310)
    DisableFlagRange((11305300, 11305306))
    EnableRandomFlagInRange((11305300, 11305306))
    SkipLinesIfFlagOff(2, 11305300)
    SkipLinesIfFlagRangeAnyOn(1, (11305251, 11305252))
    DisableFlag(11305310)
    SkipLinesIfFlagOff(2, 11305301)
    SkipLinesIfFlagRangeAnyOn(1, (11305253, 11305254))
    DisableFlag(11305310)
    SkipLinesIfFlagOff(2, 11305302)
    SkipLinesIfFlagRangeAnyOn(1, (11305255, 11305256))
    DisableFlag(11305310)
    SkipLinesIfFlagOff(2, 11305303)
    SkipLinesIfFlagRangeAnyOn(1, (11305257, 11305258))
    DisableFlag(11305310)
    SkipLinesIfFlagOff(2, 11305304)
    SkipLinesIfFlagRangeAnyOn(1, (11305259, 11305260))
    DisableFlag(11305310)
    SkipLinesIfFlagOff(2, 11305305)
    SkipLinesIfFlagRangeAnyOn(1, (11305261, 11305262))
    DisableFlag(11305310)
    SkipLinesIfFlagOff(2, 11305306)
    SkipLinesIfFlagRangeAnyOn(1, (11305263, 11305264))
    DisableFlag(11305310)
    RestartIfFlagOn(11305310)
    IfDoesNotHaveTAEEvent(0, Characters.c3320_0000, tae_event_id=700)
    Restart()


def Event11305398():
    """ 11305398: Event 11305398 """
    IfHealthLessThanOrEqual(0, Characters.c3320_0000, 0.30000001192092896)
    EnableFlag(11305399)
    AICommand(Characters.c3320_0000, command_id=1, slot=1)
    ReplanAI(Characters.c3320_0000)
    RunEvent(11305330, slot=0, args=(Characters.c3320_0001, 11305251))
    RunEvent(11305330, slot=1, args=(Characters.c3320_0002, 11305252))
    RunEvent(11305330, slot=2, args=(Characters.c3320_0003, 11305253))
    RunEvent(11305330, slot=3, args=(Characters.c3320_0004, 11305254))
    RunEvent(11305330, slot=4, args=(Characters.c3320_0005, 11305255))
    RunEvent(11305330, slot=5, args=(Characters.c3320_0006, 11305256))
    RunEvent(11305330, slot=6, args=(Characters.c3320_0007, 11305257))
    RunEvent(11305330, slot=7, args=(Characters.c3320_0008, 11305258))
    RunEvent(11305330, slot=8, args=(Characters.c3320_0009, 11305259))
    RunEvent(11305330, slot=9, args=(Characters.c3320_0010, 11305260))
    RunEvent(11305330, slot=10, args=(Characters.c3320_0011, 11305261))
    RunEvent(11305330, slot=11, args=(Characters.c3320_0012, 11305262))
    RunEvent(11305330, slot=12, args=(Characters.c3320_0013, 11305263))
    RunEvent(11305330, slot=13, args=(Characters.c3320_0014, 11305264))
    IfFlagRangeAllOff(0, (11305251, 11305264))
    AICommand(Characters.c3320_0000, command_id=2, slot=1)
    ReplanAI(Characters.c3320_0000)
    IfFlagOn(1, 11305399)
    IfHasTAEEvent(1, Characters.c3320_0000, tae_event_id=700)
    IfConditionTrue(0, input_condition=1)
    AICommand(Characters.c3320_0000, command_id=1, slot=1)
    ReplanAI(Characters.c3320_0000)
    RunEvent(
        11305350,
        slot=10,
        args=(
            11305251,
            11305252,
            Characters.c3320_0001,
            Characters.c3320_0002,
            Boxes.PinwheelWarpPoint02,
            Boxes.PinwheelWarpPoint03,
            11305300,
        ),
    )
    RunEvent(
        11305350,
        slot=11,
        args=(
            11305253,
            11305254,
            Characters.c3320_0003,
            Characters.c3320_0004,
            Boxes.PinwheelWarpPoint04,
            Boxes.PinwheelWarpPoint05,
            11305301,
        ),
    )
    RunEvent(
        11305350,
        slot=12,
        args=(
            11305255,
            11305256,
            Characters.c3320_0005,
            Characters.c3320_0006,
            Boxes.PinwheelWarpPoint07,
            Boxes.PinwheelWarpPoint08,
            11305302,
        ),
    )
    RunEvent(
        11305350,
        slot=13,
        args=(
            11305257,
            11305258,
            Characters.c3320_0007,
            Characters.c3320_0008,
            Boxes.PinwheelWarpPoint09,
            Boxes.PinwheelWarpPoint12,
            11305303,
        ),
    )


def Event11305330(_, arg_0_3: int, arg_4_7: int):
    """ 11305330: Event 11305330 """
    AICommand(arg_0_3, command_id=1, slot=1)
    ReplanAI(arg_0_3)
    IfFlagOff(0, arg_4_7)
    AICommand(arg_0_3, command_id=-1, slot=1)
    ReplanAI(arg_0_3)


def Event11305350(
    _,
    arg_0_3: int,
    arg_4_7: int,
    arg_8_11: int,
    arg_12_15: int,
    arg_16_19: int,
    arg_20_23: int,
    arg_24_27: int,
):
    """ 11305350: Event 11305350 """
    SkipLinesIfFlagOn(5, 11305399)
    IfHost(1)
    IfFlagOff(1, 11305310)
    IfFlagOn(1, arg_24_27)
    IfConditionTrue(0, input_condition=1)
    WaitForNetworkApproval(max_seconds=3.0)
    DisableFlag(arg_24_27)
    AddSpecialEffect(arg_8_11, 5450)
    AddSpecialEffect(arg_12_15, 5450)
    Move(arg_8_11, destination=arg_16_19, destination_type=CoordEntityType.Region, short_move=True)
    Move(arg_12_15, destination=arg_20_23, destination_type=CoordEntityType.Region, short_move=True)
    EnableCharacter(arg_8_11)
    EnableCharacter(arg_12_15)
    ReplanAI(arg_8_11)
    ReplanAI(arg_12_15)
    ForceAnimation(arg_8_11, 7000)
    ForceAnimation(arg_12_15, 7000)
    EnableFlag(arg_0_3)
    EnableFlag(arg_4_7)
    EndIfFlagOn(11305399)
    RestartEvent(11305250)
    Restart()


def Event11305370(_, arg_0_3: int, arg_4_7: int):
    """ 11305370: Event 11305370 """
    IfFlagOn(1, arg_4_7)
    IfHasTAEEvent(1, arg_0_3, tae_event_id=710)
    IfHealthLessThanOrEqual(2, Characters.c3320_0000, 0.0)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    WaitForNetworkApproval(max_seconds=3.0)
    SkipLinesIfFinishedConditionTrue(3, 1)
    AICommand(arg_0_3, command_id=1, slot=1)
    ReplanAI(arg_0_3)
    IfHasTAEEvent(0, arg_0_3, tae_event_id=710)
    SetNetworkUpdateRate(arg_0_3, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    ResetAnimation(arg_0_3, disable_interpolation=True)
    DisableCharacter(arg_0_3)
    DisableFlag(arg_4_7)
    EndIfFinishedConditionTrue(2)
    RestartEvent(11305250)
    RestartIfFlagOff(arg_4_7)


def Event11305250():
    """ 11305250: Event 11305250 """
    IfFlagOn(0, 11305392)
    AIEvent(Characters.c3320_0000, command_id=0, slot=0, first_event_flag=11305251, last_event_flag=11305264)
    AIEvent(Characters.c3320_0001, command_id=0, slot=0, first_event_flag=11305251, last_event_flag=11305264)
    AIEvent(Characters.c3320_0002, command_id=0, slot=0, first_event_flag=11305251, last_event_flag=11305264)
    AIEvent(Characters.c3320_0003, command_id=0, slot=0, first_event_flag=11305251, last_event_flag=11305264)
    AIEvent(Characters.c3320_0004, command_id=0, slot=0, first_event_flag=11305251, last_event_flag=11305264)
    AIEvent(Characters.c3320_0005, command_id=0, slot=0, first_event_flag=11305251, last_event_flag=11305264)
    AIEvent(Characters.c3320_0006, command_id=0, slot=0, first_event_flag=11305251, last_event_flag=11305264)
    AIEvent(Characters.c3320_0007, command_id=0, slot=0, first_event_flag=11305251, last_event_flag=11305264)
    AIEvent(Characters.c3320_0008, command_id=0, slot=0, first_event_flag=11305251, last_event_flag=11305264)
    AIEvent(Characters.c3320_0009, command_id=0, slot=0, first_event_flag=11305251, last_event_flag=11305264)
    AIEvent(Characters.c3320_0010, command_id=0, slot=0, first_event_flag=11305251, last_event_flag=11305264)
    AIEvent(Characters.c3320_0011, command_id=0, slot=0, first_event_flag=11305251, last_event_flag=11305264)
    AIEvent(Characters.c3320_0012, command_id=0, slot=0, first_event_flag=11305251, last_event_flag=11305264)
    AIEvent(Characters.c3320_0013, command_id=0, slot=0, first_event_flag=11305251, last_event_flag=11305264)
    AIEvent(Characters.c3320_0014, command_id=0, slot=0, first_event_flag=11305251, last_event_flag=11305264)
    ReplanAI(Characters.c3320_0000)
    ReplanAI(Characters.c3320_0001)
    ReplanAI(Characters.c3320_0002)
    ReplanAI(Characters.c3320_0003)
    ReplanAI(Characters.c3320_0004)
    ReplanAI(Characters.c3320_0005)
    ReplanAI(Characters.c3320_0006)
    ReplanAI(Characters.c3320_0007)
    ReplanAI(Characters.c3320_0008)
    ReplanAI(Characters.c3320_0009)
    ReplanAI(Characters.c3320_0010)
    ReplanAI(Characters.c3320_0011)
    ReplanAI(Characters.c3320_0012)
    ReplanAI(Characters.c3320_0013)
    ReplanAI(Characters.c3320_0014)
    IfCharacterDead(0, Characters.c3320_0000)
    End()


@RestartOnRest
def Event11300880():
    """ 11300880: Event 11300880 """
    DisableHealthBar(Characters.c3320_0001)
    DisableHealthBar(Characters.c3320_0002)
    DisableHealthBar(Characters.c3320_0003)
    DisableHealthBar(Characters.c3320_0004)
    DisableHealthBar(Characters.c3320_0005)
    DisableHealthBar(Characters.c3320_0006)
    DisableHealthBar(Characters.c3320_0007)
    DisableHealthBar(Characters.c3320_0008)
    DisableHealthBar(Characters.c3320_0009)
    DisableHealthBar(Characters.c3320_0010)
    DisableHealthBar(Characters.c3320_0011)
    DisableHealthBar(Characters.c3320_0012)
    DisableHealthBar(Characters.c3320_0013)
    DisableHealthBar(Characters.c3320_0014)
    DisableCharacter(Characters.c3320_0001)
    DisableCharacter(Characters.c3320_0002)
    DisableCharacter(Characters.c3320_0003)
    DisableCharacter(Characters.c3320_0004)
    DisableCharacter(Characters.c3320_0005)
    DisableCharacter(Characters.c3320_0006)
    DisableCharacter(Characters.c3320_0007)
    DisableCharacter(Characters.c3320_0008)
    DisableCharacter(Characters.c3320_0009)
    DisableCharacter(Characters.c3320_0010)
    DisableCharacter(Characters.c3320_0011)
    DisableCharacter(Characters.c3320_0012)
    DisableCharacter(Characters.c3320_0013)
    DisableCharacter(Characters.c3320_0014)
    SkipLinesIfFlagOn(14, 6)
    EnableImmortality(Characters.c3320_0001)
    EnableImmortality(Characters.c3320_0002)
    EnableImmortality(Characters.c3320_0003)
    EnableImmortality(Characters.c3320_0004)
    EnableImmortality(Characters.c3320_0005)
    EnableImmortality(Characters.c3320_0006)
    EnableImmortality(Characters.c3320_0007)
    EnableImmortality(Characters.c3320_0008)
    EnableImmortality(Characters.c3320_0009)
    EnableImmortality(Characters.c3320_0010)
    EnableImmortality(Characters.c3320_0011)
    EnableImmortality(Characters.c3320_0012)
    EnableImmortality(Characters.c3320_0013)
    EnableImmortality(Characters.c3320_0014)
    EndIfFlagOff(6)
    Kill(Characters.c3320_0001, award_souls=False)
    Kill(Characters.c3320_0002, award_souls=False)
    Kill(Characters.c3320_0003, award_souls=False)
    Kill(Characters.c3320_0004, award_souls=False)
    Kill(Characters.c3320_0005, award_souls=False)
    Kill(Characters.c3320_0006, award_souls=False)
    Kill(Characters.c3320_0007, award_souls=False)
    Kill(Characters.c3320_0008, award_souls=False)
    Kill(Characters.c3320_0009, award_souls=False)
    Kill(Characters.c3320_0010, award_souls=False)
    Kill(Characters.c3320_0011, award_souls=False)
    Kill(Characters.c3320_0012, award_souls=False)
    Kill(Characters.c3320_0013, award_souls=False)
    Kill(Characters.c3320_0014, award_souls=False)


def Event11300700(_, arg_0_3: int, arg_4_7: int):
    """ 11300700: Event 11300700 """
    IfEntityWithinDistance(0, arg_0_3, PLAYER, radius=1.5)
    CreateHazard(
        arg_4_7,
        arg_0_3,
        model_point=100,
        behavior_param_id=5120,
        target_type=DamageTargetType.Character,
        radius=0.10000000149011612,
        life=1.0,
        repetition_time=0.0,
    )
    CreateHazard(
        arg_4_7,
        arg_0_3,
        model_point=101,
        behavior_param_id=5120,
        target_type=DamageTargetType.Character,
        radius=0.10000000149011612,
        life=1.0,
        repetition_time=0.0,
    )
    CreateHazard(
        arg_4_7,
        arg_0_3,
        model_point=102,
        behavior_param_id=5120,
        target_type=DamageTargetType.Character,
        radius=0.10000000149011612,
        life=1.0,
        repetition_time=0.0,
    )
    ForceAnimation(arg_0_3, 0, wait_for_completion=True)
    Restart()


def Event11300300():
    """ 11300300: Event 11300300 """
    IfFlagOff(0, 11300402)
    CreateHazard(
        11300301,
        Objects.o3000_0000,
        model_point=2,
        behavior_param_id=5100,
        target_type=DamageTargetType.Character,
        radius=0.5,
        life=10.0,
        repetition_time=5.0,
    )
    CreateHazard(
        11300302,
        Objects.o3000_0000,
        model_point=4,
        behavior_param_id=5100,
        target_type=DamageTargetType.Character,
        radius=1.0,
        life=10.0,
        repetition_time=5.0,
    )
    CreateHazard(
        11300303,
        Objects.o3000_0000,
        model_point=6,
        behavior_param_id=5100,
        target_type=DamageTargetType.Character,
        radius=1.0,
        life=10.0,
        repetition_time=5.0,
    )
    CreateHazard(
        11300304,
        Objects.o3000_0000,
        model_point=8,
        behavior_param_id=5100,
        target_type=DamageTargetType.Character,
        radius=1.0,
        life=10.0,
        repetition_time=5.0,
    )
    CreateHazard(
        11300305,
        Objects.o3000_0000,
        model_point=10,
        behavior_param_id=5100,
        target_type=DamageTargetType.Character,
        radius=1.0,
        life=10.0,
        repetition_time=5.0,
    )
    CreateHazard(
        11300306,
        Objects.o3000_0000,
        model_point=12,
        behavior_param_id=5100,
        target_type=DamageTargetType.Character,
        radius=1.0,
        life=10.0,
        repetition_time=5.0,
    )
    CreateHazard(
        11300307,
        Objects.o3000_0000,
        model_point=14,
        behavior_param_id=5100,
        target_type=DamageTargetType.Character,
        radius=1.0,
        life=10.0,
        repetition_time=5.0,
    )
    CreateHazard(
        11300308,
        Objects.o3000_0000,
        model_point=15,
        behavior_param_id=5100,
        target_type=DamageTargetType.Character,
        radius=0.5,
        life=10.0,
        repetition_time=5.0,
    )
    IfFlagOn(0, 11300402)
    RemoveObjectFlag(11300301)
    RemoveObjectFlag(11300302)
    RemoveObjectFlag(11300303)
    RemoveObjectFlag(11300304)
    RemoveObjectFlag(11300305)
    RemoveObjectFlag(11300306)
    RemoveObjectFlag(11300307)
    RemoveObjectFlag(11300308)
    Restart()


def Event11300350():
    """ 11300350: Event 11300350 """
    IfFlagOff(0, 11300403)
    CreateHazard(
        11300351,
        Objects.o3001_0000,
        model_point=2,
        behavior_param_id=5100,
        target_type=DamageTargetType.Character,
        radius=0.5,
        life=10.0,
        repetition_time=5.0,
    )
    CreateHazard(
        11300352,
        Objects.o3001_0000,
        model_point=4,
        behavior_param_id=5100,
        target_type=DamageTargetType.Character,
        radius=1.0,
        life=10.0,
        repetition_time=5.0,
    )
    CreateHazard(
        11300353,
        Objects.o3001_0000,
        model_point=6,
        behavior_param_id=5100,
        target_type=DamageTargetType.Character,
        radius=1.0,
        life=10.0,
        repetition_time=5.0,
    )
    CreateHazard(
        11300354,
        Objects.o3001_0000,
        model_point=8,
        behavior_param_id=5100,
        target_type=DamageTargetType.Character,
        radius=1.0,
        life=10.0,
        repetition_time=5.0,
    )
    CreateHazard(
        11300355,
        Objects.o3001_0000,
        model_point=10,
        behavior_param_id=5100,
        target_type=DamageTargetType.Character,
        radius=1.0,
        life=10.0,
        repetition_time=5.0,
    )
    CreateHazard(
        11300356,
        Objects.o3001_0000,
        model_point=12,
        behavior_param_id=5100,
        target_type=DamageTargetType.Character,
        radius=1.0,
        life=10.0,
        repetition_time=5.0,
    )
    CreateHazard(
        11300357,
        Objects.o3001_0000,
        model_point=14,
        behavior_param_id=5100,
        target_type=DamageTargetType.Character,
        radius=1.0,
        life=10.0,
        repetition_time=5.0,
    )
    CreateHazard(
        11300358,
        Objects.o3001_0000,
        model_point=33,
        behavior_param_id=5100,
        target_type=DamageTargetType.Character,
        radius=1.0,
        life=10.0,
        repetition_time=5.0,
    )
    CreateHazard(
        11300359,
        Objects.o3001_0000,
        model_point=35,
        behavior_param_id=5100,
        target_type=DamageTargetType.Character,
        radius=1.0,
        life=10.0,
        repetition_time=5.0,
    )
    CreateHazard(
        11300360,
        Objects.o3001_0000,
        model_point=37,
        behavior_param_id=5100,
        target_type=DamageTargetType.Character,
        radius=1.0,
        life=10.0,
        repetition_time=5.0,
    )
    CreateHazard(
        11300361,
        Objects.o3001_0000,
        model_point=39,
        behavior_param_id=5100,
        target_type=DamageTargetType.Character,
        radius=0.5,
        life=10.0,
        repetition_time=5.0,
    )
    IfFlagOn(0, 11300403)
    RemoveObjectFlag(11300351)
    RemoveObjectFlag(11300352)
    RemoveObjectFlag(11300353)
    RemoveObjectFlag(11300354)
    RemoveObjectFlag(11300355)
    RemoveObjectFlag(11300356)
    RemoveObjectFlag(11300357)
    RemoveObjectFlag(11300358)
    RemoveObjectFlag(11300359)
    RemoveObjectFlag(11300360)
    RemoveObjectFlag(11300361)
    Restart()


def Event11300900(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11300900: Event 11300900 """
    SkipLinesIfThisEventSlotOff(4)
    EndOfAnimation(arg_8_11, 2)
    EndOfAnimation(arg_4_7, 2)
    DisableObjectActivation(arg_4_7, obj_act_id=-1)
    End()
    EnableNavmeshType(arg_12_15, NavmeshType.Solid)
    IfObjectActivated(0, obj_act_id=arg_0_3)
    ForceAnimation(arg_8_11, 1)
    DisableNavmeshType(arg_12_15, NavmeshType.Solid)


def Event11305030(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int, arg_20_23: int):
    """ 11305030: Event 11305030 """
    SkipLinesIfFlagOff(4, arg_0_3)
    DisableObjectActivation(arg_12_15, obj_act_id=3011)
    EndOfAnimation(arg_16_19, 0)
    EndOfAnimation(arg_12_15, 2)
    SkipLines(2)
    DisableObjectActivation(arg_12_15, obj_act_id=3012)
    EnableNavmeshType(arg_20_23, NavmeshType.Solid)
    IfFlagOn(1, arg_4_7)
    IfFlagOn(2, arg_8_11)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    DisableFlag(arg_4_7)
    DisableFlag(arg_8_11)
    SkipLinesIfFinishedConditionTrue(6, 2)
    EnableFlag(arg_0_3)
    ForceAnimation(arg_16_19, 3)
    WaitFrames(140)
    EnableObjectActivation(arg_12_15, obj_act_id=3012)
    DisableNavmeshType(arg_20_23, NavmeshType.Solid)
    Restart()
    DisableFlag(arg_0_3)
    ForceAnimation(arg_16_19, 1)
    WaitFrames(140)
    EnableObjectActivation(arg_12_15, obj_act_id=3011)
    EnableNavmeshType(arg_20_23, NavmeshType.Solid)
    Restart()


def Event11305032(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11305032: Event 11305032 """
    IfObjectActivated(1, obj_act_id=arg_0_3)
    IfObjectActivated(2, obj_act_id=arg_4_7)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionTrue(2, 2)
    EnableFlag(arg_8_11)
    Restart()
    EnableFlag(arg_12_15)
    Restart()


def Event11305000():
    """ 11305000: Event 11305000 """
    DisableNetworkSync()
    IfSingleplayer(1)
    IfInsideMap(1, game_map=CATACOMBS)
    IfCharacterInsideRegion(1, PLAYER, region=Boxes.CoffinMonitor)
    IfFlagOff(1, 11310000)
    IfPlayerHasGood(1, 109, including_box=False)
    IfConditionTrue(0, input_condition=1)
    Wait(30.0)
    RestartIfMultiplayer()
    IfCharacterInsideRegion(6, PLAYER, region=Boxes.CoffinMonitor)
    RestartIfConditionFalse(6)
    IfHealthLessThanOrEqual(7, PLAYER, 0.0)
    RestartIfConditionTrue(7)
    EnableFlag(11310050)
    PlayCutscene(
        130020,
        skippable=True,
        fade_out=False,
        player_id=PLAYER,
        move_to_region=m13_01_Boxes.ArrivalInCoffin,
        move_to_map=TOMB_OF_THE_GIANTS,
    )
    PlayCutscene(130120, skippable=True, fade_out=False, player_id=PLAYER)
    WaitFrames(1)
    EnableObjectActivation(m13_01_Objects.o3060_0000, obj_act_id=-1)
    ResetStandbyAnimationSettings(PLAYER)
    Restart()


@RestartOnRest
def Event11305001():
    """ 11305001: Event 11305001 """
    IfCharacterInsideRegion(1, PLAYER, region=Boxes.CoffinMonitor)
    IfTimeElapsed(1, 2.0)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(11305006)
    DisableObjectActivation(Objects.o3060_0000, obj_act_id=3060)
    EnableObjectActivation(Objects.o3060_0000, obj_act_id=3061)
    RestartEvent(11305002)
    RestartEvent(11305009)
    Restart()


@RestartOnRest
def Event11305002():
    """ 11305002: Event 11305002 """
    DisableNetworkSync()
    IfFlagOn(0, 11305006)
    DisableFlag(11305006)
    Wait(5.0)
    EnableFlag(11305008)
    Restart()


def Event11305003():
    """ 11305003: Event 11305003 """
    IfFlagOn(0, 11305008)
    EnableObjectActivation(Objects.o3060_0000, obj_act_id=3060)
    DisableObjectActivation(Objects.o3060_0000, obj_act_id=3061)
    DisableFlag(11305006)
    DisableFlag(11305008)
    RestartEvent(11305000)
    RestartEvent(11305001)
    RestartEvent(11305002)
    Restart()


@RestartOnRest
def Event11305004():
    """ 11305004: Event 11305004 """
    IfCharacterTargeting(1, Characters.c2300_0000, PLAYER)
    IfCharacterHasSpecialEffect(1, PLAYER, 4130)
    IfConditionTrue(0, input_condition=1)
    ClearTargetList(Characters.c2300_0000)
    ReplanAI(Characters.c2300_0000)
    Restart()


def Event11305009():
    """ 11305009: Event 11305009 """
    IfAllPlayersOutsideRegion(1, region=Boxes.CoffinMonitor)
    IfEntityWithinDistance(1, Objects.o3060_0000, PLAYER, radius=10.0)
    IfTimeElapsed(1, 2.0)
    IfConditionTrue(0, input_condition=1)
    EnableObjectActivation(Objects.o3060_0000, obj_act_id=3060)
    DisableObjectActivation(Objects.o3060_0000, obj_act_id=3061)
    Restart()


def Event11300420(_, arg_0_3: int):
    """ 11300420: Event 11300420 """
    DisableNetworkSync()
    WaitFrames(1)
    IfEntityWithinDistance(1, Objects.o3060_0000, arg_0_3, radius=10.0)
    IfCharacterInsideRegion(1, arg_0_3, region=Boxes.CoffinMonitor)
    IfConditionTrue(0, input_condition=1)
    SetStandbyAnimationSettings(arg_0_3, standby_animation=7151, death_animation=6082)
    IfEntityWithinDistance(2, Objects.o3060_0000, arg_0_3, radius=10.0)
    IfCharacterOutsideRegion(2, arg_0_3, region=Boxes.CoffinMonitor)
    IfConditionTrue(0, input_condition=2)
    ResetStandbyAnimationSettings(arg_0_3)
    Restart()


def Event11300100(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11300100: Event 11300100 """
    SkipLinesIfThisEventSlotOff(2)
    DisableObject(arg_8_11)
    End()
    IfFlagOff(1, arg_0_3)
    IfCharacterInsideRegion(1, PLAYER, region=arg_4_7)
    IfConditionTrue(0, input_condition=1)
    DestroyObject(arg_8_11)
    CreateTemporaryVFX(130000, anchor_entity=arg_8_11, anchor_type=CoordEntityType.Object, model_point=-1)
    PlaySoundEffect(anchor_entity=arg_8_11, sound_type=SoundType.o_Object, sound_id=arg_12_15)


def Event11300150():
    """ 11300150: Event 11300150 """
    SkipLinesIfThisEventOff(2)
    PostDestruction(Objects.o3036_0000)
    End()
    DisableAI(Characters.c2910_0001)
    IfCharacterInsideRegion(0, PLAYER, region=Boxes.CeilingBreakTrigger)
    EnableAI(Characters.c2910_0001)
    DestroyObject(Objects.o3036_0000)
    PlaySoundEffect(anchor_entity=Objects.o3036_0000, sound_type=SoundType.a_Ambient, sound_id=303600000)


def Event11300160():
    """ 11300160: Event 11300160 """
    SkipLinesIfThisEventOff(2)
    DisableObject(Objects.o3661_0000)
    End()
    IfObjectDestroyed(0, Objects.o3661_0000)
    EnableFlag(11300160)


def Event11300200():
    """ 11300200: Event 11300200 """
    SkipLinesIfThisEventOff(2)
    EndOfAnimation(Objects.o3350_0000, 0)
    End()
    IfFlagOn(0, 6)
    ForceAnimation(Objects.o3350_0000, 0)


def Event11300210():
    """ 11300210: Event 11300210 """
    SkipLinesIfThisEventOff(3)
    DisableObject(Objects.o3871_0000)
    DisableObject(Objects.o3872_0000)
    End()
    IfCharacterInsideRegion(1, PLAYER, region=Boxes.VamosCutsceneTrigger)
    IfConditionTrue(0, input_condition=1)
    SkipLinesIfMultiplayer(3)
    PlayCutscene(
        130010,
        skippable=True,
        fade_out=False,
        player_id=PLAYER,
        move_to_region=Boxes.VamosCutsceneTrigger,
        move_to_map=CATACOMBS,
    )
    WaitFrames(1)
    SkipLines(5)
    SkipLinesIfFlagOff(2, 11305060)
    PlayCutscene(
        130010,
        skippable=False,
        fade_out=False,
        player_id=PLAYER,
        move_to_region=Boxes.VamosCutsceneTrigger,
        move_to_map=CATACOMBS,
    )
    SkipLines(1)
    PlayCutscene(130010, skippable=False, fade_out=False, player_id=PLAYER)
    WaitFrames(1)
    DisableObject(Objects.o3871_0000)
    DisableObject(Objects.o3872_0000)


def Event11305060():
    """ 11305060: Event 11305060 """
    EndIfFlagOn(11300210)
    DisableNetworkSync()
    DisableFlag(11305060)
    IfCharacterInsideRegion(0, PLAYER, region=Boxes.VamosCutsceneTrigger)
    EnableFlag(11305060)
    IfCharacterOutsideRegion(0, PLAYER, region=Boxes.VamosCutsceneTrigger)
    Restart()


@RestartOnRest
def Event11300800():
    """ 11300800: Event 11300800 """
    EnableFlag(11305200)
    EnableFlag(11305040)
    RunEvent(
        11305050,
        slot=1,
        args=(11305040, Characters.c2650_0000, Cylinders.NecromancerNest2, 10.0),
        arg_types="iiif",
    )
    RunEvent(
        11305050,
        slot=2,
        args=(11305051, Characters.c2650_0000, Cylinders.NecromancerNest3, 10.0),
        arg_types="iiif",
    )
    RunEvent(
        11305050,
        slot=3,
        args=(11305052, Characters.c2650_0000, Cylinders.NecromancerNest4, 10.0),
        arg_types="iiif",
    )
    RunEvent(
        11305050,
        slot=4,
        args=(11305053, Characters.c2650_0000, Cylinders.NecromancerNest5, 10.0),
        arg_types="iiif",
    )
    RunEvent(11300801, slot=0, args=(Characters.c2650_0000,))
    RunEvent(11300801, slot=1, args=(Characters.c2650_0001,))
    RunEvent(11300801, slot=2, args=(Characters.c2650_0002,))
    RunEvent(11300801, slot=3, args=(Characters.c2650_0003,))
    RunEvent(11300801, slot=4, args=(Characters.c2650_0004,))
    RunEvent(11300801, slot=5, args=(Characters.c2650_0005,))
    RunEvent(11305100, slot=0, args=(Characters.c2650_0000, Characters.c2900_0002))
    RunEvent(11305100, slot=1, args=(Characters.c2650_0000, Characters.c2900_0003))
    RunEvent(11305100, slot=2, args=(Characters.c2650_0000, Characters.c2900_0004))
    RunEvent(11305100, slot=3, args=(Characters.c2650_0000, Characters.c2900_0005))
    RunEvent(11305100, slot=4, args=(Characters.c2650_0000, Characters.c2900_0006))
    RunEvent(11305100, slot=5, args=(Characters.c2650_0000, Characters.c2900_0007))
    RunEvent(11305100, slot=6, args=(Characters.c2650_0000, Characters.c2900_0008))
    RunEvent(11305100, slot=7, args=(Characters.c2650_0000, Characters.c2900_0009))
    RunEvent(11305100, slot=8, args=(Characters.c2650_0000, Characters.c2900_0010))
    RunEvent(11305100, slot=9, args=(Characters.c2650_0000, Characters.c2900_0011))
    RunEvent(11305100, slot=10, args=(Characters.c2650_0000, Characters.c2900_0012))
    RunEvent(11305100, slot=11, args=(Characters.c2650_0000, Characters.c2900_0013))
    RunEvent(11305100, slot=12, args=(Characters.c2650_0000, Characters.c2900_0014))
    RunEvent(11305100, slot=13, args=(Characters.c2650_0000, Characters.c2900_0015))
    RunEvent(11305100, slot=14, args=(Characters.c2650_0001, Characters.c2900_0022))
    RunEvent(11305100, slot=15, args=(Characters.c2650_0001, Characters.c2900_0023))
    RunEvent(11305100, slot=16, args=(Characters.c2650_0001, Characters.c2900_0024))
    RunEvent(11305100, slot=17, args=(Characters.c2650_0001, Characters.c2900_0025))
    RunEvent(11305100, slot=18, args=(Characters.c2650_0001, Characters.c2900_0026))
    RunEvent(11305100, slot=19, args=(Characters.c2650_0001, Characters.c2900_0021))
    RunEvent(11305100, slot=20, args=(Characters.c2650_0001, Characters.c2900_0044))
    RunEvent(11305100, slot=21, args=(Characters.c2650_0001, Characters.c2900_0020))
    RunEvent(11305100, slot=22, args=(Characters.c2650_0002, Characters.c2900_0027))
    RunEvent(11305100, slot=23, args=(Characters.c2650_0002, Characters.c2900_0028))
    RunEvent(11305100, slot=24, args=(Characters.c2650_0002, Characters.c2900_0029))
    RunEvent(11305100, slot=25, args=(Characters.c2650_0002, Characters.c2900_0030))
    RunEvent(11305100, slot=26, args=(Characters.c2650_0002, Characters.c2900_0031))
    RunEvent(11305100, slot=27, args=(Characters.c2650_0002, Characters.c2900_0032))
    RunEvent(11305100, slot=28, args=(Characters.c2650_0002, Characters.c2900_0033))
    RunEvent(11305100, slot=29, args=(Characters.c2650_0003, Characters.c2900_0016))
    RunEvent(11305100, slot=30, args=(Characters.c2650_0003, Characters.c2900_0017))
    RunEvent(11305100, slot=31, args=(Characters.c2650_0003, Characters.c2900_0018))
    RunEvent(11305100, slot=32, args=(Characters.c2650_0003, Characters.c2900_0019))
    RunEvent(11305100, slot=33, args=(Characters.c2650_0003, Characters.c2900_0052))
    RunEvent(11305100, slot=34, args=(Characters.c2650_0003, Characters.c2900_0053))
    RunEvent(11305100, slot=35, args=(Characters.c2650_0004, Characters.c2900_0048))
    RunEvent(11305100, slot=36, args=(Characters.c2650_0004, Characters.c2900_0049))
    RunEvent(11305100, slot=37, args=(Characters.c2650_0004, Characters.c2900_0047))
    RunEvent(11305100, slot=38, args=(Characters.c2650_0004, Characters.c2900_0045))
    RunEvent(11305100, slot=39, args=(Characters.c2650_0004, Characters.c2900_0046))
    RunEvent(11305100, slot=40, args=(Characters.c2650_0004, Characters.c2900_0000))
    RunEvent(11305100, slot=41, args=(Characters.c2650_0004, Characters.c2900_0001))
    RunEvent(11305100, slot=44, args=(Characters.c2650_0005, Characters.c2900_0035))
    RunEvent(11305100, slot=45, args=(Characters.c2650_0005, Characters.c2900_0036))
    RunEvent(11305100, slot=46, args=(Characters.c2650_0005, Characters.c2900_0037))
    RunEvent(11305100, slot=47, args=(Characters.c2650_0005, Characters.c2900_0038))
    RunEvent(11305100, slot=48, args=(Characters.c2650_0005, Characters.c2900_0039))
    RunEvent(11305100, slot=49, args=(Characters.c2650_0005, Characters.c2900_0042))
    RunEvent(11305100, slot=50, args=(Characters.c2650_0005, Characters.c2900_0043))
    RunEvent(11305070, slot=0, args=(Characters.c2900_0008, 5.0), arg_types="if")
    RunEvent(11305070, slot=1, args=(Characters.c2900_0010, 5.0), arg_types="if")
    RunEvent(11305070, slot=2, args=(Characters.c2900_0011, 5.0), arg_types="if")
    RunEvent(11305070, slot=3, args=(Characters.c2900_0014, 5.0), arg_types="if")
    RunEvent(11305070, slot=4, args=(Characters.c2900_0022, 5.0), arg_types="if")
    RunEvent(11305070, slot=5, args=(Characters.c2900_0023, 5.0), arg_types="if")
    RunEvent(11305070, slot=6, args=(Characters.c2900_0024, 5.0), arg_types="if")
    RunEvent(11305070, slot=7, args=(Characters.c2900_0025, 5.0), arg_types="if")
    RunEvent(11305070, slot=8, args=(Characters.c2900_0026, 5.0), arg_types="if")
    RunEvent(11305070, slot=9, args=(Characters.c2900_0033, 5.0), arg_types="if")
    RunEvent(11305070, slot=10, args=(Characters.c2900_0048, 5.0), arg_types="if")
    RunEvent(11305070, slot=11, args=(Characters.c2900_0049, 5.0), arg_types="if")
    RunEvent(11305070, slot=12, args=(Characters.c2900_0000, 5.0), arg_types="if")
    RunEvent(11305070, slot=13, args=(Characters.c2900_0001, 5.0), arg_types="if")
    RunEvent(11305070, slot=16, args=(Characters.c2900_0018, 5.0), arg_types="if")
    RunEvent(11305070, slot=17, args=(Characters.c2900_0019, 5.0), arg_types="if")
    RunEvent(11305070, slot=18, args=(Characters.c2900_0020, 5.0), arg_types="if")
    RunEvent(11305210, slot=0, args=(Characters.c3501_0006,))
    RunEvent(11305210, slot=1, args=(Characters.c3501_0007,))
    RunEvent(11305210, slot=2, args=(Characters.c3501_0008,))
    RunEvent(11305210, slot=3, args=(Characters.c3501_0009,))
    RunEvent(11305210, slot=4, args=(Characters.c3501_0010,))
    RunEvent(11305210, slot=5, args=(Characters.c3501_0011,))
    RunEvent(11305210, slot=6, args=(Characters.c3501_0012,))
    RunEvent(11305210, slot=7, args=(Characters.c3501_0013,))
    RunEvent(11305210, slot=8, args=(Characters.c3501_0014,))
    RunEvent(11305210, slot=9, args=(Characters.c3501_0015,))
    RunEvent(11305210, slot=10, args=(Characters.c3501_0016,))
    RunEvent(11305210, slot=13, args=(Characters.c3501_0019,))


@UnknownRestart
def Event11305050(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: float):
    """ 11305050: Event 11305050 """
    EndIfThisEventSlotOn()
    IfFlagOn(1, arg_0_3)
    IfEntityWithinDistance(1, arg_4_7, PLAYER, radius=arg_12_15)
    IfCharacterType(2, PLAYER, CharacterType.BlackPhantom)
    IfConditionFalse(1, input_condition=2)
    IfConditionTrue(0, input_condition=1)
    SetNest(arg_4_7, arg_8_11)
    AICommand(arg_4_7, command_id=10, slot=0)
    ReplanAI(arg_4_7)
    IfCharacterInsideRegion(0, arg_4_7, region=arg_8_11)
    AICommand(arg_4_7, command_id=-1, slot=0)
    ReplanAI(arg_4_7)


@RestartOnRest
def Event11300801(_, arg_0_3: int):
    """ 11300801: Event 11300801 """
    SkipLinesIfThisEventSlotOff(3)
    DisableCharacter(arg_0_3)
    Kill(arg_0_3, award_souls=False)
    End()
    IfCharacterDead(0, arg_0_3)
    End()


@UnknownRestart
def Event11305070(_, arg_0_3: int, arg_4_7: float):
    """ 11305070: Event 11305070 """
    SkipLinesIfThisEventSlotOff(2)
    ResetStandbyAnimationSettings(arg_0_3)
    End()
    IfEntityWithinDistance(0, PLAYER, arg_0_3, radius=arg_4_7)
    SetStandbyAnimationSettings(arg_0_3, cancel_animation=9061)


@UnknownRestart
def Event11305100(_, arg_0_3: int, arg_4_7: int):
    """ 11305100: Event 11305100 """
    SkipLinesIfThisEventSlotOff(2)
    CancelSpecialEffect(arg_4_7, 5451)
    End()
    EnableImmortality(arg_4_7)
    IfCharacterDead(0, arg_0_3)
    CancelSpecialEffect(arg_4_7, 5451)
    DisableImmortality(arg_4_7)


@UnknownRestart
def Event11305210(_, arg_0_3: int):
    """ 11305210: Event 11305210 """
    SkipLinesIfThisEventSlotOn(1)
    IfHasTAEEvent(0, arg_0_3, tae_event_id=400)
    DisableCharacter(arg_0_3)


@RestartOnRest
def Event11305045():
    """ 11305045: Event 11305045 """
    EndIfThisEventOn()
    DisableAI(Characters.c2300_0000)
    SetStandbyAnimationSettings(Characters.c2300_0000, standby_animation=9000)
    IfEntityWithinDistance(-1, Characters.c2300_0000, PLAYER, radius=5.0)
    IfAttacked(-1, Characters.c2300_0000, attacker=PLAYER)
    IfConditionTrue(0, input_condition=-1)
    ResetStandbyAnimationSettings(Characters.c2300_0000)
    EnableAI(Characters.c2300_0000)


@RestartOnRest
def Event11300850(_, arg_0_3: int, arg_4_7: int):
    """ 11300850: Event 11300850 """
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


def Event11300510(_, arg_0_3: int, arg_4_7: int):
    """ 11300510: Event 11300510 """
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


def Event11300520(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11300520: Event 11300520 """
    SkipLinesIfThisEventSlotOff(2)
    DropMandatoryTreasure(arg_0_3)
    End()
    IfHealthLessThanOrEqual(0, arg_0_3, 0.0)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)


def Event11300530(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11300530: Event 11300530 """
    IfFlagOff(1, 1622)
    IfFlagOff(1, 1625)
    IfFlagOff(1, 1627)
    IfFlagOff(1, 1628)
    IfFlagOn(1, 1620)
    IfFlagOn(1, 11300593)
    IfCharacterAlive(1, arg_0_3)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)


def Event11300531(_, arg_0_3: int, arg_4_7: int):
    """ 11300531: Event 11300531 """
    IfFlagOn(1, 1620)
    IfHealthLessThanOrEqual(1, arg_0_3, 0.0)
    IfFlagOn(2, 1621)
    IfHealthLessThanOrEqual(2, arg_0_3, 0.0)
    IfFlagOn(3, arg_4_7)
    IfThisEventOn(3)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    DisableFlag(1627)
    EnableFlag(arg_4_7)
    EndIfFinishedConditionFalse(3)
    DropMandatoryTreasure(arg_0_3)


def Event11300533(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11300533: Event 11300533 """
    IfFlagOff(1, 1627)
    IfFlagOff(1, 1628)
    IfFlagOn(-7, 1620)
    IfFlagOn(-7, 1621)
    IfConditionTrue(1, input_condition=-7)
    IfConditionTrue(2, input_condition=1)
    IfFlagOn(2, 6)
    IfConditionTrue(3, input_condition=1)
    IfFlagOn(3, 1173)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)
    DisableCharacter(arg_0_3)


def Event11305025():
    """ 11305025: Event 11305025 """
    SkipLinesIfClient(1)
    SetNetworkUpdateAuthority(Characters.c0000_0004, UpdateAuthority.Forced)
    SkipLinesIfFlagOn(3, 11305028)
    IfClient(2)
    IfFlagOn(2, 11305026)
    SkipLinesIfConditionTrue(1, 2)
    DisableCharacter(Characters.c0000_0004)
    EndIfFlagOn(6)
    IfHost(1)
    IfCharacterHuman(1, PLAYER)
    IfCharacterBackreadEnabled(1, Characters.c0000_0004)
    IfConditionTrue(0, input_condition=1)
    PlaceSummonSign(
        SummonSignType.BlueEyeSign,
        Characters.c0000_0004,
        region=Points.LeeroySummonSign,
        summon_flag=11305026,
        dismissal_flag=11305028,
    )
    IfFlagOn(0, 11305026)
    SetNest(Characters.c0000_0004, Boxes.LeeroySummonNest)


def Event11305990(_, arg_0_3: int, arg_4_7: int):
    """ 11305990: Event 11305990 """
    IfFlagOn(0, arg_0_3)
    EraseNPCSummonSign(summoned_character=arg_4_7)
    IfFlagOff(0, arg_0_3)
    Restart()


def Event11305029():
    """ 11305029: Event 11305029 """
    SkipLinesIfClient(1)
    SetNetworkUpdateAuthority(Characters.c0000_0004, UpdateAuthority.Forced)
    SkipLinesIfFlagOn(3, 11305028)
    IfClient(2)
    IfFlagOn(2, 11305026)
    SkipLinesIfConditionTrue(1, 2)
    DisableCharacter(Characters.c0000_0004)
    EndIfFlagOn(6)
    IfMultiplayerCount(1, arg1=4, arg2=3)
    IfHost(1)
    IfFlagOff(1, 11305026)
    IfFlagOff(1, 11305028)
    IfCharacterHuman(1, PLAYER)
    IfCharacterBackreadEnabled(1, Characters.c0000_0004)
    IfCharacterHasSpecialEffect(1, PLAYER, 28)
    IfConditionTrue(0, input_condition=1)
    PlaceSummonSign(
        SummonSignType.BlueEyeSign,
        Characters.c0000_0004,
        region=Points.LeeroySummonSign,
        summon_flag=11305026,
        dismissal_flag=11305028,
    )
    IfFlagOn(0, 11305026)
    SetNest(Characters.c0000_0004, Boxes.LeeroySummonNest)


def Event11305027():
    """ 11305027: Event 11305027 """
    EndIfThisEventOn()
    IfFlagOn(1, 11305026)
    IfFlagOn(1, 11305393)
    IfConditionTrue(0, input_condition=1)
    AICommand(Characters.c0000_0004, command_id=10, slot=0)
    ReplanAI(Characters.c0000_0004)
    IfCharacterInsideRegion(0, Characters.c0000_0004, region=Boxes.PinwheelFogPrompt)
    RotateToFaceEntity(Characters.c0000_0004, Boxes.PinwheelFogRotationTarget)
    ForceAnimation(Characters.c0000_0004, 7410)
    AICommand(Characters.c0000_0004, command_id=-1, slot=0)
    ReplanAI(Characters.c0000_0004)


@RestartOnRest
def Event11305061(_, arg_0_3: int):
    """ 11305061: Event 11305061 """
    EndIfThisEventOn()
    DisableCharacterCollision(arg_0_3)
    DisableGravity(arg_0_3)
    WaitFrames(10)
    EnableCharacterCollision(arg_0_3)
    EnableGravity(arg_0_3)


def Event11300592():
    """ 11300592: Event 11300592 """
    IfHost(1)
    IfFlagOn(1, 1620)
    IfFlagOff(1, 11300403)
    IfCharacterInsideRegion(1, PLAYER, region=Boxes.PatchesBridgeSwitchTrigger2)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(11300592)
    ActivateObject(Objects.o3011_0002, obj_act_id=3011, relative_index=-1)


def Event11300593():
    """ 11300593: Event 11300593 """
    IfHost(1)
    IfFlagOn(1, 1620)
    IfFlagOn(1, 11300592)
    IfFlagOn(1, 11300403)
    IfCharacterInsideRegion(1, PLAYER, region=Boxes.PatchesBridgeSwitchTrigger1)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(11300593)
    ActivateObject(Objects.o3011_0002, obj_act_id=3012, relative_index=-1)


def Event11305843(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11305843: Event 11305843 """
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


def Event11305846(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 11305846: Event 11305846 """
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
