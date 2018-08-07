from django.db import models

class Tweet(models.Model):
    user = models.CharField(max_length = 64)
    tweet_id = models.CharField(max_length = 24)
    tweet_date = models.DateTimeField()
    classification = models.CharField(max_length = 1)
    search = models.CharField(max_length = 32)

