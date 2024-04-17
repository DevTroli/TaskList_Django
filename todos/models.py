from django.db import models

class Todo(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)
    done_date = models.DateField(null=True, blank=True)
