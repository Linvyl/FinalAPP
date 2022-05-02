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
