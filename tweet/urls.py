from django.conf.urls import url
from django.conf.urls import include
from tweet import views

urlpatterns = [    
    url(r'^$', views.search, name='index'),
    url(r'^classification/', views.classification, name='classification'),
]