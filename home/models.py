from django.db import models


def upload_location(instance, filename):
	return "%s/%s" %(instance.id, filename)

class Siswa(models.Model):
	nama = models.CharField(max_length=40)
	email = models.EmailField()
	asal_sekolah = models.CharField(max_length=40)

	def __str__(self):
		return self.nama

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
		('4', 'Pangkalan kerinci'),
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
	height_field = models.IntegerField(default=0)
	width_field = models.IntegerField(default=0)
	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)


	class Meta:
		ordering = ["-timestamp", "-status_pembayaran"]