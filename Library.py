class DigitalLibrary:
    def __init__(self):
        self.books = {}

    def add_book(self, title, author, publication_year):
        book_id = len(self.books) + 1
        self.books[book_id] = {
            'title': title,
            'author': author,
            'publication_year': publication_year
        }
        print(f"Book with ID {book_id} added to the library.")

    def get_book(self, book_id):
        return self.books.get(book_id)

    def search_books_by_title(self, title):
        found_books = []
        for book_id, book_info in self.books.items():
            if title.lower() in book_info['title'].lower():
                found_books.append((book_id, book_info))
        return found_books

    def search_books_by_author(self, author):
        found_books = []
        for book_id, book_info in self.books.items():
            if author.lower() in book_info['author'].lower():
                found_books.append((book_id, book_info))
        return found_books

    def display_all_books(self):
        print("All books in the library:")
        for book_id, book_info in self.books.items():
            print(f"Book ID: {book_id}")
            print(f"Title: {book_info['title']}")
            print(f"Author: {book_info['author']}")
            print(f"Publication Year: {book_info['publication_year']}")
            print('-' * 30)

if __name__ == "__main__":
    library = DigitalLibrary()

    # Adding some books to the library
    library.add_book("Python Crash Course", "Eric Matthes", 2019)
    library.add_book("Automate the Boring Stuff with Python", "Al Sweigart", 2015)
    library.add_book("Fluent Python", "Luciano Ramalho", 2015)

    # Display all books in the library
    library.display_all_books()

    # Search books by title
    search_title = "Python"
    found_books_by_title = library.search_books_by_title(search_title)
    if found_books_by_title:
        print(f"Found books matching '{search_title}':")
        for book_id, book_info in found_books_by_title:
            print(f"Book ID: {book_id}")
            print(f"Title: {book_info['title']}")
            print(f"Author: {book_info['author']}")
            print(f"Publication Year: {book_info['publication_year']}")
            print('-' * 30)
    else:
        print(f"No books found with the title '{search_title}'.")

    # Search books by author
    search_author = "Eric Matthes"
    found_books_by_author = library.search_books_by_author(search_author)
    if found_books_by_author:
        print(f"Found books written by '{search_author}':")
        for book_id, book_info in found_books_by_author:
            print(f"Book ID: {book_id}")
            print(f"Title: {book_info['title']}")
            print(f"Author: {book_info['author']}")
            print(f"Publication Year: {book_info['publication_year']}")
            print('-' * 30)
    else:
        print(f"No books found written by '{search_author}'.")
