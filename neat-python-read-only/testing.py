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
		inputs = []
		home_stats = teams[home_team].team_stats()
		away_stats = teams[away_team].team_stats()
		for i in range(0, len(home_stats)):
			inputs.append(home_stats[i]-away_stats[i])

		outcome_prediction = best_net.sactivate(inputs)[0]
		if random.random() < outcome_prediction:
			standings[home_team] += 1
		else:
			standings[away_team] += 1

for key in standings.keys():
	print "%s had %d wins" % (key, standings[key])


# while True:
# 	home_team = raw_input("Enter home team ")
# 	away_team = raw_input("Enter away team ")
# 	inputs = []
# 	home_stats = teams[home_team].team_stats()
# 	away_stats = teams[away_team].team_stats()
# 	for i in range(0, len(home_stats)):
# 		inputs.append(home_stats[i]-away_stats[i])

# 	outcome_prediction = best_net.sactivate(inputs)[0]
# 	print "Probability home team wins: " + str(outcome_prediction)
# 	if random.random() < outcome_prediction:
# 		print "Simulated outcome is a home win"
# 	else:
# 		print "Simulated outcome is a home loss"
