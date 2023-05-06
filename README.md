# budhabot_for_linuxcommand_healthchecks
WE have developed a rule based bot for Linux health check and basic Linux commands for Linux operating system<br>
REQUIREMENTS:

To install VirtualBox and set up Ubuntu and Python in it, please follow the following steps:

1.Download and install VirtualBox

-Go to the VirtualBox website at https://www.virtualbox.org/ and download the appropriate version for your operating system.
-Once downloaded, follow the installation wizard to install VirtualBox on your computer.

2.Download Ubuntu ISO file

-Go to the Ubuntu website at https://ubuntu.com/download and download the appropriate version of Ubuntu ISO file.
-Make sure to download the Desktop version of Ubuntu.

3.Create a new virtual machine in VirtualBox

-Open VirtualBox and click on the "New" button.
-Give your virtual machine a name, choose "Linux" as the type, and "Ubuntu (64-bit)" as the version.
-Set the amount of memory you want to allocate to your virtual machine. The recommended amount is at least 2 GB.
-Choose "Create a virtual hard disk now" and click "Create".

4.Install Ubuntu on the virtual machine

-Select the newly created virtual machine and click on "Start".
-In the first screen, select the Ubuntu ISO file you downloaded earlier as the startup disk.
-Follow the installation wizard to install Ubuntu on your virtual machine.

5.Install Python on Ubuntu

-Open a terminal window on your Ubuntu virtual machine.
-Type the following command to update the package list:
        sudo apt-get update
-Type the following command to install Python 3:
        sudo apt-get install python3
-Verify that Python has been installed by typing the following command:
        python3 --version
