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
