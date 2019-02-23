from functions import *
from block_stack import *



initial_state = "b,a"  #Start State
print "intial State"
print "|a|"
print "|b|"
print "-------------"
final_state = "a,b" #Goal State
print "Goal State"
print "|b|"
print "|a|"
print "-------------"
# demo = ["BA","EDC"]
# print demo[0][0]
table = []
end_state = []

initial_data = initial_state.split(",")
initial_data_count = len(initial_data)
print initial_data_count


while initial_data_count > 1:
    initial_data_count -= 1
    table.append(initial_data[-1])
    initial_data.pop(-1)



print table
temp = 0
print len(table)
print table[0]
print initial_data[0]
while len(table) > 0:
   if table[temp] < initial_data[temp]:
       table.append(initial_data[temp])
       initial_data.pop()
       break
       print len(table)
       print "1"

print initial_data
print ','.join(table)
print final_state


if ','.join(table) == final_state:
    print True

# Test test
# print initial_data_count
# while initial_data_count > 0:
#     s.push(initial_data[initial_data_count-1])
#     initial_data_count -= 1
# for i in initial_data:
#     print "|",i,"|"
# # print initial_data
# print s.data
# print s.peek()
# print s.data.pop(-1)
# print s.data
# Armempty()
# unstack(initial_data[0], initial_data[1])
# holding(initial_data[0])
# putdown(initial_data[0])
# Armempty()
# ontable(initial_data[0])
# clear(initial_data[0])

