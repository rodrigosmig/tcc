from rest_framework.serializers import ModelSerializer
from tweet.models import Tweet, Search

class TweetSerializer(ModelSerializer):
    class Meta:
        model = Tweet
        fields = ('id', 'user', 'tweet_id', 'tweet_date', 'tweet_text', 'classification', 'search')

class SearchSerializer(ModelSerializer):
    class Meta:
        model = Search
        fields = ('expression', 'search_date')