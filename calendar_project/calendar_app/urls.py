from django.contrib import admin
from django.urls import path,include
from calendar_app import views as calendar_views
from . import views
#from .views import CustomLoginView


urlpatterns = [
   # path('admin/', admin.site.urls),
    path('admin_interface/', calendar_views.admin_interface, name='admin_interface'),

    path('signup/', calendar_views.signup, name='signup'),
    path('login/', calendar_views.login_view, name='login'),
    path('logout/', calendar_views.logout_view, name='logout'),
    path('displaytask/',calendar_views.displaytask, name='displaytask'),
    path('displaytask2/',calendar_views.displaytask2, name='displaytask2'),

    path('index/',calendar_views.index, name='index'),
   #path('calendar/', include('calendar_app.urls')),
   # path('accounts/', include('django.contrib.auth.urls')),
    path('', calendar_views.calendar_view, name='calendar'),
    path('calendar2/', calendar_views.calendar_view2, name='calendar2'),
    path('calendar3', calendar_views.calendar_view3, name='calendar3'),

    path('add_task/<int:year>/<int:month>/<int:day>/', views.add_task, name='add_task'),
    path('add-task/', calendar_views.add_task, name='add_task'),

    #admin panel urls
    path('admin_task_list/', calendar_views.admin_task_list, name='admin_task_list'),#admin dep1
    path('admin_task_approve/<int:task_id>/', calendar_views.approve_task, name='approve_task'),
    path('admin_task_list2/', calendar_views.admin_task_list2, name='admin_task_list2'),#admin dep2
    path('admin_task_approve2/<int:task_id>/', calendar_views.approve_task2, name='approve_task2'),
    path('admin_task_list3/', calendar_views.admin_task_list3, name='admin_task_list3'),#admin dep3
    path('admin_task_approve3/<int:task_id>/', calendar_views.approve_task3, name='approve_task3'),
    
    path('task_list/', calendar_views.task_list, name='task_list'),
    path('task_list2/', calendar_views.task_list2, name='task_list2'),
    path('task_list3/', calendar_views.task_list3, name='task_list3'),

    path('admin_task_views3/', calendar_views.admin_task_views3, name='admin_task_views3'),
    path('admin_task_views2/', calendar_views.admin_task_views2, name='admin_task_views2'),
    path('admin_task_views/', calendar_views.admin_task_views, name='admin_task_views'),




    path('admin_edit_task/<pk>/', calendar_views.admin_edit_task, name='admin_edit_task'),
    path('admin_edit_task2/<pk>/', calendar_views.admin_edit_task2, name='admin_edit_task2'),
    path('admin_edit_task3/<pk>/', calendar_views.admin_edit_task3, name='admin_edit_task3'),

    path('master/', calendar_views.my_view, name='master'),
    path('calview/', calendar_views.my_viewcal, name='calview'),
    path('fetchtask/', calendar_views.fetch_task, name='fetchtask'),






   # path('admin_login/', CustomLoginView.as_view(), name='admin_login'),

 ]
