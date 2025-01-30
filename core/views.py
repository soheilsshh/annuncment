from django.shortcuts import render , redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate , login
from .models import CustomUser, Post, Comment
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def home(request):
    search_query = request.GET.get('query')
    result = []
    if search_query:
        result = Post.objects.filter(title__icontains = search_query)
    
    
    post = Post.objects.all()
    
    context = {
        'user' : request.user,
        'post' : post,
        'results' : result
    }
    return render(request , 'home.html' , context)


def sign_in(request):  # this is function for login
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        if( not CustomUser.objects.filter(username = username).exists()):
            messages.error(request , 'invalid user')
            return redirect('/login/')
        
        user = authenticate(username = username , password = password)
        
        if(user is None):
            messages.error(request , 'invalid password')
            return redirect('/login/')
        else:
            login(request , user)
            return redirect('/home/')
        
    return render(request , 'login.html')

def sign_up(request):
    # this is function for registering user
    if request.method == 'POST':
        username = request.POST.get('username')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        pass1 = request.POST.get('password')
        pass2 = request.POST.get('confirm_password')
        
        if pass1 == pass2:
            myuser = CustomUser.objects.create_user(username , email , pass1)
            myuser.first_name = username
            myuser.last_name = lastname
            myuser.save()
            messages.success(request , "done!!!!!")
            return render(request , 'login.html')
            
    return render(request , 'sign_up.html')

@login_required
def post_detail(request , post_id):
    post = get_object_or_404(Post , id = post_id)
    comment = Comment.objects.filter(post = post).filter(comment = None).order_by('-date_posted')
    
    if request.method == 'POST':
        comment_text = request.POST.get('text')
        parent_id = request.POST.get('parent_id')

        comment = Comment(post=post, user=request.user, comment_text=comment_text)
        if parent_id:
            comment.comment_id = parent_id
        comment.save()
        return redirect('post_detail', post_id = post_id)
    
    context = {
        'ad' : post,
        'comments' : comment
        }

    return render(request, 'detail_post.html', context)


@login_required
def post_ad(request):
    if request.method == 'POST':
        
        title = request.POST['title']
        description = request.POST['description']
        
        if request.FILES.get('image'):
            image = request.FILES['image']
            post = Post.objects.create(
                 title = title,
                 description = description,
                 post_image = image,
                 customuser = request.user
             )
        else:
            post = Post.objects.create(
                 title = title,
                 description = description,
                 customuser = request.user
             )
            
        post.save()
        
        return redirect('/home/')
        
    return render(request , 'post_ad.html')


@login_required
def user_post(request):
    userpost = Post.objects.filter(customuser = request.user)
    context = {
        'user_posts' : userpost
    }

    return render(request , 'user_post.html' , context)


@login_required
def update_post(request , post_id):
    post = get_object_or_404(Post , id = post_id)
    
    context = {
        'ad' : post
    }
    
    if request.method == 'POST':
        post.title = request.POST['title']
        post.description = request.POST['description']
        
        if request.FILES.get('image'):
            post.post_image = request.FILES['image']
        
        post.save()
        return redirect('/home/')
    
    return render(request , 'update_post.html' , context)

        
@login_required
def delete_post(request , post_id):
    post = get_object_or_404(Post ,id = post_id )
    post.delete()
    return redirect('/home/')
