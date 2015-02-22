import math
import random
import cPickle as pickle

import time
import platform
import traceback
import sys
import copy

from scraper import Scraper

from neat import config, population, chromosome, genome
from neat.nn import nn_pure as nn

config.load('nba_predict_config')

# set node gene type
chromosome.node_gene_type = genome.NodeGene

# scrape web for training set statistics
stats_scraper = Scraper()
games = stats_scraper.retrieve_games()
teams = stats_scraper.retrieve_teams()

def eval_fitness(population):
	for chromo in population:
		net = nn.create_ffphenotype(chromo)

		fitness = 0
		possible_fitness = 0
		num_correct = 0
		for game in games:
			#print
			#print game.home() + " vs " + game.away()
			inputs = []
			home_stats = teams[game.home()].team_stats()
			away_stats = teams[game.away()].team_stats()
			for i in range(0, len(home_stats)):
				inputs.append(home_stats[i]-away_stats[i])

			#print inputs

			home_win_prob = net.sactivate(inputs)[0]
			r = random.random()

			if (r < home_win_prob) == (game.result() > 0):
				fitness += math.fabs(game.result())
				num_correct += 1

			possible_fitness += math.fabs(game.result())
		
		#chromo.fitness = fitness / float(possible_fitness)
		chromo.fitness = num_correct / float(len(games))
		#print "A fitness was " + str(chromo.fitness)

population.Population.evaluate = eval_fitness

pop = population.Population()
pop.epoch(100, report=True, save_best=False)

winner = pop.stats[0][-1]
print 'Number of evaluations: %d' %winner.id

# Visualize the winner network (requires PyDot)
#visualize.draw_net(winner) # best chromosome

# Plots the evolution of the best/average fitness (requires Biggles)
#visualize.plot_stats(pop.stats)
# Visualizes speciation
#visualize.plot_species(pop.species_log)

# Let's check if it's really solved the problem
print '\nBest network output:'
brain = nn.create_ffphenotype(winner)
print brain.neurons
print brain.synapses

# saves the winner
file = open('winner_chromosome', 'w')
pickle.dump(winner, file)
file.close()


