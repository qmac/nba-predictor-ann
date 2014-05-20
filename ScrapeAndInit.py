'''
Script to scrape the contents of Basketball-Reference.com
Utilizing the BeautifulSoup and URL-Lib libraries
Author: Quinn McNamara
'''

import GamesAndTeams
import urllib2
from GamesAndTeams import *
from bs4 import BeautifulSoup
from urllib2 import urlopen

#returns list of Game instances with data gathered from sub-site of Basketball-Reference
def retrieve_games():
    website = urlopen("http://www.basketball-reference.com/leagues/NBA_2014_games.html").read()
    soup = BeautifulSoup(website)
    #uses CSS selectors to retrieve teams and scores of each game cell of table
    game_list = soup.select("#games tbody tr td[align$=\"t\"]")
    my_text = []
    #strips selected list of soups of their tags
    for game in game_list:
        my_text.append(game.get_text())

    #loads formatted Game instances into a new list to be returned
    my_games = []
    for i in range(0, len(my_text), 6):
        my_games.append(Game(my_text[i+3], my_text[i+1], int(my_text[i+4]), int(my_text[i+2])))
    return my_games

#returns a dictionary of NBA teams and statistics gathered from sub-site of Basketball-Reference
def retrieve_teams():
    website = urlopen("http://www.basketball-reference.com/leagues/NBA_2014.html")
    soup = BeautifulSoup(website)
    #uses CSS selectors to retrieve stats for each team
    team_list = soup.select("#misc tbody tr td")
    my_text = []
    #strips selected list of soups of their tags
    for team in team_list:
        my_text.append(team.get_text())

    #loads formatted team names and statistics into a Python dictionary to be returned
    my_teams = dict()
    for i in range(0, len(my_text), 23):
        team_name = my_text[i+1]
        if team_name[len(team_name) - 1] == "*":
            team_name = team_name[0 : -1]
        my_teams[team_name] = Team([float(my_text[i+8]), float(my_text[i+9])])
    return my_teams
