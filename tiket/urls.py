from django.conf.urls import url
from .views import index, beli_tiket, status
#url for app
urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^beli/', beli_tiket, name='beli_tiket'),
    url(r'^status/', status, name='status'),
]
