def make_sudoku(size):

	sudoku = []
	small = []
	copy = []
	k = 1
	num = -size - 1
	j = 0
	
	while k <= size**2:
		small.append(k)
		k += 1
 
	while j < size**2:
		i = 0
		num = size + num
		if j%size == 0:
			num += 1	
		while i < size**2:
			if (num + i) >= size**2:
				copy.append(small[i + num-size**2])
				num = num - size**2
			else:
				copy.append(small[i + num])
			i += 1
		sudoku.append(copy)
		copy = []
		j += 1
		
	return sudoku
		
