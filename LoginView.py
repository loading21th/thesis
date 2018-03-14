# coding:utf-8
from django.shortcuts import render
from django.views.generic import View

from django.http import HttpResponse
from django.http import FileResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
# Create your views here.
from golearnApp.gomodels import BaseTable
import os 
import json



class LoginView(View):
    def get(self,request):
        return render(request,'login.html');

    @csrf_exempt
    def post(self,request):
        name = request.POST.get('name')
        users =  BaseTable.Ustudentinfo.objects.filter(name=name)
        if users:
            user = user[0]
        else:
            user = BaseTable.UTeacherinfo.objects.filter(name=name)
        hlsdic = {'status':'fail'}
        if ( (request.POST.get('passwd')) == user.upasswd ):
            request.session['name']=name
            hlsdic['status'] = 'success'
        response = JsonResponse(hlsdic, safe=False)
        response["Access-Control-Allow-Origin"] = "*"
        response["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
        response["Access-Control-Max-Age"] = "1000"
        response["Access-Control-Allow-Headers"] = "*"
        return response
