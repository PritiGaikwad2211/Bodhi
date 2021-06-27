from django.http import request
from django.shortcuts import render,redirect

from django.conf import settings as set 
from bodhitech.models import carousel,section,clients,about
from django.contrib import messages
from django.core.mail import BadHeaderError, send_mail
from socket import gaierror
from smtplib import SMTPAuthenticationError, SMTPDataError
from bodhitech.forms import ContactForm


btech=set.CNAME
car=carousel.objects.all()
sec=section.objects.all()
cli=clients.objects.all()
abo=about.objects.all()

# Create your views here.
def lname(request):
    return render(request,"layout/weblayout.html")




def homepage(request):
    return render(request,"layout/weblayout.html")


def homepageTest(request):
    return render(request,"webpages/test.html")

def java(request):
    return render(request,"webpages/java.html")

def django(request):
    return render(request,"webpages/django.html")

def python(request):
    return render(request,"webpages/python.html")

def web_1(request):
    return render(request,"webpages/fun_web.html")


def web_application(request):
    return render(request,"webpages/web_application.html")



def mobile_application(request):
    return render(request,"webpages/mobile_application.html")

    
def bodhitech_homepage(request):
    page_title="index"
    text="Priti"
    text1="Bodhi Technology"
    text2="Why you choose us?"
    text3="Our clients"
    text4="About Us"
    text5="Bodhi Technology"
    context={'title':page_title,
              'text':text,
              'text1':btech,
              'text2':text2,
              'text3':text3,
              'text4':text4,
              'text5':btech,
              'car':car,
              'sec':sec,
              'cli':cli,
              'abo':abo

               }
    return render(request,"webpages/index.html",context)
def web_contact(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            person_name=form.cleaned_data['name']
            subject = form.cleaned_data['subject']
            user_email = form.cleaned_data['emailid']
            message = form.cleaned_data['message']
            mobileno=form.cleaned_data['mobileno']
            message_send="\n Name : "+person_name+"\n Message : "+message+"\n User Email : "+user_email+"\n mobileno:"+mobileno
            from_email=set.EMAIL_HOST_USER
            try:
                send_mail(subject,message_send,from_email, ['pritigaikwad155@gmail.com'])
            except (BadHeaderError,gaierror,SMTPAuthenticationError,SMTPDataError):
                messages.error(request,"Check your Internet connection... Try again")
                return redirect('pp')
            messages.success(request,"Thank you for contacting school! Your form successfully submited")
            return redirect('pp')
            
    context = {
        'form': form,
        
        
    }        
    return render(request, "webpages/contact.html",context)


