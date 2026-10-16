class Movie:
    def __init__(self, name, lang, rating):
        self.name = name
        self.lang = lang
        self.rating = rating


    def getName(self):
        return self.name
    def setName(self, newname):
        self.name = newname

    def getLang(self):
        return self.lang
    def setLang(self, newlang):
        self.lang = newlang

    def getRating(self):
        return self.rating
    def setRating(self, newrating):
        self.rating = newrating

    def display(self):
        print(f"Name = {self.name}\tLanguage = {self.lang}\tRating = {self.rating}")

e1 = Movie("Drishyam", 'Hindi', 5)
e2 = Movie("Hunkkar", 'Hindi', 4)
print(e1.getName())
e1.display()
e2.display()
e2.setRating(5)
e2.display()