from django.db import models
from django_ckeditor_5.fields import CKEditor5Field
from datetime import datetime
from django.utils.text import slugify
from django.urls import reverse
# Create your models here.
class Project(models.Model):
    project_name = models.CharField(max_length=255)
    project_description = models.TextField()
    link = models.URLField()
    def __str__(self):
        return self.project_name

class Blog(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=500, help_text="A brief description or summary of the blog post")
    publication_datetime = models.DateTimeField(default=datetime.now)
    # thumbnail = models.ImageField(upload_to='thumbnailbs', blank=True, null=True, 
    #                                help_text="Blog thumbnail image")
    content = CKEditor5Field('Content', config_name='extends', blank=True, null=True)
    author = models.CharField(max_length=255, default='engr umair')
    slug = models.SlugField(default='', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-publication_datetime']
        
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse("blog_view", kwargs={"slug": self.slug})
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
