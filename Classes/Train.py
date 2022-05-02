class Train:
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
