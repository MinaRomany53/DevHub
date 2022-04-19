from django.shortcuts import render , redirect
from django.contrib.auth.models import User # User Table 
from .models import Profile
 
from django.contrib.auth import authenticate , login ,logout
# https://docs.djangoproject.com/en/4.0/ref/contrib/messages/
from django.contrib import messages 
from django.contrib.auth.decorators import login_required


# Authentication 
def loginUser (request):

    # Hide LogIn Page from loggedin users 
    if request.user.is_authenticated:
        return redirect("profiles")


    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        try:
            checkUser = User.objects.get(username=username)
        except:
            # print("Sorry, User Not Found !")
            messages.error(request, "Sorry, User Not Found !")

        checkUser = authenticate(request , username=username , password=password) 

        if checkUser:
            login(request,checkUser)  # Start Session using Cookies 
            return redirect("profiles")
        else:
            # print("Wrong Username OR Password !")
            messages.error(request, "Wrong Username OR Password !")

    return render(request , "users/login-sign.html" )


def logoutUser (request):
    logout(request)  # End Session
    messages.success(request, "You Logged Out Successfully.")
    return redirect("login")






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