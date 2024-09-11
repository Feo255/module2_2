first=input("введите целое число: ")
second=input("введите целое число: ")
third=input("введите целое число: ")
print(first,second,third)
if first == second and first == third:
    print(3)
elif first == second or first == third or second == third:
    print(2)
else:
    print(0)