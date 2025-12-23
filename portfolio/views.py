from django.shortcuts import render
from portfolio.models import Project

def home(request):

    all_Projects = Project.objects.all()
    return render(request,'Main-Page.html',{'all_Projects':all_Projects})
# Create your views here.

def projectDetail(request,project_id):
    project = Project.objects.get(id=project_id)
    context = {'project':project}
    return render(request,'Project_Details.html',context)