"""
linked:


strings:

"""
from soulstruct.darksouls1r.events import *
from ..entities.m12_00_00_00_entities import *
from ..entities.m12_01_00_00_entities import Points as m12_01_Points
from ..entities.common_entities import *


def Constructor():
    """ 0: Event 0 """
    RegisterBonfire(
        11200984,
        obj=Objects.o0200_0000,
        reaction_distance=2.0,
        reaction_angle=180.0,
        initial_kindle_level=0,
    )
    RegisterLadder(start_climbing_flag=11200010, stop_climbing_flag=11200011, obj=Objects.o2400)
    RegisterLadder(start_climbing_flag=11200012, stop_climbing_flag=11200013, obj=Objects.o2401)
    CreateProjectileOwner(Characters.c2330_0026)
    SkipLinesIfFlagOn(2, 11200000)
    SkipLinesIfFlagOn(1, 11200002)
    SkipLines(1)
    DisableObject(Objects.o2300)
    SkipLinesIfClient(10)
    DisableObject(Objects.o2901_0000)
    DeleteVFX(VFX.MultiplayerFog1, erase_root_only=False)
    DisableObject(Objects.o2902_0000)
    DeleteVFX(VFX.MultiplayerFog2, erase_root_only=False)
    DisableObject(Objects.o2903_0000)
    DeleteVFX(VFX.MultiplayerFog3, erase_root_only=False)
    DisableObject(Objects.o2907_0000)
    DeleteVFX(VFX.MultiplayerFog4, erase_root_only=False)
    DisableObject(Objects.o2908_0000)
    DeleteVFX(VFX.MultiplayerFog5, erase_root_only=False)
    RunEvent(
        11200090,
        slot=0,
        args=(Objects.o2906_0000, VFX.CheckpointFog1, Boxes.CheckpointFog1FrontSide, Boxes.CheckpointFog1BackSide),
    )
    RunEvent(11200100, slot=0, args=(11200110, Objects.o2110, 120020, Boxes.CrestDoorPrompt, 0, 61200500))
    RunEvent(11200110, slot=0, args=(11200100, Objects.o2110, Boxes.CrestDoorPrompt, 0))
    RunEvent(11200100, slot=1, args=(11200111, Objects.o2111, 120021, Boxes.SifOpenDoorPrompt, 1, 61200501))
    RunEvent(11200110, slot=1, args=(11200101, Objects.o2111, Boxes.SifOpenDoorPrompt, 1))
    RunEvent(11200120)
    RunEvent(11205000)
    RunEvent(11200800)
    RunEvent(11200200)
    RunEvent(11200690)
    RunEvent(11200600, slot=0, args=(Objects.o0110_0000, 11200600))
    RunEvent(11200600, slot=1, args=(Objects.o0110_0001, 11200601))
    DisableSoundEvent(1203800)
    SkipLinesIfFlagOff(4, 5)
    RunEvent(11205392)
    DisableObject(Objects.o2900_0000)
    DeleteVFX(VFX.SifEntranceFog, erase_root_only=False)
    SkipLines(9)
    RunEvent(11200000)
    RunEvent(11205390)
    RunEvent(11205391)
    RunEvent(11205393)
    RunEvent(11205392)
    RunEvent(11200001)
    RunEvent(11205394)
    RunEvent(11205395)
    RunEvent(11205396)
    RunEvent(11200002)
    DisableSoundEvent(1203801)
    SkipLinesIfFlagOff(6, 11200900)
    RunEvent(11205382)
    DisableObject(Objects.o2904_0000)
    DeleteVFX(VFX.ButterflyEntranceFog, erase_root_only=False)
    DisableObject(Objects.o2905_0000)
    DeleteVFX(VFX.ButterflyExitFog, erase_root_only=False)
    SkipLines(17)
    RunEvent(11205380)
    RunEvent(11205381)
    RunEvent(11205383)
    RunEvent(11205382)
    RunEvent(11200900)
    RunEvent(11205384)
    RunEvent(11205385)
    RunEvent(11205120, slot=0, args=(Boxes.ButterflyFlyingArea1, Spheres.ButterflyAirJunction1))
    RunEvent(11205120, slot=1, args=(Boxes.ButterflyFlyingArea2, Spheres.ButterflyAirJunction2))
    RunEvent(11205120, slot=2, args=(Boxes.ButterflyFlyingArea3, Spheres.ButterflyAirJunction3))
    RunEvent(11205120, slot=3, args=(Boxes.ButterflyFlyingArea4, Spheres.ButterflyAirJunction4))
    RunEvent(11205120, slot=4, args=(Boxes.ButterflyFlyingArea5, Spheres.ButterflyAirJunction5))
    RunEvent(11205120, slot=5, args=(Boxes.ButterflyFlyingArea6, Spheres.ButterflyAirJunction6))
    RunEvent(11205120, slot=6, args=(Boxes.ButterflyFlyingArea7, Spheres.ButterflyAirJunction7))
    RunEvent(11205120, slot=7, args=(Boxes.ButterflyFlyingArea8, Spheres.ButterflyAirJunction8))
    RunEvent(11205120, slot=8, args=(Boxes.ButterflyFlyingArea9, Spheres.ButterflyAirJunction9))
    RunEvent(11205120, slot=9, args=(Boxes.ButterflyFlyingArea10, Spheres.ButterflyAirJunction10))
    RunEvent(11200801)
    RunEvent(11205300, slot=0, args=(1, 0, 3530, 3530, Characters.c3531_0000, 91, 0, 0), arg_types="hhiiiBBi")
    RunEvent(11205300, slot=1, args=(2, 0, 3531, 3531, Characters.c3531_0001, 92, 0, 1), arg_types="hhiiiBBi")
    RunEvent(11205300, slot=2, args=(3, 0, 3532, 3532, Characters.c3531_0002, 93, 0, 2), arg_types="hhiiiBBi")
    RunEvent(11205300, slot=3, args=(4, 0, 3533, 3533, Characters.c3531_0003, 94, 0, 3), arg_types="hhiiiBBi")
    RunEvent(11205300, slot=4, args=(5, 0, 3534, 3534, Characters.c3531_0004, 95, 0, 4), arg_types="hhiiiBBi")
    RunEvent(11205300, slot=5, args=(6, 0, 3535, 3535, Characters.c3531_0005, 96, 0, 5), arg_types="hhiiiBBi")
    RunEvent(11205300, slot=6, args=(8, 0, 3536, 3536, Characters.c3531_0006, 97, 0, 6), arg_types="hhiiiBBi")
    RunEvent(11205250, slot=0, args=(Characters.c2330_0003, Boxes.EntTrigger1))
    RunEvent(11205290, slot=0, args=(Characters.c2330_0004, 51200170, 0.0, 1), arg_types="iifi")
    RunEvent(11205290, slot=1, args=(Characters.c2330_0005, 51200170, 0.20000000298023224, 1), arg_types="iifi")
    RunEvent(11205290, slot=2, args=(Characters.c2330_0006, 51200170, 0.800000011920929, 1), arg_types="iifi")
    RunEvent(11205250, slot=1, args=(Characters.c2330_0007, Boxes.EntTrigger2))
    RunEvent(11205290, slot=3, args=(Characters.c2330_0008, 11205263, 0.0, 0), arg_types="iifi")
    RunEvent(11205290, slot=4, args=(Characters.c2330_0009, 11205263, 0.6000000238418579, 0), arg_types="iifi")
    RunEvent(11205290, slot=5, args=(Characters.c2330_0010, 11205264, 0.0, 0), arg_types="iifi")
    RunEvent(11205290, slot=6, args=(Characters.c2330_0011, 11205264, 0.8999999761581421, 0), arg_types="iifi")
    RunEvent(11205200, slot=0, args=(Characters.c2330_0019, 8.0), arg_types="if")
    RunEvent(11205200, slot=1, args=(Characters.c2330_0021, 8.0), arg_types="if")
    RunEvent(11205200, slot=2, args=(Characters.c2330_0023, 5.0), arg_types="if")
    RunEvent(11205200, slot=3, args=(Characters.c2330_0024, 5.0), arg_types="if")
    RunEvent(11205200, slot=4, args=(Characters.c2330_0025, 5.0), arg_types="if")
    RunEvent(11205230, slot=0, args=(Characters.c3370_0000, 3.0), arg_types="if")
    RunEvent(11205230, slot=2, args=(Characters.c3370_0002, 3.0), arg_types="if")
    RunEvent(11205240, slot=0, args=(Characters.c3370_0000, Boxes.TreeLizardNestAfterAmbush1))
    RunEvent(11205240, slot=2, args=(Characters.c3370_0002, Boxes.TreeLizardNestAfterAmbush3))
    RunEvent(11205280, slot=0, args=(Characters.c2380_0000, 6.0, Boxes.StoneKnightTrigger), arg_types="ifi")
    RunEvent(11205280, slot=1, args=(Characters.c2380_0001, 2.0, Boxes.StoneKnightTrigger), arg_types="ifi")
    RunEvent(11205260, slot=0, args=(Characters.c2380_0002, 6.0), arg_types="if")
    RunEvent(11205260, slot=1, args=(Characters.c2380_0003, 10.0), arg_types="if")
    RunEvent(11205260, slot=2, args=(Characters.c2380_0004, 8.0), arg_types="if")
    RunEvent(11205260, slot=3, args=(Characters.c2380_0005, 4.0), arg_types="if")
    RunEvent(11205260, slot=4, args=(Characters.c2380_0006, 4.0), arg_types="if")
    RunEvent(11205190, slot=0, args=(Characters.c3410_0001, Boxes.FrogRayTrigger, 0.0), arg_types="iif")
    RunEvent(11205190, slot=1, args=(Characters.c3410_0002, Boxes.FrogRayTrigger, 0.5), arg_types="iif")
    RunEvent(11205190, slot=2, args=(Characters.c3410_0003, Boxes.FrogRayTrigger, 1.2000000476837158), arg_types="iif")
    RunEvent(11205190, slot=3, args=(Characters.c3410_0004, Boxes.FrogRayTrigger, 0.699999988079071), arg_types="iif")
    RunEvent(11205150, slot=0, args=(Characters.c2280_0000,))
    RunEvent(11205150, slot=1, args=(Characters.c2280_0001,))
    RunEvent(11205150, slot=2, args=(Characters.c2280_0002,))
    RunEvent(11205150, slot=3, args=(Characters.c2280_0003,))
    RunEvent(11205150, slot=4, args=(Characters.c2280_0004,))
    RunEvent(11205150, slot=5, args=(Characters.c2280_0005,))
    RunEvent(11205150, slot=6, args=(Characters.c2280_0006,))
    RunEvent(11205150, slot=7, args=(Characters.c2280_0007,))
    RunEvent(11205180, slot=0, args=(Characters.c5360_0000, 1))
    RunEvent(11205180, slot=1, args=(Characters.c5360_0001, 0))
    RunEvent(11205180, slot=2, args=(Characters.c5360_0002, 0))
    RunEvent(11200810, slot=0, args=(Characters.c3350_0000, 0, 0))
    RunEvent(11200810, slot=1, args=(Characters.c3350_0001, 0, 0))
    RunEvent(11200810, slot=2, args=(Characters.c3300_0000, 0, 33004000))
    RunEvent(11200810, slot=3, args=(Characters.c5360_0000, 0, 0))
    RunEvent(11200810, slot=4, args=(Characters.c5360_0001, 0, 0))
    RunEvent(11200810, slot=5, args=(Characters.c5360_0002, 0, 0))
    RunEvent(11200810, slot=6, args=(Characters.c2795_0000, 0, 27901000))
    RunEvent(11200810, slot=7, args=(Characters.c0000_0004, 0, 0))
    RunEvent(11200810, slot=8, args=(Characters.c0000_0007, 1, 0))
    RunEvent(11200810, slot=9, args=(Characters.c0000_0009, 0, 0))
    RunEvent(
        11205843,
        slot=0,
        args=(
            11200900,
            Objects.o2904_0000,
            Boxes.MoonlightButterflyFogPrompt,
            Boxes.MoonlightButterflyFogRotationTarget,
        ),
    )
    RunEvent(11205846, slot=0, args=(11200900, Objects.o2904_0000, VFX.ButterflyEntranceFog))
    RunEvent(11205843, slot=1, args=(5, Objects.o2900_0000, Boxes.SifFogPrompt, Boxes.SifFogRotationTarget))
    RunEvent(11205846, slot=1, args=(5, Objects.o2900_0000, VFX.SifEntranceFog))
    # <!--!>


