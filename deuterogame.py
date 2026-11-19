import protogame
print("You have loaded the weaker and more dependent version of Digital Esque Scrabble Esque...please be sure that you are running this program with a competent executable and in the same folder with the protogame file and the dictionary file.")
protogame.toContinue()
print("Provide the name of the file to be the English dictionary for this run (inclusive of the .txt extension): ", end="")
nofile = "File not found; please check directories and try again."
dictionary = protogame.filetoOneVarList(protogame.inputFile(nofile))
print("The game shall run with this new dictionary now...")
protogame.toContinue()
history = []
while True:
    protogame.main(dictionary, history)
    protogame.toLoop()