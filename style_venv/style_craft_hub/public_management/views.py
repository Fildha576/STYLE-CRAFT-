from django.shortcuts import render,redirect
from . forms import *
from django.contrib.auth import authenticate, login
from django.contrib import auth
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request,'index.html')
def about(request):
    return render(request,'about.html')

def Login(request):
    return render(request,'login.html')

def register(request):
    form = RegisterForm(request.POST,request.FILES)
    if request.method=='POST':
        if form.is_valid():
            
            try:
                email = form.cleaned_data["email"]
                Register.objects.get(email=email)
                
                return render(request,'login.html',{'form':form,'z':True})
            except Register.DoesNotExist:
                
                    Register.objects.create_user(
                        name = form.cleaned_data["name"],
                        email = form.cleaned_data["email"],
                        password = form.cleaned_data["password"],
                        username = form.cleaned_data["name"],
                        contact = form.cleaned_data["contact"],
                        address = form.cleaned_data["address"],
                        usertype = "2"
                        )
                    messages.success(request, f'Your Registration has been succesfull ! You can login ', extra_tags='user_reg')
                    return redirect('/Login')
    else:
        form = RegisterForm()
    return render(request,'register.html',{'form':form})


def t_register(request):
    form = TRegisterForm(request.POST,request.FILES)
    if request.method=='POST':
        if form.is_valid():
            
            try:
                email = form.cleaned_data["email"]
                Register.objects.get(email=email)
                redirect('/')
            except Register.DoesNotExist:
                
                    Register.objects.create_user(
                        name = form.cleaned_data["name"],
                        email = form.cleaned_data["email"],
                        password = form.cleaned_data["password"],
                        username = form.cleaned_data["name"],
                        contact = form.cleaned_data["contact"],
                        address = form.cleaned_data["address"],
                        usertype = "3",
                        license = form.cleaned_data["license"],
                        id_proof = form.cleaned_data["id_proof"],
                        location = form.cleaned_data["location"],
                        is_active = False
                        )
                    messages.success(request, f'Your Registration has been succesfull ! You can login only after approval from admin ', extra_tags='user_reg')
                    return redirect('/')
    else:
        form = TRegisterForm(request.POST,request.FILES)
    return render(request,'register.html',{'form':form})


def product_add(request):
    form = ProductForm(request.POST,request.FILES)
    if request.method=='POST':
        if form.is_valid():
            form.save()
            messages.success(request, f'Your Registration has been succesfull ! You can login only after approval from admin ', extra_tags='user_reg')
            return redirect('/')
    else:
        form = ProductForm(request.POST,request.FILES)
    return render(request,'product_add.html',{'form':form})



def doLogin(request):
    form = LoginForm()
    if request.method == "POST":
        user = authenticate(request,username=request.POST["username"],password=request.POST["password"] )
        print(user)
        if user is None:
            return render(request,'index.html',{'form':form,'k':True})   
        else:
            login(request, user)
            data = Register.objects.get(username=user)
            print(data)
            request.session['ut']=data.usertype
            data.usertype
            request.session['uid']=data.id
            data.usertype
            print(data.usertype)
            # messages.success(request, f'Login Successfull!! Welcome {data.username}', extra_tags='log')
            return redirect('/')
    else:
        form = LoginForm()
    return render(request,'login.html',{'form':form})


def doLogout(request):
    auth.logout(request)
    return redirect('/')



def view_users(request):
    a = Register.objects.filter(usertype=2)
    print(a)
   
    return render(request, 'view_users.html', {'a': a})

def view_approval(request):
    a = Register.objects.filter(usertype=3,is_active=0)
    print(a)
   
    return render(request, 'view_approval.html', {'a': a})


def appro(request,id):
    user=Register.objects.get(id=id)
    user.is_active=True
    user.save()
    return redirect('/view_tailor')

def reject(request,id):
    user=Register.objects.get(id=id)
    user.is_active=2
    user.save()
    return redirect('/view_tailor')



def view_tailor(request):
    a = Register.objects.filter(usertype=3,is_active=True)
    print(a)
    return render(request, 'view_tailor.html', {'a': a})
