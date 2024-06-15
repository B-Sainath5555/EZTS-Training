num=int(input())
if(num%2==0):
    print("even")
else:    
  print("odd")

print("---------------------------------------------------------")
age=int(input("enter the age of the person"))
weight=int(input("enter the weight of the person"))
if age<18 and age>55 and weight<45:
    print("0")
else:
    print("1")
              

print("---------------------------------------------------------")
day=input()
if day=="sunday":
    print("its holiday")
else:
    print("its working day")
              
clsstr=int(input("enter strength of class"))
if clsstr<=120:
        print("seminar hall")
else:
    print("not seminar hall")


n=int(input())
if n>0:
    print("its positive")
elif n<0:
    print("its negative")
else:
    print("its zero")


cp=int(input("enter the cost price"))
sp=int(input("enter the selling price"))
print("profit:$",sp-cp)if sp>cp else print("loss:$",cp-sp)
cp=int(input("enter the cost price"))
sp=int(input("enter the selling price"))
print("profit:$",sp-cp)if sp>cp else print("loss:$",cp-sp)


sal=int(input())
if sal>25000 and sal<40000:
    print("manager")
elif sal>15000 and sal<=25000:
    print("accountant")
else:
    print("clerk")

