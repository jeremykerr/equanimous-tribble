# equanimous-tribble

This is just a test application so that I can learn a bit more about the life of applications from conception to implementation, including all the phases from learning the platforms to building the end product. The application itself probably will be a simple shopping cart application, just like any of the other thousands of shopping cart applications that exist. Nothing will make it special or different, other than the inclusion of what was involved to get each feature up and running.

## Contents
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

* Git setup
* Application Development


## Raspberry Pi Software Update
Update your package lists so that you can access the latest and greatest versions of the software you're running

    sudo apt-get update

Install the latest and greatest versions of the software you're running

    sudo apt-get upgrade

Clean the memory used by installation files

    sudo apt-get clean

View Memory Usage

    df -h


