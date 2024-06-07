## RPI Setup

### Connect to the RPI

```
ssh ofry@mserver
```
```
sudo apt-get update && sudo apt update && sudo apt install git && sudo apt-get install libgl1-mesa-glx
```
```
sudo reboot
```

## RPI XRDP

Add remote desktop to the raspberry pi:

```sh
sudo apt-get install xrdp && sudo apt-get install tightvncserver && sudo systemctl start xrdp && ifconfig
```

Find the rpi ip address:
```sh
ifconfig
```

add a user
```
sudo adduser ofryma
sudo usermod -aG sudo ofryma && groups ofryma
```

Editing the sudoers file
open the sudoers file using the command:
```
sudo visudo
```

Add this line with the name of the new user:
```
ofryma ALL=(ALL:ALL) ALL
```

### On windows
Open the *Remote Desktop Connection* (MSTSC) software, enter the rpi ip address and press **connect**.

You can also allow the VNC (Remote GUI) by following this steps:

1. Go to the rpi configuration using this :

```
sudo raspi-config
```

Navigate to: Interface Options > VNC and enable the VNC Server

## Get the project

clone the project's repo:
```
git clone https://github.com/ofryma/rpi-camera-tracker.git
cd rpi-camera-tracker
```

open a python virtual environment:
```
python -m venv --system-site-packages venv
```

activate the environment:
```
venv/bin/python -m pip install -r requirements.txt
```

run script:
```
venv/bin/python camera.py
```

## Camera Configuration

### Step 1: Install Camera Utilities
You need to install the libraspberrypi-bin package, which includes the raspistill command:

Try to take an image with this command:
```
rpicam-still --output test.jpg
```




