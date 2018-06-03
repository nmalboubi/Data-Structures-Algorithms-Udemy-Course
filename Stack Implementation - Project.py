#Stack Implementation Project
class Stack:

	def __init__(self):
		self.stack = []
		
	def isEmpty(self):
	#if empty array it returns true. If not empty returns false. Boolean values
		return self.stack == []
		
	def push(self, data):
		self.stack.append(data)
		#keep appending the given item, which is data in this case, to the stack.
		
	def pop(self):
		#stack has a LIFO structure so last item in, is the first item out
		data = self.stack[-1]
		#returns the last item
		del self.stack[-1]
		return data
		
	def peek(self):
		return self.stack[-1]
			#return last item without removing the last item
			# structure remains the same
	def sizeStack(self):
		return len(self.stack)
		
stack = Stack()
stack.push(10)
stack.push(22)
stack.push(33)
#pushing values into the stack, and 33 is the last item in the stack, so if pop is called 33 is the first out
print(stack.sizeStack())
print("Popped: ", stack.pop())
print("Popped: ", stack.pop())
#33 and 22 popped out first
print(stack.sizeStack())
print("Peek:", stack.peek())
#peek will return 10, but size will remain the same so length of 1 is shown below
print(stack.sizeStack())