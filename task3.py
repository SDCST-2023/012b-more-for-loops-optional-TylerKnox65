#!python3

"""
Similar to task2.py
Program will ask the user to enter their username and password
If the username is a match, see if the password is the correct one
annie's password is 12345
betty's is password
etc.

"""

users = ["annie","betty","charles","doug","eddie","flon"]
passwords = ["12345","password","iloveyou","mom","default","0"]
'''
userlogin = str(input("Enter user: "))
passlogin = str(input("Enter pass: "))
if passlogin in passwords and userlogin in users:
    userindex = users.index(userlogin)
    passindex = passwords.index(passlogin)
else:
    print("denied")
if userindex == passindex:
    print("access granted")
else:
    print("denied")
'''
userlogin = str(input("Enter user: "))
passlogin = str(input("Enter pass: "))
for i in users:
    if users.index(userlogin) == passwords.index(passlogin):
        print("access granted")
        exit()
print("denied")
