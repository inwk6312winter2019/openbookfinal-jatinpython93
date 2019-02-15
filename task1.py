import string

def funk(filename):
	hist = dict() 		 # Empty Dictionary created
	my_file = open(filename) # Opening the txt file 
	for line in hist:
		new_funk(line,hist)
	return hist

def new_funk(line,hist):
	line = line.replace("-" , " ")
	for word in line.split():
		word = word.strip(string.punctuation,string.whitespace)		#Removing the punctuation and whitespaces using String module
		word = word.lower()
		hist[word] = hist.get(word,0) + 1

my_book = funk(Book1.txt)
my_book2 = funk(Book2.txt)
my_book3 = funk(Book3.txt)

# The above program creates a file and returns a histogram 

# First task says to count unique no of words in the txt file

def unique_words(hist):
	return sum(list(hist.values()))			# returns the no of unique words from the histogram

