a=int(input("enter first number: "))
b=int(input("enter second number: "))

print("before swapping:a=",a,",b=",b)

#swapping logic
a=a+b
b=a-b
a=a-b

print("after swapping:a=",a,"b=",b)