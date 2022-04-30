from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox
from tkinter import ttk
from PIL import Image, ImageTk
from tkcalendar import *
from random import *




root = Tk()
root.title("UserGUI")

canvas = Canvas(root,width=500,height=500)

label1 = Label(root, text = "WELCOME TO OUR TRAIN BOOKING SYSTEM",font="Raleway").grid(row=0, column=0)

logo = Image.open("C:/Users/Administrator/Desktop/logo.jpg")
logo = ImageTk.PhotoImage(logo)
logo_label = Label(image=logo)
logo_label.image = logo
logo_label.grid(column=0,row=1)
my_tree = None
count=0
i=0

def booking():
    root.destroy()
    root2 = Tk()
    root2.title("Booking")
    fr = Frame(root2)
    fr.pack(pady=20)
           
    Label(fr,text="From: ").grid(row=0,column=0)
    c1=Combobox(fr,values=["Hà Nội","TP Hồ Chí Minh"])
    c1.grid(row=0,column=1)
    Label(fr,text="To: ").grid(row=1,column=0)
    c2=Combobox(fr,values=["Hà Nội","TP Hồ Chí Minh"])
    c2.grid(row=1,column=1)
    Label(fr,text="Type: ").grid(row=2,column=0)

    def set_value():
        if r.get() == 1:
            cal2["state"] = "disabled"
        else:
            cal2["state"] = "normal"
    r = IntVar()
    r.set("1")
    r1=Radiobutton(fr,text="One-way",variable=r, value=1,command=set_value)
    r1.grid(row=2,column=1)
    r2=Radiobutton(fr,text="Round Trip",variable=r, value=2,command=set_value)
    r2.grid(row=3,column=1)
    Label(fr,text="Departure date: ").grid(row=4,column=0)
    cal1=DateEntry(fr)
    cal1.grid(row=4,column=1)
    Label(fr,text="Return date: ").grid(row=5,column=0)
    cal2=DateEntry(fr,state=DISABLED)
    cal2.grid(row=5,column=1)
    Label(fr,text="Name: ").grid(row=6,column=0)
    
    a1=Entry(fr)
    a1.grid(row=6,column=1)
    Label(fr,text="Identity Card: ").grid(row=7,column=0)
    a2=Entry(fr)
    a2.grid(row=7,column=1)
    Label(fr,text="Phone: ").grid(row=8,column=0)
    a3=Entry(fr)
    a3.grid(row=8,column=1)
    Label(fr,text="Email: ").grid(row=9,column=0)
    a4=Entry(fr)
    a4.grid(row=9,column=1)

    my_tree = ttk.Treeview(root2)
    my_tree.pack(pady=20)

    my_tree["columns"] = ("ID", "Name", "Email","Type","Destination","Date")

    my_tree.column("#0",width=0,stretch=0)
    my_tree.column("ID",anchor=CENTER,width=100)
    my_tree.column("Name",anchor=W,width=140)
    my_tree.column("Email",anchor=W,width=140)
    my_tree.column("Type",anchor=W,width=140)
    my_tree.column("Destination",anchor=W,width=140)
    my_tree.column("Date",anchor=W,width=140)

    my_tree.heading("#0",text="",anchor=W)
    my_tree.heading("ID",text="ID",anchor=CENTER)
    my_tree.heading("Name",text="Name",anchor=W)
    my_tree.heading("Email",text="Email",anchor=W)
    my_tree.heading("Type",text="Type",anchor=W)
    my_tree.heading("Destination",text="Destionation",anchor=W)
    my_tree.heading("Date",text="Date",anchor=W)

        

    def receipt():
        receipt = Tk()
        receipt.title("Recipt")

        selected = my_tree.focus()
        values = my_tree.item(selected,"values")
                
        v1 = c1.get()
        v2 = c2.get()
        v3 = r.get()
                
        cost = ""
        Label(receipt,text="ID: "+values[0]).pack()
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
                
                
        def confirm():
            receipt.destroy()            

        cf_button=Button(receipt,text="Confirm",command = confirm)
        cf_button.pack()

    def add_record():
        global count
        global i
        
        if c1.get() == "" or c2.get() == "" or a1.get() =="" or a2.get() =="" or a3.get()=="" or a4.get() =="":
            messagebox.showerror("Error", message = "Opps, you can't leave any field empty")
        else:
            if c1.get() == c2.get():
                messagebox.showerror("Error",message="Sorry,you can't choose the same city")
            else:
                messagebox.showinfo("Records",message="Success!")
                while i <=999999:
                    ticket_id = randint(1,999999)
                    i+=1
                    break
                if r.get() == 1:
                    my_tree.insert(parent="",index="end",iid=count,text="",values=(ticket_id,a1.get(),a4.get(),"One-Way",
                    c1.get()+"-"+c2.get(),cal1.get()))
                    count +=1
                else:
                    my_tree.insert(parent="",index="end",iid=count,text="",values=(ticket_id,a1.get(),a4.get(),"Round Trip"
                    ,c1.get()+"-"+c2.get(),cal1.get()+"-"+cal2.get(),a2.get(),a3.get()))
                    count +=1
            a1.delete(0, END)
            a2.delete(0, END)
            a3.delete(0, END)
            a4.delete(0, END)
    def delete():
        x = my_tree.selection()[0]
        my_tree.delete(x)

    

    booking_button=Button(root2,text="Add Ticket", command  = add_record)
    booking_button.pack(pady=10)
    recepit_button=Button(root2,text="Receipt",command = receipt)
    recepit_button.pack(pady=10)
    details_button = Button(root2, text="Delete",command = delete)
    details_button.pack(pady=10)
    root2.mainloop()






button1 = Button(root, text="Ticket Booking",command=booking)
button1.grid(row=2, column=0,sticky="nsew")







root.mainloop()
