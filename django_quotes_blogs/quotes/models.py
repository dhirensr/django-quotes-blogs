from django.db import models


class Quotes(models.Model):
    quotes_text = models.CharField(max_length=400)

class Blogs(models.Model):
    blog_links = models.CharField(max_length=800)