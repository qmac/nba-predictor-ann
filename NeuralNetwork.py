'''
Outline of class definitions for structures: Neuron, Layer, NeuralNetwork
Author: Quinn McNamara
'''

import random

BIAS = 1.0 #bias will always be 1.0 and will be for every function/structure

#Hierarchy of structures: NeuralNet(work) is composed of Layers, Layers are composed of Neurons
#Weights are given as parameters, which are passed down in hierarchy to construct each structure properly
class Neuron:
    def __init__(self, w):
        self.weights = w
    #activation function takes summation of (weight times input) and fires the result
    def fire(self, inputs):
        total = 0.0
        for i in range(0, len(inputs)):
            total += inputs[i] * self.weights[i]
        total += BIAS * self.weights[len(inputs)]
        ''' Use this code for step-function neurons
        if total > 0:
            return 1.0
        else:
            return 0.0
        '''
        #output is variable-output for neuron
        return total


class Layer:
    def __init__(self, weights):
        self.neurons = []
        for i in range(0, len(weights)):
            self.neurons.append(Neuron(weights[i]))


class NeuralNet:    
    def __init__(self, weights):
        self.layers = []
        for i in range(0, len(weights)):
            self.layers.append(Layer(weights[i])) 
    #fires all neurons in network to determine output
    def fire(self, inputs):
        signals = inputs
        for l in self.layers:
            outputs = []
            for n in l.neurons:
                outputs.append(n.fire(signals))
            signals = outputs
        #output determined by step-function threshold for network
        if signals[0] > 0:
            return 1.0
        else:
            return 0.0
        #return signals[0] #Use this code for variable-output network
