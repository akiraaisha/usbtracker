# USBTracker #

USBTracker is a quick & dirty coded Python script to dump USB related information and artifacts in a Windows OS (vista and later). 

## Special recommandations ##

USBTracker read some protected log files and needs to be run with administrator permissions. The most simple way to run USBTracker is to launch a CMD or Powershell console with a right click **"run as administrator"**, then execute the script inside it.

## "Compiled" binary version ##

If you don't have a python distribution installed on the computer you want to run USBTracker, you can also find an *.exe "compiled" version with *PyInstaller* of the script in the repository.

## Dependencies ##

USBTracker is developed with Python 2.7 and has not been tested with other Python versions.
It uses the great Python module *![python-evtx](http://www.williballenthin.com/evtx/)* of Willi Ballenthin. So, please don't forget to install it before use USBTracker.