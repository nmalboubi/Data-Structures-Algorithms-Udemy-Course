#DFS Implementation Project
class Node(object):

	#assign name to every single node
	def __init__(self, name):
		self.name = name;
		self.neighborList = [];
		self.explored = False;
		
class DepthFirstSearch(object): # BFS -> queue + layer by layer algorithm   DFS -> stack + goes as deep as possible into the tree

	def dfsmethod(self, node):
	
		node.explored = True;
		#recursive manner; use operating system stack. Don't explicitly need to define stack here because we've implemented in a recursive manner	
		print("%s " % node.name);
		
		for n in node.neighborList:
			if not n.explored:
				self.dfsmethod(n);
		
	
node1 = Node("X");
node2 = Node("Y");
node3 = Node("A");
node4 = Node("B");
node5 = Node("L");		
	
node1.neighborList.append(node4);
node1.neighborList.append(node5);
node4.neighborList.append(node2);
node2.neighborList.append(node3);	
#XBAYL

dfsmethod = DepthFirstSearch();
dfsmethod.dfsmethod(node1);

