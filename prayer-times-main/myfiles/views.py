from django.shortcuts import render
import requests
from django.http import HttpResponse
from myfiles.models import Citys,Viloyatlar
# Create your views here.


def home(request_api):
    city = f"Toshkent"
    url = f"https://islomapi.uz/api/present/day?region={city}"
    r = requests.get(url).json()['times']
    Bomdod = r['tong_saharlik']
    quyosh =r['quyosh']
    peshin = r['peshin']
    asr = r['asr']
    shom = r['shom_iftor']
    hufton = r['hufton']
    return render(request_api,"home.html",{'bomdod':Bomdod,"quyosh":quyosh,"peshin":peshin,"asr":asr,"shom":shom,"hufton":hufton})

def web2(request):
    results = request.GET['Citys']
    city = f"{results}"
    url = f"https://islomapi.uz/api/present/day?region={city}"
    r = requests.get(url).json()['times']
    Bomdod = r['tong_saharlik']
    quyosh =r['quyosh']
    peshin = r['peshin']
    asr = r['asr']
    shom = r['shom_iftor']
    hufton = r['hufton']
    return render(request,"Prayers_time.html",{'bomdod':Bomdod,"quyosh":quyosh,"peshin":peshin,"asr":asr,"shom":shom,"hufton":hufton,"sity":results})
