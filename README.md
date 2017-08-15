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

### Clone the repository
Clone this repository by running ``git clone https://github.com/michi1992/database-logs-analysis`` in your terminal window. 

Also make sure to unzip the ``newsdata.zip`` file and move the ``newsdata.sql`` file into the ``vagrant`` folder.

### Start the virtual machine
From your terminal, inside the vagrant subdirectory, run the command `vagrant up`. This will cause Vagrant to download the Linux operating system and install it. This may take quite a while (many minutes) depending on how fast your Internet connection is.

*Note:* The command ``vagrant up`` threw an error on my machine. I had to enable SVM in my BIOS in order to fix it.

When vagrant up is finished running, you will get your shell prompt back. At this point, you can run `vagrant ssh` to log in to your newly installed Linux VM!

![screenshot of the vagrant login page](https://github.com/michi1992/database-logs-analysis/blob/master/images_for_readme/vagrant_loginscreen.png)

### Prepare the data
Once you are connected to your virtual machine, load the data by entering the following commands: 
```
$ cd /vagrant
$ psql -d news -f newsdata.sql
```
Running this command will connect to your installed database server and execute the SQL commands in the downloaded file, creating tables and populating them with data.

If you want to play around with the database you can do this by running ``psql news`` inside that virtual maschine.

![screenshot of how to run sql-statements against the database](https://github.com/michi1992/database-logs-analysis/blob/master/images_for_readme/run_sql_statements.png)


## Authors

* **Michael Haar** - *Initial work* - [Michael Haar](https://github.com/michi1992)


## License

This project is licensed under the MIT License - see the [LICENSE.md](https://github.com/michi1992/database-logs-analysis/blob/master/LICENSE) file for details
