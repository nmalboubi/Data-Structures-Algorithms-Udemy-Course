#Dijkstra Algorithm Notes

import sys;
import heapq;

class Edge(object):

	def __init__(self, weight, startVertex, targetVertex):
		self.weight = weight;
		self.startVertex = startVertex;
		self.targetVertex = targetVertex;
		
class Node(object):

	def __init__(self, name):
	#assign string to every single node	
		self.name = name;
		self.visited = False;
		self.predecessor = None;
		self.adjacenciesList = [];
		self.minDistance = sys.maxsize;
		#every node will have min Distance. Min distance from start vertex
		
	def __cmp__(self, otherVertex):
		return self.cmp(self.minDistance, otherVertex.minDistance);
		#push nodes into the heap because we have to find in every iteration the node
		#according to variables above, we would like to select the minimum node
		#important because we are storing nodes in the heap data structure	
		#find the order
		#Find vertex with minimum distance value
		#Define less than method
		
		
	def __lt__(self, other):
		selfPriority = self.minDistance;
		otherPriority = other.minDistance;
		return selfPriority < otherPriority;
		#this is how we override cmp, because we would like to use heap to select  node with min distance because Dijkstra algorithm is greedy
		#going to visit node with min distance in every iteration
		#need to use heap because finding Min uses O(1) time complexity

class Algorithm(object):

	def calculateShortestPath(self, vertexList, startVertex):
		#rely on heappush method on the heap
		#this q is a heap; one dimensional array, list
		
		q = [];
		startVertex.minDistance = 0;
		heapq.heappush(q, startVertex);
		
		while q:
		
			actualVertex = heapq.heappop(q);
			#going to return with the vertex or node with min distance. If we keep pushing vertices, whenever we pop it will return node with min distance (FIFO)
			
			
			for edge in actualVertex.adjacenciesList:
			#need to iterate through the edges
				u = edge.startVertex;
				v = edge.targetVertex;
				newDistance = u.minDistance + edge.weight;
				
				if newDistance < v.minDistance:
				# it means we have found a shorter path
					v.predecessor = u;
					v.minDistance = newDistance;
					#now we have to update the heap
					heapq.heappush(q, v);
					
	def getShortestPathTo(self, targetVertex):
		print("Shortest path to vertex is: ", targetVertex.minDistance);
		#we can tell min distance from vertex A to vertex D
		
		node = targetVertex;
		
		while node is not None:
			print("%s " % node.name);
			node = node.predecessor;


#tests of all algorithms				
node1 = Node("A");
node2 = Node("B");
node3 = Node("C");
node4 = Node("D");
node5 = Node("E");
node6 = Node("F");
node7 = Node("G");
node8 = Node("H");

edge1 = Edge(5,node1,node2);
edge2 = Edge(8,node1,node8);
edge3 = Edge(9,node1,node5);
edge4 = Edge(15,node2,node4);
edge5 = Edge(12,node2,node3);
edge6 = Edge(4,node2,node8);
edge7 = Edge(7,node8,node3);
edge8 = Edge(6,node8,node6);
edge9 = Edge(5,node5,node8);
edge10 = Edge(4,node5,node6);
edge11 = Edge(20,node5,node7);
edge12 = Edge(1,node6,node3);
edge13 = Edge(13,node6,node7);
edge14 = Edge(3,node3,node4);
edge15 = Edge(11,node3,node7);
edge16 = Edge(9,node4,node7);

node1.adjacenciesList.append(edge1);
node1.adjacenciesList.append(edge2);
node1.adjacenciesList.append(edge3);
node2.adjacenciesList.append(edge4);
node2.adjacenciesList.append(edge5);
node2.adjacenciesList.append(edge6);
node8.adjacenciesList.append(edge7);
node8.adjacenciesList.append(edge8);
node5.adjacenciesList.append(edge9);
node5.adjacenciesList.append(edge10);
node5.adjacenciesList.append(edge11);
node6.adjacenciesList.append(edge12);
node6.adjacenciesList.append(edge13);
node3.adjacenciesList.append(edge14);
node3.adjacenciesList.append(edge15);
node4.adjacenciesList.append(edge16);


vertexList = (node1,node2,node3, node4, node5, node6, node7, node8);

algorithm = Algorithm();
algorithm.calculateShortestPath(vertexList, node1);
algorithm.getShortestPathTo(node7);
#25
#GCFEA

algorithm.getShortestPathTo(node4);
#17
#DCFEA
