import random
import cPickle as pickle

from scraper import Scraper

from neat.nn import nn_pure as nn

file = open("winner_chromosome")
chromo = pickle.load(file)
best_net = nn.create_ffphenotype(chromo)
file.close()

stats_scraper = Scraper()
teams = stats_scraper.retrieve_teams()

standings = dict.fromkeys(teams.keys(), 0)

for home_team in teams.keys():
	for away_team in teams.keys():
		inputs = [teams[home_team].offense() - teams[away_team].offense(), teams[home_team].defense() - teams[away_team].defense()]

		outcome_prediction = best_net.sactivate(inputs)[0]
		if random.random() < outcome_prediction:
			standings[home_team] += 1
		else:
			standings[away_team] += 1

for key in standings.keys():
	print "%s had %d wins" % (key, standings[key])


# while True:
# 	inputs = []
# 	home_team = raw_input("Enter home team ")
# 	away_team = raw_input("Enter away team ")
# 	inputs = [teams[home_team].offense() - teams[away_team].offense(), teams[home_team].defense() - teams[away_team].defense()]

# 	outcome_prediction = best_net.sactivate(inputs)[0]
# 	print "Probability home team wins: " + str(outcome_prediction)
# 	if random.random() < outcome_prediction:
# 		print "Simulated outcome is a home win"
# 	else:
# 		print "Simulated outcome is a home loss"
