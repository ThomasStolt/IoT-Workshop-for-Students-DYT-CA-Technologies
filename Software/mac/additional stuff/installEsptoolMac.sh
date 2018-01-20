#!/bin/bash

echo "this scipt will download and install esptool.py into ./esptool
read -rsp $'Press any key to continue...\n' -n 1 key

echo "downloading from github"
git clone https://github.com/themadinventor/esptool.git
echo "installing esptool"
cd esptool
sudo python ./setup.py install
echo "installation completed"


