# Problem Set 2 Solution, Evan Dieterich 

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
    for letter in range(len(secret_word)):
        if not secret_word[letter] in letters_guessed:
            return False
    return True

def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    guessed = ''
    for letter in range(len(secret_word)):
        if secret_word[letter] in letters_guessed:
            guessed += secret_word[letter] + ' '
        else:
            guessed += '_ '
    return guessed
    
def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    alphabet = list(string.ascii_lowercase)
    for i in letters_guessed:
        if i in alphabet:
            alphabet.remove(i)
    return ' '.join(str(i) for i in alphabet)

def hangman(secret_word):
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
    letters_guessed = []
    guesses_left = 6
    warnings_left = 3
    print('Welcome to Hangman!')

    while guesses_left >= -1:
        score = guesses_left * warnings_left
        print('You have ' + str(guesses_left) + ' guesses remaining.')
        print('Available letters: ' + get_available_letters(letters_guessed))
        guess = input('Please guess a letter: ').lower()

        if guess not in string.ascii_letters:
            if warnings_left == 0:
                guesses_left -= 1
                print('Oops! That is not a valid letter! You have ' +
                      str(guesses_left) + ' guesses left. ' + get_guessed_word(secret_word, letters_guessed))
                continue
            else:
                warnings_left -= 1
                print('Oops! That is not a valid letter! You have ' +
                      str(warnings_left) + ' warnings left. ' + get_guessed_word(secret_word, letters_guessed))
                print('----------------------------------')
                continue
        else:
            letters_guessed.append(guess)

 
        if guess not in secret_word:
            print('Oops! That letter is not in my word: ' + get_guessed_word(secret_word, letters_guessed))
            print('----------------------------------')
            guesses_left -= 1
        else:
            print('Good guess: ' + get_guessed_word(secret_word, letters_guessed))
            print('----------------------------------')

        if guesses_left <= 0:
            print('You ran out of guesses!')
            print('The word was: ' + secret_word)
            break

        if is_word_guessed(secret_word, letters_guessed):
            print('Congratulations, you won!')
            print('Your score for this game was: ' + str(score))
            break


def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    my_word = my_word.replace(' ','')
    if len(my_word) != len(other_word):
        return False
    for i in range(len(my_word)):
            if (my_word[i] in string.ascii_lowercase) and my_word[i] != other_word[i]:
                return False
            
    return True



def show_possible_matches(wordlist, my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    hint_wordlist = []
    for i in wordlist:
        if match_with_gaps(my_word, i):
            hint_wordlist.append(i)
            
    return hint_wordlist



def hangman_with_hints(secret_word):
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
    letters_guessed = []
    guesses_left = 6
    warnings_left = 3
    print('Welcome to Hangman!')

    while guesses_left >= -1:
        score = guesses_left * warnings_left
        print('You have ' + str(guesses_left) + ' guesses remaining.')
        print('Available letters: ' + get_available_letters(letters_guessed))
        guess = input('Please guess a letter: ').lower()

        if guess == '*':
            print('Possible matches: ', show_possible_matches(wordlist, get_guessed_word(secret_word, letters_guessed)))
            continue

        if guess not in string.ascii_letters:
            if warnings_left == 0:
                guesses_left -= 1
                print('Oops! That is not a valid letter! You have ' +
                      str(guesses_left) + ' guesses left. ' + get_guessed_word(secret_word, letters_guessed))
                continue
            else:
                warnings_left -= 1
                print('Oops! That is not a valid letter! You have ' +
                      str(warnings_left) + ' warnings left. ' + get_guessed_word(secret_word, letters_guessed))
                print('----------------------------------')
                continue
        else:
            letters_guessed.append(guess)

 
        if guess not in secret_word:
            print('Oops! That letter is not in my word: ' + get_guessed_word(secret_word, letters_guessed))
            print('----------------------------------')
            guesses_left -= 1
        
        else:
            print('Good guess: ' + get_guessed_word(secret_word, letters_guessed))
            print('----------------------------------')

        if guesses_left <= 0:
            print('You ran out of guesses!')
            print('The word was: ' + secret_word)
            break

        if is_word_guessed(secret_word, letters_guessed):
            print('Congratulations, you won!')
            print('Your score for this game was: ' + str(score))
            break




# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    #secret_word = choose_word(wordlist)
    #hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