def Preconstructor():
    """ 50: Event 50 """
    HumanityRegistration(Characters.c0000_0014, 8932)
    RunEvent(11205030)
    RunEvent(11205035)
    RunEvent(11205032)
    RunEvent(11200300)
    RunEvent(11205990, slot=0, args=(11205031, Characters.c0000_0014))
    SkipLinesIfClient(2)
    DisableFlagRange((11200210, 11200213))
    DisableFlag(11200215)
    HumanityRegistration(Characters.c0000_0012, 8350)
    HumanityRegistration(Characters.c0000_0015, 8350)
    SkipLinesIfClient(6)
    SkipLinesIfFlagOff(2, 1123)
    DisableFlagRange((1120, 1139))
    EnableFlag(1122)
    SkipLinesIfFlagOff(2, 1130)
    DisableFlagRange((1120, 1139))
    EnableFlag(1129)
    SkipLinesIfFlagOn(1, 1121)
    DisableCharacter(Characters.c0000_0012)
    SkipLinesIfFlagOn(1, 1123)
    DisableCharacter(Characters.c0000_0015)
    SkipLinesIfFlagOn(1, 1130)
    DisableCharacter(Characters.c0000_0015)
    SetStandbyAnimationSettings(Characters.c0000_0015, standby_animation=7875)
    RunEvent(11200520, slot=0, args=(Characters.c0000_0012, 1120, 1139, 1125))
    RunEvent(11200520, slot=1, args=(Characters.c0000_0015, 1120, 1139, 1125))
    RunEvent(11200530, slot=0, args=(Characters.c0000_0012, 1120, 1139, 1121))
    RunEvent(11200531, slot=0, args=(Characters.c0000_0012, 1120, 1139, 1122))
    RunEvent(11200534, slot=0, args=(Characters.c0000_0012, 1120, 1139, 1123))
    RunEvent(11200532, slot=0, args=(Characters.c0000_0012, 1120, 1139, 1126))
    RunEvent(11200533)
    RunEvent(11205040, slot=0, args=(11200210, Spheres.DuskSummonSpawn00, VFX.DuskSummonSign00))
    RunEvent(11205040, slot=1, args=(11200211, Spheres.DuskSummonSpawn01, VFX.DuskSummonSign01))
    RunEvent(11205040, slot=2, args=(11200212, Spheres.DuskSummonSpawn02, VFX.DuskSummonSign02))
    RunEvent(11205040, slot=3, args=(11200213, Spheres.DuskSummonSpawn03, VFX.DuskSummonSign03))
    RunEvent(11200529, slot=0, args=(1120, 1139, 1127))
    RunEvent(11200527, slot=0, args=(Characters.c0000_0012, 1120, 1139, 1129))
    RunEvent(11200525, slot=0, args=(Characters.c0000_0012, 1120, 1139, 1130))
    RunEvent(11205070, slot=0, args=(11200210, Spheres.DuskSummonSpawn00, VFX.DuskSummonSign00))
    RunEvent(11205070, slot=1, args=(11200211, Spheres.DuskSummonSpawn01, VFX.DuskSummonSign01))
    RunEvent(11205070, slot=2, args=(11200212, Spheres.DuskSummonSpawn02, VFX.DuskSummonSign02))
    RunEvent(11205070, slot=3, args=(11200213, Spheres.DuskSummonSpawn03, VFX.DuskSummonSign03))
    DeleteVFX(VFX.OolacilePortal, erase_root_only=False)
    RunEvent(11200005)
    RunEvent(11200006)
    SkipLinesIfClient(1)
    DisableFlagRange((11205050, 11205068))
    DisableCharacterCollision(Characters.c5361_0000)
    DisableGravity(Characters.c5361_0000)
    EnableImmortality(Characters.c5361_0000)
    SkipLinesIfFlagOn(2, 1710)
    SkipLinesIfFlagOn(1, 1712)
    DisableCharacter(Characters.c5361_0000)
    RunEvent(11200538, slot=0, args=(Characters.c5361_0000, 1710, 1712, 1711))
    RunEvent(11200539, slot=0, args=(Characters.c5361_0000, 1710, 1712, 1712))
    RunEvent(11200540, slot=0, args=(Characters.c5361_0000, 1710, 1712, 1711))
    RunEvent(11205058)
    RunEvent(11205054)
    RunEvent(11205056)
    RunEvent(11205057)
    RunEvent(11205060, slot=0, args=(Characters.c0000_0002,))
    RunEvent(11205060, slot=1, args=(Characters.c0000_0013,))
    RunEvent(11205060, slot=2, args=(Characters.c0000_0003,))
    RunEvent(11205060, slot=3, args=(Characters.c0000_0004,))
    RunEvent(11205060, slot=4, args=(Characters.c0000_0005,))
    RunEvent(11205060, slot=5, args=(Characters.c0000_0006,))
    RunEvent(11205060, slot=6, args=(Characters.c0000_0007,))
    RunEvent(11205060, slot=7, args=(Characters.c0000_0008,))
    RunEvent(11205060, slot=8, args=(Characters.c0000_0009,))
    HumanityRegistration(Characters.c0000_0002, 8470)
    HumanityRegistration(Characters.c0000_0013, 8900)
    DisableCharacter(Characters.c0000_0002)
    DisableCharacter(Characters.c0000_0013)
    RunEvent(11200520, slot=2, args=(Characters.c0000_0002, 1600, 1619, 1604))
    RunEvent(11200520, slot=3, args=(Characters.c0000_0013, 1760, 1769, 1764))
    RunEvent(11200501, slot=0, args=(Characters.c0000_0002, 1603))
    RunEvent(11200535, slot=0, args=(Characters.c0000_0002,))


