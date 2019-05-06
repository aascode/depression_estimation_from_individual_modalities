import numpy as np
import keras

from keras.models import Model, Sequential, load_model
from keras.layers import Dense, CuDNNLSTM, Input, Concatenate, Dropout
from keras import regularizers


def load_model(location=None):

	if(location != None):
		model = keras.models.load_model(location)
		print("Loaded the model.")
		return model

	X = Input(shape = (10000, 2482,))
	X_gender = Input(shape = (1,))

	Y = CuDNNLSTM(255, name = 'lstm_cell', kernel_regularizer = regularizers.l2(0.01), recurrent_regularizer = regularizers.l2(0.01))(X)
	Y = Concatenate(axis = -1)([Y, X_gender])

	Y = Dense(20, activation = 'relu', kernel_regularizer = regularizers.l2(0.01))(Y)
	
	Y = Dense(1, activation = None)(Y)

	model = Model(inputs = [X, X_gender], outputs = Y)

	print("Created a new model.")

	return model