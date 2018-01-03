from django.shortcuts import render
from django.http import HttpResponseRedirect
from uigtr.settings import SAVE_DIRECTORY
from django.core.validators import validate_email
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Siswa, Tiket
from datetime import datetime, timedelta
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from .forms import UploadFileForm
from io import StringIO, BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
import qrcode

status_pembayaran_choices = {'Belum dibayar' : '0' ,
							'Dibayar' : '1',
							'Menunggu konfirmasi' : '2' ,
							'Lunas' : '3',
							'Ditolak' : '4',
							'Tidak dibayar' : '5' }

st_pembayaran_lst = ['Belum dibayar', 'Dibayar', 'Menunggu konfirmasi', 'Lunas', 'Ditolak', 'Tidak dibayar']
lk_to_lst = ['Pekanbaru', 'Bangkinang', 'Duri', 'Dumai', 'Pangkalan Kerinci']

def index(request):
	html = 'tiket/tiket.html'
	response = {}
	return render(request, html, response)

def beli_tiket(request):
	if request.user.is_authenticated :
		siswa = request.user.siswa
		tiket = Tiket.objects.filter(siswa = siswa).reverse()[0]
		if tiket.status_pembayaran == status_pembayaran_choices['Belum dibayar']:
			return HttpResponseRedirect(reverse('tiket:bayar')) #TRANSFER
		elif tiket.status_pembayaran == status_pembayaran_choices['Dibayar']:
			return HttpResponseRedirect(reverse('tiket:upload_bukti')) #UPLOAD FOTO
	response = {}
	html = 'tiket/form_tiket.html'
	return render(request, html, response)

# ==> STEP 2 : ADD FORM 

def bayar(request):
	if request.user.is_authenticated :
		siswa = request.user.siswa
		tiket = Tiket.objects.filter(siswa = siswa).reverse()[0]
		if tiket.status_pembayaran == status_pembayaran_choices['Dibayar']:
			return HttpResponseRedirect(reverse('tiket:upload_bukti')) #UPLOAD FOTO
		else :
			siswa = request.user.siswa
			tiket = Tiket.objects.get(siswa=siswa)
			deadline = tiket.time_remaining.replace(tzinfo=None)
			if (deadline < datetime.now()):
				tiket.status_pembayaran = status_pembayaran_choices['Tidak dibayar']
				return HttpResponseRedirect(reverse('tiket:beli_tiket'))
			delta_time = deadline - datetime.now()
			res = {}
			res["time_remaining"] = delta_time.seconds / 60 #sisa waktu

			amount = calculate_amount(int(tiket.jumlah_tiket_ipa), int(tiket.jumlah_tiket_ips), int(tiket.lokasi_TO))
			res["amount"] = amount
			html = 'tiket/bayar_tiket.html'
			return render(request, html, res)
	else :
		print("==>>> COBA BAYAR TANPA LOGIN")
		response = HttpResponseRedirect(reverse('tiket:beli_tiket'))
		return response

# BUFFER
def transfer(request):
	if request.method == 'POST':
		if request.user.is_authenticated :
			siswa = request.user.siswa
			tiket = Tiket.objects.filter(siswa = siswa)
			try:
				tiket = tiket.reverse()[0]
			except :
				print("==> ERROR KARENA BACK, ")
				return HttpResponseRedirect(reverse('tiket:upload_bukti'))
			print('====> ',tiket.status_pembayaran)
			if tiket.status_pembayaran == status_pembayaran_choices['Dibayar']:
				return HttpResponseRedirect(reverse('tiket:upload_bukti')) #UPLOAD FOTO
			else:
				siswa = request.user.siswa
				semua_tiket = Tiket.objects.filter(siswa=siswa)
				current_tiket = semua_tiket.filter(status_pembayaran= status_pembayaran_choices['Belum dibayar']).reverse()[0]
				print(">>>>> current_tiket: ", current_tiket)
				current_tiket.status_pembayaran = status_pembayaran_choices['Dibayar']
				current_tiket.save()
				return HttpResponseRedirect(reverse('tiket:upload_bukti'))
		else :
			print("GA LOGIN :p")
			print("===>", request.user)
			return HttpResponseRedirect(reverse('tiket:beli_tiket'))
	else:
		print("GA BISA GET TRANSFER :p")
		return HttpResponseRedirect(reverse('tiket:beli_tiket'))

