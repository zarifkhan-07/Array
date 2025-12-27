def is_power_of_4(n):
    if n <= 0:
        return False
    while n% 40:
        n=n//4
        return n==1
num=int(input("Enter a number: "))
if is_power_of_4(num):
    print("It is a power of 4")
else:
    print("It is NOT a power of 4")