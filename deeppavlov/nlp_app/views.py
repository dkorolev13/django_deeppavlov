from django.shortcuts import render
from requests import post


def index(request):
    data = {"data1": "Здесь будет указано одинаковые/разные значения у текстов",
            "data2": "Здесь будет указана тональность текстов"}

    if request.method == 'POST' and 'btn1' in request.POST:
        link = "http://127.0.0.1:5001/model"
        body = {
            "text_a": [
                request.POST.get('json_data', '')
            ],
            "text_b": [
                request.POST.get('json_data2', '')
            ]
        }
        responce = post(link, json=body)

        if responce.text[1] == '1':
            data = {"data1": "Данные два текста имеют одинаковое значение"}
        elif responce.text[1] == '0':
            data = {"data1": "Данные два текста разные по своим значениям"}

        return render(request, 'nlp_app/index.html', data)

    if request.method == 'POST' and 'btn2' in request.POST:
        link = "http://172.17.0.2:5000"
        ENDPOINT = "model/"
        body = {
            "x": [
                request.POST.get('json_data3', '')
            ]
        }
        responce = post(link+"/"+ENDPOINT, json=body)
        print(responce.text[1])
        if responce.text == '["negative"]':
            data = {"data2": "Негативная тональность текста"}
        elif responce.text == '["positive"]':
            data = {"data2": "Положительная тональность текста"}
        else:
            data = {"data2": "Нейтральная тональность текста"}

        return render(request, 'nlp_app/index.html', data)

    return render(request, 'nlp_app/index.html', data)
