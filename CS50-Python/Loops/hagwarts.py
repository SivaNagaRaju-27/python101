def student_list():
    students = ["Hermione", "Harry", "Ron", "Draco"]
    # display_students2(students)

def studentsAndHouses():
    students = {
        "Hermione": "Gryffindor",
        "Harry": "Gryffindor",
        "Ron": "Gryffindor",
        "Draco": "Slyterine"
    }

    display_students3(students)


def display_students1(students):
    for student in students:
        print(student)

def display_students2(students):
    for i in range(len(students)):
        print(students[i])

def display_students3(students):
    for student in students:
        print(student, students[student], sep = ", ")

studentsAndHouses()
