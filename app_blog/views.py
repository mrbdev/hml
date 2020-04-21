from django.shortcuts import render, get_object_or_404

# Create your views here.
from .models import Post

def vw_PostsList(request):
    qs_AllPosts = Post.objects.all() #filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    myContex = {
        'all_posts': qs_AllPosts
    }
    return render(request, template_name, myContex)
    #return render(request, template_name, {})


def vw_PostDetail(request, prm_post_slug):
    template_name = 'post_detail.html'
    output_post = get_object_or_404(Post, post_slug=prm_post_slug)
    myContex = {
        'in_slug': prm_post_slug,
        'post4detail': output_post
    }
    return render(request, template_name, myContex)
