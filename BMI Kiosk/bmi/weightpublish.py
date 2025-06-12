import paho.mqtt.client as mqtt
import random, threading, json
from datetime import datetime


#====================================================
# MQTT Settings 
MQTT_Broker = "68.178.163.199" #IP address of the MQTT broker
MQTT_Port = 1883
Keep_Alive_Interval =600
MQTT_Topic_Humidity = "weight/measure"

#====================================================

def on_connect2(client, userdata, rc):
	if rc != 0:
		pass
		print("Unable to connect to MQTT Broker")
	else:
		print("Connected with MQTT Broker: ") + str(MQTT_Broker)
def on_publish2(client, userdata, mid):
	pass		
def on_disconnect2(client, userdata, rc):
	if rc !=0:
		pass
		
mqttc = mqtt.Client()
mqttc.on_connect = on_connect2
mqttc.on_disconnect = on_disconnect2
mqttc.on_publish = on_publish2
mqttc.connect(MQTT_Broker, int(MQTT_Port), int(Keep_Alive_Interval))		
	
def publish_To_Topic2(topic, message):
	mqttc.publish(topic,message)
	print ("Published: " + str(message) + " " + "on MQTT Topic: " + str(topic))
	print ("")

#====================================================
# Code to generate Dummy data to MQTT Broker
no_of_records = 0 # counter to get the number of dummy records generated

def publish_value_to_ESP322():
	#threading.Timer(0.3, publish_Fake_Sensor_Values_to_MQTT_test).start()
	#Humidity_Fake_Value = float("{0:.2f}".format(random.uniform(50, 100)))
	Humidity_Data = {}
	Humidity_Data['value1'] = 1
	#Humidity_Data['Date_n_Time'] = str((datetime.today()).strftime("%d-%b-%Y-%H-%M-%S-%f"))
        # Humidity_Data['Humidity'] = str(Humidity_Fake_Value)
	humidity_json_data = json.dumps(Humidity_Data)
	#print ("Publishing fake Humidity Value: " + str(Humidity_Fake_Value) + "...")
	publish_To_Topic2(MQTT_Topic_Humidity, humidity_json_data)
	global no_of_records
	no_of_records = no_of_records + 1
	print("no of records", no_of_records)

publish_value_to_ESP322()
