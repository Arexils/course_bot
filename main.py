import random
import vk_api
import datetime
from week import answerWeek
from schedule import schedule
from vk_api.longpoll import VkLongPoll, VkEventType

with open('key.txt', 'r') as file_api:
    file_api = file_api.readline()

vk_session = vk_api.VkApi(token=file_api)
longpoll = VkLongPoll(vk_session)
vk = vk_session.get_api()
global random


def random_id():
    Random = 0
    Random = random.randint(1, 100000000)
    return Random


def send_msg(send_id, message=None, attachment=None):
    vk.messages.send(
        user_id=send_id,
        message=message,
        attachment=attachment,
        random_id=random_id(),
    )


hello = ['привет', 'приветствую вас', 'приветик', 'здравствуйте', 'приветствую', 'добрый день', 'доброе утро',
         'добрый вечер', 'здорово', 'хай', 'хей', 'хэллоу', 'хэлло', 'хэллоу', 'хаюшки', 'приветствую',
         'приветствую тебя', 'мое почтение', ' здрасти', 'hi', 'hey', 'yo', 'q', 'qq', 'ку', 'куку', 'ку-ку', 'hello',
         'здрасте']

while True:
    print('BOT запущен:')
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.to_me:
            if event.text.lower() in hello:
                vk.messages.send(user_id=event.user_id,
                                 message='Привет, как дела? Чем могу помочь?',
                                 random_id=random_id(),
                                 keyboard=open('mainKeyboard.json', "r", encoding="UTF-8").read()
                                 )
            elif event.text == 'На главную':
                vk.messages.send(user_id=event.user_id,
                                 message='Вы вернулись в главное меню.',
                                 random_id=random_id(),
                                 keyboard=open('mainKeyboard.json', "r", encoding="UTF-8").read()
                                 )
            # перевести клавиатуру в другой режим
            elif event.text == 'Расписание':
                vk.messages.send(user_id=event.user_id,
                                 message='Выберите какой день хотите посмотреть или всю неделю.',
                                 random_id=random_id(),
                                 keyboard=open('studyWeekKeyboard.json', "r", encoding="UTF-8").read()
                                 )
            # расписание на конкретный день
            elif event.text in ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота',
                                'Расписание на всю неделю', 'Расписание звонков']:
                send_msg(event.user_id,
                         schedule(event.text))
            elif event.text == 'Какая неделя?':
                send_msg(event.user_id,
                         answerWeek())
            elif event.text == 'Оформить диплом, курсовой':
                send_msg(event.user_id,
                         'http://bsac.by/students#%D0%9A%D0%B0%D0%BA%D0%BE%D1%84%D0%BE%D1%80%D0%BC%D0%B8%D1%82%D1%8C%D0%B4%D0%B8%D0%BF%D0%BB%D0%BE%D0%BC,%D0%BA%D1%83%D1%80%D1%81%D0%BE%D0%B2%D0%BE%D0%B9,%D0%B4%D1%80%D1%83%D0%B3%D0%B8%D0%B5%D0%B4%D0%BE%D0%BA%D1%83%D0%BC%D0%B5%D0%BD%D1%82%D1%8B')
            else:
                send_msg(event.user_id,
                         'Я в режиме разработки, еще немного нужно подождать)')
            try:
                print(f'Сообщение: [{event.text}] от: ' + str(
                    vk.users.get(user_ids=event.user_id,
                                 fields='online, last_seen')))
            except:
                pass
