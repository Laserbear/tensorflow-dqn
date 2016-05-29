import tensorflow as tf 
import numpy as np 

class Layer(object): #construct a layer with specified dimensionality
  def __init__(self, input_size, output_size, var_scope):
    self.input_size = input_size
    self.output_size = output_size
    self.var_scope = var_scope

    with tf.variable_scope(self.scope):
      self.weights = []


  def get_vars():


class CNN(object):
  def __init__(self, input_size, scope, layers): 
    self.input_size = input_size
    self.scope = scope
    self.layers = layers

    with tf.variable_scope(self.scope): #input layer as separate so we don't have to call it layers[0]
      self.input_layer = layers[0]
      self.layers = layers[1:]
  def get_vars(): #collect variables from each layer
    variables = self.input_layer.get_vars()
    for layer in self.layers:
      variables.extend(layer.get_vars())

class DQN(object):
  def __init__(self, ...): #alot of params go here