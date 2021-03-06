from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    LEVEL_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
        (6, '6'),
        (7, '7'),
        (8, '8'),
        (9, '9'),
        (10, '10'),
    )
    CATEGORIES = (
        ('-','-'),
        ('ATT','Allgemeine Tipps und Tricks'),
        ('EB','Ernährungsbericht'),
        ('AB','Ausrüstungsbericht'),
        ('TF','Trainingsfortschritt'),
        ('MT','Motivationstipps'),
        ('LGT','Laufgruppentrainingseinheit'),
    )
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    cover = models.ImageField(upload_to='images/', null=True, blank=True)
    distance_run = models.DecimalField(max_digits=5, decimal_places=2, default=0.000)
    performance_satisfaction = models.IntegerField(choices=LEVEL_CHOICES, default=1)
    kategorie = models.CharField(choices=CATEGORIES, default=1, max_length=200)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title