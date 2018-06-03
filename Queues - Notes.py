#Queues Notes
#FIFO - first -> first, unlike stack	

class Queue:

	def __init__(self):
	#1 dimensional array that's empty	
		self.queue = []
		#1 dimensional array
		#queue is similar to stack
		
	def isEmpty(self):
	#check if empty
		return self.queue == []
		
	def enqueue(self, data):
		self.queue.append(data)
		#data is inserted in queue
		
	def dequeue(self):
		data = self.queue[0] # for stack it's -1
		del self.queue[0] #removes reference		
		return data
		
	def peek(self):
		return self.queue[0]
		
	def sizeQueue(self):
		return len(self.queue)
	
	
	#lots of algorithms rely on queue
queue = Queue()
queue.enqueue(110)
queue.enqueue(225)
queue.enqueue(359)
print(queue.sizeQueue())
print("Dequeue: ", queue.dequeue())
print("Dequeue: ", queue.dequeue())
print(queue.sizeQueue())