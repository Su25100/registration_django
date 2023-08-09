from django.shortcuts import render,HttpResponse,redirect
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login

# Create your views here.

class  HomeView(View):
    def get(self,request):
         
        return render(request,"templates/home.html")
    

class LoginView(View):
    def get(self, request):
      return render(request, "login.html")
    def post(self,request):
        if request.method=="POST":
           username=request.POST.get('username')
           password1=request.POST.get('password')
           user=authenticate(request,username=username,password=password1)
           if user is not None:
               login(request,user)
               return redirect('home')
           else:
               return HttpResponse("Username or Password is incorrect!!")
                
        return render(request,"templates/login.html")
    

class SignupView(View):
    def get(self, request):
       return render(request, "signup.html")

    def post(self,request):
        if request.method=="POST":
           username=request.POST.get('username')
           email=request.POST.get('email')
           password=request.POST.get('password')
           password1=request.POST.get('password1')

    
           my_user =User.objects.create(username=username, password=password , email=email)
           my_user.save()
           return HttpResponse("user has been created Successfully!!")
           
        return render(request,"templates/signup.html")   
    
      
    
    
