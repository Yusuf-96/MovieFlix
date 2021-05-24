from django.db import models
from django.db.models.signals import pre_save
from django.utils import timezone
from django.utils.text import slugify
from videos.models import Video
# Create your models here.


class PublishStateOptions(models.TextChoices):
    PUBLISH = 'PU', 'Publish'
    DRAFT = 'DR', 'Draft'


class PlaylistQuerySet(models.QuerySet):
    def published(self):
        now = time
        return self.filter(
            state=PublishStateOptions.PUBLISH,
            publish_timestamp__lte=now
        )


class PlaylistManager(models.Manager):
    def get_queryset(self):
        return PlaylistQuerySet(self.model, using=self._db)

    def published(self):
        return self.get_queryset().published()


class Playlist(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    video = models.ForeignKey(Video, null=True, on_delete=models.SET_NULL)
    slug = models.SlugField(blank=True, null=True)
    active = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    state = models.CharField(
        max_length=2, choices=PublishStateOptions.choices, default=PublishStateOptions.DRAFT)
    publish_timestamp = models.DateTimeField(
        auto_now_add=False, auto_now=False, blank=True, null=True)

    objects = PlaylistManager()

    @property
    def is_published(self):
        return self.active

    def save(self, *args, **kwargs):
        if self.slug is None:
            self.slug = slufgify(self.title)
        super().save(*args, **kwargs)

def publish_state_pre_save(sender, instance, *args, **kwargs):
    is_publishe = instance.state == instance.PublishStateOptions.PUBLISH
    is_draft = instance.state == instance.PublishStateOptions.DRAFT
    if is_publish and instance.publish_timestamp is None:
        instance.publish_timestamp = timezone.now()
    elif is_draft:
        instance.publish_timestamp = None

pre_save.connect(publish_state_pre_save, sender = Playlist)

def slugify_pre_save(sender, instance, *args, **kwargs):
    title = instance.title
    slug = instance.slug
    if slug is None:
        instance.slug = slugify(title)

pre_save.connect(slugify_pre_save, sender = Playlist)
        
