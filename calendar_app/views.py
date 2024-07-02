from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import SignUpForm
from django.http import HttpResponse
from django.http import HttpResponseForbidden
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Task1,Task2,Task3,UserProfile
from .forms import TaskForm1,TaskForm2,TaskForm3,RedirectForm
import calendar
from calendar import monthrange, month_name, calendar
from calendar import monthrange, month_name
from calendar import monthcalendar as get_month_calendar
from datetime import datetime, timedelta
from datetime import date, timedelta
from django.utils import timezone
from calendar import monthcalendar
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy


from .forms import MonthYearForm

@staff_member_required
def admin_interface(request):
    return render(request, 'admin_interface.html')

def index(request):
    if request.method == 'POST':
        form = RedirectForm(request.POST)
        if form.is_valid():
            redirect_to = form.cleaned_data['redirect_to']
            if redirect_to == 'Department1':
                return redirect('calendar')
            elif redirect_to == 'Department2':
                return redirect('calendar2')
            elif redirect_to == 'Department3':
                return redirect('calendar3')
    else:
        form = RedirectForm()
    return render(request, 'index.html', {'form': form})

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    if user.is_staff:
                        user_profile = UserProfile.objects.get(user=user)
                        department = user_profile.department
                        if department == 'department1':
                            return redirect('admin_task_list')
                        elif department == 'department2':
                            return redirect('admin_task_list2')
                        elif department == 'department3':
                            return redirect('admin_task_list3')
                        
                        #return redirect('calendar')  # redirect to staff dashboard
                    else:
                        return redirect('index')  # redirect to user dashboard
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

