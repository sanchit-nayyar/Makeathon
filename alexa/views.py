from django.shortcuts import render

# Create your views here.

def home(request):
	if request.method == 'POST':
		print(len(request.POST['img']))
		f = open('test.jpg', 'w')
		f.write(request.POST['img'])
		f.close()
	return render(request, 'alexa/index.html', {})