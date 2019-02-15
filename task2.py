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



