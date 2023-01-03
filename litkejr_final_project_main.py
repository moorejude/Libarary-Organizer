"""
Jude Litke
Class: CS 521 - Spring 2
Date: May 1, 2021
Term Project
This program takes tuples of books and adds them to a Library class. The Library
    class organizes the books and performs various functions depending on what
    the user wants to use the catalogue for.
"""

import sys
from collections import namedtuple
from litkejr_library_class import Library

# START is for the while loops within the program, and there are empty lists
# for functions to fill with data. input_str is used a lot, so it is global.
START = True
book_types = []
key_words = []
input_str = "Input Here: "


def read_genre_data():
    """
    Once initialized, it opens a text file and reads through it and appends
    data to lists book_types and key_words.
    Param: none
    Return: none
    """
    data_source = "GenreData.txt"
    file = open(data_source, "r")
    line_read = file.readline().rstrip()
    while line_read != '':
        index_of_key = line_read.index("for")
        dataset = line_read[index_of_key + 4:]
        book_types.append(dataset)
        line_read = file.readline().rstrip()
        datalist = line_read.split(" ")
        key_words.append(datalist)
        line_read = file.readline().rstrip()
    file.close()


def find_key_words(a_user_input):
    """
    This function takes a string input from a user, and finds key words in the
    user input that fall into a specific category.
    Param: a string input(from a user)
    Return: A set with the key words.
    """
    read_genre_data()
    empty_set = set()
    index = 0
    for items in key_words:
        for word in items:
            if word in a_user_input.lower():
                empty_set.add(index)
                break
        index += 1
    return empty_set


def find_the_genre(a_set):
    """
    This function takes a set, and then finds the corresponding book type in
    the list book_types according to the list index.
    Param: A set
    Return: corresponding index in book_types
    """
    for i in range(len(key_words)):
        if i in a_set:
            return book_types[i]


# This is all of my current book data for my Library class. My next steps on
# improving this library cataloguing system would be to move all of this
# data into a text file, and work on the user being able to modify the text file
# with data by adding or deleting books. For now, all the book data is being
# stored here.
books = namedtuple('Book', 'name author genre pages year')
Library = Library()
Library.add_book(books('Stay Gold', 'McSmith', 'Romance', 368, 0))
Library.add_book(books('The Black Prism', 'Brent Weeks', 'Fantasy', 640, 0))
Library.add_book(books('Woven in Moonlight', 'Isabel Ibanez', 'Romance',
                       400, 0))
Library.add_book(books('The Inexplicable Logic of my Life',
                       'Benjamin Alire Saenz', "Romance", 464, 0))
Library.add_book(books('The Companions', 'Katie M. Flynn', 'Science Fiction',
                       272, 0))
Library.add_book(books('Iron Master', 'Jennifer Ashley', 'Romance', 266, 0))
Library.add_book(books('Cold Magic', 'Kate Elliot', 'Fantasy', 614, 0))
Library.add_book(books('The Lies of Locke Lamora', 'Scott Lynch',
                       'Fantasy', 499, 0))
Library.add_book(books('Daughter of Joy', 'Kathleen Morgan', 'Romance', 324,
                       2016))
Library.add_book(books('Mate Bond', 'Jennifer Ashley', 'Romance', 300, 2016))
Library.add_book(books('Touched by an Alien', 'Gini Koch', 'Science Fiction',
                       389, 2016))
Library.add_book(books('Alien Tango', 'Gini Koch', 'Science Fiction', 428,
                       2016))
Library.add_book(books('Alien Diplomacy', 'Gini Koch', 'Science Fiction', 425,
                       2016))
Library.add_book(books('Hawksong', 'Amelia Atwater-Rhodes', 'Fantasy', 243,
                       2016))
Library.add_book((books('Snakecharm', 'Amelia Atwater-Rhodes', 'Fantasy', 166,
                        2016)))
Library.add_book(books('Lady Midnight', 'Cassandra Clare', 'Fantasy', 668,
                       2017))
Library.add_book(books('The Clockwork Prince', 'Cassandra Clare', 'Fantasy',
                       502, 2017))
Library.add_book(books('The Clockwork Angel', 'Cassandra Clare', 'Fantasy', 497,
                       2017))
Library.add_book(books('The Clockwork Princess', 'Cassandra Clare', 'Fantasy',
                       609, 2017))
Library.add_book(books('Ready Player One', 'Ernest Cline', 'Science Fiction',
                       374, 2018))
Library.add_book(books('Call Me By Your Name', 'Andre Aciman', 'Romance',
                       256, 2018))
Library.add_book(books('Furies of Calderon', 'Jim Butcher', 'Fantasy', 440,
                       2018))
Library.add_book(books('Academs Fury', 'Jim Butcher', 'Fantasy', 480, 2018))
Library.add_book(books('Carry On', 'Rainbow Rowell', 'Romance', 528, 2018))
Library.add_book(books('What if its Us', 'Becky Albertalli', 'Romance',
                       448, 2019))
