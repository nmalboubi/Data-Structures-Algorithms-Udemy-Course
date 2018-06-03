#Prims-Jarnik Notes

import heapq;
#relies on heaps

class Vertex(object):

	def __init__(self, name):
		self.name = name;
		self.visited = False;
		#checks to see if we have visited node or not
		self.predecessor = None;
		self.adjacenciesList = [];
		
	def __str__(self):
		return self.name;
		
class Edge(object):

	def __init__(self, weight, startVertex, targetVertex):
		self.weight = weight;
		self.startVertex = startVertex;
		self.targetVertex = targetVertex;
		
	def __cmp__(self, otherEdge):
		return self.cmp(self.weight, otherEdge.weight);
		#store edges in the heap; need to tell heap  that according to weight we would like to compare the edges, not vertices
		
	def __lt__(self, other):
	#other  = other edge
		selfPriority = self.weight;
		otherPriority = other.weight;
		#other weight
		return selfPriority < otherPriority;
	
	
class PrimsJarnik(object):

	def __init__(self, unvisitedList):
	
		self.unvisitedList = unvisitedList;
		self.spanningTree = [];
		self.edgeHeap = [];
		#use list as heap
		self.fullCost = 0;
		
	def calculateSpanningTree(self, vertex):
	
		self.unvisitedList.remove(vertex);
		#define starting vertex
		
		while self.unvisitedList:
		#while not empty, iterate through edges
			for edge in vertex.adjacenciesList:
			#adjacenciesList stores the edges
				if edge.targetVertex in self.unvisitedList:
				#if the edge target vertex is in unvisited list and we haven't considered it so far; then we have to push it to the heap
					heapq.heappush(self.edgeHeap, edge);
					
			minEdge = heapq.heappop(self.edgeHeap);
			#this is how we get edge with min weight
			#we push every edge that is necessary on to heap; then we get item with min edge weight; we then add to spanning tree
			
			self.spanningTree.append(minEdge);
			#print out that edge was added
			print("Edge added to spanning tree: %s - %s" % (minEdge.startVertex.name, minEdge.targetVertex.name));
			self.fullCost = self.fullCost + minEdge.weight;
			
			vertex = minEdge.targetVertex;   
			self.unvisitedList.remove(vertex);
			#final step to remove it from the invisited vertex list

	def getSpanningTree(self):
		return self.spanningTree;


node1 = Vertex("A");
node2 = Vertex("B");
node3 = Vertex("C");

edge1 = Edge(100,node1,node2);
edge2 = Edge(100,node2,node1);
edge3 = Edge(1000,node1,node3);
edge4 = Edge(1000,node3,node1);
edge5 = Edge(0.01,node3,node2);
edge6 = Edge(0.01,node2,node3);

node1.adjacenciesList.append(edge1);
node1.adjacenciesList.append(edge3);
node2.adjacenciesList.append(edge2);
node2.adjacenciesList.append(edge6);
node3.adjacenciesList.append(edge4);
node3.adjacenciesList.append(edge5);

unvisitedList = [];
unvisitedList.append(node1);
unvisitedList.append(node2);
unvisitedList.append(node3);

algorithm = PrimsJarnik(unvisitedList);
algorithm.calculateSpanningTree(node2);