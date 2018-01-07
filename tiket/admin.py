from django.contrib import admin
from .models import Siswa, Tiket
import urllib.parse

def jumlah_tiket_ipa(obj):
	return obj.jumlah_tiket_ipa
jumlah_tiket_ipa.short_description = 'IPA'

def jumlah_tiket_ips(obj):
	return obj.jumlah_tiket_ips
jumlah_tiket_ips.short_description = 'IPS'

def siswa_email(obj):
	return obj.siswa.email
siswa_email.short_description = 'EMAIL'

def siswa(obj):
	return obj.siswa
siswa.short_description = 'NAMA SISWA'

def url_bukti(obj):
	s = str(obj.bukti_pembayaran)
	print("==>>>> s :", s)
	url = get_url(s)
	print("==>>>> ", url)
	return '<a href="%s%s">%s</a>' % ('//localhost:8000/media/',url, obj.bukti_pembayaran)
url_bukti.allow_tags = True
url_bukti.short_description = 'Bukti pembayaran'

def get_url(the_url):
	return urllib.parse.quote(u"%s" % (the_url))

class SiswaAdmin(admin.ModelAdmin):
	list_display = ('nama', 'email', 'asal_sekolah')
	search_fields = ('email', 'nama', 'asal_sekolah')

class TiketAdmin(admin.ModelAdmin):
	list_display = (siswa, siswa_email, 'status_pembayaran', jumlah_tiket_ipa, jumlah_tiket_ips, url_bukti, 'created_time', 'time_remaining')
	list_filter = ('status_pembayaran', 'created_time', 'time_remaining')
	search_fields = ('siswa__nama', 'siswa__asal_sekolah','siswa__email', 'lokasi_TO')

admin.site.register(Siswa, SiswaAdmin)
admin.site.register(Tiket, TiketAdmin)