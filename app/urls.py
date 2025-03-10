from django.urls import path
from . import views
from . views import *
urlpatterns = [
    path('', views.index, name='index'),
    path('student/dashboard/', views.student_dashboard, name='student_dashboard'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('logout/', views.logout_view, name='logout'),
    path('django-web-development/', views.django_roadmap, name='django_roadmap'),  # New URL pattern
    path('enroll/', views.enroll_view, name='enroll'),
    path('web-basics-course/', views.web_basics_course, name='web_basics_course'),
    path('privacy-policy/', views.privacy_policy, name='privacy_policy'),
    path('terms-and-conditions/', views.terms_and_conditions, name='terms_and_conditions'),
    path('django',views.django_doc),
    path('django-introduction',views.django_introduction),
    path('django-projects/',views.django_projects),
    path('django-projects/<str:project_name>/',views.project_detail),
    path('web-development-basic/', views.web_development_basic),
    path('flask/', views.flask),
    path('python/', views.python),
    path('database/', views.database),
    path('git-github-basic/', views.git_github_basic),



    path("blogs/", blogs, name="blogs"),
    path("blog/<str:slug>/", blog_view, name="blog_view"),
    path('ckeditor/upload/', upload_ckeditor_image, name='ckeditor_upload'),

    
]
