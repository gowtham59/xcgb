string1=input()
count2=0
for i in string1:
    if(i.isalpha() or i.isdigit()):
      count2=count2+1
if count2!=0:
    print("Yes")
else:
    print("No")
