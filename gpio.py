import RPi.GPIO as GPIO
import tkinter as tk
from tkinter.constants import HORIZONTAL, LEFT
from typing import Counter

led_pin = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(led_pin,GPIO.OUT)
pwm_led=GPIO.PWM(led_pin,500)
pwm_led.start(led_pin,GPIO.OUT)

def update(duty):
    pwm_led.ChangeDutyCycle(float(duty)
    

root = tk.Tk()
root.title("PWM　Power Control")
counter=0
backgroundcolor=0
var.set(str(counter)
label=tk.Label(root,textvariable=var,bg='SpringGreen',fg='white',font=('Consolas',18),width=50,height=2)
scale=tk.Scale(root,from=0, to=100, resolution=1, orient=tk.HORIZONTAL,command=update)
scale.pack()
label.pack()

def add1():
    global counter
    if counter>=100:
        counter=100
    else:
        counter=counter+1
    var.set(str(counter))
    pwm_led.ChangeDutyCycle(counter)

btn1=tk.Button(root,text="+1",font=('Consolas',18),width=15,height=2,command=add1)
btnl.pack(side=tk.LEFT)

def clear():
    global counter
    counter=0
    var.set(str(counter))
    pwm_led.ChangeDutyCycle(counter)

btn3=tk.Button(root,text="0",font=('Consolas',18),width=15,height=2,command=clear)
btn3.pack(side=tk.LEFT)

def sub1():
    global counter
    if counter<=0:
        counter=0
    else:
        counter=counter-1
    var.set(str(counter))
    pwm_led.ChangeDutyCycle(counter)

btn2=tk.Button(root,text="-1",font=('Consolas',18),width=15,height=2,command=sub1)
btn2.pack(side=tk.RIGHT)

root mainloop()
