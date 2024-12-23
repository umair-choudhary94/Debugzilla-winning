from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('student/dashboard/', views.student_dashboard, name='student_dashboard'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('logout/', views.logout_view, name='logout'),
    path('django-web-development/', views.django_roadmap, name='django_roadmap'),  # New URL pattern
    path('enroll/', views.enroll_view, name='enroll'),
    
]
