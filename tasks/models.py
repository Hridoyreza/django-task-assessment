from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image
# Create your models here.

class Task(models.Model):
    PRIORITY_CHOICES = [
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High'),
    ]


    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=1000)
    due_date = models.DateTimeField()
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES)
    is_complete = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated_at = models.DateTimeField(auto_now=True)
    img = models.ImageField(default='stock.jpg', upload_to='task_images', blank=True, null=True)
    

    def __str__(self):
        return self.title
    

    def get_absolute_url(self):
        return reverse('task-detail', args=[str(self.id)])
    

    '''def save(self):
        super().save()
        img = Image.open(self.img.path)'''