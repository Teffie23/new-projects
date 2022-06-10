import asyncio
import datetime
import random
import webbrowser
import humor
from fuzzywuzzy import fuzz
import config
import get_audio
import input_audio
import weather
import greeting
import news

print(f'Я {config.name}', 'являюсь голосовым помощником ')
welcom = ['Привет,Я рада тебя видеть', 'привет', 'Я рада тебя видеть снова', 'ухты ты вернулся']
welcom += greeting.greeting_list_update
get_audio.speak(random.choice(welcom))


def respond(voice: str):
    if voice.startswith(config.aliens):
        cmd = recognize_cmd(filter_cmd(voice))
        if cmd['cmd'] not in config.cmd_list.keys():
            get_audio.speak('Что?')
        else:
            execute_cmd(cmd['cmd'])


def filter_cmd(row_voice: str):
    cmd = row_voice
    for x in config.aliens:
        cmd = cmd.replace(x, '').strip()
    for x in config.tbr:
        cmd = cmd.replace(x, '').strip()
    return cmd


def recognize_cmd(cmd):
    rc = {'cmd': '', 'percent': 0}
    for c, v in config.cmd_list.items():
        for x in v:
            vrt = fuzz.ratio(cmd, x)
            if vrt > rc['percent']:
                rc['cmd'] = c
                rc['percent'] = vrt
    return rc


def execute_cmd(cmd: str):
    if cmd == 'help':
        text = 'Я могу... '
        text += 'сказать время '
        text += 'рассказывать анекдоты '
        text += 'включать музыку '
        text += 'открывать браузер '
        get_audio.speak(text)
    elif cmd == 'ctime':
        now = datetime.datetime.now()
        text = f'Сейчас {now.hour}' + ' ' + f'{now.minute}'
        get_audio.speak(text)
    elif cmd == 'radio':
        get_audio.speak('включаю')
        path_web = 'C:/Users/игорь/AppData/Local/Yandex/YandexBrowser/Application/browser.exe %s'
        path_lofi = 'https://lofiradio.ru/'
        webbrowser.get(path_web).open(path_lofi)

    elif cmd == 'joke':
        jokes = ['Программист это машина для преобразования кофе в код',
                 'заходит улмтка в бар и говорит я из машины...']
        for i in humor.list_of_jokes:
            jokes.insert(0, i)
        # print(jokes)
        get_audio.speak(random.choice(jokes))
    elif cmd == 'browser':
        get_audio.speak('открываю')
        browser_path = 'C:/Users/игорь/AppData/Local/Yandex/YandexBrowser/Application/browser.exe %s'
        webbrowser.get(browser_path).open('https://yandex.ru/')
    elif cmd == 'weather':
        loop = asyncio.get_event_loop()
        limit_info = loop.run_until_complete(weather.getweather('да'))
        get_audio.speak(limit_info)
    elif cmd == 'performance':
        message = 'Я предствитель нового покаления человечества '
        message += 'Я создана человеком в помощь всему человечеству '
        message += 'Кстати я потребляю только электричество в от личии от вас '
        message += 'И ещё я не замужем '
        get_audio.speak(message)
    elif cmd == 'news':
        get_audio.speak('Вот что произошло за сегодня')
        for i in news.news_list:
            get_audio.speak(i)
p = input_audio.my_listen(respond)
