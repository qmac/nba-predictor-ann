'''
Script to scrape the contents of Basketball-Reference.com
Utilizing the BeautifulSoup and URL-Lib libraries
Author: Quinn McNamara
'''

import stats
import urllib2

from stats import Game, Team
from bs4 import BeautifulSoup
from urllib2 import urlopen

class Scraper:
    def retrieve_games(self):
        #returns list of Game instances with data gathered from sub-site of Basketball-Reference
        website = urlopen("http://www.basketball-reference.com/leagues/NBA_2015_games.html").read()
        soup = BeautifulSoup(website)
        #uses CSS selectors to retrieve teams and scores of each game cell of table
        game_list = soup.select("#games tbody tr td")
        my_text = []
        #strips selected list of soups of their tags
        for game in game_list:
            my_text.append(game.get_text())

        #loads formatted Game instances into a new list to be returned
        my_games = []
        for i in range(0, len(my_text), 8):
            try:
                my_games.append(Game(my_text[i+4], my_text[i+2], int(my_text[i+5]), int(my_text[i+3])))
            except ValueError:
                break

        return my_games

    #returns a dictionary of NBA teams and statistics gathered from sub-site of Basketball-Reference
    def retrieve_teams(self):
        website = urlopen("http://www.basketball-reference.com/leagues/NBA_2015.html")
        soup = BeautifulSoup(website)
        #uses CSS selectors to retrieve stats for each team
        team_list = soup.select("#team tbody tr td")
        opp_list = soup.select("#opponent tbody tr td")

        team_text = []
        opp_text = []

        #strips selected list of soups of their tags
        for team in team_list:
            team_text.append(team.get_text())
        for opp in opp_list:
            opp_text.append(opp.get_text())

        #loads formatted team names and statistics into a Python dictionary to be returned
        my_teams = dict()
        for i in range(0, len(team_text), 26):
            team_name = team_text[i+1]
            if team_name[len(team_name) - 1] == "*":
                team_name = team_name[0 : -1]
            my_teams[team_name] = Team([float(team_text[i+6]), float(opp_text[i+6])])
        return my_teams
