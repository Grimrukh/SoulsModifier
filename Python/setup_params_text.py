
import pickle
import typing as tp
from pathlib import Path

from soulstruct.darksouls1ptde.params.enums import SpecialStateInfo, ATKPARAM_REP_DMGTYPE
from soulstruct.darksouls1r.params import GameParamBND, Param
from soulstruct.darksouls1r.text import MSGDirectory

from file_paths import VANILLA_PATH, MOD_PATH, INSTALLER_PATH
from project.entities_templates.common_entities import CommonEffects, CommonText


def install_params_text():
    params = GameParamBND(VANILLA_PATH / "param/GameParam/GameParam.parambnd.dcx")
    text = MSGDirectory(VANILLA_PATH / "msg/ENGLISH")
    create_event_text(text)

    params.better_debug_player()
    add_patches_params(params)
    create_speffects(params)
    create_aggressive_ai(params)
    add_oops_enemy_levels(params)
    create_cosplay_equipment(params, text)
    add_item_lots(params)
    edit_spells(params)

    with Path("project/params.ssp").open("wb") as f:
        pickle.dump(params, f)
    params.write(MOD_PATH / "param/GameParam/GameParam.parambnd.dcx")
    params.write(INSTALLER_PATH / "param/GameParam/GameParam.parambnd.dcx")

    # Write an additional copy to installer containing the `NpcThinkParam.param` for hyper aggression.
    aggressive_ai_param = Param("HyperAggression_NpcThinkParam.param")
    params.params["N:\\FRPG\\data\\INTERROOT_x64\\param\\GameParam\\NpcThinkParam.param"] = aggressive_ai_param
    params.write(INSTALLER_PATH / "param/GameParam/HyperAggressionGameParam.parambnd.dcx")

    with Path("project/text.ssp").open("wb") as f:
        pickle.dump(text, f)
    text.write(MOD_PATH / "msg/ENGLISH")
    text.write(INSTALLER_PATH / "msg/ENGLISH")


def create_event_text(text: MSGDirectory):
    text.EventText[CommonText.HookConnectionError.value] = "Manager not connected"
    text.EventText[CommonText.ManusDefeated.value] = "The Abyss has already been conquered"
    text.EventText[CommonText.InstantDeathWarning.value] = "You feel terribly frail..."
    text.EventText[CommonText.DeathFollowsWarning.value] = "Death follows your footsteps... RUN."
    text.EventText[CommonText.PraiseTheSun.value] = "Praise the Sun!"


def add_patches_params(params: GameParamBND):
    params.Characters[6322] = params.Characters[6320].copy()
    params.Characters[6322]["teamType"] = 0
    params.Characters[6322]["itemLotId_1"] = -1


def create_speffects(params: GameParamBND):
    """Create new effects from above dictionaries."""

    # Create repair effect for left hand.
    left_hand_repair = params.SpecialEffects[3100].copy()
    left_hand_repair["wepParamChange"] = 2  # left hand
    params.SpecialEffects[3101] = left_hand_repair

    # Default duration is 60 seconds.
    template = params.SpecialEffects[91111].copy()
    template.update(**{
        "effectTargetEnemy:1": True,
        "effectTargetFriend:1": True,
        "effectTargetWhiteGhost:1": True,
        "effectTargetBlackGhost:1": True,
        "effectTargetAttacker:1": True,
        "isExtendSpEffectLife:1": True,
        "effectEndurance": 120.0,
    })

    for name, (effect_id, effect_dict) in CUSTOM_EFFECTS.items():
        if isinstance(effect_dict, int):
            params.SpecialEffects[effect_id] = params.SpecialEffects[effect_dict].copy()
        else:
            params.SpecialEffects[effect_id] = template.copy()
            params.SpecialEffects[effect_id].update(**effect_dict)
        params.SpecialEffects[effect_id].name = name

    for i, (effect_name, effect_dict) in enumerate(PLAYER_EFFECTS.items()):
        params.SpecialEffects[100000 + i] = template.copy()
        params.SpecialEffects[100000 + i].name = effect_name
        params.SpecialEffects[100000 + i].update(**effect_dict)

    for i, (effect_name, effect_dict) in enumerate(ENEMY_EFFECTS.items()):
        params.SpecialEffects[200000 + i] = template.copy()
        params.SpecialEffects[200000 + i].name = f"Enemy{effect_name}"
        params.SpecialEffects[200000 + i].update(**effect_dict)


