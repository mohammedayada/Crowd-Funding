from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Donation, Project
# Create your views here.

#Add donation
@login_required
def add_donation(request, pk):
    # pk for project to retrive project
    if request.POST:
        project = Project.objects.filter(pk=pk).first()
        donation = Donation.objects.create(project=project, user=request.user, value=request.POST['donation'])
        return render(request, 'home.html', {'msg': "Donation added successfully"})

    return render(request, 'home.html', {'msg': "can't added donation"})
