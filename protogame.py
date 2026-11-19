def toContinue():
	input("Return to continue...")
def toLoop():
	input("Return to restart...")
def isFloat(value):
	if value.replace(".","",1).replace("-","",1).isdigit():
		return True
	return False
def inputInteger(error):
	number = input()
	while not isFloat(number):
		number = input(error)
	return int(number)
def inputString(options, error):
	entry = input().strip()
	while not entry in options:
		entry = input(error).strip().lower()
	return entry
def inputFile(error):
	while True:
		try:
			filename = open(input())
			return filename
		except FileNotFoundError:
			filename = open(input(error))
def filetoOneVarList(fileInQuestion):
	list = []
	for line in fileInQuestion:
		list.append(line.strip("\n"))
	return list
def filetoTwoVarList(fileInQuestion, splittingItem):
	list = []
	for line in fileInQuestion:
		list.append(line.split(splittingItem).strip("\n"))
	return list
def leninput(string):
	if len(input(string)) > 0:
		return True
	return False
def randomize(deck):
	import random
	newdeck = []
	for iteration in range(len(deck[:])):
		newdeck.append(deck.pop(random.randint(0,len(deck))))
	return newdeck
def inputBoard(length, name):
	board = input().strip().lower()
	budgeting = False
	betabet = False
	duplicate = False
	if not board.isalpha():
		betabet = True
	if len(board) > length:
		budgeting = True
	for index in range(len(board)-1):
		for pivot in board[index+1:]:
			if board[index] == board[pivot]:
				duplicate = True
	if budgeting and duplicate and betabet:
		print("What a wondeful showing of complete disregard for laws and regulations, ",name, end=", ")
		print("You somehow brought all three de facto penalties upon yourself.\nWell, here's your second try to generate a board with a proper length, characters and variability: ", end="")
		board = input.strip().lower()
	elif (budgeting and duplicate) or (budgeting and betabet) or (duplicate and betabet):
		print("Double strike, ",name, end=", ")
		print("You hit yourself with two out of three de facto penalties. Better be sure to avoid such magic for the rest of the game.\nHere's your second try to generate a board that won't screw you over: ", end="")
		board = input().strip().lower()
	elif budgeting:
		print("Dear", name, end=", ")
		print("You have been charged with the Budgeting penalty...attempting to place too many letters into your board, the excess of which will be cut off.\nHere's your second try to generate a board that actually considered its vital firsts: ", end="")
		board = input().strip().lower()
	elif betabet:
		print("Dear", name, end=", ")
		print("You have been charged with the Betabet penalty...attempting to place a letter which is not Latin nor alphanumerical.\nHere's your second try to generate a board maximizing its useful element: ", end="")
		board = input().strip().lower()
	elif duplicate:
		print("Dear", name, end=", ")
		print("You have been charged with the Duplicate penalty...putting in a letter more than once because you probably didn't read the Readme.\nHere's your second try to generate a board minimizing redundancy: ", end="")
		board = input().strip().lower()
	else:
		pass
	return board
def wordValue(n,e,inGame):
	value = e * n + e * (n/2) * (n - 1)
	if inGame:
		return value - int(e/2)
	else:
		return value