# SYSTEM BACK DONE, NOT HANDLED: FORWARD/ ACCESS BY URL
def upload_bukti(request):
	if request.user.is_authenticated :
		# form = UploadFileForm()
		response = {}
		# response['form'] = form
		html = 'tiket/upload_bukti.html'
		return render(request, html, response)
	else :
		print("===>>>> COBA UPLOAD BUKTI W/O LOGIN, LINK BERUBAH GA?")
		return HttpResponseRedirect('/tiket/beli')

# BUFFER
def tunggu_konfirmasi(request):
	# CEK IMAGE VALID ATAU ENGGA
	if request.method == 'POST':
		try:
			bukti_foto = request.FILES['bukti_foto']
			print(">>> bukti foto : ", type(bukti_foto))
			print(">>> bukti_foto nama = ", bukti_foto.name)
			if is_file_valid(bukti_foto.name) and request.user.is_authenticated:
				siswa = request.user.siswa
				tiket = Tiket.objects.filter(siswa=siswa).reverse()[0]

				print(">>>>> current_tiket: ", tiket)
				tiket.bukti_pembayaran.save(bukti_foto.name, bukti_foto)
				tiket.status_pembayaran = status_pembayaran_choices['Menunggu konfirmasi']
				tiket.save()
				return HttpResponseRedirect(reverse('tiket:status'))
			else : 
				print(">>>>>> ANONYMOUS USER")
				return HttpResponseRedirect('/tiket/beli')
		except :
			response = {}
			response['message'] = "Mohon pilih foto (format jpg, jpeg, gif) terlebih dahulu, kemudian tekan tombol upload."
			html = 'tiket/upload_bukti.html'
			return render(request, html, response)
	else:
		print(">>>>>> COBA UPLOAD BUKTI W/O LOGIN")
		return HttpResponseRedirect('/tiket/beli')


# LOGOUT
def status(request):
	response = {}
	html = 'tiket/status.html'
	if request.user.is_authenticated :
		siswa = request.user.siswa
		tiket = Tiket.objects.filter(siswa=siswa).reverse()[0]
		response['siswa'] = siswa
		response['tiket'] = tiket
		response['status_pembayaran'] = st_pembayaran_lst[ int(tiket.status_pembayaran) ]
		response['lokasi_to'] = lk_to_lst[ int(tiket.lokasi_TO) ]
		return render(request, html, response)
	else :
		print("===>>>> COBA KE STATUS, LINK BERUBAH GA?")
		return HttpResponseRedirect('/tiket/beli')

@login_required
def verif(request):
	if request.user.is_superuser and request.method == 'POST':
		email = request.POST['email']
		if create_qrcode_by_email(email):
			return HttpResponseRedirect('Success!')
		else :
			return HttpResponseRedirect('Error! Tanya Rehan')
	elif request.user.is_superuser:
		response = {}
		html = 'tiket/verif.html'
		return render(request, html, response)
	else :
		print("===>>>> BUKAN ADMIN GABOLEH MASUK :p")
		return HttpResponseRedirect('/tiket/beli')

def create_qrcode_by_email(email):
	try:
		siswa = User.objects.get(email=email).siswa
		tiket = Tiket.objects.filter(siswa=siswa).reverse()[0]

		nama = siswa.nama
		sekolah = siswa.asal_sekolah
		lokasi = int(tiket.lokasi_TO)
		ipa = int(tiket.jumlah_tiket_ipa)
		ips = int(tiket.jumlah_tiket_ips)

		message = qr_code_message(nama, sekolah, lokasi, ipa, ips)
		file_name = generate_file_name(nama, sekolah, ipa, ips)

		img = generate_qrcode(message, file_name)
		img_io = BytesIO()
		img.save(img_io, format='JPEG')
		image_file = InMemoryUploadedFile(img_io, None, file_name, 'image/jpeg', img_io.getbuffer().nbytes, None)
		print(">>>>> BERHASIL SAVE! image type : ", type(img))

		tiket.qr_code_image.save(file_name, image_file)
		tiket.save()
		return True
	except:
		return False


