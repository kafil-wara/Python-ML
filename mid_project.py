course_list = []

def prereq_check(code):
    for list in course_list:
        for i in list:
            if i != code:
                print("??????????????????????????????")

def delete_course():
    code = input("Code of the Course to be deleted: ")
    for list in course_list:
        for i in list:
            if i == code:
                pass

def add_course():
    code = input("Course Code: ")
    name = input("Name: ")
    credit = input("No. of Credits: ")
    prerequisites = [item for item in input("Prerequisites: ").split()]
    course = [code, name, credit, prerequisites]
    course_list.append(course)
    print("Course successfully added!")
    

while(True):
    print(
    '''
    1. Add
    2. print deets
    '''
)
    inp = input()
    if inp == '1':
        add_course()        
    elif inp == '2':
        
    elif inp == 'quit':
        exit()
    else:
        print("XXX")






















# course_List = {}

# class Course:
#     def __init__(self, name, code, credit, prerequisites):
#         self.name = name
#         self.code = code
#         self.credit = credit
#         self.prerequisites = prerequisites

# while(True):
#     print(
#     '''
#     1. Add
#     2. print deets
#     '''
# )
#     inp = input()
#     if inp == '1':
#         name = input("Name: ")
#         code = input("Course Code: ")
#         credit = input("No. of Credits: ")
#         prerequisites = [item for item in input("Prerequisites: ").split()]
#         course_List[code] = Course(name, code, credit, prerequisites)
        
#     elif inp == '2':
#         for i in course_List.values():
#             print(i)
#     elif inp == 'quit':
#         exit()
#     else:
#         print("XXX")















# # c1 = Course("PIP", "CSE401", 3, ["algo", "data structure"])
# # c1.print_Details()