fout = open("access.log" , "r")			# Opening the accessing log file


log1_file = open("Get.txt" , "w") 		# Get file created 

log2_file = open("Post.txt" , "w")		# Post file created

log3_file = open("put.txt" , "w")		# Put file created

log4_fle = open("Delete.txt" , "w")		# Delete file created 

# Checking the conditions for GEt,Post,Put & delete and appending the log files 

for letter in fout:
	if letter == "GET":
		log1_file.append(letter)

	elif letter == "POST":
		log2_file.apend(letter)

	elif letter == "PUT":
		log3_file.append(letter)

	elif letter == "POST":
		log4_file.append(letter)

	else:

		break


def check_funk(log1_file,log2_file):			#taking the two log files as two parameters

	for num in log1_file an letter in log2_file:

		for num i range(20) and letter in range(20):

			if num[0] == letter[0]:
				num +=1
				letter +=1
			return num
			return letter
			else:
				print("Top twenty IP addresses not found \n")

