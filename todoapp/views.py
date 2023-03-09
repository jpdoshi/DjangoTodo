from django.shortcuts import render, redirect
from .models import TodoItem

# Create your views here.
def index(request):
	context = {
		'title': "Django Todo App",
		'todos': TodoItem.objects.order_by('todo_time'),
	}
	if request.method == "POST":
		title = request.POST.get("title")
		time = request.POST.get("time")
		
		todo = TodoItem(todo_title=title, todo_time=time)
		todo.save()

	return render(request, 'index.html', context)

def update(request, todo_id):
	todo = TodoItem.objects.get(pk=todo_id)
	context = {
		'todo_id': todo_id,
		'todo_time': todo.todo_time,
		'todo_title': todo.todo_title,
	}
	if request.method == "POST":
		todo.todo_time = request.POST.get("time")
		todo.todo_title = request.POST.get("title")
		todo.save()
		return redirect("index")

	return render(request, 'update.html', context)

def delete(request, todo_id):
	todo = TodoItem.objects.get(pk=todo_id)
	todo.delete()

	return redirect("index")
