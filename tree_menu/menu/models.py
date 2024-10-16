from django.db import models
from django.urls import reverse
from mptt.models import MPTTModel, TreeForeignKey


class Paragraph(MPTTModel):
    title = models.CharField(max_length=100, verbose_name='Название',
                             help_text='Название этого раздела')
    parent = TreeForeignKey('self', on_delete=models.CASCADE,
                            null=True, blank=True, related_name='children',
                            verbose_name='Родитель')
    slug = models.SlugField(max_length=100, unique=True, verbose_name='Слаг')
    menu_title = models.CharField(max_length=100, verbose_name='Название меню',
                                  help_text='Общее название меню')

    class Meta:
        verbose_name = 'Раздел'
        verbose_name_plural = 'Разделы'

    def __str__(self):
        return str(self.title)

    def get_absolute_url(self):
        return reverse('get_page', args=[str(self.slug)])
