
#5
student_names = []
student_scores = []
studentone_name = input("enter 1st student name")
studentone_score = int(input("enter 1st student score"))
student_names.append(studentone_name)
student_scores.append(studentone_score)
studenttwo_name = input("enter 2nd student name")
studenttwo_score = int(input("enter 2nd student score"))
student_names.append(studenttwo_name)
student_scores.append(studenttwo_score)
studentthree_name = input("enter 3rd student name")
studentthree_score = int(input("enter 3rd student score"))
student_names.append(studentthree_name)
student_scores.append(studentthree_score)
print(f"Student\t Scores\n{student_names[0]}\t{student_scores[0]}\n{student_names[1]}\t{student_scores[1]}\n{student_names[2]}\t{student_scores[2]}")
