from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
def index(request):
    return render(request, 'design2.html')


def student_dashboard(request):
    """
    View function for the student dashboard.
    """
    return render(request, 'student_dashboard.html')



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

