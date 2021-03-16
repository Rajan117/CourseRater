from django.urls import path

from CourseRate import views

app_name = 'CourseRate'

urlpatterns = [
    path('home/', views.home, name='home'),
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('add_university/', views.add_university, name='add_university'),
]
