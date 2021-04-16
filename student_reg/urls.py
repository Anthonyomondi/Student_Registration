from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.student_form,name='student_insert'), #get and post request for insert op
    path('<int:id>/', views.student_form,name='student_update'), #get and post request for update op
    path('delete/<int:id>/', views.student_delete, name='student_delete'),
    path('list/',views.student_list,name='student_list'), #get request to retrieve and display all records
]