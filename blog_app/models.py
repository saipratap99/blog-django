from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
  title = models.CharField(max_length=100)
  content = models.TextField()
  # timezone.now is a function but is called only when the data is inserted
  date_posted = models.DateTimeField(default=timezone.now)
  auth = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return self.title

  def get_absolute_url(self):
    return reverse('post-details',kwargs={'pk': self.id})
