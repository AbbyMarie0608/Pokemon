'''
Author: Abby-Marie Tong
KUID: 3178667
Date: 4/16/2025
Lab: 8
Last Modified: 4/17/2025
Purpose: Creates a main that takes in a file and hands off the rest of the code

'''
from pokemon import PokemonTree
def main():
    file_name = input('Input a file: ')
    tree = PokemonTree()
    tree.read_file(file_name)
    tree.main()

if __name__ == "__main__":
    main()