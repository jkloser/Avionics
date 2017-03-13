from Tkinter import *
import csv
import time


data = csv.DictReader(open("data.txt"))

    

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

  

        #self.messages = Label(frame, text="No messages to display")
        #self.messages.grid(ERROR)

        self.messages2 = Canvas(frame, width=250, height=50, bg="yellow")
        self.messages2.grid(row=0, column=1)

        self.text_id = self.messages2.create_text(10, 10, anchor="nw", text="No messages to display")

############# Still trying to figure out how to read from csv files  ###########################
        for row in data:
            if row['airbrake'] == '1':
                self.airbrake_status.itemconfig(self.airbrake_text_id, text="Yes")
            else:
                self.airbrake_status.itemconfig(self.airbrake_text_id, text="No")

        

    def airbrake_deploy(self):
        #Do something to deploy airbrakes
        self.messages2.itemconfig(self.text_id, text="Airbrakes Deployment sent")
        


root = Tk()
app = App(root)
root.title("SLURPL Ground Station")
root.mainloop()

file.close()
