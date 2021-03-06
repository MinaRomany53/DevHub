from django.forms import ModelForm 
from django.contrib.auth.forms import UserCreationForm  
from django.contrib.auth.models import User
from .models import Profile , Skill

# Inherit from UserCreationForm Class
class CustomUserCreationForm(UserCreationForm):  
    class Meta:
        model = User
        fields =['first_name','email','username','password1','password2']
        labels = {
            'first_name': "Name",
        }

class profileForm (ModelForm):  
    class Meta:
        model = Profile
        fields = ['name','email','username','headline','image','bio','location','social_github','social_twitter','social_linkedin','social_stackoverflow','social_website']


class SkillForm (ModelForm):  
    class Meta:
        model = Skill
        fields = ['name','description']