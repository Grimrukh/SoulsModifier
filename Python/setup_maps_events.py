import pickle
from pathlib import Path

from soulstruct.darksouls1r.events import convert_events
from soulstruct.darksouls1r.maps import MapStudioDirectory, MSB
from soulstruct.darksouls1r.maps.utilities import build_ffxbnd
from soulstruct.darksouls1r.params import GameParamBND
from soulstruct.game_types import Map

from file_paths import VANILLA_PATH, MOD_PATH, INSTALLER_PATH
from setup_params_text import ENEMY_EFFECTS, PLAYER_EFFECTS


def install_maps_events():
    maps = MapStudioDirectory(VANILLA_PATH / "map/MapStudio")

    add_seal_key_item_corpse(maps.NewLondoRuins)
    remove_bonfires_from_collisions(maps)
    # remove_enemy_collisions(maps)  # probably adds more problems (e.g. bosses falling to their death)
    assign_map_piece_ids(maps)
    all_char_entity_ids = assign_chr_entity_ids(maps)
    gwyn_entity_ids = add_gwyns(maps, all_char_entity_ids)
    bonewheel_entity_ids = add_bonewheels(maps, all_char_entity_ids)
    add_patches(maps)
    add_channeler(maps)
    add_models(maps)
    add_manus_warp_point(maps.Oolacile)

    for map_name, msb in maps.msbs.items():
        game_map = maps.GET_MAP(map_name)

        ffxbnd = build_ffxbnd(
            msb,
            ffxbnd_path=MOD_PATH / f"sfx/{game_map.ffxbnd_file_name}.ffxbnd.dcx",
            ffxbnd_search_directory=VANILLA_PATH / "sfx",
            prefer_bak=True,
        )
        # Also write new FFXBND to installer package.
        ffxbnd.write(INSTALLER_PATH / f"sfx/{game_map.ffxbnd_file_name}.ffxbnd.dcx")

        entity_ai_params = {
            char.entity_id: char.ai_id
            for char in msb.parts.Characters
            if char.entity_id >= 1000000 and char.ai_id > 1
        }

        create_events(
            game_map,
            all_char_entity_ids[game_map.area_id, game_map.block_id],
            gwyn_entity_ids,
            bonewheel_entity_ids,
            entity_ai_params
        )

    create_common_events()
    create_common_entities()

    with Path("project/maps.ssp").open("wb") as f:
        pickle.dump(maps, f)
    maps.write(MOD_PATH / "map/MapStudio")
    maps.write(INSTALLER_PATH / "map/MapStudio")

    convert_events("emevd.dcx", MOD_PATH / "event", "evs.py", "project/events")
    convert_events("emevd.dcx", INSTALLER_PATH / "event", "evs.py", "project/events")


def add_seal_key_item_corpse(new_londo_ruins: MSB):
    new_londo_ruins.parts.new_object(
        "o0500_0038",
        name="o0500_KeyToTheSeal",
        translate=(59.62, -135.80, 9.78),
        default_animation=20,
        draw_parent_name="h0023B0_0000",
    )
    new_londo_ruins.events.new_treasure(
        36,  # 宝死体37
        name="Treasure_KeyToTheSeal",
        treasure_part_name="o0500_KeyToTheSeal",
        item_lot_1=1100,
    )


def add_manus_warp_point(oolacile: MSB):
    oolacile.parts.new_player_start(
        name="c0000_ManusWarp",
        translate=(854.100, -576.780, 870.450),
        rotate=(0.0, 10.0, 0.0),
        entity_id=1210980,
    )


def remove_enemy_collisions(maps: MapStudioDirectory):
    for map_name, msb in maps.msbs.items():
        for collision in msb.parts.Collisions:
            if collision.hit_filter_id == 11:
                print(map_name, collision.name)


def remove_bonfires_from_collisions(maps: MapStudioDirectory):
    """Invisible Gwyns/Bonewheels may block bonfire usage otherwise."""
    for msb in maps.msbs.values():
        for collision in msb.parts.Collisions:
            collision.attached_bonfire = -1


