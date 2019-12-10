class Node(object): 
    def __init__(self, val_x,val_y): 
        self.val_x = val_x 
        self.val_y = val_y
        self.left = None
        self.right = None
        self.height = 1

class AVLTree(object): 
  
    # new root of subtree. 
    def insert(self, root, key_x, key_y):
        # Normal BST 
        if not root:
            return Node(key_x,key_y) 
        elif key_x < root.val_x:
            root.left = self.insert(root.left, key_x, key_y)
        elif key_x == root.val_x:
        	if key_y < root.val_y:
        		root.left = self.insert(root.left, key_x, key_y)
        	else:
        		root.right = self.insert(root.right, key_x, key_y)
        else:
            root.right = self.insert(root.right, key_x, key_y) 
  
        # Update the height of above node 
        root.height = 1 + max(self.getHeight(root.left), 
                           self.getHeight(root.right)) 
  
        # check if node is unbalanced
        balance = self.getBalance(root) 
  
        # If unbalanced, then see which of the 4 case apply

        # left left case 
        if balance > 1:
        	if key_x < root.left.val_x:
        		return self.rightRotate(root)
        	elif key_x == root.left.val_x:
        		if key_y < root.left.val_y:
        			return self.rightRotate 
  
        # right right case
        if balance < -1:
        	if key_x > root.right.val_x:
        		return self.leftRotate(root)

        	elif key_x == root.right.val_x :
        		if key_y > root.right.val_y:
        			return self.leftRotate(root)
  
        # Left Right case 
        # in this first right rotate child and then left rotate node
        if balance > 1:
        	if key_x > root.left.val_x:
        		root.left = self.leftRotate(root.left)
        		return self.rightRotate(root)
        	elif key_x == root.left.val_x:
        		if key_y > root.left.val_y:
        			root.left = self.leftRotate(root.left)
        			return self.rightRotate(root)

  
        # Right Left
        # in this first left rotate child then right rotate node 
        if balance < -1:
        	if key_x < root.right.val_x:
        		root.right = self.rightRotate(root.right)
        		return self.leftRotate(root)
        	elif key_x == root.right.val_x:
        		if key_y < root.right.val_y:
        			root.right = self.rightRotate(root.right) 
        			return self.leftRotate(root)

  
        return root 
  
    def leftRotate(self, node):
  
        child = node.right 
        grandChild = child.left 
  
        # Perform rotation 
        child.left = node 
        node.right = grandChild 
  
        # Update heights 
        node.height = 1 + max(self.getHeight(node.left), 
                         self.getHeight(node.right)) 
        child.height = 1 + max(self.getHeight(child.left), 
                         self.getHeight(child.right)) 
  
        # Return the new root 
        return child 
  
    def rightRotate(self, node):
  
        child = node.left 
        grandChild = child.right 
  
        # Perform rotation 
        child.right = node 
        node.left = grandChild 
  
        # Update heights 
        node.height = 1 + max(self.getHeight(node.left), 
                        self.getHeight(node.right)) 
        child.height = 1 + max(self.getHeight(child.left), 
                        self.getHeight(child.right)) 
  
        # Return the new root 
        return child
  
    def getHeight(self, root):
        if not root: 
            return 0
  
        return root.height 
  
    def getBalance(self, root):
        if not root: 
            return 0
  
        return self.getHeight(root.left) - self.getHeight(root.right) 
  
    def preOrder(self, root):
  
        if not root: 
            return
  
        print(root.val_x , root.val_y) 
        self.preOrder(root.left) 
        self.preOrder(root.right) 

    #def searchNearby(self, x , y):


# code referenced from geek for geeks. Studied and modified for the project
# Link: https://www.geeksforgeeks.org/avl-tree-set-1-insertion/  
  

# Uncomment the driver code to validate
  
# myTree = AVLTree() 
# root = None
  
# root = myTree.insert(root, 10,20) 
# root = myTree.insert(root, 10,30) 
# root = myTree.insert(root, 10,40) 
# root = myTree.insert(root, 20,60)
# root = myTree.insert(root, 20,50)
# root = myTree.insert(root, 30,60)
# root = myTree.insert(root, 30,70)


# myTree.preOrder(root) 
# print() 
