#Using Dynamic Programming Approach
#Use Hidden Markov Model for Stock Market Fluctuations
start_probability = {'1': 0.5, '2': 0.2, '3': 0.3} #Starting probability of the respective states
states = ('1','2','3') #States as per diagram
observations = ('Up','Up','Up') #Observations for which we need the most likely sequence of hidden states
transition_probability = { #Transition probabilities from each state to all other states
           '1' : {'1': 0.6, '2': 0.2,'3': 0.2 },
          '2' :  {'1': 0.5, '2': 0.3, '3': 0.2 },
          '3' : {'1': 0.4,'2': 0.1 ,'3': 0.5 }
          }
emission_probability = { #Ouput probabilities that represent the chance that a certain action happens given the state that is present
          '1' : {'Up': 0.7, 'Down': 0.1, 'Unchanged': 0.2},
          '2' : {'Up': 0.1, 'Down': 0.6, 'Unchanged': 0.3},
          '3' : {'Up': 0.3, 'Down': 0.3, 'Unchanged': 0.4}
          }

V = [dict()] #Empty Dynamic Programming table
path = dict() #Empty dict for path

for s in states: #for each state
    V[0][s] = start_probability[s] * emission_probability[s][observations[0]] #Initialize all the base cases using start probability
    path[s] = [s] #Initialize respective paths for each state as well
size = len(observations)
for t in range(1, size): # Run Viterbi for t > 0 and process each observation one by one
    V.insert(len(V),dict()) #Insert dict at the end of V by using Length of V
    newpath = dict() 

    for fs in states:
        (prob, state) = max((V[t-1][ss] * transition_probability[ss][fs] * emission_probability[fs][observations[t]],ss) for ss in states) #Trellis diagram formula followed
        V[t][fs] = prob 
        newpath[fs] = path[state] + [fs] #Append path of previos state with current one
    path = newpath #Overwrite old path
(prob, state) = max((V[t][fs],fs) for fs in states) #Assign the max value in V as probability and the respective state which leads to list of observations
print "For the given Observation, the most likely sequence of hidden states are as below:"
for each in path[state]:
  print each,
print "\nThe probability is " + str(prob)