#!/usr/bin/python

import smbus
import math
import os
from gps import *
from time import *
import time
import threading
import time
import serial
import smbus
import time
import datetime
from Tkinter import *
import csv


###################################  Open Log File  ##################################
f=open('DataInLog.txt','a')




radio = serial.Serial(
              
               port='/dev/ttyAMA0',
               baudrate = 9600,
               parity=serial.PARITY_NONE,
               stopbits=serial.STOPBITS_ONE,
               bytesize=serial.EIGHTBITS,
               timeout=1
           )
           counter=0

while True:      

datain=radio.readline()

now = datetime.datetime.now()
timestamp = now.strftime("%Y/%m/%d %H:%M")
#Timestamp,Strattoaltitude,GPSAlt,Latitude,Longitude,Xaccel,Yaccel,Zaccel,Xrot,Yrot,Zrot
outstring = str(timestamp)+","+str(datain)+"\n"
f.write(outstring)
    
    
except (KeyboardInterrupt, SystemExit): #when you press ctrl+c
    print "\nKilling Thread..."
    print "Done.\nExiting."    
    
    
    
f.close()







###################################  Create User Window  ###############################

class App:
  
  def __init__(self, master):

        frame = Frame(master)
        frame.grid()

        self.button = Button(frame, text="Quit", bg = "red", fg="black", command=root.destroy)
        self.button.grid(row=0, column=0)

        self.airbrakes = Button(frame, text="Deploy Airbrakes", command=self.airbrake_deploy)
        self.airbrakes.grid(row=1, column=0)

        self.airbrake_text = Label(frame, text="Have the airbrakes deployed?")
        self.airbrake_text.grid(row=2, column=0)

        self.airbrake_status = Canvas(frame, width = 150, height=50, bg="blue")
        self.airbrake_status.grid(row=2, column=1)
        
        self.airbrake_text_id = self.airbrake_status.create_text(10, 10, anchor="nw", text="No")


        self.messages2 = Canvas(frame, width=250, height=50, bg="yellow")
        self.messages2.grid(row=0, column=1)

        self.text_id = self.messages2.create_text(10, 10, anchor="nw", text="No messages to display")
        
        
  def airbrake_deploy(self):
        #Do something to deploy airbrakes
        self.messages2.itemconfig(self.text_id, text="Airbrakes Deployment sent")
        


root = Tk()
app = App(root)
root.title("SLURPL Ground Station")
root.mainloop()