def assign_map_piece_ids(maps: MapStudioDirectory) -> dict[tuple[int, int], int]:
    """Give map pieces entity IDs. Skips skyboxes (models in 9000 range) and map pieces with existing IDs.

    Resulting range of new IDs is contiguous. Returns dictionary mapping `(area_id, block_id)` to the number of affected
    map pieces (for event script usage).
    """

    piece_count = {}
    for map_name, msb in maps.items():
        game_map = maps.GET_MAP(map_name)
        base_id = game_map.base_entity_id + 8500

        entity_index = 0
        for map_piece in msb.parts.MapPieces:
            if 9000 <= int(map_piece.model_name[1:5]) <= 9999 or map_piece.entity_id != -1:
                # Skip skybox map piece and pieces with existing entity IDs.
                continue
            map_piece.entity_id = base_id + entity_index
            entity_index += 1
        piece_count[game_map.area_id, game_map.block_id] = entity_index
    return piece_count


def assign_chr_entity_ids(maps: MapStudioDirectory) -> dict[tuple[int, int], list[int]]:
    """Give all characters entity IDs.

    Does not change existing IDs, but still returns them in list for map.
    """

    all_entity_ids = {}
    for map_name, msb in maps.items():
        game_map = maps.GET_MAP(map_name)  # type: Map
        existing_part_entity_ids = {part.entity_id for part in msb.parts} - {-1}
        base_id = game_map.base_entity_id + 200

        next_entity_id = base_id
        while next_entity_id in existing_part_entity_ids:
            next_entity_id += 1
        entities = []
        for char in msb.parts.Characters:
            if char.entity_id == -1:
                char.entity_id = next_entity_id
                next_entity_id += 1
                while next_entity_id in existing_part_entity_ids:
                    next_entity_id += 1
            entities.append(char.entity_id)
        all_entity_ids[game_map.area_id, game_map.block_id] = entities
    return all_entity_ids


def add_gwyns(maps: MapStudioDirectory, all_chr_entity_ids: dict[tuple[int, int], list[int]]):
    """Add a 'guardian Gwyn' for every entity ID."""
    params = GameParamBND(VANILLA_PATH / "param/GameParam/GameParam.parambnd.dcx")
    gwyn_entity_ids = {}  # type: dict[int, int]
    for map_name, msb in maps.msbs.items():
        game_map = maps.GET_MAP(map_name)
        map_entity_ids = all_chr_entity_ids[game_map.area_id, game_map.block_id]

        existing_part_entity_ids = {part.entity_id for part in msb.parts} - {-1}
        base_id = game_map.base_entity_id + 600
        next_entity_id = base_id
        while next_entity_id in existing_part_entity_ids:
            next_entity_id += 1

        entity_id_dict = msb.get_entity_id_dict("parts", "Character")
        for i, entity_id in enumerate(map_entity_ids):

            # Unfortunately, replacing every enemy with a Gwyn is simply too many Gwyns,
            # especially in crowded maps like Undead Burg. Only replacing every fifth
            # enemy, but still disabling the rest.
            if i % 5:
                gwyn_entity_ids[entity_id] = -1  # still disable character when Gwyns are enabled
                continue

            char = entity_id_dict[entity_id]
            if (
                entity_id in NO_GWYNS
                or char.model_name == "c1000"
                or 3900 <= (entity_id % 10000) < 4000  # Vagrants
                or 900 <= (entity_id % 10000) < 4000  # Black Phantoms
            ):
                continue
            char_level = params.Characters[char.character_id]["spEffectID4"]
            gwyn_character_id = max(537050, (char_level - 7000) + 537050)
            msb.parts.new_character(
                name=f"c5370_Gwyn{i}",
                model_name="c5370",
                character_id=gwyn_character_id,  # matches enemy level
                ai_id=537000,  # standard Gwyn
                entity_id=next_entity_id,
                translate=char.translate,
                rotate=char.rotate,
                draw_parent_name=char.draw_parent_name,
            )
            gwyn_entity_ids[entity_id] = next_entity_id
            next_entity_id += 1
            while next_entity_id in existing_part_entity_ids:
                next_entity_id += 1

    return gwyn_entity_ids


