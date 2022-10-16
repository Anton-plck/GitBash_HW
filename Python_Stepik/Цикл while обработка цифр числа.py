#1. Дано натуральное число. Напишите программу, которая выводит его цифры в столбик в обратном порядке.

num = int(input())
while num!=0:
    a = num%10
    print(a)
    num = num//10

#2. Дано натуральное число. Напишите программу, которая меняет порядок цифр числа на обратный.

num = int(input())
while num!=0:
    a = num%10
    print(a, end="")
    num = num//10

#3. Дано натуральное число n, (n≥10). Напишите программу, которая определяет его максимальную и минимальную цифры.

num = int(input())
max1 = 0
min1 = 9

while num != 0:
    if num % 10 > max1:
        max1 = num % 10
    if num % 10 < min1:
        min1 = num % 10
    num = num // 10

print('Максимальная цифра равна', max1)
print('Минимальная цифра равна', min1)

#4. Дано натуральное число. Напишите программу, которая вычисляет:
#сумму его цифр;
#количество цифр в нем;
#произведение его цифр;
#среднее арифметическое его цифр;
#его первую цифру;
#сумму его первой и последней цифры.

num = int(input())
summ = 0
mult = 1
kolvo = 0
last = num % 10
while num != 0:
    a = num % 10
    summ += a
    kolvo += 1
    mult *= a
    aver = summ / kolvo
    first = num % 10
    num = num // 10

print(summ, kolvo, mult, aver, first, last + first, sep="\n")

#5. Дано натуральное число n (n > 9). Напишите программу, которая определяет его вторую (с начала) цифру.

num = int(input())
n = 0
while num>9:
    n = num%10
    num = num //10
print(n)

#6. Дано натуральное число. Напишите программу, которая определяет, состоит ли указанное число из одинаковых цифр.

num = int(input())
d = num % 10
nat_num = True
while num != 0:
    a = num % 10
    num = num // 10
    if a != d:
        nat_num = False
if nat_num == True:
    print("YES")
else:
    print("NO")

#7. Дано натуральное число. Напишите программу, которая определяет, является ли последовательность его цифр при просмотре справа налево упорядоченной по неубыванию.

num = int(input())
d = num % 10
print(d)
flag = True
while num != 0:
    a = num % 10
    print(a)
    if a < d:
        flag = False
    d, a = a, d
    num = num // 10

if flag == True:
    print("YES")
else:
    print("NO")