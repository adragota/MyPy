from file_finder import FileFinder

"""
@author: Andrew Anca
"""

"""This module houses the menu"""


class Menu:
    """
    Represents a "Menu" object
    """

    def __init__(self):
        self._file_finder = FileFinder()

    # METHODS

    def display_menu(self):
        """Displays the menu"""

        user_input  = None

        while user_input != 4:
            print("\nWelcome to MyPy\n")
            print("1. Show .py files in current directory")
            print("2. Show .py files in parent directory")
            print("3. Quit")

            string_input = input("Please enter your choice (1-3)\n")

            user_input = int(string_input)

            if user_input == 1:
                current_dir = self._file_finder.get_current_directory()
                self._file_finder.print_files(current_dir)

            elif user_input == 2:
                current_dir = self._file_finder.get_current_directory()
                parent_dir = self._file_finder.get_parent_directory(current_dir)
                self._file_finder.print_files(parent_dir)

            elif user_input == 3:
                break
        else:
            print("Could not process the input. Please enter a number from 1 - 3.")

        # only executed after user quits cli
        print("Thank you for using Formatter!!!")
