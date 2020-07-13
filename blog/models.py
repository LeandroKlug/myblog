from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    STATUS  = (
        ('rascunho', 'Rascunho'),
        ('publicado', 'Publicado'),
    )
    title   = models.CharField(max_length=250)
    slug    = models.SlugField(max_length=250)
    author  = models.ForeignKey(User,
                                on_delete=models.CASCADE)
    context = models.TextField() 
    publicado= models.DateTimeField(default=timezone.now)
    criado  = models.DateTimeField(auto_now_add=True)
    alterado= models.DateTimeField(auto_now=True)
    status  = models.CharField(max_length=10,
                                choices=STATUS,
                                default='rascunhos')

    class Meta:
        ordering = ('-publicado',)

    def __str__(self):
        return '{} - {}'.format(self.title,self.author)
                   
