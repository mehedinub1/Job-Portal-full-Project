from django.shortcuts import render,redirect

from myApp.models import *
from django.contrib.auth import authenticate,login,logout
from django.db.models import Q
from django.contrib.auth.decorators import login_required


def signupPage(request):
    
    if request.method=='POST':
        
        username=request.POST.get("username")
        email=request.POST.get("email")
        password=request.POST.get("password")
        Confirm_password=request.POST.get("Confirm_password")
        user_type=request.POST.get("user_type")
        Profile_Pic=request.FILES.get("Profile_Pic")
    
        
        if password==Confirm_password:
            
            
            user=customUser.objects.create_user(
                username=username,
                email=email,
                password=password,
                user_type=user_type,
                Profile_Pic=Profile_Pic,
            )
            if user_type=='seeker':
                seekerProfileModel.objects.create(user=user)
                
            elif user_type=='recruiter':
                recruiterProfileModel.objects.create(user=user)
            
            return redirect("signInPage")
            
    return render(request,"signupPage.html")


def signInPage(request):
    if request.method == 'POST':
        
        user_name=request.POST.get("username")
        pass_word=request.POST.get("password")

        try:
            user = authenticate(request, username=user_name, password=pass_word)

            if user is not None:
                login(request, user)
                return redirect('homePage') 
            else:
                return redirect('signInPage')

        except customUser.DoesNotExist:
            return redirect('signInPage')

    return render(request, 'signInPage.html')

@login_required
def homePage(request):

    total_job=JobModel.objects.all().count()

    total_user=customUser.objects.all().count()

    total_applications=jobApplyModel.objects.all().count()

    context={
        'total_job':total_job,
        'total_user':total_user,
        'total_applications':total_applications
    }
    
    
    return render(request,"homePage.html",context)


def logoutPage(request):
    
    logout(request)
    
    return redirect('signInPage')

@login_required
def profilePage(request):
    
    return render(request,"profilePage.html")



def logoutPage(request):
    
    logout(request)
    
    return redirect('signInPage')

@login_required
def profilePage(request):
    
    return render(request,"profilePage.html")


def addjob(request):
    current_user=request.user
    if current_user.user_type == "recruiter":
        if request.method=="POST":
            jobs=JobModel()
            jobs.user=current_user
            jobs.job_title=request.POST.get("job_title")
            jobs.category=request.POST.get("category")
            jobs.skill=request.POST.get("skill")
            jobs.vacancy=request.POST.get("vacancy")
            jobs.description=request.POST.get("description")
            jobs.job_Pic=request.FILES.get("job_Pic")
            
            jobs.save()
            
            
            return redirect("jobfeed")
        return render(request,'addjob.html')
 


def createjob(request):
    current_user=request.user
    jobs=JobModel.objects.filter(user=current_user)

    text={
        "jobs":jobs
    }
    
    return render(request,"createjob.html",text)

def jobfeed(request):
    jobs=JobModel.objects.all()

    text={
        "jobs":jobs
    }
    
    return render(request,"jobfeed.html",text)


def deletejob(request,id):
    jobs=JobModel.objects.filter(id=id)
    jobs.delete()


    
    return redirect("createjob")


def editjob(request,id):
    
    
    jobs=JobModel.objects.get(id=id)
    
    current_user=request.user
    if current_user.user_type == "recruiter":
        if request.method=="POST":
            jobs=JobModel()
            jobs.id=request.POST.get("id")
            jobs.user=current_user
            jobs.job_title=request.POST.get("job_title")
            jobs.vacancy=request.POST.get("vacancy")
            jobs.skill=request.POST.get("skill")
            jobs.category=request.POST.get("category")
            jobs.description=request.POST.get("description")
            jobs.job_Pic=request.FILES.get("job_Pic")
            jobs.save()
            
            
            return redirect("createjob")
     
    
    context={
        "jobs":jobs
    }
    
    return render(request,"editjob.html",context)



def viewjob(request,id):
    jobs=JobModel.objects.filter(id=id)
    text={
        "jobs":jobs
    }
    return render(request,"viewjob.html",text)

from django.shortcuts import render,redirect

from myApp.models import *
from django.contrib.auth import authenticate,login,logout
from django.db.models import Q
from django.contrib.auth.decorators import login_required


def signupPage(request):
    
    if request.method=='POST':
        
        username=request.POST.get("username")
        email=request.POST.get("email")
        password=request.POST.get("password")
        Confirm_password=request.POST.get("Confirm_password")
        user_type=request.POST.get("user_type")
        Profile_Pic=request.FILES.get("Profile_Pic")
        contact_no=request.POST.get("contact_no")
    
        
        if password==Confirm_password:
            
            
            user=customUser.objects.create_user(
                username=username,
                email=email,
                password=password,
                user_type=user_type,
                Profile_Pic=Profile_Pic,
                contact_no=contact_no,
            )
            if user_type=='seeker':
                seekerProfileModel.objects.create(user=user)
                
            elif user_type=='recruiter':
                recruiterProfileModel.objects.create(user=user)
            
            return redirect("signInPage")
            
    return render(request,"signupPage.html")


