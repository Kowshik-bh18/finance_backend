from django.db import models

# Create your models here.
# core/models.py
class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True