# ZiMAD Junior Data Engineer тестовое задание

## Задание 


Имеется CSV-файл, который представляет из себя выгруженные из таблицы БД данные с логом игровых событий.

Структура таблицы:
- **event_time** - время события
- **event_name** - имя события
- **user_id** - айди игрока
- **event_value** - значение события

Необходимо написать скрипт, который:
- Загружает этот файл с адреса https://testiws.ximad.com/export/events.csv.gz.
- По данным из файла считает **ARPDAU** (Average Revenue Per Daily Active User).
- На выходе скрипт должен вывести среднее значение **ARPDAU** по всем дням, которые есть в файле.
- Скрипт должен быть написан на Python 3.8+, разрешается использовать любые библиотеки (перечислить их в requirements.txt).

Также необходимо написать расчёт данного значение в виде SQL-запроса (приложить отдельный файл). То есть какой бы мы написали SQL-запрос к этой таблице, если бы мы могли обратиться непосредственно к БД (здесь неважно, какая именно БД, нужен просто SQL в общем виде).
## Average Revenue Per Daily Active User
Данный показатель просчитывается ежедневно. Берем дневной доход и делим на количество пользователей за день.
![img](https://i.imgur.com/N1Ab1dO.jpg)
## Установка и запуск
Клонировать репозиторий себе на машину
```sh
$ git clone https://github.com/tabarincev/zimad_interview_task.git
```
Установить *virtualenv*
```sh
$ pip install virtualenv
```
После установки создать виртуальное окружение командами:
- Windows
```sh
$ python -m venv venv
$ venv/Scripts/activate.bat
```
- Linux
```sh
$ python -m venv venv
$ source venv/bin/activate
```
Установить библиотеки из *requirements.txt*
```sh
$ pip install -r requirements.txt
```
Для запуска скрипта
```sh
$ python main.py
```



## Используемые библиотеки
 
 
| Библиотека | Документация |
| ------ | ------ |
| requests | https://docs.python-requests.org/en/latest/ |
| wget | https://pypi.org/project/wget/|
| gzip | https://docs.python.org/3/library/gzip.html |


