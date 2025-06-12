#Simple BMI calculator using python
import bmi

def bodymassindex(height, weight):
    return round((weight / height**2),2)
#name = input("Enter your name: ")
height = bmi.h
w = bmi.w
h = height/100
water = round(float(w*0.033),1)

bmi = bodymassindex(h, w)

import show_text
a1=show_text.a
b2=show_text.b
c2=show_text.c
d2=show_text.d
def display():
    print(" ")
    print("❗❗General Health tips to maintain the normal BMI value")
    print("--------------------------------------------------------")
    print(" ")
    print( "you must drink atleast 🥛",water,"litres of water")
    print(" ")
    return None
def A1():
    result = print("RESULT : Your weight is  underweight.")
    display()
    print(a1)
    return None
def B1():
    print("RESULT : Your weight is normal.")
    display()
    print(b2)
    return None
def C1():
    print("RESULT : Your BMI is overweight.")
    display()
    print(c2)
    return None
def D1():
    print("RESULT : Your are obese.")
    display()
    print(d2)
    return None
if bmi <= 18.5:    
     result=A1
     
elif 18.5 < bmi <= 24.9:
     result=B1
     
elif 25 < bmi <= 29.29:
     result=C1
     
else:
     result=D1
     
