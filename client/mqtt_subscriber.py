import paho.mqtt.client as mqtt

host = "mqtt.eclipseprojects.io"
port = 1883

list_topic = ['SENSOR/HUMIDITY','SENSOR/TEMP','SENSOR/THERMAL']

def on_connect(client, userdata, flags, rc):
    print("Connected to MQTT broker with result code " + str(rc))
    # Subscribe to topic on successful connection
    for topic in list_topic:
        client.subscribe(topic)
        
    
def on_message(client, userdata,msg):
    print(msg.payload.decode("utf-8", "strict"))
    
    #save the data to database ... 
    #code below
    

client = mqtt.Client()
client.max_payload_size = 250
client.on_connect = on_connect
client.on_message = on_message
client.connect(host,port)
client.loop_forever()