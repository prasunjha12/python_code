from datetime import datetime
start_time = datetime.now()

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

end_time = datetime.now()
print('Duration: {}'.format(end_time - start_time))