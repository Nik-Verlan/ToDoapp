from django.db import models


class Task(models.Model):
    title = models.CharField('Название', max_length=200)
    description = models.TextField('Описание', null=True, blank=True)
    complete = models.BooleanField('Выполнение', default=False)
    created = models.DateTimeField('Создана', auto_now_add=True)
    PRIORITY_CHOISES = (('Высокий', 'Высокий'), ('Средний', 'Средний'), ('Низкий', 'Низкий'))
    priority = models.CharField('Приоритет', max_length=10, choices=PRIORITY_CHOISES, null=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['priority']
