from django.db import models

# Create your models here.


class BlogUser(models.Model):
    email = models.EmailField(verbose_name='이메일')
    name = models.CharField(max_length=128, verbose_name='이름')
    password = models.CharField(max_length=128, verbose_name='비밀번호')
    phonenumber = models.IntegerField(verbose_name='전화번호')

    # level = models.CharField(max_length=8, verbose_name='등급',
    #     choices=(
    #         ('admin', 'admin'),
    #         ('user', 'user')
    #     ))
    register_date = models.DateTimeField(
        auto_now_add=True, verbose_name='등록날짜')

    def __str__(self):
        return self.email

    class Meta:
        db_table = 'user'
        verbose_name = '이용자'
        verbose_name_plural = '이용자'
