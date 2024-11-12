var=int(input("enter a number "))
if var>1:
    for i in range(2,var):
        if var %i==0:
            print(var,"is not a prime number")
            break
        else:
            print(var,"is a prime number")
else:
    print(var,"is a prime number")