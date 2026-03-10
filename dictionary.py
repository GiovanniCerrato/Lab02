class Dictionary:
    def __init__(self):
        self.words = {}

    def addWord(self,alien, translation):
        self.words[alien] = translation


    def translate(self, alien):
        return self.words.get(alien, None)


    def translateWordWildCard(self):
        pass