from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .forms import Project_form, Category
from tag.models import Tag, proiect_tag
from .models import Project, Project_imgs
from comment.models import Comment
# Create your views here.




@login_required
def add_project(request):
    if (request.POST):
        form = Project_form(request.POST, request.FILES)
        if form.is_valid():
            data = request.POST
            category = Category.objects.filter(pk=int(data['category'])).first()
            project = Project.objects.create(
                                             user=request.user,
                                             title=data['title'],
                                             category=category,
                                             details=data['details'],
                                             target=data['target'],
                                             start_date=data['start_date'],
                                             end_date=data['end_date'],
                                             )

            tags = data['tages'].split(',')
            for tag in tags:
                new = Tag.objects.filter(name=tag).first()
                if new is None:
                    new = Tag.objects.create(name=tag,
                                             user=request.user
                                             )
                proiect_tag.objects.create(tag=new,
                                           project=project
                                           )

            Project_imgs.objects.create(img=request.FILES['projectImgs'],
                                        project=project
                                        )

            return render(request, 'home.html', {'msg': "Project created successfully"})
        else:
            return render(request, 'project/add_project.html', {'form': form,
                                                                'msg': "Invalid data"})


    else:
        form = Project_form()
        return render(request, 'project/add_project.html', {'form': form})



def show_project(request,pk):
    project = Project.objects.filter(pk=pk).first()
    project_tags = proiect_tag.objects.filter(project=project)
    comment = Comment.objects.filter(project=project)
    if project:
        return render(request, 'project/show_project.html', {'project': project,
                                                             'tags': project_tags,
                                                             'comments': comment})
    else:
        return render(request, 'home.html', {'msg': "Project not found"})
