from django.shortcuts import render
from django.http import HttpResponse
from requests_oauthlib import OAuth1Session
from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from django.conf import settings
from tweet.models import Tweet, Search
from datetime import datetime, timezone
import numpy as np
import requests
import json
import pickle
import pytz
import numbers

def search(request):
    if(request.method == 'POST'):

        #codifica a expressão para o padrão utilizado na web
        expression = request.POST.get('expression')

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

    template = 'tweet/index.html'

    return render(request, template)

def classification(request):
    classificacao = ['positivo', 'negativo']
    categories = [] #array com a mesma função do twenty_train.target
    dataset = []

    with open(settings.MEDIA_ROOT + "/taspt-dataset.csv", 'r') as original_file:
        linha = original_file.readline().replace('\n', '')
        line_full = ""

        for line in original_file:
            #retira a quebra de linha
            line = line.replace('\n', '')
            id = None
            try:
                id = int(line[:1])
                line_full = line
                print(id)
            except ValueError:
                line_full += line
                print(id)
                continue
            
            #adiciona a linha no dataset e insere o indice na lista de classificação, 0 para positivo e 1 para negativo
            if(id):
                if(":)" in line_full):
                    categories.append(0)
                    #retira o emoticon da linha
                    line_full = line_full.replace(":)", "")
                    dataset.append(line_full)
                elif(":-)" in line_full):
                    categories.append(0)
                    line_full = line_full.replace(":-)", "")
                    dataset.append(line_full)
                elif(":(" in line_full):
                    categories.append(1)
                    line_full = line_full.replace(":(", "")
                    dataset.append(line_full)
                elif(":-(" in line_full):
                    categories.append(1)
                    line_full = line_full.replace(":-(", "")
                    dataset.append(line_full)
                """ if(id):
                    print("Não nulo")
                else:
                    print("None") """

    for x in range(20):
        print(dataset[x])

    array_np = np.array(categories)

    text_clf = Pipeline([('vect', CountVectorizer()),
        ('tfidf', TfidfTransformer()),
        ('clf', MultinomialNB()),
    ])

    """ for y in dataset:
        print(y) """

    text_clf.fit(dataset, array_np)

    pickle.dump(text_clf, open(settings.MEDIA_ROOT + "/model.sav", 'wb'))

    docs_new = ['O filme é divertido, mas o final estraga tudo', 'o filme todo é uma porcaria', 'Achei o programa muito chato', 'o filme me fez chorar', 'o filme me fez rir']

    predicted = text_clf.predict(docs_new)

    for doc, category in zip(docs_new, predicted):
        print('%r => %s' % (doc, classificacao[category]))
    
    return HttpResponse("Classificação realizada")
