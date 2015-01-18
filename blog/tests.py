"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""
import datetime

from django.utils import timezone
from django.test import TestCase

from blog.models import Poll

class PollMethodTests(TestCase):

    def was_published_recently(self):
	    now = timezone.now()
	    return now - datetime.timedelta(days=1) <= self.pub_date <= now
