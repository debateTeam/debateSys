# coding: utf-8  

from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext, loader
from django.shortcuts import render,get_object_or_404,RequestContext

from django.views import generic
#from blog.models import Poll,Choice,Blog
from django import forms
from debateSNS.models import *
import datetime
from django.utils import timezone
from django.conf import settings
import hashlib

# Create your views here.
def Index(request):
	return HttpResponse("密码错误") 

def Member(request):
	return HttpResponse("get the mumber")

def Article(request):
	return	HttpResponse("get the articele")

def Register(request):
	return HttpResponse("register the MM")

