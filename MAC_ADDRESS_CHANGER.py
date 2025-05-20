#!/usr/bin/env python

import subprocess # module to allow us to execute OS command
import optparse # module to allow us to use aplication interface
import re # module to allow us to use regex expression

#function to get the argumment from de command line
def get_argumente():
    parser = optparse.OptionParser() #create Object parser
    parser.add_option('-i', '--interface', dest='interface', help='Interface to change the mac')# create a option command-line interface
    parser.add_option('-m', '--mac', dest='mac', help='mac to setting up')# create a option command-line interface
    (options, arguments) = parser.parse_args()                  # using object parser to get argument from command-line user input stored in options variable
    if not options.interface:                                   #check if interface value is missed 
        parser.error("[*] missing value for interface argument")
    elif not options.mac:                                       #check if mac value is missed 
        parser.error("[*] missing value for mac argument")
    return options                                              # if conditions is false return the optinos value

#functio to change the mac executing OS commnad

def mac_change(interface, mac):
    print(f"[*] Changing mac address for {interface} to {mac}")
    
    subprocess.call(["ifconfig", interface, "down"])             #use command line to down interface
    subprocess.call(["ifconfig", interface, "hw", "ether", mac]) #change the interface mac
    subprocess.call(["ifconfig", interface, "up"])               #use command os to up interface

#functio to chech the corruent mac wrt the interface

def get_current_mac(interface):
    ifconfig_result = subprocess.check_output(['ifconfig', interface])
    mac_add_search = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(ifconfig_result))
    if mac_add_search:
        return mac_add_search.group(0)
    else:
        print(f'[-] Could not read MAC address')

try:
        
    options = get_argumente()                                        #get returned value from the get_argumeent function and store in variable options
    current_mac = get_current_mac(options.interface)
    print(f"Current MAC: {current_mac}")
    mac_change(options.interface, options.mac)                       #get the value option for interface and MAC
    current_mac = get_current_mac(options.interface)
    if current_mac == options.mac:
        print(f'[*] MAC address was Sucessfully changed to {current_mac}')
    else:
        print("[-] MAC address did not get changed.")

except Exception as e:
    print(f'ATT: {e}')