<img alt="RKAS" title="Relay kodi addon service" src="resources/icon.png" width="100" height="100">

# Relay kodi addon service

This is the [gcr-server](https://github.com/nearlg/gcr-server) version for Kodi.
It allows to manage relays connected to a Raspberry Pi using Kodi.

## Requirements

- Raspberry Pi or compatible
- A Gnu/Linux system installed
- Kodi installed
- *Recommendable the [Android app](https://github.com/nearlg/gcr-cli-android) to control the relays ;)*

## Installation

Just download the [ZIP](https://github.com/nearlg/script.service.relay/archive/master.zip),
 and install it using Kodi add-on installer.

## Configuration

You can change the configuration variables in the *settings add-on area* in Kodi.</br>Configuration variables:

### Socket port:
Used by the socket for the comunication with the app.

*By default: 10000*

### Database file:
This is the file name of the database file (SQLite).

*By default: [plugin root path]/resources/gcrserver/resources/database.db*
