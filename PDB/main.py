def report(student):
    name=student['name']
    surname=student['surname']
    course=student['course']
    return f'{name} {surname}  took  {course}'

def print_report(students):
    for student in students:
        print(report(student))

if __name__=='__main__':
    students=[
        {'name':'name1','surname':'surname1','age':12,'course':'Python'},
        {'name':'name2','surname':'surname2','age':13,'course':'Java'},
        {'name':'name3','surname':'surname3','age':14,'course':'JavaScript'},
        {'name':'name4','surname':'surname4','age':15},
        {'name':'name5','surname':'surname5','age':16,'course':'C++'},
    ]

    print_report(students)


