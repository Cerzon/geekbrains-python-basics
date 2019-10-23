
""" 
== OpenWeatherMap ==

OpenWeatherMap — онлайн-сервис, который предоставляет бесплатный API
 для доступа к данным о текущей погоде, прогнозам, для web-сервисов
 и мобильных приложений. Архивные данные доступны только на коммерческой основе.
 В качестве источника данных используются официальные метеорологические службы
 данные из метеостанций аэропортов, и данные с частных метеостанций.

Необходимо решить следующие задачи:

== Получение APPID ==
    Чтобы получать данные о погоде необходимо получить бесплатный APPID.
    
    Предлагается 2 варианта (по желанию):
    - получить APPID вручную
    - автоматизировать процесс получения APPID, 
    используя дополнительную библиотеку GRAB (pip install grab)

        Необходимо зарегистрироваться на сайте openweathermap.org:
        https://home.openweathermap.org/users/sign_up

        Войти на сайт по ссылке:
        https://home.openweathermap.org/users/sign_in

        Свой ключ "вытащить" со страницы отсюда:
        https://home.openweathermap.org/api_keys
        
        Ключ имеет смысл сохранить в локальный файл, например, "app.id"

        
== Получение списка городов ==
    Список городов может быть получен по ссылке:
    http://bulk.openweathermap.org/sample/city.list.json.gz
    
    Далее снова есть несколько вариантов (по желанию):
    - скачать и распаковать список вручную
    - автоматизировать скачивание (ulrlib) и распаковку списка 
     (воспользоваться модулем gzip 
      или распаковать внешним архиватором, воспользовавшись модулем subprocess)
    
    Список достаточно большой. Представляет собой JSON-строки:
{"_id":707860,"name":"Hurzuf","country":"UA","coord":{"lon":34.283333,"lat":44.549999}}
{"_id":519188,"name":"Novinki","country":"RU","coord":{"lon":37.666668,"lat":55.683334}}
    
    
== Получение погоды ==
    На основе списка городов можно делать запрос к сервису по id города. И тут как раз понадобится APPID.
        By city ID
        Examples of API calls:
        http://api.openweathermap.org/data/2.5/weather?id=2172797&appid=b1b15e88fa797225412429c1c50c122a

    Для получения температуры по Цельсию:
    http://api.openweathermap.org/data/2.5/weather?id=520068&units=metric&appid=b1b15e88fa797225412429c1c50c122a

    Для запроса по нескольким городам сразу:
    http://api.openweathermap.org/data/2.5/group?id=524901,703448,2643743&units=metric&appid=b1b15e88fa797225412429c1c50c122a


    Данные о погоде выдаются в JSON-формате
    {"coord":{"lon":38.44,"lat":55.87},
    "weather":[{"id":803,"main":"Clouds","description":"broken clouds","icon":"04n"}],
    "base":"cmc stations","main":{"temp":280.03,"pressure":1006,"humidity":83,
    "temp_min":273.15,"temp_max":284.55},"wind":{"speed":3.08,"deg":265,"gust":7.2},
    "rain":{"3h":0.015},"clouds":{"all":76},"dt":1465156452,
    "sys":{"type":3,"id":57233,"message":0.0024,"country":"RU","sunrise":1465087473,
    "sunset":1465149961},"id":520068,"name":"Noginsk","cod":200}    


== Сохранение данных в локальную БД ==    
Программа должна позволять:
1. Создавать файл базы данных SQLite со следующей структурой данных
   (если файла базы данных не существует):

    Погода
        id_города           INTEGER PRIMARY KEY
        Город               VARCHAR(255)
        Дата                DATE
        Температура         INTEGER
        id_погоды           INTEGER                 # weather.id из JSON-данных

2. Выводить список стран из файла и предлагать пользователю выбрать страну 
(ввиду того, что список городов и стран весьма велик
 имеет смысл запрашивать у пользователя имя города или страны
 и искать данные в списке доступных городов/стран (регуляркой))

3. Скачивать JSON (XML) файлы погоды в городах выбранной страны
4. Парсить последовательно каждый из файлов и добавлять данные о погоде в базу
   данных. Если данные для данного города и данного дня есть в базе - обновить
   температуру в существующей записи.


При повторном запуске скрипта:
- используется уже скачанный файл с городами;
- используется созданная база данных, новые данные добавляются и обновляются.


При работе с XML-файлами:

Доступ к данным в XML-файлах происходит через пространство имен:
<forecast ... xmlns="http://weather.yandex.ru/forecast ...>

Чтобы работать с пространствами имен удобно пользоваться такими функциями:

    # Получим пространство имен из первого тега:
    def gen_ns(tag):
        if tag.startswith('{'):
            ns, tag = tag.split('}')
            return ns[1:]
        else:
            return ''

    tree = ET.parse(f)
    root = tree.getroot()

    # Определим словарь с namespace
    namespaces = {'ns': gen_ns(root.tag)}

    # Ищем по дереву тегов
    for day in root.iterfind('ns:day', namespaces=namespaces):
        ...

"""

