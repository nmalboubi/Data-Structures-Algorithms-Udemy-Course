#Merge Sort Algorithm Notes	

def merge_sort(nums):
    #recursive call, so we need to develop the base case first
	if len(nums) == 1:                                  
		return
	#generate middle index
	middle_index = len(nums) // 2
	
		#2 indices: left and right subarrays
	left_half = nums[:middle_index]
	right_half = nums[middle_index:]
	
	#call merge sort recursively on left and right subarrays
	merge_sort(left_half)
	merge_sort(right_half)
	
	#define 3 indices
	#tracks left subarray
	i = 0
	#tracks right subarray
	j = 0
	#track items in result array; this is why it's not an inplace algorithm
	k = 0
	
	while i<len(left_half) and j<len(right_half):
	#consider every item from left and right subarray
	#if item from left subarray is smaller than item from the right subarray, insert it into the nums array
		if left_half[i] < right_half[j]:
			
			nums[k] = left_half[i]
			i = i + 1
			#insert item from left subarray so we need to increment the index by 1
		else:
			nums[k] = right_half[j]
			j = j + 1
			#insert item from right subarray so we need to increment the index by 1
		k = k + 1
			#tracks result array	
	#checks to see that items are remaining in left subarray to add to result array	
	while i<len(left_half):
		nums[k] = left_half[i]
		k = k + 1
		i = i + 1	

	#checks to see that items are remaining in right subarray to add to result array
	while j<len(right_half):
		nums[k] = right_half[j]
		k = k + 1
		j = j + 1
	
if __name__ == "__main__":
   
   nums = [-3,-2,-1,1,2,1,0,-1,-2,-3]
   merge_sort(nums)
   print(nums)
  