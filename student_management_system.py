# ==========================================
# Student Management System
# ==========================================

# Variables
college_name = "Lovely Professional University"
course_name = "B.Tech CSE (AI & ML)"

# Dictionary for Student 1
student1 = {
    "Roll No": 101,
    "Name": "Midhun Kumar",
    "Age": 19,
    "Department": "CSE AI & ML",
    "CGPA": 8.75
}

# Dictionary for Student 2
student2 = {
    "Roll No": 102,
    "Name": "Rahul Sharma",
    "Age": 20,
    "Department": "Computer Science",
    "CGPA": 8.50
}

# Store dictionaries in a list
students = [student1, student2]

# Display College Information
print("====================================")
print("   STUDENT MANAGEMENT SYSTEM")
print("====================================")
print("College Name :", college_name)
print("Course       :", course_name)

# Display Student 1 Details
print("\nStudent 1 Details")
print("----------------------------")
print("Roll No    :", students[0]["Roll No"])
print("Name       :", students[0]["Name"])
print("Age        :", students[0]["Age"])
print("Department :", students[0]["Department"])
print("CGPA       :", students[0]["CGPA"])

# Display Student 2 Details
print("\nStudent 2 Details")
print("----------------------------")
print("Roll No    :", students[1]["Roll No"])
print("Name       :", students[1]["Name"])
print("Age        :", students[1]["Age"])
print("Department :", students[1]["Department"])
print("CGPA       :", students[1]["CGPA"])
