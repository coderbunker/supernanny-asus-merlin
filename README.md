# Raspberry Pi Setup
## Requirements
- Development PC
- Raspberry Pi
- USB Power plug
- Micro USB Cable
- Micro or full size SD Card (Depends on your Pi)
- Way of connecting the card to your Dev PC
## Installing Raspian
Note: This guide is currently written with universal and mac specific instructions. Please feel free to add any other OS specific instructions.
### Get Raspian
Download Raspian Stretch Lite from [here](https://www.raspberrypi.org/downloads/raspbian/) or in your  terminal run:
```
    $ wget https://downloads.raspberrypi.org/raspbian_lite_latest
    $ unzip raspbian_lite_latest
```
### Flash the SD card
Download Etcher [here](https://www.balena.io/etcher/) or on mac/homebrew:
```
    $ brew cask install etcher
```
Open Etcher and select the stretch lite image, the SD and then Flash. After close etcher but dont remove the SD from your PC.

### Setting the image up for wifi
The steps here are taken from [howchoo's guide](https://howchoo.com/g/mzgzy2mwowj/how-to-set-up-raspberry-pi-without-keyboard-monitor-mouse).
To make deployment smoother, we want to set up the Pi without needing to plug the Pi into ethernet, screen, or a mouse and keyboard.

Navigate to the boot directory of your pi (you may need to remove and push back into your Dev PC for this to be doable).
On MacOS:
```
    $ cd /Volumes/boot/
```
Create and empty file called ssh (enables the ssh at boot)
```
    $ touch ssh
```
To enable wifi, in the boot directory, create a file called wpa_supplicant.conf with the contents:
```
    ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
network={
        ssid="YOUR_NETWORK_NAME"
        psk="YOUR_PASSWORD"
        key_mgmt=WPA-PSK
    }
```
Eject your SD card from the Dev PC.

### Connecting to the Pi
Place the SD card in your Pi and Connect power via the micro USB cable and plug.

If there is only one Pi on your network, to get the IP, you can simply:

```
    $ ping raspberrypi
```
Or if there is more than one Pi on your network, you can try finding yours using [nmap](https://raspberrypi.stackexchange.com/questions/13936/find-raspberry-pi-address-on-local-network).

Then SSH by:

```
    $ ssh pi@PI_IP_ADDRESS
```
The default user is `pi` and the password is `raspberry`.

Make sure you change the username and password right away to avoid anyone having access.

Or if there is more than one Pi on your network, you can try finding yours using [nmap](https://raspberrypi.stackexchange.com/questions/13936/find-raspberry-pi-address-on-local-network).

Two issues faced at this stage:
- Cant find IP via nmap, one solution is sadly plugging in a monitor.
- cant connect via SSH? Remove SD and place back in Dev PC, check that the ssh file is still present, if not, create again.