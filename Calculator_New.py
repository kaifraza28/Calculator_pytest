def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mult(a,b):
    return a*b
def div(a,b):
    return a/b
if __name__=="__main__":
    num1 = int(input("Please Enter  your 1st number:\n"))
    num2 = int(input("Please Enter  your 2nd number:\n"))
    print(add(num1,num2))
    print(sub(num1,num2))
    print(mult(num1,num2))
    print(div(num1,num2))
