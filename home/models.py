# from django.db import models

# class Tiket(models.Model):
# 	STATUS_PEMBAYARAN_CHOICES = (
#         ('0', 'Belum lunas'),
#         ('1', 'Menunggu konfirmasi'),
#         ('2', 'Lunas'),
#         ('3', 'Ditolak'),
#     )

#     LOKASI_TO_CHOICES = (
#     	('0', 'Pekanbaru'),
#     	('1', 'Bangkinang')
#     	('2', 'Duri'),
#     	('3', 'Dumai'),
#     	('4', 'Pangkalan kerinci')
#     )
# 	name = models.CharField(max_length=40)
# 	email = models.EmailField()
# 	asal_sekolah = models.CharField(max_length=40)
# 	status_pembayaran = models.CharField(max_length=1, choices=STATUS_PEMBAYARAN_CHOICES)
# 	jumlah_tiket = models.IntegerField()
# 	lokasi_TO = models.CharField(max_length=1, choices=LOKASI_TO_CHOICES)
# 	bukti_pembayaran = models.FileField()