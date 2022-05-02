import math
class Admin:
    
    def __init__(admin,Admin_ID , Admin_Name , Admin_Age, ContactAddress,Admin_Email,Admin_Personal_Email):
        admin.Admin_Name = Admin_Name
        admin.ContactAddress = ContactAddress
        admin.Admin_Age = Admin_Age  
        admin.Admin_ID = Admin_ID
        admin.Admin_Email = Admin_Email
        admin.Admin_Personal_Email = Admin_Personal_Email

    def set_Admin_Name(admin, Admin_Name):
        admin.Admin_Name = Admin_Name
    
    def set_Admin_Age(admin, Admin_Age):
        admin.Admin_Age = Admin_Age
    
    def set_Admin_ID(admin, Admin_ID):
        admin.Admin_ID = Admin_ID

    def set_Admin_Email(admin, Admin_Email):
        admin.Admin_Email = Admin_Email

    def set_ContactAddress(admin, ContactAddress):
        admin.ContactAddress = ContactAddress

    def set_Admin_Personal_Email(admin, Admin_Personal_Email):
        admin.Admin_Personal_Email = Admin_Personal_Email          


    def get_Admin_Age(admin):
        return admin.Admin_Age   

    def get_Admin_Name(admin):
        return admin.Admin_Name

    def get_ContactAddress(admin):
        return admin.ContactAddress
    
    def get_Admin_Email(admin):
        return admin.Admin_Email
    
    def get_Admin_Personal_Email(admin):
        return admin.Admin_Personal_Email 

    def get_Admin_ID(admin):
        return admin.Admin_ID     
    
    def show_info(admin):
        print(f"{ admin.get_Admin_ID()}\t {admin.get_Admin_Name() }\t{ admin.get_Admin_Age()}\t{ admin.get_ContactAddress() }\t{ admin.get_Admin_Email()}\t{ admin.get_Admin_Personal_Email()}")
  
class Customer:
    
    def __init__(customer,customer_ID , customer_Name , customer_Age, customer_Gender,customer_Email):
        customer.customer_Name = customer_Name
        customer.customer_Gender = customer_Gender
        customer.customer_Age = customer_Age  
        customer.customer_ID = customer_ID
        customer.customer_Email = customer_Email

    def set_customer_Name(customer, customer_Name):
        customer.customer_Name = customer_Name
    
    def set_customer_Age(customer, customer_Age):
        customer.customer_Age = customer_Age
    
    def set_customer_ID(customer, customer_ID):
        customer.customer_ID = customer_ID

    def set_customer_Email(customer, customer_Email):
        customer.customer_Email = customer_Email

    def set_customer_Gender(customer, customer_Gender):
        customer.customer_Gender = customer_Gender
        
    def get_customer_Age(customer):
        return customer.customer_Age   

    def get_customer_Name(customer):
        return customer.customer_Name

    def get_customer_Gender(customer):
        return customer.customer_Gender
    
    def get_customer_Email(customer):
        return customer.customer_Email
    
    def get_customer_ID(customer):
        return customer.customer_ID     
    
    def show_customer(customer):
        print(f"{ customer.get_customer_ID()}\t{ customer.get_customer_Name() }\t{ customer.get_customer_Gender() }\t{ customer.get_customer_Email()}\t{ customer.get_customer_Age()}")

class Reservation:
    
    def __init__(Res,Customer_ID , Ticket_ID , Res_ID, Date,Admin_ID):
        Res.Ticket_ID = Ticket_ID
        Res.Date = Date
        Res.Res_ID = Res_ID  
        Res.Customer_ID = Customer_ID
        Res.Admin_ID = Admin_ID

    def set_Ticket_ID(Res, Ticket_ID):
        Res.Ticket_ID = Ticket_ID
    
    def set_Res_ID(Res, Res_ID):
        Res.Res_ID = Res_ID
    
    def set_Customer_ID(Res, Customer_ID):
        Res.Customer_ID = Customer_ID

    def set_Admin_ID(Res, Admin_ID):
        Res.Admin_ID = Admin_ID

    def set_Date(Res, Date):
        Res.Date = Date
        
    def get_Res_ID(Res):
        return Res.Res_ID   

    def get_Ticket_ID(Res):
        return Res.Ticket_ID

    def get_Date(Res):
        return Res.Date
    
    def get_Admin_ID(Res):
        return Res.Admin_ID
    
    def get_Customer_ID(Res):
        return Res.Customer_ID     
    
    def show_res(Res):
        print(f"{ Res.get_Customer_ID() }\t{ Res.get_Ticket_ID() }\t{ Res.get_Res_ID()}\t{ Res.get_Date()}\t{ Res.get_Admin_ID()}")