def create_aggressive_ai(params: GameParamBND):
    """Create aggressive versions of every AI entry at +50.

    Note that there is one vanilla entry ending in 50 (or greater): 267050, a male ghost variant. As there is no entry
    267100, it's still OK to add 50 to this one.
    """
    aggr_ai = Param("HyperAggression_NpcThinkParam.param")
    for entry_id, entry in tuple(params.AI.items()):
        if entry_id < 120000:
            continue  # don't touch NPCs
        try:
            aggressive_entry = aggr_ai[entry_id]
        except KeyError:
            aggressive_entry = entry  # no change
        params.AI[entry_id + 50] = aggressive_entry


def add_oops_enemy_levels(params):
    for base_id in (293000, 335000, 537000):
        default_param = params.Characters[base_id]
        for i in range(0, 16):
            level_param = default_param.copy()
            level_param["spEffectID4"] = -1 if i == 0 else 7000 + i
            params.Characters[base_id + 50 + i] = level_param


def create_cosplay_equipment(params: GameParamBND, text: MSGDirectory):
    """Create forced equipment, which largely involves just removing stat requirements and reducing weight."""

    def _copy_weapon(weapon_id: int, new_id: int):
        new_weapon = params.Weapons[weapon_id].copy()
        new_weapon["properStrength"] = 5
        new_weapon["properAgility"] = 5
        new_weapon["properMagic"] = 5
        new_weapon["properFaith"] = 5
        new_weapon["weight"] = 1.0
        new_weapon["durability"] = 300  # just so it's less likely to screw with real weapon durability
        new_weapon["durabilityMax"] = 300
        params.Weapons[new_id] = new_weapon

        for i in range(16):
            # Names for levels (up to +15).
            if weapon_id + i in params.Weapons.rows:
                text.WeaponNames[new_id + i] = text.WeaponNames[weapon_id + i]
        text.WeaponSummaries[new_id] = text.WeaponSummaries[weapon_id]
        text.WeaponDescriptions[new_id] = text.WeaponDescriptions[weapon_id]

    def _copy_armor(armor_id: int, new_id: int):
        new_armor = params.Armor[armor_id].copy()
        new_armor["weight"] *= 0.25
        new_armor["durability"] = 300  # just so it's less likely to screw with real armor durability
        new_armor["durabilityMax"] = 300
        params.Armor[new_id] = new_armor
        text.ArmorNames[new_id] = text.ArmorNames[armor_id]

        for i in range(11):
            if armor_id + i in params.Armor.rows:
                text.ArmorNames[new_id + i] = text.ArmorNames[armor_id + i]
        text.ArmorSummaries[new_id] = text.ArmorSummaries[armor_id]
        text.ArmorDescriptions[new_id] = text.ArmorDescriptions[armor_id]

    def _create_set(
        index, right_weapon_1, right_weapon_2, left_weapon_1, left_weapon_2, head, body=None, arms=None, legs=None
    ):
        base = 3000000 + index * 10000
        if right_weapon_1 != -1:
            _copy_weapon(right_weapon_1, base + 0)
            if right_weapon_1 == 1330000:  # Pyromancy Flame
                for i in range(1, 16):
                    _copy_weapon(right_weapon_1 + i * 100, base + i)
        if right_weapon_2 != -1:
            _copy_weapon(right_weapon_2, base + 1000)
        if left_weapon_1 != -1:
            _copy_weapon(left_weapon_1, base + 2000)
        if left_weapon_2 != -1:
            _copy_weapon(left_weapon_2, base + 3000)
        if head != -1:
            _copy_armor(head, base + 4000)
            if body is None:
                body = head + 1000
            if arms is None:
                arms = head + 2000
            if legs is None:
                legs = head + 3000
        if body != -1:
            _copy_armor(body, base + 5000)
        if arms != -1:
            _copy_armor(arms, base + 6000)
        if legs != -1:
            _copy_armor(legs, base + 7000)

    # Giant Dad (Chaos Zweihander, Giant Shield/Grass Crest Shield, Mask of the Father, Giant set)
    _create_set(0, 350900, -1, 1502000, 1453000, 590000, 531000, 532000, 533000)

    # Gwyn
    _create_set(1, 314000, -1, -1, -1, 550000)

    # Havel
    _create_set(2, 854000, -1, 1505000, -1, 440000)

    # Mildred (Butcher Knife, Plank Shield, Sack)
    _create_set(3, 703000, -1, 1409000, -1, 560000, -1, -1, -1)

    # UFC (Caestus x2, Dark set)
    _create_set(4, 901300, -1, -1, -1, 40000)

    # Crystal
    _create_set(5, 304000, -1, 1471000, -1, 130000)

    # Logan
    _create_set(6, 1303000, -1, 1403000, -1, 380000)

    # Pharis
    _create_set(7, 1202000, -1, 1400000, -1, 240000)

    # Laurentius (Pyromancy Flame +5)
    _create_set(8, 1330500, -1, 1406000, -1, 230000)

    # Oswald
    _create_set(9, 801000, -1, 1361000, -1, 150000)

    # Noob (Drake Sword, Knight Shield, Fang Boar Helm, Elite Knight set)
    _create_set(10, 211000, -1, 1451000, -1, 620000, 351000, 352000, 353000)


