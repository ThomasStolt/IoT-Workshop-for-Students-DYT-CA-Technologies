#!/bin/bash

# NodeMCU firmware update script
# prerequisite: esptool.py needs to be installed
# installation instructions for esptool: 
#      git clone https://github.com/themadinventor/esptool.git
#      cd esptool
#      sudo python ./setup.py install
# please make sure directory and filename of firmware binary file are correct
#

echo "Hold down the FLASH button on the device and hit the RST button while doing so"
read -rsp $'Press any key to continue...\n' -n 1 key

# writing firmware to NodeMCU using esptool
echo "flashing NodeMCU"
python ./esptool.py --port=/dev/cu.SLAB_USBtoUART  write_flash  -fm=dio -fs=32m 0x00000 ./nodemcu-master-10-modules-2017-03-24-07-38-31-float.bin
echo "done flashing. Unplug MCU and plug in again"
echo "Have fun"



