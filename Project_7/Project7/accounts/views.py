from django.shortcuts import render,reverse,get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from .forms import Register_form, Login_form, More_User_Details_Form, Edit_Profile_Form, Edit_Password_Form
from .models import More_User_Details



def home_view(request):
    return render(request, 'home.html')


def register_view(request):
    if request.method == 'POST':
        form = Register_form(data=request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.set_password(form.password)
            form.save()
            return HttpResponseRedirect(reverse('home'))

    else:
        form = Register_form()
    return render(request, 'accounts/register.html', {"form":form})


def login_view(request):
    if request.method=='POST':
        form = Login_form(data=request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')

        if form.is_valid():
            user = authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect(reverse('home'))

    else:
        form = Login_form()
    return render(request, 'accounts/login.html', {'form':form})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))


def profile_view(request):
    user = request.user
    if request.method == 'POST':
        form = More_User_Details_Form(data=request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.relation = user
            form.save()

            if 'avatar' in request.FILES:
                form.avatar = request.FILES['avatar']
                form.save()


            return HttpResponseRedirect(reverse('home'))

    else:
        form = More_User_Details_Form()

    return render(request, 'accounts/profile.html', {'person':user, 'form':form})



def edit_profile_view(request):                                           # https://stackoverflow.com/questions/26651688/django-integrity-error-unique-constraint-failed-user-profile-user-id
    user = request.user                                                   # How I was able to change the users.more_user_details details.
    try:
        profile = request.user.more_user_details                          # I found the user first, then again I put the users 'more_user_details' object into a variable called 'profile'
    except More_User_Details.DoesNotExist:                                # If you look at the else clause at the bottom, I used the captured object and put it into the more_user_details_form.
        profile = More_User_Details(relation=user)                        # So now, we have passed the user we want to the form, thats the logged in user, and we have passed in the extra details we wanted into the other form.
                                                                          # We've essentially, captured both objects.

    if request.method== 'POST':
        print("yes past post")
        form = Edit_Profile_Form(data=request.POST, instance=request.user)     # Please pass the data to this form2, and also this is the user we want these details to give to, basically the user that is already logged in.
        form2 = More_User_Details_Form(data=request.POST, instance=profile)
        if form.is_valid() and form2.is_valid():
            form = form.save(commit=False)                                     # Save the first form
            form.set_password(form.password)
            form.save()

            form2 = form2.save(commit=False)                                   # Then save the second form but dont commit the change
            form2.user = user

            if 'avatar' in request.FILES:
                form2.avatar = request.FILES['avatar']                         # Check for an image in the data from form2
                form2.save()

            update_session_auth_hash(request, user=request.user)

            if user.is_active:
                print('Yes active')
                return redirect('home')

    else:
        form = Edit_Profile_Form(instance=request.user)
        form2 = More_User_Details_Form(instance=profile)
    return render(request, 'accounts/edit_profile.html', {'form':form, 'form2':form2})



# *********************************************************************************************************************************************************
# def edit_profile_view(request):
#     user = request.user
#     if request.method== 'POST':
#         form = Edit_Profile_Form(data=request.POST, instance=request.user)
#         form2 = More_User_Details_Form(data=request.POST)
#         if form.is_valid() and form2.is_valid():
#             form = form.save(commit=False)                                       # This was my old method, but it didnt work, so I used the method above
#             form.set_password(form.password)                                     # https://stackoverflow.com/questions/4822724/check-password-from-a-user-again
#             form.save()
#
#             form2 = form2.save(commit=False)
#             form2.user = user
#
#
#             if 'avatar' in request.FILES:
#                 form2.avatar = request.FILES['avatar']
#                 form2.save()
#
#             update_session_auth_hash(request, user=request.user)
#
#             if user.is_active:
#                 print('Yes active')
#                 return redirect('home')
#
#     else:
#         form = Edit_Profile_Form(instance=request.user)
#         form2 = More_User_Details_Form()
#     return render(request, 'accounts/edit_profile.html', {'form':form, 'form2':form2})
#
# **********************************************************************************************************************************************************


def edit_password_view(request):
    if request.method == 'POST':
        form = Edit_Password_Form(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, user=request.user)
            return HttpResponseRedirect(reverse('home'))


    else:
        form = Edit_Password_Form(user=request.user)
    return render(request, 'accounts/edit_password.html', {'form':form})



























