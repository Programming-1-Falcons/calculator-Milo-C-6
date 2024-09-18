import math

while True:
    operation = input("Addition(+), Subtraction(-), Division(/), Multiplication(*), or Exponents(^)?: ")
    while operation != "+" and operation!="-" and operation!="/" and operation!="*" and operation!="^":
        print("That's not an operation! Please input the symbol")
        operation = input("Addition(+), Subtraction(-), Division(/), Multiplication(*), or Exponents(^)?: ")

    dontBreak=True #no clue what else to call this

    while dontBreak:
        num0 = input("Input the first number (or pi): ")
        try: 
            num0 = float(num0)
            dontBreak=False
        except: 
            if num0=="pi":
                num0=math.pi
                dontBreak=False
            else:
                print("Thats not a valid input")
            
    dontBreak=True

    while dontBreak:
        num1 = input("Input the second number (or pi): ")
        try: 
            num1 = float(num1)
            if num1==0 and operation=="/":
                print("Can't Devide by 0")
            else:
                dontBreak=False
        except: 
            if num1=="pi":
                num1=math.pi
                dontBreak=False
            else:
                print("Thats not a valid input")

    if operation=="+":
        finalNumber = num0+num1
    elif operation=="-":
        finalNumber = num0-num1
    elif operation=="/":
        finalNumber = num0/num1
    elif operation=="*":
        finalNumber = num0*num1
    else:
        finalNumber = num0**num1

    if num0==math.pi: #the final number is already calculated, all this is used for is printing!
        num0="π"
    if num1==math.pi:
        num1="π"

    print(num0,operation,num1,"=",finalNumber)