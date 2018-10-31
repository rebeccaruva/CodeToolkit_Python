from django.urls import path

from . import views #make this file talk to the views.py file

urlpatterns = [
    # path('', views.homepageview, name = 'home'), #in views.py find homepageview function
    path('', views.HomePageView.as_view(), name = 'home'), #use template view instead
    # path('about/', views.aboutpageview, name = 'about'),
    path('about/', views.AboutPageView.as_view(), name = 'about'),
    path('music/', views.MusicPageView.as_view(), name = 'music'),
    ]
