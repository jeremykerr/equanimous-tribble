# equanimous-tribble

This is just a test application so that I can learn a bit more about the life of applications from inception to implementation, including all the phases from learning the platforms to building the end product. The application itself will probably be a simple shopping cart application, just like any of the other thousands of shopping cart applications that exist. Nothing will make it special or different, other than the inclusion of what was involved to get each feature up and running.

*Any subsection in this documentation that includes information pulled from a cited source is made available under that source's license, if that license conflicts with the terms of the MIT license. If you have a citation concern or would like to request specific citation formatting, please email jeremy.p.kerr@gmail.com. Thank you.*

## Contents

* Hardware Required
* Raspberry Pi Installation and Initial Configuration
  * Loading Raspbian onto a micro SD card
  * Configuring Raspbian on your Raspberry Pi
    * Expanding the filesystem
      * Jessie
      * Wheezy
    * Disabling the User Interface and default login
      * Jessie
      * Wheezy
    * Changing the Hostname
    * Modifying Location, Time, and Keyboard Settings
    * Changing your password
    * Enabling SSH connections over the local network
    * Configuring hostnames for SSH
  * Updating the Raspbian OS and software packages
* Using Flask on the Raspberry Pi
  * Install Flask for Raspberry Pi
  * Build a simple hello world application
  * Allow web access to the application
    * Allow web access over the local network
    * **TODO:** *Allow web access over the internet*
**TODO:** *Visiting your site by its IP Address*
      * Installing No-IP for Dynamic DNS
**TODO:** *Visiting your application by its domain name*
  * Running the application
  * Closing the application
* **TODO:** *Using PostgreSQL on the Raspberry Pi*
  * Installing PostgreSQL
  * Running the PostgreSQL postmaster
  * Changing the default PostgreSQL credentials
  * **TODO:** *Letting PostgreSQL listen to a machine on the local network on port 5432*
  * **TODO:** *Connecting to the PostgreSQL instance*
* Git setup
* **TODO:** *Application Development*

### Hardware Required

In order to fully follow along with these instructions, you will need the following items. I used two separate Raspberry Pi units, one for the database machine and one for the web interface machine, though you can install both requirements on a single unit with decreased performance if cost is a factor.

* 1 or more Raspberry Pies
* 1 or more micro usb chargers (standard phone chargers usually work)
* 1 or more micro SD cards (I used 32 GB micro SD cards)
* 1 computer on the same network (Ideally it is running a unix based OS, though you can look up instructions on the web for flashing the Raspbian image to a micro SD card on Windows and for using PuTTy as an SSH terminal.)
* 1 micro SD card to USB adapter (An adapter for a different port available on your local PC would also be fine.)
* 1 network switch (Any generic network switch should be fine, I used a TP-Link 5-Port Gigabit Desktop Switch. This is a soft requirement, if you have 2 extra ethernet ports available on your primary modem/router/switch you can plug the Raspberry Pi units into those instead.)
* 3 ethernet cables (These are for the Raspberry Pi units and the network switch.)
* 1 power strip
* 1 USB keyboard (You can install the Raspberry Pi units separately. If you intend to use them directly each time as opposed to using them remotely through SSH you will need two instead.)
* 1 USB mouse (This is assuming Raspberry Pi units are installed separately.)
* 1 HDMI cable (This is assuming Raspberry Pi units are installed separately.)
* 1 HDMI monitor + power source (This is assuming Raspberry Pi units are installed separately.)

### Raspberry Pi Installation and Initial Configuration

#### Loading Raspbian onto a micro SD card

Raspberry Pi has outstanding documentation for getting up and running. The documentation is much more likely to contain up to date information and more detail concerning the specific details in implementation. The implementation steps for loading a Raspbian image onto a micro SD card were pulled from the following source, and are available under the Creative Commons license listed on their website.

https://www.raspberrypi.org/documentation/installation/installing-images/linux.md

These instructions for loading Raspbian onto a micro SD card are relevant for unix based operating systems. They are made with the assumption that you have a micro SD card and either a port on your computer or an adapter you can plug into your computer that is available to plug the micro SD card into.

The first thing you should do is determine what devices are mounted on your computer (without the micro SD card plugged in). Run the following command:

    jeremykerr@jeremykerr ~ $ df -h

