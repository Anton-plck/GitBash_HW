#1. На плоскости евклидово расстояние между двумя точками (x1;y1) и (x2;y2) определяется так p = sqrt(x1-x2)^2 + (y1-y2)^2
#Напишите программу определяющую евклидово расстояние между двумя точками, координаты которых заданы.

x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

from math import *

p = sqrt((x1-x2)**2+(y1-y2)**2)
print(p)

#2. Напишите программу определяющую площадь круга и длину окружности по заданному радиусу R.

from math import *
r = float(input())
s = pi*r**2
print(s)
c = (2*pi)*r
print(c)

#3. вывести 4 числа – среднее арифметическое, геометрическое, гармоническое и квадратичное.

from math import *
a = float(input())
b = float(input())
ar = (a+b)/2
print(ar)
geom = sqrt(a*b)
print(geom)
gar = (2*a*b)/(a+b)
print(gar)
kvad = sqrt(a**2+b**2)/sqrt(2)
print(kvad)

#4. апишите программу, вычисляющую значение тригонометрического выражения sin(x) + cos(x) + tan^2(x).

from math import *
x = float(input())
x = radians(x)
total = sin(x)+cos(x)+tan(x)**2
print(total)

#5. Напишите программу, вычисляющую значение ceil(x) + floor(x) по заданному вещественному числу x.

from math import *
x = float(input())
total = floor(x)+ceil(x)
print(total)

#6. Даны три вещественных числа a,b,c. Напишите программу, которая находит вещественные корни квадратного уравнения
#ax^2 + bx + c = 0.

from math import *
a = float(input())
b = float(input())
c = float(input())
d = b**2-4*a*c
if d>0:
    x1 = ((-b)-sqrt(d))/(2*a)
    x2 = ((-b)+sqrt(d))/(2*a)
    print(min(x1, x2))
    print(max(x1, x2))
elif d==0:
    print(-b/(2*a))
else:
    print("Нет корней")

#7. Правильный многоугольник — выпуклый многоугольник, у которого равны все стороны и все углы между смежными сторонами.
#Площадь правильного многоугольника с длиной стороны aa и количеством сторон nn вычисляется по формуле:
#S = n*a**2 / 4tg(π/n)

from math import *
n = int(input())
a = float(input())
s = (n*(a**2))/(4*(tan(pi/n)))
print(s)