def add_bonewheels(maps: MapStudioDirectory, all_chr_entity_ids: dict[tuple[int, int], list[int]]):
    """Add a Bonewheel for every entity ID."""
    params = GameParamBND(VANILLA_PATH / "param/GameParam/GameParam.parambnd.dcx")
    bonewheel_entity_ids = {}  # type: dict[int, int]
    for map_name, msb in maps.msbs.items():
        game_map = maps.GET_MAP(map_name)
        map_entity_ids = all_chr_entity_ids[game_map.area_id, game_map.block_id]

        existing_part_entity_ids = {part.entity_id for part in msb.parts} - {-1}
        base_id = game_map.base_entity_id + 400
        next_entity_id = base_id
        while next_entity_id in existing_part_entity_ids:
            next_entity_id += 1

        entity_id_dict = msb.get_entity_id_dict("parts", "Character")
        for i, entity_id in enumerate(map_entity_ids):
            char = entity_id_dict[entity_id]
            if (
                entity_id in NO_GWYNS
                or char.model_name == "c1000"
                or 3900 <= (entity_id % 10000) < 4000  # Vagrants
                or 900 <= (entity_id % 10000) < 4000  # Black Phantoms
            ):
                continue
            char_level = params.Characters[char.character_id]["spEffectID4"]
            bonewheel_chr_id = max(293050, (char_level - 7000) + 293050)
            msb.parts.new_character(
                name=f"c2930_Bonewheel{i}",
                model_name="c2930",
                character_id=bonewheel_chr_id,  # matches enemy level
                ai_id=293000,  # standard Bonewheel
                entity_id=next_entity_id,
                translate=char.translate,
                rotate=char.rotate,
                draw_parent_name=char.draw_parent_name,
            )
            bonewheel_entity_ids[entity_id] = next_entity_id
            next_entity_id += 1
            while next_entity_id in existing_part_entity_ids:
                next_entity_id += 1

    return bonewheel_entity_ids


def add_patches(maps: MapStudioDirectory):
    """Add Patches to every map, prepared to ambush the player."""

    for i, msb in enumerate(maps.msbs.values()):
        msb.parts.new_character(
            name="c0000_PatchesAmbush",
            model_name="c0000",
            player_id=6320,  # standard Patches
            character_id=6322,  # new enemy Patches with no drop
            ai_id=6320,  # standard Patches
            entity_id=7980 + i,
            translate=(0, 0, 0),
            rotate=(0, 0, 0),
        )


def add_channeler(maps: MapStudioDirectory):
    """Add a troll Channeler to every map, prepared to ambush the player."""

    for i, msb in enumerate(maps.msbs.values()):

        if not any(model.name == "c2370" for model in msb.models.Characters):
            # Add Channeler model to map.
            msb.models.new_character_model(name="c2370")

        msb.parts.new_character(
            name="c2370_TrollChanneler",
            model_name="c2370",
            character_id=237010,  # new Troll Channeler
            ai_id=0,  # only performs one animation (buff dance) and then disappears
            entity_id=7960 + i,
            translate=(0, 0, 0),
            rotate=(0, 0, 0),
        )


def add_models(maps: MapStudioDirectory):
    """Add special "Oops! All X" models to every map for C# use."""
    for i, msb in enumerate(maps.msbs.values()):
        if not any(model.name == "c5370" for model in msb.models.Characters):
            msb.models.new_character_model(name="c5370")  # Gwyn, Lord of Cinder
        if not any(model.name == "c3350" for model in msb.models.Characters):
            msb.models.new_character_model(name="c3350")  # Possessed Tree
        if not any(model.name == "c2930" for model in msb.models.Characters):
            msb.models.new_character_model(name="c2930")  # Bonewheel


