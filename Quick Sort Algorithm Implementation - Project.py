#Write Quick Sort Algorithm; Ascending Order	

def quicksort (array, low, high):
	if low >= high:
		return
		
	#partition array
	#select middle item in array
	piv_index = (low+high)//2
	#sort
	temp1 = array[piv_index]
	temp2 = array[high]
	array[piv_index]=temp2
	array[high]=temp1
	
	i = low
	#make sure all items smaller than piv, wil be on left; all items greater than piv, will be on the right
	for j in range(low,high,1):
		if array[j] <= array[high]:	
			#sort	
			temp3 = array[i]
			temp4=array[j]
			array[i]=temp4
			array[j]=temp3	
			i = i + 1
	#sort. Divide and conquer	
	temp5 = array[i]
	temp6 = array[high]
	array[i]=temp6
	array[high]=temp5
	#make sure to make i index of the piv
	piv_index=i
	
	#divide and conquer algorithm and that's why it can be implemented with recursive calls
	#partition with piv, creates threshold
	quicksort(array,low, piv_index-1)
	quicksort(array, piv_index+1,high)	

   
a = [-2,-1,0,1,0,-1,-2]
b= [-5,3,1,-10,-20,-30,-2,-7,0,1,-1,7,10,13,-13,7,-12]
quicksort(a,0,len(a)-1)
quicksort(b,0,len(b)-1)
print(a)
print(b)
