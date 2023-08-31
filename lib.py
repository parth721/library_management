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
student.display_info()
staff.display_info()
