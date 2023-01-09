def reverse(str):
    string = " "
    for i in str:
        string = i + string
    return string
str = "Prasun"
print("The original string is:",str)
print("The reverse string is:", reverse(str))