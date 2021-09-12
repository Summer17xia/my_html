from typing import ChainMap
from django.shortcuts import render
from django.http import HttpResponse
from myapp.models import mylast, myup2
import math
import datetime


# def index(request):
#     for i in range(510,5561):
#         mod = mylast.objects.get(id=i)
#         mod.id=i-509
#         mod.save()

#     return HttpResponse("aa")

# Create your views here.
def index(request):
    sid=1
    mod = mylast.objects
    ulist = mod.filter(id__gte=(sid-1)*20+1,id__lte=sid*20)
    
    if sid<4:
        cnm=[1,2,3,4,5]
    if sid<252 and sid>=4:
        for i in range(sid-2,sid+2):
            cnm=[sid-2,sid-1,sid,sid+1,sid+2]
    if sid>=252:
        cnm=[249,250,251,252,253]
    
    if sid!=1 and sid!=253:
        up=sid-1
        down=sid+1
    if sid==1:
        up=1
        down=sid+1
    if sid==253:
        up=sid-1
        down=253
    context = {"userlist":ulist,"cnm":cnm,"up":up,"down":down}
    # return HttpResponse(ulist)
    # lists = mylast.objects.all()
    return render(request,"myapp/users/hola.html",context)

def hola(request,sid):
    try:
        sid = int(request.POST.get('page'))
    except:
        pass
    mod = mylast.objects
    ulist = mod.filter(id__gte=(sid-1)*20+1,id__lte=sid*20)
    
    if sid<4:
        cnm=[1,2,3,4,5]
    if sid<252 and sid>=4:
        for i in range(sid-2,sid+2):
            cnm=[sid-2,sid-1,sid,sid+1,sid+2]
    if sid>=252:
        cnm=[249,250,251,252,253]
    
    if sid!=1 and sid!=253:
        up=sid-1
        down=sid+1
    if sid==1:
        up=1
        down=sid+1
    if sid==253:
        up=sid-1
        down=253
    context = {"userlist":ulist,"cnm":cnm,"up":up,"down":down}
    # return HttpResponse(ulist)
    # lists = mylast.objects.all()
    return render(request,"myapp/users/hola.html",context)

def upinfo(request,sid):
    try:
        sid = int(request.POST.get('page'))
    except:
        pass
    mod1 = myup2.objects
    mod = mod1.filter()
    ulist = mod1.filter(UPID__gte=mod[(sid-1)*10+1].UPID,UPID__lte=mod[min(sid*10,len(mod)-1)].UPID)
    
    if sid<4:
        cnm=[1,2,3,4,5]
    if sid<114 and sid>=4:
        for i in range(sid-2,sid+2):
            cnm=[sid-2,sid-1,sid,sid+1,sid+2]
    if sid>=114:
        cnm=[111,112,113,114,115]

    
    if sid!=1 and sid!=115:
        up1=sid-1
        down1=sid+1
    if sid==1:
        up1=1
        down1=sid+1
    if sid==115:
        up1=sid-1
        down1=115

    context = {"userlist":ulist,"cnm":cnm,"up1":up1,"down1":down1}
    # return HttpResponse(ulist)
    # lists = mylast.objects.all()
    return render(request,"myapp/users/upinfo.html",context)

def upfind(request):
    now1=datetime.datetime.now()

    calll=str(request.GET.get('kind'))[:-1]
    try:
        sid=int(request.GET.get('page'))
    except:
        sid=int(request.GET.get('page')[:-1])


    mod1 = myup2.objects
    # vedioo=mod1.filter(UP主名称__contains=calll)
    fuck=mod1.filter(UP主介绍__contains=calll)
    gannima=mod1.filter(UPID__contains=calll)
    vedioo=fuck | gannima

    ulist=vedioo[(sid-1)*20:sid*20]

    lennn=math.ceil(len(vedioo)/20)
    lennnn=[str(math.ceil(len(vedioo)/20))]      
    if sid<4:
        cnm=[]
        for i in range(1,min(5,lennn)):
            cnm.append(i)
    if sid<lennn-1 and sid>=4:
        for i in range(sid-2,sid+2):
            cnm=[sid-2,sid-1,sid,sid+1,sid+2]
    if sid>=lennn-1 and sid>=4:
        cnm=[lennn-4,lennn-3,lennn-2,lennn-1,lennn]

    
    if sid!=1 and sid!=lennn:
        up=sid-1
        down=sid+1
    if sid==1:
        up=1
        down=sid+1
    if sid==lennn:
        up=sid-1
        down=lennn
    now2=str(datetime.datetime.now()-now1)[6:]


    context = {"userlist":ulist,"cnm":cnm,"calll":calll,"lennn":lennnn,"up":up,"down":down,"time":now2,"length":len(vedioo)}
    # return HttpResponse(ulist)
    # lists = mylast.objects.all()
    return render(request,"myapp/users/upfind.html",context)
    # return HttpResponse(calll)

