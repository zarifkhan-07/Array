def reverse(a, a_size, n):
    temp = 0
    while temp < a_size:
        start = temp
        end = min(temp + n - 1, a_size - 1)

        while start < end:
            a[start], a[end] = a[end], a[start]
            start += 1
            end -= 1

        temp += n


a = [5, 4, 2, 6, 8, 54, 89, 34, 9, 58]
n = 2
a_size = len(a)

reverse(a, a_size, n)

for i in range(a_size):
    print(a[i], end=" ")
