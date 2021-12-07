Team member names: Mark Bowen, Kimberle Sotelo
Git Repo: 
https://github.com/usc-ee250-fall2021/bowen-soltelo.git 
Link to view demo online: https://youtu.be/ax50ZWUA-bE

Instructions on how to compile/execute program(s):
Use this link to Enable you IC2 interface on rpi 
https://www.raspberrypi-spy.co.uk/2014/11/enabling-the-i2c-interface-on-the-raspberry-pi
then Install Grove Pi Firmware Updater Tool
cd ~
sudo curl -kL dexterindustries.com/update_grovepi | bash
then  Update Grove Pi Firmware
cd ~/Dexter/GrovePi/Firmware
./firmware_update.sh 
sudo reboot 
then install requests on rpi
sudo pip3 install requests --upgrade
then install python-kasa
pip3 install python-kasa
trouble shooting** allternatively you can clone the repository and use poetry to install (you will need to have poetry installed)
git clone https://github.com/python-kasa/python-kasa.git
cd python-kasa/
poetry install

List of any external libraries that were used:
asyncio
python-kasa
Grovepi 
time
math
requests
