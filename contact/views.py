from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import ContactForm
from django.core.mail import EmailMessage

# Create your views here.
def contact(request):
    #print("tipo de peticion", request.method)
    contactForm=ContactForm()
    if request.method == "POST":
        contactForm=ContactForm(data=request.POST)
        if contactForm.is_valid():
            firstname=request.POST.get('firstname','')
            lastname=request.POST.get('lastname','')
            email=request.POST.get('email','')
            nickname=request.POST.get('nickname','')
            commentary=request.POST.get('commentary','')    
            emailContact=EmailMessage(
                "Yami no game store: nuevo mensaje de contacto",
                "De {} {} <{}> {} \n\nComentarios:\n\n{}".format(firstname,lastname,email,nickname,commentary),
                "davidbra12345@gmail.com",
                ["correo-prueba@imbox.mailtrap.io"],
                reply_to=[email ]
            )
            try:
                emailContact.send() 
                return redirect(reverse('contact')+"?ok")
            except:
                return redirect(reverse('contact')+"?fail")      

           

            
    return render(request, "contact/contact.html", {'contactForm':contactForm})