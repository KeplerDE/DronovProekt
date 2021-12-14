from django.db import models

class Bb(models.Model):
    title = models.CharField(max_length=50, verbose_name='Material')
    content = models.TextField(null=True, blank=True, verbose_name='Description')
    price = models.FloatField(null=True, blank=True, verbose_name='Price')
    published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Published')
    rubric = models.ForeignKey('Rubric', null=True, on_delete=models.PROTECT, verbose_name='Kategorie')

    class Meta:
        verbose_name_plural = 'Anzeigen'
        verbose_name = 'Material'
        ordering = ['-published']


class Rubric(models.Model):
    name = models.CharField(max_length=20, db_index=True, verbose_name='Name')
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Kategorien'
        verbose_name = 'Kategorie'
        ordering = ['name']