Next, insert your micro SD card into your PC and run the command again to determine what partitions it contains.

    jeremykerr@jeremykerr ~ $ df -h

The new entries are partitions stored on your micro SD card. For each entry, the Filesystem column includes the device name and partition number. For me, they were structured as '/dev/sdc1' (on a blank micro SD card) and 'dev/sdc1', '/dev/sdc2' on cards that had prior versions of Raspbian installed (when reimaging a micro SD card for a fresh install). For names structured like this, '/dev/sdc' is the device name and '1', '2' are partition numbers.

For each partition entry, unmount it using the following command (modified with the appropriate partition number). Be very careful when typing any partitioning commands, since they can overwrite your hard drive and other drives if you type the wrong entries. All partition entries need to be unmounted in order to flash the entire micro SD card.

    jeremykerr@jeremykerr ~ $ umount /dev/sdc1

Write the Raspbian image to your micro SD card using the device name without the partition number. You only have to do this once for each micro SD, since all the partitions on it should have been unmounted. Be very careful to use the correct device name in order to avoid accidentally overwriting other drives. You can try as a normal user, but you may require super user permissions in order to accomplish this step.

    jeremykerr@jeremykerr ~ $ sudo dd bs=4M if=2015-09-24-raspbian-jessie.img of=/dev/sdc

I tried installing PostgreSQL 9.4 on the Jessie build, but it failed. As a workaround, I'm going to be using Wheezy for my database unit until I can get a Jessie build with PostgreSQL 9.4 installed. The command below resembles what you might use to load Wheezy onto a micro SD card.

    jeremykerr@jeremykerr ~ $ sudo dd bs=4M if=2015-05-05-raspbian-wheezy.img of=/dev/sdc

It's very likely that this will take awhile, and as entered it is not verbose, so your terminal will look hung. Don't panic, just let it go for 10-15 minutes if need be. It took 5 minutes on my system using the specific brands of micro SD cards I purchased.

After this command is finished running, your micro SD card should contain the Raspbian operating system.

#### Configuring Raspbian on your Raspberry Pi

Plug your micro SD card into your Raspberry Pi and power it on. To power in a Raspberry Pi, you should just need to plug in the micro USB charger. It turns on automatically. You should plug in the micro SD card before you plug in the micro USB power source.

With builds after and including Jessie (the build I used), the default behavior is to launch the User Interface instead of a command line interface. Since these units are going to serve as a web server and a database server, they don't require their own user interfaces. Instead, we want that performance to go to their ability to serve remote clients.

##### Expanding the filesystem

###### Jessie

Open the System configuration in order to expand the filesystem (to use the full SD card). After that we will reboot and disable the User Interface.

```
[Menu]
[Preferences]
[Raspberry Pi Configuration]
[System]
[Expand Filesystem]
```
Press OK to expand the filesystem. Then press OK to apply the configuration settings. When prompted to reboot, select yes. Any other changes applied through this menu will not persist after the reboot.

###### Wheezy

The system configuration opens by default, so you can simply select the following options.

```
[1 Expand Filesystem]
<OK>
```

When you select [Finish] after changing this option, if it prompts you to reboot, select [Yes].

##### Disabling the User Interface and default login

###### Jessie

Now we can disable the User Interface and disable the default behavior of logging in as user pi.

```
[Menu]
[Preferences]
[Raspberry Pi Configuration]
[System]
```

Apply the following settings:

```
[ ] Login as user 'pi' # Uncheck this box
Boot: ( ) To Desktop (*) To CLI # Command Line Interface
```

Press OK to apply the configuration settings. When prompted to reboot, select yes. This time it should boot into a command line interface. Login using the default credentials.

```
raspberrypi login: pi
password: raspberry
```

###### Wheezy

By default, Wheezy builds boot to the Console requiring a login, so these settings don't need to be manually applied. Nevertheless, if you want to apply them, you can.

To disable the User Interface and require a login, select the following options.

```
[3 Enable Boot to Desktop/Scratch]
[Console Text console, requiring login (default)]
```

The default credentials are the same as on a Jessie build.

```
raspberrypi login: pi
password: raspberry
```

##### Changing the Hostname

