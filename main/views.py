"""
This script is used to create models for this app
Author: Peter Murimi
Date: 4/23/2020
"""
from django.shortcuts import render, redirect
from django.template.loader import get_template
from django.core.mail import EmailMessage
from .models import TopCarousel, OurServices, Team
from django.contrib import messages


def index(request):
    """
    Index Module
    """
    carousels = TopCarousel.objects.all()
    services = OurServices.objects.all()
    teams = Team.objects.all()

    context = {'carousels': carousels, 'services': services, 'teams': teams}

    if request.method == 'POST':
        message = request.POST['text']
        name = request.POST['name']
        email = request.POST['email']

        template = get_template('contact_form.txt')

        ourmesssages = {
            'contact_name' : name,
            'contact_email' : email,
            'contact_content' : message,
        }

        content = template.render(ourmesssages)

        email = EmailMessage(
            "New Mail for BYT",
            content,
            "Create web" + " ",
            ['peetsmore001@gmail.com'],
            headers={'Reply to' : email})
        
        email.send()
        
    return render(request, 'index.html', context=context)
