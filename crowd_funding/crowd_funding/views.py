from django.shortcuts import render
from project.models import Project, Category


def home(request):
    # All Category
    categories = Category.objects.all().order_by('pk')[:5]

    # top rated
    toprated5_projects = Project.objects.all().order_by('-avg_rate', '-pk')[:5]
    # to get featured project
    featured4_projects = Project.objects.filter(featured=True).order_by('-pk')[1:5]
    # to get featured first project
    featured_first_project = Project.objects.filter(featured=True).order_by('-pk').first()

    # to get latest 5 project
    latest5_projects = Project.objects.all().order_by('-pk')[:5]
    context = {
        'categories': categories,
        'latest5_projects': latest5_projects,
        'featured4_projects': featured4_projects,
        'featured_first_project': featured_first_project,
        'toprated5_projects': toprated5_projects,
    }
    return render(request, 'index.html', context)
