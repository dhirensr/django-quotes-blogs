from django.db import models


class Quotes(models.Model):
    quotes_text = models.CharField(max_length=400)
    added_date = models.DateTimeField('date added')