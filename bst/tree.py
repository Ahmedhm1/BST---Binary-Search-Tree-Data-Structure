"""
Binary Search Tree (BST) implementation in Python.

This module provides two classes:
1. Node: Represents a node in the tree.
2. Tree: Represents the binary search tree with basic operations:
   - Insert (append)
   - Traversals (pre-order, in-order, post-order)
   - Search
   - Get min/max
   - Remove a value
   - Change a value

Author: [Ahmed Hisham]
License: MIT
"""

class Node:
    """
    Represents a single node in the binary search tree.

    Attributes:
        value (int/float): The value stored in the node.
        left (Node): Reference to the left child node.
        right (Node): Reference to the right child node.
    """
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None


class Tree:
    """
    Binary Search Tree (BST) implementation.

    Attributes:
        root (Node): The root node of the tree.
        items (int): The number of nodes in the tree.
    """
    def __init__(self):
        self.items = 0
        self.root = None

    def append(self, value):
        """
        Insert a value into the BST.

        Args:
            value (int/float): Value to insert.

        Returns:
            True if inserted successfully.
            str if the value already exists.
        """
        new_node = Node(value)
        if self.items == 0:  # If tree is empty, set root
            self.root = new_node
            self.items += 1
            return True
        
        current = self.root
        while True:
            if value < current.value:  # Go left
                if current.left is None:
                    current.left = new_node
                    self.items += 1
                    return True
                current = current.left
            elif value > current.value:  # Go right
                if current.right is None:
                    current.right = new_node
                    self.items += 1
                    return True
                current = current.right
            else:
                return f"{value} already added"

    def print_pre_order(self, current=1):
        """
        Print tree values in pre-order traversal (Root -> Left -> Right).
        """
        if self.items == 0:
            print("Tree is empty")
            return
        if current is None:
            return
        if current == 1:
            current = self.root 

        print(current.value)
        self.print_pre_order(current.left)       
        self.print_pre_order(current.right)       

    def print_in_order(self, current=1):
        """
        Print tree values in in-order traversal (Left -> Root -> Right).
        """
        if self.items == 0:
            print("Tree is empty")
            return
        if current is None:
            return
        if current == 1:
            current = self.root
        
        self.print_in_order(current.left)
        print(current.value)
        self.print_in_order(current.right)

    def print_post_order(self, current=1):
        """
        Print tree values in post-order traversal (Left -> Right -> Root).
        """
        if self.items == 0:
            print("Tree is empty")
            return
        if current is None:
            return
        if current == 1:
            current = self.root

        self.print_post_order(current.left)
        self.print_post_order(current.right)
        print(current.value)

    def is_empty(self):
        """Check if the tree is empty."""
        return self.items == 0

    def remove_value(self, value):
        """
        Remove a node by value.

        Args:
            value (int/float): The value to remove.

        Returns:
            The value removed, or False if not found.
        """
        if self.is_empty():
            raise Exception("Tree is empty")
        
        before_deleted_node = self.root
        deleted_node = self.root
        found = False

        # Search for node to delete
        while deleted_node and not found:
            if deleted_node.value == value:
                found = True
                break
            elif value < deleted_node.value:
                before_deleted_node = deleted_node
                deleted_node = deleted_node.left
            elif value > deleted_node.value:
                before_deleted_node = deleted_node
                deleted_node = deleted_node.right

        if not found:
            return False
        
        # Case 1: Node has no children
        if not deleted_node.left and not deleted_node.right:
            if self.root.value == value:
                self.root = None
            elif before_deleted_node.left == deleted_node:
                before_deleted_node.left = None
            elif before_deleted_node.right == deleted_node:
                before_deleted_node.right = None

        # Case 2: Node has one child
        elif not deleted_node.left or not deleted_node.right:
            child = deleted_node.left if deleted_node.left else deleted_node.right
            if self.root.value == value:
                self.root = child
            elif before_deleted_node.left == deleted_node:
                before_deleted_node.left = child
            elif before_deleted_node.right == deleted_node:
                before_deleted_node.right = child

        # Case 3: Node has two children
        elif deleted_node.left and deleted_node.right:
            before_successor_node = deleted_node
            successor_node = deleted_node.right

            # Find in-order successor
            while successor_node.left:
                before_successor_node = successor_node
                successor_node = successor_node.left

            if before_successor_node != deleted_node:
                before_successor_node.left = successor_node.right
                successor_node.right = deleted_node.right

            successor_node.left = deleted_node.left

            if before_deleted_node.left == deleted_node:
                before_deleted_node.left = successor_node
            elif before_deleted_node.right == deleted_node:
                before_deleted_node.right = successor_node

            if self.root == deleted_node:
                self.root = successor_node

        self.items -= 1
        return deleted_node.value
                
    def change_value(self, old_value, new_value, current=1):
        """
        Change a node's value.

        Args:
            old_value (int/float): Value to search and replace.
            new_value (int/float): New value to set.

        Returns:
            True if changed, False otherwise.
        """
        if self.is_empty():
            raise Exception("Tree is empty")
        if current is None:
            return False
        if current == 1:
            current = self.root

        if current.value == old_value:
            current.value = new_value
            return True
        elif old_value < current.value and current.left:
            return self.change_value(old_value, new_value, current.left)
        elif old_value > current.value and current.right:
            return self.change_value(old_value, new_value, current.right)
        return False

    def search(self, value, current=1):
        """
        Search for a value in the tree.

        Returns:
            True if found, False otherwise.
        """
        if self.is_empty():
            raise Exception("Tree is empty")
        if current is None:
            return False
        if current == 1:
            current = self.root

        if current.value == value:
            return True
        elif value < current.value and current.left:
            return self.search(value, current.left)
        elif value > current.value and current.right:
            return self.search(value, current.right)
        return False
    
    def get_min(self, current=1):
        """
        Get the minimum value in the tree.
        """
        if self.is_empty():
            raise Exception("Tree is empty")
        if current == 1:
            current = self.root

        while current.left:
            current = current.left

        return current.value

    def get_max(self, current=1):
        """
        Get the maximum value in the tree.
        """
        if self.is_empty():
            raise Exception("Tree is empty")
        if current == 1:
            current = self.root

        while current.right:
            current = current.right

        return current.value
