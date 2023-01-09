from mimetypes import init
from time import time
init=time()

def search(lst , n , ele):
    for i in range(0,n):
        if lst[i] == ele:
            b = i
            break
        else:
            b = -1
    return b
n = int(input())
lst = []
for i in range(0,n):
        ins = int(input())
        lst.append(ins)
ele = int(input("Enter the element you want to search for:"))
print("It is at Index",search(lst , n ,ele))

print("Total time taken: ",time()-init)



