# a dictionary is a key value pair
# this is a single dictionary
students= {
    "Hermione": "Gryffindor",
    "Harry":"Gryffindor",
    "Ron": "Gryffindor",
    "Draco":"Slytherin",
}

# this will print the keys and the values seperated by commas
for student in students:
    print(student, students[student], sep=", ")

    #this is a lsit of dictionaries
    #We will have a4 students each student is a dictionary(a collection of key value pairs)
    # each dictionary has three keys name, house and patronus
    #each key has a definition or a value

classmates = [
     {"name":"Hermione", "house":"Gryffindor", "patronus":"Otter"},
     {"name":"Harry", "house":"Gryffindor", "patronus":"Stag"},
     {"name":"Ron", "house":"Gryffindor", "patronus":"Jack Russell terrier"},
     {"name":"Draco", "house":"Slytherin", "patronus":None},
     
 ]

#iterate through the list of classmates
#print the value of each key "name" and key "house" and key "petronous"
#seperated by commas
for classmate in classmates:
    print(classmate["name"], classmate["house"], classmate["patronus"], sep=", ")
   