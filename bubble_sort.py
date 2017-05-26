import time

def bubble_sort(list):
	n = len(list)
	for i in xrange(0, n):
		for j in xrange(0, n - i - 1):
			if list[j] > list[j + 1]:
				list[j], list[j + 1] = list[j + 1], list[j]
	print list
				
t = time.clock()
bubble_sort([9, 5, 4, 6, 2, 11, 7])
print 'time: ', time.clock() - t