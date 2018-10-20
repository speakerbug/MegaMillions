# File: megamillions.py
# Henry Saniuk, Jr.
# This script reads in a ticket file and a string of winning numbers
# and determins how much money you won in Mega Millions
#
# Command Line usage:
#   python megamillions.py <winning white balls> <winning yellow ball>

import sys

try:
	whiteBalls = str(sys.argv[1]).split(",")
	yellowBall = int(sys.argv[2])
	
	# Open the tickets file and read/parse it
	with open('tickets.txt','r') as f:
	    	seq_data = f.readlines()
    		for i in range(len(seq_data)):
        		seq_data[i] = seq_data[i].rstrip()
	#loop through your numbers to see if any won
	for i in range(len(seq_data)):
		currentNumbers = seq_data[i].split(",")
		numbersMatched = 0
		for n in range(len(currentNumbers)-1):
			if currentNumbers[n] in whiteBalls:
				numbersMatched = numbersMatched + 1
		if int(currentNumbers[len(currentNumbers)-1]) == yellowBall:
			yellowBallMatched = "MATCHED"
		else:
			yellowBallMatched = "NOT MATCHED"
		print currentNumbers
		print 'White Balls Matched: ' + str(numbersMatched) + ' Yellow Ball: ' + yellowBallMatched

except IndexError:
	print 'Usage: python megamillions.py <winning white balls> <winning yellow ball>'
