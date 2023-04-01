import platform
import subprocess

def install_tkinter():
    # get the current platform
    curr_platform = platform.system()

    # install tkinter for Linux
    if curr_platform == "Linux":
        
        
        
            distro = platform.platform().lower()
    
            if distro in ['debian', 'ubuntu']:
                subprocess.run(['sudo', 'apt-get', 'install', 'python3-tk'], check=True)
            elif distro == 'fedora':
                subprocess.run(['sudo', 'dnf', 'install', 'python3-tkinter'], check=True)
            elif distro in ['centos', 'redhat', 'rhel']:
                subprocess.run(['sudo', 'yum', 'install', 'python3-tkinter'], check=True)
            elif distro == 'arch':
                subprocess.run(['sudo', 'pacman', '-S', 'tk'], check=True)
            elif distro == 'opensuse':
                subprocess.run(['sudo', 'zypper', 'install', 'python3-tk'], check=True)
            else:
                print(f"Error: Unsupported distribution: {distro}")
        
        
        
        
        
        
       
            
    
    # install tkinter for macOS
    elif curr_platform == "Darwin":
        try:
            subprocess.run(["brew", "install", "tcl-tk"])
        except subprocess.CalledProcessError:
            print("Error installing tkinter. Please install it manually.")

    # skip installation for Windows
    elif curr_platform == "Windows":
        print("Skipping tkinter installation on Windows.")
        
    # unsupported platform
    else:
        print(f"{curr_platform} platform is not supported.")

if __name__ == "__main__":
    install_tkinter()