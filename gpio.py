
import RPi.GPIO as GPIO
import tkinter as tk


GPIO.setwarnings(False)
led_pin = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(led_pin,GPIO.OUT)

pwm_led=GPIO.PWM(led_pin,500)
pwm_led.start(0)

def update(duty):
    global counter
    pwm_led.ChangeDutyCycle(float(duty))
    counter=int(duty)
    var.set(str(counter))
    colorchange()
root=tk.Tk()
root.title("PWM　Power Control")
counter=0
backgroundcolor=0
var=tk.StringVar()
var.set(str(counter))
label=tk.Label(root,textvariable=var,fg='white',font=('Arial',18),width=50,height=2)
scale=tk.Scale(root,from_=0, to=100, resolution=1, orient=tk.HORIZONTAL,command=update,length=500)

scale.pack()
label.pack()
def colorchange():
    if counter > 100:
        label.config(bg='mediumorchid')
    elif counter >= 90 and counter <= 100:
        label.config(bg='violet')
    elif counter >= 80 and counter < 90:
        label.config(bg='royalblue')
    elif counter >= 70 and counter < 80:
        label.config(bg='cyan')
    elif counter >= 60 and counter < 70:
        label.config(bg='paleTurquoise')
    elif counter >= 50 and counter < 60:
        label.config(bg='palegreen')
    elif counter >= 40 and counter < 50:
        label.config(bg='lightgreen')
    elif counter >= 30 and counter < 40:
        label.config(bg='gold')
    elif counter >= 20 and counter < 30:
        label.config(bg='orange')
    elif counter >= 10 and counter < 20:
        label.config(bg='lightcoral')
    elif counter >= 0 and counter < 10:
        label.config(bg='gray')
        
def add1():
    global counter
    if counter>=100:
        counter=100
    else:
        counter=counter+1
    var.set(str(counter))
    pwm_led.ChangeDutyCycle(counter)
    scale.set(counter)

btn1=tk.Button(root,text="+1",font=('Arial',18),width=15,height=2,command=add1)
btn1.pack(side=tk.RIGHT)

def clear():
    global counter
    counter=0
    var.set(str(counter))
    pwm_led.ChangeDutyCycle(counter)
    scale.set(counter)

btn3=tk.Button(root,text="0",font=('Arial',18),width=15,height=2,command=clear)
btn3.pack(side=tk.RIGHT)

def sub1():
    global counter
    if counter<=0:
        counter=0
    else:
        counter=counter-1
    var.set(str(counter))
    pwm_led.ChangeDutyCycle(counter)
    scale.set(counter)

btn2=tk.Button(root,text="-1",font=('Arial',18),width=15,height=2,command=sub1)
btn2.pack(side=tk.LEFT)

root.mainloop()

