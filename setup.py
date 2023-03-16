import sys
from cx_Freeze import setup, Executable

build_exe_options = {"packages": ["os"], "includes": [""], "include_files": []}

base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name="APP CADU",
    version="1.0",
    description="O melhor app do mundo",
    options={"build_exe": build_exe_options},
    executables=[Executable(script="main.py", base=base)]
)