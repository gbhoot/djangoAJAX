from django.shortcuts import render
from .forms import RegisterForm

# Create your views here.
def index(request):
    form = RegisterForm()
    data = {
        'regForm'   :   form
    }

    return render(request, 'index.html', data)