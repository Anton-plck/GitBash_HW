#1. Даны два целых числа mm и nn (m≤n). Напишите программу, которая выводит все числа от m до n включительно.

m = int(input())
n = int(input())
for i in range(m, n+1):
    print(i)

#2. Даны два целых числа m и n. Напишите программу, которая выводит все числа от m до n включительно в порядке возрастания,
#если m<n, или в порядке убывания в противном случае.

m = int(input())
n = int(input())
if m<n:
    for i in range(m, n+1):
        print(i)
elif m>n:
    for i in range(m, n-1, -1):
        print(i)
elif m==n:
    print(m)

#3. Даны два целых числа m и n (m>n). Напишите программу, которая выводит все нечетные числа от m до n включительно в порядке убывания.

m = int(input())
n = int(input())
for i in range(m, n, -2):
    if m%2 == 0:
        print(i-1)
    else:
        print(i) 