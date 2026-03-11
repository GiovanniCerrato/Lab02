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


    def translateWordWildCard(self,query):
        results = []
        for alien in self.words:
            match = False
            if len(query) == len(alien):
                match = True
                for q,a in zip(query,alien):
                    if (q!='?' and q!=a):
                        match = False
            if match:
                results.append((alien, self.words[alien]))

        return results


