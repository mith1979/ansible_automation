__author__ = 'mithunbanerjee'
#!/usr/bin/env python
"""
Lab Credential:
IP address = 50.76.53.27

pynet-rtr1 (Cisco 881) snmp_port=7961, ssh_port=22
pynet-rtr2 (Cisco 881) snmp_port=8061, ssh_port=8022
pynet-sw1 (Arista vEOS switch) ssh_port=8222, eapi_port=8243
pynet-sw2 (Arista vEOS switch) ssh_port=8322, eapi_port=8343
pynet-sw3 (Arista vEOS switch) ssh_port=8422, eapi_port=8443
pynet-sw4 (Arista vEOS switch) ssh_port=8522, eapi_port=8543
pynet-jnpr-srx1 (Juniper SRX) ssh_port=9822, netconf_port=830

Question
========

4. SNMP Basics

    a. Create an 'SNMP' directory in your home directory.

$ mkdir SNMP
$ cd SNMP

    b. Verify that you can import the snmp_helper library.  This is a small library that I created to simplify aspects of PySNMP.

$ python
Python 2.7.5 (default, Feb 11 2014, 07:46:25)
[GCC 4.8.2 20140120 (Red Hat 4.8.2-13)] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>>
>>> import snmp_helper

    c. Create a script that connects to both routers (pynet-rtr1 and pynet-rtr2) and prints out both the MIB2 sysName and sysDescr.


"""

import pysnmp

from snmp_helper import snmp_get_oid, snmp_extract

print(pysnmp.version)

COMMUNITY_STRING = 'galileo'

SNMP_PORT_rt1 = 7961
RT1_IP = '50.76.53.27'
SNMP_PORT_rt2 = 8061


cisco_rt1_device = (RT1_IP, COMMUNITY_STRING, SNMP_PORT_rt1)
cisco_rt2_device = (RT1_IP, COMMUNITY_STRING, SNMP_PORT_rt2)

snmp_data = snmp_get_oid(cisco_rt1_device, oid='.1.3.6.1.2.1.1.1.0', display_errors=True)
#print(snmp_data)
output = snmp_extract(snmp_data)
print('sysDescription_rt1:', output)
print('#############')

snmp_data = snmp_get_oid(cisco_rt1_device, oid='.1.3.6.1.2.1.1.5.0', display_errors=True)
#print(snmp_data)
output = snmp_extract(snmp_data)
print('sysName_rt1 :', output)
print('#############')

snmp_data = snmp_get_oid(cisco_rt2_device, oid='.1.3.6.1.2.1.1.1.0', display_errors=True)
#print(snmp_data)
output = snmp_extract(snmp_data)
print('sysDescription_rt2:', output)

print('#############')
snmp_data = snmp_get_oid(cisco_rt2_device, oid='.1.3.6.1.2.1.1.5.0', display_errors=True)
#print(snmp_data)
output = snmp_extract(snmp_data)
print('sysName_rt2 :', output)




