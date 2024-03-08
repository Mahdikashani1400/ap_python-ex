from pprint import pprint

datas = {
    "students": [
     #    {"dep": "CE", "num": 110, "grade_avg": 0, "emergency_remove": ""},
     #    {"dep": "CE", "num": 111, "grade_avg": 0, "emergency_remove": ""},
     #    {"dep": "CE", "num": 112, "grade_avg": 0, "emergency_remove": ""}
    ],
    "professors": [
     #    {
     #        "id": 22,
     #        "name": "ali",
     #        "dep": "ce",
     #        "courses_skills": ['honar', "riazi"],
     #        "courses": [
     #            {
     #                "course_name": "riazi",
     #                "day": "sun",
     #                "start": 9,
     #                "end": 11
     #            }
     #        ]
     #    },
     #    {
     #        "id": 23,
     #        "name": "sara",
     #        "dep": "ce",
     #        "courses_skills": ['honar', "math"],
     #        "courses": [
     #            {
     #                "course_name": "math",
     #                "day": "mon",
     #                "start": 10,
     #                "end": 12
     #            }
     #        ]
     #    }
    ],
    "courses": [
     #    {
     #        "dep": "ed",
     #        "name": "maghalat",
     #        "unit": 5,
     #        "day": "mon",
     #        "start": 16,
     #        "end": 18,
     #        "professor_state": False,
     #        "grade_state": False,
     #        "grade_avg": 0,
     #        "students": [
     #            {
     #                "num": 222,
     #                "grade": 20
     #            },
     #            {
     #                "num": 333,
     #                "grade": 18
     #            }
     #        ]
     #    },
     #    {
     #        "dep": "ce",
     #        "name": "fizik",
     #        "unit": 3,
     #        "day": "sun",
     #        "start": 15,
     #        "end": 18,
     #        "professor_state": False,
     #        "grade_state": False,
     #        "grade_avg": 0,
     #        "students": []
     #    }
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

      

def add_professor(dep,id,name,age):
    has_professor = False
    
    for  professor in datas['professors']:
        if id==professor['id']:
            has_professor = True

            print("professor with this id already exists")
    if has_professor is False:
            courses_input = input()
            add_professor
            datas["professors"].append({
                "dep":dep,"id":id,"name":name,"age":age,"courses_skills":courses_input.split(' '),"courses":[]
            })  


def add_course(dep,name,unit,day,start,end):
    has_course = False
    professors_id = []
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
         for professor in datas['professors']:
            professors_state = True


            if  name in professor["courses_skills"]:
                 if len(professor['courses'])!=0:
                      for professor_course in professor["courses"]:
                         if (  (professor_course['day'] == day) and (not (aysync_time(start,end,professor_course['start'],professor_course['end'])))):

                            professors_state = False                    
                 else:
                        
                        professors_id.append(int(professor['id']))
                              
                 if professors_state:
                       professors_id.append(int(professor['id']))
                                      
                
                         
                            
                     
                                  

                           
         if len(professors_id)>0:
            datas['courses'].append(data_course)                    
            for  professor in datas['professors']:
                if min(professors_id)==professor['id']:
                    print(professor['id'])
                    try:
                         professor['courses'].append(data_course)
                    except:
                         professor['courses'] = []     
                         professor['courses'].append(data_course)

                    
         else:
               print('there is no professor for this course')
                        
         



def aysync_time(start1,end1,start2,end2):
     isTime = True     
     for i in range(start1,end1):
          for j in range(start2,end2):
               if int(i)==int(j):
                    isTime=False
     return isTime


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
def submit_grades_course(course_name):
     if has_course(course_name):
          for course in datas['courses']:
           if course['name']==course_name:
                    if len(course['students'])==1:
                        print('no student has taken this course')
                    elif course['grade_state']:
                            print("grades have already been recorded")
                    else:
                            
                        
                            
                            
                            grades = [round(float(grade),2) for grade in input().split(' ')]         
                            if(len(grades)!=len(course['students'])-1):
                                 print("the number of grades and students are not equal")
                            else:
                                 course["grade_state"] = True
                                 course['students'].sort(key=lambda x :x['num'])
                                 course['grade_avg'] = round(float(sum(grades)/len(grades)),2)
                                 for i in range(len(grades)):
                                
                                       course['students'][i+1]['grade']= grades[i]
                                       get_avg_grade_student(course["students"][i+1]['num'],'update')   
                             
    
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
                                   print(round(float(student['grade']),2))
                   
                   
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
                         student['grade_avg'] = round(float(grade_sum/count_unit),2)
               if state!="update":
                    print(round(float(grade_sum/count_unit),2)) 
           
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
     student_info = []
     student_info.append(f"student number: {num_student}")
     for student in datas['students']:
          if(num_student==student['num']):
               student_info.append(f"department: {student['dep']}")
     if(has_student(num_student)):
          datas['courses'].sort(key=lambda x : x['dep'])
          for course in datas['courses']:
               for student in course['students']:
                    if num_student == student['num']:
                         course_name =str( course['name'])
                         course_unit =str( course['unit'])
                         if course['grade_state']:
                                course_avg_grades =str( course['grade_avg'])
                                student_grade =str( student['grade'])
                              
                              
                                
                         else:
                              course_avg_grades ="None"
                              student_grade ="None"
                         # print([course_name,course_unit,student_grade,course_avg_grades,])     
                         student_info.append(" ".join([course_name,course_unit,student_grade,course_avg_grades]))
                         student_info
          # print (student_info)
          for i in student_info:
               print(i)                                         


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
                   
     return (round(float(sum_grade/count_student),2))                       
                         
def chart_on_grades(course_name,avg):
     valid_command = False
     for course in datas['courses']:
          if course['name']==course_name and len(course['students']) and course['grade_state']:
                    valid_command = True
               
                    avg_course_var = avg_of_course(course_name)
                    if avg>avg_course_var:
                         course['grade_avg']+=round(float(avg-avg_course_var),2)
                         for student in course['students']:
                              if student['num']!=0:

                                   # print(round(avg-avg_course_var,2))

                                   
                                   student['grade']+=round(float(avg-avg_course_var),2)
                                  
                                   if(student['grade']>20):
                                      student['grade'] = 20
                                   get_avg_grade_student(student['num'],'update')   
                                   

                    else:
                         print("sorry, that is not fair")

     if valid_command is False:
          print("invalid command")
             

    


# add_student("iE",40025)
# add_student("iE",40030)
# add_student("iE",40035)
# add_professor("iE",345,"ahmad",49,['math','english','varzesh'])
# # print(datas['professors'])
# add_course("iE","english",4,"mon",8,11)
# add_course("iE","math",4,"mon",12,14)
# add_course("iE","varzesh",2,"san",15,18)
# register_course("english",40025)
# register_course("english",40030)
# register_course("math",40030)
# register_course("varzesh",40030)
# register_course("math",40035)
# submit_grades_course("english",[20,18])
# # submit_grades_course("math",[13,17])
# # submit_grades_course("varzesh",[19])
# # get_grade_student("english",40030)
# get_avg_grade_student(40025)
# find_rank_of_student(40030)
# drop_course("math",40030)
# drop_course("varzesh",40030)
# # show_the_report_card_of_student(40030)
# chart_on_grades('english',19.2)
# pprint(datas)        


def split_input(user_input):
     try:
            input_list=(user_input.split(" ")[0]+" "+user_input.split(' ')[1])
     except:
          ""        
     return input_list

while True:
     user_input = input()
     input_spread = user_input.split(' ')
     answer_list = []
     if user_input=="exit":
          break
     elif split_input(user_input)=='add student':
        answer_student=  add_student(input_spread[2],int(input_spread[3]))
        answer_list.append(answer_student)
     elif split_input(user_input)=="add professor":
           
         professor_answer =  add_professor(input_spread[2],int(input_spread[3]),input_spread[4],int(input_spread[5]))
         answer_list.append(professor_answer)
     elif split_input(user_input)=="add course":
          answer_course=add_course(input_spread[2],
                     input_spread[3],int(input_spread[4]),input_spread[5],int(input_spread[6]),int(input_spread[7]))
          answer_list.append(answer_course)
     elif split_input(user_input)=="take course":
          answer_register_course = register_course(input_spread[2],int(input_spread[-1]))
          answer_list.append(answer_register_course)
     elif split_input(user_input)=="add grades":
          answer_submit_grades = submit_grades_course(input_spread[3])
          answer_list.append(answer_submit_grades)
     elif split_input(user_input)=="find grade":
          answer_find_grade = get_grade_student(input_spread[3],int(input_spread[-1]))
          answer_list.append(answer_find_grade)
     elif split_input(user_input)=="find GPA":
          answer_get_avg = get_avg_grade_student(int(input_spread[-1]))
          answer_list.append(answer_get_avg)
     elif split_input(user_input)=="find rank":
          answer_find_rank =find_rank_of_student(int(input_spread[-1]))
          answer_list.append(answer_find_rank)
     elif split_input(user_input)=="drop course":
          answer_drop_course =drop_course(input_spread[2],int(input_spread[-1]))
          answer_list.append(answer_drop_course)
     elif split_input(user_input)=="show the" and input_spread[2]=='report':
          answer_show_card =show_the_report_card_of_student(int(input_spread[-1]))
          # for i in answer_show_card:
          #      answer_list.append(answer_show_card)

     elif split_input(user_input)=="have mercy":
          answer_chart_grades =chart_on_grades(input_spread[6],float(input_spread[-1]))




# add student ME 97654321
# add student ce 10
# add professor ch 11 Amiri 41
# AP DSD phy
# add course ce FP 3 sat 9 11
# add course ce AP 3 tue 10 12
# take course AP for student 10
# take course AP for student 97654321
# add grades of AP course
# 11 16.75 18.9
# add grades of AP course
# 11 16.75
# find grade of AP course for student number 10
# find rank of student 10
# drop course AP for student 97654321
# show the report card of student 10
# have mercy on the students of AP course, expected average 19.1
# find grade of AP course for student number 97654321
# exit          
          



# there is no professor for this course
# 11
# the number of grades and students are not equal
# 11.00
# 1
# it is too late to drop this course
# student number: 10
# department: ce
# AP 3 11.00 13.88
# 20.00

          



          
# add student CH 24
# add student CH 13
# add student CH 16
# add student CE 7
# add student PHY 48
# add student CH 34
# add student CH 30
# add student CH 37
# add professor PHY 11 C 45
# AC PC AP AB AB
# add professor CH 18 D 31
# AB AP PA PC AC
# add professor CH 2 C 33
# PA AP AP AB AC
# add professor CH 21 G 35
# HR AP ML AB PA
# add professor PHY 7 B 43
# PA AP AB AP AC
# add course PHY PA 4 son 10 11
# add course PHY Pl 2 son 12 16
# add course PHY ML 4 sat 9 13
# add course CH AP 4 sat 9 13
# add course CH PC 1 son 11 15
# add course PHY Pl 3 sat 11 14
# add course PHY AB 1 sat 12 13
# add course CH PC 4 sat 10 14
# add course PHY PC 1 sat 12 14
# add course PHY Pl 1 sat 11 12
# add course CE HR 1 sat 10 13
# add course PHY AC 1 tue 11 14
# add course CE HR 1 sat 9 11
# add course PHY Pl 1 son 11 13
# exit




# 2
# there is no professor for this course
# 21
# 2
# 11
# there is no professor for this course
# 7
# course with this name already exists
# course with this name already exists
# there is no professor for this course
# there is no professor for this course
# 2
# there is no professor for this course
# there is no professor for this course

# pprint(datas)



               




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
          



# add student phy 7413
# add student me 7413
# add student me 2
# add student me 34
# add professor me 34 ahmadi 60
# phy ml LA
# add course ce ml 3 sat 12 14
# add course ma LA 4 sat 13 15

# add professor ma 50 akbari 39
# LA
# add course ma LA 4 sat 13 15
# take course phy for student 11
# take course LA for student 34
# take course ml for student 34
# show the report card of student 34
# exit



# student with this student number already exists
# 34
# there is no professor for this course
# 50
# invalid command
# student number: 34
# department: me
# LA 4 None None
# ml 3 None None          

# pprint(datas)          