Library.add_book(books('Artemis', 'Andy Weir', 'Science Fiction', 309, 2019))
Library.add_book(books('The Cruel Prince', 'Holly Black', 'Fantasy', 416, 2019))
Library.add_book(books('The Wicked King', 'Holly Black', 'Fantasy', 368, 2019))
Library.add_book(books('Starless', 'Jacqueline Carey', 'Fantasy', 592, 2019))
Library.add_book(books('The Name of the Wind', 'Patrick Rothfuss', 'Fantasy',
                       662, 2019))
Library.add_book(books('The Wise Mans Fear', 'Patrick Rothfuss', 'Fantasy',
                       994, 2019))
Library.add_book(books('The Queen of Nothing', 'Holly Black', 'Fantasy', 336,
                       2020))
Library.add_book(books('The Sound of Stars', 'Alechia Dow', 'Science Fiction',
                       432, 2020))

# 1. Greeting: First, the user of the Library catalogue is greeted. Since this
# is all of my own book data, it is greeting me.
print("Welcome, to your Book Organizer.")

# 2. Start the while loop.
while START is True:
    try:
        # 3. User options: The user has multiple options. If the user does not
        # type in a number, an exception is caught and it loops back through.
        print("Please read the options carefully and then input a number.")
        print("     (1) Find a new book to read by genre \n"
              "     (2) Find a book by author \n"
              "     (3) See a list of books you have read in a year\n"
              "     (4) See a list of all the books in your library\n")
        user_input = int(input(input_str))
        if user_input == 1:
            # 4. User input for the first option is any string. The string is
            # then checked for key words, and the program finds a genre that
            # is associated with those words. If there are no key words, it
            # lists all the categories to chose from. If the user still does
            # not input something, they are sent to the top of the while loop
            # to try again. This part of the program suggests books in a given
            # genre that the user has not read yet.
            print("Please write a short sentence about what kind of book"
                  " you would like to read: ")
            user_input2 = input(input_str)
            found_words = find_key_words(user_input2)
            if len(found_words) > 0:
                find_genre = find_the_genre(found_words)
                print("\nHere are a list of books that you have not read in "
                      "the {} genre: \n".format(find_genre))
                Library.search_book_genre_unread(find_genre)
                break
            else:
                print("Sorry, I could not recommend a book genre for you "
                      "based on your input. Here is a list of genres that "
                      "I have: ")
                for item in book_types:
                    print(item)
                print("What category interests you?")
                user_input3 = input(input_str)
                found_words = find_key_words(user_input3)
                find_genre = find_the_genre(found_words)
                if len(find_genre) > 0:
                    print(
                        "Here are a list of books that you haven not read in "
                        "the {} genre: ".format(find_genre))
                    Library.search_book_genre_unread(find_genre)
                    break
                else:
                    print("Sorry, I still couldn't get that. Please try again!")
                    continue
        elif user_input == 2:
            # 5. If the user wants to find a book by author, the program will
            # loop and allow them to type in as many inputs as they want. The
            # program won't catch if the user has inputted a name incorrectly,
            # but will give them as many chances as they want.
            while START is True:
                print("Please input the name of the author that you would "
                      "like to find: (Remember to capitalize the name, and"
                      " any first and last names with a space!)")
                user_input5 = input(input_str)
                Library.search_book_author(user_input5)
                print("Would you like to search again? [Y/N] ")
                validate_search = input(input_str)
                if validate_search.lower() == "yes" \
                        or validate_search.lower() == "y":
                    continue
                elif validate_search.lower() == "no" \
                        or validate_search.lower() == "n":
                    sys.exit()
                else:
                    "Sorry, I didn't understand that input. Please run the " \
                        "program again."
                    sys.exit()
        elif user_input == 3:
            # 6. For this option, the user will get a chance to input a year.
            # It is another while loop, and the program checks to make sure the
            # input is numeric, 4 numbers long, and if it is between the years
            # suggested. Once a year is accepted, it prints out all the data
            # derived from that year, like all the books read and pages read.
            print("Please input a year between 2016 and 2020: ")
            while START is True:
                user_input4 = input(input_str)
                if user_input4.isnumeric():
                    if len(user_input4) == 4:
                        if 2021 > int(user_input4) > 2015:
                            print("=" * 40)
                            print("Books read in {}:".format(user_input4))
                            Library.books_in_year(int(user_input4))
                            print("\nPages read in {}:".format(user_input4),
                                  Library.__add__(int(user_input4)))
                            print("=" * 40)
                            sys.exit()
                        else:
                            print("Error: That is not between 2016 and 2020."
                                  " Please try again.")
                            continue
                    else:
                        print("Error: That is not the correct amount of numbers"
                              "for a year. Please try again.")
                        continue
                else:
                    print("Error: that is not a number. Please try again.")
                    continue
        elif user_input == 4:
            # 7. Lastly, this outputs all the books in the Library, and the
            # amount of books in the Library class.
            Library.__str__()
            sys.exit()
        else:
            print("Error: That is not an option listed. Please try again!\n")
            continue
    except ValueError:
        print("Error: That is not a number. Please try again! \n")
        continue
