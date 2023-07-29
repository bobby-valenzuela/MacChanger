#!/usr/bin/env python3
import optparse
import subprocess
import re

def get_args():
    # Create parser object
    parser = optparse.OptionParser()

    # Set arguments
    parser.add_option("-i","--interface",dest="interface",help="Interface to change its MAC address")
    parser.add_option("-m","--mac",dest="new_mac",help="New MAC address")

    # Listen for arguments
    (options, arguments) = parser.parse_args()

    # Error handling
    if not options.interface:
        parser.error("[-] Please specify an interface to use. See --help for more info.")
    elif not options.new_mac:
        parser.error("[-] Please specify a MAC to set. See --help for more info.")

    return options

def get_current_mac(interface):
    ifconfig_result = subprocess.check_output(["ifconfig",interface])
    current_mac_find = re.search(r"(\w{2}:){5}\w{2}",str(ifconfig_result))
    current_mac = current_mac_find.group(0)
    return current_mac

def change_mac(interface, new_mac):
    print(f"[+] Changing MAC address for {interface} to {new_mac}")

    subprocess.call(["ifconfig", interface,"down"])
    subprocess.call(["ifconfig", interface,"hw","ether", new_mac])
    subprocess.call(["ifconfig", interface,"up"])


args = get_args()

current_mac = get_current_mac(args.interface)
print(f"Current MAC : {current_mac}")

change_mac(args.interface,args.new_mac)

if current_mac == args.new_mac:
    print(f"[+] MAC address sucessfully changed to {current_mac}.")
else:
    print(f"[-] MAC address was not updated.")


