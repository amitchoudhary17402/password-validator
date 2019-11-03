# Created by Amit-Choudhary
# Python program to check validation of password 
# Module of regular expression is used with search() 
import re 
password=input("enter your password\n")
print(password)
flag = 0
while True: 
    if (len(password)<8): 
        flag = -1
        print("password to small")
        break
    elif not re.search("[a-z]", password): 
        flag = -1
        print("lowercase character missing")
        break
    elif not re.search("[A-Z]", password): 
        flag = -1
        print("uppercase character missing")
        break
    elif not re.search("[0-9]", password): 
        flag = -1
        print("numeric character missing")
        break
    elif not re.search("[_@$]", password): 
        flag = -1
        print("lspecial character missing")
        break
    elif re.search("\s", password): 
        flag = -1
        break
    else: 
        flag = 0
        print("password accepted") 
        break

if flag ==-1: 
    print("Not a Valid Password") 
    print("""the password must follow:-
1.at least 8 characters long
2.must contain any one _@$
3.one capital letter
4.one numeric value""")
#enter Amit@17402 or any you have to check that one

if (flag==0 and (len(password)<=8)):
    print("pass_strength LOW")
elif flag==0 and len(password)>8 and len(password)<=10:
    print("pass_strength MEDIUM")
elif flag==0 and len(password)>10:
    print("pass_strength STRONG")
