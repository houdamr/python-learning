name=input("enter your name: ")
print("hello",name)

word=input("enter a word: ")
print("first:",word[0])
print("last:",word[-1])
print("length:",len(word))

phrase=input("enter a sentence:")
i=0
for letter in phrase:
    if letter=='a':
     i=i+1
print("a appears:",i,"times")

word=input("enter a word: ")
for i in range(len(word)):
   print(i ,word[i])

p=input("enter a sentence: ")
i=0
for letter in p:
   if letter in "aeiuo":
    i=i+1
print("number of vowels: ",i)

word=input("enter a word: ")
inv=""
for letter in word:
  inv=letter+inv
print("inverse:",inv)

word=input("enter a word:")
inverse=word[::-1]
if word==word[::-1]:
  print("palindrome")
else:
  print("not palindrome")

