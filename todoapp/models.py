from django.db import models
from django.utils import timezone

# Create your models here.
class TodoItem(models.Model):
	todo_id = models.AutoField(primary_key=True)
	todo_title = models.CharField(max_length=50)
	todo_time  = models.TimeField(default=timezone.now())

	def __str__(self):
		return f'{self.todo_title}'
