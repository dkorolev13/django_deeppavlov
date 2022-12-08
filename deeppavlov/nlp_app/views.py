from django.shortcuts import render
from requests import post


def index(request):
    data = {"data1": "", "data2": ""}

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
        data = {"data1": responce.text}

        return render(request, 'nlp_app/index.html', data)

    if request.method == 'POST' and 'btn2' in request.POST:
        link = "http://127.0.0.1:5000/model"
        body = {
            "x": [
                request.POST.get('json_data3', '')
            ]
        }
        responce = post(link, json=body)
        data = {"data2": responce.text}

        return render(request, 'nlp_app/index.html', data)
