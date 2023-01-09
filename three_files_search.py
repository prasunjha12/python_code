from collections import Counter

fp=open("f1.py","r")
numbers=[]
for number in fp:
    numbers.append(number)
print(numbers)

ele=int(input("Enter the element you want to search"))

for i in range(0,100):
    if numbers[i] == ele:
        print(i)
        break

