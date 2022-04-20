from pickle import FALSE
from django.shortcuts import render , redirect
from django.contrib.auth.models import User # User Table 
from .models import Profile
 
from django.contrib.auth import authenticate , login ,logout
# https://docs.djangoproject.com/en/4.0/ref/contrib/messages/
from django.contrib import messages 
from django.contrib.auth.decorators import login_required

#https://www.javatpoint.com/django-usercreationform
from django.contrib.auth.forms import UserCreationForm  
from .forms import CustomUserCreationForm



# Authentication 
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
            return redirect("profiles")
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
            form.save()
            messages.success(request, "Your Account Created Successfully ")
            return redirect("login")
        else:
            messages.error(request, "An Error Occurred Please Enter Valid Data ")

    page = "register"
    context = {"page":page, "form":form}
    return render(request , "users/login-register.html" , context)




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