#!/usr/bin/env python3
import optparse
import subprocess

def change_mac(interface, new_mac):
    print(f"[+] Changing MAC address for {interface} to {new_mac}")

    subprocess.call(["ifconfig", interface,"down"])
    subprocess.call(["ifconfig", interface,"hw","ether", new_mac])
    subprocess.call(["ifconfig", interface,"up"])

# Create parser object
parser = optparse.OptionParser()

# Set arguments
parser.add_option("-i","--interface",dest="interface",help="Interface to change its MAC address")
parser.add_option("-m","--mac",dest="new_mac",help="New MAC address")

# Listen for arguments
(options, arguments) = parser.parse_args()

change_mac(options.interface,options.new_mac)


