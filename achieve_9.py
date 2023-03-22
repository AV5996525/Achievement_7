#Name:          achieve_7.py
#Author:        AJ Varatharajan
#Date Created:  February 23, 2023
#Date Last Modified: February 23, 2023
#Purpose: User is able to input student information and select courses by inputting the course code when prompted.
#
#This program will output the translation of the course code entered to it's respective course title along with student information. 
from tabulate import tabulate
course = {} #initializing empty dictionary
course = {
    "ENG1221":"English",
    "CRE1342":"Careers",
    "NTB3070":"Networking Basics",
    "SCL1020":"Sociology"
}
stuInfo = {} #initializing empty dictionary
firstN = input("Enter your first name:") #Prompting input for field
stuInfo["First name"] = firstN #Adding input into dictionary associated with value
lastN = input("Enter your last name:") #Prompting input for field
stuInfo["Last name"] = lastN  #Adding input into dictionary associated with value
studN = input("Enter your student number:") #Prompting input for field
stuInfo["Student #"] = studN  #Adding input into dictionary associated with value
courSel = {}
print(dict(course),"\nSelect your courses by entering any of these course codes: ENG1221, CRE1342 , NTB3070, SCL1020\nSeperate your choices with a ','") #printing course items stored in dictrionary
while True:
    try:
        courSel = input().split(",") #Prompting input for field
        for x in courSel:
            if x not in course.keys():
                raise Exception
        stuInfo["Course selection"] = courSel #Prompting input for field
    except:
        print("invalid entry")  
        exiQ = input("Do you want to exit?")
        if exiQ == "1":
            exit()
            break
        elif exiQ == '2':
            continue  
    finally:
        print("Your course registration summary:\n") #output title
        print(tabulate([[(stuInfo.get("First name"))], [(stuInfo.get("Last name"))], [(stuInfo.get("Student #"))]], headers = ["Student Information:"])) #output 
        print(tabulate([[('')]] , headers = ["Course's selected:"])) #output
        for x in courSel: # using for loop to cycle through each entry inputed by user
            print(course.get(x)) #printing the corresponding value for each entry in coursel by referencing the course dictionary




        
    




    

    










