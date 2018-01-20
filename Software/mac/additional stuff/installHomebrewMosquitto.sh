#!/bin/bash

# this will install Mosquitto. To do so, homebrew needs to be installed first

echo "Installing homebrew..."
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
echo "now installing mosquitto MQTT..."
brew install mosquitto
echo "done. Have fun"

