from django.shortcuts import render

#TODO Implement
#Create a content paragraph for your landing page:
landing_page_content = 'Selamat datang di website UIGTR !'
mhs_name = 'rehan'
def index(request):
    response = {'name': mhs_name, 'content': landing_page_content}
    return render(request, 'home/index.html', response)

# def upload_bukti_pembayaran(request, id=None):
# 	instance = get_object_or_404(Post, id=id)
# 	form = PostForm(request.POST or None, request.FILES or None, instance = instance)
# 	if form.is_valid():
# 		instance = form.save(commit=False)
# 		instance.save()
# 		message.success = 