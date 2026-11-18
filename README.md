# Welcome Players

**To a variant of the New York Spelling Bee Game**

It is time to test your ability and affinity with the language that finds its great roots in the language of the Mass and its worldwide affluence through the prosperity of those small islands who stood at the core of a land where the sun never set: we are of course talking about the English Language.

## Details

This game allows for 1-8 players; the singleplayer mode being a little distinct from the multiplayer mode. As of now, there is no instance of time-controlled gameplay so it is up to the players to decide if and how time shall be controlled. 

The words of which this game will be based on will be found in the words.txt file in the repository. To make changes to this dictionary base for the gameplay, download the entire repository and run deuterogame.py with a Python executable that can retrieve the data.

*Be warned because the most ordinary and many Python executables will not be able to retrieve the data from outside itself; this is why protogame.py is data-independent for the game*

## Instructions and Gameplay

On every turn, the player simply generates a word from their own in-built dictionary. Depending on the difficulty, scores will be added according to the length of the word they can provide. 

The similarity to Scrabble lies in the board of letters which may be provided through automatic or manual work. This board is going to consist of seven to twelve letters depending on the difficulty. In it, there will be a required letter--the letter which must be in every word generated--and optional letters--the letters which don't have to be in every word generated--which together make up the native letters.

### Penalties

Under manual board generation, only the first seven to twelve characters will be counted. If you attempt to 
