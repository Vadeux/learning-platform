from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Subject(models.Model):
    title = models.CharField(max_length=225)
    slug = models.SlugField(unique=True)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title


class Course(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='courses_created')
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='courses')
    title = models.CharField(max_length=225)
    slug = models.SlugField(unique=True)
    overview = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.title


class Module(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='modules')
    title = models.CharField(max_length=225)
    description = models.TextField(blank=True)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title
