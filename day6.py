numbers=(10, 20, 30, 40, 50)
print(numbers[0])
print(numbers[-1])
for number in numbers:
    print(number)

numbers=(12, 5, 20, 8, 15)
max=numbers[0]
for i in range(5):
    if max<numbers[i]:
        max=numbers[i]
print("max :",max)

student = {
    "name":"houda",
    "age":18,
    "grade":15
}
for key, value in student.items():
    print(key ,":", value)
student["age"]=19
student["grade"]=16
student["city"]="setif"
for key, value in student.items():
    print(key,":",value)

student = {
    "name":"sara",
    "math": 15,
    "python": 18,
    "english": 14
}
sum=0
for key, value in student.items():
    if key!="name":
        sum=sum+value
average=sum/3
print("average: ",average)