from django.shortcuts import render
from .models import TodoList
from .forms import AddTaskForm
from django.http import HttpResponseRedirect


# Create your views here.

def addTask(request):
    displayData = TodoList.objects.all().order_by('task')
    if request.method == 'POST':
        fm = AddTaskForm(request.POST)
        if fm.is_valid():
            tk = fm.cleaned_data['task']
            data = TodoList(task=tk)
            data.save()
            return HttpResponseRedirect('/')
    else:
        fm = AddTaskForm()
    return render (request, 'index.html', {'forms': fm, 'displaydata':displayData})

def deleteTask(request, pk):
    if request.method == 'POST':
        deleteObj = TodoList.objects.get(id=pk)
        deleteObj.delete()
        return HttpResponseRedirect('/')