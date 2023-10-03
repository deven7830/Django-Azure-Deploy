from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views import View
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.http import JsonResponse

# Create your views here.

class SignUpView(View):
    def get(self, request):
        form=UserCreationForm()
        context={'form':form}
        template_name='authapp/signup.html'
        return render(request,template_name,context)
    def post(self,request):
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('signin_url')
        return JsonResponse({"msg":"Password Mismatched"})

class SignInView(View):
    def get(self,request):
        context={}
        template_name='authapp/signin.html'
        return render(request,template_name,context)

    def post(self,request):
        un=request.POST.get("un")
        pw=request.POST.get("pw")

        user=authenticate(username=un, password=pw)

        if user is not None:
            login(request,user)
            return redirect('display_url')
        return HttpResponse('<h2>DATA INVALID </h2>')

class SignOutView(View):
    def get(self,request):
        logout(request)
        return redirect('signin_url')

