from django.db import models
from django.urls import reverse


class Products(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    photo = models.ImageField(upload_to='photos/%Y/%M/%D/', blank=True)
    price = models.IntegerField()
    available = models.BooleanField(default=True)
    category = models.ForeignKey('Category', on_delete=models.PROTECT)

    def get_absolute_url(self):
        return reverse('view_products', kwargs={"products_id": self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ['category']


class Category(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name='Категория')

    def get_absolute_url(self):
        return reverse('category', kwargs={"category_id": self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['id']
