class book:
    def __init__(self, id_book, name, author,editorial):
        self.id_book=id_book
        self.name=name
        self.author=author
        self.editorial=editorial
        self.available=True

    def show_books_info(self):
        return f"{self.id_book}-{self.name}-{self.author}"