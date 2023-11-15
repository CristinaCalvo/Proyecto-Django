from django.urls import path
from . import views

urlpatterns = [
	#path('', views.task_list, name='task_list'),
	#path('nueva_task/', views.nueva_task, name='nueva_task'),
	path('', views.TaskClass.as_view(), name='task_list'),
	path('nueva_task/', views.TaskNueva.as_view(), name='nueva_task'),
    path('detalles/<int:pk>/', views.DetallesClass.as_view(), name='detalles')
]
