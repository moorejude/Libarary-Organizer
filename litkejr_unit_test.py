"""
Jude Litke
Class: CS 521 - Spring 2
Date: May 1, 2021
Term Project
This file includes my Library class unit tests.
"""

from collections import namedtuple
from litkejr_library_class import Library

# Used this information to test that the Library class works as intended.
books = namedtuple('Book', 'name author genre pages year')
Library = Library()
Library.add_book(books('name', 'author', 'genre', 100, 0))


def test_amount_in_library():
    assert Library.amount_in_library() == 1, \
        "amount_in_library should return 1"


def test_book_reader():
    assert Library.book_reader() == "Jude", \
        "book_reader should return 'Jude'"


def test_book_types():
    assert Library.book_types() == "Paperback", \
        "book_types should return 'Paperback'"


def test_book_list():
    assert Library.book_list() == [('name', 'author',
                                    'genre', 100, 0)], \
        "book_list should return [('name', 'author','genre', 100, 0)]"


def test_add():
    assert Library.__add__(0) == 100, \
        "__add__ should return 100"


def test_search_book_genre_undread():
    assert Library.get_genre_test('genre') == [('name', 'author',
                                                'genre', 100, 0)], \
        "search_book_genre should return all the books with the same genre"


def test_books_in_year():
    assert Library.books_year_test(0) == [('name', 'author',
                                           'genre', 100, 0)], \
        "books_in_year should return all the books with the same year"


def test_search_book_author():
    assert Library.books_by_author_test('author') == [('name', 'author',
                                                       'genre', 100, 0)], \
        "search_book_author should return all the books with the same author"


if __name__ == "__main__":
    test_amount_in_library()
    test_book_reader()
    test_book_types()
    test_book_list()
    test_add()
    test_search_book_genre_undread()
    test_books_in_year()
    test_search_book_author()

    print("Passed all unit tests.")
