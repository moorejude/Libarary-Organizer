"""
Jude Litke
Class: CS 521 - Spring 2
Date: May 1, 2021
Term Project
This file includes my Library class that is utilized by my main program,
    and also includes the unit tests.
"""


class Library:
    language = "English"

    def __init__(self):
        self.books = []
        self.__reader = "Jude"
        self.a_book = "Paperback"

    def __str__(self):
        print("Here are all the books in {}'s library: ".format(self.__reader))
        print("=" * 40)
        for book in self.books:
            print("{}, Author: {}, Genre: {}, Pages: {}".format(
                    book.name, book.author, book.genre, book.pages))
        print("=" * 40)
        print("Books in Library: ", Library.amount_in_library(self))

    def __repr__(self):
        """Explains to user how to add a book to Library"""
        return print("Library.add_book(books('name', 'author', "
                     "'genre', 100, 0))")

    def add_book(self, book):
        """Adds a book to the Library class"""
        self.books.append(book)

    def delete_book(self, book):
        """Reserving this function for the future"""
        pass

    def search_book_genre_unread(self, genre):
        """Finds unread books in a specific genre"""
        book_by_genre = []
        for book in self.books:
            if book.genre == genre:
                if book.year == 0:
                    book_by_genre.append(book)
        if len(book_by_genre) == 0:
            return print("Sorry, there are no unread books in that genre.")
        else:
            return Library.__catalogue_name_author(book_by_genre)

    def books_in_year(self, year):
        """Finds the amount of books read in a year"""
        book_by_year = []
        for book in self.books:
            if book.year == year:
                book_by_year.append(book)
        if len(book_by_year) == 0:
            return print("Sorry, could not find any books read in that year.")
        else:
            return Library.__catalogue_name_author_pages(book_by_year)

    def search_book_author(self, author):
        """Finds a book by author"""
        written_by_author = []
        for book in self.books:
            if book.author == author:
                written_by_author.append(book)
        if len(written_by_author) == 0:
            return print("Sorry, could not find that author."), None
        else:
            return Library.__catalogue_name_author(written_by_author)

    @staticmethod
    def __catalogue_name_author(a_tuple):
        """Utilized privately by the class, prints out the tuples properly"""
        for book in a_tuple:
            print("{}, by {}".format(book.name, book.author))

    @staticmethod
    def __catalogue_name_author_pages(a_tuple):
        """Utilized privately by the class, prints out the tuples properly"""
        for book in a_tuple:
            print("{}, by {}: {} pages".format(book.name, book.author,
                                               book.pages))

    def __add__(self, year):
        """This adds all of the pages read in the year that is given"""
        book_pages_list = []
        total = 0
        for book in self.books:
            if book.year == year:
                book_pages_list.append(book.pages)
        for ele in range(0, len(book_pages_list)):
            total = total + book_pages_list[ele]
        return total

    def amount_in_library(self):
        """Counts the amount of books in the Library"""
        return len(self.books)

    def book_types(self):
        """Returns the types of books in a class"""
        return self.a_book

    def book_reader(self):
        """Returns the reader of the books in the Library."""
        return self.__reader

    def book_list(self):
        """Returns the books in the Library as lists. Used this to test that
        Library.add_book actually works as intended."""
        return self.books

    def get_genre_test(self, genre):
        """Returns all the books in the Library with same genre as a List. Used
        this to test that Library.get_book_genre_unread works as intended."""
        book_by_genre = []
        for book in self.books:
            if book.genre == genre:
                if book.year == 0:
                    book_by_genre.append(book)
        if len(book_by_genre) == 0:
            return None
        else:
            return book_by_genre

    def books_year_test(self, year):
        """Returns all the books in the Library with the same year as a List.
        Used to check that Library.books_in_year works as intended."""
        book_by_year = []
        for book in self.books:
            if book.year == year:
                book_by_year.append(book)
        if len(book_by_year) == 0:
            return None
        else:
            return book_by_year

    def books_by_author_test(self, author):
        """Returns all the books in the Library with the same author as a List.
        Used to check that Library.search_book_author works as intended."""
        written_by_author = []
        for book in self.books:
            if book.author == author:
                written_by_author.append(book)
        if len(written_by_author) == 0:
            return None
        else:
            return written_by_author
