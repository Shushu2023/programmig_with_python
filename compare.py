x= int(input("what's x? "))
y = int (input("what's y? "))
# the longest and most repetative approach(not recommended)
if x < y:
    print("x is less than y") # a boolean expression has a yes or no answer
if x > y:
    print("x is greater than y")   
if x == y:
    print("x is equal to y")
###################################################
#second best but still repetative 

if x < y:
    print("x is less than y") # a boolean expression has a yes or no answer
elif x > y:
    print("x is greater than y")   
elif x == y:
    print("x is equal to y")
################################################
#better way but not optmal 
if x < y:
    print("x is less than y") # a boolean expression has a yes or no answer
elif x > y:
    print("x is greater than y")   
else:
    print("x is equal to y")
####################################################
#better and simpler 
if x < y or x > y:
    print("x is not equal to y")
else:
    print("x is equal to y")
####################################################
#even simpler 
if x != y:
    print("x is not eqaul to y")
else:
    print("x is equal to y")

# the inverted version
if ( x == y):
    print("x is equal to y")
else:
    print("x is not equal to y")
    