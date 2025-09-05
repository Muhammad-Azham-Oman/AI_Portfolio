print("Welcome to School Management System\n")

print("If you want to use 'Student Management System' press 's'.")
print("If you want to use 'Teacher Management System' press 't'.")
choice = input("Enter your choice:")

if(choice=="s"):
 print("Welcome to Students Management System\n")
 print("Press '1' to add a student.")
 print("Press '2' to see student information.")
 print("Press '3' to remove a student.")
 print("Press '4' to update student information.")
 print("Press '5' to exit.")

 students = []

 while True:
    try:
        n = int(input("Enter the number from (1 to 5): "))

        if (n == 5):
            print("Goodbye, see you soon.")
            break

        elif (n == 1):
            name = input("Enter the name: ")
            roll_number = int(input("Enter the roll number: "))
            grade = int(input("Enter the grade: "))
            student = {"Name": name,"Roll no.": roll_number,"Grade": grade}
            students.append(student)
            print("Student added successfully.\n")

        elif (n == 2):
            roll = int(input("Enter the roll number of the student: "))
            for student in students:
                if student["Roll no."] == roll:
                    print(f"Name: {student['Name']}, Roll no.: {student['Roll no.']}, Grade: {student['Grade']}\n")
                    break
                else:
                    print("Student not found.\n")
        elif (n == 3):
            roll = int(input("Enter the roll number to delete: "))
            for student in students:
                if (student["Roll no."] == roll):
                    students.remove(student)
                    print("Student removed successfully.\n")
                    break
                else:
                    print("Student not found.\n")

        elif (n == 4):
            print("Click 'n' if you want to update name of the student.")
            print("Click 'r' if you want to update Roll number of the student.")
            print("Click 'g' if you want to update grade of the student.")
            update = input("Enter your choice: ")

            if (update == "n"):
              roll = int(input("Enter the roll number you want to update: "))
              for student in students:
                if (student["Roll no."]==roll):
                    new_name = input("Enter the new name of the student: ")
                    student.update({"Name" : new_name})
                    print("The name of the student updated suceessfully.\n")
                    break
                else:
                    print("Student not found.\n")

            elif(update=="r"):
              roll = int(input("Enter the roll number you want to update: "))
              for student in students:
                if (student["Roll no."]==roll):
                    new_roll = int(input("Enter the new roll number: "))
                    student.update({"Roll no." : new_roll})
                    print("The roll number of the student updated suceessfully.\n")
                    break
                else:
                    print("Student not found.\n")

            elif(update=="g"):
              roll = int(input("Enter the roll number you want to update: "))
              for student in students:
                if (student["Roll no."]==roll):
                    new_grade = int(input("Enter the new grade of the student: "))
                    student.update({"Grade" : new_grade})
                    print("The grade of the student updated suceessfully.\n")
                    break
                else:
                    print("Student not found.\n")


        else:
            print("Invalid,Please enter a number between 1 to 4.\n")

    except ValueError:
        print("You enter an invalid number.\n")


elif(choice=="t"):
 print("Welcome to Teacher Management System\n")

 print("Press '1' to add a teacher.")
 print("Press '2' to view a teacher by ID.")
 print("Press '3' to delete a teacher.")
 print("Press '4' to update details of a teacher.")
 print("Press '5' to exit.\n")

 teachers = []

 while True:
   try:
    choice = int(input("Enter your choice (1 to 5t): "))

    if (choice == 5):
        print("Goodbye, see you soon.")
        break

    elif (choice == 1):
        name = input("Enter the teacher's name: ")
        subject = input("Enter the subject: ")
        teacher_id = int(input("Enter the teacher ID: "))

        teacher = {"Name": name, "Subject": subject, "ID": teacher_id}
        teachers.append(teacher)
        print("Teacher added successfully.\n")

    elif (choice == 2):
        Id = int(input("Enter the teacher ID to view: "))
        for teacher in teachers:
            if (teacher["ID"] == Id):
                print(f"Name: {teacher['Name']}, Subject: {teacher['Subject']}, ID: {teacher['ID']}\n")
                break
        else:
            print("Teacher not found.\n")

    elif (choice == 3):
        remove_id = int(input("Enter the teacher ID to delete: "))
        for teacher in teachers:
            if (teacher["ID"] == remove_id):
                teachers.remove(teacher)
                print("Teacher deleted successfully.\n")
                break
        else:
            print("Teacher not found.\n")

    elif (choice == 4):
            print("Click 'n' if you want to update name of the teacher.")
            print("Click 's' if you want to update subject of the teacher.")
            print("Click 'i' if you want to update ID of the teacher.")
            update = input("Enter your choice: ")

            if (update == "n"):
              id = int(input("Enter the ID of teacher you want to update: "))
              for teacher in teachers:
                if (teacher["ID"]==id):
                    new_name = input("Enter the new name of the teacher: ")
                    teacher.update({"Name" : new_name})
                    print("The name of the teacher updated suceessfully.\n")
                    break
                else:
                    print("Teacher not found.\n")

            elif(update=="s"):
              id = int(input("Enter the ID of the teacher you want to update: "))
              for teacher in teachers:
                if (teacher["ID"]==id):
                    new_subject = input("Enter the new subject of the teacher: ")
                    teacher.update({"Subject" : new_subject})
                    print("The subject of the teacher updated suceessfully.\n")
                    break
                else:
                    print("Teacher not found.\n")

            elif(update=="i"):
              id = int(input("Enter the ID of the teacher you want to update: "))
              for teacher in teachers:
                if (teacher["ID"]==id):
                    new_id = int(input("Enter the new id of the teacher: "))
                    teacher.update({"ID" : new_id})
                    print("The ID of the teacher updated suceessfully.\n")
                    break
                else:
                    print("teacher not found.\n")


    else:
        print("Invalid,Please enter a number from 1 to 4.\n")

   except ValueError:
      print("You entered an invalid number.")

else:
    print("System not found")