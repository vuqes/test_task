from django.db import models
import uuid
from .utils import WEBPField


def image_folder(instance, filename):
    return 'photos/{}.webp'.format(uuid.uuid4().hex)


class Product(models.Model):
    name = models.CharField(max_length=255)
    art = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.ForeignKey('Status', on_delete=models.PROTECT)
    image = models.ImageField(upload_to=image_folder, verbose_name='image', null=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.name, self.status


class Status(models.Model):
    status_value = models.CharField(max_length=50)

    def __str__(self):
        return self.status_value

    class Meta:
        ordering = ['status_value']
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'