def Event11200090(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11200090: Event 11200090 """
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


@RestartOnRest
def Event11200000():
    """ 11200000: Event 11200000 """
    EndIfThisEventOn()
    EndIfFlagOn(11200002)
    DisableCharacter(Characters.c5210_0000)
    DisableObject(Objects.o2900_0000)
    DeleteVFX(VFX.SifEntranceFog, erase_root_only=False)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterHollow(-1, PLAYER)
    IfConditionTrue(1, input_condition=-1)
    IfFlagOff(1, 11210021)
    IfCharacterInsideRegion(1, PLAYER, region=Spheres.SifCutsceneTrigger)
    IfConditionTrue(0, input_condition=1)
    SkipLinesIfClient(1)
    NotifyBossBattleStart()
    ActivateMultiplayerBuffs(Characters.c5210_0000)
    EnableFlag(11205390)
    EnableFlag(11205391)
    EnableFlag(11205393)
    IfCharacterType(2, PLAYER, CharacterType.BlackPhantom)
    SkipLinesIfConditionFalse(1, 2)
    IfFlagOn(0, 703)
    SkipLinesIfMultiplayer(2)
    PlayCutscene(
        120000,
        skippable=True,
        fade_out=False,
        player_id=PLAYER,
        move_to_region=Boxes.PlayerPointAfterSifCutscene,
        move_to_map=DARKROOT_GARDEN,
    )
    SkipLines(4)
    SkipLinesIfClient(2)
    PlayCutscene(
        120000,
        skippable=False,
        fade_out=False,
        player_id=PLAYER,
        move_to_region=Boxes.PlayerPointAfterSifCutscene,
        move_to_map=DARKROOT_GARDEN,
    )
    SkipLines(1)
    PlayCutscene(120000, skippable=False, fade_out=False, player_id=PLAYER)
    WaitFrames(1)
    DisableObject(Objects.o2300)
    Move(
        Characters.c5210_0000,
        destination=Boxes.SifPointAfterSifCutscene,
        destination_type=CoordEntityType.Region,
        short_move=True,
    )
    EnableCharacter(Characters.c5210_0000)
    EnableObject(Objects.o2900_0000)
    CreateVFX(VFX.SifEntranceFog)
    EnableFlag(11200002)


def Event11200002():
    """ 11200002: Event 11200002 """
    EndIfThisEventOn()
    EndIfFlagOn(11200000)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterHollow(-1, PLAYER)
    IfConditionTrue(1, input_condition=-1)
    IfFlagOn(1, 11210021)
    IfCharacterInsideRegion(1, PLAYER, region=Spheres.SifCutsceneTrigger)
    IfConditionTrue(0, input_condition=1)
    SkipLinesIfClient(1)
    NotifyBossBattleStart()
    ActivateMultiplayerBuffs(Characters.c5210_0000)
    EnableFlag(11205390)
    EnableFlag(11205391)
    EnableFlag(11205393)
    IfCharacterType(2, PLAYER, CharacterType.BlackPhantom)
    SkipLinesIfConditionFalse(1, 2)
    IfFlagOn(0, 703)
    SkipLinesIfMultiplayer(2)
    PlayCutscene(
        120003,
        skippable=True,
        fade_out=False,
        player_id=PLAYER,
        move_to_region=Boxes.PlayerPointAfterSifCutsceneIfRescued,
        move_to_map=DARKROOT_GARDEN,
    )
    SkipLines(4)
    SkipLinesIfClient(2)
    PlayCutscene(
        120003,
        skippable=False,
        fade_out=False,
        player_id=PLAYER,
        move_to_region=Boxes.PlayerPointAfterSifCutsceneIfRescued,
        move_to_map=DARKROOT_GARDEN,
    )
    SkipLines(1)
    PlayCutscene(120003, skippable=False, fade_out=False, player_id=PLAYER)
    WaitFrames(1)
    DisableObject(Objects.o2300)
    EnableCharacter(Characters.c5210_0000)
    EnableObject(Objects.o2900_0000)
    CreateVFX(VFX.SifEntranceFog)
    EnableFlag(11200000)


def Event11205390():
    """ 11205390: Event 11205390 """
    IfFlagOff(1, 5)
    IfFlagOn(1, 11200000)
    IfActionButton(
        1,
        prompt_text=10010403,
        anchor_entity=Boxes.SifFogPrompt,
        anchor_type=CoordEntityType.Region,
        line_intersects=Objects.o2900_0000,
        boss_version=True,
    )
    IfConditionTrue(0, input_condition=1)
    RotateToFaceEntity(PLAYER, Boxes.SifFogRotationTarget)
    ForceAnimation(PLAYER, 7410)
    Restart()


def Event11205391():
    """ 11205391: Event 11205391 """
    IfFlagOff(1, 5)
    IfFlagOn(1, 11205393)
    IfCharacterType(1, PLAYER, CharacterType.WhitePhantom)
    IfActionButton(
        1,
        prompt_text=10010403,
        anchor_entity=Boxes.SifFogPrompt,
        anchor_type=CoordEntityType.Region,
        trigger_attribute=TriggerAttribute.All,
        line_intersects=Objects.o2900_0000,
    )
    IfConditionTrue(0, input_condition=1)
    RotateToFaceEntity(PLAYER, Boxes.SifFogRotationTarget)
    ForceAnimation(PLAYER, 7410)
    Restart()


def Event11205393():
    """ 11205393: Event 11205393 """
    SkipLinesIfThisEventOn(8)
    IfFlagOn(1, 11200000)
    IfFlagOff(1, 5)
    IfCharacterInsideRegion(1, PLAYER, region=Boxes.SifCombatStart)
    IfThisEventOn(2)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(2)
    SkipLinesIfClient(1)
    NotifyBossBattleStart()
    ActivateMultiplayerBuffs(Characters.c5210_0000)


@RestartOnRest
def Event11205392():
    """ 11205392: Event 11205392 """
    SkipLinesIfFlagOff(3, 5)
    DisableCharacter(Characters.c5210_0000)
    Kill(Characters.c5210_0000, award_souls=False)
    End()
    DisableAI(Characters.c5210_0000)
    IfFlagOn(1, 11200000)
    IfFlagOn(1, 11205393)
    IfConditionTrue(0, input_condition=1)
    EnableAI(Characters.c5210_0000)
    EnableBossHealthBar(Characters.c5210_0000, name=5210, slot=0)


def Event11200001():
    """ 11200001: Event 11200001 """
    IfCharacterDead(0, Characters.c5210_0000)
    EnableFlag(5)
    KillBoss(1200800)
    DisableObject(Objects.o2900_0000)
    DeleteVFX(VFX.SifEntranceFog, erase_root_only=True)


def Event11205394():
    """ 11205394: Event 11205394 """
    DisableNetworkSync()
    IfFlagOff(1, 5)
    IfFlagOn(1, 11205392)
    SkipLinesIfHost(1)
    IfFlagOn(1, 11205391)
    IfCharacterInsideRegion(1, PLAYER, region=Boxes.SifMusic)
    IfConditionTrue(0, input_condition=1)
    EnableSoundEvent(1203800)


def Event11205395():
    """ 11205395: Event 11205395 """
    DisableNetworkSync()
    IfFlagOn(1, 5)
    IfFlagOn(1, 11205394)
    IfConditionTrue(0, input_condition=1)
    DisableSoundEvent(1203800)


@RestartOnRest
def Event11205396():
    """ 11205396: Event 11205396 """
    SkipLinesIfThisEventOn(1)
    IfHealthLessThanOrEqual(0, Characters.c5210_0000, 0.10000000149011612)
    AddSpecialEffect(Characters.c5210_0000, 5401)


def Event11205380():
    """ 11205380: Event 11205380 """
    IfFlagOff(1, 11200900)
    IfActionButton(
        1,
        prompt_text=10010403,
        anchor_entity=Boxes.MoonlightButterflyFogPrompt,
        anchor_type=CoordEntityType.Region,
        line_intersects=Objects.o2904_0000,
        boss_version=True,
    )
    IfConditionTrue(0, input_condition=1)
    RotateToFaceEntity(PLAYER, Boxes.MoonlightButterflyFogRotationTarget)
    ForceAnimation(PLAYER, 7410)
    Restart()


def Event11205381():
    """ 11205381: Event 11205381 """
    IfFlagOff(1, 11200900)
    IfFlagOn(1, 11205383)
    IfCharacterType(1, PLAYER, CharacterType.WhitePhantom)
    IfActionButton(
        1,
        prompt_text=10010403,
        anchor_entity=Boxes.MoonlightButterflyFogPrompt,
        anchor_type=CoordEntityType.Region,
        trigger_attribute=TriggerAttribute.All,
        line_intersects=Objects.o2904_0000,
    )
    IfConditionTrue(0, input_condition=1)
    RotateToFaceEntity(PLAYER, Boxes.MoonlightButterflyFogRotationTarget)
    ForceAnimation(PLAYER, 7410)
    Restart()


def Event11205383():
    """ 11205383: Event 11205383 """
    SkipLinesIfThisEventOn(3)
    IfFlagOff(1, 11200900)
    IfCharacterInsideRegion(1, PLAYER, region=Boxes.MoonlightButterflyCombatStart)
    IfConditionTrue(0, input_condition=1)
    SkipLinesIfClient(2)
    NotifyBossBattleStart()
    AddSpecialEffect(PLAYER, 5500)
    ActivateMultiplayerBuffs(Characters.c3230_0000)


@RestartOnRest
def Event11205382():
    """ 11205382: Event 11205382 """
    DisableCharacter(Characters.c2330_0026)
    SkipLinesIfClient(1)
    SetNetworkUpdateAuthority(Characters.c3230_0000, UpdateAuthority.Forced)
    SkipLinesIfFlagOff(3, 11200900)
    DisableCharacter(Characters.c3230_0000)
    Kill(Characters.c3230_0000, award_souls=False)
    End()
    DisableHealthBar(Characters.c3230_0000)
    DisableAI(Characters.c3230_0000)
    SetStandbyAnimationSettings(Characters.c3230_0000, standby_animation=7000)
    IfFlagOn(0, 11205383)
    SetStandbyAnimationSettings(Characters.c3230_0000, cancel_animation=7001)
    EnableAI(Characters.c3230_0000)
    EnableBossHealthBar(Characters.c3230_0000, name=3230, slot=0)


def Event11200900():
    """ 11200900: Event 11200900 """
    IfCharacterDead(0, Characters.c3230_0000)
    CancelSpecialEffect(PLAYER, 5500)
    EnableFlag(11200900)
    KillBoss(1200801)
    DisableObject(Objects.o2904_0000)
    DeleteVFX(VFX.ButterflyEntranceFog, erase_root_only=True)
    DisableObject(Objects.o2905_0000)
    DeleteVFX(VFX.ButterflyExitFog, erase_root_only=True)


def Event11205384():
    """ 11205384: Event 11205384 """
    DisableNetworkSync()
    IfFlagOff(1, 11200900)
    IfFlagOn(1, 11205382)
    SkipLinesIfHost(1)
    IfFlagOn(1, 11205381)
    IfCharacterInsideRegion(1, PLAYER, region=Boxes.MoonlightButterflyMusic)
    IfConditionTrue(0, input_condition=1)
    EnableSoundEvent(1203801)


def Event11205385():
    """ 11205385: Event 11205385 """
    DisableNetworkSync()
    IfFlagOn(1, 11200900)
    IfFlagOn(1, 11205384)
    IfConditionTrue(0, input_condition=1)
    DisableSoundEvent(1203801)


def Event11205120(_, arg_0_3: int, arg_4_7: int):
    """ 11205120: Event 11205120 """
    IfCharacterInsideRegion(1, Characters.c3230_0000, region=arg_0_3)
    IfHasTAEEvent(1, Characters.c3230_0000, tae_event_id=10)
    IfConditionTrue(0, input_condition=1)
    Move(Characters.c3230_0000, destination=arg_4_7, destination_type=CoordEntityType.Region, short_move=True)
    IfDoesNotHaveTAEEvent(0, Characters.c3230_0000, tae_event_id=10)
    Restart()


def Event11200100(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int, arg_20_23: int):
    """ 11200100: Event 11200100 """
    SkipLinesIfFlagOn(1, arg_20_23)
    SkipLinesIfThisEventSlotOff(2)
    EndOfAnimation(arg_4_7, 1)
    End()
    CreateObjectVFX(arg_8_11, obj=arg_4_7, model_point=200)
    SkipLinesIfEqual(1, left=arg_16_19, right=1)
    IfPlayerHasGood(1, 2002, including_box=False)
    IfActionButton(
        1,
        prompt_text=10010400,
        anchor_entity=arg_12_15,
        anchor_type=CoordEntityType.Region,
        line_intersects=arg_4_7,
        boss_version=True,
    )
    IfConditionTrue(0, input_condition=1)
    EnableFlag(arg_0_3)
    EnableFlag(arg_20_23)
    RotateToFaceEntity(PLAYER, arg_4_7)
    ForceAnimation(PLAYER, 7114, wait_for_completion=True)
    SkipLinesIfEqual(1, left=arg_16_19, right=1)
    SkipLinesIfClient(1)
    SkipLinesIfEqual(1, left=arg_16_19, right=1)
    DisplayDialog(
        10010861,
        anchor_entity=arg_4_7,
        display_distance=3.0,
        button_type=ButtonType.Yes_or_No,
        number_buttons=NumberButtons.NoButton,
    )
    ForceAnimation(arg_4_7, 1)
    DeleteObjectVFX(arg_4_7, erase_root=True)


def Event11200110(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11200110: Event 11200110 """
    DisableNetworkSync()
    IfFlagOn(-1, arg_0_3)
    SkipLinesIfEqual(1, left=arg_12_15, right=0)
    IfFlagOn(1, 703)
    SkipLinesIfEqual(1, left=arg_12_15, right=1)
    IfPlayerDoesNotHaveGood(1, 2002, including_box=False)
    IfActionButton(
        1,
        prompt_text=10010400,
        anchor_entity=arg_8_11,
        anchor_type=CoordEntityType.Region,
        trigger_attribute=TriggerAttribute.All,
        line_intersects=arg_4_7,
    )
    IfClient(2)
    IfActionButton(
        2,
        prompt_text=10010400,
        anchor_entity=arg_8_11,
        anchor_type=CoordEntityType.Region,
        trigger_attribute=TriggerAttribute.All,
        line_intersects=arg_4_7,
    )
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EndIfFlagOn(arg_0_3)
    DisplayDialog(
        10010160,
        anchor_entity=arg_4_7,
        display_distance=3.0,
        button_type=ButtonType.Yes_or_No,
        number_buttons=NumberButtons.NoButton,
    )
    Restart()


def Event11200120():
    """ 11200120: Event 11200120 """
    SkipLinesIfThisEventOff(2)
    DisableObject(Objects.o2120)
    End()
    IfObjectDestroyed(0, Objects.o2120)
    EnableFlag(11200120)


@RestartOnRest
def Event11205150(_, arg_0_3: int):
    """ 11205150: Event 11205150 """
    IfHealthLessThanOrEqual(1, arg_0_3, 0.800000011920929)
    IfCharacterBackreadEnabled(1, arg_0_3)
    IfConditionTrue(0, input_condition=1)
    AICommand(arg_0_3, command_id=1, slot=0)
    ReplanAI(arg_0_3)


@RestartOnRest
def Event11205180(_, arg_0_3: int, arg_4_7: int):
    """ 11205180: Event 11205180 """
    SkipLinesIfEqual(3, left=arg_4_7, right=0)
    IfHasAIStatus(0, arg_0_3, ai_status=AIStatusType.Battle)
    SetNest(arg_0_3, Boxes.GreatFelineNest)
    End()
    SkipLinesIfThisEventSlotOn(6)
    SetStandbyAnimationSettings(arg_0_3, standby_animation=9000)
    DisableAI(arg_0_3)
    IfHealthLessThanOrEqual(0, Characters.c5360_0000, 0.4000000059604645)
    WaitRandomSeconds(min_seconds=0.0, max_seconds=1.0)
    SetStandbyAnimationSettings(arg_0_3, cancel_animation=9060)
    EnableAI(arg_0_3)
    SetNest(arg_0_3, Boxes.GreatFelineNest)


@RestartOnRest
def Event11205190(_, arg_0_3: int, arg_4_7: int, arg_8_11: float):
    """ 11205190: Event 11205190 """
    EndIfThisEventSlotOn()
    DisableGravity(arg_0_3)
    DisableCharacter(arg_0_3)
    DisableAI(arg_0_3)
    IfCharacterInsideRegion(0, PLAYER, region=arg_4_7)
    Wait(arg_8_11)
    EnableGravity(arg_0_3)
    EnableCharacter(arg_0_3)
    ForceAnimation(arg_0_3, 7000, wait_for_completion=True)
    EnableAI(arg_0_3)


@RestartOnRest
def Event11205200(_, arg_0_3: int, arg_4_7: float):
    """ 11205200: Event 11205200 """
    SkipLinesIfThisEventSlotOff(2)
    ResetStandbyAnimationSettings(arg_0_3)
    End()
    DisableAI(arg_0_3)
    IfEntityWithinDistance(-1, arg_0_3, PLAYER, radius=arg_4_7)
    IfAttacked(-1, arg_0_3, attacker=PLAYER)
    IfAttacked(-1, arg_0_3, attacker=Characters.c0000_0014)
    IfConditionTrue(0, input_condition=-1)
    EnableAI(arg_0_3)
    SetStandbyAnimationSettings(arg_0_3, cancel_animation=9060)


@RestartOnRest
def Event11205250(_, arg_0_3: int, arg_4_7: int):
    """ 11205250: Event 11205250 """
    SkipLinesIfThisEventSlotOff(2)
    ResetStandbyAnimationSettings(arg_0_3)
    End()
    DisableAI(arg_0_3)
    IfAttacked(-1, arg_0_3, attacker=PLAYER)
    IfAttacked(-1, arg_0_3, attacker=Characters.c0000_0014)
    IfCharacterInsideRegion(-1, PLAYER, region=arg_4_7)
    IfCharacterInsideRegion(-1, Characters.c0000_0014, region=arg_4_7)
    IfConditionTrue(0, input_condition=-1)
    EnableAI(arg_0_3)
    SetStandbyAnimationSettings(arg_0_3, cancel_animation=9060)


@RestartOnRest
def Event11205290(_, arg_0_3: int, arg_4_7: int, arg_8_11: float, arg_12_15: int):
    """ 11205290: Event 11205290 """
    SkipLinesIfThisEventSlotOff(2)
    ResetStandbyAnimationSettings(arg_0_3)
    End()
    DisableAI(arg_0_3)
    IfAttacked(-1, arg_0_3, attacker=PLAYER)
    IfAttacked(-1, arg_0_3, attacker=Characters.c0000_0014)
    SkipLinesIfEqual(1, left=0, right=arg_12_15)
    SkipLinesIfClient(1)
    IfFlagOn(-1, arg_4_7)
    IfConditionTrue(0, input_condition=-1)
    Wait(arg_8_11)
    EnableAI(arg_0_3)
    SetStandbyAnimationSettings(arg_0_3, cancel_animation=9060)


@RestartOnRest
def Event11205230(_, arg_0_3: int, arg_4_7: float):
    """ 11205230: Event 11205230 """
    SkipLinesIfThisEventSlotOff(2)
    ResetStandbyAnimationSettings(arg_0_3)
    End()
    DisableCharacterCollision(arg_0_3)
    DisableGravity(arg_0_3)
    IfEntityWithinDistance(-1, arg_0_3, PLAYER, radius=arg_4_7)
    IfEntityWithinDistance(-1, arg_0_3, Characters.c0000_0014, radius=arg_4_7)
    IfAttacked(-2, arg_0_3, attacker=PLAYER)
    IfAttacked(-2, arg_0_3, attacker=Characters.c0000_0014)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(2, input_condition=-2)
    IfConditionTrue(-3, input_condition=1)
    IfConditionTrue(-3, input_condition=2)
    IfConditionTrue(0, input_condition=-3)
    EnableCharacterCollision(arg_0_3)
    EnableGravity(arg_0_3)
    EndIfFinishedConditionTrue(2)
    SetStandbyAnimationSettings(arg_0_3, cancel_animation=9063)


@RestartOnRest
def Event11205240(_, arg_0_3: int, arg_4_7: int):
    """ 11205240: Event 11205240 """
    IfCharacterHasSpecialEffect(0, arg_0_3, 5110)
    SetNest(arg_0_3, arg_4_7)


@RestartOnRest
def Event11205260(_, arg_0_3: int, arg_4_7: float):
    """ 11205260: Event 11205260 """
    SkipLinesIfThisEventSlotOff(2)
    ResetStandbyAnimationSettings(arg_0_3)
    End()
    IfEntityWithinDistance(-1, arg_0_3, PLAYER, radius=arg_4_7)
    IfEntityWithinDistance(-1, arg_0_3, Characters.c0000_0014, radius=arg_4_7)
    IfConditionTrue(0, input_condition=-1)
    SetStandbyAnimationSettings(arg_0_3, cancel_animation=9060)


@RestartOnRest
def Event11205280(_, arg_0_3: int, arg_4_7: float, arg_8_11: int):
    """ 11205280: Event 11205280 """
    SkipLinesIfThisEventSlotOff(2)
    ResetStandbyAnimationSettings(arg_0_3)
    End()
    IfEntityWithinDistance(-1, arg_0_3, PLAYER, radius=arg_4_7)
    IfEntityWithinDistance(-1, arg_0_3, Characters.c0000_0014, radius=arg_4_7)
    IfCharacterInsideRegion(-1, PLAYER, region=arg_8_11)
    IfCharacterInsideRegion(-1, Characters.c0000_0014, region=arg_8_11)
    IfConditionTrue(0, input_condition=-1)
    SetStandbyAnimationSettings(arg_0_3, cancel_animation=9060)


@RestartOnRest
def Event11205000():
    """ 11205000: Event 11205000 """
    DisableGravity(Characters.c3350_0000)
    DisableCharacterCollision(Characters.c3350_0000)
    SkipLinesIfThisEventOn(1)
    IfCharacterInsideRegion(0, PLAYER, region=Boxes.LivingTreeMovementTrigger)
    EnableGravity(Characters.c3350_0000)
    EnableCharacterCollision(Characters.c3350_0000)
    SetNest(Characters.c3350_0000, Boxes.LivingTreeMovementTarget)


@RestartOnRest
def Event11200800():
    """ 11200800: Event 11200800 """
    DisableCharacter(Characters.c2711_0000)
    EndIfThisEventOn()
    SkipLinesIfFlagOn(1, 11200801)
    IfFlagOn(0, 703)
    EnableCharacter(Characters.c2711_0000)
    IfCharacterBackreadEnabled(0, Characters.c2711_0000)
    SetDisplayMask(Characters.c2711_0000, bit_index=0, switch_type=OnOffChange.Off)
    IfCharacterDead(0, Characters.c2711_0000)
    EnableFlag(11200800)


@RestartOnRest
def Event11200801():
    """ 11200801: Event 11200801 """
    SkipLinesIfThisEventOff(2)
    DisableCharacter(Characters.c3530_0000)
    End()
    IfCharacterDead(-1, Characters.c3530_0000)
    IfCharacterDead(1, Characters.c3531_0000)
    IfCharacterDead(1, Characters.c3531_0001)
    IfCharacterDead(1, Characters.c3531_0002)
    IfCharacterDead(1, Characters.c3531_0003)
    IfCharacterDead(1, Characters.c3531_0004)
    IfCharacterDead(1, Characters.c3531_0005)
    IfCharacterDead(1, Characters.c3531_0006)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(0, input_condition=-1)
    Kill(Characters.c3530_0000, award_souls=True)
    IfCharacterHuman(-7, PLAYER)
    IfCharacterHollow(-7, PLAYER)
    EndIfConditionFalse(-7)
    AwardItemLot(35300100, host_only=True)


@RestartOnRest
def Event11205300(
    _,
    arg_0_1: short,
    arg_2_3: short,
    arg_4_7: int,
    arg_8_11: int,
    arg_12_15: int,
    arg_16_16: uchar,
    arg_17_17: uchar,
    arg_20_23: int,
):
    """ 11205300: Event 11205300 """
    DisableCharacter(arg_8_11)
    SkipLinesIfThisEventSlotOff(4)
    SetDisplayMask(Characters.c3530_0000, bit_index=arg_16_16, switch_type=OnOffChange.On)
    SetCollisionMask(Characters.c3530_0000, bit_index=arg_17_17, switch_type=OnOffChange.Off)
    AddSpecialEffect(Characters.c3530_0000, arg_20_23)
    End()
    IfCharacterBackreadEnabled(0, Characters.c3530_0000)
    CreateNPCPart(
        Characters.c3530_0000,
        npc_part_id=arg_2_3,
        part_index=arg_0_1,
        part_health=176,
        damage_correction=1.0,
        body_damage_correction=1.0,
        is_invincible=False,
        start_in_stop_state=False,
    )
    IfCharacterPartHealthLessThanOrEqual(1, Characters.c3530_0000, npc_part_id=arg_4_7, value=0)
    IfHealthLessThanOrEqual(2, Characters.c3530_0000, 0.0)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(2)
    ResetAnimation(Characters.c3530_0000, disable_interpolation=False)
    Move(
        arg_8_11,
        destination=Characters.c3530_0000,
        destination_type=CoordEntityType.Character,
        model_point=arg_12_15,
        copy_draw_parent=Characters.c3530_0000,
    )
    EnableCharacter(arg_8_11)
    ForceAnimation(arg_8_11, 8100)
    ForceAnimation(Characters.c3530_0000, 8000)
    SetDisplayMask(Characters.c3530_0000, bit_index=arg_16_16, switch_type=OnOffChange.On)
    SetCollisionMask(Characters.c3530_0000, bit_index=arg_17_17, switch_type=OnOffChange.Off)
    AddSpecialEffect(Characters.c3530_0000, arg_20_23)


def Event11200200():
    """ 11200200: Event 11200200 """
    DisableNetworkSync()
    EndIfClient()
    IfHost(1)
    IfPlayerCovenant(2, Covenant.ForestHunter)
    IfConditionFalse(1, input_condition=2)
    IfStandingOnCollision(-1, 1203500)
    IfStandingOnCollision(-1, 1203501)
    IfStandingOnCollision(-1, 1203502)
    IfStandingOnCollision(-1, 1203503)
    IfStandingOnCollision(-1, 1203504)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    AddSpecialEffect(PLAYER, 4500)
    WaitFrames(10)
    Restart()


@RestartOnRest
def Event11200810(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 11200810: Event 11200810 """
    SkipLinesIfThisEventSlotOff(6)
    SkipLinesIfEqual(3, left=arg_4_7, right=1)
    DisableCharacter(arg_0_3)
    Kill(arg_0_3, award_souls=False)
    End()
    DropMandatoryTreasure(arg_0_3)
    End()
    IfCharacterDead(0, arg_0_3)
    EndIfEqual(left=arg_8_11, right=0)
    IfCharacterHuman(-7, PLAYER)
    IfCharacterHollow(-7, PLAYER)
    EndIfConditionFalse(-7)
    AwardItemLot(arg_8_11, host_only=True)


def Event11200600(_, arg_0_3: int, arg_4_7: int):
    """ 11200600: Event 11200600 """
    SkipLinesIfThisEventSlotOff(4)
    EndOfAnimation(arg_0_3, 0)
    DisableObjectActivation(arg_0_3, obj_act_id=-1)
    EnableTreasure(arg_0_3)
    End()
    DisableTreasure(arg_0_3)
    IfObjectActivated(0, obj_act_id=arg_4_7)
    WaitFrames(10)
    EnableTreasure(arg_0_3)


def Event11200690():
    """ 11200690: Event 11200690 """
    SkipLinesIfThisEventOn(6)
    DisableTreasure(Objects.o0504_0000)
    DisableObject(Objects.o0504_0000)
    IfFlagOn(-1, 1123)
    IfFlagOn(-1, 1130)
    IfConditionTrue(0, input_condition=-1)
    EnableObject(Objects.o0504_0000)
    EnableTreasure(Objects.o0504_0000)


def Event11200510(_, arg_0_3: int, arg_4_7: int):
    """ 11200510: Event 11200510 """
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


def Event11200520(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11200520: Event 11200520 """
    SkipLinesIfThisEventSlotOff(2)
    DropMandatoryTreasure(arg_0_3)
    End()
    IfHealthLessThanOrEqual(0, arg_0_3, 0.0)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)


def Event11200501(_, arg_0_3: int, arg_4_7: int):
    """ 11200501: Event 11200501 """
    IfFlagOff(1, 1603)
    IfFlagOn(1, 1600)
    IfHealthLessThanOrEqual(1, arg_0_3, 0.8999999761581421)
    IfHealthGreaterThan(1, arg_0_3, 0.0)
    IfAttacked(1, arg_0_3, attacker=PLAYER)
    IfThisEventOff(1)
    IfFlagOff(2, 1763)
    IfFlagOn(2, 1760)
    IfHealthLessThanOrEqual(2, Characters.c0000_0013, 0.8999999761581421)
    IfHealthGreaterThan(2, Characters.c0000_0013, 0.0)
    IfAttacked(2, Characters.c0000_0013, attacker=PLAYER)
    IfThisEventOff(2)
    IfFlagOn(3, 746)
    IfThisEventOff(3)
    IfFlagOn(-2, arg_4_7)
    IfFlagOn(-2, 1763)
    IfConditionTrue(4, input_condition=-2)
    IfThisEventOn(4)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(-1, input_condition=4)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionTrue(4, 4)
    SkipLinesIfFlagOn(1, 1604)
    EnableFlag(arg_4_7)
    SkipLinesIfFlagOn(1, 1764)
    EnableFlag(1763)
    SkipLinesIfFlagOn(1, 1604)
    EnableCharacter(arg_0_3)
    SkipLinesIfFlagOn(1, 1764)
    EnableCharacter(Characters.c0000_0013)
    SetTeamType(arg_0_3, TeamType.Enemy)
    SetTeamType(Characters.c0000_0013, TeamType.Enemy)
    SaveRequest()
    EnableFlag(1766)


def Event11200530(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11200530: Event 11200530 """
    IfFlagOn(1, 1120)
    IfFlagOn(1, 11200800)
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
    Wait(0.5)
    SetStandbyAnimationSettings(arg_0_3, standby_animation=7875)
    ForceAnimation(arg_0_3, 7876)


def Event11200531(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11200531: Event 11200531 """
    IfFlagOn(1, 1121)
    IfFlagOn(1, 11200590)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)
    ForceAnimation(arg_0_3, 7877, wait_for_completion=True)
    ForceAnimation(arg_0_3, 8289, wait_for_completion=True)
    DisableCharacter(arg_0_3)


def Event11200532(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11200532: Event 11200532 """
    IfFlagOn(1, 1121)
    IfFlagOn(1, 11200591)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)
    ForceAnimation(arg_0_3, 7877, wait_for_completion=True)
    ForceAnimation(arg_0_3, 8289, wait_for_completion=True)
    DisableCharacter(arg_0_3)


def Event11200533():
    """ 11200533: Event 11200533 """
    DeleteVFX(VFX.DuskSummonSign00, erase_root_only=False)
    DeleteVFX(VFX.DuskSummonSign01, erase_root_only=False)
    DeleteVFX(VFX.DuskSummonSign02, erase_root_only=False)
    DeleteVFX(VFX.DuskSummonSign03, erase_root_only=False)
    EndIfClient()
    IfPlayerDoesNotHaveGood(1, 2520, including_box=False)
    IfFlagOn(1, 1122)
    IfFlagOn(2, 1129)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EnableRandomFlagInRange((11200210, 11200213))
    SkipLinesIfFlagOff(1, 11200210)
    CreateVFX(VFX.DuskSummonSign00)
    SkipLinesIfFlagOff(1, 11200211)
    CreateVFX(VFX.DuskSummonSign01)
    SkipLinesIfFlagOff(1, 11200212)
    CreateVFX(VFX.DuskSummonSign02)
    SkipLinesIfFlagOff(1, 11200213)
    CreateVFX(VFX.DuskSummonSign03)


def Event11205040(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 11205040: Event 11205040 """
    SkipLinesIfFlagOff(2, 11200215)
    EnableCharacter(Characters.c0000_0015)
    End()
    IfFlagOn(1, 1122)
    IfFlagOn(1, arg_0_3)
    IfActionButton(1, prompt_text=50000000, anchor_entity=arg_4_7, anchor_type=CoordEntityType.Region, model_point=0)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(11200215)
    DeleteVFX(arg_8_11, erase_root_only=True)
    Move(
        Characters.c0000_0015,
        destination=arg_4_7,
        destination_type=CoordEntityType.Region,
        set_draw_parent=Collisions.h0018B0,
    )
    Wait(5.0)
    EnableCharacter(Characters.c0000_0015)
    CreateTemporaryVFX(120, anchor_entity=arg_4_7, anchor_type=CoordEntityType.Region)
    SetStandbyAnimationSettings(Characters.c0000_0015, standby_animation=7875)
    ForceAnimation(Characters.c0000_0015, 6951, wait_for_completion=True)
    ForceAnimation(Characters.c0000_0015, 7876)
    EnableFlag(11205310)


def Event11200534(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11200534: Event 11200534 """
    IfFlagOn(1, 1122)
    IfFlagOn(1, 11205310)
    IfCharacterAlive(1, arg_0_3)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)


def Event11200529(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 11200529: Event 11200529 """
    EndIfFlagOn(17)
    IfFlagOn(-1, 1122)
    IfFlagOn(-1, 1125)
    IfFlagOn(-1, 1126)
    IfConditionTrue(1, input_condition=-1)
    IfPlayerHasGood(1, 2520, including_box=False)
    IfConditionTrue(0, input_condition=1)
    SkipLinesIfFlagOn(2, 1125)
    SkipLinesIfFlagOn(1, 1126)
    DisableFlagRange((arg_0_3, arg_4_7))
    EnableFlag(arg_8_11)


def Event11200527(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11200527: Event 11200527 """
    IfFlagOn(0, 1128)
    SkipLinesIfFlagOn(5, 1125)
    SkipLinesIfFlagOn(8, 1126)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)
    DisableCharacter(arg_0_3)
    End()
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(1125)
    DisableCharacter(arg_0_3)
    End()
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(1126)
    DisableCharacter(arg_0_3)


def Event11205070(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 11205070: Event 11205070 """
    SkipLinesIfFlagOff(2, 11200215)
    EnableCharacter(Characters.c0000_0015)
    End()
    IfFlagOn(1, 1129)
    IfFlagOn(1, arg_0_3)
    IfActionButton(1, prompt_text=50000000, anchor_entity=arg_4_7, anchor_type=CoordEntityType.Region, model_point=0)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(11200215)
    DeleteVFX(arg_8_11, erase_root_only=True)
    Move(
        Characters.c0000_0015,
        destination=arg_4_7,
        destination_type=CoordEntityType.Region,
        set_draw_parent=Collisions.h0018B0,
    )
    Wait(5.0)
    EnableCharacter(Characters.c0000_0015)
    CreateTemporaryVFX(120, anchor_entity=arg_4_7, anchor_type=CoordEntityType.Region)
    SetStandbyAnimationSettings(Characters.c0000_0015, standby_animation=7875)
    ForceAnimation(Characters.c0000_0015, 6951, wait_for_completion=True)
    ForceAnimation(Characters.c0000_0015, 7876)
    EnableFlag(11205311)


def Event11200525(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11200525: Event 11200525 """
    IfFlagOn(1, 1129)
    IfFlagOn(1, 11205311)
    IfCharacterAlive(1, arg_0_3)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)


def Event11200535(_, arg_0_3: int):
    """ 11200535: Event 11200535 """
    SkipLinesIfClient(1)
    DisableFlag(11205021)
    SkipLinesIfHost(1)
    SkipLinesIfFlagOn(5, 11205021)
    IfFlagOff(1, 1603)
    IfFlagOff(1, 1601)
    IfHost(1)
    IfPlayerCovenant(1, Covenant.ForestHunter)
    IfConditionTrue(0, input_condition=1)
    SkipLinesIfFlagOn(1, 1604)
    EnableCharacter(arg_0_3)
    SkipLinesIfFlagOn(2, 1764)
    EnableCharacter(Characters.c0000_0013)
    EnableFlag(1766)
    EnableFlag(11205021)


def Event11200538(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11200538: Event 11200538 """
    IfAttacked(0, arg_0_3, attacker=PLAYER)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)
    ForceAnimation(arg_0_3, 9030, wait_for_completion=True)
    DisableCharacter(arg_0_3)


def Event11200539(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11200539: Event 11200539 """
    IfFlagOn(1, 1710)
    IfFlagOn(1, 746)
    IfCharacterAlive(1, arg_0_3)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)


def Event11200540(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11200540: Event 11200540 """
    IfFlagOn(1, 1712)
    IfFlagOn(1, 11200596)
    IfCharacterAlive(1, arg_0_3)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)
    ForceAnimation(arg_0_3, 7003, wait_for_completion=True)
    DisableCharacter(arg_0_3)


def Event11205054():
    """ 11205054: Event 11205054 """
    IfPlayerCovenant(7, Covenant.ForestHunter)
    IfCharacterHuman(-7, PLAYER)
    IfCharacterHollow(-7, PLAYER)
    IfFlagOff(1, 11205055)
    IfFlagOn(1, 11205053)
    IfConditionTrue(1, input_condition=-7)
    IfConditionFalse(1, input_condition=7)
    IfFlagOff(1, 11205050)
    IfFlagOff(2, 11205055)
    IfFlagOn(2, 11205053)
    IfConditionTrue(2, input_condition=-7)
    IfConditionTrue(2, input_condition=7)
    IfAttacked(-6, Characters.c5361_0000, attacker=PLAYER)
    IfFlagOn(-6, 11205060)
    IfFlagOn(-6, 11205061)
    IfFlagOn(-6, 11205062)
    IfFlagOn(-6, 11205063)
    IfFlagOn(-6, 11205064)
    IfFlagOn(-6, 11205065)
    IfFlagOn(-6, 11205066)
    IfFlagOn(-6, 11205067)
    IfFlagOn(-6, 11205068)
    IfFlagOn(-6, 745)
    IfConditionTrue(2, input_condition=-6)
    IfFlagOff(3, 11205055)
    IfFlagOff(3, 11205053)
    IfConditionTrue(3, input_condition=-7)
    IfConditionFalse(3, input_condition=7)
    IfFlagOn(3, 11205050)
    IfFlagOff(4, 11205055)
    IfFlagOff(4, 11205053)
    IfConditionTrue(4, input_condition=-7)
    IfConditionTrue(4, input_condition=7)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(-1, input_condition=4)
    IfConditionTrue(0, input_condition=-1)
    EnableFlag(11205055)
    SkipLinesIfFinishedConditionFalse(1, 1)
    EnableFlag(11205051)
    SkipLinesIfFinishedConditionFalse(1, 2)
    EnableFlag(11205051)
    SkipLinesIfFinishedConditionFalse(1, 3)
    EnableFlag(11205052)
    SkipLinesIfFinishedConditionFalse(1, 4)
    EnableFlag(11205052)
    Restart()


@RestartOnRest
def Event11205056():
    """ 11205056: Event 11205056 """
    IfPlayerCovenant(7, Covenant.ForestHunter)
    IfCharacterHuman(-7, PLAYER)
    IfCharacterHollow(-7, PLAYER)
    IfFlagOn(1, 11205051)
    IfConditionTrue(1, input_condition=-7)
    IfConditionTrue(1, input_condition=7)
    IfFlagOn(2, 11205051)
    IfConditionTrue(2, input_condition=-7)
    IfConditionFalse(2, input_condition=7)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    DisableFlag(11205051)
    DisableFlag(11205053)
    SkipLinesIfFinishedConditionTrue(9, 2)
    IfCharacterHuman(-6, PLAYER)
    IfCharacterHollow(-6, PLAYER)
    SkipLinesIfConditionFalse(3, -6)
    BetrayCurrentCovenant()
    SkipLinesIfFlagOn(2, 9001)
    IncrementPvPSin()
    EnableFlag(9001)
    EnableFlag(742)
    EnableFlag(746)
    SetTeamType(Characters.c0000_0002, TeamType.Enemy)
    SetTeamType(Characters.c0000_0013, TeamType.Enemy)
    SetTeamType(Characters.c0000_0003, TeamType.Enemy)
    SetTeamType(Characters.c0000_0004, TeamType.Enemy)
    SetTeamType(Characters.c0000_0005, TeamType.Enemy)
    SetTeamType(Characters.c0000_0006, TeamType.Enemy)
    SetTeamType(Characters.c0000_0007, TeamType.Enemy)
    SetTeamType(Characters.c0000_0008, TeamType.Enemy)
    SetTeamType(Characters.c0000_0009, TeamType.Enemy)
    SaveRequest()
    DisableFlag(11205055)
    Restart()


@RestartOnRest
def Event11205057():
    """ 11205057: Event 11205057 """
    IfFlagOn(0, 11205052)
    DisableFlag(11205052)
    EnableFlag(11205053)
    SetTeamType(Characters.c0000_0002, TeamType.Ally)
    SetTeamType(Characters.c0000_0013, TeamType.Ally)
    SetTeamType(Characters.c0000_0003, TeamType.Ally)
    SetTeamType(Characters.c0000_0004, TeamType.Ally)
    SetTeamType(Characters.c0000_0005, TeamType.Ally)
    SetTeamType(Characters.c0000_0006, TeamType.Ally)
    SetTeamType(Characters.c0000_0007, TeamType.Ally)
    SetTeamType(Characters.c0000_0008, TeamType.Ally)
    SetTeamType(Characters.c0000_0009, TeamType.Ally)
    ClearTargetList(Characters.c0000_0002)
    ClearTargetList(Characters.c0000_0013)
    ClearTargetList(Characters.c0000_0003)
    ClearTargetList(Characters.c0000_0004)
    ClearTargetList(Characters.c0000_0005)
    ClearTargetList(Characters.c0000_0006)
    ClearTargetList(Characters.c0000_0007)
    ClearTargetList(Characters.c0000_0008)
    ClearTargetList(Characters.c0000_0009)
    ReplanAI(Characters.c0000_0002)
    ReplanAI(Characters.c0000_0013)
    ReplanAI(Characters.c0000_0003)
    ReplanAI(Characters.c0000_0004)
    ReplanAI(Characters.c0000_0005)
    ReplanAI(Characters.c0000_0006)
    ReplanAI(Characters.c0000_0007)
    ReplanAI(Characters.c0000_0008)
    ReplanAI(Characters.c0000_0009)
    SaveRequest()
    DisableFlag(11205055)
    Restart()


def Event11205058():
    """ 11205058: Event 11205058 """
    SkipLinesIfFlagOff(2, 11205053)
    EnableFlag(11205052)
    End()
    SetTeamType(Characters.c0000_0002, TeamType.Enemy)
    SetTeamType(Characters.c0000_0013, TeamType.Enemy)
    SetTeamType(Characters.c0000_0003, TeamType.Enemy)
    SetTeamType(Characters.c0000_0004, TeamType.Enemy)
    SetTeamType(Characters.c0000_0005, TeamType.Enemy)
    SetTeamType(Characters.c0000_0006, TeamType.Enemy)
    SetTeamType(Characters.c0000_0007, TeamType.Enemy)
    SetTeamType(Characters.c0000_0008, TeamType.Enemy)
    SetTeamType(Characters.c0000_0009, TeamType.Enemy)
    SaveRequest()


@RestartOnRest
def Event11205060(_, arg_0_3: int):
    """ 11205060: Event 11205060 """
    SkipLinesIfFlagOff(1, 746)
    SetTeamType(arg_0_3, TeamType.Enemy)
    IfCharacterHuman(-7, PLAYER)
    IfCharacterHollow(-7, PLAYER)
    IfConditionTrue(1, input_condition=-7)
    IfPlayerCovenant(1, Covenant.ForestHunter)
    IfAttacked(1, arg_0_3, attacker=PLAYER)
    IfHealthLessThanOrEqual(1, arg_0_3, 0.8999999761581421)
    IfConditionTrue(0, input_condition=1)
    End()


def Event11205030():
    """ 11205030: Event 11205030 """
    SkipLinesIfClient(1)
    SetNetworkUpdateAuthority(Characters.c0000_0014, UpdateAuthority.Forced)
    SkipLinesIfFlagOn(3, 11205033)
    IfClient(2)
    IfFlagOn(2, 11205031)
    SkipLinesIfConditionTrue(1, 2)
    DisableCharacter(Characters.c0000_0014)
    EndIfFlagOn(11200900)
    IfHost(1)
    IfCharacterHuman(1, PLAYER)
    IfCharacterBackreadEnabled(1, Characters.c0000_0014)
    IfEntityWithinDistance(1, Characters.c0000_0014, PLAYER, radius=10.0)
    IfConditionTrue(0, input_condition=1)
    PlaceSummonSign(
        SummonSignType.BlueEyeSign,
        Characters.c0000_0014,
        region=Points.WitchBeatriceSummonSign,
        summon_flag=11205031,
        dismissal_flag=11205033,
    )


def Event11205035():
    """ 11205035: Event 11205035 """
    SkipLinesIfClient(1)
    SetNetworkUpdateAuthority(Characters.c0000_0014, UpdateAuthority.Forced)
    SkipLinesIfFlagOn(3, 11205033)
    IfClient(2)
    IfFlagOn(2, 11205031)
    SkipLinesIfConditionTrue(1, 2)
    DisableCharacter(Characters.c0000_0014)
    EndIfFlagOn(11200900)
    IfMultiplayerCount(1, arg1=4, arg2=3)
    IfHost(1)
    IfFlagOff(1, 11205031)
    IfFlagOff(1, 11205033)
    IfCharacterHuman(1, PLAYER)
    IfCharacterBackreadEnabled(1, Characters.c0000_0014)
    IfEntityWithinDistance(1, Characters.c0000_0014, PLAYER, radius=10.0)
    IfCharacterHasSpecialEffect(1, PLAYER, 28)
    IfConditionTrue(0, input_condition=1)
    PlaceSummonSign(
        SummonSignType.BlueEyeSign,
        Characters.c0000_0014,
        region=Points.WitchBeatriceSummonSign,
        summon_flag=11205031,
        dismissal_flag=11205033,
    )


def Event11205990(_, arg_0_3: int, arg_4_7: int):
    """ 11205990: Event 11205990 """
    IfFlagOn(0, arg_0_3)
    EraseNPCSummonSign(summoned_character=arg_4_7)
    IfFlagOff(0, arg_0_3)
    Restart()


def Event11205032():
    """ 11205032: Event 11205032 """
    EndIfThisEventOn()
    IfFlagOn(1, 11205031)
    IfFlagOn(1, 11205383)
    IfConditionTrue(0, input_condition=1)
    AICommand(Characters.c0000_0014, command_id=10, slot=0)
    ReplanAI(Characters.c0000_0014)
    IfCharacterInsideRegion(0, Characters.c0000_0014, region=Boxes.MoonlightButterflyFogPrompt)
    RotateToFaceEntity(Characters.c0000_0014, Boxes.MoonlightButterflyFogRotationTarget)
    ForceAnimation(Characters.c0000_0014, 7410)
    AICommand(Characters.c0000_0014, command_id=-1, slot=0)
    ReplanAI(Characters.c0000_0014)


def Event11200300():
    """ 11200300: Event 11200300 """
    IfFlagOn(0, 11205031)
    EnableFlag(11200300)


def Event11200005():
    """ 11200005: Event 11200005 """
    IfFlagOn(-1, 1125)
    IfFlagOn(-1, 1126)
    IfFlagOn(-1, 1127)
    IfConditionTrue(1, input_condition=-1)
    IfPlayerHasGood(1, 2520, including_box=False)
    IfFlagOff(1, 17)
    IfConditionTrue(0, input_condition=1)
    EndIfClient()
    IfSingleplayer(0)
    CreateVFX(VFX.OolacilePortal)
    IfMultiplayer(0)
    DeleteVFX(VFX.OolacilePortal, erase_root_only=True)
    Restart()


def Event11200006():
    """ 11200006: Event 11200006 """
    IfFlagOn(-1, 1125)
    IfFlagOn(-1, 1126)
    IfFlagOn(-1, 1127)
    IfConditionTrue(1, input_condition=-1)
    IfPlayerHasGood(1, 2520, including_box=False)
    IfFlagOff(1, 17)
    IfSingleplayer(1)
    IfActionButton(
        1,
        prompt_text=10010100,
        anchor_entity=Boxes.OolacilePortalPrompt,
        anchor_type=CoordEntityType.Region,
    )
    IfConditionTrue(0, input_condition=1)
    EndIfClient()
    PlayCutscene(
        120002,
        skippable=True,
        fade_out=False,
        player_id=PLAYER,
        move_to_region=m12_01_Points.ArrivalFromDarkroot,
        move_to_map=OOLACILE,
    )
    WaitFrames(1)
    SaveRequest()
    Restart()


def Event11205843(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11205843: Event 11205843 """
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


def Event11205846(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 11205846: Event 11205846 """
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
