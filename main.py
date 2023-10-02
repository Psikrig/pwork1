import math
p = 1
while (p == 1):
    try:
    print(
        "выберите действие: " 
"\r\n1. Сложить 2 числа",
"\r\n2. Вычесть первое из второго",
"\r\n3. Перемножить два числа",
"\r\n4. Разделить первое на второе",
"\r\n5. Возвести в степень N первое число",
"\r\n6. Найти квадратный корень из числа",
"\r\n7. Найти факториал из числа",
"\r\n8. Найти синус числа",
"\r\n9. Найти косинус числа",
"\r\n10. Найти тангенс числа",
"\r\n11. Выйти из программы")
    x = int(input())
    if x == 1:
        print("введите первое слогаемое.")
        a = int(input())
        print("введите второе слогаемое.")
        s = int(input())
        d = a + s
        print("Ответ:", d)
    elif x == 2:
          print("введите уменьшаемое.")
          a = int(input())
          print("введите вычитаемое.")
          s = int(input())
          d = a - s
          print("Ответ:", d)
    elif x == 3:
          print("введите первый множитель.")
          a = int(input())
          print("введите второй множитель.")
          s = int(input())
          d = a * s
          print("Ответ:", d)
    elif x == 4:
          print("введите делимое.")
          a = int(input())
          print("введите делитель.")
          s = int(input())
          if s == 0:
                print("error")
          d = a / s
          print("Ответ:", d)
    elif x == 5:
          print("введите число.")
          a = int(input())
          print("введите степень.")
          s = int(input())
          d = a ** s
          print("Ответ:", d)
    elif x == 6:
          print("введите число.")
          a = int(input())
          if a < 0:
                print("error")
          d = math.sqrt(a)
          print("Ответ:", d)
    elif x == 7:
          print("введите число.")
          a = int(input())
        if a < 0: print("error") break
          d = math.factorial(a)
          print("Ответ:", d)
    elif x == 8:
          print("введите число.")
          a = int(input())
          d = math.sin(a)
          print("Ответ:", d)
    elif x == 9:
          print("введите число.")
          a = int(input())
          d = math.cos(a)
          print("Ответ:", d)
    elif x == 10:
          print("введите число.")
          a = int(input())
          d = math.tan(a)
          print("Ответ:", d)
    elif x == 11:
         break
    else:
          print("error")
except: print("error")
