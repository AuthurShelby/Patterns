'''
check if the input number is even or odd if it's odd give a diamond shape

'''
userInput = int(input("enter a number: "))
if userInput%2 == 0:
    print("It's Even")
else:
    for row in range(userInput):
        for cols in range(row,userInput):
            print(" ",end="")
        for cols in range(row):
            print("*",end="")
        for cols in range(row-1):
            print('*',end="")
        print()
    for row in range(userInput):
        for cols in range(row):
            print(" ",end="")
        for cols in range(row,userInput):
            print("*",end="")
        for cols in range(row,userInput-1):
            print("*",end="")
        print()
