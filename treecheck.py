import sys

class TreeNode:                                 #Die Node selbst, die für den Tree gebraucht wird
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1
#########################################################################################
#---------------------------------KLASSE FÜR AUFGABE 1----------------------------------#
#########################################################################################

class BinaryTree:                               
    def __init__(self):
        self.root = None
        self.avl_factor = None
    
    def insert(self, value):
        #Wenn es keinen "value" hat:
        if not self.root:
            #erstelle eine TreeNode                          
            self.root = TreeNode(value)             
        else:
            #Wenn es einen "value" hat: finde einen neuen "Platz" für die Zahl
            self.insert_recursive(self.root, value)
        #Danach berechne den Balance-Value neu    
        self.balance(self.root, value)              
    
    def insert_recursive(self, node, value):
        #WENN die Zahl kleiner als die Node-Zahl ist:
        if value < node.value:                    
            if node.left is None:                  
                node.left = TreeNode(value)         
            else:
                #Wenn es nichts gibt: ruft dich rekursiv auf, damit du einen Platz für die Variable findest  
                self.insert_recursive(node.left, value)

        #WENN die Zahl größer als die Node-Zahl ist: 
        elif value > node.value:                    
            if node.right is None:
                node.right = TreeNode(value)
            else:
                #Wenn es nichts gibt: ruft dich rekursiv auf, damit du einen Platz für die Variable findest 
                self.insert_recursive(node.right, value)  

        #Nachdem einfügen der Zahl: kalkuliere deine Höhe neu
        node.height = 1 + max(self.height(node.left), self.height(node.right)) 
    
    def balance(self, node, new_value):
        #Finde den Balance-Faktor von den Unterbäumen heraus
        balance_factor = self.height(node.right) - self.height(node.left)
        
        #Wenn die Balance von dem Root nicht gegeben ist: dann soll eine AVL-Violation dargestellt werden
        if balance_factor > 1 or balance_factor < -1:
            print(f"bal({new_value}) = {balance_factor} (AVL-Violation)")
        else:
            print(f"bal({new_value}) = {balance_factor}")

        #Speichere den AVL-Wert 
        self.avl_factor = balance_factor
    
    def height(self, node):
        if node is None:
            return 0
        return node.height

    def print_tree(self):
        self.print_tree_recursive(self.root, 0)
    
    def print_tree_recursive(self, node, level):
        if node is None:
            return
        self.print_tree_recursive(node.right, level + 1)
        print('   ' * level + '->', node.value)
        self.print_tree_recursive(node.left, level + 1)

    def build_tree_from_file(self, filename):
        with open(filename, 'r') as file:
            for line in file:                           #PRO LOOP:
                value = int(line.strip())               #hol dir die Line und speichere es in "value"
                self.insert(value)                      #call "insert" mit dem Parameter "value"
                numbers.append(value)                   #gib die Zahl in das Array
#########################################################################################
#---------------------------------KLASSE FÜR AUFGABE 2----------------------------------#
#########################################################################################

class searchTree:
    def __init__(self):
        self.root = None
        self.counter = 0
    
    def insert(self, value):
        if not self.root:
            self.root = TreeNode(value)
        else:
            self.insert_recursive(self.root, value)
    
    def insert_recursive(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = TreeNode(value)
            else:
                self.insert_recursive(node.left, value)
        elif value > node.value:
            if node.right is None:
                node.right = TreeNode(value)
            else:
                self.insert_recursive(node.right, value)
   
    def search_simple_tree(self, value):
        #Schaut ob es einen Wert im Tree gibt und gibt einen Bool-Wert mit einem Array zurück
        found, path = self.search_simple_recursive(self.root, value, [])
        if found:
            #nimmt das Array "path" und erstellt aus jedem Element ein String und fügt Sie zusammen | DANN "joint" er die Strings und nach jedem weiteren Element gibt er ", " hinzu
            path_string = ', '.join(map(str, path))      
            print(f"{value} found: {path_string}")
        else:
            print(f"{value} not found!")

    def search_simple_recursive(self, node, value, path):
        #Wenn es keinen Wert von Anfang an gibt
        if node is None:
            return False, []
        #Wenn der Wert der Gleiche ist
        if node.value == value:
            return True, path + [node.value]
        elif value < node.value:
        #Wenn der Wert kleiner als die Node-Zahl ist
            return self.search_simple_recursive(node.left, value, path + [node.value])
        #Wenn der Wert größer als die Node-Zahl ist
        else:
            return self.search_simple_recursive(node.right, value, path + [node.value])

    def search_sub_tree(self, searchtree):
        #Schaut ob es einen Subtree gibt und gibt True/False zurück
        if self.is_sub_tree(self.root, searchtree.root):
            print("subtree found")
        else:
            print("subtree not found")
    
    def is_sub_tree(self, originaltree, searchtree):         
        if searchtree is None:
            return True
        elif originaltree is None:
            return False       
        elif originaltree.value != searchtree.value:
             #WENN eines der beiden rekursiven Funktionen ein "True" bekommt == "True" 
             return (self.is_sub_tree(originaltree.left, searchtree) or self.is_sub_tree(originaltree.right, searchtree))
        #WENN Beide ein "True" herausbekommen == "True"
        return (self.is_sub_tree(originaltree.left, searchtree.left) and self.is_sub_tree(originaltree.right, searchtree.right))
    
    def print_tree(self):
        self.print_tree_recursive(self.root, 0)
    
    def print_tree_recursive(self, node, level):
        if node is None:
            return
        self.print_tree_recursive(node.right, level + 1)
        print('   ' * level + '->', node.value)
        self.print_tree_recursive(node.left, level + 1)

    def build_tree_from_file(self, filename):
        with open(filename, 'r') as file:      
            for line in file:
                value = int(line.strip())
                self.insert(value)
                self.counter += 1

#########################################################################################
#------------------------------------Main-Funktion--------------------------------------#
#########################################################################################
numbers = []
tree = BinaryTree()

#MINDESTENS 2 Argumente weil "python" das Programm ist UND "treecheck.py baum_daten.txt" die beiden Argumente
if len(sys.argv) == 2:                  #AVL-ÜBERPRÜFUNG
    filename = sys.argv[1]
    tree.build_tree_from_file(filename) #Erstellt den Baum aus dem text-file
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

    #Erstelle OriginalTree
    filename = sys.argv[1]              
    originaltree.build_tree_from_file(filename)

    #Erstelle Tree für die Suche
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
