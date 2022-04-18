from django.db import models
import uuid
from users.models import Profile

# Project Table
class Project (models.Model):
    # id (Primary Key)
    id = models.UUIDField(default=uuid.uuid4, unique=True , primary_key=True, editable=False)
    #owner (Foreign Key One To Many Relation)
    owner = models.ForeignKey(Profile,null=True, blank=True , on_delete=models.SET_NULL)
    # title
    title = models.CharField(max_length=200)
    # description  
    description = models.TextField(null=True, blank=True)
    # demo_link 
    demo_link= models.CharField(max_length=2000 ,null=True, blank=True)
    # source_link 
    source_link= models.CharField(max_length=2000 ,null=True, blank=True)
    # created 
    created = models.DateTimeField(auto_now_add=True)
    # image
    image = models.ImageField(null=True , blank=True , default="default.jpg")
    # vote_count 
    vote_count = models.IntegerField(default=0 , null=True , blank=True)
    # vote_ratio 
    vote_ratio = models.IntegerField(default=0 , null=True , blank=True)
    # tag_id (Foreign Key in Many To Many Relation) 
    # Django Create a Dummy Table that includes tag_id && project_id
    tag_id = models.ManyToManyField('Tag' , blank = True) 

    def __str__(self):
        return self.title


# Review Table
class Review (models.Model):
    VOTE_TYPE = (
        ('up','Up Vote'),
        ('down' , 'Down Vote')
    )
    # id (Primary Key)
    id = models.UUIDField(default=uuid.uuid4, unique=True , primary_key=True, editable=False)
    # project (Foreign Key One To Many Relation)
    project = models.ForeignKey(Project , on_delete=models.CASCADE)
    #owner (Foreign Key One To One Relation)
    #######################################
    # body
    body = models.TextField(null=True , blank=True)
    # value
    value = models.CharField(max_length=200 , choices = VOTE_TYPE )
    # created
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.value


# Tag Table
class Tag (models.Model):
    # id (Primary Key)
    id = models.UUIDField(default=uuid.uuid4, unique=True , primary_key=True, editable=False)
    # name (Primary Key)
    name = models.CharField(max_length=200)
    # created
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name