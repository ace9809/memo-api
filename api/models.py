from django.db import models


class Memo(models.Model):
    title = models.CharField(max_length=256, default='title')
    description = models.CharField(max_length=2048, default='')

    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    class Meta:
        ordering = ('updated', )

    def save(self, *args, **kwargs):
        super(Memo, self).save(*args, **kwargs)

# Create your models here.
