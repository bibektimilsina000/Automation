import platform
import subprocess
import os

def install_chromedriver():
    os_name = platform.system()
    if os_name == 'Linux':

        distro  = platform.platform()
         

        if 'debian' in distro.lower():

            subprocess.run(['sudo', 'apt-get', 'update'])

            subprocess.run(['sudo', 'apt-get', 'install', 'chromedriver'])

        elif 'red hat' in distro.lower() or 'centos' in distro.lower():

            subprocess.run(['sudo', 'yum', 'install', '-y', 'epel-release'])

            subprocess.run(['sudo', 'yum', 'install', '-y', 'chromedriver'])

        elif 'arch' in distro.lower():

            subprocess.run(['sudo', 'pacman', '-Sy'])

            subprocess.run(['yay', '-S', 'chromedriver'])
        else:
            print(f"Unsupported distribution: {distro}  ")
    elif os_name == 'Darwin':

        if not os.system('/usr/bin/which brew'):
            subprocess.run(
                ['/usr/bin/ruby', '-e', '$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)'])

        subprocess.run(['brew', 'cask', 'install', 'chromedriver'])
    elif os_name == 'Windows':

        if not os.system('choco'):
            subprocess.run(['@powershell -NoProfile -ExecutionPolicy unrestricted -Command "iex ((New-Object System.Net.WebClient).DownloadString(\'https://chocolatey.org/install.ps1\'))" && SET PATH=%PATH%;%ALLUSERSPROFILE%\\chocolatey\\bin'])

        subprocess.run(['choco', 'install', 'chromedriver'])
    else:
        print(f"Unsupported operating system: {os_name}")
