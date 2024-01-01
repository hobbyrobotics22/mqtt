
from MQTT import MQTT


mqtt = MQTT("10.42.0.1")
mqtt.createListener("apple", "DriveControl")

while True:
    try:
        print(mqtt.MQTT_Message["DriveControl"])
    except:
        pass