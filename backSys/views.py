# Create your views here.
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

def login(request):
	return render(request, 'blog/login.html' )
