import numpy as np

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

    def searchNear(self, root, x , y, velx, vely): #please call this function in specific region
        junc = np.ones(2)
        
        if root == None:
            junc[0] = None
            junc[1] = None
            return junc

        if velx>0.1 and abs(vely)<0.1:


            if root.val_x-x >0 and root.val_x-x > 1:
                return self.searchNear(root.left,x,y,velx, vely)

            if root.val_x-x >0 and root.val_x-x <1:
                if abs(root.val_y-y)<0.1:
                    junc[0]= root.val_x
                    junc[1]= root.val_y
                    return junc

                else:
                    if root.val_y < y :
                        return self.searchNear(root.right,x,y,velx, vely)

                    else:
                        return self.searchNear(root.left,x,y,velx,vely)

            if root.val_x-x < 0:
                return self.searchNear(root.right,x,y,velx,vely)


        if velx<-0.1 and abs(vely)<0.1:

            if x-root.val_x >0 and x-root.val_x > 1:
                return self.searchNear(root.right,x,y,velx, vely)

            if x-root.val_x >0 and x-root.val_x <1:
                if abs(root.val_y-y)<0.1:
                    junc[0]= root.val_x
                    junc[1]= root.val_y
                    return junc

                else:
                    if root.val_y < y :
                        return self.searchNear(root.right,x,y,velx, vely)

                    else:
                        return self.searchNear(root.left,x,y,velx,vely)

            if x-root.val_x < 0:
                return self.searchNear(root.left,x,y,velx,vely)


        if vely>0.1 and abs(velx)<0.1:

            if abs(root.val_x-x) < 0.1:
                if root.val_y-y < 1 and root.val_y-y>0:
                    junc[0]=root.val_x
                    junc[1]=root.val_y
                    return junc

                else:
                    if root.val_y>y :
                        return self.searchNear(root.left,x,y,velx,vely)
                    else:
                        return self.searchNear(root.right,x,y,velx,vely)
                
            else:
                if root.val_x < x:
                    return self.searchNear(root.right,x,y,velx,vely)
                else:
                    return self.searchNear(root.left,x,y,velx,vely)

        if vely<-0.1 and abs(velx) <0.1:
            if abs(root.val_x-x) < 0.1:
                if y-root.val_y < 1 and y-root.val_y>0:
                    junc[0]=root.val_x
                    junc[1]=root.val_y
                    return junc

                else:
                    if root.val_y>y :
                        return self.searchNear(root.left,x,y,velx,vely)
                    else:
                        return self.searchNear(root.right,x,y,velx,vely)
                
            else:
                if root.val_x < x:
                    return self.searchNear(root.right,x,y,velx,vely)
                else:
                    return self.searchNear(root.left,x,y,velx,vely)

       

        
# code referenced from geek for geeks. Studied and modified for the project
# Link: https://www.geeksforgeeks.org/avl-tree-set-1-insertion/  
  

# Uncomment the driver code to validate
  
# myTree = AVLTree() 
# root = None
  
# root = myTree.insert(root, 0.5,0.5) 
# root = myTree.insert(root, 1.5,0.5) 
# root = myTree.insert(root, 2.5,0.5) 
# root = myTree.insert(root, 0.5,1.5)
# root = myTree.insert(root, 0.5,2.5)
# root = myTree.insert(root, 1.5,1.5)
# root = myTree.insert(root, 1.5,2.5)
# root = myTree.insert(root, 2.5,1.5)
# root = myTree.insert(root, 2.5,2.5)



# myTree.preOrder(root) 
# print() 

# junc = myTree.searchNear(root,0.1,0.525,4,0)
# print(junc[0],junc[1])
# junc = myTree.searchNear(root,0.2,1.525,4,0)
# print(junc[0],junc[1])
# junc = myTree.searchNear(root,0.25,2.525,4,0)
# print(junc[0],junc[1])
# junc = myTree.searchNear(root,1.34,0.527,4,0)
# print(junc[0],junc[1])
# junc = myTree.searchNear(root,1.4,1.526,4,0)
# print(junc[0],junc[1])
# junc = myTree.searchNear(root,1.3,2.528,4,0)
# print(junc[0],junc[1])
# junc = myTree.searchNear(root,2.36,0.525,4,0)
# print(junc[0],junc[1])
# junc = myTree.searchNear(root,2.29,1.525,4,0)
# print(junc[0],junc[1])
# junc = myTree.searchNear(root,2.28,2.525,4,0)
# print(junc[0],junc[1])


# junc = myTree.searchNear(root,2.7,0.475,-4,0)
# print(junc[0],junc[1])
# junc = myTree.searchNear(root,2.7,1.475,-4,0)
# print(junc[0],junc[1])
# junc = myTree.searchNear(root,2.7,2.475,-4,0)
# print(junc[0],junc[1])
# junc = myTree.searchNear(root,1.7,0.477,-4,0)
# print(junc[0],junc[1])
# junc = myTree.searchNear(root,1.7,1.460,-4,0)
# print(junc[0],junc[1])
# junc = myTree.searchNear(root,1.7,2.457,-4,0)
# print(junc[0],junc[1])
# junc = myTree.searchNear(root,0.7,0.475,-4,0)
# print(junc[0],junc[1])
# junc = myTree.searchNear(root,0.7,1.4725,-4,0)
# print(junc[0],junc[1])
# junc = myTree.searchNear(root,0.7,2.49,-4,0)
# print(junc[0],junc[1])

# junc = myTree.searchNear(root, 0.475 , 0.4 , 0 , 4 )
# print(junc[0],junc[1])
# junc = myTree.searchNear(root,0.46,1.4,0,4)
# print(junc[0],junc[1])
# junc = myTree.searchNear(root,0.46,2.45,0,4)
# print(junc[0],junc[1])
# junc = myTree.searchNear(root,1.46,0.4,0,4)
# print(junc[0],junc[1])
# junc = myTree.searchNear(root,1.46,1.4,0,4)
# print(junc[0],junc[1])
# junc = myTree.searchNear(root,1.46,2.2,0,4)
# print(junc[0],junc[1])
# junc = myTree.searchNear(root,2.462,0.4,0,4)
# print(junc[0],junc[1])
# junc = myTree.searchNear(root,2.46,1.4,0,4)
# print(junc[0],junc[1])
# junc = myTree.searchNear(root,2.46,2.4,0,4)
# print(junc[0],junc[1])

# junc = myTree.searchNear(root, 0.525 , 0.7 , 0 , -4 )
# print(junc[0],junc[1])
# junc = myTree.searchNear(root,0.526,1.7,0,-4)
# print(junc[0],junc[1])
# junc = myTree.searchNear(root,0.526,2.75,0,-4)
# print(junc[0],junc[1])
# junc = myTree.searchNear(root,1.53,0.7,0,-4)
# print(junc[0],junc[1])
# junc = myTree.searchNear(root,1.54,1.7,0,-4)
# print(junc[0],junc[1])
# junc = myTree.searchNear(root,1.525,2.7,0,-4)
# print(junc[0],junc[1])
# junc = myTree.searchNear(root,2.53,0.7,0,-4)
# print(junc[0],junc[1])
# junc = myTree.searchNear(root,2.53,1.7,0,-4)
# print(junc[0],junc[1])
# junc = myTree.searchNear(root,2.57,2.7,0,-4)
# print(junc[0],junc[1])




