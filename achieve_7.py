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
print(stuInfo.get("First name"))
print(stuInfo.get("Last name"))
for x in courSel:
    print(course.get(x))
    



    
   




    

    










