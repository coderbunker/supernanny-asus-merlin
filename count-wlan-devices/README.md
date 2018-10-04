# Installation
## Create a new user on the raspberry py
```
sudo adduser asus-merlin
```

## Install python virtualenv
```
sudo apt-get install virtualenv
```


## Generate a ssh key for the user
```
sudo su - asus-merlin
ssh-keygen -b 4096
```
Deploy the key to all routers

## Clone the code
```
cd /home/asus-merlin
git clone git@github.com:coderbunker/supernanny-assus-merlin.git
```

## Create python virtual env
```
virtualenv /home/asus-merlin/asus-merlin
source /home/asus-merlin/asus-merlin/bin/activate
pip install -r /home/asus-merlin/count-wlan-devices/requirements.txt
```

## Create cron for script
```
crontab -e
```
Content:
```
* * * * * /home/asus-merlin/asus-merlin/bin/python /home/asus-merlin/bin/count-wlan-devices.py
* * * * * ( sleep 15 ; /home/asus-merlin/asus-merlin/bin/python /home/asus-merlin/bin/count-wlan-devices.py )
* * * * * ( sleep 30 ; /home/asus-merlin/asus-merlin/bin/python /home/asus-merlin/bin/count-wlan-devices.py )
* * * * * ( sleep 45 ; /home/asus-merlin/asus-merlin/bin/python /home/asus-merlin/bin/count-wlan-devices.py )
```

