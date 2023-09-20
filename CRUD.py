import json
maindic={}
print("crud is here, perform your task here")
while True:
    print("1)create\n2)read\n3)update\n4)delete")
    option=int(input("choose an option to move forward.."))
    if option==1:
            name=input("enter the name:- ")
            phone_number=int(input("enter the phone number:- "))
            email=input("enter the email:- ")
            password= (input("enter the account password:-"))
            maindic.update({phone_number:{'name':name , 'email':email , 'password':password,"phone_number":phone_number}})
            print(maindic)
            data=json.dumps(maindic,indent=4)
            with open("temp.json","w") as file:
                 file.write(data)

    elif option==2:
        phone_number=int(input("enter the number>>"))
        if phone_number in maindic:
             print(maindic[phone_number])
        else:
            print("Do not exist")
    elif option==3:
        phone_number=int(input("enter the number>>"))
        if phone_number in maindic:
            print("what you want to update>>")
            option1=int(input("enter the option\n1>name>>\n2>phone_number>>\n3>email>>\n4>password>>"))
            if option1==1:
                name1=input("enter the new name>>")
                maindic[phone_number]["name"]=name1
                print("successfull added new name.")
           
            elif option1==2:
                 phone_number1=int(input("enter the new phone_number>>"))
                 maindic[phone_number]["phone_number"]=phone_number1
                 maindic[phone_number1]=maindic[phone_number]
                 del maindic[phone_number]
                 print("successfully new phone number saves")
            elif option1==3:
                 new_email=input("enter the new email>>")
                 maindic[phone_number]["email"]=new_email
                 print("successfull added new email.")

            
            elif option1==4:
                 new_password=input("enter the new password>>")
                 maindic[phone_number]["password"]=new_password
                 print("successfull added new password.")
            
            else:
                 print("choose the correct option")
        else:
             print("enter wrong phone number")

    elif option==4:
        print("what you want to delete>>")
        option2=int(input("enter the option\n1>name>>\n2>phone_number>>\n3>email>>\n4>password>>\n5>>whole>>"))
        if option2==1:
             phone_number=int(input("enter the phone number"))
             del maindic[phone_number]["name"]
             print("successfully deleted")

        elif option2==2:
             phone_number=int(input("enter the phone number"))
             del maindic[phone_number]["phone_number"]
             print("successfully deleted")

        elif option2==3:
             phone_number=int(input("enter the phone number"))
             del maindic[phone_number]["email"]
             print("successfully deleted")

        elif option2==4:
             phone_number=int(input("enter the phone number"))
             del maindic[phone_number]["password"]
             print("successfully deleted")

        elif option2==5:
             phone_number=int(input("enter the phone number"))
             del maindic[phone_number]
             print("successfully deleted")
        else:
             print("enter the correct option")