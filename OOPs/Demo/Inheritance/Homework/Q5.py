class Players:
    def __init__(self, player_id, name, age, country):
        self.player_id = player_id
        self.name = name
        self.age = age
        self.country = country

    def getPlayer_id(self):
        return self.player_id

    def setPlayer_id(self, newplayer_id):
        self.player_id = newplayer_id

    def getName(self):
        return self.name

    def setName(self, newname):
        self.name = newname

    def getAge(self):
        return self.age

    def setAge(self, newage):
        self.age = newage

    def getCountry(self):
        return self.country

    def setCountry(self, newcountry):
        self.country = newcountry

    def display(self):
        print(f"Player ID = {self.player_id}\tName = {self.name}\tAge = {self.age}\tCountry = {self.country}")


class CricketPlayer(Players):
    def __init__(self, player_id, name, age, country, batting_style):
        super().__init__(player_id, name, age, country)
        self.batting_style = batting_style

    def getBatting_style(self):
        return self.batting_style

    def setBatting_style(self, newbatting_style):
        self.batting_style = newbatting_style

    def display(self):
        print(f"Batting Style = {self.batting_style}\t")
        return super().display()


class HockeyPlayer(Players):
    def __init__(self, player_id, name, age, country, position):
        super().__init__(player_id, name, age, country)
        self.position = position

    def getPosition(self):
        return self.position

    def setPosition(self, newposition):
        self.position = newposition

    def display(self):
        print(f"Position = {self.position}\t")
        return super().display()


p1 = Players(101, "Amisha", 22, "India")
c1 = CricketPlayer(102, "Rohit", 30, "India", "Right Hand")
h1 = HockeyPlayer(103, "Amit", 25, "India", "Forward")
p1.display()
c1.display()
h1.display()