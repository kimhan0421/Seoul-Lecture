from django.db import models


class Post(models.Model):
    title = models.CharField(
        verbose_name='제목',
        max_length=80,
    )

    content = models.TextField(
        verbose_name='내용'
    )

    created_at = models.DateTimeField(
        verbose_name='작성일'
    )

    created_by = models.CharField(
        verbose_name='작성자',
        max_length=100
    )

    is_view = models.BooleanField(
        verbose_name='공개 여부',
        default=True
    )

    image = models.ImageField(upload_to='images/', default='')

    def __str__(self):
        return '%s - %s - %s - %s - %s - %s' % (self.title, self.content, self.created_at, self.created_by, self.is_view, self.image)


class Comment(models.Model):
    comment_title = models.ForeignKey(to=Post, on_delete=models.CASCADE)
    comment_content = models.CharField(max_length=100)