from django.db import models

status_choices = [('new', 'Новая'), ('in_progress', 'В процессе'),  ('done', 'Сделано')]
# Create your models here.
class Card(models.Model):
    description = models.CharField(max_length=255, null=False, blank=False)
    status = models.CharField(max_length=32, null=False, blank=False, choices=status_choices, default='new')
    date = models.DateField(null=True)
    more_description = models.TextField(max_length=1024, null=True)

    class Meta:
        db_table = 'cards'
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'

    def __str__(self):
        return f'{self.id}. {self.description}: {self.status}'