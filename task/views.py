from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm
from django.views import View
from django.shortcuts import get_object_or_404

"""def task_list(request):
    tasks = Task.objects.all()

    if request.method == 'POST':
        form=TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form=TaskForm()
    return render(request, 'task/task_list.html', {'tasks': tasks, 'form' : form})"""

"""
def task_list(request):
 tasks = Task.objects.all()
 return render(request, 'task/task_list.html', {'tasks': tasks})


def nueva_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('nueva_task') 
    else:
        form = TaskForm()

    return render(request, 'task/nueva_tarea.html', {'form': form})"""


class TaskClass(View):
    template_name = 'task/task_list.html'

    def get(self, request):
        tasks = Task.objects.all()
        return render(request, self.template_name, {'tasks': tasks})

    def post(self, request):
        form = TaskForm(request.POST)
        form.save()
        tasks = Task.objects.all() #actualizar
        return render(request, self.template_name, {'tasks': tasks})
        

class TaskNueva(View):
    tasks = Task.objects.all()

    def post(self, request):
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('nueva_task')
        return render(request, 'task/nueva_tarea.html', {'tasks': self.tasks, 'form' : form})
    

    def get(self, request):
        tasks = Task.objects.all()
        form=TaskForm()
        return render(request, 'task/nueva_tarea.html', {'tasks': tasks, 'form' : form})
                

class DetallesClass(View):

    def get(self, request, pk): 
     task = get_object_or_404(Task, pk=pk) #no queremos todas las task solo la indicada, pasamos pk 
     return render(request, 'task/detalles.html', {'tasks': task})