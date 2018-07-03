#USAGE: python q4.py 18 
#where 18 is passed as an argument to represent number of iterations
import sys

states = ['cool','warm','overheated'] #three states
actions = ['slow','fast'] #two possible actions

#function to return probability given a state, corresponding action and respective future states
def prob(state,action,future_state):
	if state == 'cool' and action == 'slow' and future_state == 'cool':
		return 1
	elif state == 'cool' and action == 'fast' and future_state == 'cool':
		return 0.5
	elif state == 'cool' and action == 'fast' and future_state == 'warm':
		return 0.5
	elif state == 'warm' and action == 'slow' and future_state == 'cool':
		return 0.5
	elif state == 'warm' and action == 'slow' and future_state == 'warm':
		return 0.5
	elif state == 'warm' and action == 'fast' and future_state == 'overheated':
		return 1
	else:
		return 0

#function to return rewards given a state, corresponding action and respective future states
def rewards(state,action,future_state):
	if state == 'cool' and action == 'slow' and future_state == 'cool':
		return 1
	elif state == 'cool' and action == 'fast' and future_state == 'cool':
		return 2
	elif state == 'cool' and action == 'fast' and future_state == 'warm':
		return 2
	elif state == 'warm' and action == 'slow' and future_state == 'cool':
		return 1
	elif state == 'warm' and action == 'slow' and future_state == 'warm':
		return 1
	elif state == 'warm' and action == 'fast' and future_state == 'overheated':
		return -10
	else:
		return 0

gamma = 1 #no discount
V_old = [0,0,0] #initial cool,warm & overheated states respective values
x = int(sys.argv[1]) #number of iterations

for i in range(x):
	V_new = [0,0,0]
	for count_major,s in enumerate(states):
		sum_over = []
		for a in actions:
			temp = 0
			for count,s_dash in enumerate(states):
				temp += prob(s,a,s_dash)*(rewards(s,a,s_dash) + gamma*V_old[count]) #the value iteration formula
			sum_over.append(temp)
		V_new[count_major] = max(sum_over)
	V_old = V_new
print V_new