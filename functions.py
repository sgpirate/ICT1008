from block_stack import *
movecounter = 0
table = []

def unstack(a,table,b):
    print "Pick up clear block " + a + " from "+ b
    pass
def stack(a,table,b):
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
    return "Block " +a+" is on Block "+ b
def ontable(a,table):
    print "Block "+a+ " is on the table"
def clear(a):
    return "Block "+a+ " is clear"
def holding(a):
    print "Arm is holding "+a
    pass
def Armempty():
    print "Arm is Empty"
    pass
