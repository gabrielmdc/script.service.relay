<img alt="RKAS" title="Relay kodi addon service" src="resources/icon.png" width="100" height="100">

# Relay kodi addon service

This add-on, allow you to switch a relay status, connected to a Raspberry Pi, (turn on or turn off), using the [Android app](https://github.com/nearlg/kodi-relay-remote) using a **local net**.

Requirements
==============
- Raspberry Pi or compatible
- A Gnu/Linux system installed
- Kodi installed
- *Recomendable the [Android app](https://github.com/nearlg/kodi-relay-remote) to control the relay ;)*

Installation
==============

Just download the [ZIP](https://github.com/nearlg/script.service.relay/archive/master.zip) , and install it using Kodi add-on installer.

Configuration
==============
You can change the configuration variables in the *settings add-on area* in Kodi.</br>Configuration variables:

### Net port
Used by the socket for the comunication with the app.</br>
*By default: 10000*
### GPIO port
The GPIO port where is connectd the relay.</br>
*By default: 18*
### GPIO path
Depends on the system, it has the OPENElec path by default.</br>
*By default: /sys/class/gpio*
