from django.db import models
from django.db import IntegrityError
from django.utils.text import slugify
from hashid_field import HashidAutoField


class Channel(models.Model):
    """
    Stores a channel and its related parent if exist
    """
    id = HashidAutoField(primary_key=True)
    name = models.CharField(max_length=60)
    slug = models.SlugField(max_length=70, unique=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        # automatically fill the slug field
        self.slug = slugify(self.name)
        super(Channel, self).save(*args, **kwargs)


class Category(models.Model):
    """
    Stores a category with or without its parent.
    A combination of name and parent must be unique.
    """
    id = HashidAutoField(primary_key=True)
    name = models.CharField(max_length=60)
    slug = models.SlugField(max_length=70)
    parent = models.ForeignKey(
        'self', on_delete=models.CASCADE,
        null=True, related_name='subcategories')
    channel = models.ForeignKey(Channel, related_name='categories')

    class Meta:
        unique_together = (('slug', 'parent', 'channel'),)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        # automatically fill the slug field
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)
