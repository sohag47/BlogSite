from django.contrib.auth.models import User
from django.db import models

# Create your models here.
# Status
STATUS = (
    (0, "Draft"),
    (1, "Publish")
)


# Category1:
class Category(models.Model):
    category = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.category

# post body:
class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    updated_on = models.DateTimeField(auto_now=True)
    description = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, related_name='post', on_delete=models.CASCADE)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

# Comments:
class Comments(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)
