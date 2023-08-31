"""
URL configuration for Project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

# from Management.views import signin
from Management import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.index , name='index' ),

    # LOGIN
    path('signin/', views.signin , name='signin' ),
    path('signup/', views.signup , name='signup' ),
    path('signout/', views.signout , name='signout' ),

    # CUSTOMERS 
    path('user_data/', views.list_user_data , name='user_data'),
    path('user_data/<int:id>/', views.detail_user_data , name='detail_user_data'),

    path('vehicle/', views.list_vehicles , name='vehicle'),
    path('vehicle/<int:id>/state/', views.state_vehicle , name='state_vehicle'),
    path('vehicle/<int:id>/delete/', views.delete_vehicle , name='delete_vehicle'),
    path('register_vehicle/', views.register_vehicle , name='register_vehicle'),

    path('appointment/', views.list_appointment , name='appointment'),
    path('appointment/<int:id>/', views.delete_appointment , name='delete_appointment'),
    path('register_date/', views.register_date ,name='register_date'),

    # WORK USERS list_mechanic
    path('list_mechanic/', views.list_mechanic ,name='list_mechanic'),
    path('list_mechanic/<int:id>/update/', views.update_mechanic ,name='update_mechanic'),
    path('list_mechanic/<int:id>/delete/', views.delete_mechanic ,name='delete_mechanic'),
    path('register_mechanic/', views.register_mechanic ,name='register_mechanic'),
    # path('list_mechanic/register_mechanic', views.register_mechanic ,name='register_mechanic'),

    path('list_jobs_pending/', views.list_jobs_pending ,name='list_jobs_pending'),
    path('list_jobs_pending/<int:id>/ot/', views.generate_ot ,name='generate_ot'),
    path('list_jobs_pending/<int:id>/delete/<str:job_type>/', views.delete_job ,name='delete_job_pending'),
    path('list_jobs_inprogress/', views.list_jobs_inprogress ,name='list_jobs_inprogress'),
    path('list_jobs_inprogress/<int:id>/checklist/', views.job_checklist ,name='checklist'),
    path('list_jobs_inprogress/<int:id>/update/', views.update_job ,name='update_job'),
    path('list_jobs_inprogress/<int:id>/<str:job_type>/delete/', views.delete_job ,name='delete_job_inprogress'),
    path('list_jobs_inprogress/<int:id>/completed/', views.completed_job ,name='completed_job'),
    path('list_jobs_completed/', views.list_jobs_completed ,name='list_jobs_completed'),
    path('list_jobs_completed/<int:id>/<str:job_type>/delete/', views.delete_job ,name='delete_job_completed'),
    # path('list_jobs/', views.list_jobs ,name='list_jobs'),
    # path('list_jobs/<int:id>/checklist/', views.job_checklist ,name='checklist'),
    # path('list_jobs/<int:id>/ot/', views.generate_ot ,name='generate_ot'),
    # path('list_jobs/<int:id>/update/', views.update_job ,name='update_job'),
    # path('list_jobs/<int:id>/delete/', views.delete_job ,name='delete_job'),
]
