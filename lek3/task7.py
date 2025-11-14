import math
#1
# a = int(input("Введіть число а:"))
# if a>0 and a<100:
#     print("Число а є додатним та меншим за 100")
# else:
#     print("Число а не є додатним або не є меншим за 100")
#2
# a = int(input("Введіть число а:"))
# if (-33<=a and 150>a)or(a==151):
#     print("Число а належить проміжку (-33;150) або дорівнює 151")
# else:
#     print("Число а не належить проміжку (-33;150) та не дорівнює 151")
#3
# a = int(input("Введіть число а:"))
# if (a>-100 and a<0) or (a>0 and a<100):
#     print("Число а належить проміжку (-100;0) або (0;100)")
# else:
#     print("Число а не належить проміжку (-100;0) та (0;100)")
#4
# a = float(input("Введіть перше число: "))
# b = float(input("Введіть друге число: "))
# c = float(input("Введіть третє число: "))

# low = 0.0
# mid = 0.0
# high = 0.0

# if a < b and a < c:
#     low = a
# elif b < a and b < c:
#     low = b
# else:
#     low = c

# if a > b and a > c:
#     high = a
# elif b > a and b > c:
#     high = b
# else:
#     high = c

# mid = (a + b + c) - low - high

# print(f"{low} < {mid} < {high}")
#5
# a = float(input("Введіть першу сторону (a): "))
# b = float(input("Введіть другу сторону (b): "))
# c = float(input("Введіть третю сторону (c): "))


    
# if (a + b > c) and (a + c > b) and (b + c > a):
#     print("Даний трикутник існує")
# else:
#     print("Трикутника із такими сторонами не існує")
#6
# a = int(input("Введіть число а:"))
# b = int(input("Введіть число b:"))

# x = (a / b) + 3
# print(x)
#7
# a = float(input())
# b = float(input())
# c = float(input())

# x1 = (c + math.sqrt(25*c**2 + 4*c*(a + b))) / (2*c)
# x2 = (c - math.sqrt(25*c**2 + 4*c*(a + b))) / (2*c)

# print(x1)
# print(x2)