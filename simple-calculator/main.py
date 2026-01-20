while True:
    a=int(input("Enter the first number"))
    b=int(input("Enter the second number"))
    user_input=input("Press + for additon \n Press - for subtraction \n Press * for multiplication\n Press / for division \n")
    try:
        match user_input:
            case "+":
                print(a+b)
            case "-":
                print(a-b)
            case "*":
                print(a*b)
            case "/":
                print(a/b)
            case default:
                print("Unexpected selection please try again")
    except Exception as e:
        print("Something went wrong please try again : ",e)
    con=input("Do you want to continue ?.. Press Y ")
    if con.lower()!="y":
        break