""" Домашнее задание №1

Использование библиотек: ephem

* Установите модуль ephem
* Добавьте в бота команду /planet, которая будет принимать на вход
  название планеты на английском, например /planet Mars
* В функции-обработчике команды из update.message.text получите
  название планеты (подсказка: используйте .split())
* При помощи условного оператора if и ephem.constellation научите
  бота отвечать, в каком созвездии сегодня находится планета.
 """
from datetime import date
import ephem
import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import settings 
logging.basicConfig(filename='bot.log', level=logging.INFO)

def great_user(update, context):
    update.message.reply_text('Введите команду /planet и название планеты. \nПример: /planet mars')


def input_planet(update, context):
    answer_user=update.message.text[7:]
    answer_user = answer_user.upper().replace(' ', '')
   
    if answer_user == 'MARS':
        date_now=date.today()
        date_now=str(date_now).replace('-','/')
        mars = ephem.Mars(date_now)
        const = ephem.constellation(mars)
        update.message.reply_text(f'Планета {answer_user} находится в созвездии {const}')
    elif answer_user == 'MERCURY':
        date_now=date.today()
        date_now=str(date_now).replace('-','/')
        mercury = ephem.Mercury(date_now)
        const = ephem.constellation(mercury)
        update.message.reply_text(f'Планета {answer_user} находится в созвездии {const}')
    elif answer_user == 'VENUS':
        date_now=date.today()
        date_now=str(date_now).replace('-','/')
        venus = ephem.Venus(date_now)
        const = ephem.constellation(venus)
        update.message.reply_text(f'Планета {answer_user} находится в созвездии {const}')
    elif answer_user == 'JUPITER':
        date_now=date.today()
        date_now=str(date_now).replace('-','/')
        jupiter = ephem.Jupiter(date_now)
        const = ephem.constellation(jupiter)
        update.message.reply_text(f'Планета {answer_user} находится в созвездии {const}')
    elif answer_user == 'SATURN':
        date_now=date.today()
        date_now=str(date_now).replace('-','/')
        saturn = ephem.Saturn(date_now)
        const = ephem.constellation(saturn)
        update.message.reply_text(f'Планета {answer_user} находится в созвездии {const}')
    elif answer_user == 'NEPTUNE':
        date_now=date.today()
        date_now=str(date_now).replace('-','/')
        neptune = ephem.Neptune(date_now)
        const = ephem.constellation(neptune)
        update.message.reply_text(f'Планета {answer_user} находится в созвездии {const}')
    elif answer_user == 'URANIUM':
        date_now=date.today()
        date_now=str(date_now).replace('-','/')
        uranium = ephem.Uranus(date_now)
        const = ephem.constellation(uranium)
        update.message.reply_text(f'Планета {answer_user} находится в созвездии {const}')
    else:
        update.message.reply_text(f'Такой планеты не существует')



def main():
    mybot = Updater(settings.API_KEY, use_context=True)
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start', great_user)) #Объявляем реакцию на команду Start
    dp.add_handler(CommandHandler('planet', input_planet))
    mybot.start_polling() #Запуск постоянных обновлений
    mybot.idle()  #непрерывная работа


main()