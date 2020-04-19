from datetime import datetime


def getWeekInYear():  # Определение кол-во дней в году и получение кол-во недель.
    year = int(str(datetime.now().date())[:4])
    if year % 4 == 0 and year % 100 != 0:
        days = 366
    else:
        days = 365
    return int(days // 7)


def resultWeekStudy(countWeek=52):
    week = 2
    for i in range(1, countWeek + 1):
        if week >= 4:
            week = 0
        week += 1
        # print(f'Сейчас {i} неделя, и учебная {week}')
        if i == datetime.now().date().isocalendar()[1]:
            # print(f'Сейчас {i} неделя, и учебная {week}')
            break
    return f'Cейчас {week} учебная неделя.'


def answerWeek():
    # print('Сегодня', datetime.now().date())
    return resultWeekStudy(getWeekInYear())


answerWeek()
