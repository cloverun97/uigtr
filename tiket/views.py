from django.shortcuts import render

def index(request):
	html = 'tiket/tiket.html'
	response = {}
	return render(request, html, response)

def beli_tiket(request):
	html = 'tiket/form_tiket.html'
	response = {}
	return render(request, html, response)
