
import mysql.connector

mydb = mysql.connector.connect(
  host = "localhost",
  user = "",
  password = "",
  database = "mqtt_db"
)

print(mydb)

mycursor = mydb.cursor()

def insert_DB(table_name, data):
    sql = "INSERT INTO " + table_name + " (Node_id, Time, Humidity, Temperature, ThermalArray) VALUES (%s, %s, %s, %s, %s)"
    mycursor.execute(sql, data)
    mydb.commit()


if __name__ == "__main__":
  print("Database")
  insert_DB("sensor_records", ("0001", "2020-01-01 00:00:00", 50, 25, "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16"))
  