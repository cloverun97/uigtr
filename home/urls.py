from django.conf.urls import url
from .views import index
#url for app
urlpatterns = [
    url(r'^$', index, name='index'),
]

handler404 = 'tiket.views.handler404'
handler500 = 'tiket.views.handler500'