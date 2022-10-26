import pickle
from fileinput import filename

course_list = []

class Course:
    def __init__(self, code, name, credit, prerequisites):
        self.code = code
        self.name = name
        self.credit = credit
        self.prerequisites = prerequisites

def add_Course(*arg):
    if arg:
        code = ''
        for a in arg:
            code += a
    else:
        code = input("Course Code: ")
    name = input("Name: ")
    credit = input("No. of Credits: ")
    prerequisites = [item for item in input("Prerequisites: ").split()]
    if len(prerequisites) != 0:
        if prereq_check(prerequisites):
            course_list.append(Course(code, name, credit, prerequisites))
            print("Course added!!!")
        else:
            for prereq in prerequisites:
                add_Course(prereq)
            
    else:
        course_list.append(Course(code, name, credit, prerequisites))
        print("Course added!")
    
    
    
def prereq_check(args):
    code_set = set()
    arg_set = set()
    for course in course_list:
        code_set.add(course.code)
    for a in args:
        arg_set.add(a)
    if arg_set.issubset(code_set):
        return True
    else:
        for arg in arg_set:      
            a = set()
            a.add(arg)
            if a.issubset(code_set):
                pass
            else:
                print(arg + " is not in the course list")
                inp = input("Do you want to add this course? Press 1 to add, any other key to pass\n")
                if inp == '1':
                    add_Course(arg)
                else:
                    return False

def search(code):
    for obj in course_list:
        if obj.code == code:
            return obj
    print("Course Not Found!")
    inp = input("Would you like to add this course? Press 1 to add, any other key to pass\n")
    if inp == '1':
        add_Course(code)
    else:
        pass

def all_course_display():
    for obj in course_list:
        print("Course Code: " + obj.code)
        print("Course Name: " + obj.name)
        print("Course Credit: " + obj.credit)
        print("Course Prerequisites: ", end='')
        print(obj.prerequisites)
        print()

def single_course_display(code):
    course = search(code)
    if course:
        print("Course Code: " + course.code)
        print("Course Name: " + course.name)
        print("Course Credit: " + course.credit)
        print("Course Prerequisites: ", end='')
        print(course.prerequisites)
        print()

def delete_course():
    global course_list
    delete_code = input("Enter Course Code: ")
    updated_course_list = [x for x in course_list if x.code != delete_code]
    if len(updated_course_list) == len(course_list):
        print("Course Not Found!")
    else:
        course_list = updated_course_list
        print("Deletion Successful")

def update_course():
    update_code = input("Enter Course Code to update: ")
    course = search(update_code)
    code = course.code
    name = course.name
    credit = course.credit
    prerequisites = course.prerequisites
    single_course_display(code)
    print('''
            Choose info to update:
            1. Name
            2. Code
            3. Credit
            4. Prerequisites
            ''')
    inp = input()
    if inp == '1':
        new_name = input("New Name: ")
        course.name = new_name
        print("Name Updated!")
    elif inp == '2':
        new_code = input("New Code: ")
        course.code = new_code
        print("Code Updated!")
    elif inp == '3':
        new_credit = input("New Credit: ")
        course.credit = new_credit
        print("Credit Updated!")
    elif inp == '4':
        new_prerequisites = [item for item in input("Prerequisites: ").split()]
        if prereq_check(new_prerequisites):
            course.prerequisites = new_prerequisites
            print("Prerequisites Updated!")
        else:
            print("Error updating prerequisites!")
    



def perma_store():
    try:
        with open('storage.pkl', 'wb') as outp:
            pickle.dump(course_list, outp)
            print("Write to file successful")
            outp.close()
    except IOError:
        print("IO Error!")

def read_storage():
    objects = []
    with (open("storage.pkl", "rb")) as openfile:
        c_list = pickle.load(openfile)
    for c in c_list:
        print("Course Code: " + c.code)
        print("Course Name: " + c.name)
        print("Course Credit: " + c.credit)
        print("Course Prerequisites: ", end='')
        print(c.prerequisites)
        print()


    

while(True):
    print(
    '''
    1. Add New Course
    2. Display All Courses
    3. Display Individual Course
    4. Search
    5. Delete Course
    6. Update Course
    7. Store Course List
    8. Read Stored Course List
    Enter 'quit' to exit
    '''
    )

    inp = input("Choose Option: ")
    if inp == '1':
        add_Course()
    elif inp == '2':
        all_course_display()
    elif inp == '3':
        code = input("Enter Course Code: ")
        single_course_display(code)
    elif inp == '4':
        code = input("Enter Course Code to Search: ")
        single_course_display(code)
    elif inp == '5':
        delete_course()
    elif inp == '6':
        update_course()
    elif inp == '7':
        perma_store()
    elif inp == '8':
        read_storage()
    elif inp == 'quit':
        exit()
    else:
        print("Wrong Input")

