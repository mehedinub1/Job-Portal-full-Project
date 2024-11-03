from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from myProject.views import *

urlpatterns = [
    path("admin/", admin.site.urls),
    path('',signupPage,name="signupPage"),
    path("signInPage/", signInPage, name="signInPage"),
    path("homePage/", homePage, name="homePage"),
    path("logoutPage/", logoutPage, name="logoutPage"),
    path("ProfilePage/", profilePage, name="profilePage"),
    path("addJobPage/", addJobPage, name="addJobPage"),
    path("createdJobPage/", createdJobPage, name="createdJobPage"),

    path("deleteJob/<str:job_id>", deleteJob, name="deleteJob"),
    path("editJob/<str:job_id>", editJob, name="editJob"),
    path("viewJOb/<str:job_id>", viewJOb, name="viewJOb"),

    path("applyJob/<str:job_id>", applyJob, name="applyJob"),


    path("jobfeed/", jobFeed, name="jobFeed"),
    path('searchJob/', searchJob, name='searchJob'),
    path('appliedJob',appliedJob,name='appliedJob'),
    
    path("editProfile/", editProfile, name="editProfile"),
    

    path("skillMatchingPage/", skillMatchingPage, name="skillMatchingPage"),

    
    
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
