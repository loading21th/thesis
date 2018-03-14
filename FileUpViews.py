# coding:utf-8
from django.shortcuts import render
from django.views.generic import View

from django.http import HttpResponse
from django.http import FileResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
# Create your views here.
from fileup.llmodels.homewore_courseware import Homewore_Courseware
import os 
import json



class FileUpView(View):
    def get(self,request,school_name,class_name):
        hlsdic = {'school_name':school_name,'class_name':class_name,'sum':3}
        return render(request,'index.html',hlsdic);
    
    @csrf_exempt
    def post(self,request,school_name,class_name):
        upload_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))),'uploadfile',school_name,class_name)
        print(upload_path)

        if not os.path.exists(upload_path):
            os.makedirs(upload_path)
        if request.FILES:
            print ('**********add data*********')
            file_obj = request.FILES.getlist('filename')[0]
            hh = Homewore_Courseware(schoolname=school_name,classname=class_name,homework=file_obj)
            hh.save()
            print ('**********save over*********')

        hlsdic = {'Courseware_name':os.listdir(upload_path)}
        response = JsonResponse(hlsdic, safe=False)
        response["Access-Control-Allow-Origin"] = "*"
        response["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
        response["Access-Control-Max-Age"] = "1000"
        response["Access-Control-Allow-Headers"] = "*"
        return response

class FileDownload(View):
    def get(self,request,school_name,class_name,filename):
        fullpath = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))),'uploadfile',school_name,class_name,filename)
        ffile = open(fullpath,'rb')
        response = FileResponse(ffile)
        print(filename)
        response['Content-Type'] = "application/octet-stream"
        response['Content-Disposition'] = 'attachment;filename="{0}"'.format(filename)
        return response 
