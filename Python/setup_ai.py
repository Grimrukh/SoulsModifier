import pickle
from pathlib import Path

from soulstruct.darksouls1ptde.ai import AIDirectory

from file_paths import VANILLA_PATH, MOD_PATH, INSTALLER_PATH


def install_ai():
    ai = AIDirectory(VANILLA_PATH / "script")
    add_goals_to_common(ai)
    with Path("project/ai.ssp").open("wb") as f:
        pickle.dump(ai, f)
    ai.write(MOD_PATH / "script")
    ai.write(INSTALLER_PATH / "script")


def add_goals_to_common(ai: AIDirectory):
    patches_goal = ai.Catacombs.get_goal(6320).copy()
    ai.Common.goals.append(patches_goal)
    bonewheel_goal = ai.Catacombs.get_goal(293000).copy()
    ai.Common.goals.append(bonewheel_goal)
    gwyn_goal = ai.KilnOfTheFirstFlame.get_goal(537000).copy()
    ai.Common.goals.append(gwyn_goal)
    tree_goal = ai.DarkrootGarden.get_goal(335000).copy()
    ai.Common.goals.append(tree_goal)

    # Remove goals from non-Common BNDs to avoid the weird DSR clash problem.
    for map_name, luabnd in ai.luabnds.items():
        if map_name == "Common":
            continue
        for goal_to_remove in (6320, 293000, 335000, 537000):
            try:
                goal = luabnd.get_goal(goal_to_remove)
            except KeyError:
                pass
            else:
                luabnd.goals.remove(goal)
