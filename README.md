# API_Yatube
### Описание
    RESTful API сервис для социальной сети блогеров Yatube.
API (Application programming interface) или программный интерфейс приложения представляет собой набор правил, определяющих способ взаимодействия между приложениями или устройствами.
REST API - это API, соответствующий принципам архитектурного стиля REST (от англ. Representational State Transfer - передача состояния представления).
По этой причине REST API иногда называют RESTful API.
Список опций, доступных при работе с тем или иным API, зависит от разработчиков.
Есть три основных пункта, описывающих работу интерфейса и методы взаимодействия с ним:

- Процесс, который может выполнять программа, используя API.
- Данные, которые нужно передать интерфейсу для выполнения функции.
- Данные, которые программа получит на выходе после обработки с помощью API.

### Технологии
	Python 3.7
	pip 22.0.3
	Django 2.2.16
	djoser 2.1.0
    djangorestframework 3.12.4
    djangorestframework-simplejwt 4.7.2
	OpenAPI
	drf-yasg 1.20.0
### Запуск проекта в dev-режиме:
Клонировать репозиторий:
`git clone https://github.com/pro100cemuk/api_final_yatube.git`

Перейти в него в командной строке:
`cd api_final_yatube`

Cоздать виртуальное окружение:
`python3 -m venv env`

Активировать виртуальное окружение:
`source env/bin/activate`

Установить обновления PIP установщика пакетов:
`python3 -m pip install --upgrade pip`

Установить зависимости из файла requirements.txt:
`pip install -r requirements.txt`

Выполнить миграции:
`python3 manage.py migrate`

Запустить проект:
`python3 manage.py runserver`

#### Документация к API проекта Yatube OpenAPI стандарта по средствам ReDoc
`<link>` :    http://127.0.0.1:8000/redoc/
#### Документация к API проекта Yatube OpenAPI стандарта по средствам Swagger
`<link>` :    http://127.0.0.1:8000/swagger/