# equanimous-tribble

This is just a test application so that I can learn a bit more about the life of applications from inception to implementation, including all the phases from learning the platforms to building the end product. The application itself will probably be a simple shopping cart application, just like any of the other thousands of shopping cart applications that exist. Nothing will make it special or different, other than the inclusion of what was involved to get each feature up and running.

## Contents
* **TODO:** *Raspberry Pi Installation and Initial Configuration*
* Raspberry Pi Software Update
* Enabling SSH for remote development
  * Enable SSH on the local network
  * **TODO:** *Enable SSH over the internet*
    * **TODO:** *Port Forwarding*
* Using Flask on the Raspberry Pi
  * Install Flask for Raspberry Pi
  * Build a simple hello world application
  * Allow web access to the application
    * Allow web access over the local network
    * **TODO:** *Allow web access over the internet*
      * **TODO:** *Visiting your site by its IP Address*
      * Installing No-IP for Dynamic DNS
      * **TODO:** *Visiting your site by its domain name*
  * Running the application
  * Closing the application
* **TODO:** *Using PostgreSQL on the Raspberry Pi*
  * Installing PostgreSQL
  * Running the PostgreSQL postmaster
  * **TODO:** *Connecting to the PostgreSQL Instance*
* Git setup
* **TODO:** *Application Development*


### **TODO:** *Raspberry Pi Installation and Initial Configuration*

### Raspberry Pi Software Update

To update your package lists so that you can access the most up to date versions of the software you're running:

    pi@raspberrypi ~ $ sudo apt-get update

To install the most up to date versions of the software you're running:

    pi@raspberrypi ~ $ sudo apt-get upgrade

To clean the memory used by installation files:

    pi@raspberrypi ~ $ sudo apt-get clean

To view the current memory usage:

    pi@raspberrypi ~ $ df -h

### Enabling SSH for remote development

#### Enable SSH on the local network

Open the Raspberry Pi config utility to enable ssh.

    pi@raspberrypi ~ $ sudo raspi-config

```
[8 Advanced Options]
[A4 SSH]
[Enable]
[OK]
[Finish]
```

Get the eth0 inet address of the Raspberry Pi device in order to be able to ssh in.

    pi@raspberrypi ~ $ ifconfig

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

> inet addr:10.0.0.7

Log in from a different machine on the same network.

    jeremykerr@jeremykerr ~ $ ssh pi@10.0.0.7

#### **TODO:** *Enable SSH over the internet*

##### **TODO:** *Port Forwarding*

### Using Flask on the Raspberry Pi

#### Install Flask for Raspberry Pi

*At the time of this writing, Raspberry Pi does not support a version of Python 3 that meets the requirements for Flask, so we'll be using Python 2.*

Install pip (the Python package index) in order to install Flask.

    pi@raspberrypi ~ $ sudo apt-get install python-pip

Install Flask (a microforamework for a Python based web server).
http://flask.pocoo.org/

    pi@raspberrypi ~ $ sudo pip install Flask

#### Build a simple hello world application

Create and open a new file called "hello.py".

    pi@raspberrypi ~ $ touch hello.py
    pi@raspberrypi ~ $ vi hello.py

Some code needs to be written in order to create the server instance and to return a "Hello, world." string when a request is made to the application. One thing worth mentioning is that app.debug is being set to False in the following code. The property app.debug can be used to dynamically reload the source file (hello.py) whenever it is changed, which is convenient when developing locally on a machine that is not accepting requests from the web. However, this dynamic reloading makes it possible for a malicious attacker to run arbitrary code through your web application, so app.debug should never be set to True on a production machine. Read the Flask documentation for more details on that. The other thing worth noting is that app.run is passed an argument, host='0.0.0.0'. This allows the server to be externally visible (meaning you will get a connection denied error when you attempt to visit the application if you have not set this argument).

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

To save changes within the vi editor:

    [ESC]
    :wq
    [ENTER]

#### Allow web access to the application

##### Allow web access over the local network

*As listed, the "Allow web access over the local network" phase will need to be repeated each time the Raspberry Pi unit is rebooted. To get around this, these actions can be scripted and set to run on startup.*

**TODO:** *Include instructions for scripting this section so that changes persist if the Raspberry Pi unit is rebooted*

View the iptables rules in place.

    pi@raspberrypi ~ $ sudo iptables -L

Add an accept rule in order to receive requests over the specified port (5000) from other machines on the local network. Then list the rules again to verify it was added.

    pi@raspberrypi ~ $ sudo iptables -I INPUT -p tcp --dport 5000 -j ACCEPT
    pi@raspberrypi ~ $ sudo iptables -L

Restart IP Tables to activate the new rule set.

    pi@raspberrypi ~ $ sudo ifconfig eth0 down
    pi@raspberrypi ~ $ sudo ifconfig eth0 up

##### **TODO:** *Allow web access over the internet*

**TODO:** *Visiting your site by its IP Address*

###### Installing No-IP for Dynamic DNS

Go to the No-IP website and create an account (you need it for the configuration in the installation).

> http://www.noip.com/

Create a directory to install No-IP in, and navigate to that directory.

    pi@raspberrypi ~ $ mkdir /home/pi/noip
    pi@raspberrypi ~ $ cd /home/pi/noip

Download and extract the No-IP application.

    pi@raspberrypi /home/pi/noip $ wget http://www.no-ip.com/client/linux/noip-duc-linux.tar.gz
    pi@raspberrypi /home/pi/noip $ tar vzxf noip-duc-linux.tar.gz

Go to the extracted directory and install the application.

    pi@raspberrypi /home/pi/noip $ cd noip-2.1.9-1/
    pi@raspberrypi /home/pi/noip/noip-2.1.9-1 $ sudo make
    pi@raspberrypi /home/pi/noip/noip-2.1.9-1 $ sudo make install

