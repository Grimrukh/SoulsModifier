from pathlib import Path

from soulstruct.darksouls1r.ezstate import TalkESDBND

from file_paths import MOD_PATH, INSTALLER_PATH


def install_talk():
    """Only Manus bonfire has been modified (to always allow warping)."""
    m12_01_talkesd = TalkESDBND(Path("project/talk/m12_01_00_00"))
    m12_01_talkesd.write(MOD_PATH / "script/talk/m12_01_00_00.talkesdbnd.dcx")
    m12_01_talkesd.write(INSTALLER_PATH / "script/talk/m12_01_00_00.talkesdbnd.dcx")
