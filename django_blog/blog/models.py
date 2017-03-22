from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length = 100) #title
    category = models.CharField(max_length = 50, blank = True) #categore
    date_time = models.DateTimeField(auto_now_add = True) #timestamp
    content = models.TextField(blank = True, null = True) #content

    # python2 __unicode__
    # python3 __str__
    def __unicode__(self):
        return self.title

    class Meta: # sort by time in descending order
        ordering = ['-date_time']


 # get URL
    def get_absolute_url(self):
        path = reverse('detail', kwargs={'id':self.id})
        return "http://127.0.0.1:8000%s" % path
