### Copyright 2018 by A.R. Plummer


### import numpy and matplotlib

import numpy as np
import matplotlib.pyplot as plt



### using an np.array to represent out data.  the first column is the
### bias term x0. the second and third columns are the truth values of
### the propositions X and Y.  The fourth column is the truth value of
### the proposition X and Y, which we take to be the class value C.

#andFunction = np.array([[1,1,1,1],
#                       [1,0,1,0],
#                       [1,1,0,0],
#                       [1,0,0,0]])
#Not using numpy for arrays

andFunction = [[1,1,1,1],
				[1,0,1,0],
				[1,1,0,0],
				[1,0,0,0]]

### the lines below are used to plot the data.

for dataPoint in andFunction:
	plt.plot(dataPoint[1:3],'ro',ms=10)

#plt.plot(andFunction[0,1],andFunction[0,2],'bo',ms=10)
plt.plot(andFunction[0][1],andFunction[0][2],'bo',ms=10)
plt.ylim((-1,2))
plt.xlim((-1,2))
plt.show()

### you need to initialize the weights for your perceptron (I suggest
### using an np.array).

andWeights = [0,0,0]


### A function for the input value of a perceptron.  It should compute
### the dot product of a weight vector and an input vector.
# weight 0 is for bias and weight 1 is for x and weight y is for y
def inValue (weights, featureVals):
	#featureVals is analogous to inputs
	# calculate the dot product of weights and input values aka featureVals
	result = featureVals[0]*weights[0] + featureVals[1]*weights[1] + featureVals[2]*weights[2]
	return result


### You need to implement a step activation function here.  This
### function should return a 1 or 0 to match the class values defined
### in the andFunction above.

def stepActivation(z):
	if z>=0:
		return 1
	else:
		return 0

### Weight update goes here. This function should return an np.array
### with 3 components.

#w1*b + w2*x + w3*y = 0
def stepUpdate(weights, featureVals, learningRate):
	#initialize the weights to respective variables
	expected_output = featureVals[3] #Get the expected outputs from feature Vals
	result = inValue(weights,featureVals[0:3]) #Compute result from inValue function
	activation_value = stepActivation(result) #Pass result to activation function to get activation value
	weights[0] += learningRate*featureVals[0]*(expected_output - activation_value) #Update weight_0
	weights[1] += learningRate*featureVals[1]*(expected_output - activation_value) #Update weight_1
	weights[2] += learningRate*featureVals[2]*(expected_output - activation_value) #Update weight_2
	return weights

### Suggested learning rate and epoch numbers.
   
learningRate = 0.09
epoch = 5000



### loop running training over the suggested number of epochs and an
### embedded loop over each data point. 

for i in range(epoch):
    for dataPoint in andFunction:
    	andWeights = stepUpdate(andWeights,dataPoint,learningRate) #andWeights updated with respective learning rate and dataPoint

#Parse through all rows of AND function and plot the red points. RO stands for red.



#for i in range(4): #4 being the length of AND function
#	sample = andFunction[i]
#	plt.plot(sample[1],sample[2],'ro',ms=10)

for dataPoint in andFunction:
	plt.plot(dataPoint[1:3],'ro',ms=10)

#Plot the blue point where output is 1 and input is 1 and 1
#plt.plot(andFunction[0,1],andFunction[0,2],'bo',ms=10)
plt.plot(andFunction[0][1],andFunction[0][2],'bo',ms=10)
plt.ylim((-1,2))
plt.xlim((-1,2))
# Our andFunction contains values in the format b x y o where b is for bias x is first input y is second input and o is the final output
x = np.linspace(-1, 2, 100) # X axis being divided between from -1 to 2 with 100 values in between
plt.plot(x,-(andWeights[1]/andWeights[2])*x -(andWeights[0]/andWeights[2]))
#The above line derieved from the relation w1b + w2x + w3y = 0 => w3y = -w1b -w2x => y = (-w1/w3)b + (-w2/w3)x
plt.show()

### after the loop above, your weights should be able to correctly
### classify the training data.  Plot the training data and the
### decision boundary that your trained weights yield.
