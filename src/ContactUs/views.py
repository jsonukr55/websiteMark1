from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
from django.core.mail import send_mail
from ContactUs.forms import ContactForm 


def contact_us(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            return HttpResponse('Thanks for contacting us!')
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})