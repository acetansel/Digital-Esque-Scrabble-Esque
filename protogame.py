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
		return False
	return True
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
			if board[index] == pivot:
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
def nativeWord(generate,data):
	for letter in generate:
		if letter in data[1]:
			return True
	return False
def headedWord(generate,data):
	for letter in generate:
		if data[1][0] == letter:
			return True
	return False
def inputWord(dict, hist, base, data, multiplayer):
	generate = input().strip().lower()
	offences = []
	penalty = 0
	if not generate.isalpha():
		offences.append("the capital offence of AntiLanguage")
		penalty += base ** 2 * 5
	if not generate in dict:
		offences.append("the second offence of AntiEnglish")
		penalty += base ** 2 * 4
	if generate in hist:
		offences.append("the third offence of Plagiarism")
		penalty += base ** 2 * 3
	if not headedWord(generate, data):
		offences.append("the fourth offence of Headless")
		penalty += base ** 2 * 2
	if not nativeWord(generate, data):
		offences.append("the sixth offence of Foreign")
		penalty += base ** 2
	if len(generate) < base:
		offences.append("the seventh offence of Stump")
	if offences:
		print("You have committed", len(offences), "offences being ", end="")
		for offence in offences[:-2]:
			print(offence, end=", ")
		print("and", offences[-1], end=".\n")
		print("With all of this, a penalty of", penalty, "has been accumulated and removed from your score, reducing it to", end=" ")
		data[2] -= penalty
		print(data[2], end="! ")
		if multiplayer:
			print("Hey", data[0], end=", ")
			print("you might want to get serious if you're going to beat your foes.")
		else:
			print("Hey", data[0], end=", ")
			print("you might want to get serious if you're going to win this game.")
	else:
		print("Treasure in; Treasure Out!\nA great word generation valued at", wordValue(len(generate), base, True))
		data[2] += wordValue(len(generate), base, True) 
		print("Keep this up", data[0], "and you may have a chance with this new score of", data[2])
		hist.append(generate)
