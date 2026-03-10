from warnings import catch_warnings

import dictionary
from dictionary import Dictionary


class Translator:

    def __init__(self):
        self.dict = Dictionary()

    def printMenu(self):
        # 1. Aggiungi nuova parola
        print("1. Aggiungi nuova parola")
        # 2. Cerca una traduzione
        print("2. Cerca una traduzione")
        # 3. Cerca con wildcard
        print("3. Cerca con wildcard")
        # 4. Stampa tutto il dizionario
        print("4. Stampa tutto il dizionario")
        # 5. Exit
        print("5. Exit")

    def loadDictionary(self, dict):
        # dict is a string with the filename of the dictionary
        try:
            f = open(dict, "r").read().splitlines()
            for line in f:
                parts = line.split(" ")
                alien = parts[0].lower()
                translation = parts[1].lower().strip()
                self.dict.addWord(alien, translation)

        except FileNotFoundError:
            print(f"file {dict} non trovato")

    def handleAdd(self, entry):
        # entry is a tuple <parola_aliena> <traduzione1 traduzione2 ...>
        pass

    def handleTranslate(self, query):
        # query is a string <parola_aliena>
        pass

    def handleWildCard(self,query):
        # query is a string with a ? --> <par?la_aliena>
        pass