def vediofind(request):
    now1=datetime.datetime.now()


    calll=str(request.GET.get('kind'))[:-1]
    try:
        sid=int(request.GET.get('page'))
    except:
        sid=int(request.GET.get('page')[:-1])

    mod1 = mylast.objects
    vedioo=mod1.filter(视频名称__contains=calll)
    fuck=mod1.filter(简介__contains=calll)
    vedioo=vedioo | fuck

    ulist=vedioo[(sid-1)*20:sid*20]
    
    lennn=math.ceil(len(vedioo)/20)
    lennnn=[str(math.ceil(len(vedioo)/20))]      
    if sid<4:
        cnm=[]
        for i in range(1,min(5,lennn)):
            cnm.append(i)
    if sid<lennn-1 and sid>=4:
        for i in range(sid-2,sid+2):
            cnm=[sid-2,sid-1,sid,sid+1,sid+2]
    if sid>=lennn-1 and sid>=4:
        cnm=[lennn-4,lennn-3,lennn-2,lennn-1,lennn]

    
    if sid!=1 and sid!=lennn:
        up=sid-1
        down=sid+1
    if sid==1:
        up=1
        down=sid+1
    if sid==lennn:
        up=sid-1
        down=lennn
    
    now2=str(datetime.datetime.now()-now1)[6:]


    context = {"userlist":ulist,"cnm":cnm,"calll":calll,"lennn":lennnn,"up":up,"down":down,"time":now2,"length":len(vedioo)}
    # return HttpResponse(ulist)
    # lists = mylast.objects.all()
    return render(request,"myapp/users/vediofind.html",context)
    # return HttpResponse(now2)

def find(request):
    aa="/p/another.png"
    context={"aa":aa}
    return render(request,"myapp/users/find.html",context)


def local(request):
    vedio = request.POST.get('title')
    whic = request.POST.get('gender')


    now1=datetime.datetime.now()

    print(whic)
    if whic=="1":
        mod = mylast.objects
        vedioo=mod.filter(视频名称__contains=vedio)
        fuck=mod.filter(简介__contains=vedio)
        vedioo=vedioo | fuck
        lennn=math.ceil(len(vedioo)/20)
        fuck1=vedioo        
        lennnn=[str(math.ceil(len(vedioo)/20))]

        vedioo=vedioo[0:20]
        
        cnm=[]
        for i in range(1,min(5,lennn)):
            cnm.append(i)        
        up=1
        if lennn>1:
            down=2
        else:
            down=1

        now2=str(datetime.datetime.now()-now1)[6:]

        context={"userlist":vedioo,"cnm":cnm,"calll":str(vedio),"lennn":lennnn,"up":up,"down":down,"time":now2,"length":len(fuck1)}

        return render(request,"myapp/users/vediofind.html",context)#这块得单独能一个搜索结果页
    else:
        mod = myup2.objects
        vedioo=mod.filter(UP主名称__contains=vedio)
        fuck=mod.filter(UP主介绍__contains=vedio)
        vedioo=vedioo | fuck        
        lennn=math.ceil(len(vedioo)/20)
        fuck1=vedioo
        lennnn=[str(math.ceil(len(vedioo)/20))]

        vedioo=vedioo[0:20]
        cnm=[]
        for i in range(1,min(5,lennn)):
            cnm.append(i)
        up=1
        if lennn>1:
            down=2
        else:
            down=1

        now2=str(datetime.datetime.now()-now1)[6:]


        context={"userlist":vedioo,"cnm":cnm,"calll":str(vedio),"lennn":lennnn,"up":up,"down":down,"time":now2,"length":len(fuck1)}
        return render(request,"myapp/users/upfind.html",context)#这块得单独能一个搜索结果页

def updetails(request,up=""):
    mod = mylast.objects
    uup=mod.filter(UP主名称=up)
    context={"upppp":uup[0],"uppp":uup}
    return render(request,"myapp/users/updetails.html",context)

def vediodetails(request,vedio=""):
    mod = mylast.objects
    vedioo=mod.filter(视频名称=vedio)[0]
    context={"user":vedioo}
    return render(request,"myapp/users/vediodetails.html",context)