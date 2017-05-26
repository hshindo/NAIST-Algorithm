import time

def binary_search(list, key):
	low = 0
	high = len(list) - 1
	
	while low <= high:
		mid = (low + high) // 2
		if key < list[mid]:
			high = mid - 1
		elif key > list[mid]:
			low = mid + 1
		else:
			print 'key found'
			return
			
	print 'key not found'
				
t = time.clock()
binary_search([1, 2, 3, 4, 5, 6, 7], 1)
print 'time: ', time.clock() - t