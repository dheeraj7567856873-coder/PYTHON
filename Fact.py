number=int(input("enter the number="))
fact=1
if(number<2):
    print(1)
for i in range(2,number+1,1):
    fact*=i;
print(fact)