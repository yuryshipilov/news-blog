from django.db import models

class Articles(models.Model):
    title = models.CharField('Название', max_length=100)
    full_text = models.TextField('Текст новости')
    date = models.DateTimeField('Дата публикации')
    anons = models.CharField('Анонс', max_length=200)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'