class Ticket:
    def __init__(Ticket,Ticket_ID , Date_Available, Date,Train_ID,Departure_Time,Landing_Time,Class,Departure,Destination,Kind):
        Ticket.Date = Date
        Ticket.Date_Available = Date_Available  
        Ticket.Ticket_ID = Ticket_ID
        Ticket.Train_ID = Train_ID
        Ticket.Landing_Time = Landing_Time
        Ticket.Departure = Departure
        Ticket.Class = Class  
        Ticket.Departure_Time = Departure_Time
        Ticket.Destination = Destination
        Ticket.Kind = Kind

    def set_Landing_Time(Ticket, Landing_Time):
        Ticket.Landing_Time = Landing_Time
    
    def set_Class(Ticket, Class):
        Ticket.Class = Class
    
    def set_Departure_Time(Ticket, Departure_Time):
        Ticket.Departure_Time = Departure_Time

    def set_Destination(Ticket, Destination):
        Ticket.Destination = Destination

    def set_Departure(Ticket, Departure):
        Ticket.Departure = Departure

    def set_Kind(Ticket, Kind):
        Ticket.Kind = Kind    

    def set_Ticket_ID(Ticket, Ticket_ID):
        Ticket.Ticket_ID = Ticket_ID
    
    def set_Date_Available(Ticket, Date_Available):
        Ticket.Date_Available = Date_Available   

    def set_Train_ID(Ticket, Train_ID):
        Ticket.Train_ID = Train_ID

    def set_Date(Ticket, Date):
        Ticket.Date = Date

    def get_Class(Ticket):
        return Ticket.Class   

    def get_Landing_Time(Ticket):
        return Ticket.Landing_Time

    def get_Departure(Ticket):
        return Ticket.Departure
    
    def get_Destination(Ticket):
        return Ticket.Destination
    
    def get_Departure_Time(Ticket):
        return Ticket.Departure_Time 

    def get_Kind(Ticket):
        return Ticket.Kind

    def get_Date_Available(Ticket):
        return Ticket.Date_Available     

    def get_Date(Ticket):
        return Ticket.Date
    
    def get_Train_ID(Ticket):
        return Ticket.Train_ID
    
    def get_Ticket_ID(Ticket):
        return Ticket.Ticket_ID     
    
    def show_ticket(Ticket):
        print(f"{ Ticket.get_Ticket_ID() }\t{ Ticket.get_Date_Available() }\t{ Ticket.get_Date()}\t{ Ticket.get_Destination()}\t{ Ticket.get_Train_ID() }\t{ Ticket.get_Departure_Time() }\t{ Ticket.get_Landing_Time()}\t{ Ticket.get_Class()}\t{ Ticket.get_Departure()}\t{ Ticket.get_Kind()}")

class train:
    def __init__(train,Train_ID , Departure, Destination, Departure_time,Departure_Date,seat,Price):
        train.Departure= Departure
        train.Departure_time = Departure_time
        train.Destination = Destination  
        train.Train_ID = Train_ID
        train.Departure_Date = Departure_Date  
        train.seat = seat
        train.Price = Price

    def set_train_Name(train, train_Departure):
        train.Departure= train_Departure

    def set_Price(train, Price):
        train.Price= Price    
    
    def set_Destination(train, Destination):
        train.Destination = Destination
    
    def set_Train_ID(train, Train_ID):
        train.Train_ID = Train_ID

    def set_Departure_Date(train, Departure_Date):
        train.Departure_Date = Departure_Date

    def set_Departure_time(train, Departure_time):
        train.Departure_time = Departure_time

    def set_seat(train, seat):
        train.seat = seat          

    def get_Price(train):
        return train.Price 

    def get_Destination(train):
        return train.Destination   

    def get_Departure(train):
        return train.Departure

    def get_Departure_time(train):
        return train.Departure_time
    
    def get_Departure_Date(train):
        return train.Departure_Date
    
    def get_seat(train):
        return train.seat 

    def get_Train_ID(train):
        return train.Train_ID     
    
    def show_train(train):
        print(f"{ train.get_Train_ID() }\t{ train.get_Departure() }\t{ train.get_Destination()}\t{ train.get_Departure_time()}\t{ train.get_Departure_Date()}\t{ train.get_seat()}\t{ train.get_Price()}")

