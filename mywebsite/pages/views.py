from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

# Create your views here.

class HomePageView(TemplateView): #class to use template
    template_name = 'home.html'

class AboutPageView(TemplateView): #class to use template
    template_name = 'about.html'

class MusicPageView(TemplateView): #class to use template
    template_name = 'music.html'

# def homepageview(request): #function instead of a class
#     return HttpResponse('''
#     <h2>Hi Bex!</h2>
#
#     <h3>welcome to your portal</h3>
#     ''');
#
# def aboutpageview(request):
#     return HttpResponse('''
#     <h2>about your day</h2>
#
#     <h3>today is wednesday, october 24</h3>
#     <h3>you are tired :(</h3>
#     ''')