#functions of department 1
@login_required
def calendar_view(request):
    user_profile = UserProfile.objects.get(user=request.user)
    if user_profile.department == 'department1':#calendar_view for dept1
       if request.method == 'POST':
        form = TaskForm1(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user  # Assign the current user to the task
            task.save()
            return redirect('calendar')
       else:
           form = TaskForm1()
    
       tasks = Task1.objects.filter(user=request.user)  # Retrieve tasks for the current user

       context = {
        'form': form,
        'tasks': tasks,
       }
       return render(request, 'calendar.html', context)
    else:
        return HttpResponseForbidden("You are not authorized to access this page.")


@login_required
def displaytask(request):                         #displaytask for users of dept1 to view task
    current_date = timezone.now().date()
    tasks = Task1.objects.filter(user=request.user, date__gte=current_date).order_by('date')
    return render(request, 'displaytask.html', {'tasks': tasks})
#admin
@login_required
def admin_task_list(request):                    #for admin of dept1 to see and approve the task for their department users
    tasks = Task1.objects.filter(approved=False)
    return render(request, 'admin_task_list.html', {'tasks': tasks})


@login_required
def approve_task(request, task_id):
    task = Task1.objects.get(id=task_id)
    task.approved = True
    task.save()
    return redirect('admin_task_list')

def task_list(request):
    tasks = Task1.objects.filter(user=request.user,approved=True)
    return render(request, 'task_list.html', {'tasks': tasks})

def admin_task_views(request):
    tasks = Task1.objects.filter(approved=True).order_by('date')
    return render(request, 'admin_task_views3.html', {'tasks': tasks})

@login_required
def admin_edit_task(request, pk):
    task = Task1.objects.get(pk=pk)
    if request.method == 'POST':
        form = TaskForm1(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('admin_task_list')
    else:
        form = TaskForm1(instance=task)
    return render(request, 'admin_edit_task.html', {'form': form, 'task': task})


#functions of department 2
@login_required
def calendar_view2(request):
    user_profile = UserProfile.objects.get(user=request.user)
    if user_profile.department == 'department2':#calendar_view for dept1
       if request.method == 'POST':
        form = TaskForm2(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user  # Assign the current user to the task
            task.save()
            return redirect('calendar')
       else:
           form = TaskForm2()
    
       tasks = Task2.objects.filter(user=request.user)  # Retrieve tasks for the current user

       context = {
        'form': form,
        'tasks': tasks,
       }
       return render(request, 'calendar2.html', context)
    else:
        return HttpResponseForbidden("You are not authorized to access this page.")

@login_required
def displaytask2(request):                        #displaytask2 for users of dept2 to view task
    current_date = timezone.now().date()
    tasks = Task2.objects.filter(user=request.user, date__gte=current_date).order_by('date')
    return render(request, 'displaytask2.html', {'tasks': tasks})
#admin
@login_required
def admin_task_list2(request):                    #for admin of dept2 to see and approve the task for their department users
    tasks = Task2.objects.filter(approved=False)
    return render(request, 'admin_task_list2.html', {'tasks': tasks})


@login_required
def approve_task2(request, task_id):
    task = Task2.objects.get(id=task_id)
    task.approved = True
    task.save()
    return redirect('admin_task_list2')

def task_list2(request):
    tasks = Task2.objects.filter(user=request.user,approved=True)
    return render(request, 'task_list2.html', {'tasks': tasks})

def admin_task_views2(request):
    tasks = Task2.objects.filter(approved=True).order_by('date')
    return render(request, 'admin_task_views3.html', {'tasks': tasks})

def admin_edit_task2(request, pk):
    task = Task2.objects.get(pk=pk)
    if request.method == 'POST':
        form = TaskForm2(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('admin_task_list2')
    else:
        form = TaskForm2(instance=task)
    return render(request, 'admin_edit_task2.html', {'form': form, 'task': task})



#functions of department 3
@login_required
def calendar_view3(request):
    user_profile = UserProfile.objects.get(user=request.user)
    if user_profile.department == 'department3':#calendar_view for dept3
       if request.method == 'POST':
        form = TaskForm3(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user  # Assign the current user to the task
            task.save()
            return redirect('calendar')
       else:
           form = TaskForm3()
    
       tasks = Task3.objects.filter(user=request.user)  # Retrieve tasks for the current user

       context = {
        'form': form,
        'tasks': tasks,
       }
       return render(request, 'calendar3.html', context)
    else:
        return HttpResponseForbidden("You are not authorized to access this page.")


@login_required
def displaytask(request):                        #displaytask for users of dept1 to view task
    current_date = timezone.now().date()
    tasks = Task3.objects.filter(user=request.user, date__gte=current_date).order_by('date')
    return render(request, 'displaytask.html', {'tasks': tasks})
#admin
@login_required
def admin_task_list3(request):      #for admin of dept3 to see and approve the task for their department us
    user_profile = UserProfile.objects.get(user=request.user)
    if user_profile.department == 'department3':
        tasks = Task3.objects.filter(approved=False)
        return render(request, 'admin_task_list3.html', {'tasks': tasks})
    else:
        return HttpResponseForbidden("You are not authorized to access this page.")



@login_required
def approve_task3(request, task_id):
    task = Task3.objects.get(id=task_id)
    task.approved = True
    task.save()
    return redirect('admin_task_list3')

def task_list3(request):
    tasks = Task3.objects.filter(user=request.user,approved=True)
    return render(request, 'task_list.html', {'tasks': tasks})
@login_required
def admin_task_views3(request):
    tasks = Task3.objects.filter(approved=True).order_by('date')   
    return render(request, 'admin_task_views3.html', {'tasks': tasks})


def admin_edit_task3(request, pk):
    task = Task3.objects.get(pk=pk)
    if request.method == 'POST':
        form = TaskForm3(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('admin_task_list3')
    else:
        form = TaskForm3(instance=task)
    return render(request, 'admin_edit_task3.html', {'form': form, 'task': task})


def my_view(request):
    
    data1 = Task1.objects.filter(approved=True)
    data2 = Task2.objects.filter(approved=True)
    data3 = Task3.objects.filter(approved=True)

    # Combine the data into a unified list
    combined_data = list(data1) + list(data2) + list(data3)

    
    return render(request, 'master.html', {
        'combined_data': combined_data,
    })



def my_viewcal(request):
      
    year = int(request.GET.get('year', date.today().year))
    month = int(request.GET.get('month', date.today().month))
    
    
    data1 = Task1.objects.filter(date__year=year, date__month=month, approved=True).order_by('date')
    data2 = Task2.objects.filter(date__year=year, date__month=month, approved=True).order_by('date')
    data3 = Task3.objects.filter(date__year=year, date__month=month, approved=True).order_by('date')

    
    combined_data = list(data1) + list(data2) + list(data3)
    cal = monthcalendar(year, month)


    
    return render(request, 'calview.html', {
        'year': year,
        'month': month,
        'month_name': month_name[month],
        'combined_data': combined_data,
        'calendar': cal,

    })

def fetch_task(request):
    day = int(request.GET.get('day'))
    selected_year = int(request.GET.get('year'))
    selected_month = int(request.GET.get('month'))

    tasks = Task1.objects.filter(due_date__year=selected_year, due_date__month=selected_month, due_date__day=day)

    return render(request, 'fetchtask.html', {
        'tasks': tasks,})


#not in use now
@login_required
def add_task(request, year, month, day):
    date = datetime(year, month, day).date()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save()#commit=false
           # task.user = request.user
            #task.date = date
            #task.save()
            return redirect('calendar')
    else:
        form = TaskForm()
    return render(request, 'add_task.html', {'form': form, 'date': date})

