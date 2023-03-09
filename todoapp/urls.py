from django.urls import path
from .views import index, update, delete

urlpatterns = [
	path('', index, name='index'),
	path('update/<int:todo_id>', update, name='update'),
	path('delete/<int:todo_id>', delete, name='delete'),
]