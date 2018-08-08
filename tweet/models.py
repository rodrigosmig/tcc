from django.db import models

class Search(models.Model):
    expression = models.CharField(max_length = 24)
    search_date = models.DateTimeField(auto_now_add = True)

class Tweet(models.Model):
    user = models.CharField(max_length = 64)
    tweet_id = models.CharField(max_length = 24)
    tweet_date = models.DateTimeField()
    tweet_text = models.CharField(max_length = 280)
    classification = models.CharField(max_length = 1)
    search = models.ForeignKey(Search, on_delete = models.CASCADE)

