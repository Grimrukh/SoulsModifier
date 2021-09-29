"""
linked:


strings:

"""
from soulstruct.darksouls1r.events import *
from ..entities.m12_01_00_00_entities import *


def Constructor():
    """ 0: Event 0 """
    RunEvent(11210700)
    SkipLinesIfClient(10)
    DisableObject(Objects.o2912_0001)
    DeleteVFX(VFX.MultiplayerFog4, erase_root_only=False)
    DisableObject(Objects.o2913)
    DeleteVFX(VFX.MultiplayerFog1, erase_root_only=False)
    DisableObject(Objects.o2914)
    DeleteVFX(VFX.MultiplayerFog2, erase_root_only=False)
    DisableObject(Objects.o2917_0000)
    DeleteVFX(VFX.MultiplayerFog3, erase_root_only=False)
    DisableObject(Objects.o2920_0000)
    DeleteVFX(VFX.MultiplayerFog5, erase_root_only=False)
    DisableCollision(Collisions.h0095B1_0000)
    SkipLinesIfFlagOff(2, 11210539)
    EnableCollision(Collisions.h0095B1_0000)
    DisableCollision(Collisions.h0095B1)
    DisableSoundEvent(1213800)
    SkipLinesIfFlagOff(6, 11210000)
    RunEvent(11210000)
    DisableObject(Objects.o2909_0001)
    DeleteVFX(VFX.SanctuaryGuardianEntranceFog, erase_root_only=False)
    DisableObject(Objects.o2910_0001)
    DeleteVFX(VFX.SanctuaryGuardianExitFog, erase_root_only=False)
    SkipLines(8)
    RunEvent(11215000)
    RunEvent(11215001)
    RunEvent(11215002)
    RunEvent(11215003)
    RunEvent(11215004)
    RunEvent(11215005)
    RunEvent(11210000)
    RunEvent(11215006, slot=0, args=(Characters.c3472_0000, Characters.c3471_0000, 34720000))
    RunEvent(11215006, slot=1, args=(Characters.c3472_0001, Characters.c3471_0001, 34720010))
    RunEvent(11215006, slot=2, args=(Characters.c3472_0002, Characters.c3471_0002, 34720020))
    RunEvent(11215007)
    RunEvent(11215008)
    RunEvent(11215009)
    DisableSoundEvent(1213801)
    SkipLinesIfFlagOff(7, 11210001)
    RunEvent(11210001)
    DisableObject(Objects.o2915_0000)
    DeleteVFX(VFX.ArtoriasEntranceFog, erase_root_only=False)
    DisableObject(Objects.o2916_0000)
    DeleteVFX(VFX.ArtoriasExitFog, erase_root_only=False)
    DisableCollision(Collisions.h7400B1)
    SkipLines(7)
    RunEvent(11215010)
    RunEvent(11215011)
    RunEvent(11215012)
    RunEvent(11215013)
    RunEvent(11215014)
    RunEvent(11215015)
    RunEvent(11210001)
    DisableSoundEvent(1213802)
    SkipLinesIfFlagOff(4, 11210002)
    RunEvent(11210002)
    DisableObject(Objects.o2911_0001)
    DeleteVFX(VFX.ManusEntranceFog, erase_root_only=False)
    SkipLines(8)
    RunEvent(11215020)
    RunEvent(11215021)
    RunEvent(11215022)
    RunEvent(11215027)
    RunEvent(11215023)
    RunEvent(11215024)
    RunEvent(11215025)
    RunEvent(11210002)
    RunEvent(11215026)
    DisableSoundEvent(1213803)
    IfFlagOn(1, 11210592)
    IfFlagOff(1, 11210004)
    SkipLinesIfConditionTrue(3, 1)
    DisableObject(Objects.o2919_0000)
    DeleteVFX(VFX.KalameetEntranceFog, erase_root_only=False)
    DisableCollision(Collisions.h7400B1)
    SkipLinesIfFlagOn(8, 11210004)
    RunEvent(11215060)
    RunEvent(11215061)
    RunEvent(11215062)
    RunEvent(11215063)
    RunEvent(11215064)
    RunEvent(11215066)
    RunEvent(11215065)
    RunEvent(11210005)
    SkipLinesIfFlagOff(1, 11210002)
    RegisterBonfire(
        11210992,
        obj=Objects.o0200_0003,
        reaction_distance=2.0,
        reaction_angle=180.0,
        initial_kindle_level=0,
    )
    RegisterBonfire(
        11210984,
        obj=Objects.o0200_0000,
        reaction_distance=2.0,
        reaction_angle=180.0,
        initial_kindle_level=0,
    )
    RegisterBonfire(
        11210976,
        obj=Objects.o0200_0001,
        reaction_distance=2.0,
        reaction_angle=180.0,
        initial_kindle_level=0,
    )
    RegisterBonfire(
        11210968,
        obj=Objects.o0200_0002,
        reaction_distance=2.0,
        reaction_angle=180.0,
        initial_kindle_level=0,
    )
    RegisterBonfire(
        11210960,
        obj=Objects.o0200_0004,
        reaction_distance=2.0,
        reaction_angle=180.0,
        initial_kindle_level=0,
    )
    RegisterLadder(start_climbing_flag=11210210, stop_climbing_flag=11210211, obj=Objects.o2402)
    RegisterLadder(start_climbing_flag=11210212, stop_climbing_flag=11210213, obj=Objects.o2790_0000)
    RegisterLadder(start_climbing_flag=11210214, stop_climbing_flag=11210215, obj=Objects.o2791_0000)
    RunEvent(11215100)
    RunEvent(
        11215110,
        slot=0,
        args=(Characters.c4130_0022, Boxes.GardenerTrap2, 0.0, Boxes.GardenerTrap2),
        arg_types="iifi",
    )
    RunEvent(
        11215110,
        slot=1,
        args=(Characters.c4130_0023, Boxes.GardenerTrap2, 0.0, Boxes.GardenerTrap2),
        arg_types="iifi",
    )
    RunEvent(
        11215110,
        slot=2,
        args=(Characters.c4130_0020, Boxes.GardenerTrap2, 10.0, Boxes.GardenerTrap3),
        arg_types="iifi",
    )
    RunEvent(
        11215110,
        slot=3,
        args=(Characters.c4130_0017, Boxes.GardenerTrap2, 10.0, Boxes.GardenerTrap3),
        arg_types="iifi",
    )
    RunEvent(11215115, slot=0, args=(Characters.c4130_0022, Boxes.GardenerTrap2, Boxes.GardenerTrap1))
    RunEvent(11215115, slot=1, args=(Characters.c4130_0023, Boxes.GardenerTrap2, Boxes.GardenerTrap1))
    RunEvent(11215120, slot=0, args=(Characters.c4130_0019, Characters.c4130_0025, Characters.c4130_0027, 51210030))
    RunEvent(
        11215140,
        slot=0,
        args=(
            Characters.c4120_0004,
            Boxes.GardeningAnimation0,
            Boxes.GardeningAnimation3,
            Boxes.GardeningAnimation7,
            11215151,
            11215152,
            11215153,
        ),
    )
    RunEvent(
        11215140,
        slot=1,
        args=(
            Characters.c4120_0007,
            Boxes.GardeningAnimation0_1,
            Boxes.GardeningAnimation3_1,
            Boxes.GardeningAnimation7_1,
            11215154,
            11215155,
            11215156,
        ),
    )
    RunEvent(11210050)
    RunEvent(11210051)
    RunEvent(11210052)
    RunEvent(11210053)
    RunEvent(11210054)
    RunEvent(11210055)
    RunEvent(11210056)
    RunEvent(11210057)
    RunEvent(11210040)
    RunEvent(11210041)
    RunEvent(11210042)
    RunEvent(11210043)
    RunEvent(11210004)
    RunEvent(11215050)
    RunEvent(11215051)
    RunEvent(11215052)
    RunEvent(11210025)
    RunEvent(11210021)
    RunEvent(11215040)
    RunEvent(11215041)
    RunEvent(11210020)
    RunEvent(11215043)
    RunEvent(11215044)
    RunEvent(11210330, slot=0, args=(11210310, 11210315, 11210330))
    RunEvent(11210310, slot=0, args=(Characters.c4170_0001, 11210310))
    RunEvent(11210310, slot=1, args=(Characters.c4170_0002, 11210311))
    RunEvent(11210310, slot=2, args=(Characters.c4170_0003, 11210312))
    RunEvent(11210310, slot=3, args=(Characters.c4172_0018, 11210313))
    RunEvent(11210310, slot=4, args=(Characters.c4172_0010, 11210314))
    RunEvent(11210310, slot=5, args=(Characters.c4171_0005, 11210315))
    RunEvent(11210600, slot=0, args=(Objects.o0110_0000, 11210600))
    RunEvent(11210600, slot=1, args=(Objects.o0110_0001, 11210601))
    RunEvent(11210600, slot=2, args=(Objects.o0110_0002, 11210602))
    RunEvent(11210600, slot=4, args=(Objects.o0110_0004, 11210604))
    RunEvent(11210600, slot=5, args=(Objects.o0110_0005, 11210605))
    RunEvent(11210230, slot=0, args=(Objects.o2795_0000, Objects.o0500_0100, 125, 126))
    RunEvent(11210350, slot=0, args=(Characters.c3300_0000, 33007200))
    RunEvent(11210350, slot=1, args=(Characters.c3300_0001, 33007000))
    RunEvent(11210350, slot=2, args=(Characters.c3300_0002, 33007100))
    RunEvent(11210350, slot=3, args=(Characters.c3300_0003, 33007300))
    RunEvent(11210350, slot=4, args=(Characters.c3300_0004, 33007100))
    RunEvent(11210350, slot=5, args=(Characters.c4160_0002, 41601000))
    RunEvent(11210100)
    RunEvent(11210103)
    RunEvent(11210110)
    RunEvent(11210120)
    RunEvent(11210123)
    RunEvent(11210130)
    RunEvent(11210133)
    RunEvent(11210140)
    RunEvent(11210150)
    RunEvent(11219100, slot=0, args=(11218102, Objects.o2700_0000, 0, 1, Objects.o2701_0010), arg_types="iiiBi")
    RunEvent(11219100, slot=1, args=(11218103, Objects.o2700_0000, 10, 0, Objects.o2701_0000), arg_types="iiiBi")
    RunEvent(11210170, slot=0, args=(11215220, Collisions.h7600B1, Boxes.Elevator0_RideArea))
    RunEvent(11210170, slot=1, args=(11215221, Collisions.h7601B1, Boxes.Elevator1_RideArea))
    RunEvent(11210170, slot=2, args=(11215222, Collisions.h7602B1, Boxes.Elevator2_RideArea))
    RunEvent(11210170, slot=3, args=(11215223, Collisions.h7603B1, Boxes.Elevator3_RideArea))
    RunEvent(11210170, slot=4, args=(11215224, Collisions.h7604B1, Boxes.Elevator4_RideArea))
    DisableSoundEvent(1213810)
    DisableSoundEvent(1213811)
    RunEvent(11210200, slot=0, args=(Objects.o2730_0000, Boxes.LightIllusoryWallTrigger0))
    RunEvent(11210200, slot=1, args=(Objects.o2732_0000, Boxes.LightIllusoryWallTrigger1))
    RunEvent(11210205, slot=0, args=(Objects.o2730_0000, Boxes.LightIllusoryWallTrigger0, 11210200))
    RunEvent(11210205, slot=1, args=(Objects.o2732_0000, Boxes.LightIllusoryWallTrigger1, 11210201))
    RunEvent(11210300)
    RunEvent(11215250, slot=0, args=(Objects.o2610_0000, VFX.ManusRock_o2610_0))
    RunEvent(11215250, slot=1, args=(Objects.o2610_0001, VFX.ManusRock_o2610_1))
    RunEvent(11215250, slot=2, args=(Objects.o2610_0002, VFX.ManusRock_o2610_2))
    RunEvent(11215250, slot=3, args=(Objects.o2611_0000, VFX.ManusRock_o2611_0))
    RunEvent(11215250, slot=4, args=(Objects.o2611_0001, VFX.ManusRock_o2611_1))
    RunEvent(11215250, slot=5, args=(Objects.o2611_0002, VFX.ManusRock_o2611_2))
    RunEvent(11215250, slot=6, args=(Objects.o2611_0003, VFX.ManusRock_o2611_3))
    RunEvent(11215250, slot=7, args=(Objects.o2611_0004, VFX.ManusRock_o2611_4))
    RunEvent(11215250, slot=8, args=(Objects.o2611_0005, VFX.ManusRock_o2611_5))
    RunEvent(11215250, slot=9, args=(Objects.o2612_0000, VFX.ManusRock_o2612_0))
    RunEvent(11215250, slot=10, args=(Objects.o2612_0001, VFX.ManusRock_o2612_1))
    RunEvent(11215250, slot=11, args=(Objects.o2612_0002, VFX.ManusRock_o2612_2))
    RunEvent(11215250, slot=12, args=(Objects.o2612_0003, VFX.ManusRock_o2612_3))
    RunEvent(11215250, slot=13, args=(Objects.o2612_0004, VFX.ManusRock_o2612_4))
    RunEvent(11215250, slot=14, args=(Objects.o2612_0005, VFX.ManusRock_o2612_5))
    RunEvent(11215250, slot=15, args=(Objects.o2613_0000, VFX.ManusRock_o2613_0))
    RunEvent(11215250, slot=16, args=(Objects.o2613_0001, VFX.ManusRock_o2613_1))
    RunEvent(11215250, slot=17, args=(Objects.o2613_0002, VFX.ManusRock_o2613_2))
    RunEvent(11215250, slot=18, args=(Objects.o2613_0003, VFX.ManusRock_o2613_3))
    RunEvent(11215250, slot=19, args=(Objects.o2613_0004, VFX.ManusRock_o2613_4))
    RunEvent(11215250, slot=20, args=(Objects.o2613_0005, VFX.ManusRock_o2613_5))
    RunEvent(11215250, slot=21, args=(Objects.o2613_0006, VFX.ManusRock_o2613_6))
    RunEvent(11215250, slot=22, args=(Objects.o2613_0007, VFX.ManusRock_o2613_7))
    RunEvent(11215250, slot=23, args=(Objects.o2613_0008, VFX.ManusRock_o2613_8))
    RunEvent(11215160, slot=0, args=(Characters.c2780_0000,))
    RunEvent(11215165, slot=0, args=(Characters.c2780_0000,))
    RunEvent(11215170, slot=0, args=(Characters.c2780_0000,))
    RunEvent(11215175, slot=0, args=(Characters.c2780_0000,))
    RunEvent(11215180, slot=0, args=(Characters.c2780_0000, Boxes.MimicNest0))
    RunEvent(11210680, slot=0, args=(Characters.c2780_0000,))
    RunEvent(11215185, slot=0, args=(Characters.c2780_0000,))
    SetNetworkUpdateRate(Characters.c2780_0001, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    RunEvent(11215160, slot=1, args=(Characters.c2780_0001,))
    RunEvent(11215165, slot=1, args=(Characters.c2780_0001,))
    RunEvent(11215170, slot=1, args=(Characters.c2780_0001,))
    RunEvent(11215175, slot=1, args=(Characters.c2780_0001,))
    RunEvent(11215180, slot=1, args=(Characters.c2780_0001, Boxes.MimicNest1))
    RunEvent(11210680, slot=1, args=(Characters.c2780_0001,))
    RunEvent(11215185, slot=1, args=(Characters.c2780_0001,))
    RunEvent(11219113)
    RunEvent(11219114)
    RunEvent(4294967295)
    RunEvent(11213888)
    RunEvent(11215846, slot=0, args=(11210000, Objects.o2909_0001, VFX.SanctuaryGuardianEntranceFog))
    RunEvent(
        11215843,
        slot=0,
        args=(11210000, Objects.o2909_0001, Boxes.SanctuaryGuardianFogPrompt, Boxes.SanctuaryGuardianFogRotationTarget),
    )
    RunEvent(11215846, slot=1, args=(11210001, Objects.o2915_0000, VFX.ArtoriasEntranceFog))
    RunEvent(
        11215843,
        slot=1,
        args=(11210001, Objects.o2915_0000, Boxes.ArtoriasFogPrompt, Boxes.ArtoriasFogRotationTarget),
    )
    RunEvent(11215846, slot=2, args=(11210004, Objects.o2919_0000, VFX.KalameetEntranceFog))
    RunEvent(
        11215843,
        slot=2,
        args=(11210004, Objects.o2919_0000, Boxes.KalameetFogPrompt, Boxes.KalameetFogRotationTarget),
    )
    RunEvent(11215846, slot=3, args=(11210002, Objects.o2911_0001, VFX.ManusEntranceFog))
    RunEvent(11215843, slot=3, args=(11210002, Objects.o2911_0001, Boxes.ManusFogPrompt, Boxes.ManusFogRotationTarget))
    # <!--!>


def Preconstructor():
    """ 50: Event 50 """
    DisableCharacter(Characters.c4090_0001)
    RunEvent(
        11215030,
        slot=1,
        args=(
            Characters.c4090_0002,
            11215036,
            11215035,
            11210901,
            Spheres.ChesterInvaderSpawn2,
            Boxes.ChesterInvaderTrigger2,
            11215032,
            11210900,
        ),
    )
    RunEvent(11210900, slot=0, args=(Characters.c4090_0001,))
    RunEvent(11210900, slot=1, args=(Characters.c4090_0002,))
    RunEvent(
        11210905,
        slot=0,
        args=(Characters.c4090_0001, 11215035, Spheres.ChesterInvaderSpawn1, Collisions.h0105B1, 11210900, 11215032),
    )
    RunEvent(
        11210905,
        slot=1,
        args=(Characters.c4090_0002, 11215036, Spheres.ChesterInvaderSpawn2, Collisions.h0103B1, 11210901, 11215033),
    )
    RunEvent(11210510, slot=0, args=(Characters.c4110_0000, 1822))
    RunEvent(11210520, slot=0, args=(Characters.c4110_0000, 1820, 1839, 1823))
    RunEvent(11210530, slot=0, args=(Characters.c4110_0000, 1820, 1839, 1821))
    RunEvent(11210535)
    RunEvent(11210910)
    RunEvent(11210912)
    RunEvent(11210915)
    SkipLinesIfFlagOff(2, 1842)
    DisableObject(Objects.o2253)
    DeleteVFX(VFX.ChesterCandlestick, erase_root_only=False)
    RunEvent(11210510, slot=1, args=(Characters.c4090_0000, 1841))
    RunEvent(11210520, slot=1, args=(Characters.c4090_0000, 1840, 1859, 1842))
    RunEvent(11210544)
    RunEvent(11210538)
    RunEvent(11210520, slot=2, args=(Characters.c4140_0000, 1870, 1889, 1872))
    SkipLinesIfFlagOn(1, 11210001)
    DisableObject(Objects.o2760_0000)
    IfFlagOn(-1, 1861)
    IfFlagOn(-1, 1862)
    SkipLinesIfConditionTrue(1, -1)
    DisableCharacter(Characters.c0000_0013)
    RunEvent(11210510, slot=3, args=(Characters.c0000_0013, 1863))
    RunEvent(11210520, slot=3, args=(Characters.c0000_0013, 1860, 1869, 1864))
    RunEvent(11210531, slot=0, args=(Characters.c0000_0013, 1860, 1869, 1861))
    RunEvent(11210532, slot=0, args=(Characters.c0000_0013, 1860, 1869, 1862))
    RunEvent(11210533, slot=0, args=(Characters.c0000_0013, 1860, 1869, 1865))
    RunEvent(11210534, slot=0, args=(Characters.c0000_0013, 1860, 1869, 1865))
    RunEvent(11210543)
    DisableCharacter(Characters.c0000_0006)
    SkipLinesIfClient(3)
    RunEvent(11210540)
    RunEvent(11210541)
    RunEvent(11210542)
    SkipLinesIfFlagOn(1, 11210345)
    DisableFlagRange((11210340, 11210345))
    DisableGravity(Characters.c4531_0000)
    EnableImmortality(Characters.c4531_0000)
    DisableHealthBar(Characters.c4531_0000)
    AddSpecialEffect(Characters.c4531_0000, 5300)
    EnableObjectInvulnerability(Objects.o2621_0000)
    RunEvent(11210340)
    RunEvent(11210341)
    RunEvent(11210345)
    RunEvent(11210346)
    RunEvent(11210347)
    EndOfAnimation(Objects.o0110_0006, 0)
    EndOfAnimation(Objects.o0110_0007, 0)
    RunEvent(11217000)
    RunEvent(11210015)


def Event11210090(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11210090: Event 11210090 """
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
def Event11215000():
    """ 11215000: Event 11215000 """
    IfFlagOff(1, 11210000)
    IfActionButton(
        1,
        prompt_text=10010403,
        anchor_entity=Boxes.SanctuaryGuardianFogPrompt,
        anchor_type=CoordEntityType.Region,
        line_intersects=Objects.o2909_0001,
        boss_version=True,
    )
    IfConditionTrue(0, input_condition=1)
    RotateToFaceEntity(PLAYER, Boxes.SanctuaryGuardianFogRotationTarget)
    ForceAnimation(PLAYER, 7410, wait_for_completion=True)
    Restart()


def Event11215001():
    """ 11215001: Event 11215001 """
    IfFlagOff(1, 11210000)
    IfFlagOn(1, 11215003)
    IfCharacterType(1, PLAYER, CharacterType.WhitePhantom)
    IfActionButton(
        1,
        prompt_text=10010403,
        anchor_entity=Boxes.SanctuaryGuardianFogPrompt,
        anchor_type=CoordEntityType.Region,
        trigger_attribute=TriggerAttribute.All,
        line_intersects=Objects.o2909_0001,
    )
    IfConditionTrue(0, input_condition=1)
    RotateToFaceEntity(PLAYER, Boxes.SanctuaryGuardianFogRotationTarget)
    ForceAnimation(PLAYER, 7410)
    Restart()


def Event11215002():
    """ 11215002: Event 11215002 """
    SkipLinesIfThisEventOn(3)
    IfFlagOff(1, 11210000)
    IfCharacterInsideRegion(1, PLAYER, region=Boxes.SanctuaryGuardianCombatStart)
    IfConditionTrue(0, input_condition=1)
    SkipLinesIfClient(2)
    NotifyBossBattleStart()
    SetNetworkUpdateAuthority(Characters.c3471_0000, UpdateAuthority.Forced)
    ActivateMultiplayerBuffs(Characters.c3471_0000)


@RestartOnRest
def Event11215003():
    """ 11215003: Event 11215003 """
    SkipLinesIfThisEventOn(5)
    DisableAI(Characters.c3471_0000)
    IfFlagOn(1, 11215002)
    IfCharacterInsideRegion(1, PLAYER, region=Boxes.SanctuaryGuardianCombatStart)
    IfConditionTrue(0, input_condition=1)
    EnableAI(Characters.c3471_0000)
    EnableBossHealthBar(Characters.c3471_0000, name=3471, slot=0)
    ForceAnimation(Characters.c3471_0000, 3017, wait_for_completion=True)


def Event11215004():
    """ 11215004: Event 11215004 """
    DisableNetworkSync()
    IfFlagOff(1, 11210000)
    IfFlagOn(1, 11215003)
    SkipLinesIfHost(1)
    IfFlagOn(1, 11215001)
    IfCharacterInsideRegion(1, PLAYER, region=Boxes.SanctuaryGuardianCombatStart)
    IfConditionTrue(0, input_condition=1)
    EnableSoundEvent(1213800)


def Event11215005():
    """ 11215005: Event 11215005 """
    DisableNetworkSync()
    IfFlagOn(1, 11215004)
    IfFlagOn(1, 11210000)
    IfConditionTrue(0, input_condition=1)
    DisableSoundEvent(1213800)


@RestartOnRest
def Event11210000():
    """ 11210000: Event 11210000 """
    SkipLinesIfThisEventOff(5)
    DisableCharacter(Characters.c3471_0000)
    Kill(Characters.c3471_0000, award_souls=False)
    DisableCharacter(Characters.c3472_0000)
    Kill(Characters.c3472_0000, award_souls=False)
    End()
    IfHealthLessThanOrEqual(0, Characters.c3471_0000, 0.0)
    Wait(1.0)
    PlaySoundEffect(anchor_entity=Characters.c3471_0000, sound_type=SoundType.s_SFX, sound_id=777777777)
    IfCharacterDead(0, Characters.c3471_0000)
    EnableFlag(11210000)
    KillBoss(1210800)
    DisableObject(Objects.o2909_0001)
    DeleteVFX(VFX.SanctuaryGuardianEntranceFog, erase_root_only=True)
    DisableObject(Objects.o2910_0001)
    DeleteVFX(VFX.SanctuaryGuardianExitFog, erase_root_only=True)


@RestartOnRest
def Event11215006(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 11215006: Event 11215006 """
    DisableCharacter(arg_0_3)
    SkipLinesIfThisEventSlotOff(4)
    SetDisplayMask(arg_4_7, bit_index=0, switch_type=OnOffChange.On)
    SetCollisionMask(arg_4_7, bit_index=1, switch_type=OnOffChange.Off)
    AICommand(arg_4_7, command_id=20, slot=0)
    End()
    SkipLinesIfFlagOn(1, 11210000)
    IfFlagOn(1, 11215002)
    IfCharacterBackreadEnabled(1, arg_4_7)
    IfConditionTrue(0, input_condition=1)
    CreateNPCPart(
        arg_4_7,
        npc_part_id=3471,
        part_index=NPCPartType.Part1,
        part_health=200,
        damage_correction=1.0,
        body_damage_correction=1.0,
        is_invincible=False,
        start_in_stop_state=False,
    )
    IfCharacterPartHealthLessThanOrEqual(2, arg_4_7, npc_part_id=3471, value=0)
    IfHealthLessThanOrEqual(3, arg_4_7, 0.0)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(3)
    Move(
        arg_0_3,
        destination=arg_4_7,
        destination_type=CoordEntityType.Character,
        model_point=150,
        copy_draw_parent=arg_4_7,
    )
    EnableCharacter(arg_0_3)
    ResetAnimation(arg_4_7, disable_interpolation=False)
    ForceAnimation(arg_4_7, 8000)
    ForceAnimation(arg_0_3, 8100)
    SetDisplayMask(arg_4_7, bit_index=0, switch_type=OnOffChange.On)
    SetCollisionMask(arg_4_7, bit_index=1, switch_type=OnOffChange.Off)
    AICommand(arg_4_7, command_id=20, slot=0)
    ReplanAI(arg_4_7)
    IfCharacterHuman(-7, PLAYER)
    IfCharacterHollow(-7, PLAYER)
    EndIfConditionFalse(-7)
    AwardItemLot(arg_8_11, host_only=True)


@RestartOnRest
def Event11215008():
    """ 11215008: Event 11215008 """
    IfFlagOn(0, 11215007)
    IfStandingOnCollision(-1, 1213020)
    IfStandingOnCollision(-2, 1213021)
    IfCharacterInsideRegion(-2, PLAYER, region=Boxes.LesserSanctuaryGuardianReturnTrigger)
    IfConditionTrue(-3, input_condition=-1)
    IfConditionTrue(-3, input_condition=-2)
    IfConditionTrue(0, input_condition=-3)
    SkipLinesIfFinishedConditionTrue(3, -1)
    SetNest(Characters.c3471_0001, Boxes.LesserSanctuaryGuardianNestSwitchingB1)
    SetNest(Characters.c3471_0002, Boxes.LesserSanctuaryGuardianNestSwitchingB2)
    SkipLines(2)
    SetNest(Characters.c3471_0001, Boxes.LesserSanctuaryGuardianNestSwitchingA1)
    SetNest(Characters.c3471_0002, Boxes.LesserSanctuaryGuardianNestSwitchingA2)
    AICommand(Characters.c3471_0001, command_id=10, slot=1)
    AICommand(Characters.c3471_0002, command_id=10, slot=1)
    IfStandingOnCollision(-2, 1213020)
    IfStandingOnCollision(-2, 1213021)
    IfCharacterInsideRegion(-2, PLAYER, region=Boxes.LesserSanctuaryGuardianReturnTrigger)
    IfConditionFalse(0, input_condition=-2)
    AICommand(Characters.c3471_0001, command_id=-1, slot=1)
    AICommand(Characters.c3471_0002, command_id=-1, slot=1)
    Restart()


@RestartOnRest
def Event11215007():
    """ 11215007: Event 11215007 """
    IfFlagOn(0, 11210001)
    DisableAI(Characters.c3471_0001)
    DisableAI(Characters.c3471_0002)
    IfCharacterInsideRegion(1, PLAYER, region=Boxes.LesserSanctuaryGuardianCombatStart0)
    IfCharacterOutsideRegion(1, PLAYER, region=Boxes.LesserSanctuaryGuardianCombatStart1)
    IfCharacterOutsideRegion(1, PLAYER, region=Boxes.LesserSanctuaryGuardianCombatStart2)
    IfConditionTrue(-1, input_condition=1)
    IfAttacked(-1, Characters.c3471_0001, attacker=PLAYER)
    IfAttacked(-1, Characters.c3471_0002, attacker=PLAYER)
    IfConditionTrue(0, input_condition=-1)
    EnableAI(Characters.c3471_0001)
    ForceAnimation(Characters.c3471_0001, 3017)
    WaitFrames(15)
    EnableAI(Characters.c3471_0002)
    ForceAnimation(Characters.c3471_0002, 3017)
    WaitFrames(15)
    ReplanAI(Characters.c3471_0001)
    ReplanAI(Characters.c3471_0002)


@RestartOnRest
def Event11215009():
    """ 11215009: Event 11215009 """
    IfFlagOn(0, 11210001)
    IfCharacterInsideRegion(0, PLAYER, region=Boxes.LesserSanctuaryGuardianNestSwitchingA0)
    Move(
        Characters.c3471_0001,
        destination=Boxes.LesserSanctuaryGuardianNestSwitchingA1,
        destination_type=CoordEntityType.Region,
        copy_draw_parent=Characters.c3471_0000,
    )
    Move(
        Characters.c3471_0002,
        destination=Boxes.LesserSanctuaryGuardianNestSwitchingA2,
        destination_type=CoordEntityType.Region,
        copy_draw_parent=Characters.c3471_0000,
    )
    SetNest(Characters.c3471_0001, Boxes.LesserSanctuaryGuardianNestSwitchingA1)
    SetNest(Characters.c3471_0002, Boxes.LesserSanctuaryGuardianNestSwitchingA2)
    IfCharacterInsideRegion(0, PLAYER, region=Boxes.LesserSanctuaryGuardianNestSwitchingB0)
    Move(
        Characters.c3471_0001,
        destination=Boxes.LesserSanctuaryGuardianNestSwitchingB1,
        destination_type=CoordEntityType.Region,
        copy_draw_parent=Characters.c3471_0000,
    )
    Move(
        Characters.c3471_0002,
        destination=Boxes.LesserSanctuaryGuardianNestSwitchingB2,
        destination_type=CoordEntityType.Region,
        copy_draw_parent=Characters.c3471_0000,
    )
    SetNest(Characters.c3471_0001, Boxes.LesserSanctuaryGuardianNestSwitchingB1)
    SetNest(Characters.c3471_0002, Boxes.LesserSanctuaryGuardianNestSwitchingB2)
    Restart()


def Event11217000():
    """ 11217000: Event 11217000 """
    IfCharacterInsideRegion(3, PLAYER, region=Boxes.LesserSanctuaryGuardianNestSwitchingC0)
    IfCharacterOutsideRegion(4, PLAYER, region=Boxes.LesserSanctuaryGuardianNestSwitchingC0)
    EndIfConditionTrue(4)
    IfCharacterDead(1, Characters.c3471_0001)
    IfCharacterDead(2, Characters.c3471_0002)
    SkipLinesIfFinishedConditionTrue(2, 1)
    Move(
        Characters.c3471_0001,
        destination=Boxes.LesserSanctuaryGuardianNestSwitchingA1,
        destination_type=CoordEntityType.Region,
        copy_draw_parent=Characters.c3471_0000,
    )
    SetNest(Characters.c3471_0001, Boxes.LesserSanctuaryGuardianNestSwitchingA1)
    SkipLinesIfFinishedConditionTrue(2, 2)
    Move(
        Characters.c3471_0002,
        destination=Boxes.LesserSanctuaryGuardianNestSwitchingA2,
        destination_type=CoordEntityType.Region,
        copy_draw_parent=Characters.c3471_0000,
    )
    SetNest(Characters.c3471_0002, Boxes.LesserSanctuaryGuardianNestSwitchingA2)


@RestartOnRest
def Event11215010():
    """ 11215010: Event 11215010 """
    IfFlagOff(1, 11210001)
    IfActionButton(
        1,
        prompt_text=10010403,
        anchor_entity=Boxes.ArtoriasFogPrompt,
        anchor_type=CoordEntityType.Region,
        line_intersects=Objects.o2915_0000,
        boss_version=True,
    )
    IfConditionTrue(0, input_condition=1)
    RotateToFaceEntity(PLAYER, Boxes.ArtoriasFogRotationTarget)
    ForceAnimation(PLAYER, 7410, wait_for_completion=True)
    Restart()


def Event11215011():
    """ 11215011: Event 11215011 """
    IfFlagOff(1, 11210001)
    IfFlagOn(1, 11215013)
    IfCharacterType(1, PLAYER, CharacterType.WhitePhantom)
    IfActionButton(
        1,
        prompt_text=10010403,
        anchor_entity=Boxes.ArtoriasFogPrompt,
        anchor_type=CoordEntityType.Region,
        trigger_attribute=TriggerAttribute.All,
        line_intersects=Objects.o2915_0000,
    )
    IfConditionTrue(0, input_condition=1)
    RotateToFaceEntity(PLAYER, Boxes.ArtoriasFogRotationTarget)
    ForceAnimation(PLAYER, 7410)
    Restart()


def Event11215012():
    """ 11215012: Event 11215012 """
    SkipLinesIfThisEventOn(3)
    IfFlagOff(1, 11210001)
    IfCharacterInsideRegion(1, PLAYER, region=Boxes.ArtoriasCombatStart)
    IfConditionTrue(0, input_condition=1)
    SkipLinesIfClient(2)
    NotifyBossBattleStart()
    SetNetworkUpdateAuthority(Characters.c4100_0000, UpdateAuthority.Forced)
    ActivateMultiplayerBuffs(Characters.c4100_0000)
    EnableFlag(11210537)


@RestartOnRest
def Event11215013():
    """ 11215013: Event 11215013 """
    SkipLinesIfFlagOff(3, 11210001)
    DisableCharacter(Characters.c4100_0000)
    Kill(Characters.c4100_0000, award_souls=False)
    End()
    SkipLinesIfFlagOn(3, 11210030)
    DisableCharacter(Characters.c4100_0000)
    DisableObject(Objects.o2800_0000)
    DisableObject(Objects.o2801_0000)
    DisableAI(Characters.c4100_0000)
    SkipLinesIfThisEventOn(11)
    IfFlagOn(1, 11215012)
    IfCharacterInsideRegion(1, PLAYER, region=Boxes.ArtoriasCombatStart)
    IfConditionTrue(0, input_condition=1)
    SkipLinesIfFlagOn(9, 11210030)
    SkipLinesIfMultiplayer(2)
    PlayCutscene(120110, skippable=True, fade_out=False, player_id=PLAYER)
    SkipLines(1)
    PlayCutscene(120110, skippable=False, fade_out=False, player_id=PLAYER)
    WaitFrames(1)
    EnableObject(Objects.o2800_0000)
    EnableObject(Objects.o2801_0000)
    EnableCharacter(Characters.c4100_0000)
    EnableFlag(11210030)
    EnableAI(Characters.c4100_0000)
    EnableBossHealthBar(Characters.c4100_0000, name=4100, slot=0)
    EnableCollision(Collisions.h7400B1)


def Event11215014():
    """ 11215014: Event 11215014 """
    DisableNetworkSync()
    IfFlagOff(1, 11210001)
    IfFlagOn(1, 11215013)
    SkipLinesIfHost(1)
    IfFlagOn(1, 11215011)
    IfCharacterInsideRegion(1, PLAYER, region=Boxes.ArtoriasCombatStart)
    IfConditionTrue(0, input_condition=1)
    EnableSoundEvent(1213801)


def Event11215015():
    """ 11215015: Event 11215015 """
    DisableNetworkSync()
    IfFlagOn(1, 11215014)
    IfFlagOn(1, 11210001)
    IfConditionTrue(0, input_condition=1)
    DisableSoundEvent(1213801)


@RestartOnRest
def Event11210001():
    """ 11210001: Event 11210001 """
    SkipLinesIfThisEventOff(6)
    DisableCharacter(Characters.c4100_0000)
    Kill(Characters.c4100_0000, award_souls=False)
    DisableBackread(Characters.c4100_0000)
    EnableCharacter(Characters.c3471_0001)
    EnableCharacter(Characters.c3471_0002)
    End()
    DisableBackread(Characters.c4110_0000)
    DisableCharacter(Characters.c3471_0001)
    DisableCharacter(Characters.c3471_0002)
    IfHealthLessThanOrEqual(0, Characters.c4100_0000, 0.0)
    Wait(1.0)
    PlaySoundEffect(anchor_entity=Characters.c4100_0000, sound_type=SoundType.s_SFX, sound_id=777777777)
    IfCharacterDead(0, Characters.c4100_0000)
    EnableFlag(11210001)
    EnableFlag(121)
    KillBoss(1210820)
    DisableFlag(11217060)
    DisableFlag(11217070)
    DisableFlag(11217080)
    DisableFlag(11217090)
    DisableObject(Objects.o2915_0000)
    DeleteVFX(VFX.ArtoriasEntranceFog, erase_root_only=True)
    DisableObject(Objects.o2916_0000)
    DeleteVFX(VFX.ArtoriasExitFog, erase_root_only=True)
    DisableCollision(Collisions.h7400B1)
    Wait(17.0)
    DisableBackread(Characters.c4100_0000)
    EnableBackread(Characters.c4110_0000)
    EnableCharacter(Characters.c3471_0001)
    EnableCharacter(Characters.c3471_0002)


def Event11210015():
    """ 11210015: Event 11210015 """
    DisableNetworkSync()
    IfFlagOn(1, 11210001)
    IfEntityBeyondDistance(1, PLAYER, Characters.c4110_0000, radius=80.0)
    IfConditionTrue(0, input_condition=1)
    DisableBackread(Characters.c4110_0000)
    IfFlagOn(2, 11210001)
    IfEntityWithinDistance(2, PLAYER, Characters.c4110_0000, radius=80.0)
    IfConditionTrue(0, input_condition=2)
    EnableBackread(Characters.c4110_0000)
    Restart()


@RestartOnRest
def Event11215020():
    """ 11215020: Event 11215020 """
    IfFlagOff(1, 11210002)
    IfActionButton(
        1,
        prompt_text=10010403,
        anchor_entity=Boxes.ManusFogPrompt,
        anchor_type=CoordEntityType.Region,
        line_intersects=Objects.o2911_0001,
        boss_version=True,
    )
    IfConditionTrue(0, input_condition=1)
    RotateToFaceEntity(PLAYER, Boxes.ManusFogRotationTarget)
    ForceAnimation(PLAYER, 7410, wait_for_completion=True)
    Restart()


def Event11215021():
    """ 11215021: Event 11215021 """
    IfFlagOff(1, 11210002)
    IfFlagOn(1, 11215023)
    IfCharacterType(1, PLAYER, CharacterType.WhitePhantom)
    IfActionButton(
        1,
        prompt_text=10010403,
        anchor_entity=Boxes.ManusFogPrompt,
        anchor_type=CoordEntityType.Region,
        trigger_attribute=TriggerAttribute.All,
        line_intersects=Objects.o2911_0001,
    )
    IfConditionTrue(0, input_condition=1)
    RotateToFaceEntity(PLAYER, Boxes.ManusFogRotationTarget)
    ForceAnimation(PLAYER, 7410)
    Restart()


def Event11215022():
    """ 11215022: Event 11215022 """
    SkipLinesIfThisEventOn(3)
    IfFlagOff(1, 11210002)
    IfCharacterInsideRegion(1, PLAYER, region=Boxes.ManusCombatStart)
    IfConditionTrue(0, input_condition=1)
    SkipLinesIfClient(2)
    NotifyBossBattleStart()
    SetNetworkUpdateAuthority(Characters.c4500_0000, UpdateAuthority.Forced)
    IfCharacterType(2, PLAYER, CharacterType.BlackPhantom)
    SkipLinesIfConditionFalse(1, 2)
    IfFlagOn(0, 703)
    ActivateMultiplayerBuffs(Characters.c4500_0000)


def Event11215027():
    """ 11215027: Event 11215027 """
    IfFlagOn(1, 11215020)
    IfCharacterInsideRegion(1, PLAYER, region=Boxes.ManusCombatStart)
    IfHost(1)
    IfConditionTrue(0, input_condition=1)
    SkipLinesIfMultiplayer(2)
    PlayCutscene(
        120140,
        skippable=True,
        fade_out=False,
        player_id=PLAYER,
        move_to_region=Cylinders.PlayerPointAfterManusCutscene,
        move_to_map=OOLACILE,
    )
    SkipLines(4)
    SkipLinesIfClient(2)
    PlayCutscene(
        120140,
        skippable=False,
        fade_out=False,
        player_id=PLAYER,
        move_to_region=Cylinders.PlayerPointAfterManusCutscene,
        move_to_map=OOLACILE,
    )
    SkipLines(1)
    PlayCutscene(120140, skippable=False, fade_out=False, player_id=PLAYER)
    WaitFrames(1)
    EnableFlag(11210031)


@RestartOnRest
def Event11215026():
    """ 11215026: Event 11215026 """
    DisableNetworkSync()
    IfCharacterInsideRegion(0, PLAYER, region=Boxes.ManusInvincibleLanding)
    EnableInvincibility(PLAYER)
    Wait(2.0)
    DisableInvincibility(PLAYER)


@RestartOnRest
def Event11215023():
    """ 11215023: Event 11215023 """
    EndIfFlagOn(17)
    SkipLinesIfThisEventOn(3)
    DisableAI(Characters.c4500_0000)
    IfCharacterInsideRegion(0, PLAYER, region=Boxes.ManusInvincibleLanding)
    EnableAI(Characters.c4500_0000)
    EnableBossHealthBar(Characters.c4500_0000, name=4500, slot=0)


def Event11215024():
    """ 11215024: Event 11215024 """
    DisableNetworkSync()
    IfFlagOff(1, 11210002)
    IfFlagOn(1, 11215023)
    SkipLinesIfHost(3)
    IfFlagOn(1, 11215021)
    IfCharacterInsideRegion(1, PLAYER, region=Boxes.ManusCombatStart)
    SkipLines(1)
    IfCharacterInsideRegion(1, PLAYER, region=Boxes.ManusMusic)
    IfConditionTrue(0, input_condition=1)
    EnableSoundEvent(1213802)


def Event11215025():
    """ 11215025: Event 11215025 """
    DisableNetworkSync()
    IfFlagOn(1, 11215024)
    IfFlagOn(1, 11210002)
    IfConditionTrue(0, input_condition=1)
    DisableSoundEvent(1213802)


def Event11210002():
    """ 11210002: Manus dies. Allows player to warp at bonfire even if they don't have the Lordvessel. """
    DisableObject(Objects.o0200_0003)
    DisableObject(Objects.o0200_0003)
    SkipLinesIfThisEventOff(4)
    DisableCharacter(Characters.c4500_0000)
    Kill(Characters.c4500_0000, award_souls=False)
    EnableObject(Objects.o0200_0003)
    End()

    IfHealthLessThanOrEqual(0, Characters.c4500_0000, 0.0)
    Wait(1.0)
    PlaySoundEffect(anchor_entity=Characters.c4500_0000, sound_type=SoundType.s_SFX, sound_id=777777777)
    IfCharacterDead(0, Characters.c4500_0000)
    EnableFlag(11210002)
    EnableFlag(17)
    KillBoss(1210840)
    DisableObject(Objects.o2911_0001)
    DeleteVFX(VFX.ManusEntranceFog, erase_root_only=True)
    DeleteVFX(VFX.SifSummonSign, erase_root_only=True)
    CreateTemporaryVFX(90014, anchor_entity=Objects.o0200_0003, anchor_type=CoordEntityType.Object, model_point=-1)
    Wait(2.0)
    EnableObject(Objects.o0200_0003)
    RegisterBonfire(
        11210992,
        obj=Objects.o0200_0003,
        reaction_distance=2.0,
        reaction_angle=180.0,
        initial_kindle_level=0,
    )


def Event11215250(_, arg_0_3: int, arg_4_7: int):
    """ 11215250: Event 11215250 """
    DeleteVFX(arg_4_7, erase_root_only=False)
    SkipLinesIfFlagOff(2, 11210002)
    DisableObject(arg_0_3)
    End()
    IfObjectDestroyed(-1, arg_0_3)
    IfCharacterDead(-1, Characters.c4500_0000)
    IfConditionTrue(0, input_condition=-1)
    DestroyObject(arg_0_3)
    ForceAnimation(arg_0_3, 0, wait_for_completion=True)
    DisableObject(arg_0_3)


@RestartOnRest
def Event11215060():
    """ 11215060: Event 11215060 """
    IfFlagOn(1, 11210592)
    IfFlagOff(1, 11210004)
    IfActionButton(
        1,
        prompt_text=10010403,
        anchor_entity=Boxes.KalameetFogPrompt,
        anchor_type=CoordEntityType.Region,
        line_intersects=Objects.o2919_0000,
        boss_version=True,
    )
    IfConditionTrue(0, input_condition=1)
    RotateToFaceEntity(PLAYER, Boxes.KalameetFogRotationTarget)
    ForceAnimation(PLAYER, 7410, wait_for_completion=True)
    Restart()


def Event11215061():
    """ 11215061: Event 11215061 """
    IfFlagOn(1, 11210592)
    IfFlagOff(1, 11210004)
    IfFlagOn(1, 11215062)
    IfCharacterType(1, PLAYER, CharacterType.WhitePhantom)
    IfActionButton(
        1,
        prompt_text=10010403,
        anchor_entity=Boxes.KalameetFogPrompt,
        anchor_type=CoordEntityType.Region,
        trigger_attribute=TriggerAttribute.All,
        line_intersects=Objects.o2919_0000,
    )
    IfConditionTrue(0, input_condition=1)
    RotateToFaceEntity(PLAYER, Boxes.KalameetFogRotationTarget)
    ForceAnimation(PLAYER, 7410)
    Restart()


def Event11215062():
    """ 11215062: Event 11215062 """
    SkipLinesIfThisEventOn(4)
    IfFlagOn(1, 11210592)
    IfFlagOff(1, 11210004)
    IfCharacterInsideRegion(1, PLAYER, region=Boxes.KalameetNotifyBattle)
    IfConditionTrue(0, input_condition=1)
    SkipLinesIfClient(2)
    NotifyBossBattleStart()
    SetNetworkUpdateAuthority(Characters.c4510_0001, UpdateAuthority.Forced)
    ActivateMultiplayerBuffs(Characters.c4510_0001)


@RestartOnRest
def Event11215063():
    """ 11215063: Event 11215063 """
    EnableInvincibility(Characters.c4510_0001)
    SkipLinesIfThisEventOn(9)
    DisableAI(Characters.c4510_0001)
    IfFlagOn(1, 11215062)
    IfCharacterInsideRegion(1, PLAYER, region=Boxes.KalameetCombatStart)
    IfStandingOnCollision(-1, 1213003)
    IfStandingOnCollision(-1, 1213004)
    IfStandingOnCollision(-1, 1213009)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    EnableAI(Characters.c4510_0001)
    DisableInvincibility(Characters.c4510_0001)
    EnableBossHealthBar(Characters.c4510_0001, name=4510, slot=0)
    EnableCollision(Collisions.h7400B1)


def Event11215064():
    """ 11215064: Event 11215064 """
    DisableNetworkSync()
    IfFlagOff(1, 11210004)
    IfFlagOn(1, 11215063)
    SkipLinesIfHost(2)
    IfFlagOn(1, 11215061)
    IfFlagOn(1, 11215067)
    IfCharacterInsideRegion(1, PLAYER, region=Boxes.KalameetMusic)
    IfConditionTrue(0, input_condition=1)
    EnableSoundEvent(1213803)


def Event11215065():
    """ 11215065: Event 11215065 """
    DisableNetworkSync()
    IfFlagOn(1, 11215064)
    IfFlagOn(1, 11210004)
    IfConditionTrue(0, input_condition=1)
    DisableSoundEvent(1213803)


def Event11215066():
    """ 11215066: Event 11215066 """
    DisableNetworkSync()
    IfFlagOn(1, 11210592)
    IfFlagOff(1, 11210004)
    IfFlagOn(1, 11215062)
    IfCharacterType(1, PLAYER, CharacterType.WhitePhantom)
    IfActionButton(
        1,
        prompt_text=10010403,
        anchor_entity=Boxes.KalameetFogPrompt,
        anchor_type=CoordEntityType.Region,
        trigger_attribute=TriggerAttribute.All,
        line_intersects=Objects.o2919_0000,
    )
    IfConditionTrue(0, input_condition=1)
    WaitFrames(75)
    EnableFlag(11215067)


def Event11210005():
    """ 11210005: Event 11210005 """
    EndIfThisEventOn()
    IfHealthLessThanOrEqual(0, Characters.c4510_0001, 0.0)
    Wait(1.0)
    PlaySoundEffect(anchor_entity=Characters.c4510_0001, sound_type=SoundType.s_SFX, sound_id=777777777)
    IfCharacterDead(0, Characters.c4510_0001)
    EnableFlag(11210004)
    EnableFlag(11210005)
    EnableFlag(121)
    KillBoss(1210401)
    DisableObject(Objects.o2919_0000)
    DeleteVFX(VFX.KalameetEntranceFog, erase_root_only=True)
    DisableCollision(Collisions.h7400B1)


def Event11210340():
    """ 11210340: Event 11210340 """
    SkipLinesIfThisEventOff(3)
    EndIfFlagOn(11210341)
    Move(
        Characters.c4531_0000,
        destination=Boxes.AlvinaWarp1,
        destination_type=CoordEntityType.Region,
        copy_draw_parent=Characters.c4531_0000,
    )
    End()
    IfHost(1)
    IfEntityWithinDistance(-1, Characters.c4531_0000, PLAYER, radius=7.0)
    IfAttacked(-1, Characters.c4531_0000, attacker=PLAYER)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    ForceAnimation_WithUnknownEffect2(
        Characters.c4531_0000,
        animation=7003,
        loop=False,
        wait_for_completion=True,
        skip_transition=False,
        arg1=5.0,
    )
    DisableCharacter(Characters.c4531_0000)
    Move(
        Characters.c4531_0000,
        destination=Boxes.AlvinaWarp1,
        destination_type=CoordEntityType.Region,
        copy_draw_parent=Characters.c4531_0000,
    )
    EnableCharacter(Characters.c4531_0000)


def Event11210341():
    """ 11210341: Event 11210341 """
    SkipLinesIfThisEventSlotOff(2)
    Move(
        Characters.c4531_0000,
        destination=Boxes.AlvinaWarp2,
        destination_type=CoordEntityType.Region,
        copy_draw_parent=Characters.c4531_0000,
    )
    End()
    IfHost(1)
    IfFlagOn(1, 11210340)
    IfEntityWithinDistance(-1, Characters.c4531_0000, PLAYER, radius=12.0)
    IfAttacked(-1, Characters.c4531_0000, attacker=PLAYER)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    ForceAnimation_WithUnknownEffect2(
        Characters.c4531_0000,
        animation=7003,
        loop=False,
        wait_for_completion=True,
        skip_transition=False,
        arg1=5.0,
    )
    DisableCharacter(Characters.c4531_0000)
    Move(
        Characters.c4531_0000,
        destination=Boxes.AlvinaWarp2,
        destination_type=CoordEntityType.Region,
        copy_draw_parent=Characters.c4531_0000,
    )
    EnableCharacter(Characters.c4531_0000)


def Event11210345():
    """ 11210345: Event 11210345 """
    SkipLinesIfThisEventOff(3)
    DisableCharacter(Characters.c4531_0000)
    DeleteVFX(VFX.IllusoryFloorLandingAura, erase_root_only=False)
    End()
    IfHost(1)
    IfFlagOn(1, 11210341)
    IfEntityWithinDistance(-1, Characters.c4531_0000, PLAYER, radius=12.0)
    IfAttacked(-1, Characters.c4531_0000, attacker=PLAYER)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    ForceAnimation_WithUnknownEffect2(
        Characters.c4531_0000,
        animation=7003,
        loop=False,
        wait_for_completion=True,
        skip_transition=False,
        arg1=5.0,
    )
    DisableCharacter(Characters.c4531_0000)
    DeleteVFX(VFX.IllusoryFloorLandingAura, erase_root_only=True)


def Event11210346():
    """ 11210346: Event 11210346 """
    DisableNetworkSync()
    IfFlagOff(1, 11210345)
    IfCharacterInsideRegion(1, PLAYER, region=Boxes.IllusoryFloorFallControl)
    IfFlagOn(2, 11210345)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(2)
    AddSpecialEffect(PLAYER, 4161)
    Restart()


def Event11210347():
    """ 11210347: Event 11210347 """
    SkipLinesIfFlagOn(1, 11215045)
    SkipLinesIfFlagOff(2, 11210345)
    DisableObject(Objects.o2621_0000)
    End()
    IfHost(1)
    IfCharacterInsideRegion(1, PLAYER, region=Boxes.IllusoryFloorTrigger)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(11215045)
    EndIfObjectDestroyed(Objects.o2621_0000)
    DisableObjectInvulnerability(Objects.o2621_0000)
    DestroyObject(Objects.o2621_0000)
    ForceAnimation(Objects.o2621_0000, 0)
    PlaySoundEffect(anchor_entity=Objects.o2621_0000, sound_type=SoundType.o_Object, sound_id=262000000)


def Event11210025():
    """ 11210025: Event 11210025 """
    SkipLinesIfThisEventOff(2)
    DisableObject(Objects.o2620_0000)
    End()
    IfObjectDestroyed(0, Objects.o2620_0000)
    End()


@RestartOnRest
def Event11210310(_, arg_0_3: int, arg_4_7: int):
    """ 11210310: Event 11210310 """
    SkipLinesIfThisEventSlotOff(3)
    DisableCharacter(arg_0_3)
    Kill(arg_0_3, award_souls=False)
    End()
    IfCharacterDead(0, arg_0_3)
    EnableFlag(arg_4_7)


def Event11210330(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 11210330: Event 11210330 """
    IfFlagRangeAllOn(0, (arg_0_3, arg_4_7))
    EnableFlag(arg_8_11)


def Event11210021():
    """ 11210021: Event 11210021 """
    DisableAI(Characters.c4520_0002)
    EnableInvincibility(Characters.c4520_0002)
    SkipLinesIfFlagOff(5, 11210330)
    DisableCharacter(Characters.c4520_0002)
    DropMandatoryTreasure(Characters.c4520_0002)
    DeleteVFX(VFX.SifBarrier, erase_root_only=False)
    DisableObject(Objects.o2630_0000)
    End()
    IfFlagOn(0, 11210330)
    Wait(6.0)
    ForceAnimation(Characters.c4520_0002, 7010, wait_for_completion=True)
    DisableCharacter(Characters.c4520_0002)
    DropMandatoryTreasure(Characters.c4520_0002)
    DeleteVFX(VFX.SifBarrier, erase_root_only=True)
    DisableObject(Objects.o2630_0000)


@RestartOnRest
def Event11215040():
    """ 11215040: Event 11215040 """
    DisableAI(Characters.c4520_0000)
    DisableCharacter(Characters.c4520_0000)
    IfFlagOff(1, 17)
    IfFlagOn(1, 11210021)
    IfCharacterHuman(1, PLAYER)
    IfActionButton(
        1,
        prompt_text=50000000,
        anchor_entity=Spheres.SifSummonSignPrompt,
        anchor_type=CoordEntityType.Region,
        model_point=0,
    )
    IfConditionTrue(0, input_condition=1)
    DisplayBattlefieldMessage(140010, display_location_index=0)
    SkipLinesIfClient(1)
    ForceAnimation(Characters.c4520_0001, 7008)
    WaitFrames(30)
    DisableCharacter(Characters.c4520_0001)
    EnableFlag(11215042)
    DeleteVFX(VFX.SifSummonSign, erase_root_only=True)
    Wait(10.0)
    EnableCharacter(Characters.c4520_0000)
    EnableAI(Characters.c4520_0000)
    SetTeamType(Characters.c4520_0000, TeamType.WhitePhantom)
    ForceAnimation(Characters.c4520_0000, 7004)
    SkipLinesIfClient(2)
    DisplayBattlefieldMessage(20001110, display_location_index=0)
    SkipLines(1)
    DisplayBattlefieldMessage(20001111, display_location_index=0)
    WaitFrames(140)


@RestartOnRest
def Event11215041():
    """ 11215041: Event 11215041 """
    DisableCharacter(Characters.c4520_0001)
    DisableAI(Characters.c4520_0001)
    DisableAnimations(Characters.c4520_0001)
    EndIfClient()
    IfFlagOn(1, 11210021)
    IfFlagOff(1, 17)
    IfCharacterInsideRegion(1, PLAYER, region=Spheres.SifSummonSignPrompt)
    IfCharacterHuman(1, PLAYER)
    IfConditionTrue(0, input_condition=1)
    EndIfFlagOn(11215042)
    EnableCharacter(Characters.c4520_0001)
    ForceAnimation(Characters.c4520_0001, 7006, wait_for_completion=True)
    ForceAnimation(Characters.c4520_0001, 7007, loop=True)
    IfCharacterOutsideRegion(2, PLAYER, region=Spheres.SifSummonSignPrompt)
    IfFlagOn(2, 11215020)
    IfConditionTrue(0, input_condition=2)
    ForceAnimation(Characters.c4520_0001, 7008, wait_for_completion=True)
    DisableCharacter(Characters.c4520_0001)
    Restart()


@RestartOnRest
def Event11215044():
    """ 11215044: Event 11215044 """
    DeleteVFX(VFX.SifSummonSign, erase_root_only=True)
    EndIfClient()
    IfFlagOff(1, 17)
    IfFlagOn(1, 11210021)
    IfCharacterHuman(1, PLAYER)
    IfConditionTrue(0, input_condition=1)
    CreateVFX(VFX.SifSummonSign)
    IfFlagOff(2, 17)
    IfFlagOn(2, 11210021)
    IfCharacterHuman(2, PLAYER)
    IfConditionFalse(0, input_condition=2)
    Restart()


def Event11210020():
    """ 11210020: Event 11210020 """
    EndIfFlagOn(17)
    IfCharacterDead(1, Characters.c4500_0000)
    IfCharacterAlive(1, Characters.c4520_0000)
    IfFlagOn(1, 11215040)
    IfCharacterDead(2, Characters.c4520_0000)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionTrue(5, 2)
    DisableAI(Characters.c4520_0000)
    WaitFrames(120)
    ForceAnimation(Characters.c4520_0000, 7005, wait_for_completion=True)
    DisableCharacter(Characters.c4520_0000)
    End()
    DisplayBattlefieldMessage(20001115, display_location_index=0)


@RestartOnRest
def Event11215043():
    """ 11215043: Event 11215043 """
    SkipLinesIfThisEventOn(1)
    IfHealthLessThanOrEqual(0, Characters.c4520_0000, 0.30000001192092896)
    AddSpecialEffect(Characters.c4520_0000, 5401)


@RestartOnRest
def Event11215100():
    """ 11215100: Event 11215100 """
    EndIfThisEventOn()
    DisableAI(Characters.c4130_0016)
    IfCharacterType(7, PLAYER, CharacterType.BlackPhantom)
    IfConditionFalse(3, input_condition=7)
    IfCharacterInsideRegion(3, PLAYER, region=Boxes.GardenerTrap2)
    IfConditionTrue(-3, input_condition=3)
    IfAttacked(-3, Characters.c4130_0016, attacker=PLAYER)
    IfConditionTrue(1, input_condition=-3)
    IfConditionFalse(2, input_condition=7)
    IfCharacterInsideRegion(2, PLAYER, region=Boxes.GardenerTrap0)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    SetStandbyAnimationSettings(Characters.c4130_0016, cancel_animation=9060)
    EnableAI(Characters.c4130_0016)
    EndIfFinishedConditionTrue(1)
    SetNest(Characters.c4130_0016, Boxes.GardenerTrap1)
    AICommand(Characters.c4130_0016, command_id=10, slot=0)
    ReplanAI(Characters.c4130_0016)
    Wait(6.0)
    IfCharacterInsideRegion(-2, PLAYER, region=Boxes.GardenerTrap2)
    IfAttacked(-2, Characters.c4130_0016, attacker=PLAYER)
    IfConditionTrue(0, input_condition=-2)
    AICommand(Characters.c4130_0016, command_id=-1, slot=0)
    ReplanAI(Characters.c4130_0016)


@RestartOnRest
def Event11215110(_, arg_0_3: int, arg_4_7: int, arg_8_11: float, arg_12_15: int):
    """ 11215110: Event 11215110 """
    SkipLinesIfThisEventSlotOff(2)
    ResetStandbyAnimationSettings(arg_0_3)
    End()
    DisableAI(arg_0_3)
    IfAttacked(-1, arg_0_3, attacker=PLAYER)
    IfCharacterInsideRegion(-1, PLAYER, region=arg_4_7)
    IfCharacterInsideRegion(-1, PLAYER, region=arg_12_15)
    IfEntityWithinDistance(-1, PLAYER, arg_0_3, radius=arg_8_11)
    IfCharacterType(7, PLAYER, CharacterType.BlackPhantom)
    IfConditionFalse(1, input_condition=7)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    EnableAI(arg_0_3)
    SetStandbyAnimationSettings(arg_0_3, cancel_animation=9060)


@RestartOnRest
def Event11215115(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 11215115: Event 11215115 """
    IfCharacterInsideRegion(0, arg_0_3, region=arg_4_7)
    SetNest(arg_0_3, arg_8_11)


@RestartOnRest
def Event11215120(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11215120: Event 11215120 """
    SkipLinesIfThisEventOff(4)
    ResetStandbyAnimationSettings(arg_0_3)
    ResetStandbyAnimationSettings(arg_4_7)
    ResetStandbyAnimationSettings(arg_8_11)
    End()
    DisableAI(arg_0_3)
    DisableAI(arg_4_7)
    DisableAI(arg_8_11)
    IfHost(1)
    IfAttacked(-1, arg_0_3, attacker=PLAYER)
    IfAttacked(-1, arg_4_7, attacker=PLAYER)
    IfAttacked(-1, arg_8_11, attacker=PLAYER)
    SkipLinesIfClient(2)
    SkipLinesIfFlagOn(1, arg_12_15)
    IfFlagOn(1, arg_12_15)
    IfConditionTrue(-2, input_condition=-1)
    IfConditionTrue(-2, input_condition=1)
    IfConditionTrue(0, input_condition=-2)
    EnableAI(arg_0_3)
    EnableAI(arg_4_7)
    EnableAI(arg_8_11)
    SetStandbyAnimationSettings(arg_0_3, cancel_animation=9060)
    SetStandbyAnimationSettings(arg_4_7, cancel_animation=9060)
    SetStandbyAnimationSettings(arg_8_11, cancel_animation=9060)


@RestartOnRest
def Event11215130(_, arg_0_3: int, arg_4_7: int, arg_8_11: float, arg_12_15: float):
    """ 11215130: Event 11215130 """
    SkipLinesIfThisEventSlotOff(2)
    ResetStandbyAnimationSettings(arg_0_3)
    End()
    IfEntityWithinDistance(-1, PLAYER, arg_4_7, radius=arg_8_11)
    IfAttacked(-1, 1210108, attacker=PLAYER)
    IfAttacked(-1, 1210109, attacker=PLAYER)
    IfAttacked(-1, 1210110, attacker=PLAYER)
    IfCharacterType(7, PLAYER, CharacterType.BlackPhantom)
    IfConditionFalse(1, input_condition=7)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    Wait(arg_12_15)
    SetStandbyAnimationSettings(arg_0_3, cancel_animation=9060)


@RestartOnRest
def Event11215140(
    _,
    arg_0_3: int,
    arg_4_7: int,
    arg_8_11: int,
    arg_12_15: int,
    arg_16_19: int,
    arg_20_23: int,
    arg_24_27: int,
):
    """ 11215140: Event 11215140 """
    IfCharacterInsideRegion(1, arg_0_3, region=arg_4_7)
    IfFlagOff(1, arg_16_19)
    IfHasAIStatus(1, arg_0_3, ai_status=AIStatusType.Normal)
    IfCharacterInsideRegion(2, arg_0_3, region=arg_8_11)
    IfFlagOff(2, arg_20_23)
    IfHasAIStatus(2, arg_0_3, ai_status=AIStatusType.Normal)
    IfCharacterInsideRegion(3, arg_0_3, region=arg_12_15)
    IfFlagOff(3, arg_24_27)
    IfHasAIStatus(3, arg_0_3, ai_status=AIStatusType.Normal)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionFalse(3, 1)
    EnableFlag(arg_16_19)
    DisableFlag(arg_20_23)
    DisableFlag(arg_24_27)
    SkipLinesIfFinishedConditionFalse(3, 2)
    DisableFlag(arg_16_19)
    EnableFlag(arg_20_23)
    DisableFlag(arg_24_27)
    SkipLinesIfFinishedConditionFalse(3, 3)
    DisableFlag(arg_16_19)
    DisableFlag(arg_20_23)
    EnableFlag(arg_24_27)
    ResetAnimation(arg_0_3, disable_interpolation=False)
    ForceAnimation(arg_0_3, 7000, skip_transition=True)
    WaitFrames(25)
    ForceAnimation(arg_0_3, 9000, skip_transition=True)
    WaitFrames(190)
    ForceAnimation(arg_0_3, 9060)
    WaitFrames(35)
    Restart()


def Event11210600(_, arg_0_3: int, arg_4_7: int):
    """ 11210600: Event 11210600 """
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
def Event11210350(_, arg_0_3: int, arg_4_7: int):
    """ 11210350: Event 11210350 """
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


@RestartOnRest
def Event11210150():
    """ 11210150: Event 11210150 """
    EndIfFlagOn(11210160)
    Move(
        Characters.c4150_0026,
        destination=Boxes.Elevator4_CallDownTrigger,
        destination_type=CoordEntityType.Region,
        set_draw_parent=Collisions.h0107B1,
    )
    Move(
        Characters.c4150_0026,
        destination=Cylinders.ChainedPrisonerWarpPoint,
        destination_type=CoordEntityType.Region,
        set_draw_parent=Collisions.h0107B1,
    )
    SetNest(Characters.c4150_0026, Cylinders.ChainedPrisonerWarpPoint)


def Event11210100():
    """ 11210100: Event 11210100 """
    SkipLinesIfFlagOff(1, 11210101)
    EndOfAnimation(Objects.o2700_0000, 0)
    SkipLinesIfFlagOn(1, 11210101)
    EndOfAnimation(Objects.o2700_0000, 10)
    IfFlagOn(0, 11210103)
    IfFlagOff(0, 11215220)
    IfFlagOff(1, 11210101)
    IfCharacterInsideRegion(1, PLAYER, region=Boxes.Elevator0_StartFromBottomTrigger)
    IfFlagOn(2, 11210102)
    IfFlagOn(2, 11210101)
    IfCharacterInsideRegion(2, PLAYER, region=Boxes.Elevator0_StartFromTopTrigger)
    IfFlagOn(3, 11210102)
    IfFlagOff(3, 11210101)
    IfCharacterInsideRegion(3, PLAYER, region=Boxes.Elevator0_CallUpTrigger)
    IfFlagOn(4, 11210101)
    IfCharacterInsideRegion(4, PLAYER, region=Boxes.Elevator0_CallDownTrigger)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(-1, input_condition=4)
    IfConditionTrue(0, input_condition=-1)
    WaitForNetworkApproval(max_seconds=3.0)
    EnableFlag(11215220)
    SkipLinesIfFinishedConditionTrue(26, 2)
    SkipLinesIfFinishedConditionTrue(25, 4)
    EnableFlag(11210102)
    EnableFlag(11218102)
    SkipLinesIfFinishedConditionTrue(11, 1)
    IfAllPlayersOutsideRegion(-2, region=Boxes.Elevator0_CallUpTrigger)
    IfCharacterInsideRegion(5, PLAYER, region=Boxes.Elevator0_CallDownTrigger)
    IfHost(5)
    IfTimeElapsed(5, 1.0)
    IfConditionTrue(-2, input_condition=5)
    IfFlagOff(7, 11218102)
    IfFlagOff(7, 11218103)
    IfConditionTrue(7, input_condition=-2)
    IfConditionTrue(0, input_condition=7)
    DisableFlag(11215220)
    Restart()
    IfAllPlayersOutsideRegion(-2, region=Boxes.Elevator0_StartFromTopTrigger)
    IfCharacterInsideRegion(5, PLAYER, region=Boxes.Elevator0_CallDownTrigger)
    IfHost(5)
    IfTimeElapsed(5, 1.0)
    IfConditionTrue(-2, input_condition=5)
    IfFlagOff(7, 11218102)
    IfFlagOff(7, 11218103)
    IfConditionTrue(7, input_condition=-2)
    IfConditionTrue(0, input_condition=7)
    DisableFlag(11215220)
    Restart()
    EnableFlag(11218103)
    SkipLinesIfFinishedConditionTrue(11, 2)
    IfAllPlayersOutsideRegion(-3, region=Boxes.Elevator0_CallDownTrigger)
    IfCharacterInsideRegion(6, PLAYER, region=Boxes.Elevator0_CallUpTrigger)
    IfHost(6)
    IfTimeElapsed(6, 1.0)
    IfConditionTrue(-3, input_condition=6)
    IfFlagOff(8, 11218102)
    IfFlagOff(8, 11218103)
    IfConditionTrue(8, input_condition=-3)
    IfConditionTrue(0, input_condition=8)
    DisableFlag(11215220)
    Restart()
    IfAllPlayersOutsideRegion(-3, region=Boxes.Elevator0_StartFromBottomTrigger)
    IfCharacterInsideRegion(6, PLAYER, region=Boxes.Elevator0_CallUpTrigger)
    IfHost(6)
    IfTimeElapsed(6, 1.0)
    IfConditionTrue(-3, input_condition=6)
    IfFlagOff(8, 11218102)
    IfFlagOff(8, 11218103)
    IfConditionTrue(8, input_condition=-3)
    IfConditionTrue(0, input_condition=8)
    DisableFlag(11215220)
    Restart()


def Event11219100(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_12: uchar, arg_16_19: int):
    """ 11219100: Event 11219100 """
    IfFlagOn(0, arg_0_3)
    CreateTemporaryVFX(120030, anchor_entity=arg_16_19, anchor_type=CoordEntityType.Object, model_point=101)
    SetFlagState(11210101, state=arg_12_12)
    CreateObjectVFX(120029, obj=arg_4_7, model_point=191)
    ForceAnimation(arg_4_7, arg_8_11)
    WaitFrames(180)
    DeleteObjectVFX(arg_4_7, erase_root=False)
    DisableFlag(arg_0_3)
    Restart()


def Event11210103():
    """ 11210103: Event 11210103 """
    IfCharacterType(7, PLAYER, CharacterType.BlackPhantom)
    IfConditionFalse(1, input_condition=7)
    IfCharacterInsideRegion(1, PLAYER, region=Boxes.Elevator0_StartTrigger)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(11210103)


def Event11210110():
    """ 11210110: Event 11210110 """
    SkipLinesIfFlagOff(1, 11210111)
    EndOfAnimation(Objects.o2700_0001, 11)
    SkipLinesIfFlagOn(1, 11210111)
    EndOfAnimation(Objects.o2700_0001, 1)
    IfFlagOff(0, 11215221)
    IfFlagOn(1, 11210111)
    IfCharacterInsideRegion(1, PLAYER, region=Boxes.Elevator1_StartFromBottomTrigger)
    IfFlagOff(2, 11210111)
    IfCharacterInsideRegion(2, PLAYER, region=Boxes.Elevator1_StartFromTopTrigger)
    IfFlagOn(3, 11210111)
    IfCharacterInsideRegion(3, PLAYER, region=Boxes.Elevator1_CallUpTrigger)
    IfFlagOff(4, 11210111)
    IfCharacterInsideRegion(4, PLAYER, region=Boxes.Elevator1_CallDownTrigger)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(-1, input_condition=4)
    IfConditionTrue(0, input_condition=-1)
    WaitForNetworkApproval(max_seconds=3.0)
    EnableFlag(11215221)
    SkipLinesIfFinishedConditionTrue(24, 2)
    SkipLinesIfFinishedConditionTrue(23, 4)
    CreateTemporaryVFX(120030, anchor_entity=Objects.o2701_0011, anchor_type=CoordEntityType.Object, model_point=101)
    DisableFlag(11210111)
    CreateObjectVFX(120029, obj=Objects.o2700_0001, model_point=191)
    ForceAnimation(Objects.o2700_0001, 1)
    WaitFrames(140)
    DeleteObjectVFX(Objects.o2700_0001, erase_root=False)
    SkipLinesIfFinishedConditionTrue(8, 1)
    IfAllPlayersOutsideRegion(-2, region=Boxes.Elevator1_CallUpTrigger)
    IfCharacterInsideRegion(5, PLAYER, region=Boxes.Elevator1_CallDownTrigger)
    IfHost(5)
    IfTimeElapsed(5, 1.0)
    IfConditionTrue(-2, input_condition=5)
    IfConditionTrue(0, input_condition=-2)
    DisableFlag(11215221)
    Restart()
    IfAllPlayersOutsideRegion(-2, region=Boxes.Elevator1_StartFromTopTrigger)
    IfCharacterInsideRegion(5, PLAYER, region=Boxes.Elevator1_CallDownTrigger)
    IfHost(5)
    IfTimeElapsed(5, 1.0)
    IfConditionTrue(-2, input_condition=5)
    IfConditionTrue(0, input_condition=-2)
    DisableFlag(11215221)
    Restart()
    CreateTemporaryVFX(120030, anchor_entity=Objects.o2701_0001, anchor_type=CoordEntityType.Object, model_point=101)
    EnableFlag(11210111)
    CreateObjectVFX(120029, obj=Objects.o2700_0001, model_point=191)
    ForceAnimation(Objects.o2700_0001, 11)
    WaitFrames(140)
    DeleteObjectVFX(Objects.o2700_0001, erase_root=False)
    SkipLinesIfFinishedConditionTrue(8, 2)
    IfAllPlayersOutsideRegion(-3, region=Boxes.Elevator1_CallDownTrigger)
    IfCharacterInsideRegion(6, PLAYER, region=Boxes.Elevator1_CallUpTrigger)
    IfHost(6)
    IfTimeElapsed(6, 1.0)
    IfConditionTrue(-3, input_condition=6)
    IfConditionTrue(0, input_condition=-3)
    DisableFlag(11215221)
    Restart()
    IfAllPlayersOutsideRegion(-3, region=Boxes.Elevator1_StartFromBottomTrigger)
    IfCharacterInsideRegion(6, PLAYER, region=Boxes.Elevator1_CallUpTrigger)
    IfHost(6)
    IfTimeElapsed(6, 1.0)
    IfConditionTrue(-3, input_condition=6)
    IfConditionTrue(0, input_condition=-3)
    DisableFlag(11215221)
    Restart()


def Event11210120():
    """ 11210120: Event 11210120 """
    SkipLinesIfFlagOff(1, 11210121)
    EndOfAnimation(Objects.o2700_0002, 2)
    SkipLinesIfFlagOn(1, 11210121)
    EndOfAnimation(Objects.o2700_0002, 12)
    IfFlagOn(0, 11210123)
    IfFlagOff(0, 11215222)
    IfFlagOff(1, 11210121)
    IfCharacterInsideRegion(1, PLAYER, region=Boxes.Elevator2_StartFromBottomTrigger)
    IfFlagOn(2, 11210122)
    IfFlagOn(2, 11210121)
    IfCharacterInsideRegion(2, PLAYER, region=Boxes.Elevator2_StartFromTopTrigger)
    IfFlagOn(3, 11210122)
    IfFlagOff(3, 11210121)
    IfCharacterInsideRegion(3, PLAYER, region=Boxes.Elevator2_CallUpTrigger)
    IfFlagOn(4, 11210121)
    IfCharacterInsideRegion(4, PLAYER, region=Boxes.Elevator2_CallDownTrigger)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(-1, input_condition=4)
    IfConditionTrue(0, input_condition=-1)
    WaitForNetworkApproval(max_seconds=3.0)
    EnableFlag(11215222)
    SkipLinesIfFinishedConditionTrue(25, 2)
    SkipLinesIfFinishedConditionTrue(24, 4)
    CreateTemporaryVFX(120030, anchor_entity=Objects.o2701_0012, anchor_type=CoordEntityType.Object, model_point=101)
    EnableFlag(11210121)
    EnableFlag(11210122)
    CreateObjectVFX(120029, obj=Objects.o2700_0002, model_point=191)
    ForceAnimation(Objects.o2700_0002, 2)
    WaitFrames(140)
    DeleteObjectVFX(Objects.o2700_0002, erase_root=False)
    SkipLinesIfFinishedConditionTrue(8, 1)
    IfAllPlayersOutsideRegion(-2, region=Boxes.Elevator2_CallUpTrigger)
    IfCharacterInsideRegion(5, PLAYER, region=Boxes.Elevator2_CallDownTrigger)
    IfHost(5)
    IfTimeElapsed(5, 1.0)
    IfConditionTrue(-2, input_condition=5)
    IfConditionTrue(0, input_condition=-2)
    DisableFlag(11215222)
    Restart()
    IfAllPlayersOutsideRegion(-2, region=Boxes.Elevator2_StartFromTopTrigger)
    IfCharacterInsideRegion(5, PLAYER, region=Boxes.Elevator2_CallDownTrigger)
    IfHost(5)
    IfTimeElapsed(5, 1.0)
    IfConditionTrue(-2, input_condition=5)
    IfConditionTrue(0, input_condition=-2)
    DisableFlag(11215222)
    Restart()
    CreateTemporaryVFX(120030, anchor_entity=Objects.o2701_0002, anchor_type=CoordEntityType.Object, model_point=101)
    DisableFlag(11210121)
    CreateObjectVFX(120029, obj=Objects.o2700_0002, model_point=191)
    ForceAnimation(Objects.o2700_0002, 12)
    WaitFrames(140)
    DeleteObjectVFX(Objects.o2700_0002, erase_root=False)
    SkipLinesIfFinishedConditionTrue(8, 2)
    IfAllPlayersOutsideRegion(-3, region=Boxes.Elevator2_CallDownTrigger)
    IfCharacterInsideRegion(6, PLAYER, region=Boxes.Elevator2_CallUpTrigger)
    IfHost(6)
    IfTimeElapsed(6, 1.0)
    IfConditionTrue(-3, input_condition=6)
    IfConditionTrue(0, input_condition=-3)
    DisableFlag(11215222)
    Restart()
    IfAllPlayersOutsideRegion(-3, region=Boxes.Elevator2_StartFromBottomTrigger)
    IfCharacterInsideRegion(6, PLAYER, region=Boxes.Elevator2_CallUpTrigger)
    IfHost(6)
    IfTimeElapsed(6, 1.0)
    IfConditionTrue(-3, input_condition=6)
    IfConditionTrue(0, input_condition=-3)
    DisableFlag(11215222)
    Restart()


def Event11210123():
    """ 11210123: Event 11210123 """
    IfCharacterType(7, PLAYER, CharacterType.BlackPhantom)
    IfConditionFalse(1, input_condition=7)
    IfCharacterInsideRegion(1, PLAYER, region=Boxes.Elevator2_StartTrigger)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(11210123)


def Event11210130():
    """ 11210130: Event 11210130 """
    SkipLinesIfFlagOff(1, 11210131)
    EndOfAnimation(Objects.o2700_0003, 3)
    SkipLinesIfFlagOn(1, 11210131)
    EndOfAnimation(Objects.o2700_0003, 13)
    IfFlagOn(0, 11210133)
    IfFlagOff(0, 11215223)
    IfFlagOff(1, 11210131)
    IfCharacterInsideRegion(1, PLAYER, region=Boxes.Elevator3_StartFromBottomTrigger)
    IfFlagOn(2, 11210132)
    IfFlagOn(2, 11210131)
    IfCharacterInsideRegion(2, PLAYER, region=Boxes.Elevator3_StartFromTopTrigger)
    IfFlagOn(3, 11210132)
    IfFlagOff(3, 11210131)
    IfCharacterInsideRegion(3, PLAYER, region=Boxes.Elevator3_CallUpTrigger)
    IfFlagOn(4, 11210131)
    IfCharacterInsideRegion(4, PLAYER, region=Boxes.Elevator3_CallDownTrigger)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(-1, input_condition=4)
    IfConditionTrue(0, input_condition=-1)
    WaitForNetworkApproval(max_seconds=3.0)
    EnableFlag(11215223)
    SkipLinesIfFinishedConditionTrue(25, 2)
    SkipLinesIfFinishedConditionTrue(24, 4)
    CreateTemporaryVFX(120030, anchor_entity=Objects.o2701_0013, anchor_type=CoordEntityType.Object, model_point=101)
    EnableFlag(11210131)
    EnableFlag(11210132)
    CreateObjectVFX(120029, obj=Objects.o2700_0003, model_point=191)
    ForceAnimation(Objects.o2700_0003, 3)
    WaitFrames(240)
    DeleteObjectVFX(Objects.o2700_0003, erase_root=False)
    SkipLinesIfFinishedConditionTrue(8, 1)
    IfAllPlayersOutsideRegion(-2, region=Boxes.Elevator3_CallUpTrigger)
    IfCharacterInsideRegion(5, PLAYER, region=Boxes.Elevator3_CallDownTrigger)
    IfHost(5)
    IfTimeElapsed(5, 1.0)
    IfConditionTrue(-2, input_condition=5)
    IfConditionTrue(0, input_condition=-2)
    DisableFlag(11215223)
    Restart()
    IfAllPlayersOutsideRegion(-2, region=Boxes.Elevator3_StartFromTopTrigger)
    IfCharacterInsideRegion(5, PLAYER, region=Boxes.Elevator3_CallDownTrigger)
    IfHost(5)
    IfTimeElapsed(5, 1.0)
    IfConditionTrue(-2, input_condition=5)
    IfConditionTrue(0, input_condition=-2)
    DisableFlag(11215223)
    Restart()
    CreateTemporaryVFX(120030, anchor_entity=Objects.o2701_0003, anchor_type=CoordEntityType.Object, model_point=101)
    DisableFlag(11210131)
    CreateObjectVFX(120029, obj=Objects.o2700_0003, model_point=191)
    ForceAnimation(Objects.o2700_0003, 13)
    WaitFrames(240)
    DeleteObjectVFX(Objects.o2700_0003, erase_root=False)
    SkipLinesIfFinishedConditionTrue(8, 2)
    IfAllPlayersOutsideRegion(-3, region=Boxes.Elevator3_CallDownTrigger)
    IfCharacterInsideRegion(6, PLAYER, region=Boxes.Elevator3_CallUpTrigger)
    IfHost(6)
    IfTimeElapsed(6, 1.0)
    IfConditionTrue(-3, input_condition=6)
    IfConditionTrue(0, input_condition=-3)
    DisableFlag(11215223)
    Restart()
    IfAllPlayersOutsideRegion(-3, region=Boxes.Elevator3_StartFromBottomTrigger)
    IfCharacterInsideRegion(6, PLAYER, region=Boxes.Elevator3_CallUpTrigger)
    IfHost(6)
    IfTimeElapsed(6, 1.0)
    IfConditionTrue(-3, input_condition=6)
    IfConditionTrue(0, input_condition=-3)
    DisableFlag(11215223)
    Restart()


def Event11210133():
    """ 11210133: Event 11210133 """
    IfCharacterInsideRegion(0, PLAYER, region=Boxes.Elevator3_StartTrigger)
    EnableFlag(11210133)


def Event11210140():
    """ 11210140: Event 11210140 """
    SkipLinesIfFlagOff(1, 11210141)
    EndOfAnimation(Objects.o2700_0004, 4)
    SkipLinesIfFlagOn(1, 11210141)
    EndOfAnimation(Objects.o2700_0004, 14)
    IfFlagOff(0, 11215224)
    IfFlagOff(1, 11210141)
    IfCharacterInsideRegion(1, PLAYER, region=Boxes.Elevator4_StartFromBottomTrigger)
    IfFlagOn(2, 11210141)
    IfCharacterInsideRegion(2, PLAYER, region=Boxes.Elevator4_StartFromTopTrigger)
    IfFlagOff(3, 11210141)
    IfCharacterInsideRegion(3, PLAYER, region=Boxes.Elevator4_CallUpTrigger)
    IfFlagOn(4, 11210141)
    IfCharacterInsideRegion(4, PLAYER, region=Boxes.Elevator4_CallDownTrigger)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(-1, input_condition=4)
    IfConditionTrue(0, input_condition=-1)
    WaitForNetworkApproval(max_seconds=3.0)
    EnableFlag(11215224)
    EnableFlag(11210160)
    SkipLinesIfFinishedConditionTrue(24, 2)
    SkipLinesIfFinishedConditionTrue(23, 4)
    CreateTemporaryVFX(120030, anchor_entity=Objects.o2701_0014, anchor_type=CoordEntityType.Object, model_point=101)
    EnableFlag(11210141)
    CreateObjectVFX(120029, obj=Objects.o2700_0004, model_point=191)
    ForceAnimation(Objects.o2700_0004, 4)
    WaitFrames(180)
    DeleteObjectVFX(Objects.o2700_0004, erase_root=False)
    SkipLinesIfFinishedConditionTrue(8, 1)
    IfAllPlayersOutsideRegion(-2, region=Boxes.Elevator4_CallUpTrigger)
    IfCharacterInsideRegion(5, PLAYER, region=Boxes.Elevator4_CallDownTrigger)
    IfHost(5)
    IfTimeElapsed(5, 1.0)
    IfConditionTrue(-2, input_condition=5)
    IfConditionTrue(0, input_condition=-2)
    DisableFlag(11215224)
    Restart()
    IfAllPlayersOutsideRegion(-2, region=Boxes.Elevator4_StartFromTopTrigger)
    IfCharacterInsideRegion(5, PLAYER, region=Boxes.Elevator4_CallDownTrigger)
    IfHost(5)
    IfTimeElapsed(5, 1.0)
    IfConditionTrue(-2, input_condition=5)
    IfConditionTrue(0, input_condition=-2)
    DisableFlag(11215224)
    Restart()
    CreateTemporaryVFX(120030, anchor_entity=Objects.o2701_0004, anchor_type=CoordEntityType.Object, model_point=101)
    DisableFlag(11210141)
    CreateObjectVFX(120029, obj=Objects.o2700_0004, model_point=191)
    ForceAnimation(Objects.o2700_0004, 14)
    WaitFrames(180)
    DeleteObjectVFX(Objects.o2700_0004, erase_root=False)
    SkipLinesIfFinishedConditionTrue(8, 2)
    IfAllPlayersOutsideRegion(-3, region=Boxes.Elevator4_CallDownTrigger)
    IfCharacterInsideRegion(6, PLAYER, region=Boxes.Elevator4_CallUpTrigger)
    IfHost(6)
    IfTimeElapsed(6, 1.0)
    IfConditionTrue(-3, input_condition=6)
    IfConditionTrue(0, input_condition=-3)
    DisableFlag(11215224)
    Restart()
    IfAllPlayersOutsideRegion(-3, region=Boxes.Elevator4_StartFromBottomTrigger)
    IfCharacterInsideRegion(6, PLAYER, region=Boxes.Elevator4_CallUpTrigger)
    IfHost(6)
    IfTimeElapsed(6, 1.0)
    IfConditionTrue(-3, input_condition=6)
    IfConditionTrue(0, input_condition=-3)
    DisableFlag(11215224)
    Restart()


def Event11210170(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 11210170: Event 11210170 """
    DisableCollision(arg_4_7)
    SkipLinesIfNotEqual(1, left=arg_0_3, right=11215220)
    IfAllPlayersOutsideRegion(1, region=Boxes.Elevator0_StartFromTopTrigger)
    IfCharacterInsideRegion(1, PLAYER, region=arg_8_11)
    IfFlagOn(1, arg_0_3)
    IfConditionTrue(0, input_condition=1)
    EnableCollision(arg_4_7)
    SkipLinesIfNotEqual(3, left=arg_0_3, right=11215220)
    IfCharacterInsideRegion(7, PLAYER, region=Boxes.Elevator0_StartFromTopTrigger)
    IfTimeElapsed(7, 2.0)
    IfConditionTrue(-1, input_condition=7)
    IfAllPlayersOutsideRegion(-1, region=arg_8_11)
    IfFlagOff(-1, arg_0_3)
    IfConditionTrue(0, input_condition=-1)
    Wait(5.0)
    Restart()


def Event11210300():
    """ 11210300: Event 11210300 """
    EndIfClient()
    EndIfThisEventOn()
    IfObjectActivated(0, obj_act_id=11210650)
    EnableFlag(11210650)
    DisplayDialog(
        10010884,
        anchor_entity=Objects.o2720_0000,
        display_distance=3.0,
        button_type=ButtonType.Yes_or_No,
        number_buttons=NumberButtons.NoButton,
    )


@RestartOnRest
def Event11210050():
    """ 11210050: Event 11210050 """
    DisableGravity(Characters.c4510_0000)
    EnableInvincibility(Characters.c4510_0000)
    DisableCharacterCollision(Characters.c4510_0000)
    DisableCharacter(Characters.c4510_0000)
    SkipLinesIfClient(1)
    SetNetworkUpdateAuthority(Characters.c4510_0000, UpdateAuthority.Forced)
    EndIfThisEventOn()
    IfCharacterInsideRegion(0, PLAYER, region=Boxes.KalameetBridgeTrigger)
    EnableFlag(11210050)
    SetNetworkUpdateRate(Characters.c4510_0000, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableCharacter(Characters.c4510_0000)
    Move(
        Characters.c4510_0000,
        destination=Points.KalameetBridgeAppearanceSnap,
        destination_type=CoordEntityType.Region,
        set_draw_parent=Collisions.h0066B1,
    )
    ForceAnimation(Characters.c4510_0000, 7000)
    WaitFrames(420)
    DisableCharacter(Characters.c4510_0000)


@RestartOnRest
def Event11210051():
    """ 11210051: Event 11210051 """
    DisableAI(Characters.c4510_0002)
    EnableImmortality(Characters.c4510_0002)
    DisableGravity(Characters.c4510_0002)
    DisableCharacterCollision(Characters.c4510_0002)
    SkipLinesIfThisEventOn(1)
    DisableCharacter(Characters.c4510_0002)
    SkipLinesIfClient(1)
    SetNetworkUpdateAuthority(Characters.c4510_0002, UpdateAuthority.Forced)
    EndIfThisEventOn()
    IfCharacterInsideRegion(1, PLAYER, region=Boxes.KalameetAirborne0Appears)
    IfFlagOff(1, 11210535)
    IfConditionTrue(0, input_condition=1)
    SetNetworkUpdateRate(Characters.c4510_0002, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableCharacter(Characters.c4510_0002)
    ForceAnimation(Characters.c4510_0002, 7006, skip_transition=True)
    WaitFrames(240)
    ForceAnimation(Characters.c4510_0002, 7008, skip_transition=True)
    WaitFrames(194)
    EnableFlag(11210062)
    EnableFlag(11210069)
    End()


@RestartOnRest
def Event11210052():
    """ 11210052: Event 11210052 """
    SkipLinesIfFlagOff(3, 11210535)
    DisableFlagRange((11210063, 11210067))
    DisableCharacter(Characters.c4510_0002)
    End()
    DisableFlagRange((11210070, 11210073))
    SkipLinesIfClient(1)
    EnableRandomFlagInRange((11210070, 11210073))
    EnableFlag(11210068)
    IfHealthLessThanOrEqual(1, Characters.c4510_0002, 0.009999999776482582)
    IfFlagOn(1, 11210062)
    IfFlagOff(1, 11210535)
    IfFlagOff(1, 11210067)
    IfFlagOn(-2, 11215056)
    IfFlagOn(-2, 11215058)
    IfConditionTrue(2, input_condition=-2)
    IfFlagOn(2, 11210062)
    IfFlagOff(2, 11210535)
    IfFlagOff(2, 11210067)
    IfFlagOn(-3, 11215055)
    IfFlagOn(-3, 11215057)
    IfConditionTrue(3, input_condition=-3)
    IfFlagOn(3, 11210062)
    IfFlagOff(3, 11210535)
    IfFlagOff(3, 11210067)
    IfConditionFalse(4, input_condition=1)
    IfConditionFalse(4, input_condition=2)
    IfConditionFalse(4, input_condition=3)
    IfFlagOn(4, 11210062)
    IfFlagOff(4, 11210535)
    IfFlagOff(4, 11210067)
    IfConditionTrue(-5, input_condition=1)
    IfConditionTrue(-5, input_condition=2)
    IfConditionTrue(-5, input_condition=3)
    IfConditionTrue(-5, input_condition=4)
    IfConditionTrue(0, input_condition=-5)
    SkipLinesIfFinishedConditionTrue(3, 1)
    SkipLinesIfFinishedConditionTrue(4, 2)
    SkipLinesIfFinishedConditionTrue(5, 3)
    SkipLinesIfFinishedConditionTrue(6, 4)
    EnableFlag(11210063)
    SkipLines(5)
    EnableFlag(11210065)
    SkipLines(3)
    EnableFlag(11210064)
    SkipLines(1)
    EnableFlag(11210066)
    EnableFlag(11210067)
    Restart()


@RestartOnRest
def Event11210053():
    """ 11210053: Event 11210053 """
    SkipLinesIfThisEventOff(3)
    DisableCharacter(Characters.c4510_0001)
    DisableCharacter(Characters.c4510_0002)
    End()
    IfFlagOn(1, 11210063)
    IfHost(1)
    IfConditionTrue(0, input_condition=1)
    ForceAnimation(Characters.c4510_0002, 7004, skip_transition=True)
    WaitFrames(176)
    DisableCharacter(Characters.c4510_0002)
    Kill(Characters.c4510_0002, award_souls=True)


@RestartOnRest
def Event11210054():
    """ 11210054: Event 11210054 """
    IfFlagOff(1, 11210065)
    IfFlagOn(1, 11210064)
    IfHost(1)
    IfConditionTrue(0, input_condition=1)
    SkipLinesIfFlagOff(3, 11210069)
    ForceAnimation(Characters.c4510_0002, 7010, skip_transition=True)
    WaitFrames(561)
    SkipLines(2)
    ForceAnimation(Characters.c4510_0002, 7002, skip_transition=True)
    WaitFrames(461)
    IfHealthLessThanOrEqual(2, Characters.c4510_0002, 0.009999999776482582)
    SkipLinesIfConditionTrue(26, 2)
    SkipLinesIfFlagOn(3, 11210070)
    SkipLinesIfFlagOn(7, 11210071)
    SkipLinesIfFlagOn(12, 11210072)
    SkipLinesIfFlagOn(17, 11210073)
    WaitFrames(6)
    ForceAnimation(Characters.c4510_0002, 7001, skip_transition=True)
    WaitFrames(269)
    DisableFlag(11210069)
    SkipLines(17)
    WaitFrames(6)
    ForceAnimation(Characters.c4510_0002, 7008, skip_transition=True)
    WaitFrames(194)
    WaitFrames(60)
    EnableFlag(11210069)
    SkipLines(11)
    WaitFrames(6)
    ForceAnimation(Characters.c4510_0002, 7008, skip_transition=True)
    WaitFrames(194)
    WaitFrames(120)
    EnableFlag(11210069)
    SkipLines(5)
    WaitFrames(6)
    ForceAnimation(Characters.c4510_0002, 7008, skip_transition=True)
    WaitFrames(194)
    WaitFrames(180)
    EnableFlag(11210069)
    DisableFlag(11210067)
    DisableFlag(11210064)
    Restart()


@RestartOnRest
def Event11210055():
    """ 11210055: Event 11210055 """
    IfFlagOn(1, 11210065)
    IfHost(1)
    IfConditionTrue(0, input_condition=1)
    SkipLinesIfFlagOff(3, 11210069)
    ForceAnimation(Characters.c4510_0002, 7011, skip_transition=True)
    WaitFrames(514)
    SkipLines(2)
    ForceAnimation(Characters.c4510_0002, 7003, skip_transition=True)
    WaitFrames(414)
    IfHealthLessThanOrEqual(2, Characters.c4510_0002, 0.009999999776482582)
    SkipLinesIfConditionTrue(26, 2)
    SkipLinesIfFlagOn(3, 11210070)
    SkipLinesIfFlagOn(7, 11210071)
    SkipLinesIfFlagOn(12, 11210072)
    SkipLinesIfFlagOn(17, 11210073)
    WaitFrames(6)
    ForceAnimation(Characters.c4510_0002, 7001, skip_transition=True)
    WaitFrames(269)
    DisableFlag(11210069)
    SkipLines(17)
    WaitFrames(6)
    ForceAnimation(Characters.c4510_0002, 7008, skip_transition=True)
    WaitFrames(194)
    WaitFrames(60)
    EnableFlag(11210069)
    SkipLines(11)
    WaitFrames(6)
    ForceAnimation(Characters.c4510_0002, 7008, skip_transition=True)
    WaitFrames(194)
    WaitFrames(120)
    EnableFlag(11210069)
    SkipLines(5)
    WaitFrames(6)
    ForceAnimation(Characters.c4510_0002, 7008, skip_transition=True)
    WaitFrames(194)
    WaitFrames(180)
    EnableFlag(11210069)
    DisableFlag(11210067)
    DisableFlag(11210065)
    Restart()


@RestartOnRest
def Event11210056():
    """ 11210056: Event 11210056 """
    IfFlagOff(1, 11210064)
    IfFlagOff(1, 11210065)
    IfFlagOn(1, 11210066)
    IfHost(1)
    IfConditionTrue(0, input_condition=1)
    SkipLinesIfFlagOff(11, 11210069)
    ForceAnimation(Characters.c4510_0002, 7009, skip_transition=True)
    WaitFrames(30)
    SkipLinesIfFlagOn(1, 11210070)
    WaitFrames(15)
    SkipLinesIfFlagOn(1, 11210071)
    WaitFrames(30)
    SkipLinesIfFlagOn(1, 11210072)
    WaitFrames(45)
    SkipLinesIfFlagOn(1, 11210073)
    WaitFrames(60)
    SkipLines(11)
    ForceAnimation(Characters.c4510_0002, 7008, skip_transition=True)
    WaitFrames(200)
    SkipLinesIfFlagOn(1, 11210070)
    WaitFrames(15)
    SkipLinesIfFlagOn(1, 11210071)
    WaitFrames(30)
    SkipLinesIfFlagOn(1, 11210072)
    WaitFrames(45)
    SkipLinesIfFlagOn(1, 11210073)
    WaitFrames(60)
    EnableFlag(11210069)
    DisableFlag(11210067)
    DisableFlag(11210066)
    Restart()


@RestartOnRest
def Event11210057():
    """ 11210057: Event 11210057 """
    IfFlagOn(1, 11210070)
    IfFlagOn(1, 11210068)
    IfFlagOn(2, 11210071)
    IfFlagOn(2, 11210068)
    IfFlagOn(3, 11210072)
    IfFlagOn(3, 11210068)
    IfFlagOn(4, 11210073)
    IfFlagOn(4, 11210068)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(-1, input_condition=4)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionTrue(3, 1)
    SkipLinesIfFinishedConditionTrue(8, 2)
    SkipLinesIfFinishedConditionTrue(13, 3)
    SkipLinesIfFinishedConditionTrue(18, 4)
    EnableFlag(11210070)
    DisableFlag(11210071)
    DisableFlag(11210072)
    DisableFlag(11210073)
    DisableFlag(11210068)
    Restart()
    DisableFlag(11210070)
    EnableFlag(11210071)
    DisableFlag(11210072)
    DisableFlag(11210073)
    DisableFlag(11210068)
    Restart()
    DisableFlag(11210070)
    DisableFlag(11210071)
    EnableFlag(11210072)
    DisableFlag(11210073)
    DisableFlag(11210068)
    Restart()
    DisableFlag(11210070)
    DisableFlag(11210071)
    DisableFlag(11210072)
    EnableFlag(11210073)
    DisableFlag(11210068)
    Restart()


@RestartOnRest
def Event11210040():
    """ 11210040: Event 11210040 """
    IfHost(1)
    IfCharacterInsideRegion(-1, PLAYER, region=Boxes.KalameetAirborne2FarBreath)
    IfCharacterInsideRegion(-1, PLAYER, region=Boxes.KalameetAirborne2FarBreathB)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(11215055)
    IfHost(2)
    IfCharacterOutsideRegion(2, PLAYER, region=Boxes.KalameetAirborne2FarBreath)
    IfCharacterOutsideRegion(2, PLAYER, region=Boxes.KalameetAirborne2FarBreathB)
    IfConditionTrue(0, input_condition=2)
    DisableFlag(11215055)
    Restart()


@RestartOnRest
def Event11210041():
    """ 11210041: Event 11210041 """
    IfHost(1)
    IfCharacterInsideRegion(1, PLAYER, region=Boxes.KalameetAirborne3NearBreath)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(11215056)
    IfHost(2)
    IfCharacterOutsideRegion(2, PLAYER, region=Boxes.KalameetAirborne3NearBreath)
    IfConditionTrue(0, input_condition=2)
    DisableFlag(11215056)
    Restart()


@RestartOnRest
def Event11210042():
    """ 11210042: Event 11210042 """
    IfClient(1)
    IfCharacterType(1, PLAYER, CharacterType.WhitePhantom)
    IfCharacterInsideRegion(-1, PLAYER, region=Boxes.KalameetAirborne2FarBreath)
    IfCharacterInsideRegion(-1, PLAYER, region=Boxes.KalameetAirborne2FarBreathB)
    IfConditionTrue(1, input_condition=-1)
    IfFramesElapsed(1, 30)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(11215057)
    WaitFrames(90)
    DisableFlag(11215057)
    Restart()


@RestartOnRest
def Event11210043():
    """ 11210043: Event 11210043 """
    IfClient(1)
    IfCharacterType(1, PLAYER, CharacterType.WhitePhantom)
    IfCharacterInsideRegion(1, PLAYER, region=Boxes.KalameetAirborne3NearBreath)
    IfFramesElapsed(1, 30)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(11215058)
    WaitFrames(90)
    DisableFlag(11215058)
    Restart()


def Event11210004():
    """ 11210004: Event 11210004 """
    SkipLinesIfThisEventOff(2)
    DisableCharacter(Characters.c4510_0001)
    End()
    IfCharacterDead(-1, Characters.c4510_0001)
    IfCharacterDead(-1, Characters.c4510_0002)
    IfConditionTrue(0, input_condition=-1)
    EnableFlag(11210004)


@RestartOnRest
def Event11215050():
    """ 11215050: Event 11215050 """
    IfCharacterInsideRegion(1, PLAYER, region=Boxes.KalameetHates0)
    IfCharacterInsideRegion(2, PLAYER, region=Boxes.KalameetHates2)
    IfAllPlayersOutsideRegion(2, region=Boxes.KalameetHates0)
    IfCharacterInsideRegion(3, PLAYER, region=Boxes.KalameetHates1)
    IfAllPlayersOutsideRegion(3, region=Boxes.KalameetHates0)
    IfAllPlayersOutsideRegion(3, region=Boxes.KalameetHates2)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(4, input_condition=-1)
    IfFlagOn(4, 11215063)
    IfConditionTrue(0, input_condition=4)
    SkipLinesIfFinishedConditionTrue(2, 1)
    SkipLinesIfFinishedConditionTrue(3, 2)
    SkipLinesIfFinishedConditionTrue(4, 3)
    SetEventPoint(Characters.c4510_0001, region=Boxes.KalameetTakeoffPoint0, reaction_range=2.0)
    SkipLines(3)
    SetEventPoint(Characters.c4510_0001, region=Boxes.KalameetTakeoffPoint0, reaction_range=2.0)
    SkipLines(1)
    SetEventPoint(Characters.c4510_0001, region=Boxes.KalameetTakeoffPoint1, reaction_range=2.0)
    Wait(1.0)
    Restart()


@RestartOnRest
def Event11215051():
    """ 11215051: Event 11215051 """
    DisableCharacter(Characters.c4511_0000)
    SkipLinesIfFlagOn(7, 11215054)
    SkipLinesIfThisEventSlotOff(4)
    SetDisplayMask(Characters.c4510_0001, bit_index=0, switch_type=OnOffChange.On)
    SetCollisionMask(Characters.c4510_0001, bit_index=1, switch_type=OnOffChange.Off)
    AICommand(Characters.c4510_0001, command_id=20, slot=0)
    End()
    IfCharacterBackreadEnabled(0, Characters.c4510_0001)
    CreateNPCPart(
        Characters.c4510_0001,
        npc_part_id=4510,
        part_index=NPCPartType.Part1,
        part_health=200,
        damage_correction=1.0,
        body_damage_correction=1.0,
        is_invincible=False,
        start_in_stop_state=False,
    )
    DisableFlag(11215054)
    IfCharacterPartHealthLessThanOrEqual(1, Characters.c4510_0001, npc_part_id=4510, value=0)
    IfHealthLessThanOrEqual(2, Characters.c4510_0001, 0.0)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(2)
    SkipLinesIfFlagOff(3, 11215053)
    SetNPCPartHealth(Characters.c4510_0001, npc_part_id=4510, desired_health=10, overwrite_max=False)
    EnableFlag(11215054)
    Restart()
    Move(
        Characters.c4511_0000,
        destination=Characters.c4510_0001,
        destination_type=CoordEntityType.Character,
        model_point=150,
        copy_draw_parent=Characters.c4510_0001,
    )
    EnableCharacter(Characters.c4511_0000)
    ResetAnimation(Characters.c4510_0001, disable_interpolation=False)
    ForceAnimation(Characters.c4510_0001, 8000)
    ForceAnimation(Characters.c4511_0000, 8100)
    SetDisplayMask(Characters.c4510_0001, bit_index=0, switch_type=OnOffChange.On)
    SetCollisionMask(Characters.c4510_0001, bit_index=1, switch_type=OnOffChange.Off)
    AddSpecialEffect(Characters.c4510_0001, 5434)
    AICommand(Characters.c4510_0001, command_id=20, slot=0)
    ReplanAI(Characters.c4510_0001)
    IfCharacterHuman(-7, PLAYER)
    IfCharacterHollow(-7, PLAYER)
    EndIfConditionFalse(-7)
    AwardItemLot(45110000, host_only=True)


@RestartOnRest
def Event11215052():
    """ 11215052: Event 11215052 """
    IfHasTAEEvent(0, Characters.c4510_0001, tae_event_id=10)
    EnableFlag(11215053)
    IfHasTAEEvent(0, Characters.c4510_0001, tae_event_id=20)
    DisableFlag(11215053)
    Restart()


@RestartOnRest
def Event11215160(_, arg_0_3: int):
    """ 11215160: Event 11215160 """
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
def Event11215165(_, arg_0_3: int):
    """ 11215165: Event 11215165 """
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
def Event11215170(_, arg_0_3: int):
    """ 11215170: Event 11215170 """
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
def Event11215175(_, arg_0_3: int):
    """ 11215175: Event 11215175 """
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
def Event11215180(_, arg_0_3: int, arg_4_7: int):
    """ 11215180: Event 11215180 """
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
def Event11210680(_, arg_0_3: int):
    """ 11210680: Event 11210680 """
    SkipLinesIfThisEventSlotOff(2)
    DropMandatoryTreasure(arg_0_3)
    End()
    IfCharacterDead(0, arg_0_3)
    End()


@RestartOnRest
def Event11215185(_, arg_0_3: int):
    """ 11215185: Event 11215185 """
    EndIfHost()
    IfCharacterBackreadDisabled(1, arg_0_3)
    EndIfConditionTrue(1)
    ResetAnimation(arg_0_3, disable_interpolation=True)
    ForceAnimation(arg_0_3, 0)
    ReplanAI(arg_0_3)


def Event11210200(_, arg_0_3: int, arg_4_7: int):
    """ 11210200: Event 11210200 """
    SkipLinesIfThisEventSlotOff(2)
    DisableObject(arg_0_3)
    End()
    IfCharacterHasSpecialEffect(-1, PLAYER, 620)
    IfCharacterHasSpecialEffect(-1, PLAYER, 6950)
    IfSkullLanternActive(-1)
    IfConditionTrue(1, input_condition=-1)
    IfCharacterInsideRegion(1, PLAYER, region=arg_4_7)
    IfConditionTrue(0, input_condition=1)
    PlaySoundEffect(anchor_entity=arg_0_3, sound_type=SoundType.o_Object, sound_id=262000000)
    ForceAnimation(arg_0_3, 1, wait_for_completion=True)
    DisableObject(arg_0_3)


def Event11210205(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 11210205: Event 11210205 """
    DisableNetworkSync()
    IfCharacterInsideRegion(0, PLAYER, region=arg_4_7)
    EndIfFlagOn(arg_8_11)
    PlaySoundEffect(anchor_entity=arg_0_3, sound_type=SoundType.o_Object, sound_id=120199999)
    Wait(2.0)
    Restart()


def Event11210230(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11210230: Event 11210230 """
    SkipLinesIfThisEventSlotOff(4)
    EndOfAnimation(arg_4_7, arg_12_15)
    PostDestruction(arg_0_3)
    EnableTreasure(arg_4_7)
    End()
    DisableTreasure(arg_4_7)
    SkipLinesIfClient(1)
    CreateObjectVFX(99005, obj=arg_4_7, model_point=90)
    ForceAnimation(arg_4_7, arg_8_11, loop=True)
    IfObjectDestroyed(0, arg_0_3)
    ForceAnimation(arg_4_7, arg_12_15, wait_for_completion=True)
    SkipLinesIfClient(1)
    DeleteObjectVFX(arg_4_7, erase_root=True)
    EnableTreasure(arg_4_7)


def Event11210510(_, arg_0_3: int, arg_4_7: int):
    """ 11210510: Event 11210510 """
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


def Event11210910():
    """ 11210910: Event 11210910 """
    SkipLinesIfThisEventOn(1)
    SetAIParamID(Characters.c4110_0000, 411001)
    IfFlagOn(0, 11210911)
    SetAIParamID(Characters.c4110_0000, 411000)


def Event11210912():
    """ 11210912: Event 11210912 """
    IfFlagOn(0, 1822)
    IfCharacterOutsideRegion(0, PLAYER, region=Boxes.GoughCombatArea)
    SetAIParamID(Characters.c4110_0000, 411001)
    SetNest(Characters.c4110_0000, Boxes.GoughNestArea)
    AICommand(Characters.c4110_0000, command_id=10, slot=0)
    ReplanAI(Characters.c4110_0000)
    IfCharacterInsideRegion(0, PLAYER, region=Boxes.GoughCombatArea)
    WaitFrames(30)
    SetAIParamID(Characters.c4110_0000, 411000)
    AICommand(Characters.c4110_0000, command_id=-1, slot=0)
    ReplanAI(Characters.c4110_0000)
    Restart()


def Event11210915():
    """ 11210915: Event 11210915 """
    EndIfFlagOn(1822)
    IfFlagOn(0, 1822)
    ForceAnimation(Characters.c4110_0000, 9060)


def Event11210520(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11210520: Event 11210520 """
    SkipLinesIfThisEventSlotOff(2)
    DropMandatoryTreasure(arg_0_3)
    End()
    IfHealthLessThanOrEqual(0, arg_0_3, 0.0)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)


def Event11210530(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11210530: Event 11210530 """
    IfFlagOff(1, 1822)
    IfFlagOn(1, 1820)
    IfFlagOn(1, 11210300)
    IfCharacterAlive(1, arg_0_3)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)


def Event11210535():
    """ 11210535: Event 11210535 """
    EndIfThisEventOn()
    DisableCharacter(Characters.c4510_0001)
    IfFlagOn(1, 1821)
    IfFlagOn(1, 11210592)
    IfConditionTrue(0, input_condition=1)
    DisableFlag(121)
    SkipLinesIfMultiplayer(1)
    PlayCutscene(120100, skippable=True, fade_out=False, player_id=PLAYER)
    SkipLines(1)
    PlayCutscene(120100, skippable=False, fade_out=False, player_id=PLAYER)
    WaitFrames(1)
    EnableFlag(11210539)
    EnableCharacter(Characters.c4510_0001)
    DisableCharacter(Characters.c4510_0002)
    EnableObject(Objects.o2919_0000)
    CreateVFX(VFX.KalameetEntranceFog)
    EnableCollision(Collisions.h0095B1_0000)
    DisableCollision(Collisions.h0095B1)


def Event11210544():
    """ 11210544: Event 11210544 """
    IfObjectDestroyed(0, Objects.o2253)
    DeleteVFX(VFX.ChesterCandlestick, erase_root_only=True)


def Event11210531(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11210531: Event 11210531 """
    IfHost(1)
    IfPlayerHasGood(1, 710, including_box=False)
    IfFlagOn(1, 1860)
    IfFlagOn(1, 11210001)
    IfConditionTrue(0, input_condition=1)
    EndIfThisEventOff()
    EnableCharacter(arg_0_3)
    EnableObject(Objects.o2760_0000)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)


def Event11210532(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11210532: Event 11210532 """
    IfFlagOff(1, 1863)
    IfFlagOn(1, 1861)
    IfFlagOn(1, 11210590)
    IfCharacterAlive(1, arg_0_3)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)
    EnableCharacter(arg_0_3)


def Event11210533(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11210533: Event 11210533 """
    IfHost(1)
    IfFlagOff(1, 1863)
    IfFlagOff(1, 1865)
    IfFlagOn(1, 1862)
    IfCharacterBackreadDisabled(1, arg_0_3)
    IfConditionTrue(0, input_condition=1)
    DisableCharacter(arg_0_3)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)


def Event11210534(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11210534: Event 11210534 """
    IfHost(1)
    IfFlagOff(1, 1863)
    IfFlagOff(1, 1864)
    IfFlagOff(1, 1865)
    IfFlagOn(1, 11210591)
    IfCharacterBackreadDisabled(1, arg_0_3)
    IfConditionTrue(0, input_condition=1)
    DisableCharacter(arg_0_3)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)


def Event11210543():
    """ 11210543: Event 11210543 """
    IfFlagOff(1, 11215210)
    IfCharacterInsideRegion(1, Characters.c0000_0013, region=Boxes.TriggerCiaranNestChange)
    IfFlagOn(2, 11215210)
    IfCharacterInsideRegion(2, Characters.c0000_0013, region=Boxes.TriggerCiaranNestRevert)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionTrue(3, 2)
    EnableFlag(11215210)
    SetNest(Characters.c0000_0013, Boxes.CiaranNest)
    Restart()
    DisableFlag(11215210)
    SetNest(Characters.c0000_0013, Boxes.CiaranInitialPosition)
    Restart()


def Event11210540():
    """ 11210540: Event 11210540 """
    IfFlagOn(1, 1127)
    IfFlagOn(1, 11210002)
    IfConditionTrue(0, input_condition=1)
    SkipLinesIfFlagOn(2, 1126)
    SkipLinesIfFlagOn(1, 1125)
    DisableFlagRange((1120, 1139))
    DisableFlag(1127)
    EnableFlag(1128)
    Move(
        Characters.c0000_0006,
        destination=Characters.c4500_0000,
        destination_type=CoordEntityType.Character,
        model_point=30,
        copy_draw_parent=Characters.c4500_0000,
    )
    RequestAnimation(Characters.c0000_0006, 7915, loop=True, wait_for_completion=False)
    EnableCharacter(Characters.c0000_0006)


def Event11210541():
    """ 11210541: Event 11210541 """
    SkipLinesIfThisEventOff(2)
    DropMandatoryTreasure(Characters.c0000_0006)
    End()
    EnableImmortality(Characters.c0000_0006)
    IfHealthLessThanOrEqual(0, Characters.c0000_0006, 0.009999999776482582)
    ForceAnimation(Characters.c0000_0006, 7917, wait_for_completion=True)
    DisableCharacter(Characters.c0000_0006)
    DisableImmortality(Characters.c0000_0006)
    Kill(Characters.c0000_0006, award_souls=True)
    Kill(Characters.c4140_0000, award_souls=False)
    DisableFlagRange((1120, 1139))
    EnableFlag(1125)


def Event11210542():
    """ 11210542: Event 11210542 """
    SkipLinesIfFlagOff(1, 11210541)
    End()
    IfAttacked(0, Characters.c0000_0006, attacker=PLAYER)
    ForceAnimation(Characters.c0000_0006, 7916, wait_for_completion=True)
    Restart()


def Event11210538():
    """ 11210538: Event 11210538 """
    SkipLinesIfThisEventOff(2)
    DropMandatoryTreasure(Characters.c4140_0000)
    End()
    IfFlagOn(0, 1125)
    DropMandatoryTreasure(Characters.c4140_0000)
    DisableFlagRange((1870, 1889))
    EnableFlag(1872)


def Event11215030(
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
    """ 11215030: Event 11215030 """
    EndIfFlagOn(arg_4_7)
    DisableCharacter(arg_0_3)
    EndIfFlagOn(17)
    IfHost(1)
    IfCharacterHuman(1, PLAYER)
    IfFlagOff(1, arg_12_15)
    IfFlagOff(1, 1842)
    IfCharacterInsideRegion(1, PLAYER, region=arg_20_23)
    IfFlagOff(-1, arg_8_11)
    IfFlagOn(2, arg_8_11)
    IfFlagOn(-2, arg_24_27)
    IfFlagOn(-2, arg_28_31)
    IfConditionTrue(2, input_condition=-2)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    DisableCharacter(Characters.c4090_0000)
    EnableCharacter(arg_0_3)
    DisplayBattlefieldMessage(20001100, display_location_index=0)
    SkipLinesIfThisEventSlotOn(3)
    CreateTemporaryVFX(130, anchor_entity=arg_16_19, anchor_type=CoordEntityType.Region)
    ForceAnimation(arg_0_3, 7000)
    ReplanAI(arg_0_3)
    EnableFlag(arg_4_7)
    EnableFlag(11210536)


def Event11210900(_, arg_0_3: int):
    """ 11210900: Event 11210900 """
    EndIfThisEventSlotOn()
    IfCharacterDead(0, arg_0_3)
    IfCharacterInsideRegion(-1, PLAYER, region=Boxes.Arena_1vs1_Small_Territory_4510)
    IfCharacterInsideRegion(-1, PLAYER, region=Boxes.Arena_2vs2_Small_Territory_4511)
    IfCharacterInsideRegion(-1, PLAYER, region=Boxes.Arena_BR_Small_Territory_4512)
    IfCharacterInsideRegion(-1, PLAYER, region=Boxes.Arena_1vs1_Large_Territory_4523)
    IfCharacterInsideRegion(-1, PLAYER, region=Boxes.Arena_2vs2_Large_Territory_4524)
    IfCharacterInsideRegion(-1, PLAYER, region=Boxes.Arena_BR_Large_Territory_4525)
    IfCharacterInsideRegion(-1, PLAYER, region=Boxes.Arena_3vs3_Small_Territory_4510)
    IfCharacterInsideRegion(-1, PLAYER, region=Boxes.Arena_BR6_Small_Territory_4510)
    IfCharacterInsideRegion(-1, PLAYER, region=Boxes.Arena_3vs3_Large_Territory_4523)
    IfCharacterInsideRegion(-1, PLAYER, region=Boxes.Arena_BR6_Large_Territory_4523)
    EndIfConditionTrue(-1)
    DisplayBattlefieldMessage(20001105, display_location_index=0)
    EnableCharacter(Characters.c4090_0000)


def Event11210905(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int, arg_20_23: int):
    """ 11210905: Event 11210905 """
    SkipLinesIfFlagOff(2, arg_20_23)
    DisableCharacter(arg_0_3)
    End()
    IfHost(1)
    IfFlagOn(1, arg_4_7)
    IfFlagOff(1, arg_16_19)
    IfCharacterInsideRegion(-1, PLAYER, region=Boxes.ChesterInvaderReturnsHomeTrigger1)
    IfCharacterInsideRegion(-1, PLAYER, region=Boxes.ChesterInvaderReturnsHomeTrigger2)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(arg_20_23)
    ForceAnimation(arg_0_3, 7001)
    WaitFrames(80)
    DisableCharacter(arg_0_3)
    Move(arg_0_3, destination=arg_8_11, destination_type=CoordEntityType.Region, set_draw_parent=arg_12_15)
    DisplayBattlefieldMessage(20001101, display_location_index=0)
    EnableCharacter(Characters.c4090_0000)


def Event11219010():
    """ 11219010: Event 11219010 """
    IfFlagRangeAnyOn(2, (7000, 7749))
    IfCharacterOutsideRegion(2, PLAYER, region=Boxes.Arena_BR_Large_Territory_4525)
    IfCharacterOutsideRegion(2, PLAYER, region=Boxes.Arena_2vs2_Large_Territory_4524)
    IfCharacterOutsideRegion(2, PLAYER, region=Boxes.Arena_1vs1_Large_Territory_4523)
    IfCharacterOutsideRegion(2, PLAYER, region=Boxes.Arena_BR6_Large_Territory_4523)
    IfCharacterOutsideRegion(2, PLAYER, region=Boxes.Arena_3vs3_Small_Territory_4510)
    IfCharacterOutsideRegion(2, PLAYER, region=Boxes.Arena_BR_Small_Territory_4512)
    IfCharacterOutsideRegion(2, PLAYER, region=Boxes.Arena_2vs2_Small_Territory_4511)
    IfCharacterOutsideRegion(2, PLAYER, region=Boxes.Arena_1vs1_Small_Territory_4510)
    IfCharacterOutsideRegion(2, PLAYER, region=Boxes.Arena_BR6_Small_Territory_4510)
    IfCharacterOutsideRegion(2, PLAYER, region=Boxes.Arena_3vs3_Large_Territory_4523)
    IfCharacterOutsideRegion(2, PLAYER, region=Boxes.Arena_StreakDisplay)
    IfConditionTrue(0, input_condition=2)
    DisableFlagRange((7000, 7749))


def Event11219111():
    """ 11219111: Event 11219111 """
    IfArenaMatchmaking(1)
    IfFlagOff(1, 11211900)
    IfConditionTrue(0, input_condition=1)
    EnableObject(Objects.o2920_0001)
    CreateVFX(VFX.MultiplayerFog6)
    EnableFlag(11211900)
    Restart()


def Event11219112():
    """ 11219112: Event 11219112 """
    IfArenaMatchmaking(1)
    IfConditionFalse(2, input_condition=1)
    IfFlagOn(2, 11211900)
    IfConditionTrue(0, input_condition=2)
    DisableObject(Objects.o2920_0001)
    DeleteVFX(VFX.MultiplayerFog6, erase_root_only=True)
    DisableFlag(11211900)
    Restart()


def Event11219114():
    """ 11219114: Event 11219114 """
    EndIfMultiplayer()
    IfPlayerDoesNotHaveGood(1, 118, including_box=False)
    IfActionButton(
        1,
        prompt_text=60000112,
        anchor_entity=Boxes.Arena_FogControlArea0,
        anchor_type=CoordEntityType.Region,
        button=1211690,
        trigger_attribute=TriggerAttribute.All,
    )
    IfConditionTrue(0, input_condition=1)
    Move(PLAYER, destination=Boxes.Arena_FogControlArea0, destination_type=CoordEntityType.Region, short_move=True)
    RotateToFaceEntity(PLAYER, Points.HostReturnPoint)
    ForceAnimation(PLAYER, 7410)
    DisableObject(Objects.o2920_0001)
    DeleteVFX(VFX.MultiplayerFog6, erase_root_only=True)
    Wait(1.5)
    AwardItemLot(2200, host_only=False)
    Restart()


def Event11219113():
    """ 11219113: Event 11219113 """
    IfClient(2)
    EndIfConditionTrue(2)
    IfHost(1)
    IfPlayerHasGood(1, 118, including_box=False)
    IfConditionTrue(0, input_condition=1)
    DisableObject(Objects.o2920_0001)
    DeleteVFX(VFX.MultiplayerFog6, erase_root_only=False)
    End()


def Event11212787():
    """ 11212787: Event 11212787 """
    DisableNetworkSync()
    IfCharacterInsideRegion(0, PLAYER, region=Boxes.TestBox)
    EnableFlag(11212785)
    IfCharacterOutsideRegion(0, PLAYER, region=Boxes.TestBox)
    DisableFlag(11212785)
    Restart()


def Event11212786():
    """ 11212786: Event 11212786 """
    IfFlagOn(0, 11212785)
    IfFlagOff(0, 11212785)
    Restart()


def Event11213888():
    """ 11213888: Event 11213888 """
    IfCharacterOutsideRegion(1, PLAYER, region=Boxes.Arena_StreakDisplay)
    EndIfConditionTrue(1)
    EqualRecovery()
    AddSpecialEffect(PLAYER, 101)
    AddSpecialEffect(PLAYER, 102)
    AddSpecialEffect(PLAYER, 103)
    AddSpecialEffect(PLAYER, 104)
    End()


def Event11215843(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11215843: Event 11215843 """
    SkipLinesIfEqual(1, left=arg_0_3, right=11210001)
    SkipLines(3)
    IfFlagOn(2, 11210592)
    IfFlagOff(2, 11210004)
    IfConditionFalse(1, input_condition=2)
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


def Event11215846(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 11215846: Event 11215846 """
    SkipLinesIfEqual(1, left=arg_0_3, right=11210001)
    SkipLines(3)
    IfFlagOn(4, 11210592)
    IfFlagOff(4, 11210004)
    IfConditionFalse(1, input_condition=4)
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


def Event11210700():
    """ 11210700: Event 11210700 """
    RunEvent(7999)
    RunEvent(7998)
    RunEvent(11219010)
    SkipLinesIfClient(1)
    DisableFlagRange((11215350, 11215365))
    DisableFlag(11215891)
    DisableFlag(11219902)
    DisableFlag(11215398)
    DisableFlagRange((11215342, 11215345))
    DisableFlagRange((11214350, 11214359))
    DisableFlag(11210810)
    DisableFlag(11218145)
    DeleteVFX(VFX.Arena_Wanted_1vs1_s_A, erase_root_only=False)
    DeleteVFX(VFX.Arena_Wanted_1vs1_s_B, erase_root_only=False)
    DeleteVFX(VFX.Arena_Wanted_2vs2_s_A, erase_root_only=False)
    DeleteVFX(VFX.Arena_Wanted_2vs2_s_B, erase_root_only=False)
    DeleteVFX(VFX.Arena_Wanted_2vs2_s_C, erase_root_only=False)
    DeleteVFX(VFX.Arena_Wanted_2vs2_s_D, erase_root_only=False)
    DeleteVFX(VFX.Arena_BR_Searching_s_A, erase_root_only=False)
    DeleteVFX(VFX.Arena_BR_Searching_s_B, erase_root_only=False)
    DeleteVFX(VFX.Arena_BR_Searching_s_C, erase_root_only=False)
    DeleteVFX(VFX.Arena_BR_Searching_s_D, erase_root_only=False)
    DeleteVFX(VFX.Arena_Wanted_1vs1_b_A, erase_root_only=False)
    DeleteVFX(VFX.Arena_Wanted_1vs1_b_B, erase_root_only=False)
    DeleteVFX(VFX.Arena_Wanted_2vs2_b_A, erase_root_only=False)
    DeleteVFX(VFX.Arena_Wanted_2vs2_b_B, erase_root_only=False)
    DeleteVFX(VFX.Arena_Wanted_2vs2_b_C, erase_root_only=False)
    DeleteVFX(VFX.Arena_Wanted_2vs2_b_D, erase_root_only=False)
    DeleteVFX(VFX.Arena_BR_Searching_b_A, erase_root_only=False)
    DeleteVFX(VFX.Arena_BR_Searching_b_B, erase_root_only=False)
    DeleteVFX(VFX.Arena_BR_Searching_b_C, erase_root_only=False)
    DeleteVFX(VFX.Arena_BR_Searching_b_D, erase_root_only=False)
    RunEvent(11210838)
    RunEvent(11210839)
    RunEvent(11210876)
    RunEvent(11210932)
    RunEvent(11210830)
    RunEvent(11210828, slot=0, args=(11218990, 11215360, 11215362, Boxes.Arena_1vs1_Small_Territory_4510))
    RunEvent(11210828, slot=1, args=(11218991, 11215360, 11215362, Boxes.Arena_1vs1_Large_Territory_4523))
    RunEvent(11210827, slot=0, args=(11218992, 11215360, 11215363, Boxes.Arena_2vs2_Small_Territory_4511))
    RunEvent(11210827, slot=1, args=(11218993, 11215360, 11215363, Boxes.Arena_2vs2_Large_Territory_4524))
    RunEvent(11210827, slot=2, args=(11218994, 11215360, 11215363, Boxes.Arena_BR_Small_Territory_4512))
    RunEvent(11210827, slot=3, args=(11218995, 11215360, 11215363, Boxes.Arena_BR_Large_Territory_4525))
    RunEvent(11210827, slot=4, args=(11218996, 11215360, 11215365, Boxes.Arena_3vs3_Large_Territory_4523))
    RunEvent(11210827, slot=5, args=(11218997, 11215360, 11215365, Boxes.Arena_3vs3_Small_Territory_4510))
    RunEvent(11210827, slot=6, args=(11218998, 11215360, 11215365, Boxes.Arena_BR6_Small_Territory_4510))
    RunEvent(11210827, slot=7, args=(11218999, 11215360, 11215365, Boxes.Arena_BR6_Large_Territory_4523))
    RunEvent(11210835, slot=0, args=(150.0, 30.0, 270.0, 30.0), arg_types="ffff")
    RunEvent(11210836)
    RunEvent(11210877)
    RunEvent(11210878)
    RunEvent(11215398)
    RunEvent(11210875, slot=0, args=(6980, 60000102, 7290))
    RunEvent(11210875, slot=1, args=(6981, 60000103, 7340))
    RunEvent(11210875, slot=2, args=(6982, 60000105, 7440))
    RunEvent(11210875, slot=3, args=(6983, 60000109, 7390))
    RunEvent(11210875, slot=4, args=(6984, 60000106, 7490))
    RunEvent(11210875, slot=5, args=(6985, 60000107, 7540))
    RunEvent(11210875, slot=6, args=(6986, 60000108, 7590))
    RunEvent(11210875, slot=7, args=(6987, 60000110, 7690))
    RunEvent(11210875, slot=8, args=(6988, 60000104, 7640))
    RunEvent(11210875, slot=9, args=(6989, 60000111, 7740))
    RunEvent(11210875, slot=10, args=(6990, 0, 0))
    RunEvent(11210727)
    RunEvent(11210845)
    RunEvent(11210846)
    RunEvent(11210847)
    RunEvent(11210848)
    RunEvent(11210860)
    RunEvent(11210861)
    RunEvent(11210849)
    RunEvent(11210826)
    RunEvent(11210837)
    RunEvent(11210817)
    RunEvent(11210401)
    RunEvent(11210402)
    RunEvent(11219901)
    RunEvent(11219111)
    RunEvent(11219112)
    RunEvent(11210404, slot=0, args=(7290, 11215408, 11218001))
    RunEvent(11210404, slot=1, args=(7340, 11215392, 11218001))
    RunEvent(11210404, slot=2, args=(7390, 11215402, 11218001))
    RunEvent(11210404, slot=3, args=(7440, 11215395, 11218001))
    RunEvent(11210404, slot=4, args=(7490, 11215405, 11218001))
    RunEvent(11210404, slot=5, args=(7540, 11215408, 11218000))
    RunEvent(11210404, slot=6, args=(7590, 11215392, 11218000))
    RunEvent(11210404, slot=7, args=(7640, 11215402, 11218000))
    RunEvent(11210404, slot=8, args=(7690, 11215395, 11218000))
    RunEvent(11210404, slot=9, args=(7740, 11215405, 11218000))
    RunEvent(11210800, slot=0, args=(Cylinders.Arena_InitialSpawnCylinderSmall_Duel1, 11215350, 0))
    RunEvent(11210800, slot=1, args=(Cylinders.Arena_InitialSpawnCylinderSmall_Duel2, 11215352, 0))
    RunEvent(11210800, slot=2, args=(Cylinders.Arena_InitialSpawnCylinderSmall_2v20, 11215350, 1))
    RunEvent(11210800, slot=3, args=(Cylinders.Arena_InitialSpawnCylinderSmall_2v21, 11215351, 1))
    RunEvent(11210800, slot=4, args=(Cylinders.Arena_InitialSpawnCylinderSmall_2v22, 11215352, 1))
    RunEvent(11210800, slot=5, args=(Cylinders.Arena_InitialSpawnCylinderSmall_2v23, 11215353, 1))
    RunEvent(11210800, slot=6, args=(Cylinders.Arena_InitialSpawnCylinderSmall_3v30, 11215350, 1))
    RunEvent(11210800, slot=7, args=(Cylinders.Arena_InitialSpawnCylinderSmall_3v31, 11215351, 1))
    RunEvent(11210800, slot=8, args=(Cylinders.Arena_InitialSpawnCylinderSmall_3v32, 11215352, 1))
    RunEvent(11210800, slot=9, args=(Cylinders.Arena_InitialSpawnCylinderSmall_3v33, 11215353, 1))
    RunEvent(11210800, slot=10, args=(Cylinders.Arena_InitialSpawnCylinderSmall_3v34, 11215354, 1))
    RunEvent(11210800, slot=11, args=(Cylinders.Arena_InitialSpawnCylinderSmall_3v35, 11215355, 1))
    RunEvent(11210800, slot=12, args=(Cylinders.Arena_InitialSpawnCylinderSmall_BR40, 11215350, 1))
    RunEvent(11210800, slot=13, args=(Cylinders.Arena_InitialSpawnCylinderSmall_BR41, 11215351, 1))
    RunEvent(11210800, slot=14, args=(Cylinders.Arena_InitialSpawnCylinderSmall_BR42, 11215352, 1))
    RunEvent(11210800, slot=15, args=(Cylinders.Arena_InitialSpawnCylinderSmall_BR43, 11215353, 1))
    RunEvent(11210800, slot=16, args=(Cylinders.Arena_InitialSpawnCylinderSmall_BR60, 11215350, 1))
    RunEvent(11210800, slot=17, args=(Cylinders.Arena_InitialSpawnCylinderSmall_BR61, 11215351, 1))
    RunEvent(11210800, slot=18, args=(Cylinders.Arena_InitialSpawnCylinderSmall_BR62, 11215352, 1))
    RunEvent(11210800, slot=19, args=(Cylinders.Arena_InitialSpawnCylinderSmall_BR63, 11215353, 1))
    RunEvent(11210800, slot=20, args=(Cylinders.Arena_InitialSpawnCylinderSmall_BR64, 11215354, 1))
    RunEvent(11210800, slot=21, args=(Cylinders.Arena_InitialSpawnCylinderSmall_BR65, 11215355, 1))
    RunEvent(11210800, slot=22, args=(Cylinders.Arena_InitialSpawnCylinderLarge_Duel20, 11215350, 0))
    RunEvent(11210800, slot=23, args=(Cylinders.Arena_InitialSpawnCylinderLarge_Duel21, 11215352, 0))
    RunEvent(11210800, slot=24, args=(Cylinders.Arena_InitialSpawnCylinderLarge_2v20, 11215350, 1))
    RunEvent(11210800, slot=25, args=(Cylinders.Arena_InitialSpawnCylinderLarge_2v21, 11215351, 1))
    RunEvent(11210800, slot=26, args=(Cylinders.Arena_InitialSpawnCylinderLarge_2v22, 11215352, 1))
    RunEvent(11210800, slot=27, args=(Cylinders.Arena_InitialSpawnCylinderLarge_2v23, 11215353, 1))
    RunEvent(11210800, slot=28, args=(Cylinders.Arena_InitialSpawnCylinderLarge_3v30, 11215350, 1))
    RunEvent(11210800, slot=29, args=(Cylinders.Arena_InitialSpawnCylinderLarge_3v31, 11215351, 1))
    RunEvent(11210800, slot=30, args=(Cylinders.Arena_InitialSpawnCylinderLarge_3v32, 11215352, 1))
    RunEvent(11210800, slot=31, args=(Cylinders.Arena_InitialSpawnCylinderLarge_3v33, 11215353, 1))
    RunEvent(11210800, slot=32, args=(Cylinders.Arena_InitialSpawnCylinderLarge_3v34, 11215354, 1))
    RunEvent(11210800, slot=33, args=(Cylinders.Arena_InitialSpawnCylinderLarge_3v35, 11215355, 1))
    RunEvent(11210800, slot=34, args=(Cylinders.Arena_InitialSpawnCylinderLarge_BR40, 11215350, 1))
    RunEvent(11210800, slot=35, args=(Cylinders.Arena_InitialSpawnCylinderLarge_BR41, 11215351, 1))
    RunEvent(11210800, slot=36, args=(Cylinders.Arena_InitialSpawnCylinderLarge_BR42, 11215352, 1))
    RunEvent(11210800, slot=37, args=(Cylinders.Arena_InitialSpawnCylinderLarge_BR43, 11215353, 1))
    RunEvent(11210800, slot=38, args=(Cylinders.Arena_InitialSpawnCylinderLarge_BR60, 11215350, 1))
    RunEvent(11210800, slot=39, args=(Cylinders.Arena_InitialSpawnCylinderLarge_BR61, 11215351, 1))
    RunEvent(11210800, slot=40, args=(Cylinders.Arena_InitialSpawnCylinderLarge_BR62, 11215352, 1))
    RunEvent(11210800, slot=41, args=(Cylinders.Arena_InitialSpawnCylinderLarge_BR63, 11215353, 1))
    RunEvent(11210800, slot=42, args=(Cylinders.Arena_InitialSpawnCylinderLarge_BR64, 11215354, 1))
    RunEvent(11210800, slot=43, args=(Cylinders.Arena_InitialSpawnCylinderLarge_BR65, 11215355, 1))
    RunEvent(11210820, slot=0, args=(11215350, 11215360, 11210825, 0))
    RunEvent(11210820, slot=1, args=(11215351, 11215361, 11210825, 1))
    RunEvent(11210820, slot=2, args=(11215352, 11215362, 11210825, 2))
    RunEvent(11210820, slot=3, args=(11215353, 11215363, 11210825, 3))
    RunEvent(11210820, slot=4, args=(11215354, 11215364, 11210825, 4))
    RunEvent(11210820, slot=5, args=(11215355, 11215365, 11210825, 5))
    RunEvent(11219950, slot=0, args=(11215360,))
    RunEvent(11219950, slot=1, args=(11215361,))
    RunEvent(11219950, slot=2, args=(11215362,))
    RunEvent(11219950, slot=3, args=(11215363,))
    RunEvent(11219950, slot=4, args=(11215364,))
    RunEvent(11219950, slot=5, args=(11215365,))
    RunEvent(11210825, slot=0, args=(11215360, 11218501))
    RunEvent(11210825, slot=1, args=(11215361, 11218502))
    RunEvent(11210825, slot=2, args=(11215362, 11218503))
    RunEvent(11210825, slot=3, args=(11215363, 11218504))
    RunEvent(11210825, slot=4, args=(11215364, 11218505))
    RunEvent(11210825, slot=5, args=(11215365, 11218506))
    RunEvent(11210701, slot=0, args=(11215350, 11218348, 11218354, 11218355, 11218501))
    RunEvent(11210701, slot=1, args=(11215351, 11218349, 11218354, 11218355, 11218502))
    RunEvent(11210701, slot=2, args=(11215352, 11218350, 11218355, 11218354, 11218503))
    RunEvent(11210701, slot=3, args=(11215353, 11218351, 11218355, 11218354, 11218504))
    RunEvent(11210701, slot=4, args=(11215354, 11218352, 11218354, 11218355, 11218505))
    RunEvent(11210701, slot=5, args=(11215355, 11218353, 11218355, 11218354, 11218506))
    RunEvent(11210434)
    RunEvent(11210430, slot=0, args=(11215350, 11218348, 11218350, 11218354, 11218355, 11218501))
    RunEvent(11210430, slot=1, args=(11215351, 11218349, 11218351, 11218354, 11218355, 11218502))
    RunEvent(11210430, slot=2, args=(11215352, 11218350, 11218348, 11218355, 11218354, 11218503))
    RunEvent(11210430, slot=3, args=(11215353, 11218351, 11218349, 11218355, 11218354, 11218504))
    RunEvent(11210430, slot=4, args=(11215354, 11218352, 11218353, 11218354, 11218355, 11218505))
    RunEvent(11210430, slot=5, args=(11215355, 11218353, 11218352, 11218355, 11218354, 11218506))
    RunEvent(11210435, slot=0, args=(11215350, 11218348, 11218349, 11218350, 11218351, 11218352, 11218353, 11218501))
    RunEvent(11210435, slot=1, args=(11215351, 11218349, 11218348, 11218350, 11218351, 11218352, 11218353, 11218502))
    RunEvent(11210435, slot=2, args=(11215352, 11218350, 11218349, 11218348, 11218351, 11218352, 11218353, 11218503))
    RunEvent(11210435, slot=3, args=(11215353, 11218351, 11218349, 11218350, 11218348, 11218352, 11218353, 11218504))
    RunEvent(11210435, slot=4, args=(11215354, 11218352, 11218349, 11218350, 11218351, 11218348, 11218353, 11218505))
    RunEvent(11210435, slot=5, args=(11215355, 11218353, 11218349, 11218350, 11218351, 11218352, 11218348, 11218506))
    RunEvent(11214435, slot=0, args=(11215350, 11218501))
    RunEvent(11214435, slot=1, args=(11215351, 11218502))
    RunEvent(11214435, slot=2, args=(11215352, 11218503))
    RunEvent(11214435, slot=3, args=(11215353, 11218504))
    RunEvent(11214435, slot=4, args=(11215354, 11218505))
    RunEvent(11214435, slot=5, args=(11215355, 11218506))
    RunEvent(11210870, slot=0, args=(11215350, 11218348, 11218354, 11218355))
    RunEvent(11210870, slot=1, args=(11215351, 11218349, 11218354, 11218355))
    RunEvent(11210870, slot=2, args=(11215352, 11218350, 11218355, 11218354))
    RunEvent(11210870, slot=3, args=(11215353, 11218351, 11218355, 11218354))
    RunEvent(11210870, slot=4, args=(11215354, 11218352, 11218354, 11218355))
    RunEvent(11210870, slot=5, args=(11215355, 11218353, 11218355, 11218354))
    RunEvent(11210831, slot=0, args=(11215360, 11218348))
    RunEvent(11210831, slot=1, args=(11215361, 11218349))
    RunEvent(11210831, slot=2, args=(11215362, 11218350))
    RunEvent(11210831, slot=3, args=(11215363, 11218351))
    RunEvent(11210831, slot=4, args=(11215364, 11218352))
    RunEvent(11210831, slot=5, args=(11215365, 11218353))
    RunEvent(11210891, slot=0, args=(11218342, 11215350, 11218343, 11218344, 11218345, 11218346, 11218347))
    RunEvent(11210891, slot=1, args=(11218343, 11215351, 11218342, 11218344, 11218345, 11218346, 11218347))
    RunEvent(11210891, slot=2, args=(11218344, 11215352, 11218343, 11218342, 11218345, 11218346, 11218347))
    RunEvent(11210891, slot=3, args=(11218345, 11215353, 11218343, 11218344, 11218342, 11218346, 11218347))
    RunEvent(11210891, slot=4, args=(11218346, 11215354, 11218343, 11218344, 11218345, 11218342, 11218347))
    RunEvent(11210891, slot=5, args=(11218347, 11215355, 11218343, 11218344, 11218345, 11218346, 11218342))
    RunEvent(11210840, slot=0, args=(11215350, 11218501, 11218511))
    RunEvent(11210840, slot=1, args=(11215351, 11218502, 11218512))
    RunEvent(11210840, slot=2, args=(11215352, 11218503, 11218513))
    RunEvent(11210840, slot=3, args=(11215353, 11218504, 11218514))
    RunEvent(11210840, slot=4, args=(11215354, 11218505, 11218515))
    RunEvent(11210840, slot=5, args=(11215355, 11218506, 11218516))
    RunEvent(11210777, slot=0, args=(11215350, 11218511))
    RunEvent(11210777, slot=1, args=(11215351, 11218512))
    RunEvent(11210777, slot=2, args=(11215352, 11218513))
    RunEvent(11210777, slot=3, args=(11215353, 11218514))
    RunEvent(11210777, slot=4, args=(11215354, 11218515))
    RunEvent(11210777, slot=5, args=(11215355, 11218516))
    RunEvent(
        11210850,
        slot=0,
        args=(
            11215350,
            11218511,
            Boxes.Arena_1vs1_Small_Territory_4510,
            Points.Arena_Spawn_DuelSmall00,
            Points.Arena_Spawn_DuelSmall25,
        ),
    )
    RunEvent(
        11210850,
        slot=1,
        args=(
            11215352,
            11218513,
            Boxes.Arena_1vs1_Small_Territory_4510,
            Points.Arena_Spawn_DuelSmall00,
            Points.Arena_Spawn_DuelSmall25,
        ),
    )
    RunEvent(
        11210850,
        slot=2,
        args=(
            11215350,
            11218511,
            Boxes.Arena_2vs2_Small_Territory_4511,
            Points.Arena_Spawn_2v2SmallInitial0,
            Points.Arena_Spawn_2v2Small21,
        ),
    )
    RunEvent(
        11210850,
        slot=3,
        args=(
            11215351,
            11218512,
            Boxes.Arena_2vs2_Small_Territory_4511,
            Points.Arena_Spawn_2v2SmallInitial0,
            Points.Arena_Spawn_2v2Small21,
        ),
    )
    RunEvent(
        11210850,
        slot=4,
        args=(
            11215352,
            11218513,
            Boxes.Arena_2vs2_Small_Territory_4511,
            Points.Arena_Spawn_2v2SmallInitial0,
            Points.Arena_Spawn_2v2Small21,
        ),
    )
    RunEvent(
        11210850,
        slot=5,
        args=(
            11215353,
            11218514,
            Boxes.Arena_2vs2_Small_Territory_4511,
            Points.Arena_Spawn_2v2SmallInitial0,
            Points.Arena_Spawn_2v2Small21,
        ),
    )
    RunEvent(
        11210850,
        slot=6,
        args=(
            11215350,
            11218511,
            Boxes.Arena_3vs3_Small_Territory_4510,
            Points.Arena_Spawn_3v3SmallInitial0,
            Points.Arena_Spawn_3v3Small26,
        ),
    )
    RunEvent(
        11210850,
        slot=7,
        args=(
            11215351,
            11218512,
            Boxes.Arena_3vs3_Small_Territory_4510,
            Points.Arena_Spawn_3v3SmallInitial0,
            Points.Arena_Spawn_3v3Small26,
        ),
    )
    RunEvent(
        11210850,
        slot=8,
        args=(
            11215352,
            11218513,
            Boxes.Arena_3vs3_Small_Territory_4510,
            Points.Arena_Spawn_3v3SmallInitial0,
            Points.Arena_Spawn_3v3Small26,
        ),
    )
    RunEvent(
        11210850,
        slot=9,
        args=(
            11215353,
            11218514,
            Boxes.Arena_3vs3_Small_Territory_4510,
            Points.Arena_Spawn_3v3SmallInitial0,
            Points.Arena_Spawn_3v3Small26,
        ),
    )
    RunEvent(
        11210850,
        slot=10,
        args=(
            11215354,
            11218515,
            Boxes.Arena_3vs3_Small_Territory_4510,
            Points.Arena_Spawn_3v3SmallInitial0,
            Points.Arena_Spawn_3v3Small26,
        ),
    )
    RunEvent(
        11210850,
        slot=11,
        args=(
            11215355,
            11218516,
            Boxes.Arena_3vs3_Small_Territory_4510,
            Points.Arena_Spawn_3v3SmallInitial0,
            Points.Arena_Spawn_3v3Small26,
        ),
    )
    RunEvent(
        11210850,
        slot=12,
        args=(
            11215350,
            11218511,
            Boxes.Arena_BR_Small_Territory_4512,
            Points.Arena_Spawn_BR4SmallInitial0,
            Points.Arena_Spawn_BR4Small23,
        ),
    )
    RunEvent(
        11210850,
        slot=13,
        args=(
            11215351,
            11218512,
            Boxes.Arena_BR_Small_Territory_4512,
            Points.Arena_Spawn_BR4SmallInitial0,
            Points.Arena_Spawn_BR4Small23,
        ),
    )
    RunEvent(
        11210850,
        slot=14,
        args=(
            11215352,
            11218513,
            Boxes.Arena_BR_Small_Territory_4512,
            Points.Arena_Spawn_BR4SmallInitial0,
            Points.Arena_Spawn_BR4Small23,
        ),
    )
    RunEvent(
        11210850,
        slot=15,
        args=(
            11215353,
            11218514,
            Boxes.Arena_BR_Small_Territory_4512,
            Points.Arena_Spawn_BR4SmallInitial0,
            Points.Arena_Spawn_BR4Small23,
        ),
    )
    RunEvent(
        11210850,
        slot=16,
        args=(
            11215350,
            11218511,
            Boxes.Arena_BR6_Small_Territory_4510,
            Points.Arena_Spawn_BR6SmallInitial0,
            Points.Arena_Spawn_BR6Small21,
        ),
    )
    RunEvent(
        11210850,
        slot=17,
        args=(
            11215351,
            11218512,
            Boxes.Arena_BR6_Small_Territory_4510,
            Points.Arena_Spawn_BR6SmallInitial0,
            Points.Arena_Spawn_BR6Small21,
        ),
    )
    RunEvent(
        11210850,
        slot=18,
        args=(
            11215352,
            11218513,
            Boxes.Arena_BR6_Small_Territory_4510,
            Points.Arena_Spawn_BR6SmallInitial0,
            Points.Arena_Spawn_BR6Small21,
        ),
    )
    RunEvent(
        11210850,
        slot=19,
        args=(
            11215353,
            11218514,
            Boxes.Arena_BR6_Small_Territory_4510,
            Points.Arena_Spawn_BR6SmallInitial0,
            Points.Arena_Spawn_BR6Small21,
        ),
    )
    RunEvent(
        11210850,
        slot=20,
        args=(
            11215354,
            11218515,
            Boxes.Arena_BR6_Small_Territory_4510,
            Points.Arena_Spawn_BR6SmallInitial0,
            Points.Arena_Spawn_BR6Small21,
        ),
    )
    RunEvent(
        11210850,
        slot=21,
        args=(
            11215355,
            11218516,
            Boxes.Arena_BR6_Small_Territory_4510,
            Points.Arena_Spawn_BR6SmallInitial0,
            Points.Arena_Spawn_BR6Small21,
        ),
    )
    RunEvent(
        11210850,
        slot=22,
        args=(
            11215350,
            11218511,
            Boxes.Arena_1vs1_Large_Territory_4523,
            Points.Arena_Spawn_DuelBigInitial0,
            Points.Arena_Spawn_DuelBig33,
        ),
    )
    RunEvent(
        11210850,
        slot=23,
        args=(
            11215352,
            11218513,
            Boxes.Arena_1vs1_Large_Territory_4523,
            Points.Arena_Spawn_DuelBigInitial0,
            Points.Arena_Spawn_DuelBig33,
        ),
    )
    RunEvent(
        11210850,
        slot=24,
        args=(
            11215350,
            11218511,
            Boxes.Arena_2vs2_Large_Territory_4524,
            Points.Arena_Spawn_2v2Big00,
            Points.Arena_Spawn_2v2Big33,
        ),
    )
    RunEvent(
        11210850,
        slot=25,
        args=(
            11215351,
            11218512,
            Boxes.Arena_2vs2_Large_Territory_4524,
            Points.Arena_Spawn_2v2Big00,
            Points.Arena_Spawn_2v2Big33,
        ),
    )
    RunEvent(
        11210850,
        slot=26,
        args=(
            11215352,
            11218513,
            Boxes.Arena_2vs2_Large_Territory_4524,
            Points.Arena_Spawn_2v2Big00,
            Points.Arena_Spawn_2v2Big33,
        ),
    )
    RunEvent(
        11210850,
        slot=27,
        args=(
            11215353,
            11218514,
            Boxes.Arena_2vs2_Large_Territory_4524,
            Points.Arena_Spawn_2v2Big00,
            Points.Arena_Spawn_2v2Big33,
        ),
    )
    RunEvent(
        11210850,
        slot=28,
        args=(
            11215350,
            11218511,
            Boxes.Arena_3vs3_Large_Territory_4523,
            Points.Arena_Spawn_3v3BigInitial0,
            Points.Arena_Spawn_3v3BigInitial5,
        ),
    )
    RunEvent(
        11210850,
        slot=29,
        args=(
            11215351,
            11218512,
            Boxes.Arena_3vs3_Large_Territory_4523,
            Points.Arena_Spawn_3v3BigInitial0,
            Points.Arena_Spawn_3v3BigInitial5,
        ),
    )
    RunEvent(
        11210850,
        slot=30,
        args=(
            11215352,
            11218513,
            Boxes.Arena_3vs3_Large_Territory_4523,
            Points.Arena_Spawn_3v3BigInitial0,
            Points.Arena_Spawn_3v3BigInitial5,
        ),
    )
    RunEvent(
        11210850,
        slot=31,
        args=(
            11215353,
            11218514,
            Boxes.Arena_3vs3_Large_Territory_4523,
            Points.Arena_Spawn_3v3BigInitial0,
            Points.Arena_Spawn_3v3BigInitial5,
        ),
    )
    RunEvent(
        11210850,
        slot=32,
        args=(
            11215354,
            11218515,
            Boxes.Arena_3vs3_Large_Territory_4523,
            Points.Arena_Spawn_3v3BigInitial0,
            Points.Arena_Spawn_3v3BigInitial5,
        ),
    )
    RunEvent(
        11210850,
        slot=33,
        args=(
            11215355,
            11218516,
            Boxes.Arena_3vs3_Large_Territory_4523,
            Points.Arena_Spawn_3v3BigInitial0,
            Points.Arena_Spawn_3v3BigInitial5,
        ),
    )
    RunEvent(
        11210850,
        slot=34,
        args=(
            11215350,
            11218511,
            Boxes.Arena_BR_Large_Territory_4525,
            Points.Arena_Spawn_BR4Big00,
            Points.Arena_Spawn_BR6BigInitial0,
        ),
    )
    RunEvent(
        11210850,
        slot=35,
        args=(
            11215351,
            11218512,
            Boxes.Arena_BR_Large_Territory_4525,
            Points.Arena_Spawn_BR4Big00,
            Points.Arena_Spawn_BR6BigInitial0,
        ),
    )
    RunEvent(
        11210850,
        slot=36,
        args=(
            11215352,
            11218513,
            Boxes.Arena_BR_Large_Territory_4525,
            Points.Arena_Spawn_BR4Big00,
            Points.Arena_Spawn_BR6BigInitial0,
        ),
    )
    RunEvent(
        11210850,
        slot=37,
        args=(
            11215353,
            11218514,
            Boxes.Arena_BR_Large_Territory_4525,
            Points.Arena_Spawn_BR4Big00,
            Points.Arena_Spawn_BR6BigInitial0,
        ),
    )
    RunEvent(
        11210850,
        slot=38,
        args=(
            11215350,
            11218511,
            Boxes.Arena_BR6_Large_Territory_4523,
            Points.Arena_Spawn_BR6Big00,
            Points.Arena_Spawn_BR6Big45,
        ),
    )
    RunEvent(
        11210850,
        slot=39,
        args=(
            11215351,
            11218512,
            Boxes.Arena_BR6_Large_Territory_4523,
            Points.Arena_Spawn_BR6Big00,
            Points.Arena_Spawn_BR6Big45,
        ),
    )
    RunEvent(
        11210850,
        slot=40,
        args=(
            11215352,
            11218513,
            Boxes.Arena_BR6_Large_Territory_4523,
            Points.Arena_Spawn_BR6Big00,
            Points.Arena_Spawn_BR6Big45,
        ),
    )
    RunEvent(
        11210850,
        slot=41,
        args=(
            11215353,
            11218514,
            Boxes.Arena_BR6_Large_Territory_4523,
            Points.Arena_Spawn_BR6Big00,
            Points.Arena_Spawn_BR6Big45,
        ),
    )
    RunEvent(
        11210850,
        slot=42,
        args=(
            11215354,
            11218515,
            Boxes.Arena_BR6_Large_Territory_4523,
            Points.Arena_Spawn_BR6Big00,
            Points.Arena_Spawn_BR6Big45,
        ),
    )
    RunEvent(
        11210850,
        slot=43,
        args=(
            11215355,
            11218516,
            Boxes.Arena_BR6_Large_Territory_4523,
            Points.Arena_Spawn_BR6Big00,
            Points.Arena_Spawn_BR6Big45,
        ),
    )
    RunEvent(11210886, slot=0, args=(11215350, 11218511))
    RunEvent(11210886, slot=1, args=(11215351, 11218512))
    RunEvent(11210886, slot=2, args=(11215352, 11218513))
    RunEvent(11210886, slot=3, args=(11215353, 11218514))
    RunEvent(11210886, slot=4, args=(11215354, 11218515))
    RunEvent(11210886, slot=5, args=(11215355, 11218516))
    RunEvent(11210688, slot=0, args=(11215350, 11218511))
    RunEvent(11210688, slot=1, args=(11215351, 11218512))
    RunEvent(11210688, slot=2, args=(11215352, 11218513))
    RunEvent(11210688, slot=3, args=(11215353, 11218514))
    RunEvent(11210688, slot=4, args=(11215354, 11218515))
    RunEvent(11210688, slot=5, args=(11215355, 11218516))
    RunEvent(11210890)
    RunEvent(11219877)
    RunEvent(11219121)
    RunEvent(11219122)
    RunEvent(11210702)
    RunEvent(11210829)
    RunEvent(11210832)


def Event11210702():
    """ 11210702: Event 11210702 """
    DisableNetworkSync()
    IfCharacterInsideRegion(-1, PLAYER, region=Boxes.Arena_1vs1_Small_Territory_4510)
    IfCharacterInsideRegion(-1, PLAYER, region=Boxes.Arena_2vs2_Small_Territory_4511)
    IfCharacterInsideRegion(-1, PLAYER, region=Boxes.Arena_BR_Small_Territory_4512)
    IfCharacterInsideRegion(-1, PLAYER, region=Boxes.Arena_1vs1_Large_Territory_4523)
    IfCharacterInsideRegion(-1, PLAYER, region=Boxes.Arena_2vs2_Large_Territory_4524)
    IfCharacterInsideRegion(-1, PLAYER, region=Boxes.Arena_BR_Large_Territory_4525)
    IfCharacterInsideRegion(-1, PLAYER, region=Boxes.Arena_3vs3_Large_Territory_4523)
    IfCharacterInsideRegion(-1, PLAYER, region=Boxes.Arena_BR6_Large_Territory_4523)
    IfCharacterInsideRegion(-1, PLAYER, region=Boxes.Arena_3vs3_Small_Territory_4510)
    IfCharacterInsideRegion(-1, PLAYER, region=Boxes.Arena_BR6_Small_Territory_4510)
    IfConditionTrue(1, input_condition=-1)
    IfFlagOff(1, 11215390)
    IfConditionTrue(0, input_condition=1)
    AddSpecialEffect(PLAYER, 101)
    AddSpecialEffect(PLAYER, 102)
    AddSpecialEffect(PLAYER, 103)
    AddSpecialEffect(PLAYER, 104)
    Restart()


def Event11210878():
    """ 11210878: Event 11210878 """
    DisableNetworkSync()
    IfCharacterInsideRegion(-1, PLAYER, region=Boxes.Arena_1vs1_Small_Territory_4510)
    IfCharacterInsideRegion(-1, PLAYER, region=Boxes.Arena_2vs2_Small_Territory_4511)
    IfCharacterInsideRegion(-1, PLAYER, region=Boxes.Arena_BR_Small_Territory_4512)
    IfCharacterInsideRegion(-1, PLAYER, region=Boxes.Arena_1vs1_Large_Territory_4523)
    IfCharacterInsideRegion(-1, PLAYER, region=Boxes.Arena_2vs2_Large_Territory_4524)
    IfCharacterInsideRegion(-1, PLAYER, region=Boxes.Arena_BR_Large_Territory_4525)
    IfCharacterInsideRegion(-1, PLAYER, region=Boxes.Arena_3vs3_Large_Territory_4523)
    IfCharacterInsideRegion(-1, PLAYER, region=Boxes.Arena_BR6_Large_Territory_4523)
    IfCharacterInsideRegion(-1, PLAYER, region=Boxes.Arena_3vs3_Small_Territory_4510)
    IfCharacterInsideRegion(-1, PLAYER, region=Boxes.Arena_BR6_Small_Territory_4510)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    AddSpecialEffect(PLAYER, 4610)
    SkipLinesIfFlagOn(1, 11215398)
    AddSpecialEffect(PLAYER, 4613)
    Wait(1.0)
    Restart()


def Event11215398():
    """ 11215398: Event 11215398 """
    DisableNetworkSync()
    IfCharacterInsideRegion(-1, PLAYER, region=Boxes.Arena_NoDead_TemporaryCancellation0)
    IfCharacterInsideRegion(-1, PLAYER, region=Boxes.Arena_NoDead_TemporaryCancellation1)
    IfConditionTrue(0, input_condition=-1)
    CancelSpecialEffect(PLAYER, 4613)
    Restart()


def Event11210876():
    """ 11210876: Event 11210876 """
    DisableNetworkSync()
    IfFlagOn(0, 11215394)
    Wait(5.0)
    DisableFlag(11215394)
    SkipLinesIfFlagOn(2, 11215391)
    DisableInvincibility(PLAYER)
    CancelSpecialEffect(PLAYER, 90000)
    Restart()


def Event11210800(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 11210800: Event 11210800 """
    DisableNetworkSync()
    IfCharacterInsideRegion(1, PLAYER, region=arg_0_3)
    IfFlagOff(1, 11215390)
    IfConditionTrue(0, input_condition=1)
    Unknown_2008_04()
    DisableFlagRange((11215350, 11215355))
    EnableFlag(arg_4_7)
    DisableAI(PLAYER)
    Unknown_2004_50()
    EqualRecovery()
    Unknown_2004_51(arg1=arg_8_11)
    IfFlagOff(0, arg_4_7)
    Restart()


def Event11210820(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11210820: Event 11210820 """
    IfMultiplayer(1)
    SkipLinesIfEqual(1, left=arg_0_3, right=11215350)
    IfClient(1)
    IfFlagOn(1, arg_0_3)
    IfTimeElapsed(1, 3.0)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(arg_4_7)
    RestartEvent(arg_8_11, slot=arg_12_15)
    Restart()


def Event11210825(_, arg_0_3: int, arg_4_7: int):
    """ 11210825: Event 11210825 """
    DisableNetworkSync()
    IfFlagOn(1, arg_0_3)
    IfTimeElapsed(1, 10.0)
    IfConditionTrue(0, input_condition=1)
    RestartIfFlagOn(arg_4_7)
    DisableFlag(arg_0_3)
    Restart()


def Event11210827(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11210827: Event 11210827 """
    IfCharacterInsideRegion(1, PLAYER, region=arg_12_15)
    IfFlagRangeAllOn(1, (arg_4_7, arg_8_11))
    IfCharacterInsideRegion(2, PLAYER, region=arg_12_15)
    IfMultiplayer(2)
    IfTrueFlagCountGreaterThanOrEqual(2, 2, (11215360, 11215365))
    IfFlagOff(2, 11215390)
    IfTimeElapsed(2, 40.0)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    DisableFlagRange((11218990, 11218999))
    EnableFlag(arg_0_3)
    RestartIfFlagOff(arg_0_3)


def Event11210828(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11210828: Event 11210828 """
    IfFlagOn(1, arg_4_7)
    IfFlagOn(1, arg_8_11)
    IfCharacterInsideRegion(1, PLAYER, region=arg_12_15)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((11218990, 11218999))
    EnableFlag(arg_0_3)
    RestartIfFlagOff(arg_0_3)


def Event11210829():
    """ 11210829: Event 11210829 """
    Unknown_3_23(condition=1, arg1=0, arg2=0)
    IfFlagOn(2, 11215390)
    IfFlagOff(2, 6990)
    IfConditionFalse(2, input_condition=1)
    IfConditionTrue(0, input_condition=2)
    EnableFlag(6990)
    Restart()


def Event11210832():
    """ 11210832: Event 11210832 """
    IfCharacterInsideRegion(-1, PLAYER, region=Boxes.Arena_BR_Large_Territory_4525)
    IfCharacterInsideRegion(-1, PLAYER, region=Boxes.Arena_2vs2_Large_Territory_4524)
    IfCharacterInsideRegion(-1, PLAYER, region=Boxes.Arena_1vs1_Large_Territory_4523)
    IfCharacterInsideRegion(-1, PLAYER, region=Boxes.Arena_BR6_Large_Territory_4523)
    IfCharacterInsideRegion(-1, PLAYER, region=Boxes.Arena_3vs3_Small_Territory_4510)
    IfCharacterInsideRegion(-1, PLAYER, region=Boxes.Arena_BR_Small_Territory_4512)
    IfCharacterInsideRegion(-1, PLAYER, region=Boxes.Arena_2vs2_Small_Territory_4511)
    IfCharacterInsideRegion(-1, PLAYER, region=Boxes.Arena_1vs1_Small_Territory_4510)
    IfCharacterInsideRegion(-1, PLAYER, region=Boxes.Arena_BR6_Small_Territory_4510)
    IfCharacterInsideRegion(-1, PLAYER, region=Boxes.Arena_3vs3_Large_Territory_4523)
    IfConditionTrue(1, input_condition=-1)
    IfSingleplayer(1)
    IfFlagOn(1, 6990)
    IfConditionTrue(0, input_condition=1)
    EqualRecovery()
    AddSpecialEffect(PLAYER, 101)
    AddSpecialEffect(PLAYER, 102)
    AddSpecialEffect(PLAYER, 103)
    AddSpecialEffect(PLAYER, 104)
    Restart()


def Event11210932():
    """ 11210932: Event 11210932 """
    DisableNetworkSync()
    IfFlagOn(1, 11215390)
    IfFlagRangeAllOff(1, (11215350, 11215355))
    IfConditionTrue(0, input_condition=1)
    DisableAI(PLAYER)
    DisplayBattlefieldMessage(150001, display_location_index=1)
    DisableFlagRange((6980, 6990))
    Wait(3.0)
    EnableAI(PLAYER)
    ArenaExitRequest()


def Event11210830():
    """ 11210830: Event 11210830 """
    IfFlagOn(-1, 11218990)
    IfFlagOn(-1, 11218991)
    IfFlagOn(-1, 11218992)
    IfFlagOn(-1, 11218993)
    IfFlagOn(-1, 11218994)
    IfFlagOn(-1, 11218995)
    IfFlagOn(-1, 11218996)
    IfFlagOn(-1, 11218997)
    IfFlagOn(-1, 11218998)
    IfFlagOn(-1, 11218999)
    IfConditionTrue(0, input_condition=-1)
    EnableFlag(11215340)
    DisableFlag(11215392)
    DisableFlag(11215395)
    DisableFlag(11215402)
    DisableFlag(11215405)
    DisableFlag(11218000)
    DisableFlag(11218001)
    EnableFlagRange((6980, 6989))
    DisableFlag(6990)
    Unknown_3_23(condition=3, arg1=0, arg2=0)
    SkipLinesIfConditionTrue(1, 3)
    DisableFlagRange((6980, 6989))
    IfCharacterInsideRegion(-2, PLAYER, region=Boxes.Arena_BR_Large_Territory_4525)
    IfCharacterInsideRegion(-2, PLAYER, region=Boxes.Arena_2vs2_Large_Territory_4524)
    IfCharacterInsideRegion(-2, PLAYER, region=Boxes.Arena_1vs1_Large_Territory_4523)
    IfCharacterInsideRegion(-2, PLAYER, region=Boxes.Arena_BR6_Large_Territory_4523)
    IfCharacterInsideRegion(-2, PLAYER, region=Boxes.Arena_3vs3_Small_Territory_4510)
    IfCharacterInsideRegion(-3, PLAYER, region=Boxes.Arena_BR_Small_Territory_4512)
    IfCharacterInsideRegion(-3, PLAYER, region=Boxes.Arena_2vs2_Small_Territory_4511)
    IfCharacterInsideRegion(-3, PLAYER, region=Boxes.Arena_1vs1_Small_Territory_4510)
    IfCharacterInsideRegion(-3, PLAYER, region=Boxes.Arena_BR6_Small_Territory_4510)
    IfCharacterInsideRegion(-3, PLAYER, region=Boxes.Arena_3vs3_Large_Territory_4523)
    SkipLinesIfConditionTrue(1, -2)
    SkipLines(2)
    EnableFlag(11218000)
    DisableFlagRange((6980, 6984))
    SkipLinesIfConditionTrue(1, -3)
    SkipLines(2)
    EnableFlag(11218001)
    DisableFlagRange((6985, 6989))
    SkipLinesIfFlagOn(2, 11218990)
    SkipLinesIfFlagOn(1, 11218991)
    SkipLines(5)
    EnableFlag(11215408)
    DisableFlagRange((6981, 6984))
    DisableFlagRange((6986, 6989))
    EnableFlag(11218348)
    EnableFlag(11218350)
    SkipLinesIfFlagOn(2, 11218992)
    SkipLinesIfFlagOn(1, 11218993)
    SkipLines(7)
    EnableFlag(11215392)
    DisableFlag(6980)
    DisableFlag(6985)
    DisableFlagRange((6982, 6984))
    DisableFlagRange((6987, 6989))
    EnableFlag(11218354)
    EnableFlag(11218355)
    SkipLinesIfFlagOn(2, 11218994)
    SkipLinesIfFlagOn(1, 11218995)
    SkipLines(6)
    EnableFlag(11215395)
    DisableFlagRange((6980, 6981))
    DisableFlagRange((6985, 6986))
    DisableFlagRange((6983, 6984))
    DisableFlagRange((6988, 6989))
    EnableFlagRange((11218348, 11218351))
    SkipLinesIfFlagOn(2, 11218996)
    SkipLinesIfFlagOn(1, 11218997)
    SkipLines(7)
    EnableFlag(11215402)
    DisableFlagRange((6980, 6982))
    DisableFlagRange((6985, 6987))
    DisableFlag(6984)
    DisableFlag(6989)
    EnableFlag(11218354)
    EnableFlag(11218355)
    SkipLinesIfFlagOn(2, 11218998)
    SkipLinesIfFlagOn(1, 11218999)
    SkipLines(4)
    EnableFlag(11215405)
    DisableFlagRange((6980, 6983))
    DisableFlagRange((6985, 6988))
    EnableFlagRange((11218348, 11218353))
    Wait(8.0)
    SkipLinesIfFlagOn(5, 11215402)
    SkipLinesIfFlagOn(4, 11215405)
    SkipLinesIfFlagOn(3, 11215395)
    SkipLinesIfFlagOn(2, 11215392)
    DisplayBattlefieldMessage(150215, display_location_index=1)
    SkipLines(1)
    DisplayBattlefieldMessage(150205, display_location_index=1)
    Wait(2.0)
    DisplayBanner(BannerType.BeginMatch)
    EnableFlag(11215390)
    IfFlagOff(0, 11215390)
    Restart()


def Event11210831(_, arg_0_3: int, arg_4_7: int):
    """ 11210831: Event 11210831 """
    IfHost(1)
    IfFlagOn(1, 11215390)
    IfFlagOff(1, arg_0_3)
    IfFlagOn(1, arg_4_7)
    IfConditionTrue(0, input_condition=1)
    SkipLinesIfFlagOn(2, 11215402)
    SkipLinesIfFlagOn(1, 11215392)
    DisableFlag(arg_4_7)
    Restart()


def Event11210835(_, arg_0_3: float, arg_4_7: float, arg_8_11: float, arg_12_15: float):
    """ 11210835: Event 11210835 """
    DisableNetworkSync()
    IfHost(1)
    IfFlagOff(1, 11215391)
    IfFlagOn(1, 11215390)
    IfConditionTrue(0, input_condition=1)
    SkipLinesIfFlagOn(5, 11215405)
    SkipLinesIfFlagOn(4, 11215402)
    SkipLinesIfFlagOn(3, 11215395)
    SkipLinesIfFlagOn(2, 11215392)
    Wait(arg_0_3)
    SkipLines(1)
    Wait(arg_8_11)
    SkipLinesIfFlagOn(1, 904)
    EnableFlag(11215396)
    SkipLinesIfFlagOn(5, 11215405)
    SkipLinesIfFlagOn(4, 11215402)
    SkipLinesIfFlagOn(3, 11215395)
    SkipLinesIfFlagOn(2, 11215392)
    Wait(arg_4_7)
    SkipLines(1)
    Wait(arg_12_15)
    IfFlagOff(0, 904)
    EnableFlag(11215391)
    Restart()


def Event11210836():
    """ 11210836: Event 11210836 """
    IfFlagOn(0, 11215396)
    EnableFlag(11215396)
    DisplayBattlefieldMessage(150110, display_location_index=0)
    IfFlagOn(0, 11215391)
    EnableFlag(11215391)
    DisplayBattlefieldMessage(150300, display_location_index=0)
    IfFlagOff(0, 11215391)
    Restart()


def Event11210887(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int):
    """ 11210887: Event 11210887 """
    DisableNetworkSync()
    IfFlagOn(1, 11215390)
    IfFlagOff(1, 11215391)
    IfFlagOn(1, arg_0_3)
    IfConditionTrue(0, input_condition=1)
    Unknown_4_15(0, arg1=1)
    SkipLinesIfFlagOn(4, 11215392)
    SkipLinesIfFlagOn(3, 11215402)
    SkipLinesIfFlagOff(2, arg_16_19)
    EqualRecovery()
    Unknown_2004_51(arg1=1)
    IfFlagOff(2, 11215392)
    IfFlagOff(2, 11215402)
    SkipLinesIfConditionTrue(1, 2)
    Unknown_2004_51(arg1=1)
    EnableFlag(arg_4_7)
    SkipLinesIfFlagOn(2, 11215395)
    SkipLinesIfFlagOn(1, 11215405)
    EnableFlag(arg_8_11)
    SkipLinesIfFlagOn(1, 11215408)
    EnableFlag(arg_12_15)
    IfFlagOff(0, arg_4_7)
    DisableFlag(arg_4_7)
    DisableFlag(arg_8_11)
    Restart()


def Event11210889(_, arg_0_3: int):
    """ 11210889: Event 11210889 """
    IfFlagOff(0, arg_0_3)
    DisableFlag(arg_0_3)
    IfFlagOn(0, arg_0_3)
    Restart()


def Event11210888(_, arg_0_3: int, arg_4_7: int):
    """ 11210888: Event 11210888 """
    IfFlagOn(1, arg_0_3)
    IfFlagOff(1, 11215391)
    IfFlagOn(1, 11215390)
    IfConditionTrue(0, input_condition=1)
    IncrementEventValue(arg_4_7, bit_count=6, max_value=63)
    DisableFlag(arg_0_3)
    Restart()


def Event11210891(
    _,
    arg_0_3: int,
    arg_4_7: int,
    arg_8_11: int,
    arg_12_15: int,
    arg_16_19: int,
    arg_20_23: int,
    arg_24_27: int,
):
    """ 11210891: Event 11210891 """
    IfFlagOn(1, arg_0_3)
    IfFlagOn(1, arg_4_7)
    IfFlagOff(1, arg_8_11)
    IfFlagOff(1, arg_12_15)
    IfFlagOff(1, arg_16_19)
    IfFlagOff(1, arg_20_23)
    IfFlagOff(1, arg_24_27)
    IfConditionTrue(0, input_condition=1)
    Unknown_2007_13(arg1=10000)
    Restart()


def Event11210892(
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
    """ 11210892: Event 11210892 """
    IfFlagOn(1, 11215390)
    IfFlagOff(1, 11215391)
    IfFlagOff(1, 11215392)
    IfFlagOff(1, 11215402)
    IfFlagOn(1, arg_0_3)
    IfEventsComparison(-1, arg_4_7, 6, ComparisonType.LessThan, arg_8_11, 6)
    IfEventsComparison(-1, arg_4_7, 6, ComparisonType.LessThan, arg_12_15, 6)
    IfEventsComparison(-1, arg_4_7, 6, ComparisonType.LessThan, arg_16_19, 6)
    IfEventsComparison(-1, arg_4_7, 6, ComparisonType.LessThan, arg_20_23, 6)
    IfEventsComparison(-1, arg_4_7, 6, ComparisonType.LessThan, arg_24_27, 6)
    IfConditionFalse(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(arg_28_31)
    Restart()


def Event11210893():
    """ 11210893: Event 11210893 """
    IfFlagOn(0, 11218360)
    WaitFrames(6)
    DisableFlag(11218360)
    Restart()


def Event11210894(
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
    """ 11210894: Event 11210894 """
    IfFlagOn(1, 11215390)
    IfFlagOff(1, 11215391)
    IfFlagOff(1, 11215392)
    IfFlagOff(1, 11215402)
    IfFlagOn(1, arg_0_3)
    IfEventsComparison(-1, arg_4_7, 6, ComparisonType.LessThan, arg_8_11, 6)
    IfEventsComparison(-1, arg_4_7, 6, ComparisonType.LessThan, arg_12_15, 6)
    IfEventsComparison(-1, arg_4_7, 6, ComparisonType.LessThan, arg_16_19, 6)
    IfEventsComparison(-1, arg_4_7, 6, ComparisonType.LessThan, arg_20_23, 6)
    IfEventsComparison(-1, arg_4_7, 6, ComparisonType.LessThan, arg_24_27, 6)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    DisableFlag(arg_28_31)
    Restart()


def Event11210895(_, arg_0_3: int, arg_4_7: int):
    """ 11210895: Event 11210895 """
    DisableNetworkSync()
    IfFlagOff(1, 11215392)
    IfFlagOff(1, 11215402)
    IfFlagOn(1, 11215390)
    IfFlagOff(1, 11215391)
    IfFlagOn(1, arg_0_3)
    IfFlagOn(1, arg_4_7)
    IfConditionTrue(0, input_condition=1)
    EqualRecovery()
    Unknown_2004_51(arg1=1)
    DisableFlag(arg_4_7)
    Restart()


def Event11212222(
    _,
    arg_0_3: int,
    arg_4_7: int,
    arg_8_11: int,
    arg_12_15: int,
    arg_16_19: int,
    arg_20_23: int,
    arg_24_27: int,
):
    """ 11212222: Event 11212222 """
    IfFlagOn(1, arg_0_3)
    IfHealthValueEqual(1, PLAYER, 1)
    IfConditionTrue(0, input_condition=1)
    Unknown_4_16(2, arg1=0, arg2=0, arg3=0)
    SkipLinesIfConditionTrue(2, 2)
    WaitFrames(7)
    Restart()
    SkipLinesIfFlagOn(7, 11215392)
    SkipLinesIfFlagOn(6, 11215402)
    EnableFlag(arg_8_11)
    SkipLinesIfFlagOn(6, 11215408)
    EnableFlag(arg_4_7)
    EnableFlag(arg_12_15)
    EnableFlag(arg_16_19)
    EnableFlag(arg_20_23)
    SkipLinesIfFlagOn(2, 11215395)
    SkipLinesIfFlagOn(1, 11215405)
    EnableFlag(arg_24_27)
    WaitFrames(7)
    Restart()


def Event11210840(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 11210840: Event 11210840 """
    IfFlagOn(1, arg_0_3)
    IfFlagOn(1, 11215390)
    IfFlagOff(1, 11215391)
    IfHealthValueEqual(1, PLAYER, 1)
    IfConditionTrue(0, input_condition=1)
    EnableInvincibility(PLAYER)
    AddSpecialEffect(PLAYER, 90001)
    AddSpecialEffect(PLAYER, 101)
    AddSpecialEffect(PLAYER, 102)
    AddSpecialEffect(PLAYER, 103)
    AddSpecialEffect(PLAYER, 104)
    AddSpecialEffect(PLAYER, 4611)
    SkipLinesIfFlagOff(1, arg_0_3)
    DisplayBattlefieldMessage(506107, display_location_index=3)
    EnableFlag(arg_4_7)
    EnableFlag(arg_8_11)
    IfFlagOff(0, arg_8_11)
    DisableFlag(arg_8_11)
    SkipLinesIfFlagOn(1, arg_0_3)
    DisableInvincibility(PLAYER)
    CancelSpecialEffect(PLAYER, 4611)
    ResetAnimation(PLAYER, disable_interpolation=True)
    SkipLinesIfFlagOn(2, arg_0_3)
    ForceAnimation_WithUnknownEffect1(
        PLAYER,
        animation=6951,
        loop=False,
        wait_for_completion=True,
        skip_transition=False,
        arg1=0,
    )
    SkipLines(1)
    ForceAnimation_WithUnknownEffect1(
        PLAYER,
        animation=6951,
        loop=False,
        wait_for_completion=True,
        skip_transition=False,
        arg1=0,
    )
    ResetAnimation(PLAYER, disable_interpolation=True)
    DisableFlag(arg_4_7)
    Restart()


def Event11210833():
    """ 11210833: Event 11210833 """
    DisableNetworkSync()
    IfHealthValueEqual(0, PLAYER, 1)
    WaitFrames(6)
    EqualRecovery()
    SkipLinesIfFlagOn(1, 11215408)
    Unknown_2004_51(arg1=1)
    Restart()


def Event11210777(_, arg_0_3: int, arg_4_7: int):
    """ 11210777: Event 11210777 """
    IfFlagOn(1, 11215390)
    IfFlagOff(1, 11215391)
    IfFlagOn(1, arg_0_3)
    IfFlagOn(1, arg_4_7)
    IfConditionTrue(0, input_condition=1)
    Wait(2.0)
    IfFlagOff(2, arg_4_7)
    IfFlagOn(2, arg_0_3)
    IfFramesElapsed(2, 120)
    IfConditionTrue(0, input_condition=2)
    SkipLinesIfFlagOn(2, arg_0_3)
    CreateTemporaryVFX(20176, anchor_entity=PLAYER, anchor_type=CoordEntityType.Character, model_point=220)
    SkipLines(1)
    Unknown_2003_48(
        entity=PLAYER,
        arg1=0,
        model_point=220,
        magic_id=5310,
        shoot_angle_x=0,
        shoot_angle_y=0,
        shoot_angle_z=0,
    )
    Restart()


def Event11210850(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int):
    """ 11210850: Event 11210850 """
    DisableNetworkSync()
    IfFlagOn(1, arg_0_3)
    IfFlagOn(1, arg_4_7)
    IfCharacterInsideRegion(1, PLAYER, region=arg_8_11)
    IfConditionTrue(0, input_condition=1)
    DisableAI(PLAYER)
    Wait(2.0)
    SkipLinesIfFlagOn(3, 11215392)
    SkipLinesIfFlagOn(2, 11215402)
    PlayCutsceneAndRandomlyWarpPlayer_WithUnknownEffect1(
        120130,
        CutsceneType.Unskippable,
        first_region=arg_12_15,
        last_region=arg_16_19,
        game_map=OOLACILE,
    )
    SkipLines(1)
    PlayCutsceneAndRandomlyWarpPlayer_WithUnknownEffect2(
        120130,
        CutsceneType.Unskippable,
        first_region=arg_12_15,
        last_region=arg_16_19,
        game_map=OOLACILE,
    )
    WaitFrames(1)
    EnableAI(PLAYER)
    EqualRecovery()
    SkipLinesIfFlagOn(1, 11215408)
    Unknown_2004_51(arg1=1)
    DisableFlag(arg_4_7)
    Wait(6.0)
    CancelSpecialEffect(PLAYER, 90001)
    DisableInvincibility(PLAYER)
    Restart()


def Event11210886(_, arg_0_3: int, arg_4_7: int):
    """ 11210886: Event 11210886 """
    IfFlagOn(1, arg_0_3)
    IfFlagOn(1, arg_4_7)
    IfConditionTrue(0, input_condition=1)
    FadeOutCharacter(PLAYER, duration=2.0)
    IfFlagOn(2, arg_0_3)
    IfFlagOff(2, arg_4_7)
    IfTimeElapsed(2, 3.0)
    IfConditionTrue(0, input_condition=2)
    FadeInCharacter(PLAYER, duration=1.0)
    Restart()


def Event11210688(_, arg_0_3: int, arg_4_7: int):
    """ 11210688: Event 11210688 """
    IfFlagOn(1, arg_0_3)
    IfFlagOn(1, arg_4_7)
    IfConditionTrue(0, input_condition=1)
    IfFlagOn(2, arg_0_3)
    IfFramesElapsed(2, 30)
    IfConditionTrue(0, input_condition=2)
    CancelSpecialEffect(PLAYER, 4611)
    IfFlagOn(3, arg_0_3)
    IfFlagOff(3, arg_4_7)
    IfConditionTrue(0, input_condition=3)
    Restart()


def Event11210870(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11210870: Event 11210870 """
    DisableNetworkSync()
    Unknown_3_23(condition=7, arg1=0, arg2=0)
    SkipLinesIfConditionFalse(1, 7)
    EnableFlag(11219000)
    IfFlagOn(1, arg_0_3)
    IfFlagOn(1, 11215390)
    IfFlagOn(1, 11215391)
    IfConditionTrue(0, input_condition=1)
    EnableInvincibility(PLAYER)
    AddSpecialEffect(PLAYER, 90000)
    Wait(6.0)
    EnableFlag(11215397)
    SkipLinesIfFlagOn(2, 11215392)
    SkipLinesIfFlagOn(1, 11215402)
    IfFlagOn(3, arg_4_7)
    SkipLinesIfFlagOn(3, 11215408)
    SkipLinesIfFlagOn(2, 11215405)
    SkipLinesIfFlagOn(1, 11215395)
    IfFlagOn(3, arg_8_11)
    SkipLinesIfFlagOn(2, 11215392)
    SkipLinesIfFlagOn(1, 11215402)
    IfFlagOff(5, arg_4_7)
    SkipLinesIfFlagOn(3, 11215408)
    SkipLinesIfFlagOn(2, 11215405)
    SkipLinesIfFlagOn(1, 11215395)
    IfFlagOff(5, arg_8_11)
    SkipLinesIfFlagOn(13, 11215402)
    SkipLinesIfFlagOn(12, 11215392)
    SkipLinesIfFlagOn(1, 11215350)
    IfFlagOn(-1, 11218348)
    SkipLinesIfFlagOn(1, 11215351)
    IfFlagOn(-1, 11218349)
    SkipLinesIfFlagOn(1, 11215352)
    IfFlagOn(-1, 11218350)
    SkipLinesIfFlagOn(1, 11215353)
    IfFlagOn(-1, 11218351)
    SkipLinesIfFlagOn(1, 11215354)
    IfFlagOn(-1, 11218352)
    SkipLinesIfFlagOn(1, 11215355)
    IfFlagOn(-1, 11218353)
    SkipLinesIfFlagOn(3, 11215408)
    SkipLinesIfFlagOn(2, 11215395)
    SkipLinesIfFlagOn(1, 11215405)
    IfFlagOn(-1, arg_12_15)
    IfConditionTrue(6, input_condition=3)
    IfConditionTrue(6, input_condition=-1)
    IfConditionTrue(2, input_condition=3)
    IfConditionFalse(2, input_condition=-1)
    SkipLinesIfFlagRangeAllOff(1, (11218342, 11218347))
    DisplayBattlefieldMessage(150420, display_location_index=3)
    SkipLinesIfConditionTrue(3, 2)
    SkipLinesIfConditionTrue(17, 5)
    SkipLinesIfConditionTrue(9, 6)
    SkipLines(8)
    EnableFlag(11215393)
    DisplayBanner(BannerType.YouWin)
    Wait(2.0)
    SkipLinesIfFlagOff(1, 11219000)
    DisplayBattlefieldMessage(150050, display_location_index=1)
    SkipLinesIfFlagOn(1, 11219000)
    DisplayBattlefieldMessage(150051, display_location_index=1)
    SkipLines(38)
    DisplayBanner(BannerType.Draw)
    Wait(2.0)
    SkipLinesIfFlagOff(1, 11219000)
    DisplayBattlefieldMessage(150055, display_location_index=1)
    SkipLinesIfFlagOn(1, 11219000)
    DisplayBattlefieldMessage(150056, display_location_index=1)
    SkipLines(7)
    RunEvent(11210871)
    DisplayBanner(BannerType.YouLose)
    Wait(2.0)
    SkipLinesIfFlagOff(1, 11219000)
    DisplayBattlefieldMessage(150060, display_location_index=1)
    SkipLinesIfFlagOn(1, 11219000)
    DisplayBattlefieldMessage(150061, display_location_index=1)
    SkipLinesIfConditionTrue(1, 5)
    SkipLines(10)
    SkipLinesIfFlagOff(1, 11215408)
    Unknown_2003_43(flag=6040, bit_count=10, arg1=0, arg2=2)
    SkipLinesIfFlagOff(1, 11215392)
    Unknown_2003_43(flag=6090, bit_count=10, arg1=1, arg2=2)
    SkipLinesIfFlagOff(1, 11215402)
    Unknown_2003_43(flag=6140, bit_count=10, arg1=2, arg2=2)
    SkipLinesIfFlagOff(1, 11215395)
    Unknown_2003_43(flag=6190, bit_count=10, arg1=3, arg2=2)
    SkipLinesIfFlagOff(1, 11215405)
    Unknown_2003_43(flag=6240, bit_count=10, arg1=4, arg2=2)
    SkipLinesIfConditionTrue(1, -1)
    SkipLines(10)
    SkipLinesIfFlagOff(1, 11215408)
    Unknown_2003_43(flag=6040, bit_count=10, arg1=0, arg2=1)
    SkipLinesIfFlagOff(1, 11215392)
    Unknown_2003_43(flag=6090, bit_count=10, arg1=1, arg2=1)
    SkipLinesIfFlagOff(1, 11215402)
    Unknown_2003_43(flag=6140, bit_count=10, arg1=2, arg2=1)
    SkipLinesIfFlagOff(1, 11215395)
    Unknown_2003_43(flag=6190, bit_count=10, arg1=3, arg2=1)
    SkipLinesIfFlagOff(1, 11215405)
    Unknown_2003_43(flag=6240, bit_count=10, arg1=4, arg2=1)
    Wait(8.0)
    EnableFlag(11215891)
    DisableInvincibility(PLAYER)
    Unknown_2004_52()
    EqualRecovery()
    CancelSpecialEffect(PLAYER, 90000)
    CancelSpecialEffect(PLAYER, 4612)
    CancelSpecialEffect(PLAYER, 4614)
    CancelSpecialEffect(PLAYER, 4615)
    CancelSpecialEffect(PLAYER, 4616)
    CancelSpecialEffect(PLAYER, 4617)
    CancelSpecialEffect(PLAYER, 4618)
    ArenaExitRequest()
    DisableFlag(11219000)
    EnableFlag(11218900)


def Event11210871():
    """ 11210871: Event 11210871 """
    SkipLinesIfFlagOff(3, 11215408)
    DisableFlagRange((7040, 7049))
    DisableFlagRange((7250, 7299))
    DisableFlagRange((7500, 7549))
    SkipLinesIfFlagOff(3, 11215392)
    DisableFlagRange((7090, 7099))
    DisableFlagRange((7300, 7349))
    DisableFlagRange((7550, 7599))
    SkipLinesIfFlagOff(3, 11215402)
    DisableFlagRange((7140, 7149))
    DisableFlagRange((7350, 7399))
    DisableFlagRange((7600, 7649))
    SkipLinesIfFlagOff(3, 11215395)
    DisableFlagRange((7190, 7199))
    DisableFlagRange((7400, 7449))
    DisableFlagRange((7650, 7699))
    SkipLinesIfFlagOff(3, 11215405)
    DisableFlagRange((7240, 7249))
    DisableFlagRange((7450, 7499))
    DisableFlagRange((7700, 7749))


def Event11210875(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 11210875: Event 11210875 """
    IfCharacterInsideRegion(2, PLAYER, region=Boxes.Arena_StreakDisplay)
    IfFlagOn(2, arg_0_3)
    IfConditionTrue(0, input_condition=2)
    DisableFlag(arg_0_3)
    EqualRecovery()
    AddSpecialEffect(PLAYER, 101)
    AddSpecialEffect(PLAYER, 102)
    AddSpecialEffect(PLAYER, 103)
    AddSpecialEffect(PLAYER, 104)
    Wait(0.0)
    SkipLinesIfEqual(1, left=arg_0_3, right=6990)
    DisplayConcatenatedMessage(message_id=arg_4_7, pad_enabled=True, concatenator_base_flag=arg_8_11, bit_count=10)
    Restart()


def Event11210705():
    """ 11210705: Event 11210705 """
    DisableNetworkSync()
    IfFlagOff(1, 11215392)
    IfFlagOff(1, 11215395)
    IfFlagOn(1, 11215393)
    IfConditionTrue(0, input_condition=1)
    SkipLinesIfFlagOff(2, 11215380)
    IncrementEventValue(7000, bit_count=10, max_value=1000)
    IfEventsComparison(2, 7000, 10, ComparisonType.GreaterThan, 6000, 10)
    SkipLinesIfFlagOff(2, 11215381)
    IncrementEventValue(7050, bit_count=10, max_value=1000)
    IfEventsComparison(2, 7050, 10, ComparisonType.GreaterThan, 6050, 10)
    SkipLinesIfFlagOff(2, 11215382)
    IncrementEventValue(7100, bit_count=10, max_value=1000)
    IfEventsComparison(2, 7100, 10, ComparisonType.GreaterThan, 6100, 10)
    SkipLinesIfFlagOff(2, 11215383)
    IncrementEventValue(7150, bit_count=10, max_value=1000)
    IfEventsComparison(2, 7150, 10, ComparisonType.GreaterThan, 6150, 10)
    IncrementEventValue(7200, bit_count=10, max_value=1000)
    SkipLinesIfConditionTrue(3, 2)
    ArenaRankingRequest1v1()
    DisableFlag(11215393)
    Restart()
    SkipLinesIfFlagOff(1, 11215380)
    IncrementEventValue(6000, bit_count=10, max_value=1000)
    SkipLinesIfFlagOff(1, 11215381)
    IncrementEventValue(6050, bit_count=10, max_value=1000)
    SkipLinesIfFlagOff(1, 11215382)
    IncrementEventValue(6100, bit_count=10, max_value=1000)
    SkipLinesIfFlagOff(1, 11215383)
    IncrementEventValue(6150, bit_count=10, max_value=1000)
    IfEventsComparison(3, 7200, 10, ComparisonType.GreaterThan, 6200, 10)
    SkipLinesIfConditionFalse(1, 3)
    IncrementEventValue(6200, bit_count=10, max_value=1000)
    ArenaRankingRequest1v1()
    DisableFlag(11215393)
    Restart()


def Event11210706():
    """ 11210706: Event 11210706 """
    DisableNetworkSync()
    IfFlagOn(1, 11215392)
    IfFlagOff(1, 11215395)
    IfFlagOn(1, 11215393)
    IfConditionTrue(0, input_condition=1)
    SkipLinesIfFlagOff(2, 11215380)
    IncrementEventValue(7250, bit_count=10, max_value=1000)
    IfEventsComparison(2, 7250, 10, ComparisonType.GreaterThan, 6250, 10)
    SkipLinesIfFlagOff(2, 11215381)
    IncrementEventValue(7300, bit_count=10, max_value=1000)
    IfEventsComparison(2, 7300, 10, ComparisonType.GreaterThan, 6300, 10)
    SkipLinesIfFlagOff(2, 11215382)
    IncrementEventValue(7350, bit_count=10, max_value=1000)
    IfEventsComparison(2, 7350, 10, ComparisonType.GreaterThan, 6350, 10)
    SkipLinesIfFlagOff(2, 11215383)
    IncrementEventValue(7400, bit_count=10, max_value=1000)
    IfEventsComparison(2, 7400, 10, ComparisonType.GreaterThan, 6400, 10)
    IncrementEventValue(7450, bit_count=10, max_value=1000)
    SkipLinesIfConditionTrue(3, 2)
    ArenaRankingRequest2v2()
    DisableFlag(11215393)
    Restart()
    SkipLinesIfFlagOff(1, 11215380)
    IncrementEventValue(6250, bit_count=10, max_value=1000)
    SkipLinesIfFlagOff(1, 11215381)
    IncrementEventValue(6300, bit_count=10, max_value=1000)
    SkipLinesIfFlagOff(1, 11215382)
    IncrementEventValue(6350, bit_count=10, max_value=1000)
    SkipLinesIfFlagOff(1, 11215383)
    IncrementEventValue(6400, bit_count=10, max_value=1000)
    IfEventsComparison(3, 7450, 10, ComparisonType.GreaterThan, 6450, 10)
    SkipLinesIfConditionFalse(1, 3)
    IncrementEventValue(6450, bit_count=10, max_value=1000)
    ArenaRankingRequest2v2()
    DisableFlag(11215393)
    Restart()


def Event11210707():
    """ 11210707: Event 11210707 """
    DisableNetworkSync()
    IfFlagOff(1, 11215392)
    IfFlagOn(1, 11215395)
    IfFlagOn(1, 11215393)
    IfConditionTrue(0, input_condition=1)
    SkipLinesIfFlagOff(2, 11215380)
    IncrementEventValue(7500, bit_count=10, max_value=1000)
    IfEventsComparison(2, 7500, 10, ComparisonType.GreaterThan, 6500, 10)
    SkipLinesIfFlagOff(2, 11215381)
    IncrementEventValue(7550, bit_count=10, max_value=1000)
    IfEventsComparison(2, 7550, 10, ComparisonType.GreaterThan, 6550, 10)
    SkipLinesIfFlagOff(2, 11215382)
    IncrementEventValue(7600, bit_count=10, max_value=1000)
    IfEventsComparison(2, 7600, 10, ComparisonType.GreaterThan, 6600, 10)
    SkipLinesIfFlagOff(2, 11215383)
    IncrementEventValue(7650, bit_count=10, max_value=1000)
    IfEventsComparison(2, 7650, 10, ComparisonType.GreaterThan, 6650, 10)
    IncrementEventValue(7700, bit_count=10, max_value=1000)
    SkipLinesIfConditionTrue(3, 2)
    ArenaRankingRequestFFA()
    DisableFlag(11215393)
    Restart()
    SkipLinesIfFlagOff(1, 11215380)
    IncrementEventValue(6500, bit_count=10, max_value=1000)
    SkipLinesIfFlagOff(1, 11215381)
    IncrementEventValue(6550, bit_count=10, max_value=1000)
    SkipLinesIfFlagOff(1, 11215382)
    IncrementEventValue(6600, bit_count=10, max_value=1000)
    SkipLinesIfFlagOff(1, 11215383)
    IncrementEventValue(6650, bit_count=10, max_value=1000)
    IfEventsComparison(3, 7700, 10, ComparisonType.GreaterThan, 6700, 10)
    SkipLinesIfConditionFalse(1, 3)
    IncrementEventValue(6700, bit_count=10, max_value=1000)
    ArenaRankingRequestFFA()
    DisableFlag(11215393)
    Restart()


def Event11210727():
    """ 11210727: Event 11210727 """
    DisableNetworkSync()
    Unknown_3_23(condition=1, arg1=0, arg2=0)
    EndIfConditionFalse(1)
    IfFlagOn(0, 11215393)
    SkipLinesIfFlagOff(55, 11218001)
    SkipLinesIfFlagOff(10, 11215408)
    IncrementEventValue(7290, bit_count=10, max_value=1000)
    CopyEventValue(source_flag=7290, destination_flag=7040, bit_count=10)
    SkipLinesIfFlagOff(1, 11215380)
    RunEvent(11210717, slot=0, args=(7250, 6250, 0, 7290, 6290, 6040, 6000), arg_types="iiBiiii")
    SkipLinesIfFlagOff(1, 11215381)
    RunEvent(11210717, slot=0, args=(7260, 6260, 0, 7290, 6290, 6040, 6010), arg_types="iiBiiii")
    SkipLinesIfFlagOff(1, 11215382)
    RunEvent(11210717, slot=0, args=(7270, 6270, 0, 7290, 6290, 6040, 6020), arg_types="iiBiiii")
    SkipLinesIfFlagOff(1, 11215383)
    RunEvent(11210717, slot=0, args=(7280, 6280, 0, 7290, 6290, 6040, 6030), arg_types="iiBiiii")
    SkipLinesIfFlagOff(10, 11215392)
    IncrementEventValue(7340, bit_count=10, max_value=1000)
    CopyEventValue(source_flag=7340, destination_flag=7090, bit_count=10)
    SkipLinesIfFlagOff(1, 11215380)
    RunEvent(11210717, slot=0, args=(7300, 6300, 1, 7340, 6340, 6090, 6050), arg_types="iiBiiii")
    SkipLinesIfFlagOff(1, 11215381)
    RunEvent(11210717, slot=0, args=(7310, 6310, 1, 7340, 6340, 6090, 6060), arg_types="iiBiiii")
    SkipLinesIfFlagOff(1, 11215382)
    RunEvent(11210717, slot=0, args=(7320, 6320, 1, 7340, 6340, 6090, 6070), arg_types="iiBiiii")
    SkipLinesIfFlagOff(1, 11215383)
    RunEvent(11210717, slot=0, args=(7330, 6330, 1, 7340, 6340, 6090, 6080), arg_types="iiBiiii")
    SkipLinesIfFlagOff(10, 11215402)
    IncrementEventValue(7390, bit_count=10, max_value=1000)
    CopyEventValue(source_flag=7390, destination_flag=7140, bit_count=10)
    SkipLinesIfFlagOff(1, 11215380)
    RunEvent(11210717, slot=0, args=(7350, 6350, 2, 7390, 6390, 6140, 6100), arg_types="iiBiiii")
    SkipLinesIfFlagOff(1, 11215381)
    RunEvent(11210717, slot=0, args=(7360, 6360, 2, 7390, 6390, 6140, 6110), arg_types="iiBiiii")
    SkipLinesIfFlagOff(1, 11215382)
    RunEvent(11210717, slot=0, args=(7370, 6370, 2, 7390, 6390, 6140, 6120), arg_types="iiBiiii")
    SkipLinesIfFlagOff(1, 11215383)
    RunEvent(11210717, slot=0, args=(7380, 6380, 2, 7390, 6390, 6140, 6130), arg_types="iiBiiii")
    SkipLinesIfFlagOff(10, 11215395)
    IncrementEventValue(7440, bit_count=10, max_value=1000)
    CopyEventValue(source_flag=7440, destination_flag=7190, bit_count=10)
    SkipLinesIfFlagOff(1, 11215380)
    RunEvent(11210717, slot=0, args=(7400, 6400, 3, 7440, 6440, 6190, 6150), arg_types="iiBiiii")
    SkipLinesIfFlagOff(1, 11215381)
    RunEvent(11210717, slot=0, args=(7410, 6410, 3, 7440, 6440, 6190, 6160), arg_types="iiBiiii")
    SkipLinesIfFlagOff(1, 11215382)
    RunEvent(11210717, slot=0, args=(7420, 6420, 3, 7440, 6440, 6190, 6170), arg_types="iiBiiii")
    SkipLinesIfFlagOff(1, 11215383)
    RunEvent(11210717, slot=0, args=(7430, 6430, 3, 7440, 6440, 6190, 6180), arg_types="iiBiiii")
    SkipLinesIfFlagOff(10, 11215405)
    IncrementEventValue(7490, bit_count=10, max_value=1000)
    CopyEventValue(source_flag=7490, destination_flag=7240, bit_count=10)
    SkipLinesIfFlagOff(1, 11215380)
    RunEvent(11210717, slot=0, args=(7450, 6450, 4, 7490, 6490, 6240, 6200), arg_types="iiBiiii")
    SkipLinesIfFlagOff(1, 11215381)
    RunEvent(11210717, slot=0, args=(7460, 6460, 4, 7490, 6490, 6240, 6210), arg_types="iiBiiii")
    SkipLinesIfFlagOff(1, 11215382)
    RunEvent(11210717, slot=0, args=(7470, 6470, 4, 7490, 6490, 6240, 6220), arg_types="iiBiiii")
    SkipLinesIfFlagOff(1, 11215383)
    RunEvent(11210717, slot=0, args=(7480, 6480, 4, 7490, 6490, 6240, 6230), arg_types="iiBiiii")
    SkipLinesIfFlagOff(55, 11218000)
    SkipLinesIfFlagOff(10, 11215408)
    IncrementEventValue(7540, bit_count=10, max_value=1000)
    CopyEventValue(source_flag=7540, destination_flag=7040, bit_count=10)
    SkipLinesIfFlagOff(1, 11215380)
    RunEvent(11210717, slot=0, args=(7500, 6500, 0, 7540, 6540, 6040, 6000), arg_types="iiBiiii")
    SkipLinesIfFlagOff(1, 11215381)
    RunEvent(11210717, slot=0, args=(7510, 6510, 0, 7540, 6540, 6040, 6010), arg_types="iiBiiii")
    SkipLinesIfFlagOff(1, 11215382)
    RunEvent(11210717, slot=0, args=(7520, 6520, 0, 7540, 6540, 6040, 6020), arg_types="iiBiiii")
    SkipLinesIfFlagOff(1, 11215383)
    RunEvent(11210717, slot=0, args=(7530, 6530, 0, 7540, 6540, 6040, 6030), arg_types="iiBiiii")
    SkipLinesIfFlagOff(10, 11215392)
    IncrementEventValue(7590, bit_count=10, max_value=1000)
    CopyEventValue(source_flag=7590, destination_flag=7090, bit_count=10)
    SkipLinesIfFlagOff(1, 11215380)
    RunEvent(11210717, slot=0, args=(7550, 6550, 1, 7590, 6590, 6090, 6050), arg_types="iiBiiii")
    SkipLinesIfFlagOff(1, 11215381)
    RunEvent(11210717, slot=0, args=(7560, 6560, 1, 7590, 6590, 6090, 6060), arg_types="iiBiiii")
    SkipLinesIfFlagOff(1, 11215382)
    RunEvent(11210717, slot=0, args=(7570, 6570, 1, 7590, 6590, 6090, 6070), arg_types="iiBiiii")
    SkipLinesIfFlagOff(1, 11215383)
    RunEvent(11210717, slot=0, args=(7580, 6580, 1, 7590, 6590, 6090, 6080), arg_types="iiBiiii")
    SkipLinesIfFlagOff(10, 11215402)
    IncrementEventValue(7640, bit_count=10, max_value=1000)
    CopyEventValue(source_flag=7640, destination_flag=7140, bit_count=10)
    SkipLinesIfFlagOff(1, 11215380)
    RunEvent(11210717, slot=0, args=(7600, 6600, 2, 7640, 6640, 6140, 6100), arg_types="iiBiiii")
    SkipLinesIfFlagOff(1, 11215381)
    RunEvent(11210717, slot=0, args=(7610, 6610, 2, 7640, 6640, 6140, 6110), arg_types="iiBiiii")
    SkipLinesIfFlagOff(1, 11215382)
    RunEvent(11210717, slot=0, args=(7620, 6620, 2, 7640, 6640, 6140, 6120), arg_types="iiBiiii")
    SkipLinesIfFlagOff(1, 11215383)
    RunEvent(11210717, slot=0, args=(7630, 6630, 2, 7640, 6640, 6140, 6130), arg_types="iiBiiii")
    SkipLinesIfFlagOff(10, 11215395)
    IncrementEventValue(7690, bit_count=10, max_value=1000)
    CopyEventValue(source_flag=7690, destination_flag=7190, bit_count=10)
    SkipLinesIfFlagOff(1, 11215380)
    RunEvent(11210717, slot=0, args=(7650, 6650, 3, 7690, 6690, 6190, 6150), arg_types="iiBiiii")
    SkipLinesIfFlagOff(1, 11215381)
    RunEvent(11210717, slot=0, args=(7660, 6660, 3, 7690, 6690, 6190, 6160), arg_types="iiBiiii")
    SkipLinesIfFlagOff(1, 11215382)
    RunEvent(11210717, slot=0, args=(7670, 6670, 3, 7690, 6690, 6190, 6170), arg_types="iiBiiii")
    SkipLinesIfFlagOff(1, 11215383)
    RunEvent(11210717, slot=0, args=(7680, 6680, 3, 7690, 6690, 6190, 6180), arg_types="iiBiiii")
    SkipLinesIfFlagOff(10, 11215405)
    IncrementEventValue(7740, bit_count=10, max_value=1000)
    CopyEventValue(source_flag=7740, destination_flag=7240, bit_count=10)
    SkipLinesIfFlagOff(1, 11215380)
    RunEvent(11210717, slot=0, args=(7700, 6700, 4, 7740, 6740, 6240, 6200), arg_types="iiBiiii")
    SkipLinesIfFlagOff(1, 11215381)
    RunEvent(11210717, slot=0, args=(7710, 6710, 4, 7740, 6740, 6240, 6210), arg_types="iiBiiii")
    SkipLinesIfFlagOff(1, 11215382)
    RunEvent(11210717, slot=0, args=(7720, 6720, 4, 7740, 6740, 6240, 6220), arg_types="iiBiiii")
    SkipLinesIfFlagOff(1, 11215383)
    RunEvent(11210717, slot=0, args=(7730, 6730, 4, 7740, 6740, 6240, 6230), arg_types="iiBiiii")
    DisableFlag(11215393)
    Restart()


def Event11210717(
    _,
    arg_0_3: int,
    arg_4_7: int,
    arg_8_8: uchar,
    arg_12_15: int,
    arg_16_19: int,
    arg_20_23: int,
    arg_24_27: int,
):
    """ 11210717: Event 11210717 """
    DisableNetworkSync()
    IncrementEventValue(arg_0_3, bit_count=10, max_value=1000)
    IfEventsComparison(1, arg_0_3, 10, ComparisonType.GreaterThan, arg_4_7, 10)
    SkipLinesIfConditionFalse(1, 1)
    CopyEventValue(source_flag=arg_0_3, destination_flag=arg_4_7, bit_count=10)
    IfEventsComparison(4, arg_4_7, 10, ComparisonType.GreaterThan, arg_24_27, 10)
    SkipLinesIfConditionFalse(1, 4)
    CopyEventValue(source_flag=arg_4_7, destination_flag=arg_24_27, bit_count=10)
    IfEventsComparison(2, arg_12_15, 10, ComparisonType.GreaterThan, arg_16_19, 10)
    SkipLinesIfConditionFalse(1, 2)
    CopyEventValue(source_flag=arg_12_15, destination_flag=arg_16_19, bit_count=10)
    IfEventsComparison(3, arg_4_7, 10, ComparisonType.GreaterThan, arg_20_23, 10)
    SkipLinesIfConditionFalse(1, 3)
    CopyEventValue(source_flag=arg_4_7, destination_flag=arg_20_23, bit_count=10)
    Unknown_2003_43(flag=arg_20_23, bit_count=10, arg1=arg_8_8, arg2=0)
    End()


def Event11210838():
    """ 11210838: Event 11210838 """
    DisableNetworkSync()
    IfCharacterInsideRegion(-1, PLAYER, region=Boxes.Arena_1vs1_Small_Territory_4510)
    IfCharacterInsideRegion(-1, PLAYER, region=Boxes.Arena_2vs2_Small_Territory_4511)
    IfCharacterInsideRegion(-1, PLAYER, region=Boxes.Arena_BR_Small_Territory_4512)
    IfCharacterInsideRegion(-1, PLAYER, region=Boxes.Arena_1vs1_Large_Territory_4523)
    IfCharacterInsideRegion(-1, PLAYER, region=Boxes.Arena_2vs2_Large_Territory_4524)
    IfCharacterInsideRegion(-1, PLAYER, region=Boxes.Arena_BR_Large_Territory_4525)
    IfCharacterInsideRegion(-1, PLAYER, region=Boxes.Arena_3vs3_Large_Territory_4523)
    IfCharacterInsideRegion(-1, PLAYER, region=Boxes.Arena_BR6_Large_Territory_4523)
    IfCharacterInsideRegion(-1, PLAYER, region=Boxes.Arena_3vs3_Small_Territory_4510)
    IfCharacterInsideRegion(-1, PLAYER, region=Boxes.Arena_BR6_Small_Territory_4510)
    IfConditionTrue(0, input_condition=-1)
    EqualRecovery()


def Event11210839():
    """ 11210839: Event 11210839 """
    DisableNetworkSync()
    DisableFlagRange((8140, 8146))


def Event11210877():
    """ 11210877: Event 11210877 """
    DisableNetworkSync()
    IfFlagOn(7, 11215390)
    IfFlagRangeAllOff(7, (11215380, 11215383))
    IfConditionTrue(0, input_condition=7)
    IfPlayerSoulLevelLessThanOrEqual(1, 50)
    SkipLinesIfConditionFalse(2, 1)
    EnableFlag(11215380)
    Restart()
    IfPlayerSoulLevelComparison(2, ComparisonType.GreaterThan, 50)
    IfPlayerSoulLevelLessThanOrEqual(2, 100)
    SkipLinesIfConditionFalse(2, 2)
    EnableFlag(11215381)
    Restart()
    IfPlayerSoulLevelComparison(3, ComparisonType.GreaterThan, 100)
    IfPlayerSoulLevelLessThanOrEqual(3, 200)
    SkipLinesIfConditionFalse(2, 3)
    EnableFlag(11215382)
    Restart()
    EnableFlag(11215383)
    Restart()


def Event11210890():
    """ 11210890: Event 11210890 """
    DisableNetworkSync()
    IfFlagOn(1, 11215390)
    IfFlagOff(1, 11215391)
    IfFlagOff(1, 8146)
    IfSingleplayer(1)
    IfConditionTrue(0, input_condition=1)
    CancelSpecialEffect(PLAYER, 4612)
    CancelSpecialEffect(PLAYER, 4614)
    CancelSpecialEffect(PLAYER, 4615)
    CancelSpecialEffect(PLAYER, 4616)
    CancelSpecialEffect(PLAYER, 4617)
    CancelSpecialEffect(PLAYER, 4618)
    SkipLinesIfFlagOn(3, 11218145)
    SkipLinesIfFlagOn(2, 8140)
    SkipLinesIfFlagOn(1, 11215350)
    DisplayBattlefieldMessage(150040, display_location_index=1)
    Wait(3.0)
    ArenaExitRequest()
    Restart()


def Event11210701(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int):
    """ 11210701: Event 11210701 """
    IfMultiplayer(1)
    IfFlagOff(-1, 11215396)
    IfFlagOn(-1, 11215397)
    IfConditionTrue(1, input_condition=-1)
    IfFlagOn(1, 11215390)
    IfFlagOff(1, 11215891)
    IfFlagOn(1, arg_0_3)
    IfFlagOff(1, arg_16_19)
    IfFlagOff(2, 11215408)
    IfFlagOff(2, 11215395)
    IfFlagOff(2, 11215405)
    IfFlagOff(2, arg_12_15)
    IfFlagOn(2, arg_8_11)
    IfFlagOn(-5, 11215395)
    IfFlagOn(-5, 11215405)
    IfFlagOn(-5, 11215408)
    IfConditionTrue(3, input_condition=-5)
    IfFlagOn(3, arg_4_7)
    SkipLinesIfFlagOn(1, 11215350)
    IfFlagOff(3, 11218348)
    SkipLinesIfFlagOn(1, 11215352)
    IfFlagOff(3, 11218350)
    SkipLinesIfFlagOn(10, 11215408)
    SkipLinesIfFlagOn(1, 11215351)
    IfFlagOff(3, 11218349)
    SkipLinesIfFlagOn(1, 11215353)
    IfFlagOff(3, 11218351)
    SkipLinesIfFlagOn(5, 11215408)
    SkipLinesIfFlagOn(4, 11215395)
    SkipLinesIfFlagOn(1, 11215354)
    IfFlagOff(3, 11218352)
    SkipLinesIfFlagOn(1, 11215355)
    IfFlagOff(3, 11218353)
    IfConditionTrue(-2, input_condition=2)
    IfConditionTrue(-2, input_condition=3)
    IfConditionTrue(1, input_condition=-2)
    IfFlagOn(4, 11215342)
    IfFlagOn(5, 11215343)
    IfFlagOn(6, 11215344)
    IfFlagOn(7, 11215345)
    IfConditionTrue(0, input_condition=1)
    SkipLinesIfFinishedConditionFalse(1, 4)
    AddSpecialEffect(PLAYER, 4615)
    SkipLinesIfFinishedConditionFalse(1, 5)
    AddSpecialEffect(PLAYER, 4616)
    SkipLinesIfFinishedConditionFalse(1, 6)
    AddSpecialEffect(PLAYER, 4617)
    SkipLinesIfFinishedConditionFalse(1, 7)
    AddSpecialEffect(PLAYER, 4618)
    SkipLinesIfFinishedConditionTrue(4, 4)
    SkipLinesIfFinishedConditionTrue(3, 5)
    SkipLinesIfFinishedConditionTrue(2, 6)
    SkipLinesIfFinishedConditionTrue(1, 7)
    AddSpecialEffect(PLAYER, 4612)
    Wait(5.0)
    Restart()


def Event11210430(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int, arg_20_23: int):
    """ 11210430: Event 11210430 """
    IfMultiplayer(1)
    IfFlagOff(-1, 11215396)
    IfFlagOn(-1, 11215397)
    IfConditionTrue(1, input_condition=-1)
    IfFlagOn(1, 11215390)
    IfFlagOff(1, 11215891)
    IfFlagOn(1, arg_0_3)
    IfFlagOff(1, arg_20_23)
    IfFlagOff(2, 11215395)
    IfFlagOff(2, 11215405)
    IfFlagOn(2, 11215408)
    IfFlagOn(2, arg_4_7)
    IfFlagOn(2, arg_8_11)
    IfFlagOn(-4, 11215392)
    IfFlagOn(-4, 11215402)
    IfConditionTrue(3, input_condition=-4)
    IfFlagOn(3, arg_12_15)
    IfFlagOn(3, arg_16_19)
    IfConditionTrue(-2, input_condition=3)
    IfConditionTrue(-2, input_condition=2)
    IfConditionTrue(1, input_condition=-2)
    IfFlagOn(-3, 11215399)
    IfFlagOn(-3, 11215397)
    IfConditionTrue(1, input_condition=-3)
    IfConditionTrue(0, input_condition=1)
    AddSpecialEffect(PLAYER, 4614)
    Wait(5.0)
    Restart()


def Event11210435(
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
    """ 11210435: Event 11210435 """
    IfMultiplayer(1)
    IfFlagOn(1, 11215390)
    IfFlagOff(1, 11215891)
    IfFlagOn(1, arg_0_3)
    IfFlagOff(1, arg_28_31)
    IfFlagOn(-5, 11215395)
    IfFlagOn(-5, 11215405)
    IfConditionTrue(1, input_condition=-5)
    IfFlagOn(-1, 11215399)
    IfFlagOn(-1, 11215397)
    IfConditionTrue(1, input_condition=-1)
    IfFlagOff(-2, 11215396)
    IfFlagOn(-2, 11215397)
    IfConditionTrue(1, input_condition=-2)
    IfFlagOn(1, arg_4_7)
    IfFlagOn(-3, arg_8_11)
    IfFlagOn(-3, arg_12_15)
    IfFlagOn(-3, arg_16_19)
    SkipLinesIfFlagOff(2, 11215405)
    IfFlagOn(-3, arg_20_23)
    IfFlagOn(-3, arg_24_27)
    IfConditionTrue(1, input_condition=-3)
    IfConditionTrue(0, input_condition=1)
    AddSpecialEffect(PLAYER, 4614)
    Wait(5.0)
    Restart()


def Event11214435(_, arg_0_3: int, arg_4_7: int):
    """ 11214435: Event 11214435 """
    IfFlagOn(1, arg_0_3)
    IfFlagOn(1, arg_4_7)
    IfFlagOn(2, 11215391)
    IfSingleplayer(2)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(0, input_condition=-1)
    CancelSpecialEffect(PLAYER, 4612)
    CancelSpecialEffect(PLAYER, 4614)
    CancelSpecialEffect(PLAYER, 4615)
    CancelSpecialEffect(PLAYER, 4616)
    CancelSpecialEffect(PLAYER, 4617)
    CancelSpecialEffect(PLAYER, 4618)
    IfFlagOn(3, arg_0_3)
    IfFlagOff(3, arg_4_7)
    IfFlagOff(-2, 11215391)
    IfConditionTrue(-2, input_condition=3)
    IfConditionTrue(0, input_condition=-2)
    Restart()


def Event11210434():
    """ 11210434: Event 11210434 """
    EnableFlag(11215399)
    End()
    IfFlagOn(1, 11215390)
    IfFlagOn(1, 11215408)
    IfFlagRangeAnyOn(-2, (11215300, 11215305))
    IfFlagRangeAnyOn(-2, (11215312, 11215317))
    IfConditionTrue(1, input_condition=-2)
    IfFlagOn(2, 11215390)
    IfFlagOn(-1, 11215392)
    IfFlagOn(-1, 11215395)
    IfConditionTrue(2, input_condition=-1)
    IfFlagRangeAnyOn(-3, (11215300, 11215305))
    IfFlagRangeAnyOn(-3, (11215306, 11215311))
    IfFlagRangeAnyOn(-3, (11215312, 11215317))
    IfFlagRangeAnyOn(-3, (11215318, 11215323))
    IfConditionTrue(2, input_condition=-3)
    IfFlagOn(3, 11215390)
    IfFlagOn(-5, 11215402)
    IfFlagOn(-5, 11215405)
    IfConditionTrue(3, input_condition=-1)
    IfFlagRangeAnyOn(-5, (11215300, 11215305))
    IfFlagRangeAnyOn(-5, (11215306, 11215311))
    IfFlagRangeAnyOn(-5, (11215312, 11215317))
    IfFlagRangeAnyOn(-5, (11215318, 11215323))
    IfFlagRangeAnyOn(-5, (11215324, 11215329))
    IfFlagRangeAnyOn(-5, (11215330, 11215335))
    IfConditionTrue(3, input_condition=-5)
    IfConditionTrue(-7, input_condition=1)
    IfConditionTrue(-7, input_condition=2)
    IfConditionTrue(-7, input_condition=3)
    IfConditionTrue(0, input_condition=-7)
    EnableFlag(11215399)


def Event11210845():
    """ 11210845: Event 11210845 """
    IfFlagOn(1, 11215350)
    IfFlagOn(1, 11215390)
    IfConditionTrue(0, input_condition=1)
    ArenaSetNametag1(PLAYER)


def Event11210846():
    """ 11210846: Event 11210846 """
    IfFlagOn(1, 11215351)
    IfFlagOn(1, 11215390)
    IfConditionTrue(0, input_condition=1)
    ArenaSetNametag2(PLAYER)


def Event11210847():
    """ 11210847: Event 11210847 """
    IfFlagOn(1, 11215352)
    IfFlagOn(1, 11215390)
    IfConditionTrue(0, input_condition=1)
    ArenaSetNametag3(PLAYER)


def Event11210848():
    """ 11210848: Event 11210848 """
    IfFlagOn(1, 11215353)
    IfFlagOn(1, 11215390)
    IfConditionTrue(0, input_condition=1)
    ArenaSetNametag4(PLAYER)


def Event11210860():
    """ 11210860: Event 11210860 """
    IfFlagOn(1, 11215354)
    IfFlagOn(1, 11215390)
    IfConditionTrue(0, input_condition=1)
    ArenaSetNametag5(PLAYER)


def Event11210861():
    """ 11210861: Event 11210861 """
    IfFlagOn(1, 11215355)
    IfFlagOn(1, 11215390)
    IfConditionTrue(0, input_condition=1)
    ArenaSetNametag6(PLAYER)


def Event11219121():
    """ 11219121: Event 11219121 """
    IfHost(1)
    IfFlagOff(1, 9121)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(9121)


def Event11219122():
    """ 11219122: Event 11219122 """
    IfFlagOn(1, 9121)
    IfFlagOn(-1, 11810000)
    IfFlagOn(-1, 257)
    IfFlagOn(-1, 710)
    IfConditionTrue(1, input_condition=-1)
    DisableFlag(9121)


def Event11210849():
    """ 11210849: Event 11210849 """
    DisableNetworkSync()
    IfCharacterHasSpecialEffect(0, PLAYER, 17)
    EnableFlag(11215891)
    EnableFlag(8146)
    IfHost(1)
    SkipLinesIfConditionTrue(2, 1)
    EnableFlag(8144)
    SkipLines(1)
    EnableFlag(8145)
    DisplayBattlefieldMessage(150031, display_location_index=1)
    Wait(1.0)
    DisableFlagRange((7000, 7749))
    Unknown_2004_52()
    ArenaExitRequest()
    EqualRecovery()
    Wait(3.0)
    WarpToMap(game_map=OOLACILE, player_start=1218146)
    Restart()


def Event11210826():
    """ 11210826: Event 11210826 """
    IfFlagOn(0, 8145)
    EnableFlag(8140)
    EnableFlag(11215891)


def Event11210837():
    """ 11210837: Event 11210837 """
    IfFlagOn(1, 8145)
    IfFlagOn(1, 11215390)
    IfFlagOff(1, 11215391)
    IfConditionTrue(0, input_condition=1)
    Unknown_2000_06(arg1=0)
    SkipLinesIfFlagOn(4, 11218145)
    SkipLinesIfFlagOff(1, 8145)
    SkipLinesIfFlagOn(2, 11215350)
    SkipLinesIfFlagOn(1, 8145)
    DisplayBattlefieldMessage(150040, display_location_index=1)
    SkipLinesIfFlagOff(2, 8145)
    Wait(3.0)
    ArenaExitRequest()
    Restart()


def Event11210817():
    """ 11210817: Event 11210817 """
    IfFlagOn(1, 8144)
    IfFlagOn(1, 11215390)
    IfFlagOff(1, 11215391)
    IfConditionTrue(0, input_condition=1)
    SkipLinesIfFlagOff(1, 8145)
    SkipLinesIfFlagOn(2, 11215350)
    SkipLinesIfFlagOn(1, 8144)
    DisplayBattlefieldMessage(20000437, display_location_index=1)
    Restart()


def Event11210401():
    """ 11210401: Event 11210401 """
    DisableNetworkSync()
    IfMultiplayer(1)
    IfTrueFlagCountGreaterThanOrEqual(1, 2, (11215360, 11215365))
    IfCharacterHasSpecialEffect(1, PLAYER, 4613)
    IfFlagOff(1, 11215340)
    IfConditionTrue(0, input_condition=1)
    Wait(5.0)
    RestartIfFlagOn(11215340)
    RestartIfSingleplayer()
    DisplayBattlefieldMessage(150000, display_location_index=1)
    Wait(5.0)
    Restart()


def Event11210402():
    """ 11210402: Event 11210402 """
    DisableNetworkSync()
    IfCharacterInsideRegion(-1, PLAYER, region=Boxes.Arena_1vs1_Small_Territory_4510)
    IfCharacterInsideRegion(-1, PLAYER, region=Boxes.Arena_2vs2_Small_Territory_4511)
    IfCharacterInsideRegion(-1, PLAYER, region=Boxes.Arena_BR_Small_Territory_4512)
    IfCharacterInsideRegion(-1, PLAYER, region=Boxes.Arena_1vs1_Large_Territory_4523)
    IfCharacterInsideRegion(-1, PLAYER, region=Boxes.Arena_2vs2_Large_Territory_4524)
    IfCharacterInsideRegion(-1, PLAYER, region=Boxes.Arena_BR_Large_Territory_4525)
    IfCharacterInsideRegion(-1, PLAYER, region=Boxes.Arena_3vs3_Large_Territory_4523)
    IfCharacterInsideRegion(-1, PLAYER, region=Boxes.Arena_BR6_Large_Territory_4523)
    IfCharacterInsideRegion(-1, PLAYER, region=Boxes.Arena_3vs3_Small_Territory_4510)
    IfCharacterInsideRegion(-1, PLAYER, region=Boxes.Arena_BR6_Small_Territory_4510)
    IfConditionTrue(1, input_condition=-1)
    IfCharacterHasSpecialEffect(-2, PLAYER, 2320)
    IfCharacterHasSpecialEffect(-2, PLAYER, 2330)
    IfConditionTrue(1, input_condition=-2)
    IfConditionTrue(0, input_condition=1)
    CancelSpecialEffect(PLAYER, 2320)
    CancelSpecialEffect(PLAYER, 2330)
    Restart()


def Event11210404(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 11210404: Event 11210404 """
    DisableNetworkSync()
    IfFlagOn(6, 11215340)
    IfFlagOn(6, arg_4_7)
    IfFlagOn(6, arg_8_11)
    IfConditionTrue(0, input_condition=6)
    IfEventValueComparison(1, arg_0_3, bit_count=10, comparison_type=ComparisonType.LessThan, value=10)
    IfEventValueComparison(2, arg_0_3, bit_count=10, comparison_type=ComparisonType.GreaterThanOrEqual, value=10)
    IfEventValueComparison(2, arg_0_3, bit_count=10, comparison_type=ComparisonType.LessThan, value=30)
    IfEventValueComparison(3, arg_0_3, bit_count=10, comparison_type=ComparisonType.GreaterThanOrEqual, value=30)
    IfEventValueComparison(3, arg_0_3, bit_count=10, comparison_type=ComparisonType.LessThan, value=50)
    IfEventValueComparison(4, arg_0_3, bit_count=10, comparison_type=ComparisonType.GreaterThanOrEqual, value=50)
    IfEventValueComparison(4, arg_0_3, bit_count=10, comparison_type=ComparisonType.LessThan, value=100)
    IfEventValueComparison(5, arg_0_3, bit_count=10, comparison_type=ComparisonType.GreaterThanOrEqual, value=100)
    SkipLinesIfConditionFalse(1, 2)
    EnableFlag(11215342)
    SkipLinesIfConditionFalse(1, 3)
    EnableFlag(11215343)
    SkipLinesIfConditionFalse(1, 4)
    EnableFlag(11215344)
    SkipLinesIfConditionFalse(1, 5)
    EnableFlag(11215345)


def Event11210407():
    """ 11210407: Event 11210407 """
    DisableNetworkSync()
    SkipLinesIfFlagOff(2, 11210709)
    DisableFlag(11210709)
    End()
    EndIfMultiplayer()
    IfCharacterInsideRegion(-1, PLAYER, region=Boxes.Arena_1vs1_Small_Territory_4510)
    IfCharacterInsideRegion(-1, PLAYER, region=Boxes.Arena_1vs1_Large_Territory_4523)
    IfCharacterInsideRegion(-1, PLAYER, region=Boxes.Arena_2vs2_Small_Territory_4511)
    IfCharacterInsideRegion(-1, PLAYER, region=Boxes.Arena_2vs2_Large_Territory_4524)
    IfCharacterInsideRegion(-1, PLAYER, region=Boxes.Arena_BR_Small_Territory_4512)
    IfCharacterInsideRegion(-1, PLAYER, region=Boxes.Arena_BR_Large_Territory_4525)
    IfCharacterInsideRegion(-1, PLAYER, region=Boxes.Arena_BR6_Large_Territory_4523)
    IfCharacterInsideRegion(-1, PLAYER, region=Boxes.Arena_3vs3_Large_Territory_4523)
    IfCharacterInsideRegion(-1, PLAYER, region=Boxes.Arena_BR6_Small_Territory_4510)
    IfCharacterInsideRegion(-1, PLAYER, region=Boxes.Arena_3vs3_Small_Territory_4510)
    EndIfConditionFalse(-1)
    Wait(2.0)
    RunEvent(11216300)
    RunEvent(11216301)
    RunEvent(11216200, slot=0, args=(1, 60000001), arg_types="Ii")
    RunEvent(11216200, slot=1, args=(2, 60000002), arg_types="Ii")
    RunEvent(11216200, slot=2, args=(3, 60000003), arg_types="Ii")
    RunEvent(11216200, slot=3, args=(4, 60000004), arg_types="Ii")
    RunEvent(11216200, slot=4, args=(5, 60000005), arg_types="Ii")
    RunEvent(11216200, slot=5, args=(6, 60000006), arg_types="Ii")
    RunEvent(11216200, slot=6, args=(7, 60000007), arg_types="Ii")
    RunEvent(11216200, slot=7, args=(8, 60000008), arg_types="Ii")
    RunEvent(11216200, slot=8, args=(9, 60000009), arg_types="Ii")
    RunEvent(11216200, slot=9, args=(10, 60000010), arg_types="Ii")
    RunEvent(11216200, slot=10, args=(11, 60000011), arg_types="Ii")
    RunEvent(11216200, slot=11, args=(12, 60000012), arg_types="Ii")
    RunEvent(11216200, slot=12, args=(13, 60000013), arg_types="Ii")
    RunEvent(11216200, slot=13, args=(14, 60000014), arg_types="Ii")
    RunEvent(11216200, slot=14, args=(15, 60000015), arg_types="Ii")
    RunEvent(11216200, slot=15, args=(16, 60000016), arg_types="Ii")
    RunEvent(11216200, slot=16, args=(17, 60000017), arg_types="Ii")
    RunEvent(11216200, slot=17, args=(18, 60000018), arg_types="Ii")
    RunEvent(11216200, slot=18, args=(19, 60000019), arg_types="Ii")
    RunEvent(11216200, slot=19, args=(20, 60000020), arg_types="Ii")
    RunEvent(11216200, slot=20, args=(21, 60000021), arg_types="Ii")
    RunEvent(11216200, slot=21, args=(22, 60000022), arg_types="Ii")
    RunEvent(11216200, slot=22, args=(23, 60000023), arg_types="Ii")
    RunEvent(11216200, slot=23, args=(24, 60000024), arg_types="Ii")
    RunEvent(11216200, slot=24, args=(25, 60000025), arg_types="Ii")
    RunEvent(11216200, slot=25, args=(26, 60000026), arg_types="Ii")
    RunEvent(11216200, slot=26, args=(27, 60000027), arg_types="Ii")
    RunEvent(11216200, slot=27, args=(28, 60000028), arg_types="Ii")
    RunEvent(11216200, slot=28, args=(29, 60000029), arg_types="Ii")
    RunEvent(11216200, slot=29, args=(30, 60000030), arg_types="Ii")
    RunEvent(11216200, slot=30, args=(31, 60000031), arg_types="Ii")
    RunEvent(11216200, slot=31, args=(32, 60000032), arg_types="Ii")
    RunEvent(11216200, slot=32, args=(33, 60000033), arg_types="Ii")
    RunEvent(11216200, slot=33, args=(34, 60000034), arg_types="Ii")
    RunEvent(11216200, slot=34, args=(35, 60000035), arg_types="Ii")
    RunEvent(11216200, slot=35, args=(36, 60000036), arg_types="Ii")
    RunEvent(11216200, slot=36, args=(37, 60000037), arg_types="Ii")
    RunEvent(11216200, slot=37, args=(38, 60000038), arg_types="Ii")
    RunEvent(11216200, slot=38, args=(39, 60000039), arg_types="Ii")
    RunEvent(11216200, slot=39, args=(40, 60000040), arg_types="Ii")
    RunEvent(11216200, slot=40, args=(41, 60000041), arg_types="Ii")
    RunEvent(11216200, slot=41, args=(42, 60000042), arg_types="Ii")
    RunEvent(11216200, slot=42, args=(43, 60000043), arg_types="Ii")
    RunEvent(11216200, slot=43, args=(44, 60000044), arg_types="Ii")
    RunEvent(11216200, slot=44, args=(45, 60000045), arg_types="Ii")
    RunEvent(11216200, slot=45, args=(46, 60000046), arg_types="Ii")
    RunEvent(11216200, slot=46, args=(47, 60000047), arg_types="Ii")
    RunEvent(11216200, slot=47, args=(48, 60000048), arg_types="Ii")
    RunEvent(11216200, slot=48, args=(49, 60000049), arg_types="Ii")
    RunEvent(11216200, slot=49, args=(50, 60000050), arg_types="Ii")
    RunEvent(11216200, slot=50, args=(51, 60000051), arg_types="Ii")
    RunEvent(11216200, slot=51, args=(52, 60000052), arg_types="Ii")
    RunEvent(11216200, slot=52, args=(53, 60000053), arg_types="Ii")
    RunEvent(11216200, slot=53, args=(54, 60000054), arg_types="Ii")
    RunEvent(11216200, slot=54, args=(55, 60000055), arg_types="Ii")
    RunEvent(11216200, slot=55, args=(56, 60000056), arg_types="Ii")
    RunEvent(11216200, slot=56, args=(57, 60000057), arg_types="Ii")
    RunEvent(11216200, slot=57, args=(58, 60000058), arg_types="Ii")
    RunEvent(11216200, slot=58, args=(59, 60000059), arg_types="Ii")
    RunEvent(11216200, slot=59, args=(60, 60000060), arg_types="Ii")
    RunEvent(11216200, slot=60, args=(61, 60000061), arg_types="Ii")
    RunEvent(11216200, slot=61, args=(62, 60000062), arg_types="Ii")
    RunEvent(11216200, slot=62, args=(63, 60000063), arg_types="Ii")
    RunEvent(11216200, slot=63, args=(64, 60000064), arg_types="Ii")
    RunEvent(11216200, slot=64, args=(65, 60000065), arg_types="Ii")
    RunEvent(11216200, slot=65, args=(66, 60000066), arg_types="Ii")
    RunEvent(11216200, slot=66, args=(67, 60000067), arg_types="Ii")
    RunEvent(11216200, slot=67, args=(68, 60000068), arg_types="Ii")
    RunEvent(11216200, slot=68, args=(69, 60000069), arg_types="Ii")
    RunEvent(11216200, slot=69, args=(70, 60000070), arg_types="Ii")
    RunEvent(11216200, slot=70, args=(71, 60000071), arg_types="Ii")
    RunEvent(11216200, slot=71, args=(72, 60000072), arg_types="Ii")
    RunEvent(11216200, slot=72, args=(73, 60000073), arg_types="Ii")
    RunEvent(11216200, slot=73, args=(74, 60000074), arg_types="Ii")
    RunEvent(11216200, slot=74, args=(75, 60000075), arg_types="Ii")
    RunEvent(11216200, slot=75, args=(76, 60000076), arg_types="Ii")
    RunEvent(11216200, slot=76, args=(77, 60000077), arg_types="Ii")
    RunEvent(11216200, slot=77, args=(78, 60000078), arg_types="Ii")
    RunEvent(11216200, slot=78, args=(79, 60000079), arg_types="Ii")
    RunEvent(11216200, slot=79, args=(80, 60000080), arg_types="Ii")
    RunEvent(11216200, slot=80, args=(81, 60000081), arg_types="Ii")
    RunEvent(11216200, slot=81, args=(82, 60000082), arg_types="Ii")
    RunEvent(11216200, slot=82, args=(83, 60000083), arg_types="Ii")
    RunEvent(11216200, slot=83, args=(84, 60000084), arg_types="Ii")
    RunEvent(11216200, slot=84, args=(85, 60000085), arg_types="Ii")
    RunEvent(11216200, slot=85, args=(86, 60000086), arg_types="Ii")
    RunEvent(11216200, slot=86, args=(87, 60000087), arg_types="Ii")
    RunEvent(11216200, slot=87, args=(88, 60000088), arg_types="Ii")
    RunEvent(11216200, slot=88, args=(89, 60000089), arg_types="Ii")
    RunEvent(11216200, slot=89, args=(90, 60000090), arg_types="Ii")
    RunEvent(11216200, slot=90, args=(91, 60000091), arg_types="Ii")
    RunEvent(11216200, slot=91, args=(92, 60000092), arg_types="Ii")
    RunEvent(11216200, slot=92, args=(93, 60000093), arg_types="Ii")
    RunEvent(11216200, slot=93, args=(94, 60000094), arg_types="Ii")
    RunEvent(11216200, slot=94, args=(95, 60000095), arg_types="Ii")
    RunEvent(11216200, slot=95, args=(96, 60000096), arg_types="Ii")
    RunEvent(11216200, slot=96, args=(97, 60000097), arg_types="Ii")
    RunEvent(11216200, slot=97, args=(98, 60000098), arg_types="Ii")
    RunEvent(11216200, slot=98, args=(99, 60000099), arg_types="Ii")
    RunEvent(11216200, slot=99, args=(100, 60000100), arg_types="Ii")


def Event11216200(_, arg_0_3: uint, arg_4_7: int):
    """ 11216200: Event 11216200 """
    DisableNetworkSync()
    IfEventValueEqual(-1, 7200, bit_count=10, value=arg_0_3)
    IfEventValueEqual(-1, 7450, bit_count=10, value=arg_0_3)
    IfEventValueEqual(-1, 7700, bit_count=10, value=arg_0_3)
    EndIfConditionFalse(-1)
    DisplayStatus(arg_4_7, pad_enabled=True)


def Event11216300():
    """ 11216300: Event 11216300 """
    DisableNetworkSync()
    IfEventValueEqual(1, 7200, bit_count=10, value=0)
    IfEventValueEqual(1, 7450, bit_count=10, value=0)
    IfEventValueEqual(1, 7700, bit_count=10, value=0)
    EndIfConditionFalse(1)
    DisplayStatus(60000000, pad_enabled=True)


def Event11216301():
    """ 11216301: Event 11216301 """
    DisableNetworkSync()
    IfEventValueGreaterThan(-1, 7200, bit_count=10, value=100)
    IfEventValueGreaterThan(-1, 7450, bit_count=10, value=100)
    IfEventValueGreaterThan(-1, 7700, bit_count=10, value=100)
    EndIfConditionFalse(-1)
    DisplayStatus(59999999, pad_enabled=True)


def Event11210439():
    """ 11210439: Event 11210439 """
    EndIfClient()
    IfCharacterInsideRegion(-1, PLAYER, region=Boxes.Arena_1vs1_Small_Territory_4510)
    IfCharacterInsideRegion(-1, PLAYER, region=Boxes.Arena_2vs2_Small_Territory_4511)
    IfCharacterInsideRegion(-1, PLAYER, region=Boxes.Arena_BR_Small_Territory_4512)
    IfCharacterInsideRegion(-1, PLAYER, region=Boxes.Arena_1vs1_Large_Territory_4523)
    IfCharacterInsideRegion(-1, PLAYER, region=Boxes.Arena_2vs2_Large_Territory_4524)
    IfCharacterInsideRegion(-1, PLAYER, region=Boxes.Arena_BR_Large_Territory_4525)
    IfCharacterInsideRegion(-1, PLAYER, region=Boxes.Arena_3vs3_Small_Territory_4510)
    IfCharacterInsideRegion(-1, PLAYER, region=Boxes.Arena_BR6_Small_Territory_4510)
    IfCharacterInsideRegion(-1, PLAYER, region=Boxes.Arena_3vs3_Large_Territory_4523)
    IfCharacterInsideRegion(-1, PLAYER, region=Boxes.Arena_BR6_Large_Territory_4523)
    EndIfConditionFalse(-1)
    SetTeamType(PLAYER, TeamType.Human)


def Event11219999():
    """ 11219999: Event 11219999 """
    IfCharacterInsideRegion(1, PLAYER, region=1219999)
    IfFlagOff(1, 11219898)
    IfConditionTrue(0, input_condition=1)
    DisableAI(PLAYER)
    EnableFlag(11219898)
    RotateToFaceEntity(PLAYER, Points.ArrivalFromDarkroot)
    Wait(10.0)
    EnableAI(PLAYER)
    Restart()


def Event11219900():
    """ 11219900: Event 11219900 """
    IfMultiplayer(1)
    IfTrueFlagCountGreaterThanOrEqual(1, 2, (11215360, 11215365))
    IfFlagOff(1, 11215390)
    IfTimeElapsed(1, 60.0)
    IfConditionTrue(0, input_condition=1)


def Event11219901():
    """ 11219901: Event 11219901 """
    IfMultiplayer(1)
    IfFlagOn(1, 11215360)
    IfFlagOff(1, 11215390)
    IfCharacterInsideRegion(-1, PLAYER, region=Boxes.Arena_BR6_Small_Territory_4510)
    IfCharacterInsideRegion(-1, PLAYER, region=Boxes.Arena_BR6_Large_Territory_4523)
    IfCharacterInsideRegion(-1, PLAYER, region=Boxes.Arena_BR_Small_Territory_4512)
    IfCharacterInsideRegion(-1, PLAYER, region=Boxes.Arena_BR_Large_Territory_4525)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(11219902)


def Event11219950(_, arg_0_3: int):
    """ 11219950: Event 11219950 """
    DisableNetworkSync()
    IfFlagOn(1, 11215390)
    IfFlagOn(1, arg_0_3)
    IfConditionTrue(0, input_condition=1)
    EnableAI(PLAYER)


def Event7999():
    """ 7999: Event 7999 """
    DisableNetworkSync()
    IfFlagOn(1, 905)
    IfFlagOn(2, 906)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFlagOn(3, 906)
    DisableFlag(905)
    AddSpecialEffect(PLAYER, 4611)
    Restart()
    DisableFlag(906)
    AddSpecialEffect(PLAYER, 4612)
    Restart()


def Event7998():
    """ 7998: Event 7998 """
    IfFlagOn(1, 5100)
    IfFlagOn(2, 5101)
    IfFlagOn(3, 5102)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    DisableFlagRange((5100, 5102))
    SkipLinesIfFinishedConditionFalse(1, 1)
    IncrementEventValue(7200, bit_count=10, max_value=1000)
    SkipLinesIfFinishedConditionFalse(1, 2)
    IncrementEventValue(7450, bit_count=10, max_value=1000)
    SkipLinesIfFinishedConditionFalse(1, 3)
    IncrementEventValue(7700, bit_count=10, max_value=1000)
    Restart()


def Event11219876():
    """ 11219876: Event 11219876 """
    IfCharacterInsideRegion(1, PLAYER, region=Boxes.TestBox)
    IfFlagOff(1, 11212778)
    IfConditionTrue(0, input_condition=1)
    Unknown_2003_43(flag=6000, bit_count=10, arg1=0, arg2=0)
    EnableFlag(11212778)
    Restart()
    IfCharacterInsideRegion(2, PLAYER, region=Boxes.TestBox)
    IfFlagOn(2, 11212778)
    IfConditionTrue(0, input_condition=2)
    Unknown_2003_43(flag=6000, bit_count=10, arg1=0, arg2=1)
    DisableFlag(11212778)
    Restart()


def Event11219877():
    """ 11219877: Event 11219877 """
    IfFlagOn(1, 11215390)
    IfFlagOn(-1, 11215392)
    IfFlagOn(-1, 11215402)
    IfFlagOff(2, 11215360)
    IfFlagOff(2, 11215361)
    IfFlagOff(2, 11215364)
    IfFlagOff(3, 11215362)
    IfFlagOff(3, 11215363)
    IfFlagOff(3, 11215365)
    IfConditionTrue(-2, input_condition=2)
    IfConditionTrue(-2, input_condition=3)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(1, input_condition=-2)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(11218145)
    Unknown_2000_06(arg1=2)
    Wait(3.0)
    Unknown_2004_52()
    ArenaExitRequest()
