#!/bin/bash

sudo apt update && apt upgrade -y
sudo apt install pip
sudo apt install git
git clone "https://github.com/ARS-83/v2ray-ConfigGenerator.git"
current_folder=$(basename "$PWD")
cd "/$current_folder/v2ray-ConfigGenerator"
echo "$PWD"
pip install -r requirements.txt
chmod +x Main.py
chmod 755 ./db
chmod 644 ./db/ars.db
mkdir "/etc/generatordb"
sudo ln -s /$current_folder/v2ray-ConfigGenerator/Main.py /usr/local/bin/generator
