# Welcome Players

**To a variant of the New York Spelling Bee Game**

It is time to test your ability and affinity with the language that finds its great roots in the language of the Mass and its worldwide affluence through the prosperity of those small islands who stood at the core of a land where the sun never set: we are of course talking about the English Language.

## Details

This game allows for 1-8 players; the singleplayer mode being a little distinct from the multiplayer mode. As of now, there is no instance of time-controlled gameplay so it is up to the players to decide if and how time shall be controlled. 

The words of which this game will be based on will be found in the words.txt file in the repository. To make changes to this dictionary base for the gameplay, download the entire repository and run deuterogame.py with a Python executable that can retrieve the data.

*Be warned because the most ordinary and many Python executables will not be able to retrieve the data from outside itself; this is why protogame.py is data-independent for the game*

## Gameplay

On every turn, the player simply generates a word from their own in-built dictionary. Depending on the difficulty, scores will be added according to the length of the word they can provide. 

The similarity to Scrabble lies in the board of letters which may be provided through automatic or manual work. This board is going to consist of seven to twelve letters depending on the difficulty. In it, there will be a required letter--the letter which must be in every word generated--and optional letters--the letters which don't have to be in every word generated--which together make up the native letters.

## Penalties

They are two kinds to watch out for: 

**De facto penalties** which are those which occur during manual board generation as handicaps imposed by faulty board generations.

**classic penalties** which are those imposed by the game during rounds for violations of the word generation.

### De-Facto Penalties

**Budgeting:** Should the player attempt to overshoot the set-by-difficulty board length (nine over seven or fifteen over twelve e.g.) all the overshot letters will be removed and not integrated into the board leaving whatever mess is at the beginning to be the board for the player.

**Betabet:** Characters not in the alphabet of Latin-based letters (called "betabets" by the whims of the creator and no official resource) _can_ be included in the board. However, the game will penalize any word generates which contain such characters, practically reducing the board's scope.

**Overdose:** Every letter in the board can be used multiple times for every word generation, therefore, repeating letters in a board is an unnecessary reduction in scope and practical use.

All of these violations will be caught during the board generation and given just one more chance to make a new board and correct them; one more chance means the system will take no trolling.

### Classic Penalties

**AntiLanguage:** Word with a Betabet character.

**AntiEnglish:** Word not in the given dictionary: "word.txt" for the protogame.py executable and whatever custom list for the deuterogame.py executable. Note that this penalty triggers to misspelling. 

**Plagiarism:** Word which has been generated in a previous turn in any given gaming cycle.

**Headless:** Word missing the board's required letter which is the first letter of the board.

**Foreign:** Word including letters outside of the board.

**Stump:** Word which is too short for the difficulty.

You shall discover the impact of each penalty during gameplay. For now, keep it registered that the requirement for every word is essentially the avoidance of the in-game penalties while the recommendations for every board is that of the de-facto penalties.

## Singleplayer and Multiplayer

**Singleplayer** is the game with only one user. In this there will be loss and victory for this one player alone according to whether they achieve the independent bar in the number of rounds set by the difficulty.

**Multiplayer** is the game with more than one user. In this there will be victory for one of the players and ranked losses for the others according to their relative standings at the end of the gaming cycle whose number of rounds will may also be automated or manual.

## Difficulties: (time to finally explain that thing we keep talking about)

These are not level of difficulties _per se_ but instead packages of the various requirements and scopes.

#### First Package

Seven-Letter Board
