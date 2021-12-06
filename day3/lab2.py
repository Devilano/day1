English=int(input("Enter your marks of English:"))
Math=int(input("Enter your marks of Math:"))
Social=int(input("Enter your marks of Social:"))
Science=int(input("Enter your marks of Science:"))
total=English+Math+Social+Science
percentage=(total/400)*100
if percentage >=70:
    print("you got distinction")
elif percentage >=60:
    print("you got first division")
elif percentage >=40:
    print("you got second division")
elif percentage  <=40:
    print("soryy your are fail")




