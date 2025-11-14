'''
Author: Abby-Marie Tong
KUID: 3178667
Date: 4/16/2025
Lab: 8
Last Modified: 4/22/2025
Purpose: Creates a Pokemon Executive

'''
from bst import BinarySearchTree
from pokeball import Pokeball

class PokemonTree:
    def __init__(self):
        '''Initializes the trees'''
        self.pokemontree = BinarySearchTree()
        self.possible_copy = None

    def read_file(self, file):
        '''Goes through the file and strips and splits each line'''
        self.file_read = open(f'{file}', 'r')
        for line in self.file_read:
            line = line.strip()
            line = line.split('\t')
            pokeball = Pokeball(line[0], int(line[1]), line[2])
            self.pokemontree.add(pokeball)
        self.file_read.close()
    
    def add(self, tree, name, number, jpn_name):
        '''Creates a pokeball class of the given information then adds it using the bst method'''
        if tree == 'Copy':
            pokeball = Pokeball(name, int(number), jpn_name)
            self.possible_copy.add(pokeball)
        else:
            pokeball = Pokeball(name, int(number), jpn_name)
            self.pokemontree.add(pokeball)

    def copy_tree(self):
        '''Makes the tree for the copy and goes in order through current tree and passes off to collect_pokeball method'''
        self.possible_copy = BinarySearchTree()
        self.pokemontree.inorder(self.collect_pokeball)

    def collect_pokeball(self, pokeball):
        '''Takes each pokeball and packs them into a node in copied tree and adds each one'''
        self.possible_copy.add(pokeball)

    def print_prompt(self,tree, traversal_order):
        '''Prompts the user to put in a specific prompt they want printed out then hands it off to the BST class'''
        if tree == 'copy':
            if traversal_order.lower() == 'pre':
                self.possible_copy.preorder(self.possible_copy.visit_function)
            elif traversal_order.lower() == 'in':
                self.possible_copy.inorder(self.possible_copy.visit_function)
            elif traversal_order.lower() == 'post':
                self.possible_copy.postorder(self.possible_copy.visit_function)
            else:
                print('Invalid Traversal Order')
        else: 
            if traversal_order.lower() == 'pre':
                self.pokemontree.preorder(self.pokemontree.visit_function)
            elif traversal_order.lower() == 'in':
                self.pokemontree.inorder(self.pokemontree.visit_function)
            elif traversal_order.lower() == 'post':
                self.pokemontree.postorder(self.pokemontree.visit_function)
            else:
                print('Invalid Traversal Order')
    
    def main(self):
        '''Prints out a specific menu for the user then has them make a choice and hands off to other functions'''
        choice = 0
        while choice != 6:
            if self.possible_copy is None:
                print('\n1) Add \n2) Search\n3) Print\n4) Remove \n5) Copy \n6) Quit')
                try:
                    choice = int(input('Choice: '))
                except ValueError:
                    print('Please type in the number for one of the choices')
                if choice == 1:
                    name = input('What is the American Name of the pokemon?: ')
                    number = int(input('What is the pokemon ID?: '))
                    jpn_name = input('What is the Japanese name of the pokemon?: ')
                    self.add('pokemontree', name, number, jpn_name)

                elif choice == 2:
                    search = int(input('Which ID would you like to search for?: '))
                    print(self.pokemontree.search(search))
                

                elif choice == 3:
                    order = input('Traversal Order (Pre, In, Post): ')
                    self.print_prompt('pokemontree', order)
                
                elif choice == 4:
                    remove = int(input('What is the ID of the pokemon you want to remove?: '))
                    self.pokemontree.remove(remove)
                
                elif choice == 5:
                    self.copy_tree()

                elif choice == 6:
                    exit()

                else:
                    print('Choose a valid option')
            else:
                print('\n1) Add\n2) Print\n3) Remove \n4) Copy \n5) Quit')
                try:
                    choice = int(input('Choice: '))
                except ValueError:
                    print('Please type in the number for one of the choices')
                if choice == 1:
                    which = input('Would you like to edit the normal or copy binary tree?: ').lower()
                    if which == 'copy':
                        name = input('What is the American Name of the pokemon?: ')
                        number = int(input('What is the pokemon ID?: '))
                        jpn_name = input('What is the Japanese name of the pokemon?: ')
                        self.add('Copy', name, number, jpn_name)
                    elif which == 'normal':
                        name = input('What is the American Name of the pokemon?: ')
                        number = int(input('What is the pokemon ID?: '))
                        jpn_name = input('What is the Japanese name of the pokemon?: ')
                        self.add('pokemontree', name, number, jpn_name)
                    else:
                        print('Choose copy or normal')
                
                elif choice == 2:
                    which = input('Would you like to edit the normal or copy binary tree?: ').lower()
                    if which == 'copy':
                        search = int(input('Which ID would you like to search for?: '))
                        print(self.possible_copy.search(search))
                    elif which == 'normal':
                        search = int(input('Which ID would you like to search for?: '))
                        print(self.pokemontree.search(search))
                    else:
                        print('Choose copy or normal')

                elif choice == 3:
                    which = input('Would you like to edit the normal or copy binary tree?: ').lower()
                    if which == 'copy':
                        order = input('Traversal Order (Pre, In, Post): ')
                        self.print_prompt('copy', order)
                    elif which == 'normal':
                        order = input('Traversal Order (Pre, In, Post): ')
                        self.print_prompt('pokemonetree', order)
                    else:
                        print('Choose copy or normal')
                
                elif choice == 4:
                    which = input('Would you like to edit the normal or copy binary tree?: ').lower()
                    if which == 'copy':
                        remove = int(input('What is the ID of the pokemon you want to remove?: '))
                        self.possible_copy.remove(remove)
                    elif which == 'normal':
                        remove = int(input('What is the ID of the pokemon you want to remove?: '))
                        self.pokemontree.remove(remove)
                    else:
                        print('Choose copy or normal')
                
                elif choice == 5:
                    print('Copy already exists')

                elif choice == 6:
                    exit()

                else:
                    print('Choose a valid option')