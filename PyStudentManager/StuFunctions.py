#students array
students = []

def get_student_title_list():
    student_titles = []
    for student in students:
        student_titles.append(student["name"], student['StudentID'])
    return student_titles

def print_student_title_list():
    student_printlist = get_student_title_list()
    for student in student_printlist:
        print(f"Rollnumber:{student['StudentID']},Student Name:{student['name']}")

def addStudent(name,student_id=999):
        student = {"name":name,"StudentID":student_id}
        students.append(student)

def save_studetails(student_name,student_id):
    f = open('studentdetails.txt', 'a')
    f.write(f'{student_name},{student_id}\n')
    f.close()

def read_studetails():
    f = open('studentdetails.txt', 'r')
    allstulist = f.readlines()
    for student in allstulist:
        student_temp = student.split(',', 1)
        student_name = student_temp[0]
        student_ID = student_temp[1]
        print(f'StudentID:{student_ID}\tStudentName:{student_name}')

read_studetails()

#student_name = str(input("Enter Student Name:"))
#student_id = int(input("Enter Student ID and the Default ID is 999:"))
# addStudent(student_name, student_id)
#save_studetails(student_name, student_id)




