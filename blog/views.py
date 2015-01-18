# coding: utf-8  
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext, loader
from django.shortcuts import render,get_object_or_404,RequestContext
from django.core.urlresolvers import reverse
from django.views import generic
#from blog.models import Poll,Choice,Blog
from django import forms
from debateSNS.models import *
import datetime
from django.utils import timezone
from django.conf import settings
import hashlib


'''def index(request):
    latest_poll_list = Poll.objects.all().order_by('-pub_date')[:5]
    context = {'latest_poll_list': 1}
    return render(request, 'blog/index.html', context)
'''

def __checkin__(request):
    try:
        request.session['username']
    except KeyError,e:
        return HttpResponseRedirect('login.html')

def login(request):
    return render(request, 'blog/login.html' )

def logout(request):
    del request.session['username']
    return HttpResponseRedirect("login.html")

def loginCertifacate(request):
    if request.method == 'POST': 
    # If the form has been submitted...
        username = request.POST.get("username")
        tmpPassword = request.POST.get("password")
        md5Encode = hashlib.new("ripemd160")
        md5Encode.update(tmpPassword)
        password = md5Encode.hexdigest()

        user = get_object_or_404(User, username=username)
        if user.password == password:
            request.session['username'] = username
            return HttpResponseRedirect('/blog/news/show')
        else:
            return HttpResponse("密码错误") 
        

def contact(request):
    '''if request.method == 'POST': # If the form has been submitted...
        # ContactForm was defined in the previous section
        form = ContactForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            subject = {'data': 2}
            context = {'latest_poll_list': 1}
            return render(request, 'tt/index.html', {'data':2,
            											'bigcity':2})
            #return HttpResponseRedirect('/thanks/') # Redirect after POST
    else:
        form = ContactForm() # An unbound form

    return render(request, 'contact.html', {
        'form': form,
    })
'''
    if request.method == 'POST':
        username = request.POST.get("username")
        request.session['username'] = data
        return HttpResponse(data)
        return render(request, 'blog/index.html', {'data':data,'bigcity':2})
    else:
        return HttpResponse(request.session['username'])

def addUserView(request):
    return render(request,"blog/addUserView.html")

def addUser(request):
    md5Encode = hashlib.new("ripemd160")
    username = request.POST.get("username")
    tmpPassword = request.POST.get("password")
    confirmPassword = request.POST.get("password2")
    if tmpPassword != confirmPassword:
        return HttpResponse("两次输入的密码不一致")
    md5Encode.update(tmpPassword)
    password = md5Encode.hexdigest()
    
    veryfyUser = User.objects.filter(username = username).all()
    
    try:
        HttpResponse(veryfyUser[0])
    except IndexError,e:
        veryfyUser = None
    if veryfyUser is not None:
        return HttpResponse("This user is already exits")

    user = User(
        username = username,
        password = password
        )
    user.save()
    return render(request,"blog/login.html")
 
def changePasswd(request):
    if request.method == "POST":
        username = request.POST.get("username")
        tmpPassword = request.POST.get("password")
        newPassword = request.POST.get("newPassword")
        md5Encode = hashlib.new("ripemd160")
        md5Encode.update(tmpPassword)
        password = md5Encode.hexdigest()

        user = get_object_or_404(User, username=username)
        if user.password == password:
            newEncode = hashlib.new("ripemd160")
            newEncode.update(newPassword)
            user.password = newEncode.hexdigest()
            user.save()
            del request.session['username']
            return HttpResponseRedirect("login.html")
        else:
            return HttpResponse("密码错误")    
        
    else:
        return render(request,"blog/changePasswd")

def index(request):
    return render(request,'blog/index2.html',{'news':News.objects.all()})
    return render(request,'blog/index2.html')


########################################################
# this view is about the news 
# contains show news list , add news , change news, 
# delete news,and add new news
# News contain three parts , title content date                 
########################################################

def news(request,method,Oid):
    try:
        request.session['username']
    except KeyError,e:
        return HttpResponseRedirect('login.html')

    if method == 'addNews' or method == '':
        title = request.POST.get('title')
        content = request.POST.get('content')
        date = datetime.datetime.now()
        news = News(
            title=title,
            content = content,
            date = date,
            uploadUser = request.session['username'],

            )
        news.save()
        #Oid = news.id
        return HttpResponseRedirect('/blog/news/show')
    elif method == 'change':
        news = News.objects.get(id=Oid)
        News.date_format(news)
        #return HttpResponse(Oid)
        return render(request,'blog/changeNews.html',{'news':news})
    elif method == 'save':
        if request.method == 'POST':
            news = {'id' : request.POST.get('id'),
                'title' : request.POST.get('title'),
                'content' : request.POST.get('content'),
                'date' : request.POST.get('date')
                }

        News.objects.filter(id=news['id']).update(content=news['content'])
        News.objects.filter(id=news['id']).update(title=news['title'])
        News.objects.filter(id=news['id']).update(date=news['date'])
       
        return HttpResponseRedirect('/blog/news/show')
    elif method == 'delete':
        News.objects.filter(id=Oid).delete()
        return HttpResponseRedirect('../show')
    elif method == 'add':
        return render(request,'blog/addNewsView.html')
    elif method == 'show':
        allNews = News.objects.all()
        for element in allNews:
             News.date_format(element)
        return render(request,'blog/showNewsList.html',{'news':index})
    else:
        return HttpResponse('没有该方法')


