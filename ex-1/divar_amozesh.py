from pprint import pprint

datas = {
    "students": [
        {"dep": "CE", "num": 110, "grade_avg": 0, "emergency_remove": ""},
        {"dep": "CE", "num": 111, "grade_avg": 0, "emergency_remove": ""},
        {"dep": "CE", "num": 112, "grade_avg": 0, "emergency_remove": ""}
    ],
    "professors": [
        {
            "id": 22,
            "name": "ali",
            "dep": "ce",
            "courses_skills": ['honar', "riazi"],
            "courses": [
                {
                    "course_name": "riazi",
                    "day": "sun",
                    "start": 9,
                    "end": 11
                }
            ]
        },
        {
            "id": 23,
            "name": "sara",
            "dep": "ce",
            "courses_skills": ['honar', "math"],
            "courses": [
                {
                    "course_name": "math",
                    "day": "mon",
                    "start": 10,
                    "end": 12
                }
            ]
        }
    ],
    "courses": [
        {
            "dep": "ed",
            "name": "maghalat",
            "unit": 5,
            "day": "mon",
            "start": 16,
            "end": 18,
            "professor_state": False,
            "grade_state": False,
            "grade_avg": 0,
            "students": [
                {
                    "num": 222,
                    "grade": 20
                },
                {
                    "num": 333,
                    "grade": 18
                }
            ]
        },
        {
            "dep": "ce",
            "name": "fizik",
            "unit": 3,
            "day": "sun",
            "start": 15,
            "end": 18,
            "professor_state": False,
            "grade_state": False,
            "grade_avg": 0,
            "students": []
        }
    ]
}


def has_student(num_student):
     student_flag = False
     for  student in datas["students"]:
          if num_student == student['num']:
               student_flag= True
         
     return student_flag                         
          

def has_course(course_name):
     course_flag = False
     for  course in datas["courses"]:
          if course_name == course['name']:
               course_flag= True
     return course_flag         
          


def submit_grades_state(course_name):
     submit_flag = False
     for course in datas['courses']:
          if course_name==course['name'] and course['grade_state'] is True:
               submit_flag= True
     print(submit_flag)
     return submit_flag         

def register_student_course_state(course_name,num_student):
     register_student_flag = False
     for course in datas['courses']:
          if course_name==course['name']:
               for student in course['students']:
                    if student['num']==num_student:
                         register_student_flag= True
     return register_student_flag
                    
          
     





def add_student(dep,num):

    has_student= False
    for  student in datas['students']:
        if num==student['num']:
            has_student = True
            print("student with this student number already exists")
    if has_student is False:
              datas["students"].append({
                "dep":dep,
                "num":num,
                "grade_avg":0,
                "emergency_remove":""
            })       

      

def add_professor(dep,id,name,age,courses_skills):
    has_professor = False
    
    for  professor in datas['professors']:
        if id==professor['id']:
            has_professor = True

            print("professor with this id already exists")
    if has_professor is False:
            
            datas["professors"].append({
                "dep":dep,"id":id,"name":name,"age":age,"courses_skills":courses_skills,"courses":[ {"dep": "",
            "name": "",
            "unit": "",
            "day": "",
            "start":"" ,
            "end": "",}]
            })  


def add_course(dep,name,unit,day,start,end):
    has_course = False
    min_professor_id = 10**90
    data_course = {
              "dep":dep,"name":name,"unit":unit,"day":day,"start":start,"end":end,"professor_state":False,"students":[{"num":0,"grade":0}],"grade_state":False,
         }
    for course in datas["courses"]:
        # print(course)
         
        if name==course["name"]:
            has_course = True
            print('course with this name already exists')

    if(has_course is False):
        #  data_course['professor_state'] = True
         for  professor in datas['professors']:

            if dep==professor['dep'] and name in professor["courses_skills"]:
                # print(professor)

                    
                for professor_course in professor["courses"]:
                    if (  professor_course['day'] == day and not (end <= professor_course['start'] or start >= professor_course['end'])):

                        data_course["professor_state"] = False

                    else:
                        data_course['professor_state'] = True

                        if min_professor_id > professor['id']:     
                            pprint("data_course")

                            min_professor_id = professor['id']
                           
         if data_course['professor_state']==True:
            datas['courses'].append(data_course)                    
            for  professor in datas['professors']:
                if min_professor_id==professor['id']:
                    professor['courses'].append(data_course)
                    
         else:
               print('there is no professor for this course')
                        
         

           
