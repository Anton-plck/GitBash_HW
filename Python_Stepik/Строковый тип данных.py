# 1. Напишите программу, которая выводит текст: "Python is a great language!", said Fred. "I don't ever remember having this much fun before."

print('''"Python is a great language!", said Fred. "I don't ever remember having this much fun before."''')

#2. Напишите программу, которая считывает с клавиатуры две строки – имя и фамилию пользователя и выводит фразу:
#«Hello [введенное имя] [введенная фамилия]! You just delved into Python».

f_name = input()
l_name = input()
print ("Hello", f_name, l_name+"!", "You just delved into Python")

#3. Напишите программу, которая считывает с клавиатуры название футбольной команды и выводит фразу:
#«Футбольная команда [введённая строка] имеет длину [длина введённой строки] символов».

fc = input()
print("Футбольная команда", fc, "имеет длину", len(fc), "символов")

#4. Даны названия трех городов. Напишите программу, которая определяет самое короткое и самое длинное название города.

a = input()
b = input()
c = input()
if min (len(a), len(b), len(c)) == len(a):
    print(a)
elif min (len(a), len(b), len(c)) == len(b):
    print(b)
else:
    print(c)
if max (len(a), len(b), len(c)) == len(a):
    print(a)
elif max (len(a), len(b), len(c)) == len(b):
    print(b)
else:
    print(c)

#5. Вводятся 3 строки в случайном порядке. Напишите программу, которая выясняет можно ли из длин этих строк построить возрастающую арифметическую прогрессию.

a = len(input())
b = len(input())
c = len(input())
if b - a == c - b or c - a == b - c or b - c == a - b or a - c == b - a or a - b == c - a or c - b == a - c:
    print('YES')
else:
    print('NO')

#6. Напишите программу, которая считывает одну строку, после чего выводит «YES», если в введенной строке есть подстрока «синий» и «NO» в противном случае.

a = input()
if "синий" in a:
    print("YES")
else:
    print("NO")

#7. Напишите программу, которая считывает одну строку, после чего выводит «YES», если в введённой строке есть подстрока «суббота» или «воскресенье», и «NO» в противном случае.

a = input()
if ("суббота" in a) or ("воскресенье" in a):
    print("YES")
else:
    print("NO")

#8. Будем считать email адрес корректным, если в нем есть символ собачки (@) и точки. Напишите программу проверяющую корректность email адреса.

email = input()
if "@" in email and "." in email:
    print("YES")
else:
    print("NO")