from django.shortcuts import render , redirect
from django.contrib.auth.models import User

from projects.views import projects # User Table 
from .models import Profile
 
from django.contrib.auth import authenticate , login ,logout
# https://docs.djangoproject.com/en/4.0/ref/contrib/messages/
from django.contrib import messages 
from django.contrib.auth.decorators import login_required

#https://www.javatpoint.com/django-usercreationform
from django.contrib.auth.forms import UserCreationForm  
from .forms import CustomUserCreationForm , profileForm ,SkillForm


################################################################
######################## Authentication ######################## 
################################################################
def loginUser (request):

    # Hide LogIn Page from logged in users 
    if request.user.is_authenticated:
        return redirect("profiles")


    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        try:
            checkUser = User.objects.get(username=username)
        except:
            # print("Sorry, User Not Found !")
            messages.error(request, "Sorry, User Not Found")

        checkUser = authenticate(request , username=username , password=password) 

        if checkUser:
            login(request,checkUser)  # Start Session using Browser Cookies 
            return redirect("account")
        else:
            # print("Wrong Username OR Password !")
            messages.error(request, "Wrong Username OR Password")

    page = "login"
    context = {"page":page}
    return render(request , "users/login-register.html" , context)


def logoutUser (request):
    logout(request)  # End Session
    messages.success(request, "You Logged Out Successfully.")
    return redirect("login")


def registerUser (request):
    form = CustomUserCreationForm()

    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            login(request,user) # Start Session using Browser Cookies 
            return redirect("edit-account")
        else:
            messages.error(request, "An Error Occurred Please Enter Valid Data ")

    page = "register"
    context = {"page":page, "form":form}
    return render(request , "users/login-register.html" , context)
################################################################
######################## Authentication ######################## 
################################################################



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


@login_required(login_url="login")
def account (request):
    profile = request.user.profile
    skills = profile.skill_set.all()
    projects = profile.project_set.all()

    context = {'profile' : profile , 'skills':skills , 'projects':projects }
    return render(request , 'users/account.html', context)


@login_required(login_url="login")
def editAccount (request):
    currProfile = request.user.profile
    form = profileForm(instance=currProfile)
    if request.method == "POST":
        form = profileForm(request.POST,request.FILES,instance=currProfile)
        if form.is_valid():
            form.save()
            messages.success(request, "Your Account Info Updated Successfully ")
            return redirect("account") 


    context={"form":form}
    return render (request , "users/profile_form.html" , context)


@login_required(login_url="login")
def addSkill (request):
    currprofile = request.user.profile
    form = SkillForm()
    if request.method == "POST":
        form = SkillForm(request.POST)
        if form.is_valid:
            skill = form.save(commit=False)
            skill.owner = currprofile
            skill.save()
            messages.success(request, "Your Skill Added Successfully ")
            return redirect("account") 


    context={"form": form}
    return render(request , 'users/skill_form.html' ,context)


@login_required(login_url="login")
def editSkill (request , pk):
    currprofile = request.user.profile
    skill = currprofile.skill_set.get(id=pk)
    form = SkillForm(instance=skill)
    if request.method == "POST":
        form = SkillForm(request.POST,instance=skill)
        if form.is_valid:
            form.save()
            messages.success(request, "Your Skill Updated Successfully ")
            return redirect("account") 


    context={"form": form}
    return render(request , 'users/skill_form.html' ,context)


@login_required(login_url="login")
def deleteSkill (request , pk):
    currprofile = request.user.profile
    skill = currprofile.skill_set.get(id=pk)
    if request.method == "POST":
        skill.delete()
        messages.success(request, "Your Skill deleted Successfully ")
        return redirect("account") 

    skillMessage =  True
    context={"object": skill , "skillMessage":skillMessage}
    return render(request , 'users/delete_template.html' ,context)