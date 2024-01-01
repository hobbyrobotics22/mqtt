import threading
from MQTT import MQTT


mqtt = MQTT("192.168.0.154")

threading.Thread(target=mqtt.startClient, args=("apple", "DriveControl")).start()
while True:
    try:
        print(mqtt.MQTT_Message["DriveControl"])
    except:
        pass