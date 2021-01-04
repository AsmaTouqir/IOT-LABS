
from tkinter import *
gui= Tk()
gui.title("Student Details")
gui.geometry('675x590')

class Student:
    def __init__(self,first,last,email):
        self.first=first
        self.last=last
        
        self.email=first+"."+last+"@gmail.com"
        email.title("Enter your Email id")
        self.label=Label(email,text="Student Information")
        self.label.pack()

        self.greet_button = Button(email,text="FULL NAME",command=self.fullname)
        self.greet_button.pack()

        self.close_button = Button(email,text="Close",command=email.quit)
        self.close_button.pack()
    def fullname(self):
        return '{}{}'.format(self.first,self.last)
class Developer(Student):
    def __init__(self,first,last,prog_lang):
        super().__init__(first,last,email)
        self.prog_lang=prog_lang
a=Developer("Asma","Tauqeer","asmatauqeer@gmail.com")
print(a.fullname())

mygui=Student(gui)
gui.mainloop()
