import random
import re
import hangman_asciiDarstellung as ascii
import hangman_woerter as words

def print_header(word):
    """
    Zeigt das Hangman-Logo, eine Willkommensnachricht und die Länge des ausgewählten Wortes an

    Parameter:
    word (str): Das geheime Wort, das der Benutzer erraten muss.

    Rückgabe:
    None
    """
    print(ascii.logo)
    print("Welcome to Hangman!")
    print(f"I think of a word, which is {len(word)} characters long")

def print_hangman(guessedLetter, chosenWord, lifes, alreadyguessed, secretWordList):
    """
    Überprüft, ob das Spiel gewonnen/ verloren wurde
    Zeigt, welche Buchstaben bereits (nicht) erraten sind
    Zeigt, wie viele Leben übrig sind

    Parameter:
    guessedLetter (str): Input vom User (Buchstabe)
    chosenWord (str): Vom Programm gewähltes Wort  
    lifes (int): Anzahl der Leben
    alreadyguessed (set): Bereits erratene Buchstaben
    secretWordList (list): mit "_" versehenes Wort 

    Rückgabe:
    None
    """
    if "".join(secretWordList) == chosenWord:
        print("**************************************")
        print("Congratulations! You won!!!")
        print("**************************************")
    
    if guessedLetter not in chosenWord:

        if lifes == 0:
            print("You Lost!")
            print("**************************************")      
            print(ascii.stufen[lifes])
            print(f"The word was \"{chosenWord}\"")
        else:
            print(ascii.stufen[lifes])
            print("**************************************")
            print(f"Sorry, \"{guessedLetter}\" is not right!")
            print("**************************************")

    print(f"Hangman: {' '.join(secretWordList)}")
    print("**************************************")
    print(f"You already guessed: {alreadyguessed}") 
    print(f"Remaining lifes: {lifes}")
    print(f"Remaining letters: {secretWordList.count('_')}")
    print("**************************************")

def get_input():
    """
    Erhält User-Eingabe mit RegEx
    Erlaubte Zeichen: A-Z case-insensitive + Umlaute + "-" + " "

    Parameter:
    None

    Rückgabe:
    guess (str): Ein einzelner Character zwischen A-Z, a-z, äüö, - , " " 
    """
    match = False

    while not match:

        guess = input("Enter a valid letter between [A-Z]: ")
        pattern = r"^[a-zA-z,\ä\ö\ü\ß\-\ ]$"
        match = re.search(pattern, guess)

        if match:
            return guess

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
    wordList = words.hangman_woerter
    return wordList

def get_secretwordlist(wordList):
    """
    Maskiert WordList mit _

    Parameter:
    wordList (list): Vom Programm gewähltes Wort

    Rückgabe:
    secretwordlist (list)
    """
    return list(len(wordList) * "_")

def hangman(chosenWord, guessedLetter, secretWordList, alreadyguessed, lifes):
    """
    Überprüft, ob Buchstabe bereits erraten 
    -> Ja, Ausgabe bereits erraten
    -> Nein, ist Buchstabe in Wort enthalten?
        -> Ja, führe Ersetzung durch
        -> Nein, Lebensabzug
    Füge Buchstabe in Set ein

    Parameter:
    chosenWord (str): vom Computer ausgewähltes Wort
    guessedLetter (str): vom User gewählter Buchstabe
    secretWordList (list): mit "_" maskiertes Wort (Liste von Strings)
    alreadyguessed (set): bereits erratene Buchstaben
    lifes (int): Anzahl Leben

    Rückgabe:
    secretWordList (list)
    alreadyguessed (set)
    lifes (int)
    """

    if guessedLetter not in alreadyguessed:
        if guessedLetter in chosenWord:
            for i in range(len(chosenWord)):
                if guessedLetter == chosenWord[i]:
                    secretWordList[i] = chosenWord[i]
        else:
            lifes -= 1
    else:
        print("**************************************")
        print(f"Ouups!! You already guessed: \"{guessedLetter}\"!")
        print("**************************************")
    alreadyguessed.add(guessedLetter)

    return secretWordList, alreadyguessed, lifes

if __name__ == "__main__":

    gameclose = False

    while not gameclose:
    
        # initialize variables     
        alreadyguessed = set()
        chosenWord = random.choice(load_wordlist()).lower()
        secretWord = get_secretwordlist(chosenWord)
        lifes = 6
        print_header(chosenWord)
        print(f"DEBUG: Das gewaehlte Wort ist {chosenWord}")

        while "_" in secretWord and lifes > 0:
            
            guessedLetter = get_input().lower()
            secretWord, alreadyguessed, lifes = hangman(chosenWord, guessedLetter, secretWord, alreadyguessed, lifes)
            gameclose = print_hangman(guessedLetter, chosenWord, lifes, alreadyguessed, secretWord, gameclose)

            if gameclose:
                print("You wish to continue [Y/N]")
                gameclose = True if get_input().lower() == "n" else False
