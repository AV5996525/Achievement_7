course = {}
course = {
    "English":"ENG1221",
    "Careers":"CRE1342",
    "Networking Basics":"NTB3070",
    "Sociology":"SCL1020"
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





