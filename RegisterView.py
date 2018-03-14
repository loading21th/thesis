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


class RegisterView(View):
    def get(self,request):
        return render(request,'register.html');
    
    @csrf_exempt
    def post(self,request):
        if request.FILES:
            file_obj = request.FILES.getlist('filename')[0]
            uname = request.POST.get('name')
            passwd = request.POST.get('passwd')
            email = request.POST.get('email')
            birth = request.POST.get('birth')
            sex = request.POST.get('sex')
            student = BaseTable.Ustudentinfo(name=uname,upasswd=passwd,uemail=email,ubirth=birth,usex=sex,uimage=file_obj,umoney=1)
            student.save()
        hlsdic = {'status':'success'}
        response = JsonResponse(hlsdic, safe=False)
        response["Access-Control-Allow-Origin"] = "*"
        response["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
        response["Access-Control-Max-Age"] = "1000"
        response["Access-Control-Allow-Headers"] = "*"
        return response

