class Book:
    def __init__(self, title, author, pages, pages_read):
        self.title = title
        self.author = author
        self.pages = pages
        self.pages_read = pages_read
    
    def get_summary(self):
        print(f"{self.title} by {self.author} has {self.pages} pages.")

    def read_pages(self):
        print(f"You have", self.pages-self.pages_read, "pages left in", self.title, ".")

    def finished_reading(self):
        if self.pages-self.pages_read <= 0:
            print(f"You have finished {self.title}.")


my_book = Book("Harry Potter and the Sorcerer's Stone", "J.K. Rowling", 223, 223)
my_book.get_summary()
my_book.read_pages()
my_book.finished_reading()