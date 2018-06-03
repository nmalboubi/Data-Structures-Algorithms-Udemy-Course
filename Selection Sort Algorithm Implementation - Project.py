#Write Selection Sort Algorithm; Ascending Order	

def selectionsort (array):
	for i in range(len(array) - 1):
	#identify index to be equal to i
		index = i
	#1 through length of array -1
		for j in range (i+1, len(array),1):	
			if array [j] < array [index]:
				#we find smallest item in that given array
				index = j
		if index != i: 
			temp1 = array[index]
			temp2 = array[i]
			array[index]=temp2
			array[i]=temp1
	return array
					
					
c = [-1,-3,-2,0]					
a = [5,2,1,7,6,8,8,0]	
b = [4,3,2,1,100,45,10,99,101,4.5]
print (selectionsort(a))				
print (selectionsort(b))
print (selectionsort(c))