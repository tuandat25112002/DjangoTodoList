from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=35)
    description = models.TextField(null=True, blank=True)
    due_date = models.DateField()
    due_time = models.TimeField()
    completed = models.BooleanField(default=False)
    task_image = models.ImageField(null=True, blank=True, upload_to = "images/")    
    
    def __str__(self) -> str:
        return f'{self.title}'
    