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



class TeacherView(View):
    def get(self,request):
        teacher = BaseTable.Uteacherinfo.objects.get(name=request.session['name'])
        context = {}
        context['yue'] = teacher.umoney
        return render(request,'teacherinfo.html',context);

    @csrf_exempt
    def post(self,request):
        teacher = BaseTable.Uteacherinfo.objects.get(name=request.session['name'])
        nowmoney = teacher.umoney
        money_update_sum = request.POST.get('money_update_sum')
        stat = "操作失败，请重试"

        if (request.POST.get('is_add')== "yes"):
            nowmoney = nowmoney + int(money_update_sum)
        else:
            nowmoney = nowmoney - int(money_update_sum)

        if nowmoney < 0:
            stat = "提款失败，余额不足"
        elif nowmoney > 10000:
            stat = "充值资金过多，有风险"
        else:
            stat = "success"
            teacher.umoney = nowmoney
            teacher.save()
        result = {'status':stat}
        response = JsonResponse(result, safe=False)
        response["Access-Control-Allow-Origin"] = "*"
        response["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
        response["Access-Control-Max-Age"] = "1000"
        response["Access-Control-Allow-Headers"] = "*"
        return response
