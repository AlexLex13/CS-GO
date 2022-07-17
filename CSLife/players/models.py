from django.db import models
from django.urls import reverse


class Player(models.Model):
    nickname = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    age = models.IntegerField(blank=True, null=True)
    information = models.TextField(blank=True)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", null=True)
    team = models.ForeignKey('Team', on_delete=models.PROTECT, null=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    def __str__(self):
        return self.nickname

    def get_absolute_url(self):
        return reverse('player', kwargs={'player_slug': self.slug})

    class Meta:
        verbose_name = 'Player'
        verbose_name_plural = 'Players'
        ordering = ['nickname']


class Team(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    country = models.CharField(max_length=255)
    coach = models.CharField(max_length=255)
    information = models.TextField(blank=True)
    logo = models.ImageField(upload_to="photos/%Y/%m/%d/")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('team', kwargs={'team_slug': self.slug})

    class Meta:
        verbose_name = 'Team'
        verbose_name_plural = 'Teams'
        ordering = ['name']
