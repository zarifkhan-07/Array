def sort(a,a_size):
    zero=0
    nonzero=0
    while nonzero!=a_size:
        if a[nonzero]!=0:
            a[nonzero], a[zero]=a[zero], a[nonzero]
            zero+=1
        nonzero+=1

    one=1
    nonone=1
    while nonone!=a_size:
        if a[nonone]!=1:
            a[nonone], a[one]=a[one], a[nonone]
            one+=1
        nonone+=1

    two=2
    nontwo=2
    while nontwo!=a_size:
        if a[nontwo]!=1:
            a[nontwo], a[two]=a[two], a[nontwo]
            two+=1
        nontwo+=1

a=[0,2,0,1,2,0,1,1,1,0,2]
a_size=len(a)
print(a)
sort(a,a_size)
print(a)