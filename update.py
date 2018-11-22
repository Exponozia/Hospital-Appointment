#updating the appointments
from tkinter import *
import tkinter.messagebox
import sqlite3

conn = sqlite3.connect('database.db')
c = conn.cursor()

class Application:
    def __init__(self,master):
        self.master = master
        # Heading Label
        self.heading = Label(master, text='Update Appointment', fg='steelblue',font=('arial 40 bold'))
        self.heading.place(x=150, y=0)

        #Search Criteria
        self.name = Label(master, text="Enter Patient's Name", fg='steelblue', font=('arial 18 bold'))
        self.name.place(x=0, y=60)

        #Entry for the name Label
        self.namenet= Entry(master, width=40)
        self.namenet.place(x=300, y=70)

        #search button
        self.search = Button(master, text="Search", width=30, height=2, bg='steelblue',command=self.search_db)
        self.search.place(x=300, y=100)
    #function to search

    def search_db(self):
        self.input = self.namenet.get()
        #Execute SQL
        sql = "SELECT * FROM appointments WHERE name LIKE ?"
        self.res = c.execute(sql,(self.input,))
        for self.row in self.res:
           self.name1 = self.row[1]
           self.age = self.row[2]
           self.gender = self.row[3]
           self.location = self.row[4]
           self.phone = self.row[5]
           self.time = self.row[6]

        #Creating the update form
        self.uname = Label(self.master, text="Patient's Name ",font=('arial 18 bold'))
        self.uname.place(x=0,y=150)


        self.uage = Label(self.master, text="Age", font=('arial 18 bold'))
        self.uage.place(x=0, y=200)

        self.ugender = Label(self.master, text="Gender", font=('arial 18 bold'))
        self.ugender.place(x=0, y=250)

        self.ulocation = Label(self.master, text="Location", font=('arial 18 bold'))
        self.ulocation.place(x=0, y=300)

        self.uphone = Label(self.master, text="Phone", font=('arial 18 bold'))
        self.uphone.place(x=0, y=350)

        self.utime = Label(self.master, text="Appointment Time", font=('arial 18 bold'))
        self.utime.place(x=0, y=400)

        #Entries for each Labels==========================================
        self.ent1 = Entry(self.master,width=30)
        self.ent1.place(x=300,y=150)
        self.ent1.insert(END,str(self.name1))

        self.ent2 = Entry(self.master, width=30)
        self.ent2.place(x=300, y=200)
        self.ent2.insert(END, str(self.age))

        self.ent3 = Entry(self.master, width=30)
        self.ent3.place(x=300, y=250)
        self.ent3.insert(END, str(self.gender))

        self.ent4 = Entry(self.master, width=30)
        self.ent4.place(x=300, y=300)
        self.ent4.insert(END, str(self.location))

        self.ent5 = Entry(self.master, width=30)
        self.ent5.place(x=300, y=350)
        self.ent5.insert(END, str(self.phone))


        self.ent6 = Entry(self.master, width=30)
        self.ent6.place(x=300, y=400)
        self.ent6.insert(END, str(self.time))

        #Button to execute upadate
        self.update = Button(self.master, text="Update", width=30, height=2, bg='lightblue',command=self.update_db)
        self.update.place(x=300, y=450)

        #Button to delete record from the database
        self.delete = Button(self.master, text="Delete", width=25, height=2, bg='#ff0000', command=self.delete_db)
        self.delete.place(x=100, y=450)


    def update_db(self):
        #declaring the variables in update
        self.var1 = self.ent1.get() #updated name
        self.var2 = self.ent2.get()
        self.var3 = self.ent3.get()
        self.var4 = self.ent4.get()
        self.var5 = self.ent5.get()
        self.var6 = self.ent6.get()

        query = "UPDATE appointments SET name=?, age=?, gender=?, location=?, phone=?, schedule_time=? WHERE name LIKE ?"
        c.execute(query,(self.var1,self.var2,self.var3,self.var4,self.var5,self.var6, self.namenet.get(),))
        conn.commit()
        tkinter.messagebox.showinfo("Updated","Record Successfully Updated")


    def delete_db(self):
        #deleting the appointment
        sql2 = "DELETE FROM appointments WHERE name LIKE ?"
        c.execute(sql2,(self.namenet.get(),))
        conn.commit()
        tkinter.messagebox.showinfo("Deleted","Record Deleted Successfully")
        self.ent1.destroy()
        self.ent2.destroy()
        self.ent3.destroy()
        self.ent4.destroy()
        self.ent5.destroy()
        self.ent6.destroy()


#creating the objects
root = Tk()
b = Application(root)
#resolution of the window
root.geometry("1200x720+0+0")

#preventing the resize feature
root.resizable(False,False)

#end the loop
root.mainloop()
