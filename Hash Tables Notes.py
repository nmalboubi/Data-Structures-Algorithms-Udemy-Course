#Hash Tables Notes
class HashTable(object):

	def __init__(self):
		self.size = 10
		self.keys = [None] * self.size
		self.values = [None] * self.size
		#underlying data structure for dictionary 
		#one dimensional array since we can achieve O(1) complexity, 
		#whether we insert or retrieve data because of random excess 
		#features of arrays
			
		#put method is going to take key and value (data) and insert it into the associative array	
	def put(self, key, data):
		#take has function and generate array index
		index = self.hashfunction(key)
		
		# not None -> it is a collision !!!
		#mapping two keys to same slot = collision - not good
			#use open addressing instead of chaining: Linear probing
		while self.keys[index] is not None:	
		#while that given array with that index is not empty; the hash function has
		#already generated a key for that given slot. In this case we have to find another empty
		#slot
			if self.keys[index] == key:
				#if key has already been inserted in the data structure
				self.values[index] = data # update
				#override old value with the new one
				return
				
			# rehash try to find another slot; generate the next index, by incrementing by 1
			#algorithm will generate next slot and see if it's empty.
			#if not empty it  will increment another slot (+1)
			#keep generating indices until we bump into an empty array slot
			#if we bump into empty array index, we just insert key value pair into that location
			index = (index+1)%self.size

		# insert
		self.keys[index] = key
		self.values[index] = data
	
	def get(self,key):
		
		index = self.hashfunction(key)
		
		while self.keys[index] is not None:
			if self.keys[index] == key:
				return self.values[index]
			#maybe there's collision by insertion so we need to shift the indices
			#if we go through all items present, and it's not there, we return none
			index = (index+1)%self.size
		
		# it means the key is not present in the associative array
		return None

	def hashfunction(self, key): 
	
	#hash function is going to get a key, where the key is the string, "100", "Kevin"
		#transform this key into array indices
	
		sum = 0
		#hash function will get key; iterate through every corrector of the key
		#transform to ascii: a-> 97, b->98, etc
		#transform correctors into integers
		for pos in range(len(key)):
			sum = sum + ord(key[pos])
		#use modular operator to limit the size of array if greater than 10
		return sum%self.size

if __name__ == "__main__":

	table =HashTable()
	
	table.put("apple",10)
	table.put("orange",20)
	table.put("car",30)
	table.put("table",40)
	
	print(table.get("cara"))
	#None
	print(table.get("car"))
	#30
	print(table.get("orange"))
	#20
	print(table.get("apple"))
	#10
