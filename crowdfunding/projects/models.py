from django.contrib.auth import get_user_model #added from users doc
from django.db import models
from django.contrib.auth.models import User #added for comments

User = get_user_model() #added from users doc

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    goal = models.IntegerField()
    image = models.URLField()
    is_open = models.BooleanField()
    date_created = models.DateTimeField(auto_now_add=True) ###added
    owner = models.ForeignKey( #from ownder, added from users doc
        User,
        on_delete=models.CASCADE,
        related_name='owner_projects'
    )
    
#new model added from DRF sheet 2
class Pledge(models.Model):
    pledge_amount = models.IntegerField()
    comment = models.CharField(max_length=200)
    anonymous = models.BooleanField()
    project = models.ForeignKey(
        'Project',
        on_delete=models.CASCADE,
        related_name='pledges'
    )
    supporter = models.ForeignKey( #from here added from user doc
        User,
        on_delete=models.CASCADE,
        related_name='supporter_pledges'
    )

#below block added for comments
class Comment(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True) ####added
    author = models.ForeignKey( 
        User,
        on_delete=models.CASCADE,
        related_name='owner_comment'
    )
    project = models.TextField()
    content = models.TextField(blank=True, null=True) ###added
    created_at = models.DateTimeField(auto_now_add=True)
    commentee = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='commentee_comment') ###added
    
