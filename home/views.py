from django.shortcuts import render

#TODO Implement
#Create a content paragraph for your landing page:
landing_page_content = 'Selamat datang di website UIGTR !'
mhs_name = 'rehan'
def index(request):
    response = {'name': mhs_name, 'content': landing_page_content}
    return render(request, 'home/index.html', response)
