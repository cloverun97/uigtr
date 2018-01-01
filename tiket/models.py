from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# from allauth.account.signals import user_signed_up

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
	return "%s/%s" %(instance.id, filename)



class Tiket(models.Model):
	STATUS_PEMBAYARAN_CHOICES = (
		('0', 'Belum lunas'),
		('1', 'Menunggu konfirmasi'),
		('2', 'Lunas'),
		('3', 'Ditolak'),
	)

	LOKASI_TO_CHOICES = (
		('0', 'Pekanbaru'),
		('1', 'Bangkinang'),
		('2', 'Duri'),
		('3', 'Dumai'),
		('4', 'Pangkalan Kerinci'),
	)
	status_pembayaran = models.CharField(max_length=1, choices=STATUS_PEMBAYARAN_CHOICES)
	jumlah_tiket_ipa = models.IntegerField(default=0)
	jumlah_tiket_ips = models.IntegerField(default=0)
	lokasi_TO = models.CharField(max_length=1, choices=LOKASI_TO_CHOICES)
	bukti_pembayaran = models.ImageField(upload_to=upload_location,
		null = True,
		blank=True,
		width_field = "width_field",
		height_field = "height_field")
	height_field = models.IntegerField(default=0, blank=True)
	width_field = models.IntegerField(default=0, blank=True)
	created_time = models.DateTimeField()
	time_remaining = models.DateTimeField()
	siswa = models.ForeignKey(Siswa, on_delete=models.CASCADE, related_name='tikets')
	
	class Meta:
		ordering = ["-created_time", "-status_pembayaran"]