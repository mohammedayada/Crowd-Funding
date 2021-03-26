from django.shortcuts import render
from project.models import Project, Category


def home(request):
    # All Category
    categories = Category.objects.all()

    # top rated
    # to get featured project
    featured4_projects = Project.objects.filter(featured=True).order_by('-pk')[:5]
    # to get featured first project
    featured_first_project = None
    if featured4_projects:
        featured4_projects = list(featured4_projects)
        featured_first_project = featured4_projects[0]
        featured4_projects.pop(0)

    # to get latest 5 project
    latest5_projects = Project.objects.all().order_by('-pk')[:5]
    context = {
        'categories': categories,
        'latest5_projects': latest5_projects,
        'featured4_projects': featured4_projects,
        'featured_first_project': featured_first_project,
    }
    return render(request, 'home.html', context)
