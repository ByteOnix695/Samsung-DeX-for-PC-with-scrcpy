import subprocess
import platform

resolution = "[YOUR DISPLAY RES]"

cmd = [
    "scrcpy", 
    f"--new-display={resolution}/160", 
    "--mouse=uhid", 
    "--keyboard=uhid"
]

try:
    subprocess.run(cmd, check=True)
except Exception as e:
    print(f"Error: {e}")
