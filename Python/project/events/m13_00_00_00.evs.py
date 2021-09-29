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


@RestartOnRest
def PatchesAmbush():
    """ 11302000: Patches teleports behind the player and attacks. """
    DisableCharacter(Characters.c0000_PatchesAmbush)

    Await(InsideMap(CATACOMBS) and TriggerFlags.PatchesAmbush and IsAlive(Characters.c0000_PatchesAmbush))
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
    """ 11302001: Channeler teleports above the player (no gravity) and uses its buff dance. """
    DisableCharacter(Characters.c2370_TrollChanneler)

    Await(InsideMap(CATACOMBS) and TriggerFlags.ChannelerAmbush and IsAlive(Characters.c2370_TrollChanneler))
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

    AddSpecialEffect(6320, 5470)
    AddSpecialEffect(6550, 5470)
    AddSpecialEffect(1300960, 5470)
    AddSpecialEffect(1300961, 5470)
    AddSpecialEffect(1300962, 5470)
    AddSpecialEffect(1300300, 5470)
    AddSpecialEffect(1300100, 5470)
    AddSpecialEffect(1300120, 5470)
    AddSpecialEffect(1300140, 5470)
    AddSpecialEffect(1300160, 5470)
    AddSpecialEffect(1300180, 5470)
    AddSpecialEffect(1300200, 5470)
    AddSpecialEffect(1300400, 5470)
    AddSpecialEffect(1300000, 5470)
    AddSpecialEffect(1300001, 5470)
    AddSpecialEffect(1300101, 5470)
    AddSpecialEffect(1300102, 5470)
    AddSpecialEffect(1300103, 5470)
    AddSpecialEffect(1300104, 5470)
    AddSpecialEffect(1300105, 5470)
    AddSpecialEffect(1300106, 5470)
    AddSpecialEffect(1300107, 5470)
    AddSpecialEffect(1300108, 5470)
    AddSpecialEffect(1300109, 5470)
    AddSpecialEffect(1300110, 5470)
    AddSpecialEffect(1300111, 5470)
    AddSpecialEffect(1300112, 5470)
    AddSpecialEffect(1300113, 5470)
    AddSpecialEffect(1300114, 5470)
    AddSpecialEffect(1300161, 5470)
    AddSpecialEffect(1300162, 5470)
    AddSpecialEffect(1300163, 5470)
    AddSpecialEffect(1300164, 5470)
    AddSpecialEffect(1300020, 5470)
    AddSpecialEffect(1300126, 5470)
    AddSpecialEffect(1300121, 5470)
    AddSpecialEffect(1300122, 5470)
    AddSpecialEffect(1300123, 5470)
    AddSpecialEffect(1300124, 5470)
    AddSpecialEffect(1300125, 5470)
    AddSpecialEffect(1300141, 5470)
    AddSpecialEffect(1300142, 5470)
    AddSpecialEffect(1300143, 5470)
    AddSpecialEffect(1300144, 5470)
    AddSpecialEffect(1300145, 5470)
    AddSpecialEffect(1300146, 5470)
    AddSpecialEffect(1300147, 5470)
    AddSpecialEffect(1300900, 5470)
    AddSpecialEffect(1300201, 5470)
    AddSpecialEffect(1300202, 5470)
    AddSpecialEffect(1300203, 5470)
    AddSpecialEffect(1300204, 5470)
    AddSpecialEffect(1300205, 5470)
    AddSpecialEffect(1300901, 5470)
    AddSpecialEffect(1300902, 5470)
    AddSpecialEffect(1300206, 5470)
    AddSpecialEffect(1300207, 5470)
    AddSpecialEffect(1300127, 5470)
    AddSpecialEffect(1300184, 5470)
    AddSpecialEffect(1300185, 5470)
    AddSpecialEffect(1300183, 5470)
    AddSpecialEffect(1300181, 5470)
    AddSpecialEffect(1300182, 5470)
    AddSpecialEffect(1300165, 5470)
    AddSpecialEffect(1300166, 5470)
    AddSpecialEffect(1300903, 5470)
    AddSpecialEffect(1300904, 5470)
    AddSpecialEffect(1300905, 5470)
    AddSpecialEffect(1300906, 5470)
    AddSpecialEffect(1300907, 5470)
    AddSpecialEffect(1300050, 5470)
    AddSpecialEffect(6200, 5470)
    AddSpecialEffect(1300208, 5470)
    AddSpecialEffect(1300209, 5470)
    AddSpecialEffect(1300210, 5470)
    AddSpecialEffect(1300211, 5470)
    AddSpecialEffect(1300212, 5470)
    AddSpecialEffect(1300213, 5470)
    AddSpecialEffect(1300214, 5470)
    AddSpecialEffect(1300908, 5470)
    AddSpecialEffect(1300909, 5470)
    AddSpecialEffect(1300910, 5470)
    AddSpecialEffect(1300500, 5470)
    AddSpecialEffect(1300501, 5470)
    AddSpecialEffect(1300800, 5470)
    AddSpecialEffect(1300801, 5470)
    AddSpecialEffect(1300802, 5470)
    AddSpecialEffect(1300803, 5470)
    AddSpecialEffect(1300804, 5470)
    AddSpecialEffect(1300805, 5470)
    AddSpecialEffect(1300806, 5470)
    AddSpecialEffect(1300807, 5470)
    AddSpecialEffect(1300808, 5470)
    AddSpecialEffect(1300809, 5470)
    AddSpecialEffect(1300810, 5470)
    AddSpecialEffect(1300811, 5470)
    AddSpecialEffect(1300812, 5470)
    AddSpecialEffect(1300813, 5470)
    AddSpecialEffect(1300814, 5470)
    AddSpecialEffect(1303900, 5470)
    AddSpecialEffect(1303910, 5470)
    AddSpecialEffect(1303902, 5470)
    AddSpecialEffect(1303901, 5470)
    AddSpecialEffect(1303911, 5470)
    AddSpecialEffect(1303912, 5470)
    AddSpecialEffect(1300350, 5470)
    AddSpecialEffect(1300351, 5470)
    AddSpecialEffect(1300352, 5470)
    AddSpecialEffect(1300353, 5470)
    AddSpecialEffect(1300354, 5470)
    AddSpecialEffect(1300355, 5470)
    AddSpecialEffect(1300356, 5470)
    AddSpecialEffect(1300357, 5470)
    AddSpecialEffect(1300358, 5470)
    AddSpecialEffect(1300359, 5470)
    AddSpecialEffect(1300360, 5470)
    AddSpecialEffect(1300363, 5470)

    return RESTART


@RestartOnRest
def RedPhantomAmbush():
    """ 11302002: Random red phantom ambushes the player. """
    DisableCharacter(Characters.c2900_0034)
    DisableCharacter(Characters.c2900_0040)
    DisableCharacter(Characters.c2900_0041)
    DisableCharacter(Characters.c2900_0054)
    DisableCharacter(Characters.c2900_0055)
    DisableCharacter(Characters.c2900_0056)
    DisableCharacter(Characters.c2900_0057)
    DisableCharacter(Characters.c2900_0058)
    DisableCharacter(Characters.c2930_0007)
    DisableCharacter(Characters.c2930_0008)
    DisableCharacter(Characters.c2930_0009)

    Await(InsideMap(CATACOMBS) and TriggerFlags.EnemyAmbush)
    DisableFlag(TriggerFlags.EnemyAmbush)

    DisableFlagRange((11812900, 11812999))
    EnableRandomFlagInRange((11812900, 11812910))

    if FlagEnabled(11812900):
        ControlRedPhantom(0, Characters.c2900_0034)
    elif FlagEnabled(11812901):
        ControlRedPhantom(0, Characters.c2900_0040)
    elif FlagEnabled(11812902):
        ControlRedPhantom(0, Characters.c2900_0041)
    elif FlagEnabled(11812903):
        ControlRedPhantom(0, Characters.c2900_0054)
    elif FlagEnabled(11812904):
        ControlRedPhantom(0, Characters.c2900_0055)
    elif FlagEnabled(11812905):
        ControlRedPhantom(0, Characters.c2900_0056)
    elif FlagEnabled(11812906):
        ControlRedPhantom(0, Characters.c2900_0057)
    elif FlagEnabled(11812907):
        ControlRedPhantom(0, Characters.c2900_0058)
    elif FlagEnabled(11812908):
        ControlRedPhantom(0, Characters.c2930_0007)
    elif FlagEnabled(11812909):
        ControlRedPhantom(0, Characters.c2930_0008)
    elif FlagEnabled(11812910):
        ControlRedPhantom(0, Characters.c2930_0009)
    
    Await(FlagEnabled(11305082))

    return RESTART


@RestartOnRest
def ControlRedPhantom(_, enemy: int):
    """ 11305081: `enemy` moves to player and appears. """
    DisableFlag(11305082)
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
    EnableFlag(11305082)


def MakeWorldInvisible():
    """ 11302003: Disable all map pieces. Undone only by reload. """
    Await(TriggerFlags.InvisibleWorld)   # note you don't need to be standing in the map
    DisableFlag(TriggerFlags.InvisibleWorld)
    for map_piece in range(1308500, 1308678):
        DisableMapPiece(map_piece)
    # No need to restart.


@RestartOnRest
def OopsAllGwyns():
    """ 11302004: Enable Gwyns and warp them to their paired normal characters. """
    DisableCharacter(1300600)
    DisableCharacter(1300601)
    DisableCharacter(1300602)
    DisableCharacter(1300603)
    DisableCharacter(1300604)
    DisableCharacter(1300605)
    DisableCharacter(1300606)
    DisableCharacter(1300607)
    DisableCharacter(1300608)
    DisableCharacter(1300609)
    DisableCharacter(1300610)
    DisableCharacter(1300611)
    DisableCharacter(1300612)
    DisableCharacter(1300613)
    DisableCharacter(1300614)
    DisableCharacter(1300615)
    DisableCharacter(1300616)
    DisableCharacter(1300617)
    DisableCharacter(1300618)
    DisableCharacter(1300619)
    DisableCharacter(1300620)
    Await(TriggerFlags.OopsAllGwyns)  # note you don't need to be standing in the map
    DisableCharacter(6320)
    EnableCharacter(1300600)
    DisableCharacter(1300300)
    EnableCharacter(1300601)
    DisableCharacter(1300180)
    EnableCharacter(1300602)
    DisableCharacter(1300101)
    EnableCharacter(1300603)
    DisableCharacter(1300106)
    EnableCharacter(1300604)
    DisableCharacter(1300111)
    EnableCharacter(1300605)
    DisableCharacter(1300162)
    EnableCharacter(1300606)
    DisableCharacter(1300121)
    EnableCharacter(1300607)
    DisableCharacter(1300141)
    EnableCharacter(1300608)
    DisableCharacter(1300146)
    EnableCharacter(1300609)
    DisableCharacter(1300203)
    EnableCharacter(1300610)
    DisableCharacter(1300206)
    EnableCharacter(1300611)
    DisableCharacter(1300183)
    EnableCharacter(1300612)
    DisableCharacter(1300050)
    EnableCharacter(1300613)
    DisableCharacter(1300211)
    EnableCharacter(1300614)
    DisableCharacter(1300801)
    EnableCharacter(1300615)
    DisableCharacter(1300806)
    EnableCharacter(1300616)
    DisableCharacter(1300811)
    EnableCharacter(1300617)
    DisableCharacter(1300350)
    EnableCharacter(1300618)
    DisableCharacter(1300355)
    EnableCharacter(1300619)
    DisableCharacter(1300360)
    EnableCharacter(1300620)
    WaitFrames(30)  # enough time for other maps to trigger too
    DisableFlag(TriggerFlags.OopsAllGwyns)
    # No need to restart.


