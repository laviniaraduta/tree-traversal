from node import Node
import unittest

class Tree:
    """ Tree class for binary tree """

    def __init__(self):
        """ Constructor for Tree class """
        self.root = None

    def getRoot(self):
        """ Method for get root of the tree """
        return self.root

    def add(self, data):
        """ Method for add data to the tree """
        if self.root is None:
            self.root = Node(data)
        else:
            self._add(data, self.root)

    def _add(self, data, node):
        """Method for add data to the tree

        Args:
            data (int): data to add

        Returns:
            None
        """
        if data < node.data:
            if node.left is not None:
                self._add(data, node.left)
            else:
                node.left = Node(data)
        else:
            if node.right is not None:
                self._add(data, node.right)
            else:
                node.right = Node(data)

    def find(self, data):
        """Method for find data in the tree

        Args:
            data (int): data to find

        Returns:
            Node: node with data
        """
        if self.root is not None:
            return self._find(data, self.root)
        else:
            return None

    def _find(self, data, node):
        if data == node.data:
            return node
        elif (data < node.data and node.left is not None):
            return self._find(data, node.left)
        elif (data > node.data and node.right is not None):
            return self._find(data, node.right)

    def deleteTree(self):
        """Method for delete tree

        Args:
            None
        Returns:
            None
        """
        self.root = None

    def printTree(self):
        """Method for print tree
        
        Args:
            None
        Returns:
            None
        """
        if self.root is not None:
            self._printInorderTree(self.root)

    def _printInorderTree(self, node):
        """Method for print tree in order
        
        Args:
            node (Node): node to start print
        Returns:
            None
        """
        if node is not None:
            self._printInorderTree(node.left)
            print(str(node.data) + ' ')
            self._printInorderTree(node.right)

    def _printPreorderTree(self, node):
        """Method for print tree pre order
        
        Args:
            node (Node): node to start print
        Returns:
            None
        """
        if node is not None:
            print(str(node.data) + ' ')
            self._printPreorderTree(node.left)
            self._printPreorderTree(node.right)

    def _printPostorderTree(self, node):
        """Method for print tree post order

        Args:
            node (Node): node to start print
        Returns:
            None
        """
        if node is not None:
            self._printPostorderTree(node.left)
            self._printPostorderTree(node.right)
            print(str(node.data) + ' ')


class TestFind(unittest.TestCase):
    def setUp(self):
        self.tree = Tree()
        self.tree.add(3)
        self.tree.add(4)
        self.tree.add(0)
        self.tree.add(8)
        self.tree.add(2)

    def test_find(self):
        self.assertEqual(self.tree.find(3).data, 3)
        self.assertEqual(self.tree.find(4).data, 4)
        self.assertEqual(self.tree.find(0).data, 0)
        self.assertEqual(self.tree.find(8).data, 8)
        self.assertEqual(self.tree.find(2).data, 2)

    def test_not_find(self):
        self.assertEqual(self.tree.find(5), None)
        self.assertEqual(self.tree.find(9), None)
        self.assertEqual(self.tree.find(-1), None)


