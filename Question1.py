# Phone directory with a Menu---------////////////

phoneDirectory={}

print("")
print("!!.....WELCOME TO THE Ronnie'S PHONE DIRECTORY.....!!")
print("")
print("!!....MENU....!!\n 1. Add a record.\n 2. Search a record.\n 3. Update a record.\n 4. Sort the record alphabetically.\n 5. Delete a record.\n 6. Quit.\n ")
print("Enter the MENU NUMBER you want to perform...")
WTD=int(input(":- "))

while (WTD!=7):
    print("!!....MENU....!!\n 1. Add a record.\n 2. Search a record.\n 3. Update a record.\n 4. Sort the record alphabetically.\n 5. Delete a record.\n 6. Quit.\n ")
    print("")
    print("Enter the MENU NUMBER you want to perform...")
    WTD=int(input(":- "))
    print("")


#FOR-1--------------------------************************
    if WTD == 1:
        a=input("Want to add a Record: (y/n): ")
        i=1
        while i==1:
            if a == "y":
                x=input(f"Enter name {i}:- ")
                y=int(input(f"Enter your 10-digit phone number :- "))
                phoneDirectory.update({x:y})
                print("")
                i=i+1
            elif a == "n":
                print("Okay")
            else:
                print("Please answer either y or n.")
                print("")
            i=i+1
        if len(phoneDirectory) > 1:
            print("SORRY THE DIRECTORY IS FULL..........!!!!!!! ")
            print("")


#FOR-2--------------------------************************
    if WTD == 2:
        print("What to search..?\n 1. Whole Directory.\n 2. Specific Directory.")
        b=int(input(":- "))
        i=1
        while i == 1:
            if b == 2:
                p=input("NAME :- ")
                if p in phoneDirectory:
                    print(p," : ",phoneDirectory[p])
                else:
                    print("No Directory exists with this name.!!!!!")
            else:
                if len(phoneDirectory) == 0:
                    print("THE DIRECTORY IS EMPTY...")
                    print("")
                else:
                    print(phoneDirectory)
                    print("")
            i=i+1
            print("")


#FOR-3--------------------------************************
    if WTD == 3:
        phoneDirectory.update()
        if len(phoneDirectory) == 0:
            print("THE DIRECTORY IS EMPTY...")
            print("")
        else:
            print("Updated Directory : ")
            print(phoneDirectory)
            print("")


#FOR-4--------------------------************************



#FOR-5--------------------------************************
    if WTD == 5:
        delete=input("DELETE SOMETHING.........??? (y/n):- ")
        if delete == "y":
            print("what to DELETE")
            c=input(":- ")
            if c in phoneDirectory:
                phoneDirectory.pop(c)
            else:
                print("Contact not found in Directory")

            print("Updated DATA")
            print(phoneDirectory)
            print("")
        else:
            print("Okay")
        print("")


    
    

#FOR-6--------------------------************************
    if WTD == 6:
        print("Terminating..........")
        break

        print("!!....MENU....!!\n 1. Add a record.\n 2. Search a record.\n 3. Update a record.\n 4. Sort the record alphabetically.\n 5. Delete a record.\n 6. Quit.\n ")
        print("")
        print("Enter the MENU NUMBER you want to perform...")
        WTD=int(input(":- "))
        print("")