@RestartOnRest
def OopsAllBonewheels():
    """ 11302005: Enable Bonewheels and warp them to their paired normal characters. """
    DisableCharacter(1300401)
    DisableCharacter(1300402)
    DisableCharacter(1300403)
    DisableCharacter(1300404)
    DisableCharacter(1300405)
    DisableCharacter(1300406)
    DisableCharacter(1300407)
    DisableCharacter(1300408)
    DisableCharacter(1300409)
    DisableCharacter(1300410)
    DisableCharacter(1300411)
    DisableCharacter(1300412)
    DisableCharacter(1300413)
    DisableCharacter(1300414)
    DisableCharacter(1300415)
    DisableCharacter(1300416)
    DisableCharacter(1300417)
    DisableCharacter(1300418)
    DisableCharacter(1300419)
    DisableCharacter(1300420)
    DisableCharacter(1300421)
    DisableCharacter(1300422)
    DisableCharacter(1300423)
    DisableCharacter(1300424)
    DisableCharacter(1300425)
    DisableCharacter(1300426)
    DisableCharacter(1300427)
    DisableCharacter(1300428)
    DisableCharacter(1300429)
    DisableCharacter(1300430)
    DisableCharacter(1300431)
    DisableCharacter(1300432)
    DisableCharacter(1300433)
    DisableCharacter(1300434)
    DisableCharacter(1300435)
    DisableCharacter(1300436)
    DisableCharacter(1300437)
    DisableCharacter(1300438)
    DisableCharacter(1300439)
    DisableCharacter(1300440)
    DisableCharacter(1300441)
    DisableCharacter(1300442)
    DisableCharacter(1300443)
    DisableCharacter(1300444)
    DisableCharacter(1300445)
    DisableCharacter(1300446)
    DisableCharacter(1300447)
    DisableCharacter(1300448)
    DisableCharacter(1300449)
    DisableCharacter(1300450)
    DisableCharacter(1300451)
    DisableCharacter(1300452)
    DisableCharacter(1300453)
    DisableCharacter(1300454)
    DisableCharacter(1300455)
    DisableCharacter(1300456)
    DisableCharacter(1300457)
    DisableCharacter(1300458)
    DisableCharacter(1300459)
    DisableCharacter(1300460)
    DisableCharacter(1300461)
    DisableCharacter(1300462)
    DisableCharacter(1300463)
    DisableCharacter(1300464)
    DisableCharacter(1300465)
    DisableCharacter(1300466)
    DisableCharacter(1300467)
    DisableCharacter(1300468)
    DisableCharacter(1300469)
    DisableCharacter(1300470)
    DisableCharacter(1300471)
    DisableCharacter(1300472)
    DisableCharacter(1300473)
    DisableCharacter(1300474)
    DisableCharacter(1300475)
    DisableCharacter(1300476)
    DisableCharacter(1300477)
    DisableCharacter(1300478)
    DisableCharacter(1300479)
    DisableCharacter(1300480)
    DisableCharacter(1300481)
    DisableCharacter(1300482)
    DisableCharacter(1300483)
    DisableCharacter(1300484)
    DisableCharacter(1300485)
    DisableCharacter(1300486)
    DisableCharacter(1300487)
    DisableCharacter(1300488)
    DisableCharacter(1300489)
    DisableCharacter(1300490)
    DisableCharacter(1300491)
    DisableCharacter(1300492)
    DisableCharacter(1300493)
    DisableCharacter(1300494)
    DisableCharacter(1300495)
    DisableCharacter(1300496)
    Await(TriggerFlags.OopsAllBonewheels)  # note you don't need to be standing in the map
    DisableCharacter(6320)
    EnableCharacter(1300401)
    DisableCharacter(6550)
    EnableCharacter(1300402)
    DisableCharacter(1300300)
    EnableCharacter(1300403)
    DisableCharacter(1300100)
    EnableCharacter(1300404)
    DisableCharacter(1300120)
    EnableCharacter(1300405)
    DisableCharacter(1300140)
    EnableCharacter(1300406)
    DisableCharacter(1300160)
    EnableCharacter(1300407)
    DisableCharacter(1300180)
    EnableCharacter(1300408)
    DisableCharacter(1300200)
    EnableCharacter(1300409)
    DisableCharacter(1300400)
    EnableCharacter(1300410)
    DisableCharacter(1300000)
    EnableCharacter(1300411)
    DisableCharacter(1300001)
    EnableCharacter(1300412)
    DisableCharacter(1300101)
    EnableCharacter(1300413)
    DisableCharacter(1300102)
    EnableCharacter(1300414)
    DisableCharacter(1300103)
    EnableCharacter(1300415)
    DisableCharacter(1300104)
    EnableCharacter(1300416)
    DisableCharacter(1300105)
    EnableCharacter(1300417)
    DisableCharacter(1300106)
    EnableCharacter(1300418)
    DisableCharacter(1300107)
    EnableCharacter(1300419)
    DisableCharacter(1300108)
    EnableCharacter(1300420)
    DisableCharacter(1300109)
    EnableCharacter(1300421)
    DisableCharacter(1300110)
    EnableCharacter(1300422)
    DisableCharacter(1300111)
    EnableCharacter(1300423)
    DisableCharacter(1300112)
    EnableCharacter(1300424)
    DisableCharacter(1300113)
    EnableCharacter(1300425)
    DisableCharacter(1300114)
    EnableCharacter(1300426)
    DisableCharacter(1300161)
    EnableCharacter(1300427)
    DisableCharacter(1300162)
    EnableCharacter(1300428)
    DisableCharacter(1300163)
    EnableCharacter(1300429)
    DisableCharacter(1300164)
    EnableCharacter(1300430)
    DisableCharacter(1300020)
    EnableCharacter(1300431)
    DisableCharacter(1300126)
    EnableCharacter(1300432)
    DisableCharacter(1300121)
    EnableCharacter(1300433)
    DisableCharacter(1300122)
    EnableCharacter(1300434)
    DisableCharacter(1300123)
    EnableCharacter(1300435)
    DisableCharacter(1300124)
    EnableCharacter(1300436)
    DisableCharacter(1300125)
    EnableCharacter(1300437)
    DisableCharacter(1300141)
    EnableCharacter(1300438)
    DisableCharacter(1300142)
    EnableCharacter(1300439)
    DisableCharacter(1300143)
    EnableCharacter(1300440)
    DisableCharacter(1300144)
    EnableCharacter(1300441)
    DisableCharacter(1300145)
    EnableCharacter(1300442)
    DisableCharacter(1300146)
    EnableCharacter(1300443)
    DisableCharacter(1300147)
    EnableCharacter(1300444)
    DisableCharacter(1300201)
    EnableCharacter(1300445)
    DisableCharacter(1300202)
    EnableCharacter(1300446)
    DisableCharacter(1300203)
    EnableCharacter(1300447)
    DisableCharacter(1300204)
    EnableCharacter(1300448)
    DisableCharacter(1300205)
    EnableCharacter(1300449)
    DisableCharacter(1300206)
    EnableCharacter(1300450)
    DisableCharacter(1300207)
    EnableCharacter(1300451)
    DisableCharacter(1300127)
    EnableCharacter(1300452)
    DisableCharacter(1300184)
    EnableCharacter(1300453)
    DisableCharacter(1300185)
    EnableCharacter(1300454)
    DisableCharacter(1300183)
    EnableCharacter(1300455)
    DisableCharacter(1300181)
    EnableCharacter(1300456)
    DisableCharacter(1300182)
    EnableCharacter(1300457)
    DisableCharacter(1300165)
    EnableCharacter(1300458)
    DisableCharacter(1300166)
    EnableCharacter(1300459)
    DisableCharacter(1300050)
    EnableCharacter(1300460)
    DisableCharacter(6200)
    EnableCharacter(1300461)
    DisableCharacter(1300208)
    EnableCharacter(1300462)
    DisableCharacter(1300209)
    EnableCharacter(1300463)
    DisableCharacter(1300210)
    EnableCharacter(1300464)
    DisableCharacter(1300211)
    EnableCharacter(1300465)
    DisableCharacter(1300212)
    EnableCharacter(1300466)
    DisableCharacter(1300213)
    EnableCharacter(1300467)
    DisableCharacter(1300214)
    EnableCharacter(1300468)
    DisableCharacter(1300500)
    EnableCharacter(1300469)
    DisableCharacter(1300501)
    EnableCharacter(1300470)
    DisableCharacter(1300801)
    EnableCharacter(1300471)
    DisableCharacter(1300802)
    EnableCharacter(1300472)
    DisableCharacter(1300803)
    EnableCharacter(1300473)
    DisableCharacter(1300804)
    EnableCharacter(1300474)
    DisableCharacter(1300805)
    EnableCharacter(1300475)
    DisableCharacter(1300806)
    EnableCharacter(1300476)
    DisableCharacter(1300807)
    EnableCharacter(1300477)
    DisableCharacter(1300808)
    EnableCharacter(1300478)
    DisableCharacter(1300809)
    EnableCharacter(1300479)
    DisableCharacter(1300810)
    EnableCharacter(1300480)
    DisableCharacter(1300811)
    EnableCharacter(1300481)
    DisableCharacter(1300812)
    EnableCharacter(1300482)
    DisableCharacter(1300813)
    EnableCharacter(1300483)
    DisableCharacter(1300814)
    EnableCharacter(1300484)
    DisableCharacter(1300350)
    EnableCharacter(1300485)
    DisableCharacter(1300351)
    EnableCharacter(1300486)
    DisableCharacter(1300352)
    EnableCharacter(1300487)
    DisableCharacter(1300353)
    EnableCharacter(1300488)
    DisableCharacter(1300354)
    EnableCharacter(1300489)
    DisableCharacter(1300355)
    EnableCharacter(1300490)
    DisableCharacter(1300356)
    EnableCharacter(1300491)
    DisableCharacter(1300357)
    EnableCharacter(1300492)
    DisableCharacter(1300358)
    EnableCharacter(1300493)
    DisableCharacter(1300359)
    EnableCharacter(1300494)
    DisableCharacter(1300360)
    EnableCharacter(1300495)
    DisableCharacter(1300363)
    EnableCharacter(1300496)
    WaitFrames(30)  # enough time for other maps to trigger too
    DisableFlag(TriggerFlags.OopsAllBonewheels)
    # No need to restart.


