class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def book_info(self):
        return f"{self.title} {self.author} {self.pages}"

    def read_pages(self, noOfPages):
        return f"You have read {noOfPages} pages."

my_books = Book("Dark Side", "Sid", "121")
print(my_books.book_info())
print(my_books.read_pages(45))