from django.shortcuts import render

def confused(request):
	context = {
	"msg": "Hello World!",
	}
	return render(request, 'cool.html', context)
