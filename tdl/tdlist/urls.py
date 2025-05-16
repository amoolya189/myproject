from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_page, name='login'),
    path('main/', views.main_page, name='main'),
    path('personal-tasks/', views.plan_personal_tasks, name='plan_personal_tasks'),
    path('work-routine/', views.plan_work_routine, name='plan_work_routine'),
    path('tasks-list/', views.tasks_list_view, name='tasks_list'),
]
