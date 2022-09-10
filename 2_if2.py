"""

Домашнее задание №1

Условный оператор: Сравнение строк

* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками. 
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные праметры 
  и выводя на экран результаты

"""

def main(stroka1, stroka2):
     if isinstance(stroka1,str) and isinstance(stroka2,str):
         pass
     else:
         print(0)  
     
     if stroka1 == stroka2:
         return 1
     elif stroka1 != stroka2 and len(stroka1) > len(stroka2):
         if stroka1 != stroka2 and stroka2 =="learn":
           return 3
         else:
           return 2

    




a=main('stroka', 'stroka')
print(a)
a=main('stroka dlinee', 'stroka')
print(a)
a=main('stroka', 'learn')
print(a)

