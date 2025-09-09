'''a program that prompts the user for the name of a variable in camel
 case and outputs the corresponding name in snake case. 
 Assume that the user’s input will indeed be in camel case.'''

camel_case = input("camelCase: ")
for i in range (len(camel_case)):
    if camel_case[i] == camel_case[i].capitalize():
       words =  camel_case.split(camel_case[i])
       for j in range (len(words)):
        camel_case = words[j]+"_"+camel_case[i].lower()
        print("camel_case: "+camel_case)