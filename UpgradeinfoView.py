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



class UpgradeinfoView(View):
    def get(self,request):
        name = request.session.get('name')
        student =  BaseTable.Ustudentinfo.objects.get(name=name)
        hlsdic = {'status':'fail'}
        if ( student.can_upgrade) == "Tru" :
            hlsdic['status'] = 'success'
        response = JsonResponse(hlsdic, safe=False)
        response["Access-Control-Allow-Origin"] = "*"
        response["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
        response["Access-Control-Max-Age"] = "1000"
        response["Access-Control-Allow-Headers"] = "*"
        return response

    @csrf_exempt
    def post(self,request):
        name = request.session.get('name')
        student =  BaseTable.Ustudentinfo.objects.get(name=name)
        teacher = BaseTable.Uteacherinfo(name=student.name,upasswd=student.upasswd,uemail=student.uemail,ubirth=student.ubirth,uimage=student.uimage,umoney=student.umoney,usex=student.usex,uGo_credential=request.POST.get("uGo_credential"),uTeach_credential=request.POST.get("teach_credential"),udescripition=request.POST.get("descripition"),can_createschool=False)
        student.delete()
        teacher.save()
        hlsdic = {'status':'success'}
        response = JsonResponse(hlsdic, safe=False)
        response["Access-Control-Allow-Origin"] = "*"
        response["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
        response["Access-Control-Max-Age"] = "1000"
        response["Access-Control-Allow-Headers"] = "*"
        return response
