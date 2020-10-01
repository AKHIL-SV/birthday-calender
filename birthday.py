dict={}
while True:
    print("")
    print("1.Show birthday")
    print("2.Add birthday")
    print("3.Exit")
    c=int(input("enter the choice: "))
    if c==1:
        if(len(dict.keys())==0):
            print("")
            print(".....NOTHING TO SHOW.....")
        else:
            n=input("enter the name for birthday: ")
            bir=dict.get(n,"no data found")
            print(bir)
    elif c==2:
        n=input("enter the name: ")
        d=input("enter birthdate: ")
        dict[n]=d
        print("birthday added")
    elif c==3:
        break
    else:
        print("choose a valid option")
            
