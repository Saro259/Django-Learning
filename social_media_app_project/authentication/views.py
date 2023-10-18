from django.shortcuts import render, redirect
from django.http import HttpResponse
from authentication.models import User
from django.contrib.auth.models import auth 
from media_app.models import Profile
# Create your views here.
def sign_up(request):
    page_name = "sign_up.html"
    if request.method=="GET":
        #print(request.user)
        #print(request.user.is_authenticated)
        return render(request, page_name)
    else:
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        if email is None:
            return render(request, page_name, context={"error":True, "error_message":"Email is Required"})
        if username is None:
            return render(request, page_name, context={"error":True, "error_message":"Username is required"})
        if password is None:
            return render(request, page_name, context={"error":True, "error_message":"Password is required"})
        if User.objects.filter(username=username).exists():
            return render(request, page_name, context={"error":True, "error_message":"Username already exists"})
        if User.objects.filter(email=email).exists():
            return render(request, page_name, context={"error":True, "error_message":"Email already exists"})
        User.objects.create_user(username=username,email=email,password=password)  # To create the user after all the above validations 
        user = auth.authenticate(username=username, email=email, password=password) # for authentication purpose, which gets true at base.html
        Profile.objects.get_or_create(user=user) # if the user exists it will do a get operation, else a create operation
        auth.login(request,user)
        return render(request, page_name)

def sign_in(request):
    page_name = "sign_in.html"
    if request.method=="GET":
        return render(request, page_name)
    else:
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if not user:
            return render(request, page_name, context={"error":True, "error_message":"User does not exists"}) # To create the user after all the above validations 
        Profile.objects.get_or_create(user=user) # if the user exists it will do a get operation, else a create operation
        auth.login(request,user)
        return render(request, page_name)
        
def sign_out(request):
    auth.logout(request)
    return redirect('sign_in')

