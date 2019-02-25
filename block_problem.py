from functions import *
from block_stack import *



start_state = "B AC EFG"  #Start State
final_state = "CBA" #Goal State
initial_state_ = []
goal_state = []
current_state = []
initial_state_ = start_state.split()
goal_state = final_state.split()
print "Initial State:"
for i in range(len(initial_state_)):
    if len(initial_state_[i]) == 1:
        ontable(initial_state_[i], table)
        print clear(initial_state_[i])
        print
    else:
        for j in range(len(initial_state_[i])):
            if j == 0:
                ontable(initial_state_[i][j], table)
            if j == len(initial_state_[i])-1:
                print clear(initial_state_[i][j])
                print
            else:
                print on(initial_state_[i][j+1],initial_state_[i][j])

# print goal_state
