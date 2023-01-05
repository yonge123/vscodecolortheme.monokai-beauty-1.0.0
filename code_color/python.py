import os
import re

"""
a python sample code

"""


class User():
    def __init__(self, first_name, last_name, email, phone):
        """
        :param first_name str:
        :param last_name str:
        :param email str:
        :param phone str:
        """
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone


def main():
    user1 = User("jack", "Sparrow", "123@email.com", "000-12345678")
    print(user1.first_name)
    print(user1.last_name)
    print(user1.email)
    print(user1.phone)
    
    
if __name__ == '__main__':
    main()
    
    
    
    