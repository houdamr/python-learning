numbers = [5, 10, 15, 20, 25]
for number in numbers:
    print(number)

sum=0
for i in range(0,5):
    sum = sum+ numbers[i]
print("sum is:",sum)

nombres = [3, 8, 12, 7, 15, 20, 9]
for i in range(0,7):
    if nombres[i]%2==0:
        print(nombres[i])

numbers =[12, 5, 27, 8, 19]
max=numbers[0]
for i in range(0,5):
    if numbers[i]>max:
        max=numbers[i]
print("max is:",max)

for i in range(0,5):
    numbers[i]=int(input("enter number: "))
print("list: ",numbers)

sum =0
for i in range(0,5):
    sum=sum +numbers[i]
print("sum: ",sum)

max=numbers[0]
for i in range(1,5):
    if max<numbers[i]:
        max=numbers[i]
print("max: ",max)

min=numbers[0]
for i in range(1,5):
    if min>numbers[i]:
        min=numbers[i]
print("min: ",min)

j=0
for i in range(0,5):
    if numbers[i]%2==0:
        j=j+1
print("even numbers: ",j)





    
