import user
import os
from docs import Document
flag=True
currentUser=None
def app():
    print('select :')
    print('\t1)Sign up')
    print('\t2 Log in')
    print('\t3 exit')
    choice = int(input())
    os.system("cls")
    if(choice == 3):
        global flag
        flag= False
        return
    elif(choice == 2):
        email=input("Enter mail id: ")
        os.system("cls")
        if(email in user.User.list_of_users.keys()):
            i=0
            while(i<3):
                passwrd=input("Enter password: ")
                if(User.list_of_users[email].login(passwrd)):
                    print("Login Success")
                    if(currentUser is not None):
                        currentUser.switch()
                    currentUser = User.list_of_users[email]
                else:
                    print(str(2-i)+ "attempts remaining")
                    input()
                    os.system("cls")
            if(i==3):
                return
        else:
            print("Email id has not been registered with us\nKindly Sign Up with us")
            input()
            return
    elif(choice == 1):
        email = input("Enter email: ")
        passwrd = input("Enter password: ")
        name = input("Enter name: ")
        age = input("Enter age: ")
        ph_no = input("Enter phone number: ")
        User(email,passwrd,name,age,ph_no)
        return
    os.system("cls")
    app_flag=True
    while(app_flag):
        os.system("cls")
        print("t\t\tWelcome "+currentUser.name)
        print("Select: ")
        print("\t1)Upload a file")
        print("\t2)Open a file")
        print("\t3)Switch account")
        print("\t4)Log Out")
        en = input("input choice: ")
        if(en == '4'):
            currentUser.logout()
            currentUser = None
            app_flag=False
            break
        elif(en == '3'):
            currentUser.switch()
            ch = 1
            emp =[]
            for i in user.User.list_of_user.keys():
                if i == currentUser.email:
                    continue
                print(str(ch)+ i)
                emp.append(i)
                ch+=1
            id = int(input())
            currentUser = emp[id-1]
        elif(en == '2'):
             open_file = input("Enter FILE name: ")
             currentUser.open_file(open_file)
             print("File Opened" +str(Document.all_files[open_file].count)+"views")
        elif(en == '1' ):
             open_file = input("Enter FILE name: ")
             currentUser.upload_file(open_file)
             print("File Uploaded")
while flag:
    os.system("cls")
    app()
print('Exitiing.......')
input()
