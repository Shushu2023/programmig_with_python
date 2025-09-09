'''a list of three strings'''
students = ["Hermione", "Harry", "Ron" ]
print(students[0]) # print the first student

# lets use a loop to iterate through the list and print out each student
for student in students:
    print(student)

# not e that the range function accepts only numbers so if 
# you want tto use the range function use the length of the list

for i in range(len(students)):
    print(i+1, students[i])