def create_events(
    game_map: Map,
    char_entity_ids: list[int],
    gwyn_entity_ids: dict[int, int],
    bonewheel_entity_ids: dict[int, int],
    entity_ai_params: dict[int, int],
):
    """Use above event template strings to print out events to copy-paste into EVS for `game_map`."""
    with Path(f"project/events_templates/{game_map.emevd_file_stem}.evs.py").open("r") as f:
        template = f.read()

    text = ""
    constructor = []

    text += PATCHES_AMBUSH.format(prefix=game_map.flag_prefix, map_variable_name=game_map.variable_name) + "\n"
    constructor.append("PatchesAmbush()")

    channeler_effect = "\n    ".join(
        f"AddSpecialEffect({entity_id}, 5470)" for entity_id in char_entity_ids
    )
    text += CHANNELER_AMBUSH.format(
        prefix=game_map.flag_prefix, map_variable_name=game_map.variable_name, channeler_effect=channeler_effect
    ) + "\n"
    constructor.append("ChannelerAmbush()")

    phantoms = PHANTOM_LISTS[game_map.area_id, game_map.block_id]

    if game_map.variable_name in ("FIRELINK_SHRINE", "UNDEAD_ASYLUM", "ASH_LAKE"):
        # No red phantoms in these maps, so Patches is conscripted again instead.
        text += RED_PHANTOM_AMBUSH_PATCHES.format(
            prefix=game_map.flag_prefix,
            map_variable_name=game_map.variable_name,
        ) + "\n"
    else:
        disable_all_characters = "\n    ".join(f"DisableCharacter(Characters.{phantom})" for phantom in phantoms)
        control_red_phantom_block = "\n    ".join(
            f"{'if' if i == 0 else 'elif'} FlagEnabled({11812900 + i}):\n"
            f"        ControlRedPhantom(0, Characters.{phantom})"
            for i, phantom in enumerate(phantoms)
        )
        text += RED_PHANTOM_AMBUSH.format(
            prefix=game_map.flag_prefix,
            map_variable_name=game_map.variable_name,
            max_random_flag=11812900 + len(phantoms) - 1,
            disable_all_characters=disable_all_characters,
            control_red_phantom_block=control_red_phantom_block,
        ) + "\n"
    constructor.append("RedPhantomAmbush()")

    text += CONTROL_RED_PHANTOM.format(prefix=game_map.flag_prefix) + "\n"
    # No constructor.

    map_piece_count = MAP_PIECE_COUNTS[game_map.area_id, game_map.block_id]
    text += MAKE_WORLD_INVISIBLE.format(
        prefix=game_map.flag_prefix,
        entity_prefix=game_map.base_entity_id // 10000,
        max_id_suffix=8500 + map_piece_count,
    ) + "\n"
    constructor.append("MakeWorldInvisible()")

    disable_gwyns = []
    gwyn_warps = []
    for gwyn_target in char_entity_ids:
        if gwyn_target not in gwyn_entity_ids:
            continue
        gwyn = gwyn_entity_ids[gwyn_target]
        if gwyn == -1:
            continue  # TODO: Maybe disable character anyway? They'll get shredded by Gwyns otherwise. Oh well.
        disable_gwyns.append(f"DisableCharacter({gwyn})")
        gwyn_warps.append(f"DisableCharacter({gwyn_target})")
        gwyn_warps.append(f"EnableCharacter({gwyn})")
    text += OOPS_ALL_GWYNS.format(
        prefix=game_map.flag_prefix,
        disable_gwyns_block="\n    ".join(disable_gwyns),
        gwyn_warp_block="\n    ".join(gwyn_warps),
    ) + "\n"
    # Effect lasts until reload, since I can't be sure exactly which characters should be re-enabled.
    constructor.append("OopsAllGwyns()")

    disable_bonewheels = []
    bonewheel_warps = []
    for bonewheel_target in char_entity_ids:
        if bonewheel_target not in bonewheel_entity_ids:
            continue
        bonewheel = bonewheel_entity_ids[bonewheel_target]
        if bonewheel == -1:
            continue
        disable_bonewheels.append(f"DisableCharacter({bonewheel})")
        bonewheel_warps.append(f"DisableCharacter({bonewheel_target})")
        bonewheel_warps.append(f"EnableCharacter({bonewheel})")
    text += OOPS_ALL_BONEWHEELS.format(
        prefix=game_map.flag_prefix,
        disable_bonewheels_block="\n    ".join(disable_bonewheels),
        bonewheel_warp_block="\n    ".join(bonewheel_warps),
    ) + "\n"
    # Effect lasts until reload, since I can't be sure exactly which characters should be re-enabled.
    constructor.append("OopsAllBonewheels()")

    enable_hyper_aggression = "\n    ".join(
        f"SetAIParamID({entity_id}, {entity_ai + 50})"
        for entity_id, entity_ai in entity_ai_params.items()
    )
    disable_hyper_aggression = "\n    ".join(
        f"SetAIParamID({entity_id}, {entity_ai})"
        for entity_id, entity_ai in entity_ai_params.items()
    )
    text += HYPER_AGGRESSION.format(
        prefix=game_map.flag_prefix,
        enable_hyper_aggression=enable_hyper_aggression,
        disable_hyper_aggression=disable_hyper_aggression,
    ) + "\n"
    constructor.append("HyperAggression()")

    text += "\n"
    for i, enemy_effect_name in enumerate(ENEMY_EFFECTS):
        add_effect = "\n    ".join(f"AddSpecialEffect({entity_id}, {200000 + i})" for entity_id in char_entity_ids)
        text += (
            f"@RestartOnRest\n"
            f"def Enemy{enemy_effect_name}():\n"
            f"    \"\"\" {game_map.flag_prefix}{2200 + i}: Temporary enemy effect. \"\"\"\n"
            f"    Await(TriggerFlags.Enemy{enemy_effect_name})\n"
            f"    {add_effect}\n"
            
            f"    WaitFrames(10)  # give other loaded maps time to trigger\n"
            f"    DisableFlag(TriggerFlags.Enemy{enemy_effect_name})\n"
            f"    return RESTART\n\n\n"
        )
        constructor.append(f"Enemy{enemy_effect_name}()")

    events = template.replace("# <!--!>", "\n    " + "\n    ".join(constructor)) + "\n" + text
    events = events.rstrip("\n") + "\n"
    with Path(f"project/events/{game_map.emevd_file_stem}.evs.py").open("w") as f:
        f.write(events)


