import time

def quick_sort(list, left, right):
	if left >= right: return
	pivot = list[(left + right) // 2]
	i, j = left, right
	while True:
		while pivot > list[i]: i += 1
		while pivot < list[j]: j -= 1
		if i >= j: break
		else:
			list[i], list[j] = list[j], list[i]
			i, j = i + 1, j - 1
	quick_sort(list, left, i - 1)
	quick_sort(list, j + 1, right)
	
t = time.clock()
list = [9, 5, 4, 6, 2, 11, 7, -1, 4, 3]
quick_sort(list, 0, len(list) - 1)
print list
print 'time: ', time.clock() - t