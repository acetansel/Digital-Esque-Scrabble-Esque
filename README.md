# Welcome Players

#### To a variant of the New York Spelling Bee Game (I think...that's what my professor told me)

It is time to test your ability and affinity with the language that finds its great roots in the language of the Mass and its worldwide affluence through the prosperity of those small islands who stood at the core of a land where the sun never set: we are of course talking about the English Language.

## Gameplay

On every turn, the player simply generates a word according to the best of their knowledge (or perhaps guesses). Each word will have its score value according to the difficulty chosen and its length so longer words are the key to prosperity here.

The similarity to Scrabble lies in the board of letters which may be provided through automatic or manual generation. This board is going to consist of seven, eight or nine letters depending on the difficulty. In it, its first letter there will be the required letter (the letter which must be in every word generated) and others will be the optional letters (the letters which don't have to be in every word generated).

## Penalties

They are two kinds to watch out for:

**De facto penalties** which are those which occur during manual board generation as handicaps imposed by faulty board generations.

**Classic penalties** which are those imposed by the game during rounds for violations of the word generation.

### De-Facto Penalties

**Budgeting:** Should the player attempt to overshoot the set-by-difficulty board length (nine over seven or fifteen over twelve e.g.) all the overshot letters will be removed and not integrated into the board leaving whatever mess is at the beginning to be the board for the player.

**Betabet:** Characters not in the alphabet of Latin-based letters (called "betabets" by the whims of the creator and no official resource) *can* be included in the board. However, the game will penalize any word generates which contain such characters, practically reducing the board's scope.

**Overdose:** Every letter in the board can be used multiple times for every word generation, therefore, repeating letters in a board is an unnecessary reduction in scope and practical use.

All of these violations will be caught during the board generation and given just one more chance to make a new board and correct them; one more chance means the system will take no trolling.

_Note: underdosing is also a violation but it won't be caught by the system; so better you overdo it instead of underdoing it if you lose count somehow_

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

**Multiplayer** is the game with more than one user (up to eight). In this there will be victory for one of the players and ranked losses for the others according to their relative standings at the end of the gaming cycle whose number of rounds will may also be automated or manual.

## Difficulties: (time to finally explain that thing we keep talking about)

These are not level of difficulties *per se* but instead packages of the various requirements and scopes.

#### First Package

* 14-Letter Board
* Scores at the 3rd Base
* At least 3-letter words

#### Second Package

* 15-Letter Board
* Scores at the 3rd Base
* At least 3-letter words

#### Third Package

* 16-Letter Board
* Scores at the 4th Base
* At least 4-letter words

#### Fourth Package

* 14-Letter Board
* Scores at the 5th Base
* At least 5-letter words

#### Fifth Package

* 15-Letter Board
* Scores at the 6th Base
* At least 6-letter words

#### Sixth Package

* 16-Letter Board
* Scores at the 7th Base
* At least 7-letter words

#### Defining "Scores at the nth Base"

The worth of each letter in a word is based on an arithmetic progression which begins counting from the upper half (if skewed) of the required length. Once it does begin, the progression starts from n and increments by n. The score value of the word is the sum of all values in this string. 

The penalties will also be based on the score base as well as the rank of the violated law which will, once again, be kept concealed until gameplay.

The singleplayer victory line will be equivalent to the total score, according to every package, of generating words with length equal to the length of the board.

_So the average length for the generated words have to be board-length to win solo?_ **No!** Because the lower half of the required length which is counted out during player score accumulation will be included in the score accumulation for the victory line. Therefore, a little more letters than the board length, being much larger with a higher package.

## Time-Keeping?

As of now, there is no instance of time control within the program itself to pace the flow of the game and aid with score generation and penalizing. So, if such is desired, another program or manual time-keeping may have to be done to do so. Shall it be done, use the chronoprotogame.py or chronodeuterogame.py executables (analogous to proto and deutero) where it will remain fixed with the second package (and where future updates for in-built time control will hopefully be placed).

## Execution and Data

**All players need is a single device (there is no multi-screen interface anyway) and the protogame.py executable.**

Should the system not have a Python interpreter:

* Shortcut Windows Key + R to open Windows Run
* Open "powershell" on Windows Run
* Enter "python" on the console
* Download the popped up Python manager from the Microsoft Store
* Return to the file and run as normal
* All data is self-contained so you should not need any file

The words which define this game is the dictionary defined in "words.txt". If you wish to modify this dictionary or use a different one to include some niche words or slang; instead download deuterogame.py and run it in the same folder with the data of the imported dictionary.

*Be sure to obtain a Python interpreter which can derive data from outside the executed program; one obtained in the steps above cannot.*

# *Happy Spelling!*



