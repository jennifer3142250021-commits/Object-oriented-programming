from books import book
from users import user
from library import library

library1=library()

book1=book("001","python for dumies","jennifer","villareal")
book2=book("002","OOP fundamental","Ana Sanchez","E.A")
user1=user("001","jennifer peña")

library1.add_book(book1)
library1.add_book(book2)
library1.add_user(user1)
library1.show_books()
library1.borrow_book("001", "001")
library1.borrow_book("001", "001")
library1.return_book("001")
library1.borrow_book("001", "001")
