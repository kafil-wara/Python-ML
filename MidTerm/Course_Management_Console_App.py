course_list = []

class Course:
    def __init__(self, code, name, credit, prerequisites):
        self.code = code
        self.name = name
        self.credit = credit
        self.prerequisites = prerequisites

    # def print_Details(self):
    #     for obj in course_List:   
    #         print(self.name)
    #         print(self.code)
    #         print(self.credit)
    #         print(self.prerequisites)

def add_Course():
    code = input("Course Code: ")
    name = input("Name: ")
    credit = input("No. of Credits: ")
    prerequisites = [item for item in input("Prerequisites: ").split()]
    # if len(prerequisites) == 0:
        #     add_Course(code, name, credit, prerequisites)
        # elif prereq_check(prerequisites):
        #     add_Course(code, name, credit, prerequisites)
        # else:
        #     print("?????????????????????????")
    course_list.append(Course(code, name, credit, prerequisites))
    print("Course added!")
    
# def prereq_check(args):
#     for prereqs in args:
#         for courses in course_list:
#             if prereqs not in courses.code:
#                 return False
#             else:
#                 return True

def search(code):
    #USE SINGLE COURSE SHOW FN TO SHOW DEETS
    for obj in course_list:
        if obj.code == code:
            return obj
        else:
            print("Course Not Found!")

def all_course_display():
    for obj in course_list:
            print(obj.code, obj.name, obj.credit, obj.prerequisites)

def single_course_display(code):
    course = search(code)
    if course:
        print(course.code, course.name, course.credit, course.prerequisites)
    ### NEED TO ADD PROMPT TO ADD

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
    code = input("Enter Course Code to update: ")
    course = search(code)
    single_course_display(code)
    print("Please update or leave blank to keep as is")



    

while(True):
    print(
    '''
    1. Add
    2. print deets
    3. single course display
    4. Delete
    5. Update
    '''
    )

    inp = input()
    if inp == '1':
        add_Course()
        
        
    elif inp == '2':
        all_course_display()
    elif inp == '3':
        code = input("Enter Course Code: ")
        single_course_display(code)
    elif inp == '4':
        delete_course()
    elif inp == '5':
        update_course()
    elif inp == 'quit':
        exit()
    else:
        print("XXX")








def perma_store():
    pass


