string=input ("enter a string")

print("length of string:",len(string))
print("uppercase :", string.upper())
print("lowercase :" ,string.lower())
if len (string)>0:
    print("first character:",string[0])
    print("second charecter:",string[-1])
else:
    print("string is empty.")
    print("reversed string: ",string[ ::-1])
