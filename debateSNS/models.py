import datetime
from django_mongodb_engine.contrib import MongoDBManager
from django.db import models
from django.utils import timezone
from djangotoolbox.fields import  ListField
from django import forms

class News(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date = models.DateTimeField()
    uploadUser = models.CharField(max_length = 100)
    objects = MongoDBManager();
    def date_format(self):
       self.date = self.date.strftime("%Y-%m-%d")
    
    def __unicode__(self):
            return self.title
        
class Product(models.Model):
    title = models.CharField(max_length=100)
    uploadUser = models.CharField(max_length = 100)
    content = models.TextField()
    
    def __unicode__(self):
            return self.title
        
class Plan(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    uploadUser = models.CharField(max_length = 100)
    
    def __unicode__(self):
            return self.title
        
class Us(models.Model):
    title = models.CharField(max_length=100)
    order = models.SmallIntegerField()
    uploadUser = models.CharField(max_length = 100)
    content = models.TextField()
    
    def __unicode__(self):
            return self.title

class admin(models.Model):
	username = models.CharField(max_length=100)
	password = models.CharField(max_length=100)

class Recruit(models.Model):
    title  = models.CharField(max_length=100)
    uploadUser = models.CharField(max_length = 100)
    content = models.TextField()

class Contact(models.Model):
    tel = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    uploadUser = models.CharField(max_length = 100)

class Image(models.Model):
    title = models.CharField(max_length=50)
    location = models.CharField(max_length=200)
    uploadUser = models.CharField(max_length = 100)
    #file = models.ImageField(upload_to = 'pic_folder/', default = 'pic_folder/None/no-img.jpg')
    
class Activity(models.Model):
    issue_name = models.CharField(max_length = 100)
    introduction = models.CharField(max_length = 500)
    time = models.DateTimeField()
    pulisher = models.CharField(max_length = 100)
    def date_format(self):
        self.time = self.time.strftime("%Y-%m-%d")
    def __unicode__(self):
        return self.title

class Article(models.Model):
    name = models.CharField(max_length = 100)
    publish_time = models.DateTimeField()
    author = models.CharField(max_length =100)
    introduction = models.CharField(max_length = 100)
    content = models.CharField(max_length = 2000)
    def date_format(self):
        self.publish_time = self.publish_time.strftime("%Y-%m-%d")
    def __unicode__(self):
        return self.title

class Member(models.Model):
    name = models.CharField(max_length = 100)
    image = models.CharField(max_length = 200)
    description = models.CharField(max_length = 200)
    blog_href = models.CharField(max_length = 200)
    uploadUser = models.CharField(max_length = 100)

class User(models.Model):
    name = models.CharField(max_length = 100)
    email = models.CharField(max_length = 100)
    password = models.CharField(max_length = 100)
    inviting_code = models.CharField(max_length =50)
    user_flag = models.SmallIntegerField()

class InvitingCode(models.Model):
    code = models.CharField(max_length = 100)
    generate_user = models.CharField(max_length = 100)
    isUsed = models.CharField(max_length = 100)