class Student:
    def GetStuden(self):
        self.__rollno = input("Enter Roll No : ")
        self.__name = input("Enter name: ")
        self.__pysiscsmarks = int(input("Enter Physics Marks:"))
        self. __chemistyMarks = int(input("Enter Chemistry Marks: "))
        self.__mathMarks = int(input("Enter Maths Marks: "))
        return(self.__rollno)
    
    def PutStudent(self):
        print(self.__rollno,self.__name,(round((self.__pysiscsmarks+self.__chemistyMarks+self.__mathMarks)/3)))
    def Search(self,min,max):
        per = round((self.__pysiscsmarks+self.__mathMarks+self.__chemistyMarks)/3)
        if(per>= min and per<=max):
            return True
        else:
            return False

studentDict = dict()
n = int(input("How Many Students you want to Input? : "))
for i in range(n):
    S= Student()
    rollno = S.GetStuden()
    studentDict.setdefault(rollno,S)

#Searching for student records with roll numhers provided by the user.
rollno = input("Enter Roll Number you want to Search? : ")
S = studentDict.get(rollno,"Not Found!")
if(isinstance(S,Student)):
    S.PutStudent()
else:
    print(S)

# Printing records of all users with marks greater than 60%
print("All students who scored more than 60 percentage are :")
gradeAStudent = list(filter(lambda s:s.Search(60,100),studentDict.values()))
if(len(gradeAStudent)==0):
    print("Record Not FOund!")
else:
    for S in gradeAStudent:
        S.PutStudent()
