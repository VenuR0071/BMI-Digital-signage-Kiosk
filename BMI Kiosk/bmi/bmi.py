import weightpublish
import weightsubscribe
import paho.mqtt.client as mqtt
import json


import subprocess
def get_bmi():
    proc1=subprocess.Popen(["python", "D:\\MiniProject\\bmi\\weightpublish.py"])
    proc1.kill()
    proc2=subprocess.Popen(["python", "D:\\MiniProject\\bmi\\weightsubscribe.py"])
    proc2.kill()
    w=weightsubscribe.get_weight()
    print("weight is", w)
    if( w > 5.0):

        import heightpublish
        import heightsubscribe

        proc3=subprocess.Popen(["python", "D:\\MiniProject\\bmi\\heightpublish.py"])
        proc3.kill()
        proc4=subprocess.Popen(["python", "D:\\MiniProject\\bmi\\heightsubscribe.py"])
        proc4.kill()
        h=heightsubscribe.get_height()
        print("height is", h)

    




  


                      

