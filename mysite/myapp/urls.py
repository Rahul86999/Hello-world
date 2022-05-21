from django.urls import path, include
from .import views

urlpatterns = [
    path('', views.indexView, name='home'),
    path('studentcreate', views.studentView, name='student'),
    path('courseadd', views.courseView, name='student'),
    path('fee', views.feeView, name='student'),
    path('oauth/', include('social_django.urls', namespace='social')),
    path('home', views.Home, name='home'),
    path('logout/',views.logout, name='logout'),

]
