from django.shortcuts import render
from .models import Project_b


def all_blogs(request):
    projects = Project_b.objects.all()
    return render(request, 'blog/all_blogs.html', {'projects': projects})
