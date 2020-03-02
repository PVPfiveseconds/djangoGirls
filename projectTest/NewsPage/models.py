from django.db import models
from django.contrib.auth import get_user_model

# Change this name according to the real use of this model


class AbstractContent(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Category(AbstractContent):
    name = models.CharField(max_length=25, null=False, blank=False)

    def __str__(self):
        return self.name


class Article(AbstractContent):
    DRAFT = 'DRAFT'
    PUBLISH = 'PUBLISH'
    ARCHIVE = 'ARCHIVE'

    STATUS = (
        (DRAFT, 'Draft'),
        (PUBLISH, 'Publish'),
        (ARCHIVE, 'Archive'),
    )

    title = models.CharField(max_length=200)
    creator = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name="related_article"
    )

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="related_article"
    )

    current_status = models.CharField(max_length=7, choices=STATUS, default=DRAFT)

    content = models.TextField()

    def __str__(self):
        return self.title
