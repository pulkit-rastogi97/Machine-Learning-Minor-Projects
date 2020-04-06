ch=True
while ch:
    try:
        def add(num1,num2):
            return (num1+num2)
        def sub(num1,num2):
            return (num1-num2)
        def mul(num1,num2):
            return (num1*num2)
        def div(num1,num2):
            return (num1/num2)
    
        num1=float(input("Enter a number : "))
        num2=float(input("Enter other number : "))
        val=True
        while val:
            print("===============================")
            print("Choose the operation : ")
            print("1. Addition ( + ) ")
            print("2. Subtraction ( - ) ")
            print("3. Multiplication ( * ) ")
            print("4. Division ( / ) ")
            print("===============================")
            op=int(input())
            if op == 1 :
                print(num1, "+", num2, "=", add(num1,num2))
            elif op == 2 :
                print(num1, "-", num2, "=", sub(num1,num2))
            elif op == 3 :
                print(num1, "/", num2, "=", mul(num1,num2))
            elif op == 4 :
                print(num1, "*", num2, "=", div(num1,num2))
            else :
                print("Sorry !! Wrong Choice Entered...")
                continue
            val=False
    except ValueError: 
        print("Sorry ! You have to type numeric values. ")
        continue
    except ZeroDivisionError: 
        print("Sorry ! You are dividing by zero. ")
        continue
    more=str(input("Press Y to perform more operations : "))
    s=more.lower()
    if(s == "y"):
        ch=True
    else:
        ch=False


