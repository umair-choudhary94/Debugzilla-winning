from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from . models import *
from django.shortcuts import get_object_or_404
from .models import Blog

from django.db.models import Q
def index(request):
    return render(request, 'design2.html')


def student_dashboard(request):
    """
    View function for the student dashboard.
    """
    return render(request, 'student_dashboard.html')


def privacy_policy(request):
    """
    View function for the privacy policy page.
    """
    return render(request, 'privacy-policy.html')

def terms_and_conditions(request):
    """
    View function for the terms and conditions page.
    """
    return render(request, 'terms-conditions.html')

def enroll_view(request):
    """
    View function for the enroll page.
    """
    return render(request, 'enroll.html')

def web_basics_course(request):
    """
    View function for the web basics course page.
    """
    return render(request, 'web-basics-course.html')


def login_view(request):
    """
    View function for user login.
    """
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.info(request, f"You are now logged in as {username}.")
            return redirect('student_dashboard')
        else:
            messages.error(request, "Invalid username or password.")
    return render(request, 'login.html')

def signup_view(request):
    """
    View function for user signup.
    """
    if request.method == 'POST':
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        
        if password1 != password2:
            messages.error(request, "Passwords don't match.")
            return render(request, 'signup.html')
        
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return render(request, 'signup.html')
        
        user = User.objects.create_user(username=username, password=password1)
        login(request, user)
        messages.success(request, "Registration successful.")
        return redirect('student_dashboard')
    
    return render(request, 'signup.html')

def logout_view(request):
    """
    View function for user logout.
    """
    logout(request)
    messages.info(request, "You have successfully logged out.") 
    return redirect('login')

def django_roadmap(request):
    """
    View function for the roadmap page.
    """
    return render(request, 'django-roadmap.html')

def enroll_view(request):
    """
    View function for course enrollment.
    """
    if request.method == 'POST':
        course_id = request.POST.get('course_id')
            # Add logic to enroll the student in the course
        messages.success(request, "You have been enrolled in the course.")
        return redirect('student_dashboard')
        
    return render(request, 'enroll.html')

def web_basics_course(request):
    """
    View function for the web basics course page.
    """
    return render(request, 'web-basics-course.html')


def django_doc(request):
    return render(request,'django/base.html')

def django_introduction(request):
    return render(request,'django/django-intro.html')

def django_projects(request):
    Projects = Project.objects.all()
    count = Projects.count()
    context = {
        'Projects' : Projects,
        'count' : count
    }
    return render(request, 'Projects/django-projects.html', context)

def project_detail(request, project_name):
    project = Project.objects.get(project_name=project_name)
    return render(request, 'Projects/view-project.html', {'project': project})

def git_github_basic(request):
    return render(request,'git-github-basic.html')

def web_development_basic(request):
    return render(request,'web-development-basic.html')

def flask(request):
    return render(request,'flask.html')
def python(request):
    return render(request,'python.html')
def database(request):
    return render(request,'database.html')

def blogs(request):
    search_term = request.GET.get('search', '').strip() 
    categories = request.GET.getlist('category[]')  

    blogs = Blog.objects.all()  

    
    if search_term:
        blogs = blogs.filter(Q(title__icontains=search_term) | Q(content__icontains=search_term))


    if categories:
        blogs = blogs.filter(category__in=categories)  


    from django.core.paginator import Paginator
    paginator = Paginator(blogs, 40)  
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        "page_obj": page_obj,
        'has_next': page_obj.has_next(),
        'has_previous': page_obj.has_previous(),
        'num_pages': paginator.num_pages,
        "blogs_recent": Blog.objects.order_by('-publication_datetime')[:5],
        'search_term': search_term,
        'selected_categories': categories,  
    }
    return render(request, 'blog.html', context)
    

def blog_view(request, slug):
    blog = get_object_or_404(Blog, slug=slug)
    context = {
        "blogs_recent": Blog.objects.order_by('-publication_datetime')[:5],
        'blog' : blog
    }
    return render(request, 'view_blog.html',context)

def python_help(request):
    return render(request,'python_help.html')



