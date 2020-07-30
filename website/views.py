from django.shortcuts import render
from datatable.models import datatables
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def index(request):
    if request.method=='POST':
        if request.POST.get('name') and request.POST.get('email') and request.POST.get('phone') and request.POST.get('noemp'):
            saverecord=datatables()
            saverecord.name=request.POST.get('name')
            saverecord.email=request.POST.get('email')
            saverecord.phone=request.POST.get('phone')
            saverecord.noemp=request.POST.get('noemp') 
                        
            sending mail
            email_from=settings.EMAIL_HOST_USER
            email_to=[saverecord.email,]
            content='Hi '+saverecord.name
            send_mail(
                'Karshakasahai',
                content,
                email_from,
                email_to)



            saverecord.save()
            messages.success(request,"Record successfully entered")
            return render(request,'submit.html')
        else:
            return render(request,'index.html')
    else:
         return render(request,'index.html')
