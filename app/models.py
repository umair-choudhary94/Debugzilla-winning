from django.db import models

# Create your models here.
class Project(models.Model):
    project_name = models.CharField(max_length=255)
    project_description = models.TextField()
    link = models.URLField()
    def __str__(self):
        return self.project_name

