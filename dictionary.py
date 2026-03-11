class Dictionary:
    def __init__(self):
        self.words = {}

    def addWord(self,alien, translations):
        #translations è una lista di stringhe
        if alien not in self.words:
            self.words[alien] = list(translations)
        else:
            for t in translations:
                if t not in self.words[alien]:
                    self.words[alien].append(t)



    def translate(self, alien):
        return self.words.get(alien, None)


    def translateWordWildCard(self):
        pass