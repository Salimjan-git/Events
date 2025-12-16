# views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Event, Category, Company, Profile

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        bio = request.POST['bio']
        phone = request.POST['phone']
        
        if User.objects.filter(username=username).exists():
            return redirect('register')
        
        user = User.objects.create_user(username=username, password=password, email=email)
        Profile.objects.create(user=user, bio=bio, phone=phone)
        login(request, user)
        return redirect('event_list')
    
    return render(request, 'auth/register.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('event_list')
    
    return render(request, 'auth/login.html')

def user_logout(request):
    logout(request)
    return redirect('event_list')

def event_list(request):
    events = Event.objects.all()
    return render(request, 'events/event_list.html', {'events': events})

def event_detail(request, pk):
    event = get_object_or_404(Event, pk=pk)
    return render(request, 'events/event_detail.html', {'event': event})

@login_required
def event_create(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        date = request.POST['date']
        category_id = request.POST['category']
        company_id = request.POST['company']
        
        category = get_object_or_404(Category, id=category_id)
        company = get_object_or_404(Company, id=company_id)
        
        event = Event.objects.create(
            title=title,
            description=description,
            date=date,
            category=category,
            company=company
        )
        return redirect('event_detail', pk=event.id)
    
    categories = Category.objects.all()
    companies = Company.objects.all()
    return render(request, 'events/event_form.html', {'categories': categories, 'companies': companies})

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'events/category_list.html', {'categories': categories})

def company_list(request):
    companies = Company.objects.all()
    return render(request, 'events/company_list.html', {'companies': companies})

@login_required
def profile_detail(request):
    profile = get_object_or_404(Profile, user=request.user)
    return render(request, 'events/profile.html', {'profile': profile})