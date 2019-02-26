from functions import *
from block_stack import *



start_state = "B AC"  #Start State
final_state = "CBA" #Goal State
KB = []
goal_state = []
table = []
plan = []
KB = []
initial_state = start_state.split()
goal_state_ = final_state.split()
print "Initial State:"
for i in range(len(initial_state)):
    if len(initial_state[i]) == 1:
        ontable(initial_state[i], table)
        KB.append("ontable_"+initial_state[i])
        print clear(initial_state[i])
        KB.append("clear_"+initial_state[i])
        print
    else:
        for j in range(len(initial_state[i])):
            if j == 0:
                ontable(initial_state[i][j], table)
                KB.append("ontable_"+initial_state[i][j])
                table.append(initial_state[i][j])
            if j == len(initial_state[i])-1:
                print clear(initial_state[i][j])
                KB.append("clear_"+initial_state[i][j])
                print
            else:
                print on(initial_state[i][j + 1], initial_state[i][j])
                KB.append("on_"+initial_state[i][j+1]+initial_state[i][j])



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
                goal_state.append("ontable_" + goal_state_[i][j])
                msg += "ontable_"+goal_state_[i][j]
                # goal_state.append(goal_state_[i][j]+goal_state_[i][j+1])
            if j == len(goal_state_[i]) - 1:
                print clear(goal_state_[i][j])
                print
            else:
                print on(goal_state_[i][j + 1], goal_state_[i][j])
                goal_state.append("on_"+goal_state_[i][j]+goal_state_[i][j+1])
                msg += " on_"+goal_state_[i][j]+goal_state_[i][j+1]
goal_state.insert(0,msg)

# if i != goal_state[-1]:
#     last_ele = goal_state[-1].replace("on_", "")
#     Armempty()
#     action_unstack(last_ele[1], table, last_ele[0])
#     print
#     goal_state.append("movetotable_" + last_ele[1] + last_ele[0])
#     goal_state.append("ontable_" + last_ele[1] + " clear_" + last_ele[1] + " clear_" + last_ele[0])
#     goal_state.append("clear_" + last_ele[1])
#     goal_state.append("clear_" + last_ele[0])
#     goal_state.append("ontable_" + last_ele[1])
#     break
counter1 = 0
counter = 0
while counter < 5 :
    for i in KB:
        if counter1 >= len(KB)-1:
            if "on_" in goal_state[-1]:
                last_ele = goal_state[-1].replace("on_", "")
                Armempty()
                action_unstack(last_ele[1], table, last_ele[0])
                print
                goal_state.append("movetotable_" + last_ele[1] + last_ele[0])
                goal_state.append("ontable_" + last_ele[1] + " clear_" + last_ele[1] + " clear_" + last_ele[0])
                goal_state.append("clear_" + last_ele[1])
                goal_state.append("clear_" + last_ele[0])
                goal_state.append("ontable_" + last_ele[1])
            elif "clear_" in goal_state[-1]:
                last_ele = goal_state[-1].replace("clear_", "")
                for i in KB:
                    if "on_" in i:
                        i  = i.replace("on_","")  # type: str
                        if last_ele in i:
                            action_stack(i[0], table, i[1])
                            print
                            print "clear section"
                            goal_state.append("movefromtable_" + i[0] + i[1])
                            goal_state.append("on_" + i[1]+i[0] + " clear_" + i[0])
                            goal_state.append("clear_" + i[0])

                break
            elif "movefromtable_" in goal_state[-1]:
                plan.append(goal_state[-1])
                goal_state.pop()
                print "321321321321"
                fromtable = goal_state[-1].replace("movefromtable_","")
                # goal_state.append("1")
                for i in KB:
                    if "on_" in i:
                        newi = i.replace("on_","")
                        # print "new",newi[0]
                        # print "new", newi[1]
                        KB.append("ontable_"+ newi[0])
                        KB.append("clear_" + newi[1])
                        KB.remove(i)








        counter1 += 1
    for i in goal_state:
        for j in KB:
            i_list = i.split(" ")
            # print j_list
            if j == i:
                goal_state.remove(j)

    check_last_ele = goal_state[-1].split(" ")
    # print "check", check_last_ele
    if len(check_last_ele) >= 2:
        goal_state.pop()

    counter +=1



# for i in initial_state:
#
# for i in initial_state:
#     if i != goal_state[-1]:
#         last_ele = goal_state[-1].replace("clear_", "")
#         Armempty()
#         action_unstack(last_ele[1], table, last_ele[0])
#         print
#         goal_state.append("movetotable_" + last_ele[1] + last_ele[0])
#         goal_state.append("ontable_" + last_ele[1] + " clear_" + last_ele[1] + " clear_" + last_ele[0])
#         goal_state.append("clear_" + last_ele[1])
#         goal_state.append("clear_" + last_ele[0])
#         goal_state.append("ontable_" + last_ele[1])



# if "clear_" in goal_state[-1]:

    # print "clear"
# Gold Stack Planning 2
# print new_list[1]
# print len(goal_state_)
# print  goal_state[-1].replace("on_","")[1]
# print "table ",table
# print "goal state " ,goal_state
j = len(goal_state[-1].split(" "))
print
for i in xrange(len(goal_state)):

    # if -i == i:
    #     for k in xrange(j):
    #         print goal_state[-1].split(" ")[-k]

    print goal_state[-i -1]




print
print
print "Goal State     ",goal_state
print "Knowledge Base " ,KB
print
print initial_state
print table
print plan

