import random
import vk_api
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


def studyweek(send_id, message):
    vk.messages.send(
        user_id=send_id,
        message=message,
        random_id=random_id(),
        keyboard=open('studyWeekKeyboard.json', "r", encoding="UTF-8").read()
    )

