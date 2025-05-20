# MAC_ADDRESS_CHANGER:
This script was created in python to change the MAC ADDRESS of the any interface on KALI LINUX

# HOW TO USE:
python mach_cheger.py --help             
Usage: mach_cheger.py [options]

Options:
  -h, --help            show this help message and exit
  -i INTERFACE, --interface=INTERFACE
                        Interface to change the mac
  -m MAC, --mac=MAC     mac to setting up

# Descriptions:
First identify the interface to cahnge the mac address, the aplication use command-line interface 
to input value for the arguments.
##### python mach_cheger.py -i eth0 -m 00:11:22:33:44:55

# Why change your MAC_Address:

- impersonate devices to get certain privileged information
- increase anonymity
