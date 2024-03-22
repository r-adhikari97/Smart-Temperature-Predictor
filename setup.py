import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
# "packages": ["os"] is used as example only
build_exe_options = {"include_msvcr": True ,
                     "packages": ['tkinter',
                                  'numpy',
                                  'csv',
                                  'continuous_threading',
                                  'time',
                                  'csv',
                                  'Stats',
                                  'R_W_Script',
                                  'Connect'],"excludes": []}
executables=[Executable(r"C:\Users\aviat\AppData\Local\Programs\Python\Python311\PRACTICE\Temp_\MAIN.py")]

# base="Win32GUI" should be used only for Windows GUI app
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name="Temperature Predictor",
    version="1.0",
    author = "Raj Adhikari",
    description="IoT and Stats",
    options={"build_exe": build_exe_options},
    executables = executables
)






















      
      
                        
                
