#Name:          achieve_7.py
#Author:        AJ Varatharajan
#Date Created:  February 23, 2023
#Date Last Modified: February 23, 2023
#Purpose: User is able to input student information and select courses by inputting the course code when prompted.
#
#This program will output the translation of the course code entered to it's respective course title along with student information. 
from tabulate import tabulate
course = {}
course = {
    "ENG1221":"English",
    "CRE1342":"Careers",
    "NTB3070":"Networking Basics",
    "SCL1020":"Sociology"
}
stuInfo = {}
firstN = input("Enter your first name:")
stuInfo["First name"] = firstN
lastN = input("Enter your last name:")
stuInfo["Last name"] = lastN
studN = input("Enter your student number:")
stuInfo["Student #"] = studN
print(list(course),"\nSelect your courses by entering any of these course codes: ENG1221, CRE1342 , NTB3070, SCL1020\nSeperate your choices with a ','")
courSel = input().split(",")
stuInfo["Course selection"] = courSel
print("Your course registration summary:\n")
print(tabulate([[(stuInfo.get("First name"))], [(stuInfo.get("Last name"))], [(stuInfo.get("Student #"))]], headers = ["Student Information:"]))
print(tabulate([[('')]] , headers = ["Course's selected:"]))
for x in courSel:
    print(course.get(x))




    
   




    

    










