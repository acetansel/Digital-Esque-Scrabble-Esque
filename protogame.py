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
	while firstDif or secondDif or thirdDif or fourthDif or fifthDif or sixthDif:
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
	if leninput("Fourth question: are we leaving the generation of the boards and the selection of the number of rounds to automation? "):
		rounds = random.randint(10,31)
		print("Therefore, we will be playing",rounds,"rounds.\nYou may deny (return nothing) to generate a new number if you wish", end="")
		if not leninput():
			return "Of course not! If you knew you had a specific number in mind; why didn't you pick manual? No problem, be sure to be manual this time as the program restarts."
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
			print("If you managed to dodge tha trap to a forceful restart; we can move on and give you your board.\nDon't get apprehensive about attempting to remember them or have them written down somewhere; the system will keep every players' board displayed as it is their turn.")
			alphabetDealings = randomize(alphabet)
			board = ""
			for letter in alphabetDealings[0:(boardScope - 1)]:
				board += letter
			playerInfo.append(board)
			print("Dear",playerInfo[0], end=" ")
			print("This is your board: ",playerInfo[1],"recalling that the first is the required and the rest are the optional.")
while True:
	main()
	toLoop()
