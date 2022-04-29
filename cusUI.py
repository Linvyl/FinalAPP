from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox
from tkinter import ttk
from PIL import Image, ImageTk
from tkcalendar import *
from random import *

root = Tk()
root.title("UserGUI")

canvas = Canvas(root,width=600,height=300)

label1 = Label(root, text = "WELCOME TO OUR TRAIN BOOKING SYSTEM",font="Raleway").grid(row=0, column=0)

logo = Image.open("C:/Users/Administrator/Desktop/logo.jpg")
logo = ImageTk.PhotoImage(logo)
logo_label = Label(image=logo)
logo_label.image = logo
logo_label.grid(column=0,row=1)
tv = None

def booking():
    root.destroy()
    root2 = Tk()
    root2.title("Booking")
    ticket_id = randint(1,999999)
    Label(root2,text="From: ").grid(row=0,column=0)
    c1=Combobox(root2,values=["Hà Nội","TP Hồ Chí Minh"])
    c1.grid(row=0,column=1)
    Label(root2,text="To: ").grid(row=1,column=0)
    c2=Combobox(root2,values=["Hà Nội","TP Hồ Chí Minh"])
    c2.grid(row=1,column=1)
    Label(root2,text="Type: ").grid(row=2,column=0)

    def set_value():
        if r.get() == 1:
            cal2["state"] = "disabled"
        else:
            cal2["state"] = "normal"
    r = IntVar()
    r.set("1")
    r1=Radiobutton(root2,text="One-way",variable=r, value=1,command=set_value).grid(row=2,column=1)
    r2=Radiobutton(root2,text="Round trip",variable=r, value=2,command=set_value).grid(row=3,column=1)
    Label(root2,text="Departure date: ").grid(row=4,column=0)
    cal1=DateEntry(root2).grid(row=4,column=1)
    Label(root2,text="Return date: ").grid(row=5,column=0)
    cal2=DateEntry(root2,state=DISABLED)
    cal2.grid(row=5,column=1)
    Label(root2,text="Name: ").grid(row=6,column=0)
    
    a1=Entry(root2)
    a1.grid(row=6,column=1)
    Label(root2,text="Identity Card: ").grid(row=7,column=0)
    a2=Entry(root2)
    a2.grid(row=7,column=1)
    Label(root2,text="Phone: ").grid(row=8,column=0)
    a3=Entry(root2)
    a3.grid(row=8,column=1)
    Label(root2,text="Email: ").grid(row=9,column=0)
    a4=Entry(root2)
    a4.grid(row=9,column=1)

    fr = Frame(root2)
    fr.grid(row=10)
    
    tv = ttk.Treeview(fr, column=("id","name","identity card","destination","date","cost"),show="headings",height="4")
        
    tv.grid(row=10)

    tv.insert("",END,values=("1","thang","001202011097","Ha Noi - TP HCM","29/4/2022","25$"))
    tv.heading("id", text="ID")
    tv.heading("name", text="Name")
    tv.heading("identity card", text="Identity Card")
    tv.heading("destination", text="Destination")
    tv.heading("date", text="Date")
    tv.heading("cost", text="Cost")
    

    def book_event():
        if c1.get() == "" or c2.get() == "" or a1.get() =="" or a2.get() =="" or a3.get()=="" or a4.get() =="":
            messagebox.showerror("Error", message = "Opps, you can't leave any field empty")
        else:
            if c1.get() == c2.get():
                messagebox.showerror("Error",message="Sorry,you can't choose the same city")
            else:
                messagebox.showinfo("Records",message="Success!")
                receipt = Tk()
                receipt.title("Recipt")
                
                v1 = c1.get()
                v2 = c2.get()
                v3 = r.get()
                
                cost = ""
                Label(receipt,text="ID: "+ str(ticket_id)).pack()
                Label(receipt,text="From: " + v1).pack()
                Label(receipt,text="To: " + v2).pack()
                Label(receipt,text="Time: 6:00 AM or 15:00 PM or 20:00 PM").pack()
                if v3 == 1:
                    cost = "25$"
                    Label(receipt,text="Type: One-way" ).pack()
                    Label(receipt,text="Cost: "+cost).pack()
                else:
                    cost = "50$"
                    Label(receipt,text="Type: Round trip" ).pack()
                    Label(receipt,text="Cost: "+cost).pack()
                
                
                    

                cf_button=Button(receipt,text="Confirm")
                cf_button.pack()

    def confirm_event():
        tv["id"] = ticket_id
        tv["name"] = a1.get()
        tv["identity card"] = a2.get()
        tv["destination"] = c1.get() + "-" + c2.get()

        tv.insert("",END,values=(tv["id"],tv["name"],tv["identity card"],tv["destination"]))
    
    def details():
        root3 = Tk()
        
        root3.title("Search")
    
    
    booking_button=Button(root2,text="Confirm", command  = confirm_event and book_event)
    booking_button.grid(row=11,column=0,stick="nsew")
    details_button = Button(root2, text="Details",command=details)
    details_button.grid(row=11, column=1,stick="nsew")
    root2.mainloop()



button1 = Button(root, text="Ticket Booking",command=booking)
button1.grid(row=2, column=0,sticky="nsew")


root.mainloop()