def main(dictionary):
	import random
	alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'y', 'v', 'w', 'x', 'y', 'z']
	history = []
	singlePlayer = []
	multiPlayer = []
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
	print("Welcome to the game!")
	if not leninput("First question: have you read the readme?\n\tType and return nothing to affirm; type and return anything to deny..."):
		print("GO AND READ IT!\nSeriously...this code is very vague in instruction becaues the meat of all of them are in the readme so you will do yourself a service in becoming familiar with it.")
		return None
	if leninput("Second question: is this going to be a multiplayer game?\n\tType and return nothing to affirm; type and return anything to deny..."):
		print("Therefore, from two to eight, how many players do we have: [input the number of players ready to play]: ", end="")
		error = "This is why we read the readme and understand it folks; an integer from two to eight inclusive please: "
		playerScope = inputInteger(error)
		while playerScope < 2 or playerScope > 8:
			print(error)
			playerScope = inputInteger(error)
		print("Now let us get their names...")
		for iteration in range(playerScope):
			serial = iteration + 1
			if serial == 1:
				ordinal = str(serial) + "st"
			elif serial == 2:
				ordinal = str(serial) + "nd"
			elif serial == 3:
				ordinal = str(serial) + "rd"
			else:
				ordinal = serial + "th"
			print("And the name of the",ordinal,"player is: ",end="")
			name = input()
			board = ""
			score = 0
			multiPlayer.extend([name,board,score])
		print("Names have been loaded into the list (just a little bit of developer jargon for you)...")
		toContinue()
	else:
		singlePlayer.append(input("What is your name, solo player? "))
		singlePlayer.append("")
		singlePlayer.append(0)
	toContinue()
	while not (firstDif or secondDif or thirdDif or fourthDif or fifthDif or sixthDif):
		if leninput("Third question: are we choosing the first difficulty?\n\tType and return nothing to affirm; type and return anything to deny..."):
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
			if not leninput("The sixth difficulty will be de facto chosen unless we receive a decision to loop through the difficulties once again until a decision is made...well?\n\tType and return nothing to affirm; type and return anything to deny..."):
				sixthDif = True
				base = 7
				boardScope = 9
	toContinue()
	if leninput("Fourth question: are we leaving the generation of the boards and the determination of the number of rounds to automation?\n\tType and return nothing to affirm; type and return anything to deny..."):
		rounds = random.randint(10,31)
		print("Therefore, we will be playing",rounds,"rounds.\nDo you accept this number?\n\tType and return nothing to affirm; type and return anything to deny...", end="")
		if not leninput():
			print("If you knew you had a specific number in mind; why didn't you pick manual? No problem, be sure to be manual with this new program run.")
			return None
		if multiPlayer:
			print("If you managed to dodge that trap to a forceful restart; we can move on and give each player their boards.\nDon't get apprehensive about attempting to remember them or have them written down somewhere; the system will keep every players' board displayed as it is their turn.")
			for row in multiPlayer:
				alphabetDealings = randomize(alphabet)
				for letter in alphabetDealings[:(boardScope - 1)]:
					row[1] += letter
				print("Dear",row[0]) 
				print("You have these board of letters:",row[1],"recalling that the first is the required and the rest are the optional.")
				toContinue()
		else:
			print("If you managed to dodge that trap to a forceful restart; we can move on and give you your board.\nDon't get apprehensive about attempting to remember them or have them written down somewhere; the system will keep your board displayed at all times.")
			alphabetDealings = randomize(alphabet)
			for letter in alphabetDealings[:(boardScope - 1)]:
				singlePlayer[1] += letter
			print("Dear",singlePlayer[0], end=", ")
			print("This is your board: ",singlePlayer[1],"recalling that the first is the required and the rest are the optional.")
	else:
		print("**Manual controls selected**\nFirst, the number of rounds: ", end="")
		rounds = inputInteger("I believe we should be getting a positive number; please endeavour to input a number of rounds that is actually a number of rounds: ")
		if not leninput("Are you sure about these number of rounds?\n\tType and return nothing to affirm; type and return anything to deny..."):
			print("Then restart the game and be sure to enter a number of rounds you actually want\nWhoever is controlling the general inputs; you really need to be more assertive of your options if you're going to do well in this game.")
			return None
		if multiPlayer:
			print("If you managed to dodge that trap to a forceful restart; we can move on and get each of the players' board.\nRemember that the first letter given will be the requirement and the rest shall be optional.\nAnd don't get apprehensive about attempting to remember them or have them written down somewhere; the system will keep every players' board displayed as it is their turn.")
			for row in multiPlayer:
				print("Now let us get the board of", row[0], end=": ")
				row[1] += inputBoard(boardScope, row[0])
		else:
			print("If you managed to dodge that trap to a forceful restart; we can move on and get your board.\nRemeber that the first letter you give will be your requirements and the rest shall be optional.\nDon't get apprehensive about attempting to remember them or have them written down somewhere; the system will keep your board displayed at all times.\nNow please solemnly enter the letters: ", end="")
			singlePlayer[1] += inputBoard(boardScope, singlePlayer[0])
		toContinue()
	soloVictory = rounds * (wordValue(boardScope, base, False))
	print("Now, let us begin!")
	if singlePlayer:
		print(singlePlayer[0], end="! ")
		print("Good luck! You will need", soloVictory, "points to win. It's going to be a tough one so make sure you have good affinity with this language.")
		toContinue()
		for cycle in range(rounds-1):
			print("ROUND", str(cycle), "... GO!\nGenerate a word...ANY word...from the letters [",singlePlayer[1],"] to bolster your score of [",singlePlayer[2],"]: ", end="")
			inputWord(dictionary, history, base, singlePlayer, False)
		print("FINAL ROUND ... LET US BRING OUT ... THE SUPERSTAR ... OR THE SUPERFLOP!\nGenerate a word...ANY word...from the letters [",singlePlayer[1],"] to make the final bolster (or atrophy) for your score of [",singlePlayer[2],"]: ", end="")
		inputWord(dictionary, history, base, singlePlayer, False)
		if singlePlayer[2] >= soloVictory:
			print("You win...")
			print("What?...You thought you were going to get flowery language and a huge celebration...this program is too primitive for that...hype yourself!")
		else:
			print("You lose...")
			print("What?...You thought you were going to get strong language and a pity fest?...this program is too primitive for that...do that yourself.")
		toLoop()
	else:
		print("In this game...we have: ", end="")
		for player in singlePlayer[:-2]:
			print(player[0], end=", ")
		print("and", singlePlayer[-1][0], "\nWhich one of you shall come out on top and which shall be the bottom feeder?\nAll of you can say what you want; but the game never lies.")
		toContinue()
		for cycle in range(rounds-1):
			print("ROUND", str(cycle), "... FIGHT!")
			for fighter in multiPlayer:
				print("Dear", fighter[0], end=", ")
				print("please make a word...ANY word...from your board of letters [",fighter[1],"] to bolster your score of [",fighter[2],"]: ", end="")
				inputWord(dictionary, history, base, fighter, True)
		print("FINAL ROUND ... LET US BRING OUT ... THE KING AND THE PEASANT ... THE SUPERSTAR AND SUPERABYSS!")
		for fighter in multiPlayer:
			print("Dear", fighter[0], end=", ")
			print("please make a word...YOUR LAST WORD...from your board of letters [",fighter[1],"] to make the final bolster (or atrophy) for your score of [",fighter[2],"]: ", end="")
			inputWord(dictionary,history,base,fighter,True)
		print("Great game! Here are the results: ")
		leaderboard = []
		ranking = {}
		for fighter in multiPlayer:
			leaderboard.append(fighter[2])
			ranking[fighter[2]] = fighter[0]
		leaderboard.sort()
		print("Last place goes to",ranking[leaderboard[0]],"with a score of", leaderboard[0], "making them the SUPERABYSS!")
		for index in range(1, len(leaderboard)-1):
			position = len(leaderboard) - index
			if position == 2:
				ordinal = str(position) + "nd"
			elif position == 3:
				ordinal = str(position) + "rd"
			else:
				ordinal = str(position) + "th"
			print(ordinal, "place goes to", ranking[leaderboard[index]], "with a score of", leaderboard[index])
		print("And 1st place goes to", ranking[leaderboard[-1]],"with a score of", leaderboard[-1],"making them the SUPERSTAR!")
while True:
	dictionary = []
	main(dictionary)
	toLoop()