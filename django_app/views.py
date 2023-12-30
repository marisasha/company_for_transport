from django.shortcuts import render
import pandas as pd
import json
from django_app import models
from django_settings import utils



def home(request):
    return render(request,'home.html',context={})


def prices(request):
    # df = pd.read_excel('prices.xlsx')
    # data = df.to_dict(orient='list')
    # json_data = json.dumps(data, ensure_ascii=False)
    # data_dict = json.loads(json_data)
    # transplate_name = data_dict["Наименование"]
    # transplate_price = data_dict["Цена"]
    
    # for i in range(len(transplate_name)):
    #     models.Transports.objects.create(title=transplate_name[i],price=transplate_price[i])
    # df.iloc[:, 0] = ''
    # df.iloc[:, 1] = ''
    
    
    obj = utils.native_paginate(request, models.Transports.objects.all().order_by("id"), 45)
    return render(request,'prices.html',context={"obj":obj})