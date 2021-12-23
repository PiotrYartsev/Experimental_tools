#make a convolutional neural network
#That is a convolutional layer, followed by a max pooling layer,
#followed by a softmax layer.


import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)
