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
    
    
book = Book("murakami", 1227, "philosophy")
print (book)

user = User("jonh", 3087, 4)
print (user)