from urllib import request
from urllib.error import HTTPError
import os
import gzip
import json
import datetime
import sqlite3


SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
SERVER_API = 'http://api.openweathermap.org/data/2.5/'


class WeatherPoint:
    def __init__(self, point_dict):
        for key, value in point_dict.items():
            setattr(self, key, value)

    def __str__(self):
        return self.name

    def __len__(self):
        return len(self.name)

    def __lt__(self, other):
        return self.name < other.name

    def __le__(self, other):
        return self.name <= other.name

    def __gt__(self, other):
        return self.name > other.name

    def __ge__(self, other):
        return self.name >= other.name

    def __eq__(self, other):
        return self.name == other.name

    def __ne__(self, other):
        return self.name != other.name


class WeatherRequest:
    def __init__(self, point_list=None):
        self._choosen_wp = point_list

    def add_wpoint(self, wpoint):
        if self._choosen_wp is None:
            self._choosen_wp = []
        if not wpoint in self._choosen_wp:
            self._choosen_wp.append(wpoint)

    def print_choosen_wp(self):
        if self._choosen_wp is None:
            print('-- empty --')
        else:
            for wpoint in self._choosen_wp:
                print(wpoint, wpoint.coord)


class UserChoiceDialog:
    """
    Диалог выбора и добавления точек для запроса погоды.
    wr - экземпляр WeaterRequest, в который будут добавлятся точки.
    """
    def __init__(self, wr):
        city_list = os.path.join(SCRIPT_DIR, 'city_list.gz')
        if not os.path.isfile(city_list):
            response = request.urlopen('http://bulk.openweathermap.org/sample/city.list.json.gz')
            if response.status == 200:
                with open(city_list, 'wb') as arc_file:
                    arc_file.write(response.read())
            else:
                raise HTTPError(response.url, response.status, response.msg, response.getheaders(),)
        with gzip.open(city_list, 'rt', encoding='utf-8') as arc_file:
            point_list = json.load(arc_file)
        self._wplist = dict()
        for point in point_list:
            country = point.get('country') or 'N/A'
            if not country in self._wplist:
                self._wplist[country] = []
            self._wplist[country].append(WeatherPoint(point))
        self._wr = wr

    def start(self):
        country_tpl = ('{:<8}' * 10 + '\n') * (len(self._wplist) // 10) + '{:<8}' * (len(self._wplist) % 10)
        while True:
            print('=' * 80)
            print('Обозначения стран')
            print('-' * 80)
            print(country_tpl.format(*sorted(self._wplist.keys())))
            print('~' * 80)
            answer = input('Введите обозначение страны: ').upper()
            if answer in self._wplist:
                ckey = answer
                self._wplist[ckey].sort()
                name_wd = max(map(len, self._wplist[ckey])) + 2
                enum_wd = len(str(len(self._wplist[ckey])))
                columns = 80 // (enum_wd + name_wd + 2)
                while True:
                    print('=' * 80)
                    print('Список пунктов')
                    print('-' * 80)
                    endchar = ''
                    for idx, point in enumerate(self._wplist[ckey], 1):
                        if idx % columns == 0:
                            endchar = '\n'
                        else:
                            endchar = ''
                        print('{:>{ew}}. {:<{nw}}'.format(idx, point.name, ew=enum_wd, nw=name_wd), end=endchar)
                    if endchar == '':
                        print('\n')
                    print('~' * 80)
                    answer = input('Введите через запятую номера добавляемых в запрос пунктов: ')
                    if answer:
                        answer = tuple(filter(lambda x: x.strip().isnumeric(), answer.split(',')))
                        answer = tuple(x - 1 for x in map(int, (x.strip() for x in answer)))
                        for idx in answer:
                            if idx < len(self._wplist[ckey]):
                                self._wr.add_wpoint(self._wplist[ckey][idx])
                    answer = input('Завершить выбор пунктов в {}? [y/n] '.format(ckey)).lower()
                    if answer == 'y':
                        break
            answer = input('Завершить выбор? [y/n] ').lower()
            if answer == 'y':
                break


wreq = WeatherRequest()
dialog = UserChoiceDialog(wreq)
dialog.start()
wreq.print_choosen_wp()