import sys

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

    def build_tree_from_file(self, filename):
        with open(filename, 'r') as file:
            for line in file:
                value = int(line.strip())
                self.insert(value)
                numbers.append(value)


class searchTree:
    def __init__(self):
        self.root = None
        self.path_to_value = []  # Array zur Speicherung des Pfads zum Wert
        self.counter = 0
    
    def insert(self, value):
        if not self.root:
            self.root = TreeNode(value)
        else:
            self._insert_recursive(self.root, value)
    
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

    def get_data(self):
        return self.path_to_value

    def search_simple_tree(self, value):
        found, path = self._search_simple_recursive(self.root, value, [])
        if found:
            #nimmt das Array "path" und erstellt aus jedem Element ein String und fügt Sie zusammen | DANN "joint" er die Strings und nach jedem weiteren Element gibt er ", " hinzu
            path_string = ', '.join(map(str, path))      
            print(f"{value} found: {path_string}")
        else:
            print(f"{value} not found!")

    def _search_simple_recursive(self, node, value, path):
        if node is None:
            return False, []
        if node.value == value:
            return True, path + [node.value]
        elif value < node.value:
            return self._search_simple_recursive(node.left, value, path + [node.value])
        else:
            return self._search_simple_recursive(node.right, value, path + [node.value])

    def search_sub_tree(self, originaltree):
        if self._is_sub_tree(self.root, originaltree.root):
            print(originaltree.root)
            print("subtree found")
        else:
            print(originaltree.root)
            print(self.root)
            print("subtree not found")

    def is_sub_root(self, mainTreeroot, subTreeroot):
        if subTreeroot is None and mainTreeroot is None:
            return True
        
        if mainTreeroot is None:
            return False
        
        if self._is_sub_tree(mainTreeroot, subTreeroot):
            return True
        
        return (self.is_sub_root(mainTreeroot.left, subTreeroot) or
                self.is_sub_root(mainTreeroot.right, subTreeroot))


    def _is_sub_tree(self, node1, node2):         
        if node2 is None:
            return True
        
        if node1 is None:
            return False
                                    
        if node1.value != node2.value:
             return (self._is_sub_tree(node1.left, node2) or
                self._is_sub_tree(node1.right, node2))
        
        return (self._is_sub_tree(node1.left, node2.left) and
                self._is_sub_tree(node1.right, node2.right))
        

    def print_tree(self):
        self._print_tree_recursive(self.root, 0)
    
    def _print_tree_recursive(self, node, level):
        if node is None:
            return
        self._print_tree_recursive(node.right, level + 1)
        print('   ' * level + '->', node.value)
        self._print_tree_recursive(node.left, level + 1)

    def build_tree_from_file(self, filename):
        with open(filename, 'r') as file:
            for line in file:
                value = int(line.strip())
                self.insert(value)
                self.counter += 1
                #numbers.append(value)

    





#MAIN-FUNCTION
numbers = []
tree = BinaryTree()

#MINDESTENS 2 Argumente weil "python" das Programm ist UND "treecheck.py baum_daten.txt" die beiden Argumente
if len(sys.argv) == 2:                  #AVL-ÜBERPRÜFUNG
    filename = sys.argv[1]
    tree.build_tree_from_file(filename)
    #CHANGE THIS(CANNOT BE "NOT NONE")
    if tree.avl_factor is not None and (tree.avl_factor > 1 or tree.avl_factor < -1):
        print("AVL: no")
    else:
        print("AVL: yes")
    
    smallestNumber = min(numbers)
    highestNumber = max(numbers)
    average = sum(numbers) / len(numbers)
    print("min:", smallestNumber, "max:", highestNumber, "avg:", average)

elif len(sys.argv) == 3:                #SUCHFUNKTION
    counter = 0
    originaltree = searchTree()
    searchtree = searchTree()

    #OriginalTree
    filename = sys.argv[1]              
    originaltree.build_tree_from_file(filename)

    #Tree für die Suche
    searchname = sys.argv[2]
    searchtree.build_tree_from_file(searchname)
    #print(searchtree.counter)

    
    if(searchtree.counter > 1):     #Wenn der Tree mehr als eine Zahl hat
        #TODO
        originaltree.search_sub_tree(searchtree)
        searchtree.print_tree()
    else:                           #Wenn der Tree nur einen Nummer hat
        originaltree.search_simple_tree(searchtree.root.value)          

else:
    print("Zuviele oder Zuwenige Argumente!")
    sys.exit(1)





tree.print_tree()