**TODO:** *Visiting your application by its domain name*

#### Running the application

To run the application in the open terminal:

    pi@raspberrypi ~ $ python hello.py

To run the application in the background:

    pi@raspberrypi ~ $ python hello.py &

Running the application in the background will tell you the pid (process id) before giving you a command prompt.

> [1] 3472

If the earlier instructions on allowing web access over the local network were followed, any computer on the network should now be able to access 10.0.0.7:5000 (or whatever the relevant eth0 inet address is) and see the "Hello, world." string. To see the eth0 inet address, type ifconfig at the command prompt.

#### Closing the application

To close the application in the open terminal:

    [Ctrl] + [C]

To find the application in the background:

    pi@raspberrypi ~ $ pgrep python

> 3472

To close the application in the background, type kill followed by the pid returned from the previous command.

    pi@raspberrypi ~ $ kill 3472

### **TODO:** *Using PostgreSQL on the Raspberry Pi*
#### Installing PostgreSQL
 
Raspbian is a Debian 7 (wheezy) build, and is currently supported by PostgreSQL. 

> https://wiki.postgresql.org/wiki/Apt

Rubens Souza posted an excellent article (http://raspberrypg.org/2015/06/step-5-update-installing-postgresql-on-my-raspberry-pi-1-and-2/) on installing PostgreSQL on a Raspberry Pi 2. Some of the following information is directly pulled from that source, and from the documentation on PostgreSQL.org (http://www.postgresql.org/download/linux/ubuntu/).

To build PostgreSQL from source on a Raspberry Pi, you have to add the PostgreSQL Apt Repository. In order to create the file to store the PostgreSQL Apt Repository location to, you need to have superuser permissions.

    pi@raspberrypi ~ $ sudo touch /etc/apt/sources.list.d/pgdg.list
    pi@raspberrypi ~ $ sudo vi /etc/apt/sources.list.d/pgdg.list

Save the following line in this file.

    deb-src http://apt.postgresql.org/pub/repos/apt/ wheezy-pgdg main

This allows us to access the PostgreSQL apt repository. In the PostgreSQL documentation, they use deb, which means they are building from binary sources. Because we are compiling from source packages from the PostgreSQL Apt repository, we will use deb-src instead.

You also need to import the repository signing key, and update your repositories.

    pi@raspberrypi ~ $ wget -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -
    pi@raspberrypi ~ $ sudo apt-get update

Finally, you can build the dependencies and compile the packages needed for running PostgreSQL. Before doing that, you should install build-essential. Build-essential is a package that contains all of the standard build tools that will be needed (dpkg-dev, g++, gcc, libc6-dev, libc-dev, make) to compile the PostgreSQL packages.

    # build-essential is preinstalled on Raspbian
    pi@raspberrypi ~ $ # sudo apt-get install build-essential

    pi@raspberrypi ~ $ sudo apt-get build-dep postgresql-9.4
    pi@raspberrypi ~ $ sudo apt-get build-dep postgresql-common
    pi@raspberrypi ~ $ sudo apt-get build-dep postgresql-client-common
    pi@raspberrypi ~ $ sudo apt-get build-dep pgdg-keyring

    pi@raspberrypi ~ $ cd /tmp
    pi@raspberrypi /tmp $ apt-get source --compile postgresql-9.4
    pi@raspberrypi /tmp $ apt-get source --compile postgresql-common
    pi@raspberrypi /tmp $ apt-get source --compile postgresql-client-common
    pi@raspberrypi /tmp $ apt-get source --compile pgdg-keyring

You can now create a local repository to move the compiled packages to, and install them from that repository.

    pi@raspberrypi ~ $ sudo mkdir /var/local/repository
    pi@raspberrypi ~ $ echo "deb [ trusted=yes ] file:///var/local/repository ./" | \
        sudo tee /etc/apt/sources.list.d/local_repos.list
    pi@raspberrypi ~ $ cd /var/local/repository
    pi@raspberrypi /var/local/repository $ sudo mv /tmp/*.deb
    pi@raspberrypi /var/local/repository $ dpkg-scanpackages ./ | sudo tee Packages > /dev/null && \
        sudo gzip -f Packages

Update your package list to include the new local repository.

    pi@raspberrypi ~ $ sudo apt-get update

Install PostgreSQL.

    pi@raspberrypi ~ $ sudo apt-get install postgresql-9.4

Finally, you can clean up your system.

    pi@raspberrypi ~ $ rm /tmp/*
    pi@raspberrypi ~ $ rm -r /tmp/pgdg-keyring-2014.1/
    pi@raspberrypi ~ $ rm -r /tmp/postgresql-common-170.pgdg70+1/
    pi@raspberrypi ~ $ rm -r /tmp/postgresql-9.4-9.4.5/
    pi@raspberrypi ~ $ sudo apt-get clean

#### Running the PostgreSQL postmaster

To start PostgreSQL, use the unix service command.

    pi@raspberrypi ~ $ sudo service postgresql start

To stop PostgreSQL:

    pi@raspberrypi ~ $ sudo service postgresql stop

To restart PostgreSQL:

    pi@raspberrypi ~ $ sudo service postgresql restart

#### **TODO:** *Connecting to the PostgreSQL instance*

### Git setup

Install git.

    pi@raspberrypi ~ $ sudo apt-get install git

Configure your account details.

    pi@raspberrypi ~ $ git config --global user.name "Jeremy Kerr"
    pi@raspberrypi ~ $ git config --global user.email "jeremy.p.kerr@gmail.com"

Clone a repository.

    pi@raspberrypi ~ $ cd ~
    pi@raspberrypi ~ $ git clone https://github.com/jeremykerr/equanimous-tribble

### **TODO:** *Application Development*




