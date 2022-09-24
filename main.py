num1=int(input("Enter number: "))
num2=int(input("Enter number: "))
num3=int(input("Enter number: "))
res=str(input("Enter znak: "))

# print(f"{a}is more")
#if int (num1*num2):
if str(res)==">":
    if int (num1>num2 and num1>num3):
        print(f"{num1} is max")
    elif int(num2>num1 and num2>num3):
        print(f"{num2} is max")
    elif int(num3>num1 and num3>num1):
        print(f"{num3} is max")
if str(res)=="<":
    if int (num1<num2 and num1<num3):
        print(f"{num1} is min")
    elif int(num2<num1 and num2<num3):
        print(f"{num2} is min")
    elif int(num3<num1 and num3<num1):
        print(f"{num3} is min")