
import paho.mqtt.client as mqtt

from sensor import *

class mqtt_publisher:
    
    def __init__(self,host,port=1883):
        self.host = host
        self.port = port
        self.client = mqtt.Client()
        self.client.connect(self.host,self.port)
        self.client.loop_start()
        
    def publish(self,topic,message):
        result, _ = self.client.publish(topic,message)
        if result == mqtt.MQTT_ERR_SUCCESS:
            print(f"Topic:'{topic}' Message:'{message}'")
        else:
            print(f"Failed to publish message to topic '{topic}': {mqtt.error_string(result)}")
        
    def read_sensor_data(self):
        # Client simultaneously reads all the sensors every 3 minutes
        for data in ReadSensor():
            Time = data[0]
            Humidity = data[1]
            Temp = data[2]
            Thermal = data[3]
            
            self.publish("SENSOR/HUMIDITY",Humidity)
            self.publish("SENSOR/TEMP",Temp)
            self.publish("SENSOR/THERMAL",Thermal)
            
    def disconnect(self):
        self.client.loop_stop()
        self.client.disconnect()


if __name__ == "__main__":
    
    #eclipse mosquitto mqtt broker
    iot_node_1 = mqtt_publisher("mqtt.eclipseprojects.io",1883)
    
    iot_node_1.read_sensor_data()
    
    
    
    
    
    