def add_item_lots(params: GameParamBND):
    params.ItemLots[500] = arrow_gift = params.ItemLots[1020].copy()
    arrow_gift["getItemFlagId"] = -1
    arrow_gift["lotItemId01"] = 2001000
    arrow_gift["lotItemNum01"] = 99


def edit_spells(params: GameParamBND):
    """Eliminate INT/FAI requirements for all spells.

    This is just easier than duplicating them, since Lobos probably won't use them outside the force equips anyway.
    """
    for spell_entry in params.Spells.values():
        spell_entry["requirementIntellect"] = 1
        spell_entry["requirementFaith"] = 1


INCOMING_DAMAGE_TYPES = ("slash", "blow", "thrust", "neutral", "magic", "fire", "thunder")
OUTGOING_DAMAGE_TYPES = ("physics", "magic", "fire", "thunder")
DAMAGE_LEVELS = ("S", "M", "L", "BlowM", "Push", "Strike", "BlowS", "Min", "Uppercut", "BlowLL", "Breath")
STATUS_TYPES = ("Poizon", "Illness", "Blood", "Curse")
ONE_FRAME = dict(effectEndurance=0.0)
DAMAGE_LEVEL_CHANGE = dict(categoryPriority=200, spCategory=1001)
VFX = {"useSpEffectEffect:1": True}  # type: dict[str, tp.Any]
WEAPON_BUFF = VFX | {"wepParamChange": 1}
CUSTOM_EFFECTS = {
    "OneHP": (800, ONE_FRAME | dict(changeHpRate=99.0)),
    "ManusReward": (CommonEffects.ManusReward.value, ONE_FRAME | dict(soul=50000)),
}

# Base effect has `effectEndurance` 60.

