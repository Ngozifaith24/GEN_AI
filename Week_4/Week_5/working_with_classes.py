# class Student:
#     def __init__(self, name, course, level):  # This runs automatically
#         print("Creating a new student...")
#         self.name = name
#         self.course = course
#         self.level = level
#         print(f"Student {name} has been created!")

# ngozi = Student("Omuekwu Ngozi", "Ai developer", 100)
# print(ngozi.name)
# print(ngozi.course)
# print(ngozi.level)

# #How init and self work Together
# class NigerianStudent:
#     def __init__(self, name, state, course):
#         print(f"Step 1: Creating student object...")
#         self.name = name           # Step 2: Assign name to THIS object
#         self.state_of_origin = state    # Step 3: Assign state to THIS object
#         self.course = course       # Step 4: Assign course to THIS object
#         self.student_id = self.generate_id()  # Step 5: Generate ID for THIS object
#         print(f"Step 6: {self.name} from {self.state_of_origin} is ready!")
    
#     def generate_id(self):
#         import random
#         return f"CONVEBIO{random.randint(1000, 9999)}"

# ngozi = NigerianStudent("Omuekwu Ngozi", "Delta","genetics")
# print(ngozi.name)
# print(ngozi.course)
# print(ngozi.state_of_origin)
# print(ngozi.student_id)


# #more examples
# class PhoneUser:
#     def __init__(self, name, network):
#         self.name = name
#         self.network = network
#         self.airtime = 0
#         print(f"{self.name} joined {self.network} network")
    
#     def buy_airtime(self, amount):
#         self.airtime += amount  # self ensures it goes to the RIGHT person
#         return f"{self.name} now has ₦{self.airtime} airtime"


# # Creating multiple users
# ngozi = PhoneUser("Omuekwu ngozi", "MTN")     
# faith = PhoneUser("Omuekwu faith", "Airtel")  

# print(ngozi.name)
# print(ngozi.network)

# print(faith.name)
# print(faith.network)



# # Each person's actions affect only their own account
# print(ngozi.buy_airtime(500))     # Ngozi now has ₦500 airtime
# print(faith.buy_airtime(1000)) # Faith now has ₦1000 airtime
# print(ngozi.airtime)              # 500 (Ngozi's airtime unchanged)
# print(faith.airtime)           # 1000 (faith's airtime unchanged)

# Defining Attributes of a student
class Student:
    def __init__(self, name, course, level, state_of_origin, cgpa, university):
        self.name = name                   
        self.course = course              
        self.level = level                
        self.state_of_origin = state_of_origin  
        self.cgpa = cgpa  
        self.university = university

# Creating a student object
Ngozi = Student("Ngozi faith omuekwu", "Microbiology", 700, "Ogun State", 4.93, "Federal University oye-ekiti")


# Accessing attributes
print("Name: " + Ngozi.name)             
print(f"Course: {Ngozi.course}")        
print("State: ", Ngozi.state_of_origin)  
print(f"CGPA: {Ngozi.cgpa}")


# Instance Attribute
student1 = Student("Anthony Johnson", "Engineering", 200, "Ogun", 4.63, "Federal University oye-ekiti")
student2 = Student("Fadilat Hassan", "Medicine", 400, "Lagos", 4.99, "Federal University oye-ekiti")

print(student1.name)  
print(student2.name) 

class Student:
    university = "Federal University oye-ekiti"  
    
    def __init__(self, name, course):
        self.name = name         
        self.course = course
        

print(Student.university)     
print(student1.university)   
print(student2.university)  


#Methods
class Student:
    def __init__(self, name, course, level, university):
        # Attributes
        self.name = name
        self.course = course
        self.level = level
        self.university = university
        self.cgpa = 0.0
        self.fees_paid = False
    

     # Method: action the student can do
    def pay_school_fees(self):                   
        self.fees_paid = True
        return f"{self.name} has paid school fees for {self.level} level"
    
    # Method: another action
    def register_courses(self):                   
        if self.fees_paid:
            return f"{self.name} has registered courses for {self.course}"
        else:
            return f"{self.name} must pay school fees first!"
    
      # Method: calculates CGPA
    def calculate_cgpa(self, grades):           
        if grades:
            self.cgpa = sum(grades) / len(grades)
            return f"{self.name}'s CGPA is now {self.cgpa:.2f}"
        return "No grades provided"
   # @classmethod
    def get_university(cls):
        return cls.university
