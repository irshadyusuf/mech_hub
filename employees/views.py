from django.shortcuts import render

# Create your views here.
def login_fun(request):
    return render(request,'employees/login.html')