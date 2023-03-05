# cpe_project_mqtt

mqtt network project  

- Mr Chanon Khanijoh			63070503408
- Mr. Tunwa Satianrapapong	63070503419
- Mr. Napas Vinitnantharat	63070603422
- Mr. Pechdanai Saepong  		63070503434
- Ms. Fasai Sae-Tae	 		63070503436

## Files

### database.py
 contain function for inserting and updating MySQL database

### mqtt_publisher.py
 contain function for publishing the node information including Node Id, Time sent, Humidity, Temperature, and Thermal array

### mqtt_subscriber.py
 contain function subscribing to three sensor topics and saving the data into MySQL database

### mqtt_broker-log.py
 Our group decided to use a public MQTT broker service named “mqtt.eclipseprojects.io”, but we can’t get the IP address from the public broker. So, we used socket python module to get the hostname and IP address of hostname, then publish to MQTT broker on topic BROKER/LOGGING.

 Each time we connect or disconnect to MQTT broker (both publisher and subscriber) will log into the BROKER/LOGGING topic. The user should run mqtt_broker-log.py first to see the logging.
 
 This file subscribe to BROKER/LOGGING

### sensor.py
 contain function for reading the sensor

### SampleInput.csv
 contain all the output of the sensor

### Create .env file and import the database from data/sensor_records.sql
```
 HOST_MQTT= mqtt.eclipseprojects.io
 PORT_MQTT= 1883
 LOCAL_HOST = 
 LOCAL_USER = 
 LOCAL_PASSWORD = 
 LOCAL_DB = 
```

### instaling packages
```
pip install paho-mqtt
pip install python-dotenv
```

## Running the file
 ### Run broker log first by using the command
 ``` 
 python mqtt_broker-log.py 
 ```

 ### To Subscribe
 ``` 
 cd client 
 python mqtt_subscriber.py
 ```

 ### To Publish
 ``` 
 cd client
 python mqtt_publisher.py 
 ```
