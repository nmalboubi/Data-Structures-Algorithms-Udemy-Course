#Heaps Notes
class Heap(object):

	HEAP_SIZE = 10
	# inserting 10 items in the HEAP as an array
	def __init__(self):
		self.heap = [0]*Heap.HEAP_SIZE;
		#defines current position that points to the index of the actual item in the 1 dimensional array (heap)
		self.currentPosition = -1;
		
	def insert(self, item):
		#get item that we would like to insert (integers)
		if self.isFull():
		#if given heap is full we just return and print out the following:
			print("Heap is full..");
			return 
			#if Heap is not full
		self.currentPosition = self.currentPosition + 1
		self.heap[self.currentPosition] = item
		self.fixUp(self.currentPosition)
		#why? if we keep inserting items. after every insertion we need to check to seek if HEAP properties are violated
			#i.e., if inserted node is greater than root node, we need to switch 	
		
	def fixUp(self, index):
		#find the parent index. Child node is 2i + 1. Parent is reverse
		parentIndex = int((index-1)/2)
		
		#allows for the swapping off nodes, based on nodes
		while parentIndex >= 0 and self.heap[parentIndex] < self.heap[index]:
		#we know that this is root node, and maximum heap and we know that parent should be greater
		#create temporary variable for swapping
			temp = self.heap[index]
			self.heap[index] = self.heap[parentIndex]
			self.heap[parentIndex] = temp
			index=parentIndex
			#update the parent index here
			parentIndex = (int)((index-1)/2)
			
	def heapsort(self):
	#allows for the numerical ordering of integers or alphabetical ordering of strings and connectors
		for i in range(0,self.currentPosition+1):
		#root node is max value in heap. Here discussing max heap. GOing to implement fix down method, not the fix up method
		#don't consider sorted items. 
			temp = self.heap[0]
			print("%d " % temp)
			#print out sorted number
			#-i is important because we are considering fewer and fewer items
			self.heap[0] = self.heap[self.currentPosition-i]
			#this is how we swap the positions	
			self.heap[self.currentPosition-i] = temp
			self.fixDown(0,self.currentPosition-i-1)
			#crucial to consider fewer and fewer items
	def fixDown(self, index, upto):
#takes the start index and the end index
		while index <= upto:
		#follows formula
			leftChild = 2*index+1
			rightChild = 2*index+2
			#these are indices 	NOT VALUES	
			if leftChild < upto:
				childToSwap = None
				
				if rightChild > upto:
					childToSwap = leftChild
				else:
					if self.heap[leftChild] > self.heap[rightChild]:
						childToSwap = leftChild
						#Because we are looking for max heap, and would like to ensure that root node is the maximum
					else:
						childToSwap = rightChild
				# below is the case where we have to swap
				if self.heap[index] < self.heap[childToSwap]:
					temp = self.heap[index]
					self.heap[index] = self.heap[childToSwap]
					self.heap[childToSwap] = temp
				else:
					break
				
				index = childToSwap
			else:
				break;							
			
	def isFull(self):
	#returns boolean values. If heap is full return true
		if self.currentPosition == Heap.HEAP_SIZE:
			return True
		else:
			return False
			
			
if __name__ == "__main__":

	heap = Heap()
	heap.insert(9)
	heap.insert(-23)
	heap.insert(1)
	heap.insert(3)
	
	
	
	heap.insert(4)
	heap.insert(5)
	heap.insert(6)
	heap.insert(7)
	heap.insert(20)
	heap.insert(15)
	
	heap.heapsort()