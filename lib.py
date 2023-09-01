from abc import ABC, abstractmethod

#-----------INHERITANCE--------------------
class Library:
    def __init__(self, name : str, ip : int):
        self.name = name 
        self.ip = ip
        
    def get_name(self):
        return self.name
    
    
class Book(Library):
    def __init__(self, name : str, ip : int, genre : str):
        super().__init__(name, ip)
        self.genre = genre
        
        
    def __str__(self):
        return f"Book name is {self.name} & its ID is {self.ip}:{self.genre} "
    
class User(Library):
    def __init__(self, name: str, ip: int, no_book : int):
        super().__init__(name, ip)
        self.no_book = no_book
        
    def __str__(self):
        return f"student with ID : {self.ip} issued {self.no_book} books."
    
    
#book = Book("murakami", 1227, "philosophy")
#print (book)

#user = User("jonh", 3087, 4)
#print (user)

#-------------ENCAPSULATION----------------------
class Rawfile:
    def __init__(self, name : str, title : str):
        self.__name = name #private
        self.title = title
        
    def get_name(self):
        return self.__name
    
    def display_info(self):
        print(f"{self.title} is a secret file 👀 🤫")
#        print(f"{self.title} by {self.name} is a secret file 👀 🤫")
#        print(f"{self.title} by {self.__name} is a secret file 👀 🤫")
#        print(f"{self.title} by {self.get_name()} is a secret file 👀 🤫")
        
    

file = Rawfile("jim", "S.C.Bose")
file.display_info()

#---------------ENCAPSULATION WITH INHERITANCE------------------
class Library:
    def __init__(self, name : str, ip : int):
        self.__name = name #private
        self.ip = ip
        
    def get_name(self):
        return self.__name
    
    
class Book(Library):
    def __init__(self, name : str, ip : int, genre : str):
        super().__init__(name, ip)
        self.genre = genre
        
        
    def __str__(self):
        return f"Book name is {self.get_name()} & its ID is {self.ip}:{self.genre} "
  
class User(Library):
    def __init__(self, name: str, ip: int, no_book : int):
        super().__init__(name, ip)
        self.no_book = no_book
        
    def __str__(self):
        return f"student with ID : {self.ip} issued {self.no_book} books."
    
    
    
#book = Book("murakami", 1227, "philosophy")
#print (book)

#user = User("jonh", 3087, 4)
#print (user)   

#-----------------ABSTRACTION WITH INHERITANCE------------------
class LibraryUser(ABC):
    def __init__(self, name, id):
        self.name = name
        self.id = id

    @abstractmethod
    def display_info(self):
        pass

class Student(LibraryUser):
    def __init__(self, name, id, no_book):
        super().__init__(name, id)
        self.no_book = no_book

    def display_info(self):
        print(f"Student: {self.name}")
        print(f"Student ID: {self.id}")
        print(f"Number of Books Issued: {self.no_book}")

class Staff(LibraryUser):
    def __init__(self, name, id, department):
        super().__init__(name, id)
        self.department = department

    def display_info(self):
        print(f"Staff Member: {self.name}")
        print(f"Staff ID: {self.id}")
        print(f"Department: {self.department}")

# Creating instances of library users
student = Student("Alice", "S123", 3)
staff = Staff("John", "T567", "Computer Science")

# Display user information
#student.display_info()
#staff.display_info()
#----------------POLTMORPHISM--------------it is used in class methods, where we can have multiple classes with the same method name.
class UG:
    def __init__(self, name):
        self.name = name
    def attendee(self):
        print("college attendee")
class PG:
    def __init__(self, name):
        self.name = name
    def attendee(self):
        print("college attendee")
class Dean: #<--------------------+
    def __init__(self, name):    #|
        self.name = name         #|
    def attendee(self):          #|
        print("collge attendee") #|
                                 #|
#create object                   #|
ug = UG("Manish")                #|
pg = PG("Rumi")                  #|
dean = Dean("B.k. Roy")#>---------+

#use loop to get the attendee status
for x in (pg, ug, dean):
    x.attendee()

#-----------------INHERITANCE CLASS POLYMORPHISM--------------What about chid classes with same name
class College:
    def __init__(self, name : str, card : str):
        self.name = name
        self.card = card
        
    def attendee(self):
        print(f"{self.name}, college attendee")
        
class Hostel(College): 
    def __init__(self, name : str, card : str):
        super().__init__(name, card) 
        
    def attendee(self):
        print(f"{self.name}, hostel attendee")
        
class Academic(College):
    def __init__(self, name : str, card : str):
        super().__init__(name, card) 
        
    def attendee(self):
        print(f"{self.name}, academic attendee")
        
class Mess(College): 
    def __init__(self, name : str, card : str):
        super().__init__(name, card) 
    
    def attendee(self):
        print(f"{self.name}, mess attendee")
 
#create object  
hostel = Hostel("sabbir", "yes")    
mess = Mess("Hmilson", "yes")
academic = Academic("debashmita", "no")

#cls_name.method(object)

for w in (hostel, mess, academic):
   w.attendee()
   print("card : " +w.card)

#here we pass data for output, from child afterretriving from parents(maybe due to "self"). Can we directly retrive from parent

#---------------COMPOSITION-------------
#these classes are part of car class.
class Engine:
    def start(self):
        print("Engine started")
        
    def stop(self):
        print("Engine stoped")
        
class Wheel:
    def inflat(self):
        print("wheels inflated")
    
    def deflat(self):
        print("wheel deflatted")
        
#using composition create car class
class Car:
    def __init__(self):
        self.engine = Engine()
        self.wheels = [Wheel() for _ in range(4)]
        
    def start(self):
        self.engine.start()
        
    def inflate_wheels(self):
        for wheel in self.wheels:
            wheel.inflat()

#create object            
my_car = Car()

#my_car.start()
#my_car.inflate_wheels()

