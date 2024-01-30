from menu import Menu

"""
@author:  Andrew Anca
@version: 1.0.0
@date:    2024-01-29
"""

"""This module houses the driver to begin the app"""


def main():
    """Instantiates a CLI object to display the menu to the user"""
    my_epic_app = Menu()

    my_epic_app.display_menu()


if __name__ == '__main__':
    main()
