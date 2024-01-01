# mqtt

This repository is used to simplify the use of the mqtt protocol by using the python library paho-mqtt to create clients and subscribe to topics.

> Tested on Ubuntu 20.04 and Ubuntu 22.04

## Setup

Start by installing the mosquitto mqtt broker and python libraries by running the setup.sh script

```
./setup.sh
```

## MQTT JoyStick App 

Check out the mqtt_joystick.py file to see a demonstration on how to subscribe to the and capture the messages sent from the MQTT JoyStick app available for IOS on the app store.

```
python3 mqtt_joystick.py
```











