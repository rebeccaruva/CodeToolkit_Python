from django.urls import path

from . import views #make this file talk to the views.py file

urlpatterns = [
    path('', views.BlogListView.as_view(), name = 'bloglist'), #use template view instead
    path('<int:pk>/', views.BlogDetailView.as_view(), name='blogdetail'),
    ]
