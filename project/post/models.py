from django.db import models

# Create your models here.


class Post(models.Model):
    email = models.ForeignKey('user.BlogUser', on_delete=models.CASCADE)
    title = models.CharField(max_length=100, verbose_name='제목')
    description = models.TextField(verbose_name='설명')
    register_date = models.DateTimeField(
        auto_now_add=True, verbose_name='작성일')

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'post'
        verbose_name = '게시글'
        verbose_name_plural = '게시글'
