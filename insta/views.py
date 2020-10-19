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

@login_required(login_url='/login')
def profile(request):
    current_user = request.user

    if request.method == 'POST':
        form = ProfileForm(request.POST,request.FILES)
        if form.is_valid():
            profile =form.save(commit=False)
            profile.user = current_user
            profile.save()
    else:
        form=ProfileForm()

    return render(request, 'profile/new_profile.html', locals())

@login_required(login_url='/accounts/login/')
def view_profile(request,id):
    searched_user=User.objects.filter(id=id).first()
    profile = searched_user
    details = Profile.get_profile_by_id(id)
    images = Image.get_images_on_profile(id)

    users = User.objects.get(id=id)
    followers = len(Follow.objects.followers(users))
    following = len(Follow.objects.following(users))
    app_users=User.objects.all()
    guys_following=Follow.objects.following(request.user)

    return render(request,'profile/user_profile.html',locals())


@login_required(login_url='/accounts/login/')
def search_user(request):
    """
    Function that searches for profiles based on the usernames
    """
    if 'username' in request.GET and request.GET["username"]:
        name = request.GET.get("username")
        searched_profiles = User.objects.filter(username__icontains=name)
        message = f"{name}"
        profiles = User.objects.all()
        people = Follow.objects.following(request.user)
        print(profiles)
        return render(request, 'search.html', {"message":message, "usernames":searched_profiles, "profiles":profiles,})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html', {"message":message})
