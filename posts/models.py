from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(User, related_name='posts')
    title = models.CharField(max_length=200)
    body = models.TextField()
    #pub_date = models.DateTimeField(auto_now_add=True)
    #up_date = models.DateTimeField(auto_now=True)
    
    pub_date = models.DateTimeField('Date Published', auto_now_add=True)
    up_date = models.DateTimeField('Date Updated', auto_now=True)
    
    def __unicode__(self):
        return self.title