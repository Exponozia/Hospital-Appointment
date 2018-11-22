#import modules
from tkinter import *
import sqlite3
import tkinter.messagebox
#connect to the database
conn = sqlite3.connect('database.db')
print("successfully connected")

#cursor to move around the database
c = conn.cursor()

#empty list to later append the ids from the database

ids = []


#tkinter window
class Application:
    def __init__(self,master):
        self.master = master

        #creating the frames in the matter
        self.left = Frame(master, width=800, height=720, bg='lightgreen')
        self.left.pack(side=LEFT)

        self.right = Frame(master,width=400,height=720, bg='steelblue')
        self.right.pack(side=RIGHT)

        #labels for the window
        self.heading = Label(self.left, text="HALAM HOSPITAL APPOINTMENTS",font=('arial 34 bold'),fg='black',bg='lightgreen')
        self.heading.place(x=0,y=0)

        #patient name
        self.name = Label(self.left, text = "Patient's Name", font=('arial 18 bold'),fg='black',bg='lightgreen')
        self.name.place(x=0, y=100)

        #patient age
        self.age = Label(self.left, text="Age", font=('arial 18 bold'), fg='black', bg='lightgreen')
        self.age.place(x=0, y=140)

        # patient Gender
        self.gender = Label(self.left, text="Gender", font=('arial 18 bold'), fg='black', bg='lightgreen')
        self.gender.place(x=0, y=180)

        # patient Location
        self.location = Label(self.left, text="Location", font=('arial 18 bold'), fg='black', bg='lightgreen')
        self.location.place(x=0, y=220)

        # Patient Number
        self.phone = Label(self.left, text="Phone No.", font=('arial 18 bold'), fg='black', bg='lightgreen')
        self.phone.place(x=0, y=260)

        # Appointment time
        self.time= Label(self.left, text="Appointment Time", font=('arial 18 bold'), fg='black', bg='lightgreen')
        self.time.place(x=0, y=300)


        #Entries for all labels==================================================================================
        self.name_ent = Entry(self.left,width=40)
        self.name_ent.place(x=220, y=110)

        self.age_ent = Entry(self.left, width=40)
        self.age_ent.place(x=220, y=150)

        self.gender_ent = Entry(self.left, width=40)
        self.gender_ent.place(x=220, y=190)

        self.location_ent = Entry(self.left, width=40)
        self.location_ent.place(x=220, y=230)

        self.phone_ent = Entry(self.left, width=40)
        self.phone_ent.place(x=220, y=270)

        self.time_ent = Entry(self.left, width=40)
        self.time_ent.place(x=220, y=310)

        #Button to perform a command

        self.submit = Button(self.left, text="Add Appointment", width=30, height=2, bg='steelblue',command=self.add_appointment)
        self.submit.place(x=220, y= 350)

        # getting the number of appointments Fixed to view in the log
        sql2 = "SELECT ID FROM appointments"
        self.result = c.execute(sql2)
        for self.row in self.result:
            self.id = self.row[0]
            ids.append(self.id)

        # ordering the ids
        self.new = sorted(ids)
        self.final_id = self.new[len(ids) - 1]

        #displaying the logs in the right frame
        self.logs = Label(self.right, text='Logs',font=('arial 28 bold'), fg='white', bg='steelblue')
        self.logs.place(x=0,y=-15)

        #displaying the logs in our right time
        self.box = Text(self.right,width=60,height=40)
        self.box.place(x=0,y=30)
        self.box.insert(END,'Total Appointment till now: ' + str(self.final_id))

#add functions and event to button
    def add_appointment(self):
        #geeting the user input
        self.val1 = self.name_ent.get()
        self.val2 = self.age_ent.get()
        self.val3 = self.gender_ent.get()
        self.val4 = self.location_ent.get()
        self.val5 = self.phone_ent.get()
        self.val6 = self.time_ent.get()

        #Check if the textbox is empty

        if self.val1=='' or self.val2=='' or self.val3 =='' or self.val4=='' or self.val5=='' or self.val6=='':
            tkinter.messagebox.showinfo("Warning","Please fill all the boxes")
        else:
            #now add to the databasee
            sql = "INSERT INTO 'appointments'  (name, age, gender, location, phone, schedule_time) VALUES (?,?,?,?,?,?)"
            c.execute(sql,(self.val1,self.val2,self.val3,self.val4,self.val5,self.val6))
            conn.commit()
            tkinter.messagebox.showinfo("Success","Appointments of " + str(self.val1) + "has been created" )


            self.box.insert(END,'Appointment fixed for ' +  str(self.val1) + 'at ' + str(self.val5))




#creating the object
root = Tk()
b = Application(root)
#resolution of the window
root.geometry("1200x720+0+0")

#preventing the resize feature
root.resizable(False,False)

#end the loop
root.mainloop()