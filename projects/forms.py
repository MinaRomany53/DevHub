
from django.forms import ModelForm ,widgets
from django import forms
from .models import Project

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['title' , 'description' , 'image' ,  'demo_link' , 'source_link' , 'tag_id']
        widgets = {
            'tag_id':forms.CheckboxSelectMultiple()
        }