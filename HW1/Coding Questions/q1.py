#! /usr/bin/env python

from collections import deque

# The state representation (x,y,z) signifies the number of missionaries, cannibals and boats on the left side of the river

class state(object):
  def __init__(self, missionaries, cannibals, boats):
    self.missionaries = missionaries
    self.cannibals = cannibals
    self.boats = boats
  
  # function to return generator for actions and new state
  def successors(self):
    if self.boats == 1:
      flag = -1
      direction = "from left to right"
    else:
      flag = 1
      direction = "from right to left"
    for missionaries in range(3):
      for cannibals in range(3):
        new_state = state(self.missionaries+ flag*missionaries, self.cannibals+ flag*cannibals, self.boats + flag*1);
        if missionaries + cannibals >= 1 and missionaries + cannibals <= 2 and new_state.valid():
          action = "transport %d missionaries and %d cannibals %s. Result state is %r" % ( missionaries, cannibals, direction, new_state)
          yield action, new_state

  # function to return if current state is a valid or invalid state
  def valid(self):
    if self.missionaries < 0 or self.cannibals < 0 or self.missionaries > 3 or self.cannibals > 3 or (self.boats != 0 and self.boats != 1):
      return False   
    # check if missionaries lesser than cannibals
    if self.cannibals > self.missionaries and self.missionaries > 0:
      return False
    if self.cannibals < self.missionaries and self.missionaries < 3:
      return False
    return True

  # function to return if current state is the goal state
  def is_goal_state(self):
    return self.cannibals == 0 and self.missionaries == 0 and self.boats == 0

  def __repr__(self):
    return "<(%d, %d, %d)>" % (self.missionaries, self.cannibals, self.boats)

class Node(object):  
  def __init__(self, parent_node,state,action,depth):
    self.parent_node = parent_node
    self.state = state
    self.action = action
    self.depth = depth

  # function for expanding the successors of current node
  def expand(self):
    for (a,s) in self.state.successors():
      s_node = Node(parent_node=self,state=s,action=a,depth=self.depth + 1)
      yield s_node

  # function to save the steps involved in reaching the goal state starting the initial state
  def save(self):
    steps = []
    node = self
    while node.parent_node is not None:
      steps.append(node.action)
      node = node.parent_node
    steps.reverse() #reverse solution to give correct steps
    return steps

#Breadth First search function 
def bfs(start_state):
  start_node = Node(parent_node=None,state=start_state,action=None,depth=0)
  FIFO = deque([start_node]) #using deque object from collections
  max_depth = -1 #initialize depth to be -1
  while 1:
    node = FIFO.popleft() #pop left most element from the FIFO
    if node.depth > max_depth:
      max_depth = node.depth
    if node.state.is_goal_state(): #if state is goal state save the steps to reach goal state
      answer = node.save() #use saver function to append actions 
      return answer
    FIFO.extend(node.expand())

def main():
  start_state = state(3,3,1) #3 missionaries and 3 cannibals on the left side of the river with the boat on this side
  answer = bfs(start_state) #call bfs to traverse state space to store solution path
  for path in answer: #print path
    print "%s" % path

if __name__ == "__main__":
  main()