Next we will want to change the hostname to something meaningful. This is just what the Raspberry Pi calls itself. When you are in a terminal, you will see a prompt formatted as username@hostname ~ $.

    pi@raspberrypi ~ $ sudo raspi-config

Select the following options to change the hostname.

```
[8 Advanced Options]
[A2 Hostname]
```

Next you will be asked to name your Raspberry Pi. I called my units 'web-dev' and 'db-dev'.

##### Modifying Location, Time, and Keyboard Settings

You should modify your location settings, time settings, and keyboard settings. This is important for making your Raspberry Pi accessible over the local network. Typing a password in a USA keyboard layout will not necessarily validate when typing the same password in a UK layout, which can create problems when trying to ssh in while using password authentication.

Select the following options to update your Locale.

```
[4 Internationalisation Options]
[I1 Change Locale]
```

Use the space bar to deselect whatever locale is selected by default, and the space bar to select the locale you prefer. I selected [en_US.UTF-8 UTF-8]. Press enter to continue, and when prompted to select a locale for the system environment, select the equivalent locale to what you chose prior. I chose [en_US.UTF-8]. If you don't see your option, but there is an [Other] option available, choose that in order to see more options.

Change your time zone using the following options.

```
[4 Internationalisation Options]
[I2 Change Timezone]
```

Next, select your preferences for time zone. I chose [US], followed by [Mountain].

Now we can change the keyboard settings to be appropriate for the keyboard you are using.

```
[4 Internationalisation Options]
[I3 Change Keyboard Layout]
[Generic 104-Key PC] # You may choose another keyboard layout if you prefer, but this is a pretty consistent standard for off brand keyboards.
[Other]
[English (US)]
[English (US)]
The default for the keyboard layout
No compose key
Use Control+Alt+Backspace to terminate the X server? <Yes>
```

This is a good time to reboot your unit in order to make sure that keyboard layout changes were applied before resetting your password. It probably would be fine if you didn't reboot, but I prefer to be safe rather than having to rebuild everything because I can't login.

Choose [Finish] in order to apply the changes you've made and then exit the configuration utility. If prompted, select [Reboot Now]. Otherwise, type the following command into the terminal in order to reboot.

    pi@web-dev ~ $ sudo shutdown -r now

##### Changing your password

When you log back in after your unit comes back online, enter into the configuration utility one last time to change your password.

    pi@web-dev ~ $ sudo raspi-config

```
[2 Change User Password]
```

Follow the prompts in order to change your password to a desired password.

Choose [Finish] in order to apply the changes you've made.

##### Enabling SSH connections over the local network

By default, your Raspberry Pi is set to allow SSH connections on the internal network. If you would like to verify that SSH is turned on, you can using the following steps.

Open the Raspberry Pi config utility to enable ssh.

    pi@web-dev ~ $ sudo raspi-config

```
[8 Advanced Options]
[A4 SSH]
[Enable]
[OK]
[Finish]
```

Get the eth0 inet address of the Raspberry Pi device in order to be able to ssh in.

    pi@web-dev ~ $ ifconfig

```
eth0      Link encap:Ethernet  HWaddr b8:27:eb:7f:8d:fa  
          inet addr:10.0.0.7  Bcast:10.0.0.255  Mask:255.255.255.0
          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
          RX packets:45485 errors:0 dropped:4 overruns:0 frame:0
          TX packets:4089 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1000 
          RX bytes:10284766 (9.8 MiB)  TX bytes:415834 (406.0 KiB)

lo        Link encap:Local Loopback  
          inet addr:127.0.0.1  Mask:255.0.0.0
          UP LOOPBACK RUNNING  MTU:65536  Metric:1
          RX packets:8 errors:0 dropped:0 overruns:0 frame:0
          TX packets:8 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:0 
          RX bytes:1104 (1.0 KiB)  TX bytes:1104 (1.0 KiB)
```

> eth0 inet addr:10.0.0.7    # web-dev
> eth0 inet addr:10.0.0.21    # db-dev

You should now be able to log in from a different machine on the same network.

    jeremykerr@jeremykerr ~ $ ssh pi@10.0.0.7    # web-dev
    jeremykerr@jeremykerr ~ $ ssh pi@10.0.0.21    # db-dev

