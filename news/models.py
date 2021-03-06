from django.db import models
from django.urls import reverse


class News(models.Model):
    title = models.CharField(max_length=150, verbose_name='Наименования')
    content = models.TextField(blank=True, verbose_name='Контент')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Публикация')
    update_at = models.DateTimeField(auto_now=True, verbose_name='Обновление')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото', blank=True)
    is_published = models.BooleanField(default=True, verbose_name='Состояние')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Категория')

    def get_absolute_url(self):
        return reverse('view_news', kwargs={"pk": self.pk})

    '''def my_func(self):
        return None'''

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'НОВОСТЬ'
        verbose_name_plural = 'НОВОСТИ'
        ordering = ['-created_at', '-title']


class Category(models.Model):
    title = models.CharField(max_length=150, db_index=True,
                             verbose_name='Название категории', blank=True)

    def get_absolute_url(self):
        return reverse('category', kwargs={"category_id": self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'КАТЕГОРИЯ'
        verbose_name_plural = 'КАТЕГОРИИ'
        ordering = ['title']
