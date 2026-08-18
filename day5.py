def bonjour():
    print("bonjour !")
    print("bienvenue en python")
bonjour()

def carre(n):
    return n*n
n = int(input("enter number: "))
print(carre(n))

def max(a, b):
    if a>b:
        return a
    else:
        return b
a = int(input("enter number :"))
b = int(input("enter number :"))
print("max is:", max(a, b))

def pair(n):
    if n%2==0:
        return True 
    else:
        return False
n = int(input("enter number:"))
print(pair(n))

def sum_list(numbers):
    sum=0
    for i in range(len(numbers)):
        sum = sum + numbers[i]
    return sum
numbers=[1, 2, 3, 4, 5, 6, 7]
result = sum_list(numbers)
print(result)

def compter_pairs(tab):
    j=0
    for i in range(len(tap)):
        if tab[i]%2==0:
            j=j+1
    return j
tap=[1, 4, 6, 7, 8, 10]
print(compter_pairs(tap))