@RestartOnRest
def HyperAggression():
    """ 11302006: Switch AI param of every enemy to its aggressive version. """
    Await(TriggerFlags.HyperAggression or TriggerFlags.HyperAggressionReTrigger)
    
    SetAIParamID(1300300, 230050)
    SetAIParamID(1300100, 265050)
    SetAIParamID(1300120, 265050)
    SetAIParamID(1300140, 265050)
    SetAIParamID(1300160, 265050)
    SetAIParamID(1300180, 265050)
    SetAIParamID(1300200, 265050)
    SetAIParamID(1300400, 279052)
    SetAIParamID(1300000, 290053)
    SetAIParamID(1300001, 290053)
    SetAIParamID(1300101, 290055)
    SetAIParamID(1300102, 290056)
    SetAIParamID(1300103, 290055)
    SetAIParamID(1300104, 290055)
    SetAIParamID(1300105, 290056)
    SetAIParamID(1300106, 290055)
    SetAIParamID(1300107, 290055)
    SetAIParamID(1300108, 290055)
    SetAIParamID(1300109, 290055)
    SetAIParamID(1300110, 290056)
    SetAIParamID(1300111, 290056)
    SetAIParamID(1300112, 290055)
    SetAIParamID(1300113, 290056)
    SetAIParamID(1300114, 290051)
    SetAIParamID(1300161, 290053)
    SetAIParamID(1300162, 290053)
    SetAIParamID(1300163, 290053)
    SetAIParamID(1300164, 290054)
    SetAIParamID(1300020, 290053)
    SetAIParamID(1300126, 290055)
    SetAIParamID(1300121, 290053)
    SetAIParamID(1300122, 290050)
    SetAIParamID(1300123, 290050)
    SetAIParamID(1300124, 290053)
    SetAIParamID(1300125, 290052)
    SetAIParamID(1300141, 290053)
    SetAIParamID(1300142, 290050)
    SetAIParamID(1300143, 290051)
    SetAIParamID(1300144, 290050)
    SetAIParamID(1300145, 290051)
    SetAIParamID(1300146, 290050)
    SetAIParamID(1300147, 290053)
    SetAIParamID(1300900, 290055)
    SetAIParamID(1300201, 290050)
    SetAIParamID(1300202, 290052)
    SetAIParamID(1300203, 290050)
    SetAIParamID(1300204, 290053)
    SetAIParamID(1300205, 290053)
    SetAIParamID(1300901, 290056)
    SetAIParamID(1300902, 290053)
    SetAIParamID(1300206, 290051)
    SetAIParamID(1300207, 290051)
    SetAIParamID(1300127, 290056)
    SetAIParamID(1300184, 290053)
    SetAIParamID(1300185, 290053)
    SetAIParamID(1300183, 290050)
    SetAIParamID(1300181, 290050)
    SetAIParamID(1300182, 290052)
    SetAIParamID(1300165, 290055)
    SetAIParamID(1300166, 290055)
    SetAIParamID(1300903, 290054)
    SetAIParamID(1300904, 290055)
    SetAIParamID(1300905, 290056)
    SetAIParamID(1300906, 290055)
    SetAIParamID(1300907, 290056)
    SetAIParamID(1300050, 291052)
    SetAIParamID(1300208, 293050)
    SetAIParamID(1300209, 293050)
    SetAIParamID(1300210, 293050)
    SetAIParamID(1300211, 293050)
    SetAIParamID(1300212, 293050)
    SetAIParamID(1300213, 293050)
    SetAIParamID(1300214, 293050)
    SetAIParamID(1300908, 293050)
    SetAIParamID(1300909, 293050)
    SetAIParamID(1300910, 293050)
    SetAIParamID(1300500, 330050)
    SetAIParamID(1300501, 330050)
    SetAIParamID(1300800, 332050)
    SetAIParamID(1300801, 332051)
    SetAIParamID(1300802, 332051)
    SetAIParamID(1300803, 332051)
    SetAIParamID(1300804, 332051)
    SetAIParamID(1300805, 332051)
    SetAIParamID(1300806, 332051)
    SetAIParamID(1300807, 332051)
    SetAIParamID(1300808, 332051)
    SetAIParamID(1300809, 332051)
    SetAIParamID(1300810, 332051)
    SetAIParamID(1300811, 332051)
    SetAIParamID(1300812, 332051)
    SetAIParamID(1300813, 332051)
    SetAIParamID(1300814, 332051)
    SetAIParamID(1303900, 349050)
    SetAIParamID(1303910, 349050)
    SetAIParamID(1303902, 349150)
    SetAIParamID(1303901, 349150)
    SetAIParamID(1303911, 349150)
    SetAIParamID(1303912, 349150)
    SetAIParamID(1300350, 350151)
    SetAIParamID(1300351, 350151)
    SetAIParamID(1300352, 350151)
    SetAIParamID(1300353, 350151)
    SetAIParamID(1300354, 350151)
    SetAIParamID(1300355, 350151)
    SetAIParamID(1300356, 350151)
    SetAIParamID(1300357, 350151)
    SetAIParamID(1300358, 350151)
    SetAIParamID(1300359, 350151)
    SetAIParamID(1300360, 350151)
    SetAIParamID(1300363, 350151)
    SetAIParamID(1300600, 537050)
    SetAIParamID(1300601, 537050)
    SetAIParamID(1300602, 537050)
    SetAIParamID(1300603, 537050)
    SetAIParamID(1300604, 537050)
    SetAIParamID(1300605, 537050)
    SetAIParamID(1300606, 537050)
    SetAIParamID(1300607, 537050)
    SetAIParamID(1300608, 537050)
    SetAIParamID(1300609, 537050)
    SetAIParamID(1300610, 537050)
    SetAIParamID(1300611, 537050)
    SetAIParamID(1300612, 537050)
    SetAIParamID(1300613, 537050)
    SetAIParamID(1300614, 537050)
    SetAIParamID(1300615, 537050)
    SetAIParamID(1300616, 537050)
    SetAIParamID(1300617, 537050)
    SetAIParamID(1300618, 537050)
    SetAIParamID(1300619, 537050)
    SetAIParamID(1300620, 537050)
    SetAIParamID(1300401, 293050)
    SetAIParamID(1300402, 293050)
    SetAIParamID(1300403, 293050)
    SetAIParamID(1300404, 293050)
    SetAIParamID(1300405, 293050)
    SetAIParamID(1300406, 293050)
    SetAIParamID(1300407, 293050)
    SetAIParamID(1300408, 293050)
    SetAIParamID(1300409, 293050)
    SetAIParamID(1300410, 293050)
    SetAIParamID(1300411, 293050)
    SetAIParamID(1300412, 293050)
    SetAIParamID(1300413, 293050)
    SetAIParamID(1300414, 293050)
    SetAIParamID(1300415, 293050)
    SetAIParamID(1300416, 293050)
    SetAIParamID(1300417, 293050)
    SetAIParamID(1300418, 293050)
    SetAIParamID(1300419, 293050)
    SetAIParamID(1300420, 293050)
    SetAIParamID(1300421, 293050)
    SetAIParamID(1300422, 293050)
    SetAIParamID(1300423, 293050)
    SetAIParamID(1300424, 293050)
    SetAIParamID(1300425, 293050)
    SetAIParamID(1300426, 293050)
    SetAIParamID(1300427, 293050)
    SetAIParamID(1300428, 293050)
    SetAIParamID(1300429, 293050)
    SetAIParamID(1300430, 293050)
    SetAIParamID(1300431, 293050)
    SetAIParamID(1300432, 293050)
    SetAIParamID(1300433, 293050)
    SetAIParamID(1300434, 293050)
    SetAIParamID(1300435, 293050)
    SetAIParamID(1300436, 293050)
    SetAIParamID(1300437, 293050)
    SetAIParamID(1300438, 293050)
    SetAIParamID(1300439, 293050)
    SetAIParamID(1300440, 293050)
    SetAIParamID(1300441, 293050)
    SetAIParamID(1300442, 293050)
    SetAIParamID(1300443, 293050)
    SetAIParamID(1300444, 293050)
    SetAIParamID(1300445, 293050)
    SetAIParamID(1300446, 293050)
    SetAIParamID(1300447, 293050)
    SetAIParamID(1300448, 293050)
    SetAIParamID(1300449, 293050)
    SetAIParamID(1300450, 293050)
    SetAIParamID(1300451, 293050)
    SetAIParamID(1300452, 293050)
    SetAIParamID(1300453, 293050)
    SetAIParamID(1300454, 293050)
    SetAIParamID(1300455, 293050)
    SetAIParamID(1300456, 293050)
    SetAIParamID(1300457, 293050)
    SetAIParamID(1300458, 293050)
    SetAIParamID(1300459, 293050)
    SetAIParamID(1300460, 293050)
    SetAIParamID(1300461, 293050)
    SetAIParamID(1300462, 293050)
    SetAIParamID(1300463, 293050)
    SetAIParamID(1300464, 293050)
    SetAIParamID(1300465, 293050)
    SetAIParamID(1300466, 293050)
    SetAIParamID(1300467, 293050)
    SetAIParamID(1300468, 293050)
    SetAIParamID(1300469, 293050)
    SetAIParamID(1300470, 293050)
    SetAIParamID(1300471, 293050)
    SetAIParamID(1300472, 293050)
    SetAIParamID(1300473, 293050)
    SetAIParamID(1300474, 293050)
    SetAIParamID(1300475, 293050)
    SetAIParamID(1300476, 293050)
    SetAIParamID(1300477, 293050)
    SetAIParamID(1300478, 293050)
    SetAIParamID(1300479, 293050)
    SetAIParamID(1300480, 293050)
    SetAIParamID(1300481, 293050)
    SetAIParamID(1300482, 293050)
    SetAIParamID(1300483, 293050)
    SetAIParamID(1300484, 293050)
    SetAIParamID(1300485, 293050)
    SetAIParamID(1300486, 293050)
    SetAIParamID(1300487, 293050)
    SetAIParamID(1300488, 293050)
    SetAIParamID(1300489, 293050)
    SetAIParamID(1300490, 293050)
    SetAIParamID(1300491, 293050)
    SetAIParamID(1300492, 293050)
    SetAIParamID(1300493, 293050)
    SetAIParamID(1300494, 293050)
    SetAIParamID(1300495, 293050)
    SetAIParamID(1300496, 293050)
        
    # Common EMEVD manages the flags that control this event.
    Await(not TriggerFlags.HyperAggressionReTrigger)
    
    SetAIParamID(1300300, 230000)
    SetAIParamID(1300100, 265000)
    SetAIParamID(1300120, 265000)
    SetAIParamID(1300140, 265000)
    SetAIParamID(1300160, 265000)
    SetAIParamID(1300180, 265000)
    SetAIParamID(1300200, 265000)
    SetAIParamID(1300400, 279002)
    SetAIParamID(1300000, 290003)
    SetAIParamID(1300001, 290003)
    SetAIParamID(1300101, 290005)
    SetAIParamID(1300102, 290006)
    SetAIParamID(1300103, 290005)
    SetAIParamID(1300104, 290005)
    SetAIParamID(1300105, 290006)
    SetAIParamID(1300106, 290005)
    SetAIParamID(1300107, 290005)
    SetAIParamID(1300108, 290005)
    SetAIParamID(1300109, 290005)
    SetAIParamID(1300110, 290006)
    SetAIParamID(1300111, 290006)
    SetAIParamID(1300112, 290005)
    SetAIParamID(1300113, 290006)
    SetAIParamID(1300114, 290001)
    SetAIParamID(1300161, 290003)
    SetAIParamID(1300162, 290003)
    SetAIParamID(1300163, 290003)
    SetAIParamID(1300164, 290004)
    SetAIParamID(1300020, 290003)
    SetAIParamID(1300126, 290005)
    SetAIParamID(1300121, 290003)
    SetAIParamID(1300122, 290000)
    SetAIParamID(1300123, 290000)
    SetAIParamID(1300124, 290003)
    SetAIParamID(1300125, 290002)
    SetAIParamID(1300141, 290003)
    SetAIParamID(1300142, 290000)
    SetAIParamID(1300143, 290001)
    SetAIParamID(1300144, 290000)
    SetAIParamID(1300145, 290001)
    SetAIParamID(1300146, 290000)
    SetAIParamID(1300147, 290003)
    SetAIParamID(1300900, 290005)
    SetAIParamID(1300201, 290000)
    SetAIParamID(1300202, 290002)
    SetAIParamID(1300203, 290000)
    SetAIParamID(1300204, 290003)
    SetAIParamID(1300205, 290003)
    SetAIParamID(1300901, 290006)
    SetAIParamID(1300902, 290003)
    SetAIParamID(1300206, 290001)
    SetAIParamID(1300207, 290001)
    SetAIParamID(1300127, 290006)
    SetAIParamID(1300184, 290003)
    SetAIParamID(1300185, 290003)
    SetAIParamID(1300183, 290000)
    SetAIParamID(1300181, 290000)
    SetAIParamID(1300182, 290002)
    SetAIParamID(1300165, 290005)
    SetAIParamID(1300166, 290005)
    SetAIParamID(1300903, 290004)
    SetAIParamID(1300904, 290005)
    SetAIParamID(1300905, 290006)
    SetAIParamID(1300906, 290005)
    SetAIParamID(1300907, 290006)
    SetAIParamID(1300050, 291002)
    SetAIParamID(1300208, 293000)
    SetAIParamID(1300209, 293000)
    SetAIParamID(1300210, 293000)
    SetAIParamID(1300211, 293000)
    SetAIParamID(1300212, 293000)
    SetAIParamID(1300213, 293000)
    SetAIParamID(1300214, 293000)
    SetAIParamID(1300908, 293000)
    SetAIParamID(1300909, 293000)
    SetAIParamID(1300910, 293000)
    SetAIParamID(1300500, 330000)
    SetAIParamID(1300501, 330000)
    SetAIParamID(1300800, 332000)
    SetAIParamID(1300801, 332001)
    SetAIParamID(1300802, 332001)
    SetAIParamID(1300803, 332001)
    SetAIParamID(1300804, 332001)
    SetAIParamID(1300805, 332001)
    SetAIParamID(1300806, 332001)
    SetAIParamID(1300807, 332001)
    SetAIParamID(1300808, 332001)
    SetAIParamID(1300809, 332001)
    SetAIParamID(1300810, 332001)
    SetAIParamID(1300811, 332001)
    SetAIParamID(1300812, 332001)
    SetAIParamID(1300813, 332001)
    SetAIParamID(1300814, 332001)
    SetAIParamID(1303900, 349000)
    SetAIParamID(1303910, 349000)
    SetAIParamID(1303902, 349100)
    SetAIParamID(1303901, 349100)
    SetAIParamID(1303911, 349100)
    SetAIParamID(1303912, 349100)
    SetAIParamID(1300350, 350101)
    SetAIParamID(1300351, 350101)
    SetAIParamID(1300352, 350101)
    SetAIParamID(1300353, 350101)
    SetAIParamID(1300354, 350101)
    SetAIParamID(1300355, 350101)
    SetAIParamID(1300356, 350101)
    SetAIParamID(1300357, 350101)
    SetAIParamID(1300358, 350101)
    SetAIParamID(1300359, 350101)
    SetAIParamID(1300360, 350101)
    SetAIParamID(1300363, 350101)
    SetAIParamID(1300600, 537000)
    SetAIParamID(1300601, 537000)
    SetAIParamID(1300602, 537000)
    SetAIParamID(1300603, 537000)
    SetAIParamID(1300604, 537000)
    SetAIParamID(1300605, 537000)
    SetAIParamID(1300606, 537000)
    SetAIParamID(1300607, 537000)
    SetAIParamID(1300608, 537000)
    SetAIParamID(1300609, 537000)
    SetAIParamID(1300610, 537000)
    SetAIParamID(1300611, 537000)
    SetAIParamID(1300612, 537000)
    SetAIParamID(1300613, 537000)
    SetAIParamID(1300614, 537000)
    SetAIParamID(1300615, 537000)
    SetAIParamID(1300616, 537000)
    SetAIParamID(1300617, 537000)
    SetAIParamID(1300618, 537000)
    SetAIParamID(1300619, 537000)
    SetAIParamID(1300620, 537000)
    SetAIParamID(1300401, 293000)
    SetAIParamID(1300402, 293000)
    SetAIParamID(1300403, 293000)
    SetAIParamID(1300404, 293000)
    SetAIParamID(1300405, 293000)
    SetAIParamID(1300406, 293000)
    SetAIParamID(1300407, 293000)
    SetAIParamID(1300408, 293000)
    SetAIParamID(1300409, 293000)
    SetAIParamID(1300410, 293000)
    SetAIParamID(1300411, 293000)
    SetAIParamID(1300412, 293000)
    SetAIParamID(1300413, 293000)
    SetAIParamID(1300414, 293000)
    SetAIParamID(1300415, 293000)
    SetAIParamID(1300416, 293000)
    SetAIParamID(1300417, 293000)
    SetAIParamID(1300418, 293000)
    SetAIParamID(1300419, 293000)
    SetAIParamID(1300420, 293000)
    SetAIParamID(1300421, 293000)
    SetAIParamID(1300422, 293000)
    SetAIParamID(1300423, 293000)
    SetAIParamID(1300424, 293000)
    SetAIParamID(1300425, 293000)
    SetAIParamID(1300426, 293000)
    SetAIParamID(1300427, 293000)
    SetAIParamID(1300428, 293000)
    SetAIParamID(1300429, 293000)
    SetAIParamID(1300430, 293000)
    SetAIParamID(1300431, 293000)
    SetAIParamID(1300432, 293000)
    SetAIParamID(1300433, 293000)
    SetAIParamID(1300434, 293000)
    SetAIParamID(1300435, 293000)
    SetAIParamID(1300436, 293000)
    SetAIParamID(1300437, 293000)
    SetAIParamID(1300438, 293000)
    SetAIParamID(1300439, 293000)
    SetAIParamID(1300440, 293000)
    SetAIParamID(1300441, 293000)
    SetAIParamID(1300442, 293000)
    SetAIParamID(1300443, 293000)
    SetAIParamID(1300444, 293000)
    SetAIParamID(1300445, 293000)
    SetAIParamID(1300446, 293000)
    SetAIParamID(1300447, 293000)
    SetAIParamID(1300448, 293000)
    SetAIParamID(1300449, 293000)
    SetAIParamID(1300450, 293000)
    SetAIParamID(1300451, 293000)
    SetAIParamID(1300452, 293000)
    SetAIParamID(1300453, 293000)
    SetAIParamID(1300454, 293000)
    SetAIParamID(1300455, 293000)
    SetAIParamID(1300456, 293000)
    SetAIParamID(1300457, 293000)
    SetAIParamID(1300458, 293000)
    SetAIParamID(1300459, 293000)
    SetAIParamID(1300460, 293000)
    SetAIParamID(1300461, 293000)
    SetAIParamID(1300462, 293000)
    SetAIParamID(1300463, 293000)
    SetAIParamID(1300464, 293000)
    SetAIParamID(1300465, 293000)
    SetAIParamID(1300466, 293000)
    SetAIParamID(1300467, 293000)
    SetAIParamID(1300468, 293000)
    SetAIParamID(1300469, 293000)
    SetAIParamID(1300470, 293000)
    SetAIParamID(1300471, 293000)
    SetAIParamID(1300472, 293000)
    SetAIParamID(1300473, 293000)
    SetAIParamID(1300474, 293000)
    SetAIParamID(1300475, 293000)
    SetAIParamID(1300476, 293000)
    SetAIParamID(1300477, 293000)
    SetAIParamID(1300478, 293000)
    SetAIParamID(1300479, 293000)
    SetAIParamID(1300480, 293000)
    SetAIParamID(1300481, 293000)
    SetAIParamID(1300482, 293000)
    SetAIParamID(1300483, 293000)
    SetAIParamID(1300484, 293000)
    SetAIParamID(1300485, 293000)
    SetAIParamID(1300486, 293000)
    SetAIParamID(1300487, 293000)
    SetAIParamID(1300488, 293000)
    SetAIParamID(1300489, 293000)
    SetAIParamID(1300490, 293000)
    SetAIParamID(1300491, 293000)
    SetAIParamID(1300492, 293000)
    SetAIParamID(1300493, 293000)
    SetAIParamID(1300494, 293000)
    SetAIParamID(1300495, 293000)
    SetAIParamID(1300496, 293000)
    
    return RESTART


