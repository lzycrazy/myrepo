from multiprocessing import context
from django.shortcuts import render,redirect
# from django.contrib.auth.models import User
# from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from. models import Contact,Post,Departmentt,Team,Appointment,Carrier,Job,Feedback,gallary,Caraousel
from django.conf import settings
from django.core.mail import send_mail

# Create your views here.
def index(request):
    cara=Caraousel.objects.all
    feedback=Feedback.objects.all
    department=Departmentt.objects.all()
    team=Team.objects.order_by('-slug')[0:7]
    post=Post.objects.order_by('-date')[0:3]
    gallery=gallary.objects.order_by('name')[0:4]
    
    context={
        'post':post,
        'department':department,
        'team':team,
        'feedback':feedback,
        'gallery':gallery,
        'cara':cara
    }
    return render(request,'index.html',context)

def about(request):
    department=Departmentt.objects.all()
    team=Team.objects.all
    context={
        'team':team,
        'department':department,
    }
    return render(request,'about.html',context)


def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        desc = request.POST['desc']

        contact = Contact(name=name,email=email,phone=phone,desc=desc)
        contact.save()
        messages.success(request, f'Your Message has been send.')
    context = {'contact':'active'}    

    return render(request,'contact.html', context)


def appointment(request):
    department=Departmentt.objects.all
    team=Team.objects.all

    context={
        'department':department,
        'team':team
    }
    if request.method=='POST': 
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        department=request.POST['department']
        doctor_name=request.POST['doctor_name']
        date=request.POST['date']
        msg=request.POST['msg']
        
        
        appointment=Appointment(name=name,email=email,phone=phone,department=department,doctor_name=doctor_name,date=date,msg=msg)
        appointment.save()
        messages.info(request,"Book Appointment Successfully")
        return redirect('/')
        
        # subject=name
        # message=msg
        # email_from=settings.EMAIL_HOST_USER
        # try:
        #     send_mail(subject,message,email_from ,['poojachauhan2102@gmail.com'])
           
        
        # except Exception as e:
        #     return redirect("appointment")
    return render(request,'appointment.html',context)

def gallery(request):
    gallery=gallary.objects.all
    team=Team.objects.all
    department=Departmentt.objects.all()
    context={
        'team':team,
        'department':department,
        'gallery':gallery
        
    }
    return render(request,'gallery.html',context)

def doctor(request):
    department=Departmentt.objects.all()
    team=Team.objects.all
    context={
        'team':team,
        'department':department,
    }
    return render(request,'doctor.html',context)

def job(request):
    jobs=Job.objects.all
    context={
        'jobs':jobs
    }


    return render(request,'job.html',context)

def carrier(request):
    department=Departmentt.objects.all()
    
    context={
        
        'department':department,
    }
    if request.method=='POST': 
        carrier=request.POST.get('carrier','')
        name=request.POST.get('name','')
        email=request.POST.get('email','')
        gender=request.POST.get('gender','')
        phone=request.POST.get('phone','')
        address=request.POST.get('address','')
        exp=request.POST.get('exp','')
        resume=request.POST.get('resume','')
        education=request.POST.get('education','')
        skill=request.POST.get('skill','')
        
        
        carrier=Carrier(carrier=carrier,name=name,email=email,gender=gender,phone=phone,address=address,exp=exp,resume=resume,education=education,skill=skill)
        carrier.save()
        messages.info(request,"Successfully Submiited")
        return redirect('/')
    return render(request,'carrier.html',context)


def doctor_details(request,slug):
    department=Departmentt.objects.all()
    
    
    team=Team.objects.filter(slug=slug)
    context={
        'team':team,
        'department':department,
    }
    return render(request,'doctor_detail.html',context)

def pricing(request):
    department=Departmentt.objects.all()
    
    context={
        
        'department':department,
    }
    return render(request,'pricing.html',context)

def project_details(request):
    
    return render(request,'project_details.html')


def services(request):
    department=Departmentt.objects.all()
    
    context={
        
        'department':department,
    }
    return render(request,'services.html',context)

def blog(request):
    department=Departmentt.objects.all()
    post=Post.objects.all
    
    team=Team.objects.all
   
    context={
        'post':post,
        'department':department,
        'team':team
    }
    return render(request,'blog.html',context)

def post(request,slug):
    department=Departmentt.objects.all()
    allpost=Post.objects.all
    post=Post.objects.filter(slug=slug)
    context={
        'post':post,
        'allpost':allpost,
        'department':department,
    }
    
    return render(request,'post.html',context)

def department(request,slug):
    department=Departmentt.objects.all()
    departments=Departmentt.objects.filter(slug=slug)
    
    context={
        
        'departments':departments,
        'department':department,
    }
    return render(request,'department.html',context)

def search(request):
    department=Departmentt.objects.all()
    
   
    query=request.GET['query']
    post=Post.objects.filter(title__icontains=query)
    # post=Post.objects.filter(desc__icontains=query)
    # post=Post.objects.filter(name__icontains=query)
    
    
    # post=Post.objects.filter(date__icontains=query)

    context={
        'post':post,
        'department':department,
    }
    return render(request,'search.html',context)


def time_table(request):
    department=Departmentt.objects.all()
    
    context={
        
        'department':department,
    }
    return render(request,'time_table.html',context)

def userlogin(request):
    department=Departmentt.objects.all()
    
    context={
        
        'department':department,
    }
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        

        user=authenticate(username=username,password=password)
        
        if user is not None:
            login(request, user)
            
            messages.success(request,'Successfully logged In')
            return redirect("/")

        else:
            messages.error(request,'User not Signup')
            return redirect('login') 

        

    return render(request,'login.html',context)
    
    
def handlelogout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('/')



def registration(request):
    department=Departmentt.objects.all()
    
    context={
        
        'department':department,
    }
    if request.method=="POST":
        username=request.POST.get('username')
        
        email=request.POST.get('email')
        pass1=request.POST.get('pass1')
        pass2=request.POST.get('pass2')

        # if User.objects.filter(name=name).exists():
        #     messages.info(request,"name already taken")
        #     return redirect("signup")
        
        if User.objects.filter(email=email).exists():
            messages.info(request,"Email already taken")
            return redirect("registration")


        # if len(username)>10:
        #     messages.error(request,"Username must be under 10 character")
        #     return redirect("signup")

        if not username.isalnum():
            messages.error(request,"Username should only contain letters and numbers")
            return redirect("registration")
        
        if pass1 != pass2:
            messages.error(request,"Password do not matched")
            return redirect("registration")

        
        myuser=User.objects.create_user(username,email,pass1)
        
        myuser.save()

        
        messages.success(request,"User Created")
        return redirect("/")
        
    else:

        
        return render(request,'registration.html',context)
    
    

