
student_grades = {
    "Ahmed": 90,
    "Sara": 95,
    "Omar": 88
}

print(f"Original Grades: {student_grades}")


print(f"Sara's grade is: {student_grades['Sara']}")


student_grades["Ali"] = 92 
student_grades["Ahmed"] = 98  
print(f"Updated Grades: {student_grades}")

del student_grades["Omar"]
print(f"Grades after deleting Omar: {student_grades}")


for name, grade in student_grades.items():
    print(f"Student: {name}, Grade: {grade}")                           