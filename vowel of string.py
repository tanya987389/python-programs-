string=input("enter a string:")

vowels="aeiouAEIOU"

count=0
for char in string:
    if char in vowels:
        count+=1
        print(f" no. of vowels in the string: {count}")