##### Configuring hostnames for SSH

In order to be able to associate eth0 inet addresses with hostnames, you can add a config file to the ~/.ssh directory in the device that you'd like to be able to login from. This allows ssh to read options from the configuration file so that you don't have to specify them in the command each time. Before making the config file, you can generate keys for key based authentication, rather than using your password each time.

    jeremykerr@jeremykerr ~ $ cd /.ssh
    jeremykerr@jeremykerr ~/.ssh $ ssh-keygen -b 4048 -t rsa -C "Home"

It will prompt you for a filename to save with and a password. To save with a default filename (id_rsa and id_rsa.pub) in the current directory, simply hit [ENTER]. After, enter a passphrasse twice. This will be used each time you use your key, so that nobody else can use it.

    jeremykerr@jeremykerr ~/.ssh $ touch ~/.ssh/config
    jeremykerr@jeremykerr ~/.ssh $ vi ~/.ssh/config

For each device that you would like to be able log into by hostname on the local network, you need to specify the host (name), hostname (location), port (if not default), user (if you are not the same user), and your identity file for key-based authentication.

```
Host web-dev
    Hostname 10.0.0.7
    Port 22
    User pi
    IdentityFile ~/.ssh/id_rsa

Host db-dev
    Hostname 10.0.0.21
    Port 22
    User pi
    IdentityFile ~/.ssh/id_rsa
```

To insert text in vi, press 'i' (for Insert). Type the desired text to insert. To stop inserting text, press [ESC]. To save changes and quit, press [:][w][q][ENTER].

You need to create a ~/.ssh folder on each unit you want to use key authentication for as well.

    pi@web-dev ~ $ mkdir .ssh
    pi@db-dev ~ $ mkdir .ssh

You also need to transfer the id_rsa.pub file you've created to each unit you'd like to be able to log in to remotely.

    jeremykerr@jeremykerr ~/.ssh $ scp ~/.ssh/id_rsa.pub pi@10.0.0.7:~/.ssh/id_rsa.pub
    jeremykerr@jeremykerr ~/.ssh $ scp ~/.ssh/id_rsa.pub pi@10.0.0.21:~/.ssh/id_rsa.pub

On each machine, append the id_rsa.pub file to the list of authorized keys.

    pi@web-dev ~/.ssh $ cat id_rsa.pub >> authorized_keys
    pi@db-dev ~/.ssh $ cat id_rsa.pub >> authorized_keys

After saving ~/.ssh/config, you should be able to ssh into each unit using its host entry.

    jeremykerr@jeremykerr ~ $ ssh web-dev
    jeremykerr@jeremykerr ~ $ ssh db-dev

#### Updating the Raspbian OS and software packages

To update your package lists so that you can access the most up to date versions of the software you're running:

    pi@web-dev ~ $ sudo apt-get update

To install the most up to date versions of the software you're running:

    pi@web-dev ~ $ sudo apt-get upgrade

To clean the memory used by installation files:

    pi@web-dev ~ $ sudo apt-get clean

To view the current memory usage:

    pi@web-dev ~ $ df -h

### Using Flask on the Raspberry Pi

#### Install Flask for Raspberry Pi

*At the time of this writing, Raspberry Pi does not support a version of Python 3 that meets the requirements for Flask, so we'll be using Python 2.*

Install pip (the Python package index) in order to install Flask.

    pi@web-dev ~ $ sudo apt-get install python-pip

Install Flask (a microforamework for a Python based web server).
http://flask.pocoo.org/

    pi@web-dev ~ $ sudo pip install Flask

#### Build a simple hello world application

Create and open a new file called "hello.py".

    pi@web-dev ~ $ touch hello.py
    pi@web-dev ~ $ vi hello.py

