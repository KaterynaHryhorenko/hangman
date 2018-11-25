# Problem Set 2, hangman.py
# Name: Kate Hryhorenko
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    number_word=0
    for i in letters_guessed:
         for j in range (len(secret_word)):
             if i == secret_word[j]:#checks for equality and count it
                 number_word+=1
    if number_word == len(secret_word):
        return True
    else:
        return False



def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    answer=['_'for i in range(len(secret_word))]#write empty word
    for  i in  range (len(letters_guessed)):
        if letters_guessed[i] in secret_word:#checks the letter rewrites the words
            for j in range(len(secret_word)):
                if secret_word[j] == letters_guessed[i]:
                    answer.pop(j)
                    answer.insert(j,letters_guessed[i])
    return list(answer)



def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    alphabet=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'] 
    if len(letters_guessed) == 0:
        return list(alphabet)
    for i in range(len(letters_guessed)) :#deletes used letters
        alphabet.remove(letters_guessed[i])
    return list(alphabet)
    

def number_of_unique_letters (secret_word):
    unique_letters=0
    for i in 'aeuio':#count unique letters in secret word
        if i in secret_word:
            unique_letters+=1
    return unique_letters

def hangman(secret_word,guesses,warings,letters_guessed):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    if guesses <= 0 :#check number of attempts
        print('secret_word:',secret_word)
        print('You failed')
        return
    elif is_word_guessed(secret_word, letters_guessed) == True:#checks if you won
        print('Congratulations, you won! Your total score for this game is:',guesses*number_of_unique_letters (secret_word)) 
        return 
        
    
    print('-------------')
    print(get_guessed_word(secret_word, letters_guessed))
    print('You have',guesses,'guesses left.')
    print('You have ',warings ,'warnings left.')
    print('You can choose from:',get_available_letters(letters_guessed))

    letter=input('Please guess a letter:')
    while letter in letters_guessed or letter.isdigit() or letter.isupper():#validation of letter
        if letter in letters_guessed:
            print("Oops! You've already guessed that letter.")
        elif letter.isdigit() or letter.isupper() :
            print('Wrong, try more')
        warings-=1
        if warings == 0:
            print('You loose 1 guess')
            guesses-=1
            warings=3
            if guesses == 0:
                return hangman(secret_word,guesses,warings,letters_guessed)
        print('you have',warings,'warings')
        letter=input('Please guess a letter:')
        
        
    letters_guessed.append(letter)#appending letter for list of letters_guessed

    if letter in secret_word:#check if letter in secret word
        print('Good guess!' )
    else:
        if letter in 'aeuio':
            guesses-=2
        else:
            guesses-=1
        print('Oops! That letter is not in my word.')
    return hangman(secret_word,guesses,warings,letters_guessed)    



# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    if len(my_word) == len(other_word):#check len of words(to reduce the search circle)
            for i in range(len(my_word)):
                     if my_word[i] != other_word[i] and my_word[i] not in '_' :#rejects not similar words
                             return False
            return True
    else:
        return False



def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    inFile = open(WORDLIST_FILENAME, 'r')
    listt=str(inFile.readlines())#turning into a string
    listt=listt[1:]
    listt=listt[:len(listt)-1]
    listt=listt.split()
    for i in range(len(listt)):#checks match
        if match_with_gaps(my_word, listt[i]) == True:
            print(listt[i])
        
    return 

	

def hangman_with_hints(secret_word,guesses,warings,letters_guessed):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    if guesses <= 0 :
        print('secret_word:',secret_word)
        print('You failed')
        return
    elif is_word_guessed(secret_word, letters_guessed) == True:
        print('Congratulations, you won! Your total score for this game is:',guesses*number_of_unique_letters (secret_word)) 
        return 
        
    
    print('-------------')
    print(get_guessed_word(secret_word, letters_guessed))
    print('You have',guesses,'guesses left.')
    print('You have ',warings ,'warnings left.')
    print('You can choose from:',get_available_letters(letters_guessed))

    letter=input('Please guess a letter:')
    if letter in '*' :#turning a hint
       show_possible_matches(get_guessed_word(secret_word, letters_guessed))
       letter=input('Please guess a letter:')
    
    while letter in letters_guessed or not(letter.isalpha()) or letter.isupper() : #validation of letter
    	if letter in letters_guessed:
    		print("Oops! You've already guessed that letter.")
    	elif not(letter .isalpha()):
    		print('Wrong, try more')
    	warings-=1
    	if warings == 0:
    		print('You loose 1 guess')
    		guesses-=1
    		warings=3
    		if guesses == 0:
    			return hangman_with_hints(secret_word,guesses,warings,letters_guessed)
    	print('you have',warings,'warings')
    	letter=input('Please guess a letter:')
        
    
        
    letters_guessed.append(letter)#appending letter for list of letters_guessed

    if letter in secret_word:
        print('Good guess!' )
    else:
        if letter in 'aeuio':
            guesses-=2
        else:
            guesses-=1
        print('Oops! That letter is not in my word.')
    return hangman_with_hints(secret_word,guesses,warings,letters_guessed)  

# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":#work of computer module
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    

    #secret_word = choose_word(wordlist)
    #print('Welcome to the game Hangman!')
    #print('I am thinking of a word that is ',len(secret_word),'letters long.')
    #hangman(secret_word,6,3,[])

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word,6,3,[])



