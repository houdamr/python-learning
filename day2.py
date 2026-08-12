name = input("what is your name? ")
age = int(input("how old are you? " ))
print("hey",name,"! you are",age,"years old")

a =10
b =3
print(a//b)
print(a ** b)

number =  int(input("enter a number : "))
if number>0:
    print(number,"positif")
elif number<0:
    print(number,"negatif")
else:
    print("zero")

note = float(input("enter your note: "))
if note>=16:
    print("excellent")
elif note>=12:
    print("good")
elif note >=10:
    print("passed")
else :
    print("fail")

nb = float(input("enter a number :" ))
if nb%2==0:
    print("even")
else:
    print("odd")
    