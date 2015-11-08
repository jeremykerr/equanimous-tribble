# equanimous-tribble

This is just a test application so that I can learn a bit more about the life of applications from inception to implementation, including all the phases from learning the platforms to building the end product. The application itself probably will be a simple shopping cart application, just like any of the other thousands of shopping cart applications that exist. Nothing will make it special or different, other than the inclusion of what was involved to get each feature up and running.

## Contents
* **TODO:** *Raspberry Pi Installation and Initial Configuration*
* Raspberry Pi Software Update
* Enabling SSH for remote development
  * Enable SSH on the local network
  * **TODO:** *Enable SSH over the internet*
* Using Flask on the Raspberry Pi
  * Install Flask for Raspberry Pi
  * Build a simple hello world application
  * Allow web access to the application
    * Allow web access over the local network
    * **TODO:** *Allow web accessibility over the internet*
      * Install No-IP for Dynamic DNS
  * Running the application
    * Running in debug mode
    * Running in production
    * Closing the application
* Git setup
* Application Development

### Raspberry Pi Software Update

To update your package lists so that you can access the most up to date versions of the software you're running:

    sudo apt-get update

To install the most up to date versions of the software you're running:

    sudo apt-get upgrade

To clean the memory used by installation files:

    sudo apt-get clean

To view the current memory usage:

    df -h

### Enabling SSH for remote development

#### Enable SSH on the local network

Open the Raspberry Pi config utility to enable ssh.

    sudo raspi-config

> [8 Advanced Options]

> [A4 SSH]

> [Enable]

> [OK]

> [Finish]

Get the inet address of the Raspberry Pi device in order to be able to ssh in.

    ifconfig

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

    ssh pi@10.0.0.7


#### **TODO:** *Enable SSH over the internet*

### Using Flask on the Raspberry Pi

#### Install Flask for Raspberry Pi

*At the time of this writing, Raspberry Pi does not support a version of Python 3 that meets the requirements for Flask, so we'll be using Python 2.*

Install pip (the Python package index) in order to install Flask.

    sudo apt-get install python-pip

Install Flask (a microforamework for a Python based web server).
http://flask.pocoo.org/

    sudo pip install Flask

#### Build a simple hello world application

#### Allow web access to the application

##### Allow web access over the local network

Get the inet address of the Raspberry Pi device.

    ifconfig

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

View the iptables rules in place.

    sudo iptables -L

Add an accept rule in order to receive requests over the specified port (5000) from other machines on the local network. Then list the rules again to verify it was added.

    sudo iptables -I INPUT -p tcp --dport 5000 -j ACCEPT
    sudo iptables -L

Restart IP Tables to activate the new rule set.

    sudo ifconfig eth0 down
    sudo ifconfig eth0 up

##### **TODO:** *Allow web accessibility over the internet*

###### Install No-IP for Dynamic DNS

Create a directory to install No-IP in, and go to that directory.

    mkdir /home/pi/noip
    cd /home/pi/noip

Download and extract the No-IP application.

    wget http://www.no-ip.com/client/linux/noip-duc-linux.tar.gz
    tar vzxf noip-duc-linux.tar.gz

Go to the extracted directory and install the application.

    cd noip-2.1.9-1/
    sudo make
    sudo make install

#### Running the application

To run the application in the open terminal:

    python hello.py

To run the application in the background:


##### Running in debug mode

##### Running in production

##### Closing the application

To close the application in the open terminal:

> Press [Ctrl] + [C]

To find the application in the background:

To close the application in the background:

### Git setup

Install git.

    sudo apt-get install git

Clone a repository.

    cd ~
    git clone https://github.com/jeremykerr/equanimous-tribble
    git config --global user.name "Jeremy Kerr"
    git config --global user.email "jeremy.p.kerr@gmail.com"

### Application Development

