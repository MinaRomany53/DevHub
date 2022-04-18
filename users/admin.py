from django.contrib import admin
from .models import Profile , Skill

 # showing this Models in the Admin Panel
admin.site.register(Profile)
admin.site.register(Skill)