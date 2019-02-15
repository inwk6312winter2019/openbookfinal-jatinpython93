# Creating a function and opening the books 

def my_funk():

	hist = dict()			# Creating an empty dictionary
	fp = open(Book1.txt)
	for line in fp:
		new_funk(line,hist)
	return hist			# reads the Book1

def my_funk2():
	hist = dict()
	fout = open(Book2.txt)
	for num in fout:
		new_funk2(num,hist)	# reads the Book2

def my_funk3():				# reading the Book3
	hist = dict()
	fin = open(Book3.txt)
	for letter in fin:
		new_funk3(letter,hist)


def new_funk(line,hist):			# Creating a file from the Book1
	for line in line.split():
		line = line.replace("-" , "")
		return hist[word] = hist.get(word,0) + 1

def new_funk2(num,hist):			# Creating a a file from the Book2
	for num in num.split():
		num = num.replace("-" , "")
		return hist[word] = hist.get(word,0) + 1

def new_funk3(letter,hist):			# creating a file from the Book3
	for letter in letter.split():
		letter = letter.replace("-" , "")
		return hist[word] = hist.get[word,0)+1
		
def top_words():				# Using If statement , traversing and comparint the msot 20 words from all the three book****
	result = new_funk()
	result_new = new_funk2()
	result_third = new_funk3()
	for x in result and y in result_new and z in result_third:
		if x[20] == y[20] == z[20]
			return dict(x,y,z)
		else:
			break
