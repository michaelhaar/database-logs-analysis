# database-logs-analysis
This project was part of my Full Stack Web Developer Nanodegree at Udacity. It's main target is to stretch our SQL database skills

## Installing the Virtual Machine
We are using a virtual machine (VM) to run an SQL database server and a Python script that uses it. The VM is a Linux server system that runs on top of your own computer.

### Install VirtualBox
VirtualBox is the software that actually runs the virtual machine. [You can download it from virtualbox.org, here](https://www.virtualbox.org/wiki/Downloads). Install the platform package for your operating system. You do not need the extension pack or the SDK. You do not need to launch VirtualBox after installing it; Vagrant will do that.

**Ubuntu users:** If you are running Ubuntu 14.04, install VirtualBox using the Ubuntu Software Center instead. Due to a reported bug, installing VirtualBox from the site may uninstall other software you need.

### Install Vagrant
Vagrant is the software that configures the VM and lets you share files between your host computer and the VM's filesystem. [Download it from vagrantup.com](https://www.vagrantup.com/downloads.html). Install the version for your operating system.

**Windows users:** The Installer may ask you to grant network permissions to Vagrant or make a firewall exception. Be sure to allow this.

If Vagrant is successfully installed, you will be able to run `vagrant --version`
in your terminal to see the version number.

## Usage

### Start the virtual machine
From your terminal, inside the vagrant subdirectory, run the command `vagrant up`. This will cause Vagrant to download the Linux operating system and install it. This may take quite a while (many minutes) depending on how fast your Internet connection is.
When vagrant up is finished running, you will get your shell prompt back. At this point, you can run `vagrant ssh` to log in to your newly installed Linux VM!


## Authors

* **Michael Haar** - *Initial work* - [Michael Haar](https://github.com/michi1992)


## License

This project is licensed under the MIT License - see the [LICENSE.md](https://github.com/michi1992/database-logs-analysis/blob/master/LICENSE) file for details
