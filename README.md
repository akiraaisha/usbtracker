# USBTracker #

USBTracker is a quick & dirty coded incident response and forensics Python script to dump USB related information and artifacts from a Windows OS (vista and later). 

## Special recommandations ##

USBTracker read some protected log files and needs to be run with administrator permissions. The most simple way to run USBTracker is to launch a CMD or Powershell console with a right click **"run as administrator"**, then execute the script inside it.

## "Compiled" binary version ##

If you don't have a python distribution installed on the computer you want to analyze with USBTracker, you can also download an *.exe "compiled" version with *PyInstaller* of the script from the repository.

## Dependencies ##

USBTracker is developed with Python 2.7 and has not been tested with other Python versions.
It uses the great Python module [Python-evtx](http://www.williballenthin.com/evtx/ "Python-evtx") of Willi Ballenthin. So, please don't forget to install it before use USBTracker.

# Usage #

## Help ##

If you want display help, just use the "-h" flag:

```bash
λ usbtracker.py -h
USBTracker v1.0.0
2015 - Alain Sullam

USBTracker it's a free tool which allow you to extract some USB artifacts from a Windows OS (Vista and later). You must execute USBTracker inside a CMD/Powershell console runnnig with administror privileges to be able to dump some log files artifacts.

usage: usbtracker.py [-h] [-u | -uu] [-nh] [-e] [-x] [-s]

optional arguments:
  -h, --help            show this help message and exit
  -u, --usbstor         Dump USB artifacts from USBSTOR registry
  -uu, --usbstor-verbose
                        Dump USB detailed artifacts from USBSTOR registry
  -nh, --no-hardwareid  Hide HardwareID value during a USBSTOR detailed
                        artifacts dump in registry
  -e, --event-log       Dump USB artifacts and events from event log
  -x, --raw-xml-event   Display event results in raw xml (with -e option
                        only).
  -s, --setupapi        Dump USB artifacts from the setupapi.dev.log (Windows
                        Vista and later)
```
