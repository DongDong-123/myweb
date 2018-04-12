def pageShow(count, p):

	begin = p - 4
	end = p + 5
	if p > count - 5:
		begin = count - 9
		end = count 

	if p < 5:
		begin = 1
		end = 10

	if count < 10:
		begin = 1
		end = count

	for i in range(begin, end + 1):
		print(i)
