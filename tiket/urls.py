from django.conf.urls import url
from .views import index, beli_tiket
#url for app
urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^beli/', beli_tiket, name='beli_tiket'),
]
