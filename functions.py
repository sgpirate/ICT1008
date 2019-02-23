from block_stack import *
s = Stack()
table_stack = Stack()

def unstack(a,b):
    print "Pick up clear block " + a + " from "+ b
    pass
def stack(a,b):
    print "Place "+a +" using the arm onto clear block "+ b
    on(a,b)
    pass
def pickup(a):
    print "Lift clear block "+a+ " with the empty arm"
    pass
def putdown(a):
    print "Place the held block "+ a + " onto a free space on the table"
    ontable(a)
    pass




def on(a,b):
    print "Block " +a+" is on Block "+ b
    pass
def ontable(a):
    print "Block "+a+ " is on the table"
    pass
def clear(a):
    print "Block "+a+ " is clear"
    pass
def holding(a):
    print "Arm is holding "+a
    pass
def Armempty():
    print "Arm is Empty"
    pass
