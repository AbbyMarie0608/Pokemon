'''
Author: Abby-Marie Tong
KUID: 3178667
Date: 4/16/2025
Lab: 8
Last Modified: 4/18/2025
Purpose: Creates a Binary Search Tree

'''
from binarynode import BinaryNode
class BinarySearchTree:
    def __init__(self):
        '''Initializes root'''
        self._root = None

    def add(self, item):
        '''Adds a node if the tree is empty if not then uses _rec_add'''
        if self._root is None:
            self._root = BinaryNode(item)
        else:
            self._rec_add(item, self._root)

    def _rec_add(self, item, cur_node):
        '''Recurses through the numbers and packages them into a node and adds them to the tree'''
        try:
            if cur_node.entry == item:
                raise KeyError
            elif cur_node.entry > item:
                if cur_node.left is None:
                    cur_node.left = BinaryNode(item)
                else:
                    self._rec_add(item, cur_node.left)
            else:
                if cur_node.right is None:
                    cur_node.right = BinaryNode(item)
                else:
                    self._rec_add(item, cur_node.right)
        except KeyError:
            print('No duplicates allowed')

    def find_max(self, cur_node):
        '''Finds and returns the max node in the LST'''
        if cur_node.right is None:
            return cur_node
        else:
            return self.find_max(cur_node.right)
        
    
    def remove(self, key):
        '''Gets an ID to remove and removes from the tree'''
        if self.search(key) is False:
            print('Item Not Found')
            return
        self._root = self._rec_remove(key, self._root)
        
    def _rec_remove(self, key, cur_node):
        '''Recurses through the tree to find the ID to remove and removes from the tree'''
        if cur_node is None:
            return
        if key < cur_node.entry.number:
            cur_node.left = self._rec_remove(key, cur_node.left)
        elif key > cur_node.entry.number:
            cur_node.right = self._rec_remove(key, cur_node.right)
        else:
            if cur_node.left is None:
                return cur_node.right
            elif cur_node.right is None:
                return cur_node.left
            temp = self.find_max(cur_node.left)
            cur_node.entry = temp.entry
            cur_node.left = self._rec_remove(temp.entry.number, cur_node.left)
        return cur_node
            
    
    def search(self, key):
        '''Gets a key and returns the node entry'''
        if self._root is None:
            return False
        else:
            return self._rec_search(key, self._root)
        
    def _rec_search(self, key, cur_node):
        '''Gets a key and returns the node entry recurses through the tree to find the node'''
        try:
            if cur_node is None:
                print('Item not found')
                return
            if cur_node.entry.number == key:
                return cur_node.entry
            if cur_node.entry.number > key:
                return self._rec_search(key, cur_node.left)
            if cur_node.entry.number < key:
                return self._rec_search(key, cur_node.right)
            raise KeyError
        except KeyError:
            print('Item not found')

    def visit_function(self, entry):
        '''Takes an entry and prints the number'''
        print(entry, end = '\n')

    def preorder(self, visit_function):
        '''Starts off the recursion of preorder'''
        self._rec_preorder(visit_function, self._root)

    def _rec_preorder(self, visit_function, cur_node):
        '''Recurses through the preorder format'''
        if cur_node is None:
            return
        visit_function(cur_node.entry)
        self._rec_preorder(visit_function, cur_node.left)
        self._rec_preorder(visit_function, cur_node.right)

    def inorder(self, visit_function):
        '''Starts off the recursion of inorder'''
        self._rec_inorder(visit_function, self._root)

    def _rec_inorder(self, visit_function, cur_node):
        '''Recurses through the inorder format'''
        if cur_node is None:
            return
        self._rec_inorder(visit_function, cur_node.left)
        visit_function(cur_node.entry)
        self._rec_inorder(visit_function, cur_node.right)

    def postorder(self, visit_function):
        '''Recurses through the postorder format'''
        self._rec_postorder(visit_function, self._root)

    def _rec_postorder(self, visit_function,cur_node):
        '''Recurses through the postorder format'''
        if cur_node is None:
            return
        self._rec_postorder(visit_function, cur_node.left)
        self._rec_postorder(visit_function, cur_node.right)
        visit_function(cur_node.entry)
        



