from django.shortcuts import render , redirect
from django.http import HttpResponse

from .models import Profile ,Skill


def profiles(request):
    profiles = Profile.objects.all()
    context = {'profiles' : profiles}
    return render(request , "users/profiles.html" , context)

def profile(request , pk):
    profile = Profile.objects.get(id=pk)
    skills = profile.skill_set.all()
    topSkills = []
    otherSkills = []
    for skill in skills:
        if skill.description:
            topSkills.append(skill)
        else:    
            otherSkills.append(skill)

    context = {'profile' : profile , 'topSkills':topSkills,'otherSkills':otherSkills}
    return render(request , "users/user_profile.html" , context)