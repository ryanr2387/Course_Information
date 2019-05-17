def main():
    course_information1 = get_dictionary1()
    course_information2 = get_dictionary2()
    course_information3 = get_dictionary3()

    print('Enter a course number to get the course information')
    print('The course numbers are: CS101, CS102, CS103, NT110, CM241')

    user_input = input('Enter course number: ')
    print('Room Number: ', course_information1[user_input])
    print('Instructor: ', course_information2[user_input])
    print('Meeting Time: ', course_information3[user_input])

def get_dictionary1():
    course_information =  {'CS101': '3004', 'CS102' : '4501', 'CS103': '6755', 'NT110' : '1244', 'CM241' : '1411'}

    return course_information
def get_dictionary2():
    course_information = {'CS101' : 'Haynes', 'CS102' : 'Alvarado', 'CS103' : 'Rich', 'NT110' : 'Burke', 'CM241' : 'Lee'}

    return course_information

def get_dictionary3():
    course_information = {'CS101' : '8.00 a.m.', 'CS102' : '9:00 a.m.', 'CS103' : '10:00 a.m.', 'NT110' : '11:00 a.m.', 'CM241' : '1:00 p.m.'}

    return course_information

main()