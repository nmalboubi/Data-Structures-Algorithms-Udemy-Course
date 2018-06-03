#Binary Search Trees Notes
class Node(object):

	def __init__(self, data):
		self.data = data;
		#set left and right nodes = to null as starting point
		self.leftChild = None;
		self.rightChild = None;
		
class BinarySearchTree(object):

	def __init__(self):
		self.root = None;
		
	def insert(self, data):
		# this is the first item to insert
		#Important to reach items in tree with help of the root node; thats why we need to store reference to root node. 
		#Start out root node to find given item
		if not self.root:
			self.root = Node(data);
		else:
			self.insertNode(data, self.root);
			
	# O(logN) if the tree is balanced  --> it can reduced to O(N) if tree is not balanced
	def insertNode(self, data, node):
	
		if data < node.data:
			if node.leftChild:
			#is there an existing left child? If there is, call is recursively below
				self.insertNode(data, node.leftChild);
			else:
				node.leftChild = Node(data);
			#if data is > root node go to right hand side
		else:
		#if right child exists, call below
			if node.rightChild:
				self.insertNode(data, node.rightChild);
				#if right child is empty
			else:
				node.rightChild = Node(data);
	
	# O(logN)	
	def removeNode(self, data, node):
	#if node is null, return with the node
		if not node:
			return node;
		#go down left side of tree	
		if data < node.data:
		#re-call recurseively to find the data on the left side of the tree
			node.leftChild = self.removeNode(data, node.leftChild);
			#check right side of tree. 
		elif data > node.data:
			node.rightChild = self.removeNode(data, node.rightChild);
		else:
			#when finding node we would like to get rid of there are 3 cases
			#if no left and right children, you can just delete the node. It is a leaf node
			if not node.leftChild and not node.rightChild:
				print("Removing a leaf node...");
				del node;
				#this is how we tell the parent node that the child has been deleted	
				return None;
				
				#you are removing a node that has a single right child
			if not node.leftChild:  # node !!!
				print("Removing a node with single right child...");
				#temporary node to host right child, and then delete node. This tells parents of node that it was deleted
				tempNode = node.rightChild;
				del node;
				return tempNode;
				#removing node with single left child
			elif not node.rightChild:   # node instead of self
				print("Removing a node with single left child...");
				#create temp node, delete and then return temporary node
				tempNode = node.leftChild;
				del node;
				return tempNode;
			
			print("Removing node with two children....");
			#get predecessor Node, which is largest on left hand side
			tempNode = self.getPredecessor(node.leftChild);   # self instead of elif  + get predecessor 
			node.data = tempNode.data;
			#call method recursively on predecessor
			node.leftChild = self.removeNode(tempNode.data, node.leftChild);
			#may end up with one of the first two situations. May be a 1 leaf node, or may have a single child
		
		return node;

	def getPredecessor(self, node):
	
		if node.rightChild:
		#goes through the left hand side and finds the largest value, which will be on the right node, if it exists
			return self.getPredeccor(node.rightChild);
			
		return node;
		
	def remove(self, data):
		if self.root:
		#if there is a node, call the removeNode function
			self.root = self.removeNode(data, self.root);
			
		# O(logN)
			# Get minimum value of a Binary Search Tree			

	def getMinValue(self):
		#if not  a null, then return getMin function. If there are items, return below
		if self.root:
			return self.getMin(self.root);
		

	# Get minimum value of a Binary Search Tree			
	def getMin(self, node):
	# if it's not a null, then return
	#left sub tree is always smallest - need to go all the way to the left
		if node.leftChild:
			return self.getMin(node.leftChild);
			
		return node.data;
		
		# O(logN)
	def getMaxValue(self):
		if self.root:
			return self.getMax(self.root);
			
	def getMax(self, node):
	#start from right node. If not null, recursively call function again
		if node.rightChild:
			return self.getMax(node.rightChild);
		#this is the else statement. If you reach the right most node, you will reach this	
		return node.data;
		
	def traverse(self):
	#moving through nodes if nodes existing
		if self.root:
			self.traverseInOrder(self.root);
			#function is defined below
			
			# O(N)
	def traverseInOrder(self, node):
	# if left node exists, then recursively call function again; 
		if node.leftChild:
			self.traverseInOrder(node.leftChild);
			#finds smallest node and prints
		print("%s " % node.data);
		#this finds deepest level node of a tree
		if node.rightChild:
			self.traverseInOrder(node.rightChild);
			
			
bst = BinarySearchTree();
bst.insert(100);
bst.insert(130);
bst.insert(45);
bst.insert(146);
#finds smallest value
print(bst.getMinValue()):
#finds Largest value
print(bst.getMaxValue()):

bst.traverse():

bst = BinarySearchTree();
bst.insert("A");
bst.insert("C");
bst.insert("Z";
bst.insert("D");

bst.traverse():


bst.traverse();


bst.insert(100);
bst.insert(130);
bst.insert(45);
bst.insert(146);


bst.remove(146);

bst.remove(130);

#removing root node. 45 is the predecessor and will be swapped with the root node. Then 100 will be a leaf node, and will be removed	
bst.remove(100)	;