class worker:
    def __init__(worker,Worker_ID,Worker_Name,Worker_age,Worker_phonenumber,shift,Job,driverlicense):
        worker.Worker_Name= Worker_Name
        worker.Worker_phonenumber =Worker_phonenumber
        worker.Destination =Worker_age  
        worker.Worker_ID = Worker_ID
        worker.shift = shift  
        worker.Job = Job
        worker.age=Worker_age
        worker.driverlicense=driverlicense

    def set_Worker_age(worker,worker_age):
        worker.worker_age=worker_age

    def set_Worker_Name(worker, Worker_Name):
        worker.Worker_Name= Worker_Name  
    
    def set_Destination(worker,Worker_age):
        worker.Destination =Worker_age
    
    def set_Worker_ID(worker, Worker_ID):
        worker.Worker_ID = Worker_ID

    def set_shift(worker, shift):
        worker.shift = shift

    def set_Worker_phonenumber(worker,Worker_phonenumber):
        worker.Worker_phonenumber =Worker_phonenumber

    def set_Job(worker, Job):
        worker.Job = Job       

    def set_driverlicense(worker, driverlicense):
        worker.driverlicense = driverlicense         

    def get_driverlicense(worker):
        return worker.driverlicense  

    def get_Worker_Name(worker):
        return worker.Worker_Name

    def get_Worker_phonenumber(worker):
        return worker.Worker_phonenumber
    
    def get_shift(worker):
        return worker.shift
    
    def get_Job(worker):
        return worker.Job 

    def get_Worker_ID(worker):
        return worker.Worker_ID 

    def get_Worker_age(worker):
        return worker.age        
    
    def show_worker(worker):
        print(f"{ worker.get_Worker_ID() }\t{ worker.get_Worker_Name() }\t{ worker.get_Worker_age()}\t{ worker.get_Worker_phonenumber()}\t{ worker.get_shift()}\t{ worker.get_Job()}\t{ worker.get_driverlicense()}")
