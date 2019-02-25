from functions import *
from block_stack import *



start_state = "B AC"  #Start State
final_state = "CBA" #Goal State
initial_state_ = []
goal_state = []
current_state = []
initial_state_ = start_state.split()
for i in range(len(initial_state_)):
    if len(initial_state_[i]) == 1:
        print clear(initial_state_[i])
        ontable(initial_state_[i],table)
    else:
        for j in range(len(initial_state_[i])):
            if j == len(initial_state_[i])-1:
                print clear(initial_state_[i][j])
            else:
                print on(initial_state_[i][j+1],initial_state_[i][j])
                ontable(initial_state_[i][j],table)


