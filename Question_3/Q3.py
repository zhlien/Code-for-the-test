# -*- coding: utf-8 -*-
"""
Created on Dec 17 2020

Code for Qusetion 3

Please refer to the answer sheet to see a complete strategy explanation for
solving this question.

@author: Haolin Zhong
"""

import keras
from keras.layers import Input
from keras.models import Model
from keras.layers.core import Dense
import numpy as np
from sklearn.model_selection import train_test_split


def build_MLP(activation_fn, optimizer):
    """
    Build the MLP model using Keras with optional parameters.
    """
    features = Input(shape=(3,))
    h1=Dense(4, activation=activation_fn)(features)
    h2=Dense(4, activation=activation_fn)(h1)
    output=Dense(1, activation=activation_fn)(h2)
        
    model = Model(input=features, output=output)
    model.compile(loss="mse", optimizer = optimizer)

    return model

if __name__ == "__main__":

    # Read input trainning data
    with open("train_data") as f1, open("train_truth") as f2:
        Y_trainval = f2.readlines()[1:]
        X_trainval = []
        for index,line in enumerate(f1):
            if index == 0:
                continue
            x1,x2,x3 = line.strip().split('\t')
            x1,x2,x3 = float(x1),float(x2),float(x3)
            X_trainval.append([x1,x2,x3])

    X_trainval = np.array(X_trainval)
    Y_trainval = np.array(Y_trainval)

    # Read input test data
    with open('test_data') as f:
        X_test = []
        for index,line in enumerate(f):
            if index == 0:
                continue
            x1,x2,x3 = line.strip().split('\t')
            x1,x2,x3 = float(x1),float(x2),float(x3)
            X_test.append([x1,x2,x3])
    X_test = np.array(X_test)


    """
    Grid search will be used for finding the best parameter for the model. Several
    parameters are involved: activation function, optimizer, batch size.
    """

    activation_functions = ['softmax', 'relu', 'tanh', 'sigmoid', 'linear']
    optimizers = ['SGD', 'RMSprop', 'Adagrad', 'Adadelta', 'Adam', 'Adamax', 'Nadam']
    batch_sizes = [10, 50, 100]

    """
    Split the data. In parameter selection, to avoid overfit, model will be trained
    on training set, and be evaluated on validation set.
    """
    X_train, X_valid, Y_train, Y_valid = train_test_split(X_trainval, Y_trainval, random_state=0)

    min_loss = 1000
    act_fn = ""
    opt = ""
    b_size = 0


    # Grid search
    for activation_fn in activation_functions:
        for optimizer in optimizers:
            for batch_size in batch_sizes:
                MLP = build_MLP(activation_fn, optimizer)
                MLP.fit(X_train,Y_train, batch_size = batch_size, epochs = 10)
                loss = MLP.evaluate(X_valid, Y_valid)
                if loss < min_loss:
                    min_loss = loss
                    act_fn = activation_fn
                    opt = optimizer
                    b_size = batch_size

    print("The best combination of parameters is: activation function: "+ str(act_fn)+", optimizer: "+str(opt)+", batch size: "+str(b_size))


    # Build MLP using the best combination of parameters
    MLP = build_MLP(act_fn, opt)
    # Train MLP in the whole input dataset
    MLP.fit(X_trainval,Y_trainval, batch_size = b_size, epochs = 10)
    # Predict for the test data
    Y_test_predicted = MLP.predict(X_test)

    # output
    with open("test_predicted.txt", "w") as output:
        output.write("y\n")
        for y in Y_test_predicted:
            output.write(str(y[0])+"\n")
 