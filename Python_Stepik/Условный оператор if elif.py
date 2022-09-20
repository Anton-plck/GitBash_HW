#1. При регистрации на сайтах требуется вводить пароль дважды. Это сделано для безопасности, поскольку такой подход уменьшает возможность неверного ввода пароля.
#Напишите программу, которая сравнивает пароль и его подтверждение. Если они совпадают, то программа выводит: «Пароль принят», иначе: «Пароль не принят».

pass1 = input()
pass2 = input()
if pass1 == pass2:
    print("Пароль принят")
else:
    print("Пароль не принят")

#2. Напишите программу, которая определяет, является число четным или нечетным.

num = int(input())
if num % 2 == 0:
    print("Четное")
else:
    print("Нечетное")

#3. Напишите программу, которая проверяет, что для заданного четырехзначного числа выполняется следующее соотношение:
# сумма первой и последней цифр равна разности второй и третьей цифр.

num = int(input())
a = (num % 10000) // 1000
b = (num % 1000) // 100
c = (num % 100) // 10
d = num % 10
if (a + d) == (b - c):
    print('ДА')
else:
    print('НЕТ')

#4. Напишите программу, которая определяет, разрешен пользователю доступ к интернет-ресурсу или нет.

age = int(input())
if age >= 18:
    print("Доступ разрешен")
else:
    print("Доступ запрещен")

#5. Напишите программу, которая определяет, являются ли три заданных числа (в указанном порядке) последовательными членами арифметической прогрессии.

a = int(input())
b = int(input())
c = int(input())
if a-b == b-c:
    print('YES')
else:
    print('NO')

#6. Напишите программу, которая определяет наименьшее из двух чисел.

num1 = int(input())
num2 = int(input())
if num1 < num2:
    print(num1)
if num1 > num2:
    print(num2)

#7. Напишите программу, которая определяет наименьшее из четырёх чисел.

num1 = int(input())
num2 = int(input())
num3 = int(input())
num4 = int(input())
if num1 < num2 and num1 < num3 and num1 <= num4:
    print(num1)
if num2 <= num1 and num2 <= num3 and num2 <= num4:
    print(num2)
if num3 < num1 and num3 < num2 and num3 < num4:
    print(num3)
if num4 <= num1 and num4 < num1 and num4 <= num3:
    print(num4)

#8. Напишите программу, которая по введённому возрасту пользователя сообщает, к какой возрастной группе он относится:

age = int(input())
if 0 <= age <= 13:
    print("детство")
if 14 <= age <= 24:
    print("молодость")
if 25 <= age <= 59:
    print("зрелость")
if age >= 60:
    print("старость")

#9. Напишите программу, которая считывает три числа и подсчитывает сумму только положительных чисел.

num1 = int(input())
num2 = int(input())
num3 = int(input())
if num1 >= 0 and num2 >= 0 and num3 >= 0:
    print(num1+num2+num3)
if num1 < 0 and num2 >= 0 and num3 >= 0:
    print(num2+num3)
if num1 < 0 and num2 < 0 and num3 >= 0:
    print(num3)
if num1 >= 0 and num2 < 0 and num3 >= 0:
    print(num1+num3)
if num1 >= 0 and num2 < 0 and num3 < 0:
    print(num1)
if num1 >= 0 and num2 >= 0 and num3 < 0:
    print(num1+num2)
if num1 < 0 and num2 >= 0 and num3 < 0:
    print(num2)
if num1 < 0 and num2 < 0 and num3 < 0:
    print(0)