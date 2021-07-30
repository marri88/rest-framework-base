from django.db import models
from django.urls import reverse
from agro_user.models import AgroUser
# from django.contrib.auth.models import AbstractUser
# class ArgoUser(AbstractUser):
#     pass


class Category(models.Model):
    title = models.CharField(max_length=255, verbose_name='Имя категории', blank=True, null=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('category_detail', kwargs={'slug': self.slug})

    class Meta:
        ordering = ['title']
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Post(models.Model):
    user = models.ForeignKey(AgroUser, verbose_name='Пользователь', on_delete=models.CASCADE, null=False, blank=False)
    slug = models.SlugField(unique=True,  blank=True, null=True)
    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.CASCADE,  blank=False, null=False)
    title = models.CharField(max_length=255, verbose_name='Наименование',  blank=False, null=False)
    descriptions = models.CharField(max_length=150, verbose_name='Описание',  blank=False, null=False)
    image = models.ImageField(verbose_name='Изображение', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Опубликовано')
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    favourite = models.ManyToManyField(AgroUser,  related_name="fav_post", blank=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'slug': self.slug})

    class Meta:
        ordering = ['title']
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'


# class Comment(models.Model):
#     user = models.ForeignKey(AgroUser, related_name='comments', on_delete=models.CASCADE, blank=True, null=True)
#     post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments', blank=True, null=True)
#     email = models.EmailField(blank=True, null=True)
#     body = models.TextField(blank=True, null=True)
#     created = models.DateTimeField(auto_now_add=True)
#
#
#     def __str__(self):
#         return 'Comment by {} on {}'.format(self.user, self.post)
#
#     class Meta:
#         verbose_name = 'Comment'
#         verbose_name_plural = 'Comments'
