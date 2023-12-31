from django.db import models


# Create your models here.
class BaseModel(models.Model):
    created_at = models.DateTimeField(("created_date"), auto_now_add=True)
    update_at = models.DateTimeField(("update_date"), auto_now=True)

    class Meta:
        abstract = True