def main():
	import random
	alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'y', 'v', 'w', 'x', 'y', 'z']
	playerInfo = []
	multiplayer = False
	firstDif = False
	secondDif = False
	thirdDif = False
	fourthDif = False
	fifthDif = False
	sixthDif = False
	base = 0
	boardScope = 0
	playerScope = 0
	rounds = 0
	copyright = []
	print("Welcome to the game!\nFor binary questions, type and return anything to affirm; type and return nothing to deny.")
	if not leninput("First question: have you read the readme? "):
		multiplayer = True
		return "GO AND READ IT!" * 3
	if leninput("Second question: is this going to be a multiplayer game?"):
		print("Therefore, do we have two, eight or in-between players: [input the number of players ready to play]: ", end="")
		error = "This is why we read the readme and understand it folks; an integer from two to eight inclusive please: "
		playerScope = inputInteger(error)
		while playerScope < 2 or playerScope > 8:
			print(error)
			playerScope = inputInteger(error)
		print("Now let us get their names...")
		for iteration in range(playerScope):
			serial = iteration + 1
			if serial == 1:
				ordinal = serial + "st"
			elif serial == 2:
				ordinal = serial + "nd"
			elif serial == 3:
				ordinal = serial + "rd"
			else:
				ordinal = serial + "th"
			playerInfo.extend([input("And the name of the",ordinal,"player is: ")])
			playerInfo[iteration].append("")
			playerInfo[iteration].append(0)
		print("Names have been loaded into the list (just a little bit of developer jargon for you)...")
		toContinue()
	else:
		playerInfo.append(input("What is your name, solo player? "))
		playerInfo.append("")
		playerInfo.append(0)
	toContinue()
	while not (firstDif or secondDif or thirdDif or fourthDif or fifthDif or sixthDif):
		if leninput("Third question: are we choosing the first difficulty?"):
			firstDif = True
			base = 3
			boardScope = 7
		elif leninput("What about the second difficulty?"):
			secondDif = True
			base = 3
			boardScope = 8
		elif leninput("...third difficulty?"):
			thirdDif = True
			base = 4
			boardScope = 9
		elif leninput("...fourth difficulty?"):
			fourthDif = True
			base = 5
			boardScope = 7
		elif leninput("...fifth difficulty?"):
			fifthDif = True
			base = 6
			boardScope = 8
		else:
			if not leninput("The sixth difficulty will be de facto chosen unless we receive a decision to loop through the difficulties once again until a decision is made...are we looping?"):
				sixthDif = True
				base = 7
				boardScope = 9
	toContinue()
	if leninput("Fourth question: are we leaving the generation of the boards and the determination of the number of rounds to automation? "):
		rounds = random.randint(10,31)
		print("Therefore, we will be playing",rounds,"rounds.\nDo you accept this number? [Anything to accept; nothing to reject]", end="")
		if not leninput():
			return "If you knew you had a specific number in mind; why didn't you pick manual? No problem, be sure to be manual with this new program run."
		if multiplayer:
			print("If you managed to dodge that trap to a forceful restart; we can move on and give each player their boards.\nDon't get apprehensive about attempting to remember them or have them written down somewhere; the system will keep every players' board displayed as it is their turn.")
			for row in range(playerScope):
				alphabetDealings = randomize(alphabet)
				board = ""
				for letter in alphabetDealings[0:(boardScope - 1)]:
					board += letter
				playerInfo[row].append(board)
				print("Dear",playerInfo[row][0]) 
				print("You have these board of letters:",playerInfo[row][1],"recalling that the first is the required and the rest are the optional.")
				toContinue()
		else:
			print("If you managed to dodge that trap to a forceful restart; we can move on and give you your board.\nDon't get apprehensive about attempting to remember them or have them written down somewhere; the system will keep your board displayed at all times.")
			alphabetDealings = randomize(alphabet)
			board = ""
			for letter in alphabetDealings[0:(boardScope - 1)]:
				board += letter
			playerInfo.append(board)
			print("Dear",playerInfo[0], end=", ")
			print("This is your board: ",playerInfo[1],"recalling that the first is the required and the rest are the optional.")
	else:
		print("**Manual controls selected**\nFirst, the number of rounds: ", end="")
		rounds = inputInteger("I believe we should be getting a positive number; please endeavour to input a number of rounds that is actually a number of rounds: ")
		if not leninput("Are you sure about these number of rounds? [Anything to affirm; nothing to deny]"):
			return "Then restart the game and be sure to enter a number of rounds you actually want\nWhoever is controlling the general inputs; you really need to be more assertive of your options if you're going to do well in this game."	
		if multiplayer:
			print("If you managed to dodge that trap to a forceful restart; we can move on and get each of the players' board.\nRemember that the first letter given will be the requirement and the rest shall be optional.\nAnd don't get apprehensive about attempting to remember them or have them written down somewhere; the system will keep every players' board displayed as it is their turn.")
			for row in range(playerScope):
				print("Now let us get the board of", playerInfo[row][0], end=": ")
				playerInfo[row].append(inputBoard(boardScope, playerInfo[row][0]))
				toContinue()
		else:
			print("If you managed to dodge that trap to a forceful restart; we can move on and get your board.\nRemeber that the first letter you give will be your requirements and the rest shall be optional.\nDon't get apprehensive about attempting to remember them or have them written down somewhere; the system will keep your board displayed at all times.\nNow please solemnly enter the letters: ", end="")
			playerInfo.append(inputBoard(boardScope, playerInfo[0]))
			toContinue()
		
	soloVictory = rounds * (wordValue(boardScope, base, False))
	print("Now, let us begin!")
	if not multiplayer:
		print(playerInfo[0], end="! ")
		print("Good luck! You will need", soloVictory, "points to win. It's going to be a tough one so make sure you have good affinity with this language.")
while True:
	main()
	toLoop()