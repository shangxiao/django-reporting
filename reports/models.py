from django.db import models


class Site(models.Model):
    name = models.CharField()


class Level(models.Model):
    site = models.ForeignKey(Site, on_delete=models.CASCADE)
    name = models.CharField()


class Space(models.Model):
    level = models.ForeignKey(Level, on_delete=models.CASCADE)
    name = models.CharField()


class Data(models.Model):
    space = models.ForeignKey(Space, on_delete=models.CASCADE)
    count = models.IntegerField()
