#Write Insertion Sort Algorithm; Ascending Order	

def insertionsort (array):
	for i in range(len(array)):
		j = i
		while j>0 and array[j-1] > array[j]:
			#consider j-1 and j>0 so we won't maniupulate array outside of the range
			temp1 = array[j]
			temp2 = array[j-1]
			array[j]=temp2
			array[j-1]=temp1
			j=j-1
	return array
					
					
c = [-1,-3,-2,0]					
a = [5,2,1,7,6,8,8,0]	
b = [4,3,2,1,100,45,10,99,101,4.5]
d = [1,5,3,8,10,100,4]
print (insertionsort(a))				
print (insertionsort(b))
print (insertionsort(c))
print (insertionsort(d))