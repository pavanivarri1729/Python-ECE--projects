a=int(input("enter any numbers"))
total=0
for i in range(1,a+1):
 count=0
  for j in range(1,i+1):
    if i%j==0:
      count+=1
  if count==2:
    total+=1
print(total)
 
