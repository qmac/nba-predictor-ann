'''
Class objects for encapsulating statistical data relevant to the algorithm
Author: Quinn McNamara
'''

class Game:
    def __init__(self, team1, team2, score1, score2):
        self.home_name = team1
        self.away_name = team2
        self.diff = score1 - score2

    def home(self):
    	return self.home_name

    def away(self):
    	return self.away_name
    	
    def result(self):
    	return self.diff

class Team:
    def __init__(self, s):
        self.offstat = s[0]
        self.defstat = s[1]

    def offense(self):
        return self.offstat

    def defense(self):
        return self.defstat