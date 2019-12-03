# coded by Park, Sehyun*-

import os

class Student:
    Name = ""
    Username = ""
    Password = ""
    
    def __init__(self, name):
        self.Name = name
        self.courseTaking = []
        
    def __init__(self, name, username, password):
        self.Name = name
        self.Username = username
        self.Password = password
        self.courseTaking = []
    
    def setUsername(self, username):
        self.Username = username
        
    def setPassword(self, password):
        self.Password = password
        
    def addCourse(self, course):
        self.courseTaking.append(course)
    
    def removeCourse(self, course):
        self.courseTaking.remove(course)
        

class Admin:
    Name = ""
    Username = ""
    Password = ""
    
    def __init__(self, name):
        self.Name = name
        
    def __init__(self, name, username, password):
        self.Name = name
        self.Username = username
        self.Password = password
    
    def setUsername(self, username):
        self.Username = username
        
    def setPassword(self, password):
        self.Password = password  
    
    def addCourse(self, course):
        self.courseTaking.append(course)
    
    def removeCourse(self, course):
        self.courseTaking.remove(course)
        
        
        
class Class:
    Name = ""
    Code = ""
    Pre_requisite = ""
    Unit = ""
    Limit = ""
    currentLimit = 0;
    
    def __init__(self, name, code, prerequisite, unit, limit):
        self.Name = name
        self.Code = code
        self.Pre_requisite = prerequisite
        self.Unit = unit
        self.Limit = int(limit)
    
    def increaseLimit (self, number):
        self.currentLimit += int(number)
    def decreaseLimit (self, number):
        self.currentLimit -= int(number)

Students = []
Classes = []
Admins = []

# These are existing student        
Park = Student('Park', 'Username', 'Password')
John = Student('John', 'USN', 'PWD') 
Students.append(Park)
Students.append(John)

Florante = Admin('Salvador', 'admin', 'admin')
Shirley = Admin('Shirly', 'ADMIN', 'ADMIN')
Ureta = Admin('Ureta', 'myteacherin', 'ccprog1')
Admins.append(Florante)
Admins.append(Shirley)
Admins.append(Ureta)


# These are existing classes
CSALGCM = Class('CSALGCM', "1190201", "CSMATH2", "4", "10")
CSINTSY = Class('CSINTSY', "1190202", "CCDSLGO", "4", "12")
Classes.append(CSALGCM)
Classes.append(CSINTSY)
clear = "\n" * 100

quit = -1

