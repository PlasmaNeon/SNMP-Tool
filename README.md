# SNMP-tool
A simple GUI SNMP Remote Monitor Tool.
For SJTU Course EE380.

## Prerequisites
1. Install SMNP in linux(Ubuntu 18.04 here)
`$ sudo apt install snmpd snmp snmp-mibs-downloader`

2. Install eel for Python
`pip3 install eel`

3. Install chromium for linux, since eel is used.

## Usage
`python setup_eel.py` to start a local server.
`python cmd_oid.py` to manually input oid.

## To-do
- [ ] Trap function.
- [ ] Set function.
