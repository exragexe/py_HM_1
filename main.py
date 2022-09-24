numbers=int(input("Enter numbers: "))
part1=int(numbers/1000%10)
part2=int(numbers/100%10)
part3=int(numbers/10%10)
part4=int(numbers%10)
res=part4*1000+part3*100+part2*10+part1
print(res)