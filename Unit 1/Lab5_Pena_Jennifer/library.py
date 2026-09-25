class library:
    def __init__(self):
        self.books=[]
        self.user=[]

    def add_book(self, book):
        self.books.append(book)

    def add_user(self,user):
        self.user.append(user)

    def show_books(self):
        for book in self.books:
            print(book.show_books_info())
            
    def borrow_book(self, id_book, id_user):
        for book in self.books:
            if book.id_book == id_book:
                if book.available:
                    book.available = False
                    print("Book borrowed successfully.")
                else:
                    print("The book is already borrowed.")

    def return_book(self, id_book):
        for book in self.books:
            if book.id_book == id_book:
                book.available = True
                print("Book returned successfully.")