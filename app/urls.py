from django.urls import path
from . import views
from . views import *
from django.contrib.sitemaps.views import sitemap  
from .sitemaps import BlogSitemap, StaticViewSitemap

sitemaps = {
    "blog": BlogSitemap(),
    "static": StaticViewSitemap(),
}
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
    path('django', views.django_doc, name='django'),
    path('django-introduction', views.django_introduction, name='django_introduction'),
    path('django-projects/', views.django_projects, name='django_projects'),
    path('django-projects/<str:project_name>/', views.project_detail, name='project_detail'),
    path('web-development-basic/', views.web_development_basic, name='web_development_basic'),
    path('flask/', views.flask, name='flask'),
    path('python/', views.python, name='python'),
    path('database/', views.database, name='database'),
    path('git-github-basic/', views.git_github_basic, name='git_github_basic'),
    path("programming-help/python-programming-assignment-help/", python_help, name="python_help"),
    path("sitemap.xml", sitemap, {"sitemaps": sitemaps}, name="sitemap"),
    path("blogs/", blogs, name="blogs"),
    path("blog/<str:slug>/", blog_view, name="blog_view"),
    

    
]
