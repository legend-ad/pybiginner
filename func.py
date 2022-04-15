#WITHOUT ARGUMENT+ NO RETURN TYPE


def add():
    a=int(input("Enter the number "))
    b=int(input("Enter the number "))
    c=a+b
    print("The answer is : ",c)
add()

#WITH ARGUMENT
def sub(a,b):
    c=a-b
    print("The defference is : ",c)
sub(34,23)

#WITH0Ut ARGUMENT+  RETURN TYPE


def mul():
    a=int(input("Enter the number "))
    b=int(input("Enter the number "))
    c=a*b
    return c
x=mul()
print("The answer is ",x)

#WITH ARGUMENT
def div(a,b):
    c=a/b
    return c
x=div(6,2)
print("The answer is ",x)
