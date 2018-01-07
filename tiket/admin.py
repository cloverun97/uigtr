from django.contrib import admin
from .models import Siswa, Tiket

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

class SiswaAdmin(admin.ModelAdmin):
    list_display = ('nama', 'email', 'asal_sekolah')
    search_fields = ('email', 'nama', 'asal_sekolah')

class TiketAdmin(admin.ModelAdmin):
    list_display = (siswa, siswa_email, 'status_pembayaran', jumlah_tiket_ipa, jumlah_tiket_ips,'created_time', 'time_remaining')
    list_filter = ('status_pembayaran', 'created_time', 'time_remaining')
    search_fields = ('siswa__nama', 'siswa__asal_sekolah','siswa__email', 'lokasi_TO')

admin.site.register(Siswa, SiswaAdmin)
admin.site.register(Tiket, TiketAdmin)