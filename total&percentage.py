#student
print(" enter  marks of student 1:")
s1_sub1=int(input("subject 1: "))
s1_sub2=int(input("subject 2: "))
s1_sub3=int(input("subject 3: "))
s1_sub4=int(input("subject 4: "))
s1_sub5=int(input("subject 5: "))
s1_total=s1_sub1+s1_sub2+s1_sub3+s1_sub4+s1_sub5
s1_percentage= (s1_total / 500) * 100

#student
s2_sub1=int(input("subject 2: "))
s2_sub2=int(input("subject 2: "))
s2_sub3=int(input("subject 3: "))
s2_sub4=int(input("subject 4: "))
s2_sub5=int(input("subject 5: "))
s2_total=s2_sub1+s2_sub2+s2_sub3+s2_sub3+s2_sub4+s2_sub5
s2_percentage=(s2_total / 500) * 100

#student
s3_sub1=int(input("subject 1: "))
s3_sub2=int(input("subject 2: "))
s3_sub3=int(input("subject 3: "))
s3_sub4=int(input("subject 4: "))
s3_sub5=int(input("subject 5: "))
s3_total=s3_sub1+s3_sub2+s3_sub3+s3_sub4+s3_sub4+s3_sub5
s3_percentage=(s3_total / 500) * 100

#display result 
print("\n--results---")
print("student 1->total:",s1_total,"percentage:",s1_percentage,"%")
print("student 2->total:",s2_total,"percentage:",s2_percentage,"%")
print("student 3->total:",s3_total,"percentage:",s3_percentage,"%")