@RestartOnRest
def EnemySpeedUp():
    """ 11302200: Temporary enemy effect. """
    Await(TriggerFlags.EnemySpeedUp)
    AddSpecialEffect(6320, 200000)
    AddSpecialEffect(6550, 200000)
    AddSpecialEffect(1300960, 200000)
    AddSpecialEffect(1300961, 200000)
    AddSpecialEffect(1300962, 200000)
    AddSpecialEffect(1300300, 200000)
    AddSpecialEffect(1300100, 200000)
    AddSpecialEffect(1300120, 200000)
    AddSpecialEffect(1300140, 200000)
    AddSpecialEffect(1300160, 200000)
    AddSpecialEffect(1300180, 200000)
    AddSpecialEffect(1300200, 200000)
    AddSpecialEffect(1300400, 200000)
    AddSpecialEffect(1300000, 200000)
    AddSpecialEffect(1300001, 200000)
    AddSpecialEffect(1300101, 200000)
    AddSpecialEffect(1300102, 200000)
    AddSpecialEffect(1300103, 200000)
    AddSpecialEffect(1300104, 200000)
    AddSpecialEffect(1300105, 200000)
    AddSpecialEffect(1300106, 200000)
    AddSpecialEffect(1300107, 200000)
    AddSpecialEffect(1300108, 200000)
    AddSpecialEffect(1300109, 200000)
    AddSpecialEffect(1300110, 200000)
    AddSpecialEffect(1300111, 200000)
    AddSpecialEffect(1300112, 200000)
    AddSpecialEffect(1300113, 200000)
    AddSpecialEffect(1300114, 200000)
    AddSpecialEffect(1300161, 200000)
    AddSpecialEffect(1300162, 200000)
    AddSpecialEffect(1300163, 200000)
    AddSpecialEffect(1300164, 200000)
    AddSpecialEffect(1300020, 200000)
    AddSpecialEffect(1300126, 200000)
    AddSpecialEffect(1300121, 200000)
    AddSpecialEffect(1300122, 200000)
    AddSpecialEffect(1300123, 200000)
    AddSpecialEffect(1300124, 200000)
    AddSpecialEffect(1300125, 200000)
    AddSpecialEffect(1300141, 200000)
    AddSpecialEffect(1300142, 200000)
    AddSpecialEffect(1300143, 200000)
    AddSpecialEffect(1300144, 200000)
    AddSpecialEffect(1300145, 200000)
    AddSpecialEffect(1300146, 200000)
    AddSpecialEffect(1300147, 200000)
    AddSpecialEffect(1300900, 200000)
    AddSpecialEffect(1300201, 200000)
    AddSpecialEffect(1300202, 200000)
    AddSpecialEffect(1300203, 200000)
    AddSpecialEffect(1300204, 200000)
    AddSpecialEffect(1300205, 200000)
    AddSpecialEffect(1300901, 200000)
    AddSpecialEffect(1300902, 200000)
    AddSpecialEffect(1300206, 200000)
    AddSpecialEffect(1300207, 200000)
    AddSpecialEffect(1300127, 200000)
    AddSpecialEffect(1300184, 200000)
    AddSpecialEffect(1300185, 200000)
    AddSpecialEffect(1300183, 200000)
    AddSpecialEffect(1300181, 200000)
    AddSpecialEffect(1300182, 200000)
    AddSpecialEffect(1300165, 200000)
    AddSpecialEffect(1300166, 200000)
    AddSpecialEffect(1300903, 200000)
    AddSpecialEffect(1300904, 200000)
    AddSpecialEffect(1300905, 200000)
    AddSpecialEffect(1300906, 200000)
    AddSpecialEffect(1300907, 200000)
    AddSpecialEffect(1300050, 200000)
    AddSpecialEffect(6200, 200000)
    AddSpecialEffect(1300208, 200000)
    AddSpecialEffect(1300209, 200000)
    AddSpecialEffect(1300210, 200000)
    AddSpecialEffect(1300211, 200000)
    AddSpecialEffect(1300212, 200000)
    AddSpecialEffect(1300213, 200000)
    AddSpecialEffect(1300214, 200000)
    AddSpecialEffect(1300908, 200000)
    AddSpecialEffect(1300909, 200000)
    AddSpecialEffect(1300910, 200000)
    AddSpecialEffect(1300500, 200000)
    AddSpecialEffect(1300501, 200000)
    AddSpecialEffect(1300800, 200000)
    AddSpecialEffect(1300801, 200000)
    AddSpecialEffect(1300802, 200000)
    AddSpecialEffect(1300803, 200000)
    AddSpecialEffect(1300804, 200000)
    AddSpecialEffect(1300805, 200000)
    AddSpecialEffect(1300806, 200000)
    AddSpecialEffect(1300807, 200000)
    AddSpecialEffect(1300808, 200000)
    AddSpecialEffect(1300809, 200000)
    AddSpecialEffect(1300810, 200000)
    AddSpecialEffect(1300811, 200000)
    AddSpecialEffect(1300812, 200000)
    AddSpecialEffect(1300813, 200000)
    AddSpecialEffect(1300814, 200000)
    AddSpecialEffect(1303900, 200000)
    AddSpecialEffect(1303910, 200000)
    AddSpecialEffect(1303902, 200000)
    AddSpecialEffect(1303901, 200000)
    AddSpecialEffect(1303911, 200000)
    AddSpecialEffect(1303912, 200000)
    AddSpecialEffect(1300350, 200000)
    AddSpecialEffect(1300351, 200000)
    AddSpecialEffect(1300352, 200000)
    AddSpecialEffect(1300353, 200000)
    AddSpecialEffect(1300354, 200000)
    AddSpecialEffect(1300355, 200000)
    AddSpecialEffect(1300356, 200000)
    AddSpecialEffect(1300357, 200000)
    AddSpecialEffect(1300358, 200000)
    AddSpecialEffect(1300359, 200000)
    AddSpecialEffect(1300360, 200000)
    AddSpecialEffect(1300363, 200000)
    WaitFrames(10)  # give other loaded maps time to trigger
    DisableFlag(TriggerFlags.EnemySpeedUp)
    return RESTART


