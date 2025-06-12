import paho.mqtt.client as mqtt
import json

Height =0
# This is the Subscriber

def on_connect(client, userdata, flags, rc):
  data=print("Connected with result code "+str(rc))
  client.subscribe("esp32/height")
  return data


def on_message(client, userdata, msg):
    global Height
    buf=msg.payload.decode()
    data = json.loads(buf)
    Height = data["Height"]
    print(Height)
    client.disconnect()  # Disconnect from the MQTT broker after receiving the weight value
    return Height
    #write_weight_to_file()  # Write the weight value to a file
    
    
    
    
client = mqtt.Client()
client.connect("68.178.163.199",1883)

client.on_connect = on_connect
client.on_message = on_message

def get_height():
   height=Height
   return height

client.loop_forever()
client.disconnect()