def signInPage(request):
    if request.method == 'POST':
        
        user_name=request.POST.get("username")
        pass_word=request.POST.get("password")

        try:
            user = authenticate(request, username=user_name, password=pass_word)

            if user is not None:
                login(request, user)
                return redirect('homePage') 
            else:
                return redirect('signInPage')

        except customUser.DoesNotExist:
            return redirect('signInPage')

    return render(request, 'signInPage.html')


def logoutPage(request):
    
    logout(request)
    
    return redirect('signInPage')

@login_required
def profilePage(request):
    
    return render(request,"profilePage.html")



def addJobPage(request):

    current_user=request.user
    if current_user.user_type == "recruiter":
        if request.method=="POST":
            jobs=JobModel()
            jobs.user=current_user
            jobs.job_title=request.POST.get("job_title")
            jobs.vacancy=request.POST.get("vacancy")
            jobs.skills=request.POST.get("skills")
            jobs.category=request.POST.get("category")
            jobs.description=request.POST.get("description")
            jobs.job_Pic=request.FILES.get("job_Pic")
            
            jobs.save()
           
            return redirect("jobFeed")
    
    return render(request,"addJobPage.html")

def createdJobPage(request):

    current_user=request.user
    jobs=JobModel.objects.filter()

    context= {
        'jobs': jobs
    }
    
    return render(request,"createdJobPage.html",context)

def jobFeed(request):

    current_user=request.user
    jobs=JobModel.objects.all()

    context= {
        'jobs': jobs
    }
    
    return render(request,"jobFeed.html",context)

def deleteJob(request,job_id):

    jobs=JobModel.objects.filter(id=job_id)
    jobs.delete()

    
    return redirect("createdJobPage")


def viewJOb(request,job_id):

    jobs=JobModel.objects.filter(id=job_id)

    context= {
        'jobs': jobs
    }
    
    
    return render(request,"viewJOb.html",context)

def editJob(request,job_id):

    jobs=JobModel.objects.get(id=job_id)

    context= {
        'jobs': jobs
    }

    current_user=request.user
    if current_user.user_type == "recruiter":
        if request.method=="POST":
            jobs=JobModel()
            jobs.id=request.POST.get("job_id")
            jobs.user=current_user
            jobs.job_title=request.POST.get("job_title")
            jobs.vacancy=request.POST.get("vacancy")
            jobs.skills=request.POST.get("skills")
            jobs.category=request.POST.get("category")
            jobs.description=request.POST.get("description")
            jobs.job_Pic=request.FILES.get("job_Pic")
            
            jobs.save()
           
            return redirect("createdJobPage")
    
    return render(request,"editJob.html",context)


def applyJob(request,job_id):


    jobs=JobModel.objects.get(id=job_id)

    context= {
        'jobs': jobs
    }

    current_user=request.user
    
    if current_user.user_type == 'seeker':
        
        
        if request.method=='POST':
            
            Resume=request.FILES.get("Resume")
            Cover=request.POST.get("Cover")
            Skills=request.POST.get("Skills")
            job_Pic=request.FILES.get("job_Pic")
            
            apply=jobApplyModel(
                user=current_user,
                job=jobs,
                Resume=Resume,
                Cover=Cover,
                Skills=Skills,
                job_Pic=job_Pic,
                
            )
            apply.save()
            return redirect("jobFeed")
    
    
    return render(request,"applyJob.html",context)

def searchJob(request):
    
    query = request.GET.get('query')
    
    if query:
        
        jobs = JobModel.objects.filter(Q(job_title=query) 
                                       |Q(skills=query) 
                                       |Q(category=query) 
                                       )
    
    else:
        jobs = JobModel.objects.none()
        
    context={
        'jobs':jobs,
        'query':query
    }
    
    return render(request,"searchJob.html",context)

def skillMatchingPage(request):
    
    user=request.user
    
    mySkill=user.seekerProfile.skills
    jobs=JobModel.objects.filter(skills=mySkill)
    context={
        'jobs':jobs
    }
    print(mySkill)
    
    return render(request,"skillMatchingPage.html",context)

def appliedJob(request):
    applied_jobs = jobApplyModel.objects.filter(user=request.user)  # Get applied jobs for the logged-in user
    return render(request, 'appliedJob.html', {'applied_jobs': applied_jobs})




def editProfile(request): 
    current_user = request.user 
 
    if request.method == 'POST': 

        if request.FILES.get('Profile_Pic'):
            current_user.Profile_Pic = request.FILES.get('Profile_Pic')
             
        current_user.save() 
        return redirect('profilePage')
 
       
 
      
 
    return render(request,"editProfile.html")
