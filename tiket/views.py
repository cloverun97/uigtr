from django.shortcuts import render
from django.http import HttpResponseRedirect
from uigtr.settings import SAVE_DIRECTORY
import qrcode
from django.core.validators import validate_email
from datetime import datetime, timedelta
from .models import Siswa, Tiket
from django.contrib.auth.models import User
from django.urls import reverse

def index(request):
	html = 'tiket/tiket.html'
	response = {}
	return render(request, html, response)

def beli_tiket(request):
	response = {}
	html = 'tiket/form_tiket.html'
	return render(request, html, response)

def status(request):
	if 'user_email' in request.COOKIES:
		html = 'tiket/status.html'
		response = {}


		file_name = generate_file_name("rehan hawari", "SMA N 1 Pasir Penyu", 2, 9)
		generate_qrcode("rehan hawari SMA N 1 Pasir Penyu", file_name)

		f()
		return render(request, html, response)
	else :
		print("===>>>> COBA KE STATUS, LINK BERUBAH GA?")
		return HttpResponseRedirect('/tiket/beli')

def upload_bukti(request):
	if 'user_email' in request.COOKIES:
		html = 'tiket/upload_bukti.html'
		return render(request, html, response)
	else :
		print("===>>>> COBA UPLOAD BUKTI W/O COOKIES, LINK BERUBAH GA?")
		return HttpResponseRedirect('/tiket/beli')

def bayar(request):
	if 'user_email' in request.COOKIES:
		delta_time = request.COOKIES.get('time_remaining') - datetime.now()
		res = {}
		res["time_remaining"] = delta_time.seconds / 60 #sisa waktu
		html = 'tiket/bayar_tiket.html'
		return render(request, html, res)
	else :
		print("==>>> COBA MASUK BAYAR TANPA COOKIE. LINK GIMANA YA?")
		response = HttpResponseRedirect(reverse('tiket:beli_tiket'))
		return response

def add_form(request):
	if (request.method == 'POST'):
		if (is_valid_form(request)):
			lst = parsing_request(request)
			nama = lst[0]
			email = lst[1]
			sekolah = lst[2]
			lokasi_to = lst[3]
			tiket_ipa = lst[4]
			tiket_ips = lst[5]

			# cek siswa
			try:
				print("==>>>>>>>>> try cek siswa")
				print(request.user)
				# print(request.user.siswa)
				current_siswa = User.objects.get(email=email)
			except User.DoesNotExist:
				# print("masuk sini ga sih") 
				# MASUK PERTAMA KALI
				current_siswa = None
			
			if current_siswa == None:
				new_password = User.objects.make_random_password()
				user = User.objects.create_user(username=nama, email=email, password=new_password)
				user.save()
				siswa = Siswa(user=user, nama=nama, email=email, asal_sekolah=sekolah)
				siswa.save()
				print(siswa)
				print("^^^^")
			else:
				siswa = current_siswa.siswa

			tiket = Tiket(status_pembayaran = 'Belum lunas', jumlah_tiket_ipa = tiket_ipa, jumlah_tiket_ips = tiket_ips,\
					lokasi_TO = lokasi_to, created_time = datetime.now(),  time_remaining = datetime.now() + timedelta(minutes = 30), siswa = siswa)
			tiket.save()

			
			response = HttpResponseRedirect(reverse('tiket:bayar'))
			response.set_cookie('user_email', email)
			response.set_cookie('time_remaining', tiket.time_remaining)
			return response
		else:
			print(">>>>> FORM TIDAK VALID :P")
			return HttpResponseRedirect('/tiket/beli')
	else:
		print("===>>>> COBA GET ADD FORM, LINK BERUBAH GA?")
		return HttpResponseRedirect('/tiket/beli')

def is_valid_form(request):
	lst = parsing_request(request)
	nama = lst[0]
	email = lst[1]
	sekolah = lst[2]
	lokasi_to = lst[3]
	tiket_ipa = lst[4]
	tiket_ips = lst[5]
	# print(nama, (0 < len(nama) <= 40))
	# print(email, is_email_valid(email))
	# print(sekolah, (0 < len(sekolah) <= 40))
	# print(tiket_ipa, (is_int(tiket_ipa)))
	# print(tiket_ips, (is_int(tiket_ips)))
	return ( (0 < len(nama) <= 40) and is_email_valid(email) and (0 < len(sekolah) <= 40) and (is_int(tiket_ipa)) and (is_int(tiket_ips)) )

def is_email_valid(email):
	try:
		validate_email(email)
		return True
	except:
		return False

def parsing_request(request):
	lst = []
	lst.append(request.POST['user_name'])
	lst.append(request.POST['user_email'])
	lst.append(request.POST['user_school'])
	lst.append(request.POST['tryout_location'])
	lst.append(request.POST['tiket_ipa'])
	lst.append(request.POST['tiket_ips'])
	return lst

def is_int(num):
	try:
		int(num)
		return True
	except:
		return False

def create_qr_code(nama, sekolah, lokasi_TO, ipa, ips):
	print(">>>> CREATING QR CODE | BEFORE BUAT MESSAGE")
	message = '33'
		# ('4', 'Pangkalan kerinci'),

	# 21= PKL KERINCI
	if lokasi_TO == 0: #PEKANBARU
		message += '23'
	elif lokasi_TO == 1: #BANGKINANG
		message += '19'
	elif lokasi_TO == 2: #DURI
		message += '22'
	elif lokasi_TO == 3: #DUMAI
		message += '20'
	elif lokasi_TO == 4:
		message += '21'
	else :
		message += '00'

	message += '.'
	message += str(ipa + ips) #JMLAH TIKET
	new_ipa = modify_tiket(ipa)
	new_ips = modify_tiket(ips)
	message = message + new_ipa + new_ips
	message += '.331998' #GINA BDAY

	file_name = generate_file_name(nama, sekolah, ipa, ips)
	generate_qrcode(message, file_name)

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
	return img

def modify_tiket(n):
	if len(str(n)) == 2 :
		return str(n)
	elif len(str(n)) == 1:
		return '0' + str(n)
	else :
		return '_' + str(n)