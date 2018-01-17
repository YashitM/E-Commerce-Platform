from django.shortcuts import render, redirect

def index(request):
    return render(request, 'main/index.html', {"custom_notifications": ""})


def login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':

            pass

        return render(request, 'main/login.html', context=None)
    else:
        return redirect('/')

