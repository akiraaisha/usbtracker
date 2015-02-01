import argparse
import sys
import os.path
import _winreg
import mmap
import contextlib

from Evtx.Evtx import FileHeader
from Evtx.Views import evtx_file_xml_view
from utilities import utils

import xml.etree.ElementTree as ET


def main():

    usage()
    parser = argparse.ArgumentParser()
    group_reg = parser.add_mutually_exclusive_group()
    group_reg.add_argument("-u", "--usbstor", help="Dump USB artifacts from USBSTOR registry", action="store_true")
    group_reg.add_argument("-uu", "--usbstor-verbose", help="Dump USB detailed artifacts from USBSTOR registry", action="store_true")
    parser.add_argument("-nh", "--no-hardwareid", help="Hide HardwareID value during a USBSTOR detailed artifacts dump in registry", action="store_true")

    group_log = parser.add_mutually_exclusive_group()
    group_log.add_argument("-e", "--event-log", help="Dump USB artifacts and events from event log", action="store_true")
    parser.add_argument("-x", "--raw-xml-event", help="Display event results in raw xml (with -e option only).", action="store_true")
    parser.add_argument("-s", "--setupapi", help="Dump USB artifacts from the setupapi.dev.log (Windows Vista and later)", action="store_true")

    # parser.add_argument("square", type=int, help="display a square of a given number")
    # parser.add_argument("-c", "--check", help="Check the source code integrity", choices=["test1","test2","test3"])
    args = parser.parse_args()

    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)

    if args.usbstor:
        dump_registry()
    elif args.usbstor_verbose:
        if args.no_hardwareid:
            dump_extra_registry(True)
        else:
            dump_extra_registry(False)

    if args.event_log:
        dump_event_log(r'C:\Windows\SysNative\winevt\Logs\Microsoft-Windows-DriverFrameworks-UserMode%4Operational.evtx', args.raw_xml_event)


def usage():

    print("USBTracker v1.0.0")
    print("2015 - Alain Sullam\n")
    print("USBTracker it's a free tool which allow you to extract some USB artifacts from a Windows OS (Vista and "
          "later).")
    print("You must execute USBTracker inside a CMD/Powershell console runnnig with administror privileges to be able to dump some "
          "log files artifacts.\n ")


def dump_registry():

    print("USB device(s) know by this computer :")
    print("=====================================\n")
    query = _winreg.OpenKey(_winreg.HKEY_LOCAL_MACHINE, r'SYSTEM\CurrentControlSet\Enum\USBSTOR', 0)
    i = 0
    try:
        while True:
            print _winreg.EnumKey(query, i)
            i += 1

    except WindowsError:
        print("\n\n")
        pass


def dump_extra_registry(hide_hardwareid):

    print("USB device(s) know by this computer :")
    print("=====================================\n")

    query = _winreg.OpenKey(_winreg.HKEY_LOCAL_MACHINE, r'SYSTEM\CurrentControlSet\Enum\USBSTOR', 0)
    # subkey = ""
    i = 0

    try:
        while True:
            key = _winreg.EnumKey(query, i)
            print key + "\n"
            i += 1
            query2 = _winreg.OpenKey(_winreg.HKEY_LOCAL_MACHINE, r'SYSTEM\CurrentControlSet\Enum\USBSTOR' + "\\" + key, 0)
            j = 0

            try:
                while True:
                    subkey = _winreg.EnumKey(query2, j)
                    print("        " + "Serial : " + subkey + "\n")
                    j += 1
                    query3 = _winreg.OpenKey(_winreg.HKEY_LOCAL_MACHINE, r'SYSTEM\CurrentControlSet\Enum\USBSTOR' + "\\" + key + "\\" + subkey, 0)
                    k = 0
                    try:
                        while True:
                            value_tuple = _winreg.EnumValue(query3, k)
                            if hide_hardwareid is True:
                                if value_tuple[0] != "HardwareID":
                                    print("        " + value_tuple[0] + " : " + str(value_tuple[1]))
                            else:
                                print("        " + value_tuple[0] + " : " + str(value_tuple[1]))
                            k += 1
                    except WindowsError, ex:
                        pass

            except WindowsError, ex:
                pass

            print("\n======================================================================\n")

    except WindowsError, ex:
        pass


def dump_event_log(event_file, xml_format):

    if os.path.isfile(event_file) is False:
        print("The log file : " + event_file + " is not found.")
        return

    print("USB related event(s) found in the event log :")
    print("=============================================\n")

    with open(event_file, 'r') as f:
        with contextlib.closing(mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)) as buf:
            fh = FileHeader(buf, 0x0)

            for xml, record in evtx_file_xml_view(fh):
                root = ET.fromstring(xml)
                if root[0][1].text == '1003':
                    if xml_format:
                        print xml
                    else:
                        print root[0][7].get('SystemTime') + " EventID : " + root[0][1].text + " Computer : " + root[0][12].text + " User SID : " + root[0][13].get('UserID') + " User : " + utils.find_username_by_sid(root[0][13].get('UserID'))
                        print root[1][0][1].text + "\n"


if __name__ == "__main__":
    main()
