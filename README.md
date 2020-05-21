# word hunt solver v1

## current roadmap:
**1. working model of the game
2. create a solver**
3. generate boards through an image 
4. have a player automatically play the game
5. have a machine physically play the game

## how to use:
be sure to download the included .yaml file and create the environment, then run in the terminal using: 

### python(3) main.py [args]
 - -i \<input file> : a screenshot of a board taken from the gamepigeon app. if none specified, will either create a random board or prompt for input.
 - -o \<output file> : a text file to store the found words in. if none specified, will print words to console.
 - -d \<dictionary json> : a JSON file of words that the board should be generated from. if none specified, will use a preselected dictionary.
 - -r : if no input file specified, will create a random board.
 - -f : if no output file specified, will print all words to console. otherwise, will only print the first 20.

### special thanks and acknowledgements:
dictionaries taken from:

 - https://github.com/dwyl/english-words.git
 - https://github.com/matthewreagan/WebstersEnglishDictionary/blob/master/dictionary.json