#main
listadmin=[]
listcustomer=[]
listtrain=[]
listworker=[]
listticket=[]
listreservation=[]
while True:
    print("1.Add Admin")
    print("2.Admin list")
    print("3.Add customer")
    print("4.Customer list")
    print("5.Add reservation")
    print("6.Reservation list")
    print("7.Add train")
    print("8.Train list")
    print("9.Add ticket")
    print("10.List ticket")
    print("11.Add worker  ")
    print("12.List worker")

    action =0
    action =int(input("Select an option: "))    
    if action == 0:
            break
    elif action == 1:
            no = int(input("Input number of admins: "))
            for i in range (0,no):
                print(f"Input admin number {i+1} : ")
                Admin_ID =input("ID: ")
                Admin_Name = input("Name: ")
                ContactAddress = input("Contact Address: ")
                Admin_Age = input("Age: ")
                Admin_Email =input ("Admin Email: ")
                Admin_Personal_Email = input("Personal Email: ")
                st = Admin(Admin_ID , Admin_Name,  ContactAddress, Admin_Age,Admin_Email,Admin_Personal_Email)
                listadmin.append(st)                 
        
    elif action == 2:
            if len(listadmin) == 0:
                print("\n 0 admin found")
            else: 
                print(f"\nADMIN LIST:")
                print(f"ID\t Name\t Address\t Age\t Admin email\t Personal email")              
                for i in listadmin:
                    i.show_info()
        
    elif action == 3:
            no = int(input("Input number of customer: "))
            for i in range (0,no):
                print(f"Input customer number {i+1} : ")
                customer_ID = input("ID: ")
                customer_Name =input("Name: ")
                customer_Gender = input("Gender: ")
                customer_Age = input("Age: ")              
                customer_Email =input ("Customer Email: ")
                cs = Customer(customer_ID , customer_Name,  customer_Gender, customer_Age, customer_Email)
                listcustomer.append(cs)    

    elif action == 4:
            if len(listcustomer) == 0:
                print("\n 0 customer found")
            else:      
                print(f"\nCUSTOMER LIST:")
                print(f"ID\t Name\tAge\tCustomer Email\tGender")       
                for i in listcustomer:
                    i.show_customer()
    
    elif action == 5:
            no = int(input("Input number of ticket you want to book online: "))
            for i in range (0,no):
                print(f"Input ticket number {i+1} : ")
                customer_ID = input("Customer ID: ")
                Ticket_ID =input("Ticket ID: ")
                Res_ID = input("Reservation ID: ")
                Date = input("Date: ")              
                Admin_ID =input ("Admin ID: ")
                rv = Reservation(customer_ID , Ticket_ID,  Res_ID, Date,  Admin_ID )
                listreservation.append(rv)  

    elif action == 6:
            if len(listreservation) == 0:
                print("\n 0 reservation found")
            else:      
                print(f"Customer ID\t Ticket ID\tReservation ID\tDate\tAdmin ID")       
                for i in listreservation:
                    i.show_res()

    elif action ==7:
            no = int(input("Input number of train: "))
            for i in range (0,no):
                print(f"Input train number {i+1} : ")
                Train_ID = input("Train ID: ")
                Departure =input("Departure: ")
                Destination = input("Destination: ")
                Departure_time = input("Departure time: ")              
                Departure_Date =input ("Departure Date ")
                seat =input ("Seat: ")
                Price =input ("Price: ")
                tr = train( Train_ID , Departure,  Destination, Departure_time,  Departure_Date,seat,Price )
                listtrain.append(tr)  

    elif action == 8:
            if len(listtrain) == 0:
                print("\n 0 train found")
            else:      
                print(f"Train ID\t Departure\t Destination\tDeparture time\tDeparture Date\tSeat\tPrice")       
                for i in listtrain:
                    i.show_train()
            
    elif action == 9:
            no = int(input("Input number of ticket: "))
            for i in range (0,no):
                print(f"Input ticket number {i+1} : ")
                Ticket_ID  = input("Ticket ID: ")
                Date_Available =input("Date Available: ")
                Date = input("Date: ")
                Train_ID = input("Train ID: ")              
                Departure_Time =input ("Departure Time: ")
                Landing_Time =input ("Landing Time: ")
                Class =input ("Class: ")
                Departure =input ("Departure: ")
                Destination =input ("Destination: ")
                Kind =input ("Type of ticket: ")
                tk = Ticket(  Ticket_ID , Date_Available, Date, Train_ID,Departure_Time,Landing_Time,Class,Departure,Destination,Kind )          
                listticket.append(tk)      
    elif action ==10:
            if len(listticket) == 0:
                print("\n 0 ticket found")
            else:      
                print(f"Ticket ID\t Date Available\tDate\t Destination\tTrain ID\tDeparture Time\tLanding Time\tClass\tDeparture\tKind")       
                for i in listticket:
                    i.show_ticket()   

    elif action == 11:
            no = int(input("Input number of worker: "))
            for i in range (0,no):
                print(f"Input worker number {i+1} : ")
                Worker_ID  = input("Worker ID: ")
                Worker_Name =input("Worker Name: ")
                Worker_age = input("Worker age: ")
                Worker_phonenumber = input("Worker phone number: ")              
                shift =input ("Shift: ")
                Job =input ("Job: ")
                driverlicense =input ("Driving license: ")
                wk = worker( Worker_ID , Worker_Name,Worker_age, Worker_phonenumber,shift,Job,driverlicense )          
                listworker.append(wk)      

    elif action ==12:
            if len(listworker) == 0:
                print("\n 0 worker found")
            else:      
                print(f"Worker ID:\t Worker Name\tWorker age\t Worker phone number\tShift\tJob\tDriving license")       
                for i in listworker:
                      i.show_worker()   
    print("\nYou must input digits!")