@RestartOnRest
def EnemyExtremeSpeedUp():
    """ 11302201: Temporary enemy effect. """
    Await(TriggerFlags.EnemyExtremeSpeedUp)
    AddSpecialEffect(6320, 200001)
    AddSpecialEffect(6550, 200001)
    AddSpecialEffect(1300960, 200001)
    AddSpecialEffect(1300961, 200001)
    AddSpecialEffect(1300962, 200001)
    AddSpecialEffect(1300300, 200001)
    AddSpecialEffect(1300100, 200001)
    AddSpecialEffect(1300120, 200001)
    AddSpecialEffect(1300140, 200001)
    AddSpecialEffect(1300160, 200001)
    AddSpecialEffect(1300180, 200001)
    AddSpecialEffect(1300200, 200001)
    AddSpecialEffect(1300400, 200001)
    AddSpecialEffect(1300000, 200001)
    AddSpecialEffect(1300001, 200001)
    AddSpecialEffect(1300101, 200001)
    AddSpecialEffect(1300102, 200001)
    AddSpecialEffect(1300103, 200001)
    AddSpecialEffect(1300104, 200001)
    AddSpecialEffect(1300105, 200001)
    AddSpecialEffect(1300106, 200001)
    AddSpecialEffect(1300107, 200001)
    AddSpecialEffect(1300108, 200001)
    AddSpecialEffect(1300109, 200001)
    AddSpecialEffect(1300110, 200001)
    AddSpecialEffect(1300111, 200001)
    AddSpecialEffect(1300112, 200001)
    AddSpecialEffect(1300113, 200001)
    AddSpecialEffect(1300114, 200001)
    AddSpecialEffect(1300161, 200001)
    AddSpecialEffect(1300162, 200001)
    AddSpecialEffect(1300163, 200001)
    AddSpecialEffect(1300164, 200001)
    AddSpecialEffect(1300020, 200001)
    AddSpecialEffect(1300126, 200001)
    AddSpecialEffect(1300121, 200001)
    AddSpecialEffect(1300122, 200001)
    AddSpecialEffect(1300123, 200001)
    AddSpecialEffect(1300124, 200001)
    AddSpecialEffect(1300125, 200001)
    AddSpecialEffect(1300141, 200001)
    AddSpecialEffect(1300142, 200001)
    AddSpecialEffect(1300143, 200001)
    AddSpecialEffect(1300144, 200001)
    AddSpecialEffect(1300145, 200001)
    AddSpecialEffect(1300146, 200001)
    AddSpecialEffect(1300147, 200001)
    AddSpecialEffect(1300900, 200001)
    AddSpecialEffect(1300201, 200001)
    AddSpecialEffect(1300202, 200001)
    AddSpecialEffect(1300203, 200001)
    AddSpecialEffect(1300204, 200001)
    AddSpecialEffect(1300205, 200001)
    AddSpecialEffect(1300901, 200001)
    AddSpecialEffect(1300902, 200001)
    AddSpecialEffect(1300206, 200001)
    AddSpecialEffect(1300207, 200001)
    AddSpecialEffect(1300127, 200001)
    AddSpecialEffect(1300184, 200001)
    AddSpecialEffect(1300185, 200001)
    AddSpecialEffect(1300183, 200001)
    AddSpecialEffect(1300181, 200001)
    AddSpecialEffect(1300182, 200001)
    AddSpecialEffect(1300165, 200001)
    AddSpecialEffect(1300166, 200001)
    AddSpecialEffect(1300903, 200001)
    AddSpecialEffect(1300904, 200001)
    AddSpecialEffect(1300905, 200001)
    AddSpecialEffect(1300906, 200001)
    AddSpecialEffect(1300907, 200001)
    AddSpecialEffect(1300050, 200001)
    AddSpecialEffect(6200, 200001)
    AddSpecialEffect(1300208, 200001)
    AddSpecialEffect(1300209, 200001)
    AddSpecialEffect(1300210, 200001)
    AddSpecialEffect(1300211, 200001)
    AddSpecialEffect(1300212, 200001)
    AddSpecialEffect(1300213, 200001)
    AddSpecialEffect(1300214, 200001)
    AddSpecialEffect(1300908, 200001)
    AddSpecialEffect(1300909, 200001)
    AddSpecialEffect(1300910, 200001)
    AddSpecialEffect(1300500, 200001)
    AddSpecialEffect(1300501, 200001)
    AddSpecialEffect(1300800, 200001)
    AddSpecialEffect(1300801, 200001)
    AddSpecialEffect(1300802, 200001)
    AddSpecialEffect(1300803, 200001)
    AddSpecialEffect(1300804, 200001)
    AddSpecialEffect(1300805, 200001)
    AddSpecialEffect(1300806, 200001)
    AddSpecialEffect(1300807, 200001)
    AddSpecialEffect(1300808, 200001)
    AddSpecialEffect(1300809, 200001)
    AddSpecialEffect(1300810, 200001)
    AddSpecialEffect(1300811, 200001)
    AddSpecialEffect(1300812, 200001)
    AddSpecialEffect(1300813, 200001)
    AddSpecialEffect(1300814, 200001)
    AddSpecialEffect(1303900, 200001)
    AddSpecialEffect(1303910, 200001)
    AddSpecialEffect(1303902, 200001)
    AddSpecialEffect(1303901, 200001)
    AddSpecialEffect(1303911, 200001)
    AddSpecialEffect(1303912, 200001)
    AddSpecialEffect(1300350, 200001)
    AddSpecialEffect(1300351, 200001)
    AddSpecialEffect(1300352, 200001)
    AddSpecialEffect(1300353, 200001)
    AddSpecialEffect(1300354, 200001)
    AddSpecialEffect(1300355, 200001)
    AddSpecialEffect(1300356, 200001)
    AddSpecialEffect(1300357, 200001)
    AddSpecialEffect(1300358, 200001)
    AddSpecialEffect(1300359, 200001)
    AddSpecialEffect(1300360, 200001)
    AddSpecialEffect(1300363, 200001)
    WaitFrames(10)  # give other loaded maps time to trigger
    DisableFlag(TriggerFlags.EnemyExtremeSpeedUp)
    return RESTART


