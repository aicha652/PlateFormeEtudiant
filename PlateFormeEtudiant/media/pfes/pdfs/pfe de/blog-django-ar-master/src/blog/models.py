from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    post_date = models.DateTimeField(default=timezone.now)
    post_update = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        # return '/detail/{}'.format(self.pk)
        return reverse('detail', args=[self.pk])

    class Meta:
        ordering = ('-post_date', )


class Comment(models.Model):
    name = models.CharField(max_length=50, verbose_name='اNom')
    email = models.EmailField(verbose_name='Email')
    body = models.TextField(verbose_name='Commentaire')
    comment_date = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return 'commenté {} sur {}.'.format(self.name, self.post)

    class Meta:
        ordering = ('-comment_date',)




