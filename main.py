
numbers = int(input("Enter  numbers: "))
res= int(numbers /100)
res2= int(numbers %100 / 10)
res3=int(numbers %10)
res4=int(res + res2 +res3)

print(res,"\n",res2,"\n",res3,"\n",res4)