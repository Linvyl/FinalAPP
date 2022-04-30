class Admin:

    def __init__(self , adminId , adminAge , contactAdd, personalEmail, adminEmail , adminPass):
        self.adminId = adminId
        self.adminAge = adminAge
        self.contactAdd = contactAdd
        self.personalEmail = personalEmail
        self.adminEmail = adminEmail
        self.adminPass = adminPass

    def set_adminId(self , adminId):
        self.adminId = adminId

    def get_adminId(self):
        return self.adminId

    def set_adminAge(self, adminAge):
        self.adminAge = adminAge

    def get_adminAge(self):
        return self.adminAge

    def set_contactAdd(self , contactAdd):
        self.contactAdd = contactAdd

    def get_contactAdd(self):
        return self.contactAdd

    def set_personalEmail(self , personalEmail):
        self.personalEmail = personalEmail

    def get_personalEmail(self):
        return self.personalEmail

    def set_adminEmail(self, adminEmail):
        self.adminEmail = adminEmail

    def get_adminEmail(self):
        return self.adminEmail

    def set_adminPass(self, adminPass):
        self.adminPass = adminPass

    def get_adminPass(self):
        return self.adminPass

    def show_info(self):
        print(f"AdminId : {self.get_adminId() }")
        print(f"Name : {self.adminAge }")
        print(f"Name : {self.contactAdd}")
        print(f"Name : {self.personalEmail}")
        print(f"Dob : {self.adminEmail }")
        print(f"Mark : {self.adminPass }")


class Train:
    count = 0

    def __init__(self, trainId, departTime, departure, destination):
        self.trainId = trainId
        self.date = date
        self.ticketId = ticketId
        self.adminId = adminId
        Train.count += 1

    def set_trainId(self , trainId):
        self.trainId= trainId

    def get_trainId(self):
        return self.trainId

    def set_date(self , date):
        self.date = date

    def get_date(self):
        return self.date

    def set_ticketId(self , ticketId):
        self.ticketId = ticketId

    def get_ticketId(self):
        return self.ticketId

    def set_adminId(self , adminId):
        self.adminId = adminId

    def get_adminId(self):
        return self.adminId


    def show_info(self):
        print(f"TrainId : {self.get_trainId() }")
        print(f"Date : {self.date }")
        print(f"TicketId : {self.get_ticketId}")
        print(f"AdminId : {self.get_adminId}")



class Worker:
    count = 0

    def __init__(self, workerId, trainId, workerName, workerAge, phoneNum, shift, job, drivingLicense):
        self.workerId = workerId
        self.trainId = trainId
        self.workerName = workerName
        self.workerAge = workerAge
        self. phoneNum =  phoneNum
        self.shift = shift
        self.job = job
        self.drivingLicense = drivingLicense
        Worker.count += 1

    def set_workerId(self, workerId):
        self.workerId = workerId

    def get_workerId(self):
        return self.workerId

    def set_trainId(self, trainId):
        self.trainId = trainId

    def get_trainId(self):
        return self.trainId

    def set_workerName(self, workerName):
        self.workerName = workerName

    def get_workerName(self):
        return self.workerName

    def set_workerAge(self, workerAge):
        self.workerAge = workerAge

    def get_workerAge(self):
        return self.workerAge

    def set_ phoneNum(self,  phoneNum):
        self.phoneNum =  phoneNum

    def get_ phoneNum(self):
        return self. phoneNum

    def set_shift(self, shift):
        self.shift = shift

    def get_shift(self):
        return self.shift

    def set_job(self, job):
        self.job = job

    def get_job(self):
        return self.job

    def set_drivingLicense(self, drivingLicense):
        self.drivingLicense = drivingLicense

    def get_drivingLicense(self):
        return self.drivingLicense

    def show_info(self):
        print(f"WorkerId : {self.get_workerId()}")
        print(f"TrainId : {self.get_trainId}")
        print(f"WorkAge : {self.workAge}")
        print(f"PhoneNum : {self.phoneNum}")
        print(f"Shift : {self.shift}")
        print(f"Job : {self.job}")
        print(f"DrivingLicense : {self.drivingLicense}")


class Customer:
    count = 0

    def __init__(self, cusId, cusName, cusEmail , cusAge, cusGender):
        self.cusId = cusId
        self.cusName = cusName
        self.cusEmail = cusEmail
        self.cusAge = cusAge
        self.cusGender = cusGender
        Customer.count += 1

    def set_cusId(self, cusId):
        self.cusId = cusId

    def get_cusId(self):
        return self.cusId

    def set_cusName(self, cusName):
        self.cusName = cusName

    def get_cusName(self):
        return self.cusName

    def set_cusEmail(self, cusEmail):
        self.cusEmail = cusEmail

    def get_cusEmail(self):
        return self.cusEmail

    def set_cusAge(self, cusAge):
        self.cusAge = cusAge

    def get_cusAge(self):
        return self.cusAge

    def set_cusGender(self, cusGender):
        self.cusGender = cusGender

    def get_cusGender(self):
        return self.cusGender

    def show_info(self):
        print(f"cusId : {self.get_cusId()}")
        print(f"cusName : {self.cusName}")
        print(f"cusEmail : {self.cusEmail}")
        print(f"CusAge : {self.cusAge}")
        print(f"CusGender : {self.cusGender}")


class Reservation:
    count = 0

    def __init__(self, resId, date, ticketId, adminId, cusId):
        self.resId = resId
        self.date = date
        self.ticketId = ticketId
        self.adminId = adminId
        self.cusId = cusId
        Train.count += 1

    def set_resId(self , resId):
        self.resId = resId

    def get_resId(self):
        return self.resId

    def set_date(self , date):
        self.date = date

    def get_date(self):
        return self.date

    def set_ticketId(self , ticketId):
        self.ticketId = ticketId

    def get_ticketId(self):
        return self.ticketId

    def set_adminId(self , adminId):
        self.adminId = adminId

    def get_adminId(self):
        return self.adminId

    def set_cusId(self , cusId):
        self.cusId = cusId

    def get_cusId(self):
        return self.cusId

    def show_info(self):
        print(f"ResId : {self.get_resId() }")
        print(f"Date : {self.date }")
        print(f"TicketId : {self.get_ticketId}")
        print(f"AdminId : {self.get_adminId}")
        print(f"CusId : {self.get_cusId}")


class Ticket:
    count = 0

    def __init__(self, ticketId, dateAvailable, trainId, resId):
        self.ticketId = ticketId
        self.dateAvailable = dateAvailable
        self.trainId = trainId
        self.resId = resId
        Ticket.count += 1

    def set_ticketId(self , ticketId):
        self.ticketId = ticketId

    def get_ticketId(self):
        return self.ticketId

    def set_dateAvailable(self , dateAvailable):
        self.dateAvailable = dateAvailable

    def get_dateAvailable(self):
        return self.dateAvailable

    def set_trainId(self ,trainId):
        self.trainId = trainId

    def get_trainId(self):
        return self.trainId

    def set_resId(self , resId):
        self.resId = resId

    def get_resId(self):
        return self.resId

    def show_info(self):
        print(f"TicketId : {self.get_ticketId() }")
        print(f"DateAvailable : {self.dateAvailable }")
        print(f"TraintId : {self.get_trainId}")
        print(f"ResId : {self.get_resId}")