########################################################
# this view is about the product 
# contains show news list , add news , change news, 
# delete news,and add new news
# News contain three parts , title content date                 
########################################################
#

def product(request,method,Oid):
    try:
        request.session['username']
    except KeyError,e:
        return HttpResponseRedirect('login.html')
    if method == 'addProduct':
        title = request.POST.get('title')
        content = request.POST.get('content')
        product = Product(
            title=title,
            content = content,
            uploadUser = request.session['username'],
            )
        product.save()
        #return HttpResponse(product.id)
        return HttpResponseRedirect('/blog/product/show')
    elif method == 'change':
        return render(request,'blog/changeProduct.html',{'product':Product.objects.get(id=Oid)})

    elif method == 'save':
        if request.method == 'POST':
            product = {'id' : request.POST.get('id'),
                'title' : request.POST.get('title'),
                'content' : request.POST.get('content'),
                }

        Product.objects.filter(id=product['id']).update(content=product['content'])
        Product.objects.filter(id=product['id']).update(title=product['title'])
        Oid = product['id']
        return HttpResponseRedirect('/blog/product/show')

    elif method == 'delete':
        Product.objects.filter(id=Oid).delete()
        return HttpResponseRedirect('../show')
    elif method == 'add':
        return render(request,'blog/addProductView.html')
    elif method == 'show':
        return render(request,'blog/showProductList.html',{'product':Product.objects.all()})
    else:
        return HttpResponse('没有该方法')


########################################################
# this view is about the Plan 
# contains show news list , add news , change news, 
# delete news,and add new news
# News contain three parts , title content date                 
########################################################


def plan(request,method,Oid):
    try:
        request.session['username']
    except KeyError,e:
        return HttpResponseRedirect('login.html')
    if method == 'addPlan':
        title = request.POST.get('title')
        content = request.POST.get('content')
        plan = Plan(
            title=title,
            content = content,
            uploadUser = request.session['username'],
            )
        plan.save()
        #Oid = news.id
        return HttpResponseRedirect('/blog/plan/show')
    elif method == 'change':
        return render(request,'blog/changePlan.html',{'plan':Plan.objects.get(id=Oid)})

    elif method == 'save':
        if request.method == 'POST':
            plan = {'id' : request.POST.get('id'),
                    'title' : request.POST.get('title'),
                    'content' : request.POST.get('content'),
                    }

            Plan.objects.filter(id=plan['id']).update(content=plan['content'])
            Plan.objects.filter(id=plan['id']).update(title=plan['title'])
            Oid = plan['id']
        return HttpResponseRedirect('/blog/plan/show')

    elif method == 'delete':
        Plan.objects.filter(id=Oid).delete()
        return HttpResponseRedirect('../show')
    elif method == 'add':
        return render(request,'blog/addPlanView.html')
    elif method == 'show':
        return render(request,'blog/showPlanList.html',{'plan':Plan.objects.all()})
    else:
        return HttpResponse('没有该方法')

########################################################
# this view is about the us
# contains show news list , add  Us , change Us, 
# delete one,and add new one
# News contain three parts , title content date                 
########################################################

def us(request,method,Oid):
    try:
        request.session['username']
    except KeyError,e:
        return HttpResponseRedirect('login.html')
    if method == 'addUs':
        title = request.POST.get('title')
        content = request.POST.get('content')
        order = request.POST.get('order')
        us = Us(
            title=title,
            order = order,
            content = content,
            uploadUser = request.session['username'],
            )
        us.save()
        #Oid = news.id
        return HttpResponseRedirect('/blog/us/show')
    elif method == 'change':
        return render(request,'blog/changeUs.html',{'us':Us.objects.get(id=Oid)})
    elif method == 'save':
        if request.method == 'POST':
            us = {'id' : request.POST.get('id'),
                    'title' : request.POST.get('title'),
                    'content' : request.POST.get('content'),
                    'order': request.POST.get('order'),
                    }

            Us.objects.filter(id=us['id']).update(content=us['content'])
            Us.objects.filter(id=us['id']).update(title=us['title'])
            Us.objects.filter(id=us['id']).update(order=us['order'])
            Oid = us['id']

        return HttpResponseRedirect('/blog/us/show')

    elif method == 'delete':
        Us.objects.filter(id=Oid).delete()
        return HttpResponseRedirect('../show')
    elif method == 'add':
        return render(request,'blog/addUsView.html')
    elif method == 'show':
        return render(request,'blog/showUsList.html',{'us':Us.objects.all()})
    else:
        return HttpResponse('没有该方法')



