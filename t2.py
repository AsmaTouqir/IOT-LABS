from tkinter import *

class Program:
    def __init__(self,master):
        self.master=master
        master.title("Welcome to our Page")

        self.label=Label(master,text="JEWELLRY STORE")
        self.label.pack()

        self.greet_button = Button(master,text="Greet",command=self.greet)
        self.greet_button.pack()

        self.close_button = Button(master,text="Close",command=master.quit)
        self.close_button.pack()
    def greet(self):
        print("Greetings!")

gui=Tk()
mygui=Program(gui)
gui.mainloop()
