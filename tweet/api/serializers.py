from rest_framework.serializers import ModelSerializer
from tweet.models import Tweet

class TweetSerializer(ModelSerializer):
    class Meta:
        model = Tweet
        fields = ('id', 'user', 'tweet_id', 'tweet_date', 'tweet_text', 'classification', 'search')