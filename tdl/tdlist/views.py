from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import CustomUserCreationForm  # Make sure this exists
from django.contrib import messages
import json

def index(request):
    return render(request, 'tdlist/index.html')

def main_page(request):
    return render(request, 'tdlist/main.html')

def login_page(request):
    if request.method == 'POST':
        if 'username' in request.POST and 'password' in request.POST and 'email' not in request.POST:
            # Login form
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('main')
            else:
                messages.error(request, 'Invalid login credentials.')

        elif 'username' in request.POST and 'email' in request.POST and 'password1' in request.POST and 'password2' in request.POST:
            # Registration form
            form = CustomUserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Registration successful. Please log in.')
                return redirect('login')
            else:
                messages.error(request, 'Registration failed. Please ensure the form is correct.')

    return render(request, 'tdlist/login.html')
def plan_personal_tasks(request):
    return render(request, 'tdlist/personal_tasks.html')

def plan_work_routine(request):
    return render(request, 'tdlist/work_routine.html') 
 
def tasks_list_view(request):
    if request.method == 'POST':
        try:
            # Load both task lists
            tasks_data = request.POST.get('tasks')
            tasks = json.loads(tasks_data) if tasks_data else []

            # Determine source: personal or work
            source = request.META.get('HTTP_REFERER', '')
            if 'personal-tasks' in source:
                request.session['personal_tasks'] = tasks
            elif 'work-routine' in source:
                request.session['work_tasks'] = tasks

        except Exception as e:
            print("Error parsing tasks:", e)

    personal_tasks = request.session.get('personal_tasks', [])
    work_tasks = request.session.get('work_tasks', [])

    return render(request, 'tdlist/tasks_lists.html', {
        'personal_tasks': personal_tasks,
        'work_tasks': work_tasks
    })