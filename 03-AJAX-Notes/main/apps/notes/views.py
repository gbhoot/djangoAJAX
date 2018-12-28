from django.shortcuts import render, redirect
from .forms import PostForm
from .models import Post

# Create your views here.
def index(request):
    form = PostForm
    print(Post.objects.all())

    data = {
        'form'  :   form,
        'notes' :   Post.objects.all(),
    }

    return render(request, 'index.html', data)

def newPost(request):
    print(request.POST)

    if request.method == 'POST':
        new_form_post = PostForm(request.POST)
        print(new_form_post.is_valid())
        print(new_form_post.errors)
        new_post = new_form_post.save()
        new_post.save()
    
    return redirect('/')