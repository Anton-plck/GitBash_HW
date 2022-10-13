#1. На вход программе подаются два целых числа a и b (a≤b). Напишите программу, которая подсчитывает количество чисел
#в диапазоне от a до b включительно, куб которых оканчивается на 44 или 99.

a = int(input())
b = int(input())
counter = 0
for i in range(a, b+1):
    if i%10==4 or i%10==9:
        counter += 1
print(counter)

#2. На вход программе подается натуральное число n, а затем n целых чисел, каждое на отдельной строке.
#Напишите программу, которая подсчитывает сумму введенных чисел.

num = int(input())
total = 0
for i in range(num):
    n = int(input())
    total += n
print(total)

#3. На вход программе подается натуральное число nn. Напишите программу, которая вычисляет значение выражения
#(1+1/2 + 1/3 + ... + 1/n)-log(n).

from math import log
total = 0
n = int(input())
for i in range(1, n + 1):
    total += (1 / i)
print(total - log(n))

#4. На вход программе подается натуральное число n. Напишите программу, которая подсчитывает сумму тех чисел от 11 до n (включительно)
#квадрат которых оканчивается на 2,5 или 8.

n = int(input())
total = 0
for i in range (1, n+1):
    if i**2%10==2 or i**2%10==5 or i**2%10==8:
        total += i
print(total)

#5. На вход программе подается натуральное число n. Напишите программу, которая вычисляет n!.

n = int(input())
mult = 1
for i in range (1,n+1):
    mult = mult * i
print(mult)

#6. Напишите программу, которая считывает 10 чисел и выводит произведение отличных от нуля чисел.

total = 1
for i in range(10):
    num = int(input())
    if num > 0:
        total *= num
print(total)

#7. На вход программе подается натуральное число n. Напишите программу, которая вычисляет сумму всех его делителей.

n = int(input())
total = 0
for i in range (1, n+1):
    if n%i==0:
        total += i
print(total)

#8. На вход программе подается натуральное число nn. Напишите программу вычисления знакочередующей суммы
#1-2+3-4+5-6 + ... + ((-1)**n+1)n

n = int(input())
total = 0
for i in range(1, n + 1):
    if i % 2 == 0:
        total -= i
    if i % 2 != 0:
        total += i
print(total)

#9. На вход программе подается натуральное число nn, а затем n различных натуральных чисел, каждое на отдельной строке.
#Напишите программу, которая выводит наибольшее и второе наибольшее число последовательности.

n = int(input())
max1 = max2 = 1
for i in range(1, n+1):
    num = int(input())
    if num > max1:
        max2 = max1
        max1 = num
    elif num > max2:
        max2 = num
print(max1)
print(max2)

#10. Напишите программу, которая считывает последовательность из 10 целых чисел и определяет является ли каждое из них четным или нет.

flag = 'YES'
for i in range(10):
    n = int(input())
    if n%2!=0:
        flag = 'NO'
print(flag)

#11. Напишите программу, которая считывает натуральное число n и выводит первые nn чисел последовательности Фибоначчи.

n = int(input())
num1 = 0
num2 = 1
for i  in range(n):
    num2 = num1 + num2
    num1 = num2 - num1
    print(num1,end=' ')