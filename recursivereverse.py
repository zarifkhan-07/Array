def reverse(num):
    if(num>0):
        last=num%10
        if(num//10>0):
            c_number=reverse((num//10))
            return last*pow(10,len(str(c_number)))+c_number
        return num
    
n=int(input("Enter the number:"))
print("Reversed:",reverse(n))