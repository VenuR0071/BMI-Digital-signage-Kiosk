import paho.mqtt.client as mqtt
import json

Weight = 0

# This is the Subscriber
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("esp32/weight")

def on_message(client, userdata, msg):
    global Weight  # Define Weight as global to assign it a value within the function
    buf = msg.payload.decode()
    data = json.loads(buf)
    Weight = data["weight"]
    print(Weight)
    client.disconnect()  # Disconnect from the MQTT broker after receiving the weight value
 


client = mqtt.Client()
client.connect("68.178.163.199", 1883)

client.on_connect = on_connect
client.on_message = on_message
def get_weight():
   weight=Weight
   return Weight

client.loop_forever()  # Start the MQTT client loop

client.disconnect()  # Disconnect from the MQTT broker after completing the program
