from django.shortcuts import render
# from django import HttpReponse
from .models import Image,Profile
from django.contrib.auth import login
# Create your views here.





@login_required(login_url='/accounts/login/')
def index(request):
    current_user = request.user
    images = Image.objects.all()
    comments = Comments.objects.all()
    likes = Likes.objects.all
    people = Follow.objects.following(request.user)
    profile = User.objects.all()
    return render(request,'index.html',locals())



@login_required(login_url='accounts/login/')
def add_new_image(request):
    current_user = request.user
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            add=form.save(commit=False)
            add.profile = current_user
            add.save()
            return redirect('indexpage')
    else:
        form = ImageForm()


    return render(request,'post.html',locals())