def register_course(course_name,num_student):
    
     
     if has_student(num_student) and  has_course(course_name) and not register_student_course_state(course_name,num_student) :
          for course in datas['courses']:
               if course_name==course['name']:
                    if course["grade_state"] is True:
                        print("it is too late to take this course")
                    else:
                         course['students'].append({
                              "num":num_student,
                              "grade":0
                         })

     else:
          print("invalid command")                         
                        
               
# get grades                   
def submit_grade_course(course_name,grades):
     if has_course(course_name):
          for course in datas['courses']:
           if course['name']==course_name:
                    if len(course['students'])==1:
                        print('no student has taken this course')
                    elif course['grade_state']==True:
                            print("grades have already been recorded")
                    else:
                            course["grade_state"] = True
                            try:
                                course['students'].sort(key=lambda x: x['num'])
                            except:
                                ""     
                            if(len(grades)!=len(course['students'])-1):
                                 print("the number of grades and students are not equal")
                            else:
                                 course['students'].sort(key=lambda x :x['num'])
                                #  submit_avg_grade_students([student['num'] for student in course['students']],[grade*course['unit'] for grade in grades])
                                 for i in range(len(grades)):
                                    #    print(course['students'][i+1])
                                       course['students'][i+1]['grade']=grades[i]
                                       get_avg_grade_student(course["students"][i+1]['num'],'update')   
                            # for student in course['students']:
                            #      print(student)        
    
     else:
          print("there is no course with this name")

# def submit_avg_grade_students(num_students,grades):
#      grade_sum = 0
     
#      for student in datas["students"]:
#           for i in range(len(grades)):
#                if student['num'] == num_students[i]:
#                     student['']
                    
                    
               
     
     
     




def get_grade_student(course_name,num_student):
     if has_student(num_student) and has_course(course_name):
          if(register_student_course_state(course_name,num_student) is False):
               print("the student has not taken this course")
          elif submit_grades_state(course_name) is False:
               print("course grades are not recorded")
          else:
               for course in datas['courses']:
                    if course_name==course['name']:
                        
                         for student in course['students']:
                              if student['num']==num_student:
                                   print(round(student['grade'],2))
                   
                   
     else:
          print("invalid course name or student number")    

def get_avg_grade_student(num_student,state=""):
     grade_sum = 0
     count_unit= 0
     grade_exist = False
     if has_student(num_student):
          for course in datas['courses']:
               if course['grade_state']==True:
                    # print(count_unit)
                    
                    for student in course['students']:
                            if student['num']==num_student:
                                count_unit +=course['unit']
                                grade_exist = True
                                # print(student['grade'])
                                grade_sum+=(student['grade']*course['unit'])

          if grade_exist:
               for student in datas['students']:
                    if num_student == student['num']:
                         student['grade_avg'] = round(grade_sum/count_unit,2)
               if state!="update":
                    print(round(grade_sum/count_unit,2)) 
               else:
                    ""    
          else:
               print("no grades have been recorded for this student")
                               

                         
     else:                          
          print("there is no student with this number")                    
                        


