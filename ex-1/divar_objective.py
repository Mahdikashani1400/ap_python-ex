from pprint import pprint

class Divar():
    def __init__(self):
        self.datas = {
            "students":{
                
            },
            "professors":{

            },
            "courses":{

            }
        }
    def new_student(self,dep,num):
        if num in list(self.datas['students'].keys()):
            print("student with this student number already exists")
        else:
            self.datas['students'][num] = {
                "dep":dep,
                "courses_name":[],
                "courses_grade":[],
                "grade_avg":-1
            }    
    def new_professor(self,dep,id,name,age):
        if id in list(self.datas['professors'].keys()):
            print("professor with this id already exists")
        else:
            courses_input = input()
            self.datas['professors'][id]= {
                'dep': dep,
                "id":id,  
                'name': name,  
                'age' : age,
                "courses_skills":courses_input.split(' '),
                "courses":{} 
            }
    def new_course(self,dep,name,unit,day,start,end):
        if name in list(self.datas['courses'].keys()):
            print("course with this name already exists")
        else:
           professors_id = list(self.datas['professors'].keys())
           professors_id.sort()
           self.datas['professors']= {id: self.datas['professors'][id] for id in professors_id}
           
           has_professor = False
           professor_target = None
           for professor in list(self.datas['professors'].values()):
               if name in professor["courses_skills"]:
                   has_professor = True
                   professor_target = professor["id"]
                   for course_check in list(professor['courses'].values()):
                       if course_check['day'] ==day and not self.aysync_time(start,end,course_check['start'],course_check['end']):
                           has_professor = False
                           break
                   break
           if has_professor:
               self.datas['courses'][name] = {
                   "dep":dep,"unit":unit,"day":day,"start":start,"end":end,"students":{},
                   "grade_state":False
               }
               self.datas['professors'][professor_target]["courses"][name]={
                   "dep":dep,"unit":unit,"day":day,"start":start,"end":end
               }
               print(professor_target)
           else   :
               print("there is no professor for this course")

    def take_course(self,name,num):
        if name in list(self.datas['courses'].keys()) and num in list(self.datas['students'].keys()):
            if self.datas['courses'][name]['grade_state'] :
                print("it is too late to take this course")
            else:
                self.datas['courses'][name]['students'][num] = -1
                self.datas['students'][num]['courses_name'].append(name)
                

        else:
            print("invalid command")    

    def add_grades(self,name):
        if name not in list(self.datas['courses']):
            print("there is no course with this name")
        else:
            student_nums = list(self.datas['courses'][name]['students'].keys())
            if not len(student_nums):
                print("no student has taken this course")
            elif self.datas['courses'][name]['grade_state']:
                print("grades have already been recorded")
            else:
                grades = input().split(' ')    
                if len(student_nums)!= len(grades):
                    print("the number of grades and students are not equal")
                else:
                    self.datas['courses'][name]['grade_state'] = True
                    student_nums.sort()
                    for i in range(len(grades)):
                        self.datas['courses'][name]['students'][student_nums[i]] = grades[i]
                        self.datas['students'][student_nums[i]]["courses_grade"].append([grades[i],self.datas['courses'][name]['unit']])
                        # معدلو همینجا حساب کن  


    def find_grade(self,name,num):
        if name in list(self.datas['courses'].keys()) and num in list(self.datas['students'].keys()):
            if name not in list(self.datas['students'][num]["courses_name"]):
                print("the student has not taken this course")
            elif not self.datas['courses'][name]['grade_state']:
                print("course grades are not recorded")
            else:
                print(self.num_2point(self.datas['courses'][name]['students'][num]))        

        else:
            print("invalid course name or student number")    

    def find_GPA(self,num):
        if not num in list(self.datas['students'].keys()):
            print("there is no student with this number")
        else:
            
            if not len(self.datas['students']['courses_grade']):
                print("no grades have been recorded for this student")
            # else:
                # grade_avg = 
                # print(self.num_2point())







    
                
                       
               
                
    def aysync_time(self,start1,end1,start2,end2):
     isTime = True     
     for i in range(start1,end1):
          for j in range(start2,end2):
               if int(i)==int(j):
                    isTime=False
     return isTime
    
    def num_2point(self,num):
     num_round = str(round(float(num),2))
     if len(str(num_round).split('.')[1])==1:
          num_round = str(num_round)+'0'
     return num_round 
        





            

test = Divar()        

test.new_student('ie',40020)
test.new_student('ie',40023)
test.new_student('ie',40024)
print(test.datas['students'])
test.new_student('ie',40020)
test.new_professor("ie",22,"ali",22)
# test.new_professor("ie",26,"ahmad",26)
# test.new_professor("ie",18,"ali",33)
test.new_course("ie","ap",3,"sun",1,3)
test.new_course("ie","ai",4,"sun",3,5)
test.take_course("ap",40023)
test.take_course("ap",40024)
test.take_course("ap",40020)
test.add_grades("ap")
test.find_grade("ap",40023)
# test.find_GPA(40023)


pprint(test.datas)