@RestartOnRest
def EnemySpeedDown():
    """ 11302202: Temporary enemy effect. """
    Await(TriggerFlags.EnemySpeedDown)
    AddSpecialEffect(6320, 200002)
    AddSpecialEffect(6550, 200002)
    AddSpecialEffect(1300960, 200002)
    AddSpecialEffect(1300961, 200002)
    AddSpecialEffect(1300962, 200002)
    AddSpecialEffect(1300300, 200002)
    AddSpecialEffect(1300100, 200002)
    AddSpecialEffect(1300120, 200002)
    AddSpecialEffect(1300140, 200002)
    AddSpecialEffect(1300160, 200002)
    AddSpecialEffect(1300180, 200002)
    AddSpecialEffect(1300200, 200002)
    AddSpecialEffect(1300400, 200002)
    AddSpecialEffect(1300000, 200002)
    AddSpecialEffect(1300001, 200002)
    AddSpecialEffect(1300101, 200002)
    AddSpecialEffect(1300102, 200002)
    AddSpecialEffect(1300103, 200002)
    AddSpecialEffect(1300104, 200002)
    AddSpecialEffect(1300105, 200002)
    AddSpecialEffect(1300106, 200002)
    AddSpecialEffect(1300107, 200002)
    AddSpecialEffect(1300108, 200002)
    AddSpecialEffect(1300109, 200002)
    AddSpecialEffect(1300110, 200002)
    AddSpecialEffect(1300111, 200002)
    AddSpecialEffect(1300112, 200002)
    AddSpecialEffect(1300113, 200002)
    AddSpecialEffect(1300114, 200002)
    AddSpecialEffect(1300161, 200002)
    AddSpecialEffect(1300162, 200002)
    AddSpecialEffect(1300163, 200002)
    AddSpecialEffect(1300164, 200002)
    AddSpecialEffect(1300020, 200002)
    AddSpecialEffect(1300126, 200002)
    AddSpecialEffect(1300121, 200002)
    AddSpecialEffect(1300122, 200002)
    AddSpecialEffect(1300123, 200002)
    AddSpecialEffect(1300124, 200002)
    AddSpecialEffect(1300125, 200002)
    AddSpecialEffect(1300141, 200002)
    AddSpecialEffect(1300142, 200002)
    AddSpecialEffect(1300143, 200002)
    AddSpecialEffect(1300144, 200002)
    AddSpecialEffect(1300145, 200002)
    AddSpecialEffect(1300146, 200002)
    AddSpecialEffect(1300147, 200002)
    AddSpecialEffect(1300900, 200002)
    AddSpecialEffect(1300201, 200002)
    AddSpecialEffect(1300202, 200002)
    AddSpecialEffect(1300203, 200002)
    AddSpecialEffect(1300204, 200002)
    AddSpecialEffect(1300205, 200002)
    AddSpecialEffect(1300901, 200002)
    AddSpecialEffect(1300902, 200002)
    AddSpecialEffect(1300206, 200002)
    AddSpecialEffect(1300207, 200002)
    AddSpecialEffect(1300127, 200002)
    AddSpecialEffect(1300184, 200002)
    AddSpecialEffect(1300185, 200002)
    AddSpecialEffect(1300183, 200002)
    AddSpecialEffect(1300181, 200002)
    AddSpecialEffect(1300182, 200002)
    AddSpecialEffect(1300165, 200002)
    AddSpecialEffect(1300166, 200002)
    AddSpecialEffect(1300903, 200002)
    AddSpecialEffect(1300904, 200002)
    AddSpecialEffect(1300905, 200002)
    AddSpecialEffect(1300906, 200002)
    AddSpecialEffect(1300907, 200002)
    AddSpecialEffect(1300050, 200002)
    AddSpecialEffect(6200, 200002)
    AddSpecialEffect(1300208, 200002)
    AddSpecialEffect(1300209, 200002)
    AddSpecialEffect(1300210, 200002)
    AddSpecialEffect(1300211, 200002)
    AddSpecialEffect(1300212, 200002)
    AddSpecialEffect(1300213, 200002)
    AddSpecialEffect(1300214, 200002)
    AddSpecialEffect(1300908, 200002)
    AddSpecialEffect(1300909, 200002)
    AddSpecialEffect(1300910, 200002)
    AddSpecialEffect(1300500, 200002)
    AddSpecialEffect(1300501, 200002)
    AddSpecialEffect(1300800, 200002)
    AddSpecialEffect(1300801, 200002)
    AddSpecialEffect(1300802, 200002)
    AddSpecialEffect(1300803, 200002)
    AddSpecialEffect(1300804, 200002)
    AddSpecialEffect(1300805, 200002)
    AddSpecialEffect(1300806, 200002)
    AddSpecialEffect(1300807, 200002)
    AddSpecialEffect(1300808, 200002)
    AddSpecialEffect(1300809, 200002)
    AddSpecialEffect(1300810, 200002)
    AddSpecialEffect(1300811, 200002)
    AddSpecialEffect(1300812, 200002)
    AddSpecialEffect(1300813, 200002)
    AddSpecialEffect(1300814, 200002)
    AddSpecialEffect(1303900, 200002)
    AddSpecialEffect(1303910, 200002)
    AddSpecialEffect(1303902, 200002)
    AddSpecialEffect(1303901, 200002)
    AddSpecialEffect(1303911, 200002)
    AddSpecialEffect(1303912, 200002)
    AddSpecialEffect(1300350, 200002)
    AddSpecialEffect(1300351, 200002)
    AddSpecialEffect(1300352, 200002)
    AddSpecialEffect(1300353, 200002)
    AddSpecialEffect(1300354, 200002)
    AddSpecialEffect(1300355, 200002)
    AddSpecialEffect(1300356, 200002)
    AddSpecialEffect(1300357, 200002)
    AddSpecialEffect(1300358, 200002)
    AddSpecialEffect(1300359, 200002)
    AddSpecialEffect(1300360, 200002)
    AddSpecialEffect(1300363, 200002)
    WaitFrames(10)  # give other loaded maps time to trigger
    DisableFlag(TriggerFlags.EnemySpeedDown)
    return RESTART


@RestartOnRest
def EnemyExtremeSpeedDown():
    """ 11302203: Temporary enemy effect. """
    Await(TriggerFlags.EnemyExtremeSpeedDown)
    AddSpecialEffect(6320, 200003)
    AddSpecialEffect(6550, 200003)
    AddSpecialEffect(1300960, 200003)
    AddSpecialEffect(1300961, 200003)
    AddSpecialEffect(1300962, 200003)
    AddSpecialEffect(1300300, 200003)
    AddSpecialEffect(1300100, 200003)
    AddSpecialEffect(1300120, 200003)
    AddSpecialEffect(1300140, 200003)
    AddSpecialEffect(1300160, 200003)
    AddSpecialEffect(1300180, 200003)
    AddSpecialEffect(1300200, 200003)
    AddSpecialEffect(1300400, 200003)
    AddSpecialEffect(1300000, 200003)
    AddSpecialEffect(1300001, 200003)
    AddSpecialEffect(1300101, 200003)
    AddSpecialEffect(1300102, 200003)
    AddSpecialEffect(1300103, 200003)
    AddSpecialEffect(1300104, 200003)
    AddSpecialEffect(1300105, 200003)
    AddSpecialEffect(1300106, 200003)
    AddSpecialEffect(1300107, 200003)
    AddSpecialEffect(1300108, 200003)
    AddSpecialEffect(1300109, 200003)
    AddSpecialEffect(1300110, 200003)
    AddSpecialEffect(1300111, 200003)
    AddSpecialEffect(1300112, 200003)
    AddSpecialEffect(1300113, 200003)
    AddSpecialEffect(1300114, 200003)
    AddSpecialEffect(1300161, 200003)
    AddSpecialEffect(1300162, 200003)
    AddSpecialEffect(1300163, 200003)
    AddSpecialEffect(1300164, 200003)
    AddSpecialEffect(1300020, 200003)
    AddSpecialEffect(1300126, 200003)
    AddSpecialEffect(1300121, 200003)
    AddSpecialEffect(1300122, 200003)
    AddSpecialEffect(1300123, 200003)
    AddSpecialEffect(1300124, 200003)
    AddSpecialEffect(1300125, 200003)
    AddSpecialEffect(1300141, 200003)
    AddSpecialEffect(1300142, 200003)
    AddSpecialEffect(1300143, 200003)
    AddSpecialEffect(1300144, 200003)
    AddSpecialEffect(1300145, 200003)
    AddSpecialEffect(1300146, 200003)
    AddSpecialEffect(1300147, 200003)
    AddSpecialEffect(1300900, 200003)
    AddSpecialEffect(1300201, 200003)
    AddSpecialEffect(1300202, 200003)
    AddSpecialEffect(1300203, 200003)
    AddSpecialEffect(1300204, 200003)
    AddSpecialEffect(1300205, 200003)
    AddSpecialEffect(1300901, 200003)
    AddSpecialEffect(1300902, 200003)
    AddSpecialEffect(1300206, 200003)
    AddSpecialEffect(1300207, 200003)
    AddSpecialEffect(1300127, 200003)
    AddSpecialEffect(1300184, 200003)
    AddSpecialEffect(1300185, 200003)
    AddSpecialEffect(1300183, 200003)
    AddSpecialEffect(1300181, 200003)
    AddSpecialEffect(1300182, 200003)
    AddSpecialEffect(1300165, 200003)
    AddSpecialEffect(1300166, 200003)
    AddSpecialEffect(1300903, 200003)
    AddSpecialEffect(1300904, 200003)
    AddSpecialEffect(1300905, 200003)
    AddSpecialEffect(1300906, 200003)
    AddSpecialEffect(1300907, 200003)
    AddSpecialEffect(1300050, 200003)
    AddSpecialEffect(6200, 200003)
    AddSpecialEffect(1300208, 200003)
    AddSpecialEffect(1300209, 200003)
    AddSpecialEffect(1300210, 200003)
    AddSpecialEffect(1300211, 200003)
    AddSpecialEffect(1300212, 200003)
    AddSpecialEffect(1300213, 200003)
    AddSpecialEffect(1300214, 200003)
    AddSpecialEffect(1300908, 200003)
    AddSpecialEffect(1300909, 200003)
    AddSpecialEffect(1300910, 200003)
    AddSpecialEffect(1300500, 200003)
    AddSpecialEffect(1300501, 200003)
    AddSpecialEffect(1300800, 200003)
    AddSpecialEffect(1300801, 200003)
    AddSpecialEffect(1300802, 200003)
    AddSpecialEffect(1300803, 200003)
    AddSpecialEffect(1300804, 200003)
    AddSpecialEffect(1300805, 200003)
    AddSpecialEffect(1300806, 200003)
    AddSpecialEffect(1300807, 200003)
    AddSpecialEffect(1300808, 200003)
    AddSpecialEffect(1300809, 200003)
    AddSpecialEffect(1300810, 200003)
    AddSpecialEffect(1300811, 200003)
    AddSpecialEffect(1300812, 200003)
    AddSpecialEffect(1300813, 200003)
    AddSpecialEffect(1300814, 200003)
    AddSpecialEffect(1303900, 200003)
    AddSpecialEffect(1303910, 200003)
    AddSpecialEffect(1303902, 200003)
    AddSpecialEffect(1303901, 200003)
    AddSpecialEffect(1303911, 200003)
    AddSpecialEffect(1303912, 200003)
    AddSpecialEffect(1300350, 200003)
    AddSpecialEffect(1300351, 200003)
    AddSpecialEffect(1300352, 200003)
    AddSpecialEffect(1300353, 200003)
    AddSpecialEffect(1300354, 200003)
    AddSpecialEffect(1300355, 200003)
    AddSpecialEffect(1300356, 200003)
    AddSpecialEffect(1300357, 200003)
    AddSpecialEffect(1300358, 200003)
    AddSpecialEffect(1300359, 200003)
    AddSpecialEffect(1300360, 200003)
    AddSpecialEffect(1300363, 200003)
    WaitFrames(10)  # give other loaded maps time to trigger
    DisableFlag(TriggerFlags.EnemyExtremeSpeedDown)
    return RESTART