#@staticmethod
    def academic_calendar():
        return "Academic session runs from September to July"

# Using methods
Abiodun = Student("Abiodun Akinola", "Gistology", 600, "Federal University oye ekiti")
print(Abiodun.pay_school_fees())        
print(Abiodun.register_courses())   
print(Abiodun.get_university())    
print(Abiodun.calculate_cgpa([4.8, 4.8, 4.6, 4.5])) 

#Methods: Instance
# 'self' refers to the specific student
def pay_school_fees(self):  
    return f"{self.name} has paid school fees"

class BankAccount:
    def __init__(self, owner, bank_name, balance=0):
        # ATTRIBUTES - What the account HAS
        self.owner = owner
        self.bank_name = bank_name
        self.balance = balance
        self.account_number = self.generate_account_number()
    
    # METHODS - What the account can DO
    def deposit(self, amount):
        """Add money to the account"""
        if amount > 0:
            self.balance += amount  # Method changes attribute
            return f"₦{amount:,} deposited to {self.owner}'s {self.bank_name} account. New balance: ₦{self.balance:,}"
        return "Invalid deposit amount"
    
    def withdraw(self, amount):
        """Remove money from the account"""
        if amount > 0 and amount <= self.balance:
            self.balance -= amount  # Method changes attribute
            return f"₦{amount:,} withdrawn from {self.owner}'s account. New balance: ₦{self.balance:,}"
        return "Insufficient funds or invalid amount"
    
    def transfer(self, amount, recipient):
        """Transfer money to another account"""
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            return f"₦{amount:,} transferred from {self.owner} to {recipient}. Remaining balance: ₦{self.balance:,}"
        return "Transfer failed: Insufficient funds"
    
    def check_balance(self):
        """Check current balance"""
        return f"{self.owner}'s {self.bank_name} account balance: ₦{self.balance:,}"
    
    def generate_account_number(self):
        """Generate a unique account number"""
        import random
        return f"01{random.randint(10000000, 99999999)}"
    
    # Creating and using the account
Ngozi_account = BankAccount("Ngozi Faith", "First Bank", 5000000000000)

# Attributes (characteristics)
print(f"Owner: {Ngozi_account.owner}")
print(f"Bank: {Ngozi_account.bank_name}")
print(f"Account Number: {Ngozi_account.account_number}")



# Methods (actions)
print(Ngozi_account.deposit(25000))    
print(Ngozi_account.withdraw(10000))  
print(Ngozi_account.transfer(15000, "Sunday James"))  
print(Ngozi_account.check_balance())   

class NaijaPhone:
    def __init__(self, brand, model, network_provider):
        self.brand = brand
        self.model = model
        self.network_provider = network_provider
        self.airtime_balance = 0
        self.data_balance = 0
        self.is_on = False
    
    def power_on(self):
        self.is_on = True
        return f"{self.brand} phone is now on. Network: {self.network_provider}"
    
    def buy_airtime(self, amount):
        self.airtime_balance += amount
        return f"₦{amount} airtime purchased. Balance: ₦{self.airtime_balance}"
    
    def make_call(self, number):
        if self.is_on and self.airtime_balance > 0:
            self.airtime_balance -= 10
            return f"Calling {number}... Remaining airtime: ₦{self.airtime_balance}"
        return "Cannot make call. Check phone power and airtime balance"
    
    def send_sms(self, message, number):
        if self.airtime_balance >= 4:
            self.airtime_balance -= 4
            return f"SMS sent to {number}: '{message}'. Remaining airtime: ₦{self.airtime_balance}"
        return "Insufficient airtime to send SMS"
    
ng = NaijaPhone("iphone", "iphone 20 pro", "Airtel")
print(ng.brand)
print(ng.model)
print(ng.network_provider)