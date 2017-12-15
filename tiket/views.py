from django.shortcuts import render

def index(request):
	html = 'tiket/form_tiket.html'
	response = {}
	return render(request, html, response)