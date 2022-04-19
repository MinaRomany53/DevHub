import email
from django.db import models
from django.contrib.auth.models import User # User Table already implemented
import uuid

# Profile Table
class Profile (models.Model):
    # id (Primary Key)
    id = models.UUIDField(default=uuid.uuid4, unique=True , primary_key=True, editable=False),
    # user (Foreign Key One To One Relation)
    user = models.OneToOneField(User , on_delete=models.CASCADE,null=True, blank=True)
    # name
    name = models.CharField(max_length=100,null=True, blank=True)
    # email
    email = models.EmailField(max_length=400,null=True, blank=True) 
    # username
    username =  models.CharField(max_length=100,null=True, blank=True)
    # headline
    headline =  models.CharField(max_length=200,null=True, blank=True)
    # image
    image = models.ImageField(null=True , blank=True , default="developer.png" , upload_to='profiles/')
    # bio
    bio =  models.TextField(null=True, blank=True)
    # location
    location =  models.CharField(max_length=200,null=True, blank=True)
    # social_links
    social_github = models.CharField(max_length=2000 ,null=True, blank=True)
    social_twitter = models.CharField(max_length=2000 ,null=True, blank=True)
    social_linkedin = models.CharField(max_length=2000 ,null=True, blank=True)
    social_stackoverflow = models.CharField(max_length=2000 ,null=True, blank=True)
    social_website = models.CharField(max_length=2000 ,null=True, blank=True)
    # created 
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str( self.user)



# Skill Table
class Skill (models.Model):
    # id (Primary Key)
    id = models.UUIDField(default=uuid.uuid4, unique=True , primary_key=True, editable=False),
    #owner (Foreign Key One To Many Relation)
    owner = models.ForeignKey(Profile,null=True, blank=True , on_delete=models.CASCADE)
    # name
    name = models.CharField(max_length=200,null=True, blank=True)
    # description  
    description = models.TextField(null=True, blank=True)
    # created 
    created = models.DateTimeField(auto_now_add=True)
   
    def __str__(self):
        return self.name




