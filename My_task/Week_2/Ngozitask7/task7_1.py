#Student Biodata

Student_name= input( "enter your details")
Student_age= input( "enter your details")
Student_course= input( "enter your details")
course = list(Student_course)

Student_info = {"name": {Student_name},
                "age":{Student_age}
                }

# print(course)
# print(Student_info)
print(f"Student Biodata page    \n====================================\n Name:\t{Student_name}\n Age:\t{Student_age}\n Course :\t{course}\n==========================")
