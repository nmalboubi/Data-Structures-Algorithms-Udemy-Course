#Write Bubble Sort Algorithm; Ascending Order

def bubblesort (array):
	for i in range(len(array) - 1):
	#1 through length of array -1
			for j in range (0, len(array)-1-i,1):
				#compare individual arrays	
				if array [j] > array [j+1]:
					temp1 = array[j]
					temp2 = array[j+1]
					array[j]=temp2
					array[j+1]=temp1
	return array
					
					
					
a = [1,5,3,2,8,4,7]	
b = [4,3,2,1,100,45,10,99,101,4.5]
print (bubblesort(a))				
print (bubblesort(b))

