from django.db import models
from multiselectfield import MultiSelectField
import os
# Create your models here.


class Jobs(models.Model):
    Id = models.AutoField(primary_key=True)
    Title = models.CharField(max_length=255)
    Job_name = models.CharField(max_length=255)
    Open_date = models.DateField()
    Close_date = models.DateField()
    is_published = models.BooleanField(default=False)
    Created_at = models.DateTimeField(auto_now_add=True)
    Updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.Title


def get_upload_path(instance, filename):
    return os.path.join('uploads', instance.Position.Job_name, filename)


class Candidates(models.Model):
    id = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=255)
    Email = models.EmailField(max_length=255)
    Position = models.ForeignKey(Jobs, on_delete=models.CASCADE)
    Created_at = models.DateTimeField(auto_now_add=True)
    CV = models.FileField(upload_to=get_upload_path)
