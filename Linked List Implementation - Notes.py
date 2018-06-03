#Linked Lists Notes

class Node (object): 
	def _init_(self,data):
	#data is data we would like to store in the node
	self.data = data;
	#reference or point to the next node - currently set to None. Next node references what it points to
	self.nextnode = None;
	
class LinkedList (object):
	def _init_(self):
	#create head of linked list; 1st node. Set equal to None
	#can access other nodes with next node reference
		self.head=None;
		self.size = 0
		
	def insertStart (self,data):
		self.size = self.size +1
		#First increase size of list.
		#Extenuate new node, which is the new data
		newNode = Node (data)
		
		
	if not self.head:
		self.head = newNode;
#if not null, set item to be the 1st linked in list. If this is the first node, set 
#self.head to be the new node. 
 
	else:
	#update pointer. New node points to original head. New head is now equal to new node	 
		newNode.nextnode=self.head
		self.head = newNode

# O(N) --> goes through each node			
	def remove(self, data):
# specify node  or data we would like to get rid of with "data"
		if self.head is None:
		#if already empty, return it...nothing in list
			return;
			
		self.size = self.size - 1;
		
		currentNode = self.head;
		previousNode = None;
		
		while currentNode.data != data:
			previousNode = currentNode;
			currentNode = currentNode.nextNode;
			
		if previousNode is None:
		#if previous node is None, it means we have to get rid of the head or root node or re-establish the 
		#the head of the list
			self.head = currentNode.nextNode;
		else:
		#if not head of the linked list, set previous node equal to the current node's next node (before deletion)
			previousNode.nextNode = currentNode.nextNode;			
				

# O(1)	
	def size1(self):
		return self.size;
		
	# O(N) not good !!!	
	def size2(self):
		
		actualNode = self.head;
		size = 0;
		#Goes through each node, calculating size
		#every insertion increase the size of the list
		while actualNode is not None:
			size+=1;
			actualNode = actualNode.nextNode;
			
		return size;	
		
#Lecture 14

# O(N)
	def insertEnd(self, data):
	
		self.size = self.size + 1;
		#new node is equal to node with the data
		newNode = Node(data);
		#starting off with first node.
		actualNode = self.head;
		#going through each Node's pointer (next node) and seeing if it's equal to None
		#if next node is equal to None then that's last node.
		
		while actualNode.nextNode is not None:
			#hop to next node
			actualNode = actualNode.nextNode;
			#Insert newNode at next node end when discovering that original next node is Null.
		actualNode.nextNode = newNode;
		
	def traverseList(self):
	
		actualNode = self.head;
		
		while actualNode is not None:
			print("%d " % actualNode.data);
			#go to next Node. Inserting at end takes a long time
			actualNode = actualNode.nextNode;

#creating a linked list		
linkedlist = LinkedList();

#head --> O(1)
linkedlist.insertStart(17);
#new head  --> O(1)
linkedlist.insertStart(19);
#new head  --> O(1)
linkedlist.insertStart(34)
#insert at  end --> O(N)
linkedlist.insertEnd(57);
#insert at  end --> O(N)
linkedlist.insertEnd(77);

linkedlist.traverseList();

#remove these items from the linkedlist
linkedlist.remove(17);
linkedlist.remove(34);
linkedlist.remove(77);
linkedlist.remove(19);

print(linkedlist.size1());		

		