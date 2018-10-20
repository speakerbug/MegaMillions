# File: megamillions.py
# Henry Saniuk, Jr.
# This script reads in a ticket file and a string of winning numbers
# and determins how much money you won in Mega Millions
#
# Command Line usage:
#   python megamillions.py <winning white balls> <winning yellow ball>

import sys

# Winning prize tables
prizes = {
'5,0': 1000000,
'4,1': 10000,
'4,0': 500,
'3,1': 200,
'3,0': 10,
'2,1': 10,
'1,1': 4,
'0,1': 2,
}

try:
	whiteBalls = str(sys.argv[1]).split(",")
	yellowBall = int(sys.argv[2])
	totalPrize = 0
	jackpotWon = False
	
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
			yellowBallMatched = '1'
			yellowBallMatchedString = "MATCHED"
		else:
			yellowBallMatched = '0'
			yellowBallMatchedString = "NOT MATCHED"
		print currentNumbers
		print 'White Balls Matched: ' + str(numbersMatched) + ' Yellow Ball: ' + yellowBallMatchedString
		if str(numbersMatched) + ',' + yellowBallMatched in prizes:
			print 'Winner'
			print '$' + str(prizes.get(str(numbersMatched) + ',' + yellowBallMatched, 0))
			totalPrize += prizes.get(str(numbersMatched) + ',' + yellowBallMatched, 0)
		elif numbersMatched == 5 and yellowBallMatched == '1':
			print 'JACKPOT'
			jackpotWon = True
		else:
			print 'Not a Winner'
	
	print '\nTotal won:'
	print '$' + str(totalPrize)
	print 
	if jackpotWon:
		print 'YOU WON THE JACKPOT!!!'
		print u"\U0001F911 \U0001F911 \U0001F911"
	else:
		print 'Sorry, you didn\'t win the jackpot :('
except IndexError:
	print 'Usage: python megamillions.py <winning white balls> <winning yellow ball>'
