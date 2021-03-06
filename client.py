import paho.mqtt.client as paho
mqttc = paho.Client()

host = "localhost"
topic = "velocity"
port = 1883


def on_connect(self, mosq, obj, rc):
    print("Connected rc: " + str(rc))


def on_message(mosq, obj, msg):
	vel = str(msg.payload)
	print("Velocity: " + vel[2:len(vel)-1] + "\n")


def on_subscribe(mosq, obj, mid, granted_qos):
    print("Subscribed OK")


def on_unsubscribe(mosq, obj, mid, granted_qos):
    print("Unsubscribed OK")


mqttc.on_message = on_message
mqttc.on_connect = on_connect
mqttc.on_subscribe = on_subscribe
mqttc.on_unsubscribe = on_unsubscribe
print("Connecting to " + host + "/" + topic)
mqttc.connect(host, port=1883, keepalive=60)
mqttc.subscribe(topic, 0)

mqttc.loop_forever()
