## RPI Setup

### Connect to the RPI

```
ssh ofry@mserver
```
```
sudo apt-get update
sudo apt update
sudo apt install git
sudo apt-get install libgl1-mesa-glx
```

clone the project's repo:
```
git clone https://github.com/ofryma/rpi-camera-tracker.git
cd rpi-camera-tracker
```

open a python virtual environment:
```
python3 -m venv venv
```

activate the environment:
```
source venv/bin/activate
pip install -r requirements.txt
```

run the sender script:
```
python3 sender.py
```

## Kill Process on port

You can check for running instances of your script or processes using the port with the netstat or ss command:

```sh
sudo netstat -tuln | grep 9999
```
or

```sh
sudo ss -tuln | grep 9999
```
This will list processes using port 9999. If you find any, note the PID (Process ID).

2. Kill the Process Using the Port
If you find a process using the port, you can kill it using the kill command:

```sh
sudo kill -9 <PID>
```
Replace <PID> with the actual process ID you found.


## Camera Configuration

### Step 1: Install Camera Utilities
You need to install the libraspberrypi-bin package, which includes the raspistill command:
```
sudo apt-get install libraspberrypi-bin
```
Try to take an image with this command:
```
rpicam-still --output test.jpg
```
