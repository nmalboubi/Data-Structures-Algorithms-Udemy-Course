#BFS Implementation Project

#represents vertices and nodes in the given graph
class Node(object):

	#assign name to every single node
	def __init__(self, name):
		self.name = name;
		self.neighborList = [];
		self.explored = False;
		self.predecessorNode = None;
		#may not be used	
		
		#finds shortest path	
class BreadthFirstSearch(object):

	def bfsmethod(self, Nodestart):
		#nodestart is what node we're starting from
		#BFS uses queue as underlying abstract data type
		#use list because in python we can implement queue with help of list
		queue = [Nodestart];
		#have to set start node to be visited
		Nodestart.explored = True;
		
		# BFS -> queue      DFS --> stack BUT usually we implement it with recursion
		while queue:
			#pop node out of queue;FIFO structure so we need to pop first item inserted	
			currentNode = queue.pop(0);
			print("%s " % currentNode.name);
			
			for n in currentNode.neighborList:
				#consider if we have visited
				if not n.explored:
					n.explored = True;
					queue.append(n);
					#append node to end of queue
					#while loop iterates until queue is not empty
					
node1 = Node("X");
node2 = Node("Y");
node3 = Node("A");
node4 = Node("B");
node5 = Node("L");

node1.neighborList.append(node4);
node1.neighborList.append(node5);
node4.neighborList.append(node2);
node2.neighborList.append(node3);
#XBLYA
bfsmethod = BreadthFirstSearch();
bfsmethod.bfsmethod(node1);