########################################################
# this view is about the recruit
# contains show news list , add  Us , change Us, 
# delete one,and add new one
# News contain three parts , title content date                 
########################################################


def recruit(request,method,Oid):
    try:
        request.session['username']
    except KeyError,e:
        return HttpResponseRedirect('login.html')
    if method == 'addRecruit':
        title = request.POST.get('title')
        content = request.POST.get('content')
        recruit = Recruit(
            title=title,
            content = content,
            uploadUser = request.session['username'],
            )
        recruit.save()
        #Oid = news.id
        return HttpResponseRedirect('/blog/recruit/show')
    elif method == 'change':
        return render(request,'blog/changeRecruit.html',{'recruit':Recruit.objects.get(id=Oid)})
    elif method == 'save':
        if request.method == 'POST':
            recruit = {'id' : request.POST.get('id'),
                    'title' : request.POST.get('title'),
                    'content' : request.POST.get('content'),
                    }

            Recruit.objects.filter(id=recruit['id']).update(content=recruit['content'])
            Recruit.objects.filter(id=recruit['id']).update(title=recruit['title'])
            Oid = recruit['id']

        return HttpResponseRedirect('/blog/recruit/show')

    elif method == 'delete':
        Recruit.objects.filter(id=Oid).delete()
        return HttpResponseRedirect('../show')
    elif method == 'add':
        return render(request,'blog/addRecruitView.html')
    elif method == 'show':
       return render(request,'blog/showRecruitList.html',{'recruit':Recruit.objects.all()})

    else:
        return HttpResponse('没有该方法')


########################################################
# this view is about the contact
# contains show news list , add  Us , change Us, 
# delete one,and add new one
# News contain three parts , title content date                 
########################################################


def contact(request,method,Oid):
    try:
        request.session['username']
    except KeyError,e:
        return HttpResponseRedirect('login.html')
    if method == 'addContact':
        tel = request.POST.get('tel')
        email = request.POST.get('email')
        address = request.POST.get('address')
        contact = Contact(
            tel=tel,
            email = email,
            address = address,
            uploadUser = request.session['username'],
            )
        contact.save()
        return HttpResponseRedirect('/blog/contact/show')
    elif method == 'change':
        return render(request,'blog/changeContact.html',{'contact':Contact.objects.get(id=Oid)})
    elif method == 'save':
        if request.method == 'POST':
            contact = {'id' : request.POST.get('id'),
                    'title' : request.POST.get('title'),
                    'content' : request.POST.get('content'),
                    }

            Contact.objects.filter(id=contact['id']).update(content=contact['content'])
            Contact.objects.filter(id=contact['id']).update(title=contact['title'])
        return HttpResponseRedirect('/blog/contact/show')

    elif method == 'delete':
        Contact.objects.filter(id=Oid).delete()
        return HttpResponseRedirect('../show')
    elif method == 'add':
        return render(request,'blog/addContactView.html')
    elif method == 'show':
       return render(request,'blog/showContactList.html',{'contact':Contact.objects.all()})

    else:
        return HttpResponse('没有该方法')


##################################################################################################
#  file operation 
#   about image and video
##################################################################################################

def addImage(request):
    try:
        request.session['username']
    except KeyError,e:
        return HttpResponseRedirect('login.html')   
    if request.method == "POST":
        return HttpResponse(1)
    return render(request,'blog/addImage.html')

def addImageInfo(request):
    if request.method == "POST":
        des_origin_path = settings.UPLOAD_PATH+'/images/'+request.POST.get('title')
        des_origin_f = open(des_origin_path, "ab") 
        tmpImg = request.FILES['img']
        for chunk in tmpImg.chunks():  
            des_origin_f.write(chunk)   
        des_origin_f.close() 
        img = Image(
            title = request.POST.get('title'),
            location = des_origin_path,
            uploadUser = request.session['username'],
            )
        img.save()
        return HttpResponseRedirect('showImgList')
    return HttpResponse('allowed only via POST')

def showImgList(request):
    try:
        request.session['username']
    except KeyError,e:
        return HttpResponseRedirect('login.html')    
    return render(request,'blog/showImgList.html',{'image':Image.objects.all() })

def deleteImg(request,Oid):
    Image.objects.filter(id=Oid).delete()
    return HttpResponseRedirect('../showImgList')
def test(request):
    BASE_DIR = os.path.dirname(os.path.dirname(__file__))
    return   HttpResponse(BASE_DIR)
