try:
    num=int(input("Enter a number : "))
    n=0
    for i in range(2,num//2+1):
        if(num%i==0):
            n=n+1
    if(n<=0):
        print(num, "is a Prime number")
    else:
        print(num, "is not a Prime number")

except ValueError:
    print("Please type a numerical value")
