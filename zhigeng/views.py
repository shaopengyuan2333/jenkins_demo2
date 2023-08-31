from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from zhigeng.models import Upload_list
from django.conf import settings
import os
import json
from urllib.parse import unquote
from zhigeng.inport_xlc import Title_Entry
from zhigeng.attack_del_update_limits import Topic_Del_Update
# def home(request):
#     return HttpResponse('Hello, world!')
# Create your views here.
# def Upload_list_(request):
#     # res = Upload_list.object.all()
#     res=Upload_list.objects.all()
#     return  render(request,"result.html",{"res":res})

#添加题目接口
def add(request):
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
        result = request.POST
        file = request.FILES['file']
        file_name = file.name
        file_path=os.path.join(settings.MEDIA_ROOT,file_name)
        with open(file_path, 'wb+') as destination:
            for chunk in file.chunks():
                destination.write(chunk)

        # file = request.FILES['file']
        # fs = FileSystemStorage()
        # filename = fs.save(file.name, file)
        # file_path = fs.url(filename)
        # file_path=unquote(file_path)

        print(file_path,22222222222)
        t = Title_Entry(file_path, result.get('header'), result.get('platform'), result.get('environment'))
        num = t.add()
        # result['Access-Control-Allow-Origin']="*"
        data['header']=result.get('header')
        data['platform']=result.get('platform')
        data['environment']=result.get('environment')
        data['file_name']=file_path
        # if num['num']==0:
        #     code=403
        # else:
        #     code=200
        # uploads['num']=num['num']
        # uploads['msg'] = num['msg']
        data['num']='num'
        data['msg']='msg1'



        return JsonResponse({'uploads': data,"code":200})
    data={
        'msg':"上传失败",
        "num":0
    }
    return JsonResponse({'uploads': data,'code': 403})
#上传文件
def upload_file(request):
    if request.method == 'POST' and request.FILES['file']:
        file = request.FILES['file']
        filePath = os.path.join(settings.MEDIA_ROOT, file.name)
        with open(filePath, 'wb+') as fp:
            for info in file.chunks():
                fp.write(info)
        # fs = FileSystemStorage()
        # filename = fs.save(file.name,file)
        # uploaded_file_url = fs.url('uploads/'+filename)
        return JsonResponse({'url': filePath})
    return JsonResponse({'error': 'Invalid request or no file provided.'})

#修改题目权限接口
def  update_topic_limits(request):
    try:
        if request.method == "POST":  # 如果提交方式是POST方法，执行如下代码
            # result=(request.form)         #使用request方法获取表单信息并传给result
            data={}
            result = request.POST
            data['header'] = result.get('header')
            data['platform'] = result.get('platform')
            data['environment'] = result.get('environment')
            data['app_id'] = result.get('app_id')

            t=Topic_Del_Update(data['platform'],data['environment'],data['header'])
            update_res=t.update_ti( data['app_id'])
            # if update_res['code']==0:
            #     code=403
            # else:
            #     code=200
            # uploads['num']=num['num']
            # uploads['msg'] = num['msg']
            data['num'] = 'num'
            data['msg'] = 'msg1'

            return JsonResponse({'total': update_res['num'],'msg': update_res['msg'], "code": update_res['code']})
    except Exception as e :
        msg=f'接口错误{e}'
        return JsonResponse({'msg': msg, 'code': 403})