from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Image,Profile,Likes,Comments
from django.contrib.auth import login, authenticate
from .forms import SignupForm,ImageForm,CommentForm,ProfileForm
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMessage
from django.contrib.auth.models import User
from friendship.models import Friend, Follow, Block


@login_required(login_url='/accounts/login/')
def index(request):
    # profile = UserProfile.objects.create(user=request.user)
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
             (print(dir(variable)) 
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


def comment(request,image_id):
    current_user=request.user
    image = Image.objects.get(id=image_id)
    profile_user = User.objects.get(username=current_user)
    the_comments = Comments.objects.all()
    print(the_comments)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment_itself = form.save(commit=False)
            comment_itself.image = image
            comment_itself.commenter = request.user

            comment_itself.save()

            print(the_comments)


        return redirect(index)

    else:
        form = CommentForm()

    return render(request, 'comment.html', locals())

@login_required(login_url='/accounts/login/')
def follow(request,user_id):
    users = User.objects.get(id = user_id)
    follow = Follow.objects.add_follower(request.user,users)

    return redirect('indexpage')

@login_required(login_url='/accounts/login/')
def unfollow(request,user_id):
    users = User.objects.get(id = user_id)

    follow = Follow.objects.remove_follower(request.user,users)

    return redirect('indexpage')


def like(request, image_id):
    current_user = request.user
    liked_image=Image.objects.get(id=image_id)
    new_like,created= Likes.objects.get_or_create(who_liked=current_user, liked_aimage=liked_image)
    new_like.save()

    return redirect('indexpage')
