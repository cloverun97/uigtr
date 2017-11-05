from django.shortcuts import render

#TODO Implement
#Create a content paragraph for your landing page:
landing_page_content = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur sollicitudin lacus vitae tortor consequat, vel ultricies nulla placerat. Sed vel suscipit arcu. Pellentesque et dolor ex. Donec blandit tortor at urna vestibulum luctus. Mauris tempus odio id dolor consectetur interdum. Vivamus id sem leo. Quisque at tincidunt odio.'
mhs_name = 'rehan'
def index(request):
    response = {'name': mhs_name, 'content': landing_page_content}
    return render(request, 'home/index.html', response)