"""tcc URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static
from tweet import views
from tweet.api.viewsets import TweetViewSet, SearchViewSet

router = routers.DefaultRouter()
router.register(r'tweets', TweetViewSet, base_name='Tweets')
router.register(r'buscas', SearchViewSet, base_name='buscas')

urlpatterns = [
    url('', include(router.urls)),
    url(r'^admin/', admin.site.urls),
    url(r'^classificacao/', include('tweet.urls', namespace='principal')),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)