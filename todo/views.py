from django.shortcuts import render, redirect
from django.http import Http404
from django.utils.timezone import make_aware
from django.utils.dateparse import parse_datetime
from todo.models import Task
from django.shortcuts import redirect

def index(request):
    if request.method == 'POST':
        task = Task(
            title=request.POST.get('title', ''),
            note=request.POST.get('note', ''),
            due_at=make_aware(parse_datetime(request.POST['due_at'])) if request.POST['due_at'] else None
        )
        task.save()
        return redirect('detail', task_id=task.id)

    tasks = Task.objects.all().order_by('due_at') 
    return render(request, 'todo/index.html', {'tasks': tasks})

def index2(request):
    if request.method == 'POST':
        task = Task(title=request.POST['title'],
                    due_at=make_aware(parse_datetime(request.POST['due_at'])))
        task.save()

    if request.GET.get('order') == 'due':
        tasks = Task.objects.order_by('due_at')
    else:
        tasks = Task.objects.order_by('-posted_at')

    context = {
        'tasks': tasks
    }
    return render(request, 'todo/index2.html', context)


def detail(request, task_id):
    try:
        task = Task.objects.get(pk=task_id)
    except Task.DoesNotExist:
        raise Http404("Task dose not exist")

    context = {
        'task': task,
    }
    return render(request, 'todo/detail.html', context)




def update(request, task_id):
    try:
        task = Task.objects.get(pk=task_id)
    except Task.DoesNotExist:
        raise Http404("Task does not exist")
    
    if request.method == 'POST':
        task.title = request.POST['title']
        task.note = request.POST['note']
        task.due_at = make_aware(parse_datetime(request.POST['due_at']))
        task.save()    
        return redirect(detail, task_id)    

def close(request, task_id):
    try:
        task = Task.objects.get(pk=task_id)
    except Task.DoesNotExist:
        raise Http404("Task does not exist")
    task.completed = True
    task.save()
    return redirect(index)


def delete(request, task_id):
    try:
        task = Task.objects.get(pk=task_id)
    except Task.DoesNotExist:
        raise Http404("Task does not exist")

    task.delete()
    return redirect(index)