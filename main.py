print("Welcome to the to do list made by Atharv Sharma")
print("Enter your 5 important tasks for the day")
t1 = str(input("Enter your first task: "))
t2 = str(input("Enter your second task: "))
t3 = str(input("Enter your third task: "))
t4 = str(input("Enter your fourth task: "))
t5 = str(input("Enter your fifth task: "))  

i = 0
while i <= 0:
    inp = input("Do you want to print the tasks?(yes or no):  ")
    if inp.lower() == "yes":
        print(t1)
        print(t2)
        print(t3)
        print(t4)
        print(t5)
    elif inp.lower() == "no":
        print("k")
    else:
        print("ERROR OPTION NOT AVAILIBLE")
        
    inp2 = input("Do you want to delete a task? (yes or no)")
    if inp2.lower() == "yes":
        inp3 = int(input("Enter the task number you want to delete"))
        if inp3 == 1:
            t1 = "---"
            print("task deleted")
        elif inp3 == 2:
            t2 = "---"
            print("task deleted")
        elif inp3 == 3:
            t3 = "---"
            print("task deleted")
        elif inp3 == 4:
            t4 = "---"
            print("task deleted")
        elif inp3 == 5:
            t5 = "---"
            print("task deleted")
        else:
            print("WRONG OPTION")
    elif inp2.lower() == "no":
        print("OK")
    inp3 = input("Do you want to add a task?(yes or no) : ")
    if inp3.lower() == "yes":
        inp4 = input("Enter the task number to replace or add task to: ")
        inp5 = input("Enter the task to add: ")
        if inp4 == 1:
            t1.replace(t2,inp5)
        elif inp4 == 2:
            t2.replace(t2,inp5)
        elif inp4 == 3:
            t3.replace(t3,inp5)
        elif inp4 == 4:
            t4.replace(t4,inp5)
        elif inp4 == 5:
            t5.replace(t5,inp5)
        else:
            print("WRONG INPUT")