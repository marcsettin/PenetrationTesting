# Penetration Testing
This software is designed with a suite of scripts that all perform a separate stage of the testing and generate a report of possible vulnerabilities. In order to test this in a safe way this project will have a target hosted on an Oracle VM Virtualbox. The virtual machine will be Metasploitable 3, which is a VM that is built from the ground up with a large amount of security vulnerabilities.

## Getting Started
------------------

System Requirements:
* OS capable of running all of the required applications listed below
* VT-x/AMD-V Supported Processor recommended
* 65 GB Available space on drive
* 4.5 GB RAM

Requirements:

* [Packer](https://www.packer.io/intro/getting-started/install.html)
* [Python 3](https://www.python.org/downloads/)
* [Vagrant](https://www.vagrantup.com/docs/installation/)
* [Vagrant Reload Plugin](https://github.com/aidanns/vagrant-reload#installation)
* [VirtualBox](https://www.virtualbox.org/wiki/Downloads)
* Internet connection

## Building Metasploitable 3
----------------------------

### Quickstart

To use the prebuilt images provided at https://app.vagrantup.com/rapid7/ create a new local metasploitable workspace:

Linux users:
```
mkdir metasploitable3-workspace
cd metasploitable3-workspace
curl -O https://raw.githubusercontent.com/rapid7/metasploitable3/master/Vagrantfile && vagrant up
```
Windows users:
```
mkdir metasploitable3-workspace
cd metasploitable3-workspace
Invoke-WebRequest -Uri "https://raw.githubusercontent.com/rapid7/metasploitable3/master/Vagrantfile" -OutFile "Vagrantfile"
vagrant up
```

### To build automatically:

1. - On **Linux/OSX** run `./build.sh windows2008` to build the Windows box or `./build.sh ubuntu1404` to build the Linux box. If /tmp is small, use `TMPDIR=/var/tmp ./build.sh ...` to store temporary packer disk images under /var/tmp.
   - On **Windows**, open powershell terminal and run `.\build.ps1 windows2008` to build the Windows box or `.\build.ps1 ubuntu1404` to build the Linux box. If no option is passed to the script i.e. `.\build.ps1`, then both the boxes are built.
2. If both the boxes were successfully built, run `vagrant up` to start both. To start any one VM, you can use:
    - `vagrant up ub1404` : to start the Linux box
    - `vagrant up win2k8` : to start the Windows box
3. When this process completes, you should be able to open the VM within VirtualBox and login. The default credentials are U: `vagrant` and P: `vagrant`.

### To build manually:

1. Clone [Metasploitable 3](https://github.com/rapid7/metasploitable3) repo and navigate to the main directory.
2. Build the base VM image by running `packer build --only=<provider> ./packer/templates/windows_2008_r2.json` where `<provider>` is your preferred virtualization platform. Currently `virtualbox-iso`, `qemu`, and `vmware-iso` providers are supported. This will take a while the first time you run it since it has to download the OS installation ISO.
3. After the base Vagrant box is created you need to add it to your Vagrant environment. This can be done with the command `vagrant box add packer/builds/windows_2008_r2_*_0.1.0.box --name=metasploitable3-win2k8`.
4. Use `vagrant plugin install vagrant-reload` to install the reload vagrant provisioner if you haven't already.
5. To start the VM, run the command `vagrant up win2k8`. This will start up the VM and run all of the installation and configuration scripts necessary to set everything up. This takes about 10 minutes.
6. Once this process completes, you can open up the VM within VirtualBox and login. The default credentials are U: vagrant and P: vagrant.

## Running Penetration Tester
------------------------------

### Run Against Vulnerable Target
1. Clone this repo and navigate to the main directory.
2. Open up the Metasploitable 3 within VirtualBox and login. The default credentials are U: vagrant and P: vagrant.
3. Navigate to the command prompt on the VM, run `ipconfig` to get the IP address for the vulnerable targert.
4. Run `python Main.py` on your local machine then select option 2 for remote host and enter the vulnerable target's IP to begin testing.

### Other Options
1. (Local Host) Perform tests against local machine.
2. (Remote Host) Perform tests against remote host.
3. (Ping Sweep) Ping sweep a local or remote network and select a target. 


