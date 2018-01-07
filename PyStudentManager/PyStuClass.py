# Defining Student Class Example

class Student:
    def Read_StudentList(self):
        studentlist = []
        f = open('studentdetails.txt', 'r')
        for line in f.readlines():
            line = line.split(',')
            student_name = line[0]
            student_id = line[1].replace('\n', '')
            studentlist_temp = {"name": f'{student_name}', "id": f'{student_id}'}
            studentlist.append(studentlist_temp)
        return studentlist

student_details = Student()
print(student_details.Read_StudentList())
