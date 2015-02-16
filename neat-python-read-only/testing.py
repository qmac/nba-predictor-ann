import math
import random
import cPickle as pickle
import sys

from scraper import Scraper

from neat import config, population, chromosome, genome
from neat.nn import nn_pure as nn

file = open("winner_chromosome")
chromo = pickle.load(file)
best_net = nn.create_ffphenotype(chromo)
file.close()
while True:
	inputs = []
	ortg_net = input("What is ORTG (net)?")
	inputs.append(int(ortg_net))
	drtg_net = input("What is DRTG (net)?")
	inputs.append(int(drtg_net))

	outcome_prediction = best_net.sactivate(inputs)[0]
	print "Probability home team wins: " + str(outcome_prediction)
	if random.random() < outcome_prediction:
		print "Simulated outcome is a home win"
	else:
		print "Simulated outcome is a home loss"
