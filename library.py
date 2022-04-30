from os import remove


class library:
    def __init__(self,books):
        self.books=books
        
    def listbook(self):
        print('Availble books are ')
        for book in self.books:
            print(book)
    
    def borrow_book(self,borrowbook):
        if borrowbook in self.books:
            print('Book is avilable')
            print('Get it now')
            self.books.remove(borrowbook)

    def recieved(self,received_book):
        print('You have returned the book')
        self.books.append(received_book)

books=['c','c++','java']
o=library(books)
msg="""
     1. Display books
     2. Borrow books
     3. Return book
    """
while True:
 print(msg)
 ch=int(input('Enter your choice : '))
 if ch==1:
     o.listbook()

 elif ch==2:
     book=input('Enter the book you want : ')
     o.borrow_book(book)

 elif ch==3:
     book=input('enter the book you return : ')
     o.recieved(book)
 
 else:
     print('You entered a wrong value')

     quit()




