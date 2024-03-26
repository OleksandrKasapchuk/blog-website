from django.db import models
import datetime
from auth_system.models import Author


class Post(models.Model):
    title = models.CharField(max_length=300)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
    
    def published_recently(self):
        if datetime.date.now() - self.published_date < 7:
            return True