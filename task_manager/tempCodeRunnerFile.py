from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    due_date = models.DateField()
    priority = models.CharField(max_length=20)
    assigned_to = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    def __str__(self):
        return self.title