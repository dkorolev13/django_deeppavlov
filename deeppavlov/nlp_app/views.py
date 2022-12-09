from django.shortcuts import render
import requests


def index(request):
    data = {"paraphrase_data": "Здесь будет указано одинаковые/разные значения у текстов",
            "sentiment": "Здесь будет указана тональность текстов"}

    URL_PARAPHRASE_API = "http://10.0.0.147:5001" # заменить на свой IP adress
    ENDPOINT = '/model'

    if request.method == 'POST' and 'paraphrase_btn' in request.POST:
        body = {
            "text_a": [
                request.POST.get('json_data_for_text_a', '')
            ],
            "text_b": [
                request.POST.get('json_data_for_text_b', '')
            ]
        }
        responce = requests.post(URL_PARAPHRASE_API + ENDPOINT, json=body)

        if responce.text[1] == '1':
            data = {"paraphrase_data": "Данные два текста имеют одинаковое значение"}
        elif responce.text[1] == '0':
            data = {"paraphrase_data": "Данные два текста разные по своим значениям"}

        return render(request, 'nlp_app/index.html', data)

    URL_SENTIMENT_API = "http://10.0.0.147:5000" # заменить на свой IP adress
    if request.method == 'POST' and 'sentiment_btn' in request.POST:
        body = {
            "x": [
                request.POST.get('json_data_for_sentiment', '')
            ]
        }
        responce = requests.post(URL_SENTIMENT_API + ENDPOINT, json=body)

        if responce.text == '["negative"]':
            data = {"sentiment": "Негативная тональность текста"}
        elif responce.text == '["positive"]':
            data = {"sentiment": "Положительная тональность текста"}
        else:
            data = {"sentiment": "Нейтральная тональность текста"}

        return render(request, 'nlp_app/index.html', data)

    return render(request, 'nlp_app/index.html', data)