Some code needs to be written in order to create the server instance and to return a "Hello, world." string when a request is made to the application. One thing worth mentioning is that app.debug is being set to False in the following code. The property app.debug can be used to dynamically reload the source file (hello.py) whenever it is changed, which is convenient when developing locally on a machine that is not accepting requests from the web. However, this dynamic reloading makes it possible for a malicious attacker to run arbitrary code through your web application, so app.debug should never be set to True on an externally visible machine. Read the Flask documentation for more details on that. The other thing worth noting is that app.run is passed an argument, host='0.0.0.0'. This allows the server to be externally visible (so if you don't set this argument before attempting to visit your site from another machine on the same network or a different network, you will get a connection denied error).

To insert within the vi editor:

    [ESC]
    [i]

Type manually:

```
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello_world():
  return "Hello, world."

if __name__ == "__main__":
  app.debug = False
  app.run(host='0.0.0.0')

```

To save changes within the vi editor, press the following keys.

    [ESC]
    [:][w][q]
    [ENTER]

#### Allow web access to the application

##### Allow web access over the local network

View the iptables rules in place.

    pi@web-dev ~ $ sudo iptables -L

Add an accept rule in order to receive requests over the specified port (5000) from other machines on the local network. Then list the rules again to verify it was added.

    pi@web-dev ~ $ sudo iptables -I INPUT -p tcp --dport 5000 -j ACCEPT
    pi@web-dev ~ $ sudo iptables -L

The commands that are used to save and restore iptables commands need to be run inside a shell console (sh -c). Creating these requires superuser privileges.

Save the iptables rule set so you don't have to recreate it from scratch.

    pi@web-dev ~ $ sudo sh -c "iptables-save > /etc/iptables.rules"

Later, if you want to restore the rule set (say after a reboot), you can use iptables-restore.

    pi@web-dev ~ $ sudo sh -c "iptables-restore < /etc/iptables.rules"

Restart IP Tables to activate the new rule set.

    pi@web-dev ~ $ sudo ifconfig eth0 down
    pi@web-dev ~ $ sudo ifconfig eth0 up

##### **TODO:** *Allow web access over the internet*

**TODO:** *Visiting your site by its IP Address*

###### Installing No-IP for Dynamic DNS

Go to the No-IP website and create an account (you need it for the configuration in the installation).

> http://www.noip.com/

Create a directory to install No-IP in, and navigate to that directory.

    pi@web-dev ~ $ mkdir /home/pi/noip
    pi@web-dev ~ $ cd /home/pi/noip

Download and extract the No-IP application.

    pi@web-dev /home/pi/noip $ wget http://www.no-ip.com/client/linux/noip-duc-linux.tar.gz
    pi@web-dev /home/pi/noip $ tar vzxf noip-duc-linux.tar.gz

Go to the extracted directory and install the application.

    pi@web-dev /home/pi/noip $ cd noip-2.1.9-1/
    pi@web-dev /home/pi/noip/noip-2.1.9-1 $ sudo make
    pi@web-dev /home/pi/noip/noip-2.1.9-1 $ sudo make install

**TODO:** *Visiting your application by its domain name*

#### Running the application

To run the application in the open terminal:

    pi@web-dev ~ $ python hello.py

To run the application in the background:

    pi@web-dev ~ $ python hello.py &

Running the application in the background will tell you the pid (process id) before giving you a command prompt.

> [1] 3472

If the earlier instructions on allowing web access over the local network were followed, any computer on the network should now be able to access 10.0.0.7:5000 (or whatever the relevant eth0 inet address is) and see the "Hello, world." string. To see the eth0 inet address, type ifconfig at the command prompt.

#### Closing the application

To close the application in the open terminal:

    [Ctrl] + [C]

To find the application in the background:

    pi@web-dev ~ $ pgrep python

> 3472

To close the application in the background, type kill followed by the pid returned from the previous command.

    pi@web-dev ~ $ kill 3472

### **TODO:** *Using PostgreSQL on the Raspberry Pi*
#### Installing PostgreSQL
 
Raspbian is a Debian 7 (wheezy) build, and is currently supported by PostgreSQL. 
Raspbian is a Debian 8 (jessie) build, and in testing was not able to build PostgreSQL. I am currently looking into it, but in the meantime, my database unit is running Wheezy.

https://wiki.postgresql.org/wiki/Apt

Rubens Souza posted an excellent article on installing PostgreSQL on a Raspberry Pi 2. Some of the following information is directly pulled from that source.

http://raspberrypg.org/2015/06/step-5-update-installing-postgresql-on-my-raspberry-pi-1-and-2/

Some of the documentation included below was pulled from on PostgreSQL.org.

http://www.postgresql.org/download/linux

To build PostgreSQL from source on a Raspberry Pi, you have to add the PostgreSQL Apt Repository. In order to create the file to store the PostgreSQL Apt Repository location to, you need to have superuser permissions. The touch command is not necessary, but was included in case any readers would prefer to use an editor other than Vi, such as Nano.

    pi@db-dev ~ $ sudo touch /etc/apt/sources.list.d/pgdg.list
    pi@db-dev ~ $ sudo vi /etc/apt/sources.list.d/pgdg.list

Save the following line in this file.

    deb-src http://apt.postgresql.org/pub/repos/apt/ wheezy-pgdg main

If you are attempting to build on Jessie, you should use the following line instead.

    deb-src http://apt.postgresql.org/pub/repos/apt/ jessie-pgdg main

This allows us to access the PostgreSQL apt repository. In the PostgreSQL documentation, they use deb, which means they are building from binary sources. Because we are compiling from source packages from the PostgreSQL Apt repository, we will use deb-src instead.

You also need to import the repository signing key, and update your repositories.

    pi@db-dev ~ $ wget -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -
    pi@db-dev ~ $ sudo apt-get update

Finally, you can build the dependencies and compile the packages needed for running PostgreSQL. Before doing that, you should install build-essential. Build-essential is a package that contains all of the standard build tools that will be needed (dpkg-dev, g++, gcc, libc6-dev, libc-dev, make) to compile the PostgreSQL packages.

    # build-essential is preinstalled on Raspbian
    pi@db-dev ~ $ # sudo apt-get install build-essential

    pi@db-dev ~ $ sudo apt-get build-dep postgresql-9.4
    pi@db-dev ~ $ sudo apt-get build-dep postgresql-common
    pi@db-dev ~ $ sudo apt-get build-dep postgresql-client-common
    pi@db-dev ~ $ sudo apt-get build-dep pgdg-keyring

    pi@db-dev ~ $ cd /tmp
    pi@db-dev /tmp $ apt-get source --compile postgresql-9.4
    pi@db-dev /tmp $ apt-get source --compile postgresql-common
    pi@db-dev /tmp $ apt-get source --compile postgresql-client-common
    pi@db-dev /tmp $ apt-get source --compile pgdg-keyring

You can now create a local repository to move the compiled packages to, and install them from that repository.

    pi@db-dev ~ $ sudo mkdir /var/local/repository
    pi@db-dev ~ $ echo "deb [ trusted=yes ] file:///var/local/repository ./" | \
        sudo tee /etc/apt/sources.list.d/local_repos.list
    pi@db-dev ~ $ cd /var/local/repository
    pi@db-dev /var/local/repository $ sudo mv /tmp/*.deb .
    pi@db-dev /var/local/repository $ dpkg-scanpackages ./ | sudo tee Packages > /dev/null && \
        sudo gzip -f Packages

Update your package list to include the new local repository.

    pi@db-dev ~ $ sudo apt-get update

Install PostgreSQL.

    pi@db-dev ~ $ sudo apt-get install postgresql-9.4

Finally, you can clean up your system.

    pi@db-dev ~ $ rm /tmp/*
    pi@db-dev ~ $ rm -r /tmp/pgdg-keyring-2014.1/
    pi@db-dev ~ $ rm -r /tmp/postgresql-common-170.pgdg70+1/
    pi@db-dev ~ $ rm -r /tmp/postgresql-9.4-9.4.5/
    pi@db-dev ~ $ sudo apt-get clean

#### Running the PostgreSQL postmaster

To start PostgreSQL, use the unix service command.

    pi@db-dev ~ $ sudo service postgresql start

To stop PostgreSQL:

    pi@db-dev ~ $ sudo service postgresql stop

To restart PostgreSQL:

    pi@db-dev ~ $ sudo service postgresql restart

#### Changing the default PostgreSQL credentials

To set the credentials:

    pi@db-dev ~ $ sudo -u postgres psql postgres
    postgres=# \password postgres

This will prompt you to enter your new password.

> Enter new password:
> Enter it again:

#### **TODO:** *Letting PostgreSQL listen to a machine on the local network on port 5432*

Initiate a PostgreSQL cluster, passing in the data directory argument for where data will be stored.

    pi@db-dev ~ $ sudo su - postgres
    postgres@db-dev ~ $ chown -R postgres: /usr/local/pgsql
    postgres@db-dev ~ $ mkdir /usr/local/pgsql/data
    postgres@db-dev ~ $ /usr/lib/postgresql/9.4/bin/initdb -D /usr/local/pgsql/data
    postgres@db-dev ~ $ logout

To start the server:

    pi@db-dev ~ $ /usr/lib/postgresql/9.4/bin/postgres -D /usr/local/pgsql/data

or:

    pi@db-dev ~ $ /usr/lib/postgresql/9.4/bin/pg_ctl -D /usr/local/pgsql/data -l logfile start

View the iptables rules in place.

    pi@db-dev ~ $ sudo iptables -L

Use ifconfig on the machine you want to be able to connect from. Get the 
Add the PostgreSQL rule for a connection to that eth0 inet address.

    pi@db-dev ~ $ sudo iptables -A INPUT -p tcp --dport 5432 -s 10.0.0.13 -j ACCEPT

Saving the iptables rules

    pi@db-dev ~ $ sudo sh -c "iptables-save > /etc/iptables.rules"

Restore the iptables rules. You need superuser privileges and you need to run this command inside of a shell (a command line interpreter) in order for the command to be interpreted correctly and with the correct privileges.

    pi@db-dev ~ $ sudo sh -c "iptables-restore < /etc/iptables.rules"


Restart IP Tables to activate the new rule set.

    pi@db-dev ~ $ sudo ifconfig eth0 down
    pi@db-dev ~ $ sudo ifconfig eth0 up

Logging into PostgreSQL as postgres from another machine:

    jeremykerr@jeremykerr ~ $ psql -U postgres -h localhost
    postgres=# 

#### **TODO:** *Connecting to the PostgreSQL instance*

### Git setup

Install git.

    jeremykerr@jeremykerr ~ $ sudo apt-get install git

    pi@web-dev ~ $ sudo apt-get install git

Configure your account details.

    jeremykerr@jeremykerr ~ $ git config --global user.name "Jeremy Kerr"
    jeremykerr@jeremykerr ~ $ git config --global user.email "jeremy.p.kerr@gmail.com"
    
    pi@web-dev ~ $ git config --global user.name "Jeremy Kerr"
    pi@web-dev ~ $ git config --global user.email "jeremy.p.kerr@gmail.com"

To list your account details, run the following command.

    jeremykerr@jeremykerr ~ $ git config -l

For key based authentication, add your SSH key (id_rsa.pub) to the list of allowed SSH keys for your repository. If you are using Github, they have instructions posted at the following link. You can generate a new key or use the key you already generated for SSH operations in the 'Configuring hostnames for SSH' section of this guide.

https://help.github.com/articles/generating-ssh-keys/

For key based authentication, you will also need to update the settings in your ~/.ssh/config file so that when you push changes to your git repository, git knows to use your key to authenticate you.


    jeremykerr@jeremykerr ~ $ cd /.ssh
    jeremykerr@jeremykerr ~/.ssh $ vi ~/.ssh/config

```
Host web-dev
    Hostname 10.0.0.7
    Port 22
    User pi
    IdentityFile ~/.ssh/id_rsa

Host db-dev
    Hostname 10.0.0.21
    Port 22
    User pi
    IdentityFile ~/.ssh/id_rsa

Host equanimous-tribble
    Hostname github.com
    User jeremykerr
    IdentityFile ~/.ssh/id_rsa
```

To insert text in vi, press 'i' (for Insert). Type the desired text to insert. To stop inserting text, press [ESC]. To save changes and quit, press [:][w][q][ENTER].

Finally you can clone your repository. If you want to use key authentication rather than having to enter your username and password each time you commit, make sure to clone using the SSH clone link instead of the HTTPS link. Since I develop on my main PC and only do git pulls from the Raspberry Pi units, I will only set up my main PC to use key authentication. This repository is public, so no authentication is needed to pull changes.

    # SSH
    jeremykerr@jeremykerr ~ $ git clone git@github.com:jeremykerr/equanimous-tribble.git

    # HTTPS
    pi@web-dev ~ $ git clone https://github.com/jeremykerr/equanimous-tribble

### **TODO:** *Application Development*




