from cx_Freeze import setup, Executable

base = None


executables = [Executable("Shrok.py", base=base)]

packages = ["discord", "discord.ext", "json", "urllib"]
options = {
    'build_exe': {

        'packages':packages,
    },

}

setup(
    name = "Shrok",
    options = options,
    version = "1.0",
    description = 'CreamyMemers DnD Discord Bot',
    executables = executables
)