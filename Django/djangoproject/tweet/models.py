from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Tweet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(max_length=280)  # Twitter's character limit is 280
    photo = models.ImageField(upload_to='tweet_photos/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.user.username}: {self.text[:10]}..."  # Display first 10 characters of the tweet content