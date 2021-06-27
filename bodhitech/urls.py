from django.contrib import admin
from bodhitech import views as bview 
from django.urls import path

urlpatterns = [
    
    path('mypage',bview.lname,name="pri"),
    #path('mypage_1',bview.homepage,name="prit"),
    path('',bview.bodhitech_homepage,name="p"),
    #path('test',bview.homepageTest,name="hom"),
    path('contact',bview.web_contact,name="pp"),
    path('java',bview.java,name="java"),
    path('python',bview.python,name="python"),
    path('django',bview.django,name="django"),
    path('web_fundamental',bview.web_1,name="web_1"),
    path('web_application',bview.web_application,name="web"),
    path('mobile_application',bview.mobile_application,name="mobile"),
   

]



