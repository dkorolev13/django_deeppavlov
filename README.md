# django_deeppavlov
Django application for paraphrase detection and sentiment analysis

## Сборка бота на локальном компьютере
* Выполнить команду <code> docker run -e CONFIG=rusentiment_convers_bert -p 5000:5000 deeppavlov/deeppavlov:latest</code>  #F1 - 0.7724
* Выполнить команду <code> docker run -e CONFIG=paraphraser_rubert -p 5001:5000 deeppavlov/deeppavlov:latest</code>  # F1 - 0.8738

* Клонировать репозиторий на локальную машину <code>git clone git@github.com:dkorolev13/django_deeppavlov.git</code>
* Создать файл .env в корневом каталоге репозитория
* Установить Docker и docker compose
* Собрать и запустить контейнеры <code>docker compose up --build</code>
* На старых версиях docker compose команда выглядит так <code>docker-compose up --build</code>

## Для .env
SECRET_KEY='django-insecure-0$87!g$kqaerw76i!rk1448(=3(_j9es7c8*w#)r1wu5w7bgj7'
DEBUG=1



 
