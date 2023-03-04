import paho.mqtt.client as mqtt
import socket

host = "mqtt.eclipseprojects.io"
port = 1883

def on_connect(client, userdata, flags, rc):
    print("Connected to MQTT broker with result code " + str(rc))
    # Subscribe to topic on successful connection
    client.subscribe("BROKER/LOGGING") 
    
def on_message(client, userdata, msg):
    print("BROKER LOGGING: " + msg.payload.decode("utf-8", "strict"))

client = mqtt.Client()
client.max_payload_size = 250
client.on_connect = on_connect
client.on_message = on_message
client.connect(host,port)
client.loop_forever()