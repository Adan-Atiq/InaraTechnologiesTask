from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings

#Custom user model 
class CustomUser(AbstractUser):
    #Unique email, Mobile number,Role choices field for each user
    email = models.EmailField(unique=True)
    mobile_number = models.CharField(max_length=20)
    ROLE_CHOICES = (
        ('writer', 'Writer'),
        ('viewer', 'Viewer'),
    )

    #define if the user is a writer or viewer
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='viewer')
    def __str__(self):
        return self.username

class BlogPost(models.Model):
    #Title and Contentof the blog post
    title = models.CharField(max_length=200)
    content = models.TextField()

    publication_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