# BUFFER
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
				# print("==>>>>>>>>> try cek siswa")
				# print(request.user)
				# print(request.user.siswa)
				current_siswa = User.objects.get(email=email)
			except User.DoesNotExist:
				# print("masuk sini ga sih") 
				# MASUK PERTAMA KALI
				current_siswa = None
			
			if current_siswa == None:
				new_password = User.objects.make_random_password()
				new_user = User.objects.create_user(username=nama, email=email, password=new_password)
				new_user.save()
				siswa = Siswa(user=new_user, nama=nama, email=email, asal_sekolah=sekolah)
				siswa.save()
				
				# login
				user = authenticate(request, username=nama, email=email, password=new_password)
				if user is not None:
					login(request, user)
					print(">>>>>>>>> LOGGED IN")
					print(">>> ", user)
				else:
					print(">>>>>>>>> ERROR GABISA LOGIN")
					return HttpResponseRedirect('/tiket/beli')
			else:
				siswa = current_siswa.siswa

			tiket = Tiket(status_pembayaran = status_pembayaran_choices['Belum dibayar'], jumlah_tiket_ipa = tiket_ipa, jumlah_tiket_ips = tiket_ips,\
					lokasi_TO = lokasi_to, created_time = datetime.now(),  time_remaining = datetime.now() + timedelta(minutes = 30), siswa = siswa)
			tiket.save()
			return HttpResponseRedirect(reverse('tiket:bayar'))
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

def qr_code_message(nama, sekolah, lokasi_TO, ipa, ips):
	print(">>>> CREATING QR CODE | BEFORE BUAT MESSAGE")
	message = '33'

	if lokasi_TO == 0: #PEKANBARU
		message += '23'
	elif lokasi_TO == 1: #BANGKINANG
		message += '19'
	elif lokasi_TO == 2: #DURI
		message += '22'
	elif lokasi_TO == 3: #DUMAI
		message += '20'
	elif lokasi_TO == 4: #PKK
		message += '21'
	else :
		message += '00'

	message += '.'
	message += modify_tiket(str(ipa + ips)) #JMLAH TIKET
	new_ipa = modify_tiket(ipa)
	new_ips = modify_tiket(ips)
	message = message + new_ipa + new_ips
	message += '.331998' #GINA BDAY

	return message

	return generate_qrcode(message, file_name)

def generate_file_name(nama, sekolah, ipa, ips):
	# NAMA_NAMASEKOLAH_2IPA1IPS.png
	nama = nama.upper().replace(" ", "_")
	sekolah = sekolah.upper().replace(" ", "_")
	ekstensi = ".PNG"
	if ipa != 0 and ips != 0:
		return nama + "_" + sekolah + "_" + str(ipa) + "IPA" + str(ips) + "IPS" + ekstensi
	if ipa != 0:
		return nama + "_" + sekolah + "_" + str(ipa) + "IPA" + ekstensi
	if ips != 0:
		return nama + "_" + sekolah + "_" + str(ips) + "IPS" + ekstensi
	return nama + "_" + sekolah + "_" + '0' + "IPA" + '0' + 'IPS' + '_Cek_Database' + ekstensi

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
	return img

def modify_tiket(n):
	if len(str(n)) == 2 :
		return str(n)
	elif len(str(n)) == 1:
		return '0' + str(n)
	else :
		return '_' + str(n)

def is_file_valid(name):
	ekstensi = name.split(".")[-1]
	return ekstensi == 'jpeg' or ekstensi == 'jpg' or ekstensi == 'png'

def calculate_amount(ipa, ips, int_lokasi_TO):
	if int_lokasi_TO == 0:
		return 32000*(ipa+ips)
	else :
		return 30000*(ipa+ips)