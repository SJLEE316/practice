from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Comment
from django.contrib.auth.decorators import login_required

@login_required

def new(request):
    return render(request, 'posts/new.html')
    
def create(request):
    if request.method == "POST":
        title = request.POST.get('title')
        writer = request.user
        content = request.POST.get('content')
        mediafile = request.FILES.get('mediafile')
        category = request.POST.get('category')
        mediatype = mediafile.content_type
        Post.objects.create(title=title, content=content, mediafile=mediafile, writer=writer, category=category, mediatype=mediatype)
        return redirect('posts:gallery')

def main(request):
    posts = Post.objects.all()
    return render(request, 'posts/main.html', {'posts':posts})

def show(request, id):
    post = Post.objects.get(pk=id)
    A = post.view_count
    A = A + 1
    post.view_count = A
    post.save() 
    all_comments = post.comments.all().order_by('-created_at')
    return render(request, 'posts/show.html', {'post': post, 'comments': all_comments})

def update(request,id):
    post = get_object_or_404(Post,pk=id)
    if request.method == "POST":
        post.title = request.POST['title']
        post.content = request.POST['content']
        post.image = request.FILES.get('image')
        post.save()
        return redirect('main')
    return render(request,'posts/update.html',{'post':post})


def delete(request, id): 
	post = get_object_or_404(Post, pk=id) 
	post.delete()
	return redirect("posts:main")


def create_comment(request, post_id):
    if request.method == "POST":
        post = get_object_or_404(Post, pk=post_id)
        current_user = request.user
        comment_content = request.POST.get('content')
        Comment.objects.create(content=comment_content, writer=current_user, post=post)
    return redirect('posts:show', post.pk)


def post_like(request, post_id):
    post = get_object_or_404(Post, pk=post_id)

    if request.user in post.like_user_set.all():
        post.like_user_set.removed(request.user)
    else:
        post.like_user_set.add(request.user)

    if request.GET.get('redirect_to')=='show':
        return redirect('posts:show', post_id)
    else:
        return redirect('posts:main')


@login_required
def like_list(request):
    likes = request.user.like_set.all()
    return render(request,'posts/like_list.html',{'likes':likes})

def gallery(request):
    posts = Post.objects.all()
    # post = request.GET.get('sort','')

    # if sort == 'latest':
    #     posts = Post.objects.order_by('-created_at')
    #     return render(request, 'posts/gallery.html', {'posts':posts})
    
    # else:
    #     posts = Post.objects.order_by('-created_at')
    #     return render(request, 'posts/gallery.html', {'posts':posts})


    return render(request, 'posts/gallery.html', {'posts':posts})

def about(request):
    return render(request, 'posts/about.html')    