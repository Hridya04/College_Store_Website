
from django.contrib import messages, auth
from django.contrib.auth.models import User



from django.shortcuts import render, redirect
from .forms import MyForm
# Create your views here.
def index2(request):
    return render(request,'index2.html')

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('newpage')
        else:
            messages.info (request,'invalid credentials')
            return redirect('login')
    return render(request,'login.html')

def register(request):
    if request.method=='POST':
        username=request.POST['username']
        password = request.POST['password']
        cpassword = request.POST['password1']
        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,'username taken')
                return redirect('register')

            else:
                user=User.objects.create_user(username=username,password=password,)
                user.save()
                print('user created')
                return redirect('login')
        else:
            messages .info (request,'password not matching')
            return redirect ('register')
        return redirect('/login')
    return render(request,'register.html')

def logout(request):
    auth.logout(request)
    return redirect('index2')

def newpage(request):
    return render(request,'newpage.html')




def form_page(request):
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():

            messages.success(request,'Request Confirmed')
            return redirect('form_page')
    else:
        form = MyForm()

    return render(request,'form.html',{'form': form})