def create_common_events():
    with Path(f"project/events_templates/common.evs.py").open("r") as f:
        template = f.read()

    text = ""
    constructor = []

    for i, player_effect_name in enumerate(PLAYER_EFFECTS):

        if player_effect_name == "InstantDeath":
            warning = (
                f"    DisplayBattlefieldMessage(CommonText.InstantDeathWarning, 0)\n"
                f"    Wait(2.0)\n"
            )
        else:
            warning = ""

        text += (
            f"def Player{player_effect_name}():\n"
            f"    \"\"\" 1181{2100 + i}: Temporary player effect. \"\"\"\n"
            f"    Await(TriggerFlags.Player{player_effect_name})\n"
            f"    DisableFlag(TriggerFlags.Player{player_effect_name})\n{warning}"
            f"    AddSpecialEffect(PLAYER, {100000 + i})\n"
            f"    return RESTART\n\n\n"
        )
        constructor.append(f"Player{player_effect_name}()")

    events = template.replace("# <!--!>", "\n    ".join(constructor)) + "\n\n" + text
    events = events.rstrip("\n") + "\n"
    with Path(f"project/events/common.evs.py").open("w") as f:
        f.write(events)


def create_common_entities():
    with Path(f"project/entities_templates/common_entities.py").open("r") as f:
        template = f.read()

    player_enums = []
    for i, player_effect_name in enumerate(PLAYER_EFFECTS):
        player_enums.append(f"Player{player_effect_name} = {11812600 + i}")

    enemy_enums = []
    for i, enemy_effect_name in enumerate(ENEMY_EFFECTS):
        enemy_enums.append(f"Enemy{enemy_effect_name} = {11812700 + i}")

    entities = template.replace("# <!--!>", "\n    ".join(player_enums) + "\n    " + "\n    ".join(enemy_enums))
    entities = entities.rstrip("\n") + "\n"
    with Path(f"project/entities/common_entities.py").open("w") as f:
        f.write(entities)


