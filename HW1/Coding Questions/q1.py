#MISSIONARIES AND CANNIBALS PROBLEM
# The state representation (num_c,num_m,pos_b) signifies the number of cannibals, missionaries and boat on the left side of the river
#The start state will be 3,3,1 and end state will be 0,0,0
class State:
    #constructor to initialize c,m,d and p being root
    def __init__(self, num_c, num_m, pos_b):
        self.num_c = num_c
        self.num_m = num_m
        self.pos_b = pos_b
        self.p = None
    #member function to find if final state has been reached
    def final(self):
        return  self.pos_b == 0 and self.num_m == 0 and self.num_c == 0
    #member function to check if current state is valid or not
    def valid(self):
        if self.num_m < 0 or self.num_c < 0 or self.num_m > 3 or self.num_c >3:
            return False
        elif self.num_c > self.num_m and self.num_m>0:
            return False
        elif self.num_c < self.num_m and self.num_m<3:
            return False
        else:
            return True

#Generate all possible successor states for given state and append if it's a valid state
def successors(present_state):
    nodes = []
    C = [1,0,1,2,0]
    M = [0,1,1,0,2]
    for countC,countM in zip(C,M):
        if present_state.pos_b == 0: #if boat is on right side of the bank
            final_state = State(present_state.num_c + countC, present_state.num_m+countM, 1) #Transport 1C from R to L
        else: #if boat is on left side of the bank
            final_state = State(present_state.num_c - countC, present_state.num_m-countM, 0) #Transport 1C from L to R
        insert_next_state(present_state, final_state, nodes)
    return nodes

#function to insert all successors of final_state to nodes
def insert_next_state(present_state,final_state, nodes):
    if final_state.valid():
        final_state.p = present_state
        nodes.insert(len(nodes),final_state)

#breadth first search algorithm implementation
def breadth_first_search():
    s_state = State(3,3,1) #start state of missionaries and cannibals
    head = []
    seen = {}
    head.insert(len(head),s_state) #head containing start state
    while head:
        tempresent_state = head.pop(0)
        if tempresent_state.final(): #if state is final return the state
            return tempresent_state
        seen[tempresent_state] = 1
        nodes = successors(tempresent_state)
        for n in nodes:
            if (n not in seen) or (n not in head):
                head.insert(len(head),n)
    return []

mcd = []
ans = breadth_first_search()
mcd.insert(len(mcd),ans)
temp = ans.p
while temp: #construct states to reach goal state and store in mcd
    mcd.insert(len(mcd),temp)
    temp = temp.p
print("MISSIONARIES AND CANNIBALS SOLUTION:")
print("START STATE: 3\t3\t1")
print("GOAL STATE:  0\t0\t0")
print("INTERMEDIATE STATES:")
for i in range(len(mcd)): #iterate through mcd
    s = mcd[len(mcd) - i - 1]
    if s.pos_b == 1: #assign place of boat using s.d value
    	side = "left"
    else:
    	side = "right"
    print(str(s.num_c) + " Cannibals and " + str(s.num_m) + " Missionaries on the left side of the bank and the boat on " + side + " side of the bank")
