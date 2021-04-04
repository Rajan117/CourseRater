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
    path('myaccount/', views.account, name='account'),
    path('search-results/', views.search_results, name='search_results'),
    path('add_university/', views.add_university, name='add_university'),
    path('university/<slug:university_name_slug>/', views.show_university, name='show_university'),
    path('university/<slug:university_name_slug>/add_department/', views.add_department, name='add_department'),
    path('university/<slug:university_name_slug>/<slug:department_name_slug>/', views.show_department, name='show_department'),
    path('university/<slug:university_name_slug>/<slug:department_name_slug>/add_module/', views.add_module, name='add_module'),
    path('university/<slug:university_name_slug>/<slug:department_name_slug>/<slug:module_name_slug>/', views.show_module, name='show_module'),
    path('university/<slug:university_name_slug>/<slug:department_name_slug>/<slug:module_name_slug>/add_review/', views.add_review, name='add_review'),
    path('like_review/', views.LikeReview.as_view(), name='like_review'),
    path('dislike_review/', views.DislikeReview.as_view(), name='dislike_review'),
]
