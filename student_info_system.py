students = []

def save_to_file(student_list):
    with open("students.txt", "w") as file:
        for student in student_list:
            file.write(f"Name: {student['name']}\n")
            file.write(f"Stident ID: {student['student_id']}\n")
            file.write(f"Favorite AI tool: {student['favorite_AI_tool']}\n")

def main():
    #ask for student details
    name = input("Enter student name: ")
    student_id = input("Enter student ID: ")
    favorite_AI_tool = input("Enter favorite AI tool: ")

    #save data in dictionary
    student = {
        "name": name,
        "student_id": student_id,
        "favorite_AI_tool": favorite_AI_tool
    }

    #append dictionary to the list
    students.append(student)

    #print number of students
    print(f"\nTotal students: {len(students)}\n")

    #print stdent details neatly
    for i, s in enumerate(students, start=1):
        print(f"Student {i}")
        print(f"Name: {s[ 'name']}")
        print(f"Student ID: {s['student_id']}")
        print(f"Favorite AI tool: {s['favorite_AI_tool']}")

    #Save to file
    save_to_file(students)
    print("Student data saved to students.txt")

if __name__ == "__main__":
    main()
    

