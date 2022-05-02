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
