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
    
    def findByID(admin, Admin_ID):
        searchResult = None
        global listadmin
        for st in admin.listadmin:
                if (st.Admin_ID == Admin_ID):
                    searchResult = st
        return searchResult