while (quit != 1 or quit > 2 or quit < 1):

    print(clear)
        
    print("Welcome to the Enlistment Page!!")
    SorA = input ("Are you an admin or a student? \n1 for Student\n2 for Admin\n = ")
    
    print(clear)
    
    if SorA == '1':
        login = input("Are you an existing student or not\n1 for existing student\n2 for new student\n = ")
        
        correctinfo = 0
        
        if login == '1':
            
            num = 0
            
            print(clear)
            
            print("Pick a corresponding number for your name among these list")
            for num in range(len(Students)):
                print("\n", num+1, Students[num].Name)
            select = int(input(" = "))
            username = input("Type in your username : ")
            password = input("Type in your password : ")
            if (username != Students[select-1].Username):
                print("Wrong Username!")
            if (password != Students[select-1].Password):
                print("Wrong Password!")
            else:
                correctinfo += 1
            
            if (correctinfo == 1):              
                print(clear)
                
                print("\nWelcome " + Students[select-1].Name)
                
                if (correctinfo == 1):
                    print("What is your errand today?")
                    errand = int(input("1 for Take course\n2 for Drop course\n = "))
                    
                    if errand == 1:
                        
                        escape = -1
                        
                        print(clear)
                        
                        while (escape != 0):
                            print("\nPick a course to add")
                            print("\n  0 Stop adding")
                            for num in range(len(Classes)):
                                print(" " , num+1, Classes[num].Name)
                            escape = int(input(" = "))
                            print(clear)
                            if Classes[escape-1].currentLimit == Classes[escape-1].Limit:
                                print("\nSorry!, this course has reached its maximum unit!")
                                escape = 0
                            elif(escape!=0):
                                Students[select-1].courseTaking.append(Classes[escape-1])
                                Classes[escape-1].increaseLimit('1')
                            
                        print("You are currently taking these subjects!\n")
                        for num in range(len(Students[select-1].courseTaking)):
                            print(Students[select-1].courseTaking[num].Name)
                            
                    if errand == 2:
                        
                        escape = -1
                        
                        print(clear)
                        
                        while (escape != 0):
                            if len(Students[select-1].courseTaking) > 0:
                                print("\nPick a course to remove")
                                print("\n  0 Stop removing")
                                if (len(Students[select-1].courseTaking) > 0):
                                    for num in range(len(Students[select-1].courseTaking)):
                                        print(" ", num+1, Students[select-1].courseTaking[num].Name)
                                escape = int(input(" = "))
                                if (escape > 0 and len(Students[select-1].courseTaking) > 0):
                                    Students[select-1].courseTaking[escape-1].decreaseLimit(1)
                                    Students[select-1].removeCourse(Students[select-1].courseTaking[escape-1])
                                print(clear)
                            else:
                                escape = 0
                                print("You are currently taking no course!")
         
    
                    
        if login == '2':
            
            num = 0
            
            print(clear)
            
            name = input("what is your name?: ")
            username = input("what will be your username?: ")
            password = input("What will be your password>: ")
            
            name = Student(name, username, password)
            Students.append(name)
            
            print(clear)
            
            print("\nWelcome " + Students[len(Students)-1].Name)
        
            print("What is your errand today?")
            errand = int(input("1 for Take course\n2 for Drop course\n = "))
            
            print(clear)
            
            if errand == 1:
             
                esc = -1
                
                while (esc != 0):
                    print("\nPick a course to add")
                    print("\n  0 Stop adding")
                    for num in range(len(Classes)):
                        print(" ", num+1, Classes[num].Name)
                    esc = int(input(" = "))
                    print(clear)
                    if Classes[esc-1].currentLimit == Classes[esc-1].Limit:
                        print("\nSorry!, this course has reached its maximum unit!")
                        esc = 0
                    elif (esc!=0):
                        name.addCourse(Classes[esc-1])
                        Classes[esc-1].increaseLimit('1')
                print("You are currently taking these subjects!\n")
                if (len(Students[len(Students)-1].courseTaking) > 0):
                    for num in range(len(Students[len(Students)-1].courseTaking)):
                        print(Students[len(Students)-1].courseTaking[num].Name)
                    
            if errand == 2:
                
                print(clear)
            
                print("You are currently taking no course!")
                            
        
        
    elif SorA == '2':
        login = input("Are you an existing admin or not\n1 for existing admin\n2 for new admin\n = ")
            
        correctinfo = 0
        
        if login == '1':
            
            num = 0
            
            print(clear)
            
            print("Pick a corresponding number for your name among these list")
            for num in range(len(Admins)):
                print("\n", num+1, Admins[num].Name)
            select = int(input(" = "))
            username = input("Type in your username : ")
            password = input("Type in your password : ")
            if (username != Admins[select-1].Username):
                print("Wrong Username!")
            if (password != Admins[select-1].Password):
                print("Wrong Password!")
            else:
                correctinfo += 1
            print(clear)
                
        if login == '2':
            print(clear)
            name = input("What is your name?: ")
            username = input("What will be your username?: ")
            password = input("What will be your password?: ")
            name = Admin(name, username, password)
            Admins.append(name)
            
    
        if (correctinfo == 1 or login == '2'):
            print(clear)
            if (correctinfo == 1):
                print("\nWelcome " + Admins[select-1].Name)
            else:
                print("\nWelcome " + Admins[len(Admins)-1].Name)
            print("What is your errand today?")
            errand = int(input("1 for Create course\n2 for Remove course\n = "))
            
            print(clear)
            
            if errand == 1:
                cName = input("What will be the course name?: ")
                cCode = input("What will be the course code?: ")
                cPre = input("What will be its pre-requisite?: ")
                cUnit = input("What will be the unit? : ")
                cLimit = input("What will be the limit: ")
                
                cName = Class(cName, cCode, cPre, cUnit, cLimit)
                Classes.append(cName)
                  
                print("The class our University offers are now as follows!\n")
                for num in range(len(Classes)):
                    print(Classes[num].Name)
                    
            print(clear)
                    
            if errand == 2:
                for num in range(len(Classes)):
                    print(num+1, Classes[num].Name)
                remove = int(input("Which course would you like to remove?: "))
                del Classes[remove-1]
                print("The class our University offers are now as follows!\n")
                for num in range(len(Classes)):
                    print(num+1, Classes[num].Name)
                    
            print(clear)
                    
                         
    quit = int(input("Anything else?\n1. Quit the Program\n2. Go back to main page\n = "))
    print(clear)
    
print("...Terminating, Goodbye- bye!")
        


        
