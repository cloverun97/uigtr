from django.conf.urls import url
from .views import index, beli_tiket, add_form, bayar, transfer, upload_bukti, tunggu_konfirmasi, status
#url for app
urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^beli/', beli_tiket, name='beli_tiket'),
    url(r'^add_form/', add_form, name='add_form'),
    url(r'^bayar/', bayar, name='bayar'),
    url(r'^transfer/', transfer, name='transfer'),
    url(r'^upload_bukti/', upload_bukti, name='upload_bukti'),
    url(r'^tunggu_konfirmasi/', tunggu_konfirmasi, name='tunggu_konfirmasi'),
    url(r'^status/', status, name='status'),
]