NO_GWYNS = [
    1000800,
    1010300,
    1010302,
    1010700,
    1010750,
    1010800,
    1010801,
    1010802,
    1100160,
    1100170,
    1100171,
    1100172,
    1200010,
    1200800,
    1200801,
    1210400,
    1210401,
    1210402,
    1210800,
    1210820,
    1210840,
    1300800,
    1310800,
    1310810,
    1320700,
    1320800,
    1400000,
    1400700,
    1400800,
    1410400,
    1410600,
    1410700,
    1410800,
    1410801,
    1410802,
    1500100,
    1500101,
    1500800,
    1510600,
    1510650,
    1510800,
    1510810,
    1510801,
    1510811,
    1600500,
    1600800,
    1600801,
    1600802,
    1600803,
    1600804,
    1700100,
    1700350,
    1700351,
    1700352,
    1700700,
    1700800,
    1800800,
]
PATCHES_AMBUSH = """
@RestartOnRest
def PatchesAmbush():
    \"\"\" {prefix}2000: Patches teleports behind the player and attacks. \"\"\"
    DisableCharacter(Characters.c0000_PatchesAmbush)

    Await(InsideMap({map_variable_name}) and TriggerFlags.PatchesAmbush and IsAlive(Characters.c0000_PatchesAmbush))
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
"""
CHANNELER_AMBUSH = """
@RestartOnRest
def ChannelerAmbush():
    \"\"\" {prefix}2001: Channeler teleports above the player (no gravity) and uses its buff dance. \"\"\"
    DisableCharacter(Characters.c2370_TrollChanneler)

    Await(InsideMap({map_variable_name}) and TriggerFlags.ChannelerAmbush and IsAlive(Characters.c2370_TrollChanneler))
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

    {channeler_effect}

    return RESTART
"""
RED_PHANTOM_AMBUSH = """
@RestartOnRest
def RedPhantomAmbush():
    \"\"\" {prefix}2002: Random red phantom ambushes the player. \"\"\"
    {disable_all_characters}

    Await(InsideMap({map_variable_name}) and TriggerFlags.EnemyAmbush)
    DisableFlag(TriggerFlags.EnemyAmbush)

    DisableFlagRange((11812900, 11812999))
    EnableRandomFlagInRange((11812900, {max_random_flag}))

    {control_red_phantom_block}
    
    Await(FlagEnabled({prefix}5082))

    return RESTART
"""
RED_PHANTOM_AMBUSH_PATCHES = """
@RestartOnRest
def RedPhantomAmbush():
    \"\"\" {prefix}2002: No phantoms in this map, so it acts as an extra Patches trigger. \"\"\"
    Await(InsideMap({map_variable_name}) and TriggerFlags.EnemyAmbush)
    DisableFlag(TriggerFlags.EnemyAmbush)
    if IsAlive(Characters.c0000_PatchesAmbush):
        EnableFlag(TriggerFlags.PatchesAmbush)
    return RESTART
"""
CONTROL_RED_PHANTOM = """
@RestartOnRest
def ControlRedPhantom(_, enemy: int):
    \"\"\" {prefix}5081: `enemy` moves to player and appears. \"\"\"
    DisableFlag({prefix}5082)
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
    EnableFlag({prefix}5082)
"""
MAKE_WORLD_INVISIBLE = """
def MakeWorldInvisible():
    \"\"\" {prefix}2003: Disable all map pieces. Undone only by reload. \"\"\"
    Await(TriggerFlags.InvisibleWorld)   # note you don't need to be standing in the map
    DisableFlag(TriggerFlags.InvisibleWorld)
    for map_piece in range({entity_prefix}8500, {entity_prefix}{max_id_suffix}):
        DisableMapPiece(map_piece)
    # No need to restart.
"""
OOPS_ALL_GWYNS = """
@RestartOnRest
def OopsAllGwyns():
    \"\"\" {prefix}2004: Enable Gwyns and warp them to their paired normal characters. \"\"\"
    {disable_gwyns_block}
    Await(TriggerFlags.OopsAllGwyns)  # note you don't need to be standing in the map
    {gwyn_warp_block}
    WaitFrames(30)  # enough time for other maps to trigger too
    DisableFlag(TriggerFlags.OopsAllGwyns)
    # No need to restart.
"""
OOPS_ALL_BONEWHEELS = """
@RestartOnRest
def OopsAllBonewheels():
    \"\"\" {prefix}2005: Enable Bonewheels and warp them to their paired normal characters. \"\"\"
    {disable_bonewheels_block}
    Await(TriggerFlags.OopsAllBonewheels)  # note you don't need to be standing in the map
    {bonewheel_warp_block}
    WaitFrames(30)  # enough time for other maps to trigger too
    DisableFlag(TriggerFlags.OopsAllBonewheels)
    # No need to restart.
"""
HYPER_AGGRESSION = """
@RestartOnRest
def HyperAggression():
    \"\"\" {prefix}2006: Switch AI param of every enemy to its aggressive version. \"\"\"
    Await(TriggerFlags.HyperAggression or TriggerFlags.HyperAggressionReTrigger)
    
    {enable_hyper_aggression}
        
    # Common EMEVD manages the flags that control this event.
    Await(not TriggerFlags.HyperAggressionReTrigger)
    
    {disable_hyper_aggression}
    
    return RESTART
"""
MAP_PIECE_COUNTS = {(10, 0): 69, (10, 1): 138, (10, 2): 61, (11, 0): 61, (12, 0): 101, (12, 1): 203, (13, 0): 178,
                    (13, 1): 56, (13, 2): 43, (14, 0): 156, (14, 1): 109, (15, 0): 51, (15, 1): 75, (16, 0): 33,
                    (17, 0): 90, (18, 0): 14, (18, 1): 40}
