
import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()
mydb = mysql.connector.connect(
  host = os.getenv('LOCAL_HOST'),
  user = os.getenv('LOCAL_USER'),
  password = os.getenv('LOCAL_PASSWORD'),
  database = os.getenv('LOCAL_DB'),
)

print(mydb)

mycursor = mydb.cursor()

def insert_DB(table_name, msg, topic):
  
  id, time, data = msg.payload.decode("utf-8", "strict").split(";")
  mycursor.execute("SELECT Node_id FROM sensor_records WHERE Node_id = " + id + " AND Time = TIMESTAMP('" + time + "')")
  query = mycursor.fetchone()

  if query is None:
    if (topic == "SENSOR/HUMIDITY"):
      sql = "INSERT INTO " + table_name + " (Node_id, Time, Humidity) VALUES (%s, %s, %s)"
    elif (topic == "SENSOR/TEMP"):
      sql = "INSERT INTO " + table_name + " (Node_id, Time, Temperature) VALUES (%s, %s, %s)"
    elif (topic == "SENSOR/THERMAL"):
      sql = "INSERT INTO " + table_name + " (Node_id, Time, ThermalArray) VALUES (%s, %s, %s)"
    
    val = (id, time, data)
    mycursor.execute(sql, val)
    mydb.commit()
  
  else:
    if (topic == "SENSOR/HUMIDITY"):
      sql = "UPDATE " + table_name + " SET Humidity = %s WHERE Node_id = %s AND Time = TIMESTAMP(%s)"
    elif (topic == "SENSOR/TEMP"):
      sql = "UPDATE " + table_name + " SET Temperature = %s WHERE Node_id = %s AND Time = TIMESTAMP(%s)"
    elif (topic == "SENSOR/THERMAL"):
      sql = "UPDATE " + table_name + " SET ThermalArray = %s WHERE Node_id = %s AND Time = TIMESTAMP(%s)"
    
    val = (data, id, time)
    mycursor.execute(sql, val)
    mydb.commit()


if __name__ == "__main__":
  print("Database")
  insert_DB("sensor_records", ("0001", "2020-01-01 00:00:00", 50, 25, "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16"))
  