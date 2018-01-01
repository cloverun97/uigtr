from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# from allauth.account.signals import user_signed_up

PKU = '0'
BKN = '1'
DUR = '2'
DUM = '3'
PKK = '4'

st_bayar = {
	'0': 'Belum dibayar',
	'1': 'Dibayar',
	'2': 'Menunggu konfirmasi',
	'3': 'Lunas',
	'4': 'Ditolak',
	'5': 'Tidak dibayar'
	}

class Siswa(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
	nama = models.CharField(max_length=40)
	email = models.EmailField()
	asal_sekolah = models.CharField(max_length=40)

	def __str__(self):
		return self.nama

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
	if created:
		Siswa.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
	instance.siswa.save()

# @receiver(user_signed_up, dispatch_uid="some.unique.string.id.for.allauth.user_signed_up")
# def user_signed_up_(request, user, **kwargs):
# 	print(">>>>>>> BARU DAFTAR?", request, user)
    # user signed up now send email
    # send email part - do your self

def upload_location(instance, filename):
	return "%s/%s" %(instance.siswa.email, filename)

class Tiket(models.Model):
	STATUS_PEMBAYARAN_CHOICES = (
		('0', 'Belum dibayar'),
		('1', 'Dibayar'),
		('2', 'Menunggu konfirmasi'),
		('3', 'Lunas'),
		('4', 'Ditolak'),
		('5', 'Tidak dibayar')
	)

	LOKASI_TO_CHOICES = (
		(PKU, 'Pekanbaru'),
		(BKN, 'Bangkinang'),
		(DUR, 'Duri'),
		(DUM, 'Dumai'),
		(PKK, 'Pangkalan Kerinci'),
	)
	status_pembayaran = models.CharField(max_length=1, choices=STATUS_PEMBAYARAN_CHOICES, default='0')
	jumlah_tiket_ipa = models.IntegerField(default=0)
	jumlah_tiket_ips = models.IntegerField(default=0)
	lokasi_TO = models.CharField(max_length=1, choices=LOKASI_TO_CHOICES, default=PKU)
	bukti_pembayaran = models.ImageField(upload_to=upload_location, null=True, blank=True)
	created_time = models.DateTimeField()
	time_remaining = models.DateTimeField()
	siswa = models.ForeignKey(Siswa, on_delete=models.CASCADE, related_name='tikets')
	qr_code_image = models.ImageField(blank=True, null=True)

	def __str__(self):
		return self.siswa.nama + " ==> " + st_bayar[self.status_pembayaran]

	class Meta:
		ordering = ["-created_time", "-status_pembayaran"]