@RestartOnRest
def EnemyHealthRegain():
    """ 11302204: Temporary enemy effect. """
    Await(TriggerFlags.EnemyHealthRegain)
    AddSpecialEffect(6320, 200004)
    AddSpecialEffect(6550, 200004)
    AddSpecialEffect(1300960, 200004)
    AddSpecialEffect(1300961, 200004)
    AddSpecialEffect(1300962, 200004)
    AddSpecialEffect(1300300, 200004)
    AddSpecialEffect(1300100, 200004)
    AddSpecialEffect(1300120, 200004)
    AddSpecialEffect(1300140, 200004)
    AddSpecialEffect(1300160, 200004)
    AddSpecialEffect(1300180, 200004)
    AddSpecialEffect(1300200, 200004)
    AddSpecialEffect(1300400, 200004)
    AddSpecialEffect(1300000, 200004)
    AddSpecialEffect(1300001, 200004)
    AddSpecialEffect(1300101, 200004)
    AddSpecialEffect(1300102, 200004)
    AddSpecialEffect(1300103, 200004)
    AddSpecialEffect(1300104, 200004)
    AddSpecialEffect(1300105, 200004)
    AddSpecialEffect(1300106, 200004)
    AddSpecialEffect(1300107, 200004)
    AddSpecialEffect(1300108, 200004)
    AddSpecialEffect(1300109, 200004)
    AddSpecialEffect(1300110, 200004)
    AddSpecialEffect(1300111, 200004)
    AddSpecialEffect(1300112, 200004)
    AddSpecialEffect(1300113, 200004)
    AddSpecialEffect(1300114, 200004)
    AddSpecialEffect(1300161, 200004)
    AddSpecialEffect(1300162, 200004)
    AddSpecialEffect(1300163, 200004)
    AddSpecialEffect(1300164, 200004)
    AddSpecialEffect(1300020, 200004)
    AddSpecialEffect(1300126, 200004)
    AddSpecialEffect(1300121, 200004)
    AddSpecialEffect(1300122, 200004)
    AddSpecialEffect(1300123, 200004)
    AddSpecialEffect(1300124, 200004)
    AddSpecialEffect(1300125, 200004)
    AddSpecialEffect(1300141, 200004)
    AddSpecialEffect(1300142, 200004)
    AddSpecialEffect(1300143, 200004)
    AddSpecialEffect(1300144, 200004)
    AddSpecialEffect(1300145, 200004)
    AddSpecialEffect(1300146, 200004)
    AddSpecialEffect(1300147, 200004)
    AddSpecialEffect(1300900, 200004)
    AddSpecialEffect(1300201, 200004)
    AddSpecialEffect(1300202, 200004)
    AddSpecialEffect(1300203, 200004)
    AddSpecialEffect(1300204, 200004)
    AddSpecialEffect(1300205, 200004)
    AddSpecialEffect(1300901, 200004)
    AddSpecialEffect(1300902, 200004)
    AddSpecialEffect(1300206, 200004)
    AddSpecialEffect(1300207, 200004)
    AddSpecialEffect(1300127, 200004)
    AddSpecialEffect(1300184, 200004)
    AddSpecialEffect(1300185, 200004)
    AddSpecialEffect(1300183, 200004)
    AddSpecialEffect(1300181, 200004)
    AddSpecialEffect(1300182, 200004)
    AddSpecialEffect(1300165, 200004)
    AddSpecialEffect(1300166, 200004)
    AddSpecialEffect(1300903, 200004)
    AddSpecialEffect(1300904, 200004)
    AddSpecialEffect(1300905, 200004)
    AddSpecialEffect(1300906, 200004)
    AddSpecialEffect(1300907, 200004)
    AddSpecialEffect(1300050, 200004)
    AddSpecialEffect(6200, 200004)
    AddSpecialEffect(1300208, 200004)
    AddSpecialEffect(1300209, 200004)
    AddSpecialEffect(1300210, 200004)
    AddSpecialEffect(1300211, 200004)
    AddSpecialEffect(1300212, 200004)
    AddSpecialEffect(1300213, 200004)
    AddSpecialEffect(1300214, 200004)
    AddSpecialEffect(1300908, 200004)
    AddSpecialEffect(1300909, 200004)
    AddSpecialEffect(1300910, 200004)
    AddSpecialEffect(1300500, 200004)
    AddSpecialEffect(1300501, 200004)
    AddSpecialEffect(1300800, 200004)
    AddSpecialEffect(1300801, 200004)
    AddSpecialEffect(1300802, 200004)
    AddSpecialEffect(1300803, 200004)
    AddSpecialEffect(1300804, 200004)
    AddSpecialEffect(1300805, 200004)
    AddSpecialEffect(1300806, 200004)
    AddSpecialEffect(1300807, 200004)
    AddSpecialEffect(1300808, 200004)
    AddSpecialEffect(1300809, 200004)
    AddSpecialEffect(1300810, 200004)
    AddSpecialEffect(1300811, 200004)
    AddSpecialEffect(1300812, 200004)
    AddSpecialEffect(1300813, 200004)
    AddSpecialEffect(1300814, 200004)
    AddSpecialEffect(1303900, 200004)
    AddSpecialEffect(1303910, 200004)
    AddSpecialEffect(1303902, 200004)
    AddSpecialEffect(1303901, 200004)
    AddSpecialEffect(1303911, 200004)
    AddSpecialEffect(1303912, 200004)
    AddSpecialEffect(1300350, 200004)
    AddSpecialEffect(1300351, 200004)
    AddSpecialEffect(1300352, 200004)
    AddSpecialEffect(1300353, 200004)
    AddSpecialEffect(1300354, 200004)
    AddSpecialEffect(1300355, 200004)
    AddSpecialEffect(1300356, 200004)
    AddSpecialEffect(1300357, 200004)
    AddSpecialEffect(1300358, 200004)
    AddSpecialEffect(1300359, 200004)
    AddSpecialEffect(1300360, 200004)
    AddSpecialEffect(1300363, 200004)
    WaitFrames(10)  # give other loaded maps time to trigger
    DisableFlag(TriggerFlags.EnemyHealthRegain)
    return RESTART


@RestartOnRest
def EnemyMaxHealthUp():
    """ 11302205: Temporary enemy effect. """
    Await(TriggerFlags.EnemyMaxHealthUp)
    AddSpecialEffect(6320, 200005)
    AddSpecialEffect(6550, 200005)
    AddSpecialEffect(1300960, 200005)
    AddSpecialEffect(1300961, 200005)
    AddSpecialEffect(1300962, 200005)
    AddSpecialEffect(1300300, 200005)
    AddSpecialEffect(1300100, 200005)
    AddSpecialEffect(1300120, 200005)
    AddSpecialEffect(1300140, 200005)
    AddSpecialEffect(1300160, 200005)
    AddSpecialEffect(1300180, 200005)
    AddSpecialEffect(1300200, 200005)
    AddSpecialEffect(1300400, 200005)
    AddSpecialEffect(1300000, 200005)
    AddSpecialEffect(1300001, 200005)
    AddSpecialEffect(1300101, 200005)
    AddSpecialEffect(1300102, 200005)
    AddSpecialEffect(1300103, 200005)
    AddSpecialEffect(1300104, 200005)
    AddSpecialEffect(1300105, 200005)
    AddSpecialEffect(1300106, 200005)
    AddSpecialEffect(1300107, 200005)
    AddSpecialEffect(1300108, 200005)
    AddSpecialEffect(1300109, 200005)
    AddSpecialEffect(1300110, 200005)
    AddSpecialEffect(1300111, 200005)
    AddSpecialEffect(1300112, 200005)
    AddSpecialEffect(1300113, 200005)
    AddSpecialEffect(1300114, 200005)
    AddSpecialEffect(1300161, 200005)
    AddSpecialEffect(1300162, 200005)
    AddSpecialEffect(1300163, 200005)
    AddSpecialEffect(1300164, 200005)
    AddSpecialEffect(1300020, 200005)
    AddSpecialEffect(1300126, 200005)
    AddSpecialEffect(1300121, 200005)
    AddSpecialEffect(1300122, 200005)
    AddSpecialEffect(1300123, 200005)
    AddSpecialEffect(1300124, 200005)
    AddSpecialEffect(1300125, 200005)
    AddSpecialEffect(1300141, 200005)
    AddSpecialEffect(1300142, 200005)
    AddSpecialEffect(1300143, 200005)
    AddSpecialEffect(1300144, 200005)
    AddSpecialEffect(1300145, 200005)
    AddSpecialEffect(1300146, 200005)
    AddSpecialEffect(1300147, 200005)
    AddSpecialEffect(1300900, 200005)
    AddSpecialEffect(1300201, 200005)
    AddSpecialEffect(1300202, 200005)
    AddSpecialEffect(1300203, 200005)
    AddSpecialEffect(1300204, 200005)
    AddSpecialEffect(1300205, 200005)
    AddSpecialEffect(1300901, 200005)
    AddSpecialEffect(1300902, 200005)
    AddSpecialEffect(1300206, 200005)
    AddSpecialEffect(1300207, 200005)
    AddSpecialEffect(1300127, 200005)
    AddSpecialEffect(1300184, 200005)
    AddSpecialEffect(1300185, 200005)
    AddSpecialEffect(1300183, 200005)
    AddSpecialEffect(1300181, 200005)
    AddSpecialEffect(1300182, 200005)
    AddSpecialEffect(1300165, 200005)
    AddSpecialEffect(1300166, 200005)
    AddSpecialEffect(1300903, 200005)
    AddSpecialEffect(1300904, 200005)
    AddSpecialEffect(1300905, 200005)
    AddSpecialEffect(1300906, 200005)
    AddSpecialEffect(1300907, 200005)
    AddSpecialEffect(1300050, 200005)
    AddSpecialEffect(6200, 200005)
    AddSpecialEffect(1300208, 200005)
    AddSpecialEffect(1300209, 200005)
    AddSpecialEffect(1300210, 200005)
    AddSpecialEffect(1300211, 200005)
    AddSpecialEffect(1300212, 200005)
    AddSpecialEffect(1300213, 200005)
    AddSpecialEffect(1300214, 200005)
    AddSpecialEffect(1300908, 200005)
    AddSpecialEffect(1300909, 200005)
    AddSpecialEffect(1300910, 200005)
    AddSpecialEffect(1300500, 200005)
    AddSpecialEffect(1300501, 200005)
    AddSpecialEffect(1300800, 200005)
    AddSpecialEffect(1300801, 200005)
    AddSpecialEffect(1300802, 200005)
    AddSpecialEffect(1300803, 200005)
    AddSpecialEffect(1300804, 200005)
    AddSpecialEffect(1300805, 200005)
    AddSpecialEffect(1300806, 200005)
    AddSpecialEffect(1300807, 200005)
    AddSpecialEffect(1300808, 200005)
    AddSpecialEffect(1300809, 200005)
    AddSpecialEffect(1300810, 200005)
    AddSpecialEffect(1300811, 200005)
    AddSpecialEffect(1300812, 200005)
    AddSpecialEffect(1300813, 200005)
    AddSpecialEffect(1300814, 200005)
    AddSpecialEffect(1303900, 200005)
    AddSpecialEffect(1303910, 200005)
    AddSpecialEffect(1303902, 200005)
    AddSpecialEffect(1303901, 200005)
    AddSpecialEffect(1303911, 200005)
    AddSpecialEffect(1303912, 200005)
    AddSpecialEffect(1300350, 200005)
    AddSpecialEffect(1300351, 200005)
    AddSpecialEffect(1300352, 200005)
    AddSpecialEffect(1300353, 200005)
    AddSpecialEffect(1300354, 200005)
    AddSpecialEffect(1300355, 200005)
    AddSpecialEffect(1300356, 200005)
    AddSpecialEffect(1300357, 200005)
    AddSpecialEffect(1300358, 200005)
    AddSpecialEffect(1300359, 200005)
    AddSpecialEffect(1300360, 200005)
    AddSpecialEffect(1300363, 200005)
    WaitFrames(10)  # give other loaded maps time to trigger
    DisableFlag(TriggerFlags.EnemyMaxHealthUp)
    return RESTART


@RestartOnRest
def EnemyMaxHealthDown():
    """ 11302206: Temporary enemy effect. """
    Await(TriggerFlags.EnemyMaxHealthDown)
    AddSpecialEffect(6320, 200006)
    AddSpecialEffect(6550, 200006)
    AddSpecialEffect(1300960, 200006)
    AddSpecialEffect(1300961, 200006)
    AddSpecialEffect(1300962, 200006)
    AddSpecialEffect(1300300, 200006)
    AddSpecialEffect(1300100, 200006)
    AddSpecialEffect(1300120, 200006)
    AddSpecialEffect(1300140, 200006)
    AddSpecialEffect(1300160, 200006)
    AddSpecialEffect(1300180, 200006)
    AddSpecialEffect(1300200, 200006)
    AddSpecialEffect(1300400, 200006)
    AddSpecialEffect(1300000, 200006)
    AddSpecialEffect(1300001, 200006)
    AddSpecialEffect(1300101, 200006)
    AddSpecialEffect(1300102, 200006)
    AddSpecialEffect(1300103, 200006)
    AddSpecialEffect(1300104, 200006)
    AddSpecialEffect(1300105, 200006)
    AddSpecialEffect(1300106, 200006)
    AddSpecialEffect(1300107, 200006)
    AddSpecialEffect(1300108, 200006)
    AddSpecialEffect(1300109, 200006)
    AddSpecialEffect(1300110, 200006)
    AddSpecialEffect(1300111, 200006)
    AddSpecialEffect(1300112, 200006)
    AddSpecialEffect(1300113, 200006)
    AddSpecialEffect(1300114, 200006)
    AddSpecialEffect(1300161, 200006)
    AddSpecialEffect(1300162, 200006)
    AddSpecialEffect(1300163, 200006)
    AddSpecialEffect(1300164, 200006)
    AddSpecialEffect(1300020, 200006)
    AddSpecialEffect(1300126, 200006)
    AddSpecialEffect(1300121, 200006)
    AddSpecialEffect(1300122, 200006)
    AddSpecialEffect(1300123, 200006)
    AddSpecialEffect(1300124, 200006)
    AddSpecialEffect(1300125, 200006)
    AddSpecialEffect(1300141, 200006)
    AddSpecialEffect(1300142, 200006)
    AddSpecialEffect(1300143, 200006)
    AddSpecialEffect(1300144, 200006)
    AddSpecialEffect(1300145, 200006)
    AddSpecialEffect(1300146, 200006)
    AddSpecialEffect(1300147, 200006)
    AddSpecialEffect(1300900, 200006)
    AddSpecialEffect(1300201, 200006)
    AddSpecialEffect(1300202, 200006)
    AddSpecialEffect(1300203, 200006)
    AddSpecialEffect(1300204, 200006)
    AddSpecialEffect(1300205, 200006)
    AddSpecialEffect(1300901, 200006)
    AddSpecialEffect(1300902, 200006)
    AddSpecialEffect(1300206, 200006)
    AddSpecialEffect(1300207, 200006)
    AddSpecialEffect(1300127, 200006)
    AddSpecialEffect(1300184, 200006)
    AddSpecialEffect(1300185, 200006)
    AddSpecialEffect(1300183, 200006)
    AddSpecialEffect(1300181, 200006)
    AddSpecialEffect(1300182, 200006)
    AddSpecialEffect(1300165, 200006)
    AddSpecialEffect(1300166, 200006)
    AddSpecialEffect(1300903, 200006)
    AddSpecialEffect(1300904, 200006)
    AddSpecialEffect(1300905, 200006)
    AddSpecialEffect(1300906, 200006)
    AddSpecialEffect(1300907, 200006)
    AddSpecialEffect(1300050, 200006)
    AddSpecialEffect(6200, 200006)
    AddSpecialEffect(1300208, 200006)
    AddSpecialEffect(1300209, 200006)
    AddSpecialEffect(1300210, 200006)
    AddSpecialEffect(1300211, 200006)
    AddSpecialEffect(1300212, 200006)
    AddSpecialEffect(1300213, 200006)
    AddSpecialEffect(1300214, 200006)
    AddSpecialEffect(1300908, 200006)
    AddSpecialEffect(1300909, 200006)
    AddSpecialEffect(1300910, 200006)
    AddSpecialEffect(1300500, 200006)
    AddSpecialEffect(1300501, 200006)
    AddSpecialEffect(1300800, 200006)
    AddSpecialEffect(1300801, 200006)
    AddSpecialEffect(1300802, 200006)
    AddSpecialEffect(1300803, 200006)
    AddSpecialEffect(1300804, 200006)
    AddSpecialEffect(1300805, 200006)
    AddSpecialEffect(1300806, 200006)
    AddSpecialEffect(1300807, 200006)
    AddSpecialEffect(1300808, 200006)
    AddSpecialEffect(1300809, 200006)
    AddSpecialEffect(1300810, 200006)
    AddSpecialEffect(1300811, 200006)
    AddSpecialEffect(1300812, 200006)
    AddSpecialEffect(1300813, 200006)
    AddSpecialEffect(1300814, 200006)
    AddSpecialEffect(1303900, 200006)
    AddSpecialEffect(1303910, 200006)
    AddSpecialEffect(1303902, 200006)
    AddSpecialEffect(1303901, 200006)
    AddSpecialEffect(1303911, 200006)
    AddSpecialEffect(1303912, 200006)
    AddSpecialEffect(1300350, 200006)
    AddSpecialEffect(1300351, 200006)
    AddSpecialEffect(1300352, 200006)
    AddSpecialEffect(1300353, 200006)
    AddSpecialEffect(1300354, 200006)
    AddSpecialEffect(1300355, 200006)
    AddSpecialEffect(1300356, 200006)
    AddSpecialEffect(1300357, 200006)
    AddSpecialEffect(1300358, 200006)
    AddSpecialEffect(1300359, 200006)
    AddSpecialEffect(1300360, 200006)
    AddSpecialEffect(1300363, 200006)
    WaitFrames(10)  # give other loaded maps time to trigger
    DisableFlag(TriggerFlags.EnemyMaxHealthDown)
    return RESTART


@RestartOnRest
def EnemyDefenseUp():
    """ 11302207: Temporary enemy effect. """
    Await(TriggerFlags.EnemyDefenseUp)
    AddSpecialEffect(6320, 200007)
    AddSpecialEffect(6550, 200007)
    AddSpecialEffect(1300960, 200007)
    AddSpecialEffect(1300961, 200007)
    AddSpecialEffect(1300962, 200007)
    AddSpecialEffect(1300300, 200007)
    AddSpecialEffect(1300100, 200007)
    AddSpecialEffect(1300120, 200007)
    AddSpecialEffect(1300140, 200007)
    AddSpecialEffect(1300160, 200007)
    AddSpecialEffect(1300180, 200007)
    AddSpecialEffect(1300200, 200007)
    AddSpecialEffect(1300400, 200007)
    AddSpecialEffect(1300000, 200007)
    AddSpecialEffect(1300001, 200007)
    AddSpecialEffect(1300101, 200007)
    AddSpecialEffect(1300102, 200007)
    AddSpecialEffect(1300103, 200007)
    AddSpecialEffect(1300104, 200007)
    AddSpecialEffect(1300105, 200007)
    AddSpecialEffect(1300106, 200007)
    AddSpecialEffect(1300107, 200007)
    AddSpecialEffect(1300108, 200007)
    AddSpecialEffect(1300109, 200007)
    AddSpecialEffect(1300110, 200007)
    AddSpecialEffect(1300111, 200007)
    AddSpecialEffect(1300112, 200007)
    AddSpecialEffect(1300113, 200007)
    AddSpecialEffect(1300114, 200007)
    AddSpecialEffect(1300161, 200007)
    AddSpecialEffect(1300162, 200007)
    AddSpecialEffect(1300163, 200007)
    AddSpecialEffect(1300164, 200007)
    AddSpecialEffect(1300020, 200007)
    AddSpecialEffect(1300126, 200007)
    AddSpecialEffect(1300121, 200007)
    AddSpecialEffect(1300122, 200007)
    AddSpecialEffect(1300123, 200007)
    AddSpecialEffect(1300124, 200007)
    AddSpecialEffect(1300125, 200007)
    AddSpecialEffect(1300141, 200007)
    AddSpecialEffect(1300142, 200007)
    AddSpecialEffect(1300143, 200007)
    AddSpecialEffect(1300144, 200007)
    AddSpecialEffect(1300145, 200007)
    AddSpecialEffect(1300146, 200007)
    AddSpecialEffect(1300147, 200007)
    AddSpecialEffect(1300900, 200007)
    AddSpecialEffect(1300201, 200007)
    AddSpecialEffect(1300202, 200007)
    AddSpecialEffect(1300203, 200007)
    AddSpecialEffect(1300204, 200007)
    AddSpecialEffect(1300205, 200007)
    AddSpecialEffect(1300901, 200007)
    AddSpecialEffect(1300902, 200007)
    AddSpecialEffect(1300206, 200007)
    AddSpecialEffect(1300207, 200007)
    AddSpecialEffect(1300127, 200007)
    AddSpecialEffect(1300184, 200007)
    AddSpecialEffect(1300185, 200007)
    AddSpecialEffect(1300183, 200007)
    AddSpecialEffect(1300181, 200007)
    AddSpecialEffect(1300182, 200007)
    AddSpecialEffect(1300165, 200007)
    AddSpecialEffect(1300166, 200007)
    AddSpecialEffect(1300903, 200007)
    AddSpecialEffect(1300904, 200007)
    AddSpecialEffect(1300905, 200007)
    AddSpecialEffect(1300906, 200007)
    AddSpecialEffect(1300907, 200007)
    AddSpecialEffect(1300050, 200007)
    AddSpecialEffect(6200, 200007)
    AddSpecialEffect(1300208, 200007)
    AddSpecialEffect(1300209, 200007)
    AddSpecialEffect(1300210, 200007)
    AddSpecialEffect(1300211, 200007)
    AddSpecialEffect(1300212, 200007)
    AddSpecialEffect(1300213, 200007)
    AddSpecialEffect(1300214, 200007)
    AddSpecialEffect(1300908, 200007)
    AddSpecialEffect(1300909, 200007)
    AddSpecialEffect(1300910, 200007)
    AddSpecialEffect(1300500, 200007)
    AddSpecialEffect(1300501, 200007)
    AddSpecialEffect(1300800, 200007)
    AddSpecialEffect(1300801, 200007)
    AddSpecialEffect(1300802, 200007)
    AddSpecialEffect(1300803, 200007)
    AddSpecialEffect(1300804, 200007)
    AddSpecialEffect(1300805, 200007)
    AddSpecialEffect(1300806, 200007)
    AddSpecialEffect(1300807, 200007)
    AddSpecialEffect(1300808, 200007)
    AddSpecialEffect(1300809, 200007)
    AddSpecialEffect(1300810, 200007)
    AddSpecialEffect(1300811, 200007)
    AddSpecialEffect(1300812, 200007)
    AddSpecialEffect(1300813, 200007)
    AddSpecialEffect(1300814, 200007)
    AddSpecialEffect(1303900, 200007)
    AddSpecialEffect(1303910, 200007)
    AddSpecialEffect(1303902, 200007)
    AddSpecialEffect(1303901, 200007)
    AddSpecialEffect(1303911, 200007)
    AddSpecialEffect(1303912, 200007)
    AddSpecialEffect(1300350, 200007)
    AddSpecialEffect(1300351, 200007)
    AddSpecialEffect(1300352, 200007)
    AddSpecialEffect(1300353, 200007)
    AddSpecialEffect(1300354, 200007)
    AddSpecialEffect(1300355, 200007)
    AddSpecialEffect(1300356, 200007)
    AddSpecialEffect(1300357, 200007)
    AddSpecialEffect(1300358, 200007)
    AddSpecialEffect(1300359, 200007)
    AddSpecialEffect(1300360, 200007)
    AddSpecialEffect(1300363, 200007)
    WaitFrames(10)  # give other loaded maps time to trigger
    DisableFlag(TriggerFlags.EnemyDefenseUp)
    return RESTART
