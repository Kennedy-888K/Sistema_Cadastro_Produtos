from django.db import models

class Brand(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nome')
    is_active = models.BooleanField(default=True, verbose_name='Ativo')
    description = models.TextField(blank=True, null=True, verbose_name='Descrição')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Criado Em')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Atualizado Em')

    class Meta:
        ordering = ['name']
        verbose_name = 'Marca'

def __str__(self):
        return self.name