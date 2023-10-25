from django.db import models


nullable = {'null': True, 'blank': True}


class Post(models.Model):
    title = models.CharField(max_length=100, verbose_name='заголовок')
    slug = models.SlugField(max_length=100, unique=True, **nullable, verbose_name='slug')
    content = models.TextField(max_length=500, verbose_name='содержимое')
    image = models.ImageField(upload_to='posts/', **nullable, verbose_name='превью')
    creation_date = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')  # дата создания
    is_published = models.BooleanField(default=True, verbose_name='опубликовано')
    view_count = models.IntegerField(default=0, verbose_name='количество просмотров')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
