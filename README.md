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

If you want display help, just use the "-h" flag :

```
PS C:\XXX\XXX\XXX\XXX> .\usbtracker.py -h
USBTracker v1.0.0
2015 - Alain Sullam

USBTracker it's a free tool which allow you to extract some USB artifacts from a Windows OS (Vista and later).
You must execute USBTracker inside a CMD/Powershell console runnnig with administror privileges to be able to dump some
log files artifacts.

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

## List know USB storage devices ##

If you want to list all USB storage devices known by Windows, use the "-u" flag to get a simple list :

```
PS C:\XXX\XXX\XXX\XXX> .\usbtracker.py -u
USBTracker v1.0.0
2015 - Alain Sullam

USBTracker it's a free tool which allow you to extract some USB artifacts from a Windows OS (Vista and later).
You must execute USBTracker inside a CMD/Powershell console runnnig with administror privileges to be able to dump some
log files artifacts.

USB device(s) know by this computer :
=====================================

CdRom&Ven_HL-DT-ST&Prod_DVDRAM_GP08NU20&Rev_1.00
Disk&Ven_Generic&Prod_STORAGE_DEVICE&Rev_0272
Disk&Ven_Kingston&Prod_DataTraveler_2.0&Rev_1.00
Disk&Ven_WD&Prod_5000AAV_External&Rev_1.65
Disk&Ven_WD&Prod_Elements_10B8&Rev_1012
Disk&Ven_WD&Prod_My_Book_1140&Rev_1012
Other&Ven_WD&Prod_SES_Device&Rev_1012
```

or the "-uu" flag if you want to get a detailed list :

```
PS C:\XXX\XXX\XXX\XXX> .\usbtracker.py -uu
USBTracker v1.0.0
2015 - Alain Sullam

USBTracker it's a free tool which allow you to extract some USB artifacts from a Windows OS (Vista and later).
You must execute USBTracker inside a CMD/Powershell console runnnig with administror privileges to be able to dump some
log files artifacts.

USB device(s) know by this computer :
=====================================

CdRom&Ven_HL-DT-ST&Prod_DVDRAM_GP08NU20&Rev_1.00

        Serial : 00101016400086C55&0

        DeviceDesc : @cdrom.inf,%gencdrom_devdesc%;CD-ROM Drive
        Capabilities : 16
        HardwareID : [u'USBSTOR\\CdRomHL-DT-STDVDRAM_GP08NU20_1.00', u'USBSTOR\\CdRomHL-DT-STDVDRAM_GP08NU20_', u'USBSTO
R\\CdRomHL-DT-ST', u'USBSTOR\\HL-DT-STDVDRAM_GP08NU20_1', u'HL-DT-STDVDRAM_GP08NU20_1', u'USBSTOR\\GenCdRom', u'GenCdRom
']
        CompatibleIDs : [u'USBSTOR\\CdRom', u'USBSTOR\\RAW']
        ContainerID : {def10b43-2e59-5e9f-8ca6-ffab1cfc9afa}
        Service : cdrom
        ClassGUID : {4d36e965-e325-11ce-bfc1-08002be10318}
        ConfigFlags : 0
        Driver : {4d36e965-e325-11ce-bfc1-08002be10318}\0001
        Class : CDROM
        Mfg : @cdrom.inf,%genmanufacturer%;(Standard CD-ROM drives)
        FriendlyName : HL-DT-ST DVDRAM GP08NU20 USB Device

======================================================================

Disk&Ven_Generic&Prod_STORAGE_DEVICE&Rev_0272

        Serial : 000000000272&0

        DeviceDesc : @disk.inf,%disk_devdesc%;Disk drive
        Capabilities : 16
        HardwareID : [u'USBSTOR\\DiskGeneric_STORAGE_DEVICE__0272', u'USBSTOR\\DiskGeneric_STORAGE_DEVICE__', u'USBSTOR\
\DiskGeneric_', u'USBSTOR\\Generic_STORAGE_DEVICE__0', u'Generic_STORAGE_DEVICE__0', u'USBSTOR\\GenDisk', u'GenDisk']
        CompatibleIDs : [u'USBSTOR\\Disk', u'USBSTOR\\RAW']
        ContainerID : {a3ce89cb-5363-54a8-8d4f-af2374c200a5}
        ConfigFlags : 0
        ClassGUID : {4d36e967-e325-11ce-bfc1-08002be10318}
        Driver : {4d36e967-e325-11ce-bfc1-08002be10318}\0004
        Class : DiskDrive
        Mfg : @disk.inf,%genmanufacturer%;(Standard disk drives)
        Service : disk
        FriendlyName : Generic STORAGE DEVICE USB Device

======================================================================

...

```