#TST Notes
class Node(object):
	#assign character to every single node
	def __init__(self, character):
		self.character = character
		#left, middle, right are equal to none at beginning
		#each node is associated with a value of 0 in beginning
		self.leftNode = None
		self.middleNode = None
		self.rightNode = None
		self.value = 0
		
class TST(object):

	def __init__(self):
		self.rootNode = None
		
	def put(self,key,value):
	#we would like to start with 0 index of that key
		self.rootNode = self.putItem(self.rootNode, key, value, 0)
		
	def putItem(self, node, key, value, index):
		#this index is going to track that corrector that we are considering as far as the key is concerned	
		
		c = key[index]
		#if node doesn't exist, we have to extend it 
		if node == None:
			node = Node(c)
			
		if c < node.character:
		#character smaller go to left; we don't increment index, because we keep considering same character of the key. 
		#increment the index if we are able to insert that given value
			node.leftNode = self.putItem(node.leftNode, key, value, index)
		elif c > node.character:
			node.rightNode = self.putItem(node.rightNode, key, value, index)
			#indices start at 0; given character is equal to node character and we're not at end of key
		elif index < len(key) - 1:
		#increment the index value if we keep getting the middle node
			node.middleNode = self.putItem(node.middleNode, key, value, index+1)
		else:
			node.value = value
			#insert value here, since we're at end of key
		return node;
		
		#retrieve item; helper function
	def get(self, key):
	
		node = self.getItem(self.rootNode, key, 0)
		
		if node == None:
			return -1
			
		return node.value
	#looking for value so it's not included in argument
	def getItem(self, node, key, index):
			#if node is None, return None
		if node == None:
			return None
		
		c = key[index]
		#again DON'T INCREMENT INDEX
		if c < node.character:
			return self.getItem(node.leftNode, key, index)
		elif c > node.character:
			return self.getItem(node.rightNode, key, index)
		elif index < len(key) - 1:
			return self.getItem(node.middleNode, key, index+1)
		else:
			return node
			
if __name__ == "__main__":

	tst = TST()
	
	tst.put("apple",190)
	tst.put("orange",222)
	
	print( tst.get("orange") )
	#222
	
	print( tst.get("apple") )
	#190
	
	print( tst.get("nima") )
	#-1
	