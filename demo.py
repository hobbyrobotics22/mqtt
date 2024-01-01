from MQTT import MQTT


mqtt = MQTT("10.42.0.1")
listener = "listener"
sender = "sender"
topic = "demo"
message = "Hello World!"

# create a listener
mqtt.createListener(listener, topic)

# create a client
mqtt.createSender(sender, topic)

# send message to the mqtt broker
mqtt.send(listener, topic, message, qos=2)
print("Sending Message")

# check the message buffer
while True:
    try:
        if mqtt.MQTT_Message[topic] == message:
            print(mqtt.MQTT_Message[topic])
            break
    except:
        pass