'''
Author: Abby-Marie Tong
KUID: 3178667
Date: 4/16/2025
Lab: 8
Last Modified: 4/18/2025
Purpose: Creates a class that holds the pokemon's information

'''

class Pokeball:
    def __init__(self, name, number, jpn_name):
        '''Initializes all the information and packs it into a pokeball (basically)'''
        self.name = name
        self.number = number
        self.jpn_name = jpn_name

    def __lt__(self, other):
        '''Less than method that lets it compare to other pokeballs or just ints'''
        if isinstance(other, Pokeball):
            return self.number < other.number
        elif isinstance(other, int):
            return self.number < other
        else:
            return False
    
    def __eq__(self, other):
        '''Equal to method that lets it compare to other pokeballs or just ints'''
        if isinstance(other, Pokeball):
            return self.number == other.number
        elif isinstance(other, int):
            return self.number == other
        else:
            return False
        
    def __str__(self):
        '''Returns a well formatted string'''
        return f'American Name: {self.name}, ID: {self.number}, JPN Name: {self.jpn_name}'
