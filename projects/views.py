from django.shortcuts import render , redirect
from django.contrib.auth.decorators import login_required


from .models import Project, Review ,Tag
from .forms import ProjectForm

def projects(request):
    projects = Project.objects.all()
    context = {"projects":projects}
    return render(request, "projects/projects.html",context)

    
def project(request , pk):
    projectObj = Project.objects.get(id=pk) 
    tags = projectObj.tag_id.all()
    return render(request, "projects/project.html",{"projectObj":projectObj,"tags": tags} )


@login_required(login_url="login") 
def createProject(request):
    form = ProjectForm()
    if request.method == "POST":
        form = ProjectForm(request.POST , request.FILES)
        if form.is_valid():
            form.save()
            return redirect("projects")

    context = {"form":form}
    return render(request, "projects/project_form.html",context)


@login_required(login_url="login") 
def updateProject(request , pk):
    projectObj = Project.objects.get(id=pk) 
    form = ProjectForm(instance=projectObj)
    if request.method == "POST":
        form = ProjectForm(request.POST,request.FILES,instance=projectObj)
        if form.is_valid():
            form.save()
            return redirect("projects")

    context = {"form":form}
    return render(request, "projects/project_form.html",context)


@login_required(login_url="login") 
def deleteProject (request , pk):
    projectObj = Project.objects.get(id=pk)
    if request.method == "POST":
        projectObj.delete()
        return redirect("projects")
    context = {"object":projectObj}
    return render(request, "projects/delete_template.html",context)