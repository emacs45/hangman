import random
import re
import hangman_asciiDarstellung
import hangman_woerter

def print_header(word):
    """
    Zeigt das Hangman-Logo, eine Willkommensnachricht und die Länge des ausgewählten Wortes an.

    Parameter:
    word (str): Das geheime Wort, das der Benutzer erraten muss.

    Rückgabe:
    None
    """
    print(hangman_asciiDarstellung.logo)
    print("Welcome to Hangman!")
    print(f"I think of a word, which is {len(word)} characters long")

def print_hangman_lifes(guessedLetter, chosenWord, lifes, alreadyguessed, secretWordList):
    """
    Überprüft, ob Buchstabe im Wort enthalten ist, sonst Lebensabzug
    Überprüft, ob das Spiel gewonnen/ verloren wurde
    Zeigt, welche Buchstaben bereits erraten sind
    Zeigt, wie viele Leben übrig sind

    Parameter:
    guessedLetter (str): Input vom User (Buchstabe)
    chosenWord (str): Vom Programm gewähltes Wort  
    lifes (int): Anzahl der Leben
    alreadyguessed (set): Bereits erratene Buchstaben
    secretWordList (list): mit "_" versehenes Wort 

    Rückgabe:
    lifes
    """
    if "".join(secretWordList) == chosenWord:
        print("Congratulations! You won!!!")
        print("**************************************")

    if guessedLetter not in chosenWord:
        lifes -= 1
        
        if lifes == 0:
            print("You Lost!")
            print("**************************************")      
            print(hangman_asciiDarstellung.stufen[lifes])
            print(f"The word was \"{chosenWord}\"")
        else:
            print(hangman_asciiDarstellung.stufen[lifes])
            print("**************************************")
            print(f"Sorry, \"{guessedLetter}\" seems not right!")
            print("**************************************")

    print(f"You already guessed: {alreadyguessed}") 
    print(f"Remaining lifes: {lifes}")
        
    return lifes

def get_input():
    """
    Erhält User-Eingabe mit RegEx
    Erlaubte Zeichen: A-Z Incase-Sensitive + Umlaute + "-" + " "

    Parameter:
    None

    Rückgabe:
    guess (str): Ein Wert zwischen A-Z
    """
    match = False

    while not match:

        guess = input("Please enter a letter: ")
        pattern = r"^[a-zA-Z,\ä\ö\ü\ß\-\ ]{1}$"
        match = re.search(pattern, guess)

        if match:
            return guess
        else:
            print("Enter a valid letter between [A-Z]: ")

def load_wordlist():
    """
    Lädt die Datei hangman_woerter.py und füllt sie in eine Liste.
    Auskommentiert: Befüllte Testdatensätze in Liste

    Parameter:
    None

    Rückgabe:
    wordList (list)
    """
    #wordList = ["Katze", "Hund", "Maus", "Hundun"]
    wordList = hangman_woerter.hangman_woerter
    return wordList

def get_secretwordlist(wordList):
    """
    Chiffriert WordList mit _

    Parameter:
    wordList (list): Vom Programm gewähltes Wort

    Rückgabe:
    secretwordlist (list)
    """
    return ["_" for _ in range(len(wordList))]

def hangman(chosenWord, guessedLetter, secretWordList, alreadyguessed):

    for i in range(len(chosenWord)):
        if guessedLetter == chosenWord[i]:
            secretWordList[i] = chosenWord[i]
        
        alreadyguessed.add(guessedLetter)

    print("**************************************")
    print(f"Hangman: {' '.join(secretWordList)}")
    print(f"Remaining letters: {secretWordList.count('_')}")
    print("**************************************")
    #print(f"Debug: {alreadyguessed}")

    return secretWordList, alreadyguessed

if __name__ == "__main__":
    
    # initialize variables     
    alreadyguessed = set()
    chosenWord = random.choice(load_wordlist()).lower()
    secretWord = get_secretwordlist(chosenWord)
    lifes = 6

    print_header(chosenWord)
    print(f"DEBUG: Das gewaehlte Wort ist {chosenWord}")

    # while not ("".join(secretWord) in chosenWord) and lifes > 0:
    while "_" in secretWord and lifes > 0:
        
        guessedLetter = get_input().lower()
        secretWord, alreadyguessed = hangman(chosenWord, guessedLetter, secretWord, alreadyguessed)
        lifes = print_hangman_lifes(guessedLetter, chosenWord, lifes, alreadyguessed, secretWord)
