class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1

class BinaryTree:
    def __init__(self):
        self.root = None
        self.avl_factor = None
    
    def insert(self, value):
        if not self.root:
            self.root = TreeNode(value)
        else:
            self._insert_recursive(self.root, value)
        self.balance(self.root, value)
    
    def _insert_recursive(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = TreeNode(value)
            else:
                self._insert_recursive(node.left, value)
        elif value > node.value:
            if node.right is None:
                node.right = TreeNode(value)
            else:
                self._insert_recursive(node.right, value)
        
        # Update the height of the current node
        node.height = 1 + max(self._height(node.left), self._height(node.right))
    
    def balance(self, node, new_value):
        self._balance_recursive(self.root)

        # Calculate the balance factor for the current node
        balance_factor = self._height(node.right) - self._height(node.left)
        
        # Check if the node is balanced or not, and print the balance factor if it's not balanced
        if balance_factor > 1 or balance_factor < -1:
            print(f"bal({new_value}) = {balance_factor} (AVL-Violation)")
        else:
            print(f"bal({new_value}) = {balance_factor}")

        self.avl_factor = balance_factor
    
    def _balance_recursive(self, node):
        if node is None:
            return 0
        
        # Recursively balance the left and right subtrees
        self._balance_recursive(node.left)
        self._balance_recursive(node.right)
    
    def _height(self, node):
        if node is None:
            return 0
        return node.height

    def print_tree(self):
        self._print_tree_recursive(self.root, 0)
    
    def _print_tree_recursive(self, node, level):
        if node is None:
            return
        self._print_tree_recursive(node.right, level + 1)
        print('   ' * level + '->', node.value)
        self._print_tree_recursive(node.left, level + 1)

# Example usage:
tree = BinaryTree()
tree.insert(5)
tree.insert(3)
tree.insert(7)
tree.insert(2)
tree.insert(4)
tree.insert(6)
tree.insert(8)
tree.insert(9)
tree.insert(10)

if(tree.avl_factor > 1 or tree.avl_factor < -1):
    print("AVL: no")
else:
    print("AVL: yes")

tree.print_tree()
