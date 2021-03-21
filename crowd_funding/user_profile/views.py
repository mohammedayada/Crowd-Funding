from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .forms import Register_form
from django.contrib.auth.models import User
from .models import user_profile
from django.db.models import Q
# Create your views here.


#login function
def user_login(request):
    # when request POST
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            context = {
                'msg': "login successfully"
            }
        else:
            context = {
                'msg': "login failed"
            }
        return render(request, 'home.html', context)
    # when request GET
    else:
        return render(request, 'home.html')


#register function
def user_register(request):
    if request.POST:
        data = request.POST
        print(request.FILES['img'])
        form = Register_form(request.POST, request.FILES)
        if form.is_valid():
            # create new user
            valid_user = User.objects.filter(Q(username=data['username']) | Q(email=data['email']))
            if len(valid_user) > 0:
                print(valid_user)
                return render(request, "user_profile/register.html", {'form': form,
                                                                      'msg': "enter valid username or email"})
            user = User.objects.create_user(username=data['username'],
                                            first_name=data['first_name'],
                                            last_name=data['last_name'],
                                            email=data['email'],
                                            password=data['password'],
                                            )
            # create new profile

            profile = user_profile.objects.create(user=user,
                                                  phone=data['phone'],
                                                  facebook_link=data['facebook_link'],
                                                  country=data['country'],
                                                  img=request.FILES['img'],
                                                  )
            if data['birth_date'] is not None:
                profile.birth_date = data['birth_date']
            return render(request, "home.html", {'msg': "user register successfully"})
        else:
            # redirect to the same page
            return render(request, "user_profile/register.html", {'form': form})
    else:
        form = Register_form()
        return render(request, "user_profile/register.html", {'form': form})


