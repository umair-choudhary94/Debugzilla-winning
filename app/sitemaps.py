from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import Blog  # Import your model

class BlogSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8

    def items(self):
        return Blog.objects.all()

    def lastmod(self, obj):
        return obj.updated_at  # Ensure your Blog model has an "updated_at" field

class StaticViewSitemap(Sitemap):
    priority = 0.5
    changefreq = "monthly"

    def items(self):
        return ["index", "login", "student_dashboard", "django_roadmap", "enroll", "web_basics_course", "privacy_policy", "terms_and_conditions", "django", "django_introduction", "django_projects", "web_development_basic", "flask", "python", "database", "git_github_basic",'blogs']  # Add your static view names

    def location(self, item):
        return reverse(item)