PHANTOM_LISTS = {
    (10, 0): [
        "c2500_0012",
        "c2500_0013",
        "c2500_0014",
        "c2500_0015",
        "c2500_0016",
        "c2660_0002",
        "c1201_0018",
        "c1201_0019",
        "c1201_0020",
        "c1201_0021",
        "c1201_0022",
        "c1201_0023",
        "c1201_0024",
        "c1201_0025",
    ],
    (10, 1): [
        "c2560_0000",
        "c2500_0035",
        "c2500_0036",
        "c2500_0037",
        "c2570_0003",
        "c2540_0014",
        "c2540_0016",
        "c2540_0017",
        "c2550_0024",
        "c2550_0025",
        "c2520_0012",
        "c2520_0013",
    ],
    (10, 2): [
        # TODO: Add some red phantoms to Firelink. Something weird, maybe.
    ],
    (11, 0): [
        "c2840_0011",
        "c2840_0012",
        "c2840_0013",
        "c2840_0014",
        "c2840_0015",
        "c2840_0016",
        "c2840_0017",
        "c2930_0009",
        "c2930_0010",
        "c2930_0011",
        "c2930_0012",
        "c2930_0013",
    ],
    (12, 0): [
        "c2380_0007",
        "c2380_0008",
        "c2380_0009",
        "c2380_0010",
        "c2280_0008",
        "c2280_0009",
        "c2280_0010",
        "c2280_0011",
        "c2270_0002",
        "c2270_0003",
    ],
    (12, 1): [
        "c4120_0011",
        "c4120_0012",
        "c4120_0013",
        "c4130_0039",
        "c4130_0040",
        "c4130_0041",
        "c4130_0042",
        "c4130_0046",
        "c4130_0047",
        "c4130_0048",
        "c4130_0049",
        "c4150_0028",
        "c4150_0029",
        "c4160_0012",
        "c4160_0013",
        "c4150_0030",
        "c4160_0015",
        "c4180_0003",
        "c4180_0005",
        "c4180_0006",
    ],
    (13, 0): [
        "c2900_0034",
        "c2900_0040",
        "c2900_0041",
        "c2900_0054",
        "c2900_0055",
        "c2900_0056",
        "c2900_0057",
        "c2900_0058",
        "c2930_0007",
        "c2930_0008",
        "c2930_0009",
    ],
    (13, 1): [
        "c2910_0022",
        "c2910_0023",
        "c2910_0024",
        "c2910_0025",
        "c2910_0026",
        "c2950_0007",
        "c2950_0008",
        "c2950_0009",
        "c2950_0010",
        "c2950_0011",
    ],
    (13, 2): [
        # TODO: Add some red phantoms.
    ],
    (14, 0): [
        "c2060_0006",
        "c2060_0011",
        "c2060_0015",
        "c2060_0019",
        "c2060_0020",
        "c2810_0003",
        "c2810_0004",
        "c2810_0005",
        "c2810_0006",
        "c2810_0007",
    ],
    (14, 1): [
        "c2240_0007",
        "c2240_0008",
        "c2240_0009",
        "c2240_0010",
        "c2240_0011",
        "c3240_0009",
        "c3240_0010",
        "c3240_0011",
    ],
    (15, 0): [
        "c2690_0012",
        "c2690_0013",
        "c2690_0014",
        "c2690_0015",
        "c2690_0016",
        "c2690_0017",
        "c2690_0018",
        "c2700_0008",
        "c2700_0009",
        "c2700_0010",
    ],
    (15, 1): [
        "c2870_0014",
        "c2870_0015",
        "c2870_0016",
        "c2410_0016",
        "c2410_0017",
        "c2410_0018",
        "c2410_0019",
        "c2410_0020",
        "c2410_0021",
        "c2410_0022",
    ],
    (16, 0): [
        "c2390_0012",
        "c2390_0013",
        "c2390_0014",
        "c2390_0015",
        "c2390_0016",
        "c2390_0017",
    ],
    (17, 0): [
        "c2370_0002",
        "c2370_0003",
        "c2370_0004",
        "c2370_0005",
        "c2710_0015",
        "c2710_0016",
        "c2710_0017",
        "c2710_0018",
        "c3330_0020",
        "c3330_0021",
    ],
    (18, 0): [
        "c2790_0006",
        "c2790_0007",
        "c2790_0008",
        "c2790_0009",
        "c2790_0010",
    ],
    (18, 1): [
        # TODO: Add some red phantoms.
    ],
}
