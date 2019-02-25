from functions import *
from block_stack import *



start_state = "B AC"  #Start State
final_state = "CBA" #Goal State
KB = []
goal_state = []
current_state = []
plan = []
KB = start_state.split()
goal_state_ = final_state.split()
print "Initial State:"
for i in range(len(KB)):
    if len(KB[i]) == 1:
        ontable(KB[i], table)
        print clear(KB[i])
        print
    else:
        for j in range(len(KB[i])):
            if j == 0:
                ontable(KB[i][j], table)
            if j == len(KB[i])-1:
                print clear(KB[i][j])
                print
            else:
                print on(KB[i][j + 1], KB[i][j])



print "Goal State"
msg = ""
for i in range(len(goal_state_)):
    if len(goal_state_[i]) == 1:
        ontable(goal_state_[i], table)
        print clear(goal_state_[i])
        table.append(goal_state_[i])
        print
    else:
        for j in range(len(goal_state_[i])):
            if j == 0:
                ontable(goal_state_[i][j], table)
                # table.append(goal_state_[i][j])
                goal_state.append("table_" + goal_state_[i][j])
                msg += "table_"+goal_state_[i][j]
                # goal_state.append(goal_state_[i][j]+goal_state_[i][j+1])
            if j == len(goal_state_[i]) - 1:
                print clear(goal_state_[i][j])
                print
            else:
                print on(goal_state_[i][j + 1], goal_state_[i][j])
                goal_state.append("on_"+goal_state_[i][j]+goal_state_[i][j+1])
                msg += " on_"+goal_state_[i][j]+goal_state_[i][j+1]
goal_state.insert(0,msg)

# while len(goal_state) > 1:
if "on_" in goal_state[-1]:
    last_ele = goal_state[-1].replace("on_","")
    Armempty()
    action_unstack(last_ele[1],table,last_ele[0])
    goal_state.append("move_"+last_ele[1]+last_ele[0])
    goal_state.append("on_"+last_ele[1]+"_Table"+" clear_"+last_ele[1]+" clear_" +last_ele[0])
    for i in (goal_state[-1].split(" ")):
        print i


# print new_list[1]
# print len(goal_state_)
# print  goal_state[-1].replace("on_","")[1]
# print "table ",table
# print "goal state " ,goal_state
for i in xrange(len(goal_state)):
    print goal_state[-i -1]
# new_list = [on(goal_state_[0][1],goal_state_[0][0]), on(goal_state_[0][2],goal_state_[0][1])]
#
# print new_list[0]