# Effect `i` uses SpEffect `100000 + i`, event `11812100 + i`, and trigger flag `11812600 + i`.
PLAYER_EFFECTS = {
    # Speed (with accompanying damage/poise changes)
    "SpeedUp": dict(grabityRate=1.25, physicsAttackPowerRate=0.7, changeSuperArmorPoint=-20),
    "ExtremeSpeedUp": dict(grabityRate=1.5, physicsAttackPowerRate=0.5, changeSuperArmorPoint=-40),
    "SpeedDown": dict(grabityRate=0.75, physicsAttackPowerRate=1.4, changeSuperArmorPoint=50),
    "ExtremeSpeedDown": dict(grabityRate=0.5, physicsAttackPowerRate=2.0, changeSuperArmorPoint=100),

    # Health
    "HealthRegain": dict(motionInterval=0.5, changeHpPoint=-10),
    "HealthDrain": dict(motionInterval=0.2, changeHpPoint=3),
    "MaxHealthUp": dict(maxHpRate=1.5),
    "MaxHealthDown": dict(maxHpRate=0.5),

    # Stamina
    "StaminaRegenUp": dict(staminaRecoverChangeSpeed=80),  # 2x Green Blossom
    "ExtremeStaminaRegenUp": dict(staminaRecoverChangeSpeed=400),  # 10x Green Blossom
    "StaminaRegenDown": dict(staminaRecoverChangeSpeed=-20),

    # Equip load
    "MaxEquipLoadUp": dict(equipWeightChangeRate=5.0),  # way up (basically fast roll with anything)
    "MaxEquipLoadDown": dict(equipWeightChangeRate=0.5),

    # Defense
    "DefenseUp": {f"{d}DamageCutRate": 0.5 for d in INCOMING_DAMAGE_TYPES},
    "Invincible": {f"{d}DamageCutRate": 0.0 for d in INCOMING_DAMAGE_TYPES} | {"stateInfo": SpecialStateInfo.CastLight},
    "DefenseDown": {f"{d}DamageCutRate": 1.5 for d in INCOMING_DAMAGE_TYPES},
    "InstantDeath": {f"{d}DamageCutRate": 100.0 for d in INCOMING_DAMAGE_TYPES} | dict(effectEndurance=10.0),

    # Misc.
    "Exterminate": {f"{d}AttackRate": 100.0 for d in OUTGOING_DAMAGE_TYPES} | dict(effectEndurance=10.0),
    # "DetectionUp": dict(sightSearchEnemyCut=-500, hearingSearchEnemyCut=-500),  # TODO: doesn't work
    "DetectionDown": dict(sightSearchEnemyCut=98, hearingSearchEnemyCut=98, stateInfo=SpecialStateInfo.Transparent),
    "SoulDrain": dict(motionInterval=0.5, soul=-50),
    "Sturdy": {f"dmgLv_{d}": ATKPARAM_REP_DMGTYPE.Small for d in DAMAGE_LEVELS} | DAMAGE_LEVEL_CHANGE,
    "Fragile": {f"dmgLv_{d}": ATKPARAM_REP_DMGTYPE.Launch for d in DAMAGE_LEVELS} | DAMAGE_LEVEL_CHANGE,
    "WeakHeals": dict(hpRecoverRate=0.5),
    "PainfulHeals": dict(hpRecoverRate=-1.0),  # works!
    "EggInfection": VFX | dict(
        effectEndurance=60.0, saveCategory=3, stateInfo=SpecialStateInfo.EggParasiteScratching,
        motionInterval=10.0,  # does not actually lead to infection, just a head scratch
    ),  # second stage (shorter)
    "BinocularsMode": dict(stateInfo=SpecialStateInfo.BinocularsZoom, effectEndurance=20.0),
    "Thorny": dict(stateInfo=SpecialStateInfo.ThornedBody, physicsAttackPower=250),

    # Enchantment effects
    "FallControl": VFX | {"stateInfo": SpecialStateInfo.FallControl},
    "FireWeapon": WEAPON_BUFF | dict(fireAttackPower=80, stateInfo=SpecialStateInfo.FireWeapon, spAttribute=2),
    "MagicWeapon": WEAPON_BUFF | dict(magicAttackPower=80, stateInfo=SpecialStateInfo.MagicWeapon, spAttribute=3),
    "LightningWeapon": WEAPON_BUFF | dict(
        thunderAttackPower=150, stateInfo=SpecialStateInfo.LightningWeapon, spAttribute=6
    ),
    # "PoisonWeapon": WEAPON_BUFF | dict(
    #     atkOccurrenceSpEffectId=3191, stateInfo=SpecialStateInfo.PoisonedWeapon, spAttribute=4
    # ),

    # Resistance
    # "StatusImmunity": dict(
    #     motionInterval=0.1, poizonAttackPower=-99999, registIllness=-99999, registBlood=-99999, registCurse=-99999
    # ),

    # One-frame effects
    "FullHeal": ONE_FRAME | dict(changeHpRate=-100.0),
    "OneHPPreHeal": ONE_FRAME | dict(changeHpRate=-100.0, replaceSpEffectId=CUSTOM_EFFECTS["OneHP"][0]),
    "SoulBoost": ONE_FRAME | dict(soul=10000),
    "SoulSteal": ONE_FRAME | dict(soul=-10000),
    # "HumanityBoost": ONE_FRAME | dict(heroPointDamage=-2),
    # "HumanitySteal": ONE_FRAME | dict(heroPointDamage=2),
    # "WeaponRepair": ONE_FRAME | dict(insideDurability=-200),  # no inverse effect!
}

# Effect `i` uses SpEffect `200000 + i`, event `{prefix}2200 + i`, and trigger flag `11812700 + i`.
ENEMY_EFFECTS = {
    # Speed (with accompanying damage/poise changes)
    "SpeedUp": dict(grabityRate=1.25, physicsAttackPowerRate=0.75, changeSuperArmorPoint=-20),
    "ExtremeSpeedUp": dict(grabityRate=1.5, physicsAttackPowerRate=0.5, changeSuperArmorPoint=-40),
    "SpeedDown": dict(grabityRate=0.75, physicsAttackPowerRate=1.5, changeSuperArmorPoint=50),
    "ExtremeSpeedDown": dict(grabityRate=0.5, physicsAttackPowerRate=2.0, changeSuperArmorPoint=100),

    "HealthRegain": dict(motionInterval=1.0, changeHpPoint=-10),
    "MaxHealthUp": dict(maxHpRate=1.5),
    "MaxHealthDown": dict(maxHpRate=0.5),

    "DefenseUp": {f"{d}DamageCutRate": 0.5 for d in INCOMING_DAMAGE_TYPES},
}
