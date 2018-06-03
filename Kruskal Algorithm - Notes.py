#Kruskal Algorithm Notes
class Vertex(object):
#assign name to every single vertex
	def __init__(self, name):
		self.name = name;
		#assign node to every single vertex
		self.node = None; # !!!!
		#assign node to every single disjoint set in the graph
		#merge starting and ending vertex together if they are in different sets
class Node(object):
#represents disjoint sets

	def __init__(self, height, nodeId, parentNode):
		#height of disjoint set
		self.height = height;
		self.nodeId = nodeId;
		self.parentNode = parentNode;
		
class Edge(object):
	#represents the concrete graph edge
	def __init__(self, weight, startVertex, targetVertex):
	#assign 2 vertices: start and end vertex
		self.weight = weight;
		self.startVertex = startVertex;
		self.targetVertex = targetVertex;
		#define comparator
		
	def __cmp__(self, otherEdge):
		
		return self.cmp(self.weight, otherEdge.weight);
		
	def __lt__(self, other):
		selfPriority = self.weight;
		otherPriority = other.weight;
		return selfPriority < otherPriority;
		
class DisjointSet(object):
#nodes will start off in disjoint set
	def __init__(self, vertexList):
		self.vertexList = vertexList;
		#will contain root of disjoint sets. Will have has as many as number of vertices in the graph in beginning
		self.rootNodes = [];
		self.nodeCount = 0;
		#count how many nodes we have in the beginning
		#count how many sets we have in the beginning
		#every disjoint set is composed of nodes
		self.setCount = 0;
		self.makeSets(vertexList);
		
		
	def find(self, node):
	
		currentNode = node;
		
		while currentNode.parentNode is not None:
		#find root node because root will represent the whole disjoint set
		#we know parent node can't be the root node in this case
			currentNode = currentNode.parentNode;
			
		root = currentNode;
		#initialize root to be equal to current node; would like to make path compression	
		currentNode = node;
		
		while currentNode is not root:
		#compress the path
		#temp will be current node that parent node
		#if we have the root node, make sure to compress the path
			temp = currentNode.parentNode;
			currentNode.parentNode = root;
			currentNode = temp;
			#swap temp and current
			
		return root.nodeId;
		#differentiate the disjoint sets based on node id's.
		#will allow for finding nodes faster	
	
	def merge(self, node1, node2):
	#will take node1 and node 2 and calculate the index
	
		index1 = self.find(node1);
		index2 = self.find(node2);
		
		if index1 == index2:
			return;  # they are in the same set. So no merging because they're in the same set
			
			#calc root nodes for all of them
		root1 = self.rootNodes[index1];
		root2 = self.rootNodes[index2];
		#keep appending the smaller tree to the greater tree
		if root1.height < root2.height:
		#append root 1 to root 2
			root1.parentNode = root2;
		elif root1.height > root2.height:
		#append root 2 to root 1
			root2.parentNode = root1;
		else:
		#same size; append root 2 to root 1
			root2.parentNode = root1;
			root1.height = root1.height + 1;
		#accoridng to height parameter, can decide what tree to link to the other
		#increment height parameter
	def makeSets(self, vertexList):
		#has same number of vertices as the original graph, so we're going to assign a single node to every single vertex
		for v in vertexList:
			self.makeSet(v);
			
	def makeSet(self, vertex):
		#going to iterate through vertices and call this method on every single vertex
		#node is equal to new node
		node = Node(0, len(self.rootNodes),None);
		#nodeid is length of root nodes
		#parent node is initialized to be none
		#0 is height
		vertex.node = node;
		self.rootNodes.append(node);
		self.setCount = self.setCount + 1;
		#increment the node count
		self.nodeCount = self.nodeCount + 1;
		
class KruskalAlgorithm(object):

	def spanningTree(self, vertexList, edgeList):
	#going to get vertex list and an edge list
	#iterate through all edges 
	
		disjointSet = DisjointSet(vertexList);
		#specify vertex list; will construct disjoint sets according to this list
		#disjoint set will assign a node to every single vertex
		spanningTree = [];
		#empty list in beginning
		
		edgeList.sort();
		#edge list that will contain edges; according to edge weights we would like to sort it in ascending order	
		
		for edge in edgeList:
		
			u = edge.startVertex;
			v = edge.targetVertex;
			
			if disjointSet.find(u.node) is not disjointSet.find(v.node):
			#means they are in different disjoint sets; can include that edge in the spanning tree
				spanningTree.append(edge);
				disjointSet.merge(u.node, v.node);
				
		for edge in spanningTree:
		#iterate through spanning tree; print out edges
			print(edge.startVertex.name," - ", edge.targetVertex.name);
			
vertex1 = Vertex("a");
vertex2 = Vertex("b");
vertex3 = Vertex("c");
vertex4 = Vertex("d");
vertex5 = Vertex("e");
vertex6 = Vertex("f");
vertex7 = Vertex("g");

edge1 = Edge(2,vertex1,vertex2);
edge2 = Edge(6,vertex1,vertex3);
edge3 = Edge(5,vertex1,vertex5);
edge4 = Edge(10,vertex1,vertex6);
edge5 = Edge(3,vertex2,vertex4);
edge6 = Edge(3,vertex2,vertex5);
edge7 = Edge(1,vertex3,vertex4);
edge8 = Edge(2,vertex3,vertex6);
edge9 = Edge(4,vertex4,vertex5);
edge10 = Edge(5,vertex4,vertex7);
edge11 = Edge(5,vertex6,vertex7);


vertexList = [];
vertexList.append(vertex1);
vertexList.append(vertex2);
vertexList.append(vertex3);
vertexList.append(vertex4);
vertexList.append(vertex5);
vertexList.append(vertex6);
vertexList.append(vertex7);

edgeList = [];
edgeList.append(edge1);
edgeList.append(edge2);
edgeList.append(edge3);
edgeList.append(edge4);
edgeList.append(edge5);
edgeList.append(edge6);
edgeList.append(edge7);
edgeList.append(edge8);
edgeList.append(edge9);
edgeList.append(edge10);
edgeList.append(edge11);

algorithm = KruskalAlgorithm();
algorithm.spanningTree(vertexList, edgeList);			
	


