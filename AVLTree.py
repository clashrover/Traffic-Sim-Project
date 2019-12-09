class Node():
	val_x = 0
	val_y = 0
	right = None
	left = None
	height = 0

	def __init__(self,val_x,val_y):
		self.val_x = val_x
		self.val_y = val_y
		self.left =None
		self.right = None
		self.height = 1

class AVLTree():

	def insert(self, root, key_x, key_y):

		#Normal BST insertion
		if not root:
			return Node(key_x,key_y)

		elif key_x < root.val_x:
			root.left = self.insert(root.left,key_x,key_y)

		elif key_x == root.val_x:
			if key_y < root.val_y:
				root.left = self.insert(root.left,key_x,key_y)
			else:
				root.right = self.insert(root.right, key_x, key_y)

		else:
			root.right = self.insert(root.right, key_x, key_y)


		#updating the height
		root.height = 1+ max(self.getHeight(root.left) , self.getHeight(root.right))

		#check if root is balanced
		balance = self.checkBalance(root)

		if balance > 1 and key_x < root.left.val_x :
			return self.rightRotate(root)

		if balance > 1 and key_x == root.left.val_x:
			if key_y < root.left.val_y:
				return self.rightRotate(root)
			else:
				root.left = self.leftRotate(root.left)
				return self.rightRotate(root)

		if balance >1 and key_x < root.left.val_x:
			root.left = self.leftRotate(root.left)
			return self.rightRotate(root)	
			
		if balance < -1 and key_x > root.right.val_x:
			return self.leftRotate(root)

		if balance < -1 and key_x == root.right.val_x:
			if key_y > root.right.val_y:
				return self.leftRotate(root)
			else:
				root.right = self.rightRotate(root.right)
				return self.leftRotate(root)

		if balance < -1 and key_x < root.right.val_x:
			root.right = self.rightRotate(root.right)
			return self.leftRotate(root)	

		return root

	def leftRotate(self, node):
		child = node.right
		n2 = child.left
		child.left = node
		node.right = n2

		node.height = 1 + max(self.getHeight(node.left), self.getHeight(node.right))				
		child = 1 + max(self.getHeight(child.left), self.getHeight(child.right))

		return child

	def rightRotate(self,node):
		child = node.left
		n1 = child.right

		child.right = node
		node.left = n1

		node.height = 1 + max(self.getHeight(node.left), self.getHeight(node.right))				
		child = 1 + max(self.getHeight(child.left), self.getHeight(child.right))

		return child

	def checkBalance(self,root):
		if not root:
			return

		return self.getHeight(root.left)-self.getHeight(root.right)

	def getHeight(self, root):
		if not root:
			return 0
		return root.height

	def preOrderTraversal(self,root):
		if not root:
			return

		#print("{0} ".format(root.val), end="") 
		self.preOrderTraversal(root.left)
		self.preOrderTraversal(root.right)


myTree = AVLTree()
root = None

root = myTree.insert(root, 10, 20)
root = myTree.insert(root, 20 , 30)
root = myTree.insert(root, 30 , 40)

myTree.preOrderTraversal(root)
