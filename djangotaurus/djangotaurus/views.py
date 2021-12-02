from django.shortcuts import render


def home(request):
    if request.method = "POST":
	user_input = str(request.POST['search'])
	return render(request,'login.html',{'user_input':user_input});
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html',{'user_input':""})


def register(request):
    return render(request, 'register.html')
