# question1

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False  # Tracks books currently borrowed

    def mark_as_borrowed(self):
        """Marks the book as borrowed."""
        if not self.is_borrowed:
            self.is_borrowed = True
            return True
        return False

    def mark_as_returned(self):
        """Marks the book as returned."""
        if self.is_borrowed:
            self.is_borrowed = False
            return True
        return False

    def __str__(self):
        """String representation of a book."""
        status = "Borrowed" if self.is_borrowed else "Available"
        return f"'{self.title}' by {self.author} ({status})"


class LibraryMember:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []  # List to track borrowed books

    def borrow_book(self, book):
        """Attempts to borrow a book if it is available."""
        if book.mark_as_borrowed():
            self.borrowed_books.append(book)
            print(f"{self.name} borrowed '{book.title}'.")
        else:
            print(f"'{book.title}' is currently borrowed by someone else.")

    def return_book(self, book):
        """Returns a book if it is currently borrowed by the member."""
        if book in self.borrowed_books:
            if book.mark_as_returned():
                self.borrowed_books.remove(book)
                print(f"{self.name} returned '{book.title}'.")
            else:
                print(f"Error returning '{book.title}'.")
        else:
            print(f"{self.name} has not borrowed '{book.title}'.")

    def list_borrowed_books(self):
        """Lists all books currently borrowed by the member."""
        if self.borrowed_books:
            print(f"{self.name} has borrowed the following books:")
            for book in self.borrowed_books:
                print(f"  - {book}")
        else:
            print(f"{self.name} has no borrowed books.")

def main():    
    books = ["       
        Book("1984", "George Orwell"),
        Book("Pride and Prejudice", "Jane Austen"),
        Book("The Great Gatsby", "F. Scott Fitzgerald")
        Book("Atomic Habits", "James Clear")"
    ]

    member = LibraryMember(name="Alice", member_id="M001")

    while True:
        print("\nOptions:")
        print("1. List available books")
        print("2. Borrow a book")
        print("3. Return a book")
        print("4. List borrowed books")
        print("5. Quit")

        choice = input("Choose an option (1-5): ")

        if choice == "1":
            # List available books
            print("\nAvailable books:")
            for book in books:
                print(f"  - {book}")

        elif choice == "2":
            # Borrow a book
            book_title = input("Enter the title of the book to borrow: ")
            book_to_borrow = next((book for book in books if book.title == book_title), None)
            if book_to_borrow:
                member.borrow_book(book_to_borrow)
            else:
                print("Book not found.")

        elif choice == "3":
            # Return a book
            book_title = input("Enter the title of the book to return: ")
            book_to_return = next((book for book in books if book.title == book_title), None)
            if book_to_return:
                member.return_book(book_to_return)
            else:
                print("Book not found.")

        elif choice == "4":
            # List borrowed books
            member.list_borrowed_books()

        elif choice == "5":
            # Quit the program
            print("Exiting program.")
            break
        else:
            print("Invalid choice, please try again.")

main()