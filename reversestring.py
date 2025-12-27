def rev(s):
    if len(s)==1:
        return s[0]
    f=s[0]
    return rev(s[1:])+f
s=int(input("Enter the string:"))
print(rev(s))