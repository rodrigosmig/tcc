from rest_framework.viewsets import ModelViewSet
from tweet.models import Search, Tweet
from .serializers import TweetSerializer
from requests_oauthlib import OAuth1Session
from datetime import datetime, timezone
from django.conf import settings
import numpy as np
import requests
import json
import pickle
import pytz

class TweetViewSet(ModelViewSet):
    serializer_class = TweetSerializer

    def get_queryset(self):
        #expressão de busca enviada
        expression = self.request.query_params.get('search')

        if(expression):            
            #codifica a expressão para o padrão utilizado na web
            search_word = requests.utils.quote(expression)

            API_KEY = '5MU3Vu3zXm6xn0XQuIZzg2Q1I'
            API_SECRET = 'huaphtigFjD0riKGuT9rZHig6RCCr0zR7eeBsNvZtldcXCYnQz'
            ACCESS_TOKEN = '27258579-r6APNk6Y1mracJWcdAln3C6NsC5hj9dZKG8G2f654'
            ACCESS_TOKEN_SECRET = 'ulF8lFGppaeqEoA7TS17IGAnCMYjsI8QinyGLTI8uCQHP'

            session = OAuth1Session(API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

            url = "https://api.twitter.com/1.1/search/tweets.json?lang=pt&q=" + search_word + "&count=30&tweet_mode=extended"

            response = session.get(url)

            tweets = json.loads(response.content.decode('utf-8'))

            #armazena os dados dos usuarios
            user_data = []
            #armazena os tweets dos usuários para posterior classificação
            user_tweets = []

            for t in tweets['statuses']:
                #converte a data para o timezone do Brasil
                d = datetime.strptime(t['created_at'],'%a %b %d %H:%M:%S %z %Y').replace(tzinfo = timezone.utc).astimezone(pytz.timezone('America/Sao_Paulo')).strftime('%Y-%m-%d %H:%M:%S')
                data = {
                    "data": d,
                    "username": t['user']['screen_name'],
                    "tweet_id": t['id'],
                    "tweet": t['full_text']
                }
                user_data.append(data)
                user_tweets.append(t['full_text'])

            #carrega o modelo gravado em arquivo
            text_clf = pickle.load(open(settings.MEDIA_ROOT + "/model.sav", 'rb'))

            #classifica os tweets
            predicted = text_clf.predict(user_tweets)
            
            #salva o termo de busca
            search = Search()
            search.expression = expression
            search.save()

            for x in range(len(predicted)):
                user_model = Tweet()
                user_model.user = user_data[x]['username']
                user_model.tweet_date = user_data[x]['data']
                user_model.tweet_id = user_data[x]['tweet_id']
                user_model.tweet_text = user_data[x]['tweet']
                user_model.classification = predicted[x]
                user_model.search = search
                user_model.save()


        else:
            print("não")

        return Tweet.objects.filter(search = search)
        