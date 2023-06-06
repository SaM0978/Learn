class Library:
    def __init__(self):
        self.no_of_books = 0
        self.books = []

    def print_all_books(self):
        if self.no_of_books == 0:
            print("There are no books in the library.")
        else:
            print("All books in the library:")
            for book in self.books:
                print(book)

    def add_book(self, book):
        self.books.append(book)
        self.no_of_books += 1
        print(f"Added book: {book}")

    def get_no_of_books(self):
        return self.no_of_books


A = Library()

A.add_book("Sam's Journey")

A.add_book("Hussain's Journey")

print(A.get_no_of_books())

print(A.print_all_books())





