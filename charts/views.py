from django.contrib.auth import get_user_model
from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import View

from rest_framework.views import APIView
from rest_framework.response import Response
import json

User = get_user_model()

class HomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'charts.html', {"customers": 10})



def get_data(request, *args, **kwargs):
    data = {
        "sales": 100,
        "customers": 10,
    }
    return JsonResponse(data) # http response


class ChartData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        json_data = open('data_file.json')
        dataSet = json.load(json_data)
        json_data.close()
        qs_count = User.objects.all().count()
        labels = ["Users", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
        default_items = dataSet["temperature"]
        default_items2 = dataSet["humidity"]
        data = {
                "labels": labels,
                "default": default_items,
                "default2": default_items2,
        }
        return Response(data)

