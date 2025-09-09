i = 0 
while i < 3:
    print("meow")
    i += 1

'''bad design you cant keep adding values if you are trying to count to a mimmioun'''
for i in [0, 1, 2]:
    print("meow")

'''better design si to use the range function'''
for i in range (15):
    print("meow")

'''even better is to replace the i with _ because we don't care about the name of this variable it is there
    becuase we need it '''
for _ in range (15):
    print("meow")

'''bad way not recommended'''
print("meow\n"*3, end="")


'''this statement creates an infinate loop that can only be stopped when the user enters a positive value for n'''
while True:
    n = int(input("What's n? "))
    if n > 0:
        break

for _ in range(n):
    print("meow")