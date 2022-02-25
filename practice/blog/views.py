from django.shortcuts import render,redirect,get_object_or_404
from .models import UserProfile
from .forms import PostForm
from django.shortcuts import get_object_or_404


# Create your views here.
# def index(request):
 #    return render(request,'index1.html')

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            print(post)
            return redirect('post_all_detail')
    else:
        form = PostForm()
    return render(request, 'index_post.html', {'form': form})

def get_user(request):
    user = UserProfile.objects.all()
    print(user)
    data = { 'user' : user}
    print(data)
    return render(request, 'index_get.html', data)


def post_edit(request, pk):
    post = get_object_or_404(UserProfile,id=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('post_detail',pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'index_post.html', {'form': form})



def get_post_user(request,pk):
    user = UserProfile.objects.filter(id=pk)
    print(user)
    data = { 'user' : user}
    print(data['user'])
    return render(request,'view_by_id.html',data)