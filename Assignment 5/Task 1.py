'''
Problem Statement: Write a Python program that:
1.   Creates a dictionary where student names are keys and their marks are values.
2.   Asks the user to input a student's name.
3.   Retrieves and displays the corresponding marks.
4.   If the student’s name is not found, display an appropriate message.

'''

Student_Dict = {
    "alice": 85,
    "bob": 92,
    "charlie": 78,
    "david": 90,
    "eva": 88,
    "harsh" : 69,
    "yash" : 100,
    "ronak" : 99,
    "vanshika" : 87
}

Student_name = input("Enter the students name : ").lower()

if (Student_name in Student_Dict):
    marks = Student_Dict.get(Student_name)
    print(f'{Student_name} Marks : {marks}')
else:
    print("Student not found.")