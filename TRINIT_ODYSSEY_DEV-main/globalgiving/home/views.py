from django.shortcuts import render,HttpResponse,redirect
from .models import *
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth.models import User,auth,Group
from django.contrib.auth import logout,login

# Create your views here.
def registerngo(request):
    if request.method=="POST":
        name= request.POST.get('name')
        email= request.POST.get('email')
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        confirmpassword = request.POST.get('confirmpassword')
        registerngo = ngo(name=name, email = email, phone = phone,password=password,confirmpassword=confirmpassword)
        if(password==confirmpassword):
            registerngo.save()
        else:
            messages.success(request, 'Passwords didnt match.')

    return render(request,'register-ngo.html')

def registerphil(request):
    if request.method=="POST":
        name= request.POST.get('name')
        email= request.POST.get('email')
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        confirmpassword = request.POST.get('confirmpassword')
        registerphil = phil(name=name, email = email, phone = phone,password=password,confirmpassword=confirmpassword)
        if(password==confirmpassword):
            registerphil.save()
        else:
            messages.success(request, 'Passwords didnt match')
            
        messages.success(request, 'Your Message has been.')

    return render(request,'register-phil.html')

# def signinphil(request):
#     return render(request,'sign-phil.html')

# def signinngo(request):
#     if request.method=="POST":
#         name = request.POST['name']
#         password = request.POST['password']
#         print(name,password)
#         user = authenticate(username=name, password=password)
#         if user is not None:
            
#             login(request,user)
#             return render(request,'ngohome')

#         else:
#             print(name,password)
#             messages.error(request,'invalid credentials')
            
#             return render(request,'sign-ngo')
    
    
    
def home(request):
    data={
        'title:'
    }
    return render(request,'home.html')

def land(request):
    return render (request,'land.html')



def logout_view(request):
    logout(request)
    return redirect("/land")

def signupn(request):
    username = request.POST['Username']
    email = request.POST['email']
    pass1 = request.POST['pass1']
    pass2 = request.POST['pass2']


    myuser = User.objects.create(username,email,pass1)
    myuser.save()

    messages.success(request,"your acc created le")

    return redirect('signin')

def rans(request):
    username = request.POST['username']
    email = request.POST['email']
    pass1 = request.POST['pass1']
    pass2 = request.POST['pass2']


    myuser = User.objects.create(username,email,pass1)
    myuser.save()

    messages.success(request,"your acc created le")

    return redirect('signin')

def SignupPage(request):
    if request.method =="POST":
        uname= request.POST.get('username')
        email= request.POST.get('email')
        pass1= request.POST.get('password1')
        pass2= request.POST.get('password2')

        print(uname,email,pass1,pass2)
        
        if pass1!=pass2:
            return HttpResponse("Your Passwords don't match")
        else:
            my_user = User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('login')
    return render(request,'signup.html')

def LoginPage(request):
    if request.method=="POST":
        username=request.POST.get('username')
        pass1 = request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('land')
        else:
            return HttpResponse("Username or Password is incorrect")
    
    return render(request,'login.html')

def ngohome(request):
    return render(request,'ngohome.html')
def philhome(request):
    return render(request,'philhome.html')

def ngoprof(request):
    if request.method == "POST":

        name =   request.POST.get('name')
        mission = request.POST.get('mission')
        history = request.POST.get('history')
        impact =  request.POST.get('impact')
        image =   request.POST.get('image')  
        ngoprof = Profile(name=name, mission=mission, history=history, impact=impact, image=image)
        ngoprof.save()
    return render(request,'ngoprof.html')


    

def ngodet(request):
    return render(request,'ngodet.html')

def ngodisplay(request):
    allUsers = Profile.objects.all()
    context = {'ngodisplay':allUsers}
    return render(request, 'ngodisplay.html',context)
def gotocon(request):
    return render(request,'contacts.html')
def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        number = request.POST.get('number')
        email = request.POST.get('email')
        message = request.POST.get('message')
        contact = Contact(name=name, email=email, number=number, message=message)
        contact.save()
        messages.success(request, 'Message sent.')
    return render(request,'contacts.html')