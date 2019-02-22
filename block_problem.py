from functions import *


initial_state = ["a", "e", "c", "b", "d"]
table = []
end_state = []


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