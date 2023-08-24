from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from zhigeng.models import Upload_list
from django.conf import settings
import os
import json
from zhigeng.inport_xlc import Title_Entry
# def home(request):
#     return HttpResponse('Hello, world!')
# Create your views here.
# def Upload_list_(request):
#     # res = Upload_list.object.all()
#     res=Upload_list.objects.all()
#     return  render(request,"result.html",{"res":res})
def list(request):
    """
        :param file: 文件路径
        :param header: 所需平台的header
        :param platform: 平台
        :param environment: 环境
    :return:
    """
    my_response = HttpResponse("list")
    my_response["Access-Control-Allow-Origin"] = "http://127.0.0.1:2020"
    # if request.method == "GET":  # 如果提交方式是POST方法，执行如下代码
    if request.method == "POST":  # 如果提交方式是POST方法，执行如下代码
        # result=(request.form)         #使用request方法获取表单信息并传给result
        data={}
        # result = (request.form)
        # result =request.body
        # print(result,11111111111111111)
        # print(11111111111111111)
        result = request.POST
        file = request.FILES['file']
        file_name = file.name
        file_path=os.path.join(settings.MEDIA_ROOT,file_name)
        with open(file_path, 'wb+') as destination:
            for chunk in file.chunks():
                destination.write(chunk)
        # t = Title_Entry(file_path, result.get('header'), result.get('platform'), result.get('environment'))
        # num = t.add()
        # result['Access-Control-Allow-Origin']="*"
        data['header']=result.get('header')
        data['platform']=result.get('platform')
        data['environment']=result.get('environment')
        data['file_name']=file_path
        # if num['num']==0:
        #     code=403
        # else:
        #     code=200
        # data['num']=num['num']
        # data['msg'] = num['msg']
        data['num']='num'
        data['msg']='msg'



        return JsonResponse({'data': data,"code":200})
    data={
        'msg':"上传失败",
        "num":0
    }
    return JsonResponse({'data': data,'code': 403})