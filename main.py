metrs=int(input("Enter meters: "))
mili = metrs / 1609
duim = metrs * 39.37
yadr = metrs * 1.094
res=str(input("Enter mil,duim or yadr: "))

# print(f"{a}is more")
if str(res)=="mil":
    print(f'{metrs}   is {mili}mil')
if str(res)=="duim":
    print(f'{metrs} is {duim}duim')
if str(res)=="yadr":
    print(f'{metrs} is {yadr}yard')














