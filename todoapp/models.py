from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    PRIORITY_CHOISES = (('1', 'Высокий'), ('2', 'Средний'), ('3', 'Низкий'))
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOISES, null=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['priority']
