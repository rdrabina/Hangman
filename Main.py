import linecache
import random

chance = 10


def read_from_file():
    words_in_file = -1
    try:
        for words_in_file, verse in enumerate(open('words', 'rU')):
            pass
        words_in_file += 1
    except IOError:
        print ("File does not exist")
        exit()
    return words_in_file


def choose_a_word():
    line = random.randint(1, read_from_file())
    lyric = linecache.getline('words', line)
    return lyric


word = choose_a_word()
word = word[:-1]
length = len(word)
guessed_letters = ["_"] * length
wrong_letters = []


def dialogue_with_user():
    word_guessed = False
    i = chance
    letter_guessed = False
    interrupt = length
    while i:
        letter = ""
        print_hangman(chance-i)
        print_letters(1)
        if i > 1:
            print ("You have " + str(i) + " chances")
        if i == 1:
            print ("You have " + str(i) + " chance")
        letter = raw_input("Enter one letter: ")
        if letter.upper() in guessed_letters or letter.upper() in wrong_letters:
            print ("You have already entered this letter. Try again!")
            print ""
            continue
        if len(letter) != 1:
            print("You entered invalid number of letters! Try again!")
            continue
        if ord(letter) < 65 or ord(letter) > 122 or (90 < ord(letter) < 97):
            print ("You did not enter the letter! Try again!")
            continue
        else:
            for j in range(0, length, 1):
                if letter.lower() == word[j] or letter.upper() == word[j]:
                    letter_guessed = True
                    guessed_letters[j] = letter.upper()
                    interrupt -= 1
            if letter_guessed:
                i += 1
                letter_guessed = False
                print "Correct letter!"
            else:
                wrong_letters.append(letter.upper())
                print "Wrong letter!"
        if interrupt == 0:
            word_guessed = True
            break
        i -= 1
    if word_guessed:
        print_hangman(chance-i+1)
        print_letters(1)
        print "Congratulations! You win! :D"
    else:
        print_hangman(chance-i+1)
        print_letters(0)
        print "Game over! :("


def print_hangman(i):
    try:
        open('hangman', 'rU')
    except IOError:
        print "File 'hangman' does not exist!"
        exit()
    hangman = []
    for j in range(1, i*20/chance, 1):
        hangman.append(linecache.getline('hangman', j))
    for a in hangman:
        print a,
    print ""
    print ""


def print_letters(end):
    if end:
        for p in guessed_letters:
            print p,
        print ""
        print ""
        print "Wrong entered letters: "
        for l in wrong_letters:
            print l,
        print ""
        print ""
    else:
        for p in guessed_letters:
            print p,
        print ""
        for p in word:
            print p.upper(),
        print ""
        print "Wrong entered letters: "
        for l in wrong_letters:
            print l,
        print ""
        print ""

dialogue_with_user()