def find_rank_of_student                           (num_student):
      dep_student = ''
      grade_student = 0
      students_target = []
      special_grades = []
      if(has_student(num_student)):
           for student in datas['students']:
                # print(student)
                if student['num']==num_student:
                     dep_student=student['dep']
                     grade_student=student['grade_avg']

           for student in datas['students']:
                if student['dep']==dep_student:
                     students_target.append(student)         
                # if student["dep"]==dep_student:
                #      students_target.append(student)
            
           special_grades = list(set([student['grade_avg'] for student in students_target]))
           special_grades.sort(reverse=True)   
           print(special_grades.index(grade_student)+1)              
        #    print(special_grades.index(grade_student)+1)              
                  
                
      else:
           print("there is no student with this number")     


def drop_course(course_name,num_student):
     has_emergency_remove = False
     if(has_student(num_student) and has_course(course_name) and register_student_course_state(course_name,num_student)):
        for student in datas["students"]:
            if student['num']==num_student:    
                if len(student["emergency_remove"]):
                    has_emergency_remove= True
                else:
                     student['emergency_remove']='y'    
        if(submit_grades_state(course_name)):
               print("it is too late to drop this course")
        elif has_emergency_remove:
                   print("the student has already dropped another course")
        else:
             for course in datas["courses"]:
                  if course["name"] == course_name:
                       for student in course["students"]:
                            if student['num']==num_student:
                                 course["students"].remove(student)
     else:
          print("invalid command")
                          
              

def show_the_report_card_of_student(num_student):
     if(has_student(num_student)):
          for course in datas['courses']:
               for student in course['students']:
                    if num_student == student['num']:
                         print(course)
     else:
          print("there is no student with this number")                         
                 
def avg_of_course(course_name):
     sum_grade = 0
     count_student = 0
     for course in datas['courses']:
          if course['name'] == course_name:
               count_student = len(course['students'])-1
               for student in  course['students']:
                    sum_grade+=student['grade']
     print(sum_grade,count_student)              
     return round(sum_grade/count_student,2)                       
                         
def chart_on_grades(course_name,avg):
     valid_command = False
     for course in datas['courses']:
          if course['name']==course_name and len(course['students']) and submit_grades_state(course_name):
                    valid_command = True
               
                    avg_course_var = avg_of_course(course_name)
                    print(avg_course_var)
                    if avg>avg_course_var:
                         for student in course['students']:
                              if student==course['students'][0] is False:
                                   get_avg_grade_student(student['num'],'update')
                                   student['grade']+=(avg-avg_course_var)
                                   if(student['grade']>20):
                                      student['grade'] = 20
                                   

                    else:
                         print("sorry, that is not fair")

     if valid_command is False:
          print("invalid command")
             

    


add_student("iE",40025)
add_student("iE",40030)
add_student("iE",40035)
add_professor("iE",345,"ahmad",49,['math','english','varzesh'])
# print(datas['professors'])
add_course("iE","english",4,"mon",8,11)
add_course("iE","math",4,"mon",12,14)
add_course("iE","varzesh",2,"san",15,18)
register_course("english",40025)
register_course("english",40030)
register_course("math",40030)
register_course("varzesh",40030)
register_course("math",40035)
submit_grade_course("english",[20,18])
# submit_grade_course("math",[13,17])
# submit_grade_course("varzesh",[19])
# get_grade_student("english",40030)
get_avg_grade_student(40025)
find_rank_of_student(40030)
drop_course("math",40030)
drop_course("varzesh",40030)
# show_the_report_card_of_student(40030)
chart_on_grades('english',19.2)
pprint(datas)        
    
# add_course("ce","fizik",3,'sun',15,18)
# add_student('ce',4001022)
# add_professor('ce',32,'mohammad',54)
# print(datas["professors"])
# print(datas["students"])



print(list(set([1,2,3])))








# a= [x==3 for x in [1,2,3,4,3]]
# print(a)
          


          
# a = [{
#      "id":334
# },
# {
#      "id":435
# },{
#      "id":122
# }]
# print(a.sort(key=lambda x : x["id"]))
# print(a)
                         
# a= [1,9,3,7
# ]                         
# a.remove(9)
# print(a)