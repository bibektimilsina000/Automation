import sys
import subprocess


def install_requirements():
    try:
        subprocess.check_call(
            [sys.executable, '-m', 'pip', 'install', '-r', 'requirements.txt'])
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
    else:
        print("All packages from requirements.txt installed successfully!")
        
install_requirements()