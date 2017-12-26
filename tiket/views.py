from django.shortcuts import render
from uigtr.settings import SAVE_DIRECTORY
import qrcode

def index(request):
	html = 'tiket/tiket.html'
	response = {}
	return render(request, html, response)

def beli_tiket(request):
	response = {}
	if request.method == 'POST':
		if request.path == '/tiket/beli/upload':
			html = 'tiket/upload_bukti.html'
			return render(request, html, response)
		print(request)
		print("masuk kok")
		html = 'tiket/bayar_tiket.html'
		return render(request, html, response)
	html = 'tiket/form_tiket.html'
	return render(request, html, response)

def status(request):
	html = 'tiket/status.html'
	response = {}
	f()
	return render(request, html, response)

def f():
	file_name = generate_file_name("rehan hawari", "SMA N 1 Pasir Penyu", 2, 9)
	generate_qrcode("rehan hawari SMA N 1 Pasir Penyu", file_name)


def generate_qrcode(message, file_name):
	qr = qrcode.QRCode(
		version = 1,
		error_correction = qrcode.constants.ERROR_CORRECT_H,
		box_size = 10,
		border = 4,
	)
	data = message
	qr.add_data(data)
	qr.make(fit=True)
	img = qr.make_image()
	img.save(SAVE_DIRECTORY + file_name, 'PNG')

def generate_file_name(nama, sekolah, ipa, ips):
	# NAMA_NAMASEKOLAH_2IPA1IPS.png
	nama = nama.upper().replace(" ", "_")
	sekolah = sekolah.upper().replace(" ", "_")
	ekstensi = ".PNG"
	if ipa != 0 and ips != 0:
		return nama + "_" + sekolah + "_" + str(ipa) + "IPA" + str(ips) + "IPS" + ekstensi
	if ipa == 0:
		return nama + "_" + sekolah + "_" + str(ipa) + "IPA" + ekstensi
	return nama + "_" + sekolah + "_" + str(ips) + "IPS" + ekstensi
