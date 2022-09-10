"""

Домашнее задание №1

Исключения: KeyboardInterrupt

* Перепишите функцию hello_user() из задания while1, чтобы она 
  перехватывала KeyboardInterrupt, писала пользователю "Пока!" 
  и завершала работу при помощи оператора break
    
"""

def hello_user():
    try:
        while True:
            user_answer = input("Как дела? ")
        
            if user_answer == 'хорошо':
                break
            else:
                pass
    except KeyboardInterrupt:
        print('\nПока')
        

    
hello_user()
