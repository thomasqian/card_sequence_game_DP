import random
from datetime import datetime as dt

MAX_VALUE = 50
LENGTH = 14
pStart = True
predict = True

seq = []
lookup = [[0 for x in range(LENGTH)] for x in range(LENGTH)]

def genSequence():
	#generate sequence of cards
	random.seed(dt.now())

	for i in range(LENGTH):
		val = random.randint(1, MAX_VALUE)
		while (val in seq): val = random.randint(1, MAX_VALUE)
		seq.append(val)

def printInstructions():
	print "Card Sequence Game!"
	print "Given a sequence of cards where you can only select from the end, "
	print "pick cards such that you maximize your total value."
	print "When it is your turn, type in your pick and press enter.\n"

def printSequence(a,b):
	print "Current Sequence: " + str(seq[a:b + 1])

def printScore(a,b):
	print "Score: Player-" + str(a) + " ; Computer-" + str(b)

def getOptimalStrategy():
	opt = [[0 for x in range(LENGTH)] for x in range(LENGTH)]

	for i in range(LENGTH):
		for j in range(LENGTH):
			if (i == j): 
				opt[i][j] = seq[i]
				lookup[i][j] = i
			elif (j - i == 1): 
				opt[i][j] = max(seq[i], seq[j])
				lookup[i][j] = (i if (opt[i][j] == seq[i]) else j)

	for a in range(LENGTH - 2):
		for j in range(a + 2, LENGTH):
			i = j - (2 + a)

			pickI = seq[i] + min(opt[i + 1][j - 1], opt[i + 2][j])
			pickJ = seq[j] + min(opt[i + 1][j - 1], opt[i][j - 2])
			opt[i][j] = max(pickI , pickJ)
			lookup[i][j] = (i if (opt[i][j] == pickI) else j)

	if (predict): print "Prediction: " + str(opt[0][LENGTH - 1]) + "\n"

def readChoice(a,b):
	choice = -1
	while (choice == -1):
		val = raw_input("Pick an end card: ")
		try:
			choice = int(val)
		except ValueError:
			print("That's not a valid integer!")
			continue
		if (choice != seq[a] and choice != seq[b]):
			if (choice in seq): 
				print("That's not an end card!")
			else:
				print("That's not even in the sequence... you blind?")
				print "Why don't you try {0} or {1}?".format(seq[a], seq[b])
			choice = -1
		else: choice = (a if (choice == seq[a]) else b)
	return choice

def main():
	genSequence()
	printInstructions()
	getOptimalStrategy()
	printSequence(0, LENGTH - 1)

	a = 0
	b = LENGTH - 1
	p1 = 0
	p2 = 0
	player = pStart
	choice = 0

	while (a <= b):
		if (player): choice = readChoice(a,b)
		else: choice = lookup[a][b]

		string = ("Player " if (player) else "Computer ")

		if (choice == a): 
			string += "chooses " + str(seq[a])
			a += 1
		elif (choice == b): 
			string += "chooses " + str(seq[b])
			b -= 1
		else: 
			print "error in lookup."
			break

		if (player): p1 += seq[choice]
		else: p2 += seq[choice]

		print string
		printScore(p1,p2)
		print
		if (a <= b): printSequence(a,b) 
		player = not(player)

	if (p1 > p2): print "Player wins!"
	elif (p2 > p1): print "Computer wins!"
	else: print "Tie!"
	printScore(p1,p2)

if __name__ == "__main__":
	main()