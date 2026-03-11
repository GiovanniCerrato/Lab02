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
                translations = [t.lower() for t in parts[1:]]
                self.dict.addWord(alien, translations)

        except FileNotFoundError:
            print(f"file {dict} non trovato")

    def handleAdd(self, entry):
        # entry is a tuple <parola_aliena> <traduzione1 traduzione2 ...>
        parts= entry.strip().split(" ")
        alien = parts[0].lower()
        translations = [t.lower() for t in parts[1:]]
        check_lowercase=True
        for t in translations:
            if not t.isalpha():
                check_lowercase = False
        if not alien.isalpha() or not check_lowercase:
            print("Errore: sono ammessi solo caratteri alfabetici [a-zA-Z]")
            return
        self.dict.addWord(alien, translations)
        print(f"Parola {alien} aggiunta con traduzione/i {', '.join(translations)}")




    def handleTranslate(self, query):
        # query is a string <parola_aliena>
        translations = self.dict.translate(query)
        if translations is not None:
            return print(f"La/e traduzione/i di {query} è/sono {', '.join(translations)}")
        return print("La parola aliena inserita non è presente nel dizionario")

    def handleWildCard(self,query):
        # query is a string with a ? --> <par?la_aliena>
        cnt=0
        for char in query:
            if char=='?':
                cnt+=1
                if cnt > 1:
                    return print("ERRORE, presente più di un '?' nella parola aliena")
        if cnt<1: return print("ERRORE, non è presente il '?' nella parola aliena")
        results = self.dict.translateWordWildCard(query)
        for alien, translations in results:
            print(f"Parola aliena corrispondente: {alien}       Traduzione/i:{', '.join(translations)}")




        pass
    def __str__(self):
        for alien in self.dict.words.keys():
            print(f"{alien} {', ' .join(self.dict.words.get(alien))}")
