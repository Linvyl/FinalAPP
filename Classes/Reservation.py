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
