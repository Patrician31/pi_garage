# pi_garage

This project (as the name suggests) is a web enabled garage door controller. With it I can open and close my garage door from anywhere with internet access. I've also added a webcam so I could get an image of the garage doors. One more thing this pi controls is a wall fan that turns on for 15 minutes every few hours to keep air circulating in the garage (I live in the hot&humid south)

#download raspbian image from:
https://www.raspberrypi.org/downloads/raspbian/

#install with dd as described here (linux version)
https://www.raspberrypi.org/documentation/installation/installing-images/linux.md

#setup wifi
https://learn.adafruit.com/adafruits-raspberry-pi-lesson-3-network-setup/setting-up-wifi-with-occidentalis
(add the following to /etc/network/interfaces file)
auto wlan0
allow-hotplug wlan0
iface wlan0 inet dhcp
        wpa-ssid "<ssid>"
        wpa-psk "<password>"

# enable SSH (new since 2016-11-25)
#SSH disabled by default; can be enabled by creating a file with name "ssh" in boot partition

# remove old ssh settings from the PC
ssh-keygen -f "/home/asaf/.ssh/known_hosts" -R 192.168.1.207

#user pi pass raspberry

# move files to raspberry pi
scp -r <-local files directory>/. pi@192.168.1.207:/home/pi/garage/

# login:
ssh pi@192.168.1.207

#update everything
sudo apt-get update

# install python, apache and php
sudo apt-get install python-dev python-rpi.gpio apache2 php5 libapache2-mod-php5 -y


# edit file to allow external web hosting access
sudo nano /etc/sudoers
    #add to bottom of file:
    www-data ALL=(root) NOPASSWD:ALL

#get the web server file to the right place and delete html file
sudo mv ~/garage/index.php /var/www/html/index.php
sudo rm /var/www/html/index.html

# add password protection to the webserver
sudo htpasswd -c /etc/apache2/.htpasswd <web_login_id>
sudo nano /etc/apache2/sites-enabled/000-default.conf
    # add to file:
    <Directory "/var/www/html">
        AuthType Basic
        AuthName "Restricted Content"
        AuthUserFile /etc/apache2/.htpasswd
        Require valid-user
    </Directory>

#restart webserver
sudo service apache2 restart

# install camera stuff
sudo apt-get install fswebcam

# automatically start fan
sudo nano .bashrc
    #add this line at the bottom
    python ~/garage/pythonFan.py &


