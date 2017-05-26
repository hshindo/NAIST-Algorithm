def select_sort(list):
	n = len(list)
	for i in xrange(0, n):
		k = i
		for j in xrange(i+1, n):
			if list[j] < list[k]:
				k = j
		list[k], list[i] = list[i], list[k]
	print list
	
select_sort([9, 5, 4, 6, 2, 11, 7])