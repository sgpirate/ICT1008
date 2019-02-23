from functions import *
from block_stack import *



initial_state = "a,e,c,b,d"  #Start State
final_state = "a,b,c,d,e" #Goal State

# demo = ["BA","EDC"]
# print demo[0][0]
table = []
end_state = []
s = Stack()
initial_data = initial_state.split(",")
initial_data_count = len(initial_data)

# Test test
print initial_data_count
while initial_data_count > 0:
    s.push(initial_data[initial_data_count-1])
    initial_data_count -= 1
for i in initial_data:
    print "|",i,"|"
# print initial_data
print s.data
print s.data.pop(-1)
print s.data
Armempty()
unstack(initial_state[0], initial_state[1])
holding(initial_state[0])
putdown(initial_state[0])
Armempty()
ontable(initial_state[0])
clear(initial_state[0])
clear(initial_state[1])
#
#
# for i in range(len(initial_state)):
#     print