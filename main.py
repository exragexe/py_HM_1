numb=(int(input("Enter numbers: ")))
part1=int(numb/1000%10)
part2=int(numb/100%10)
part3=int(numb/10%10)
part4=int(numb%10)
res=part1*part2*part3*part4
print(res)