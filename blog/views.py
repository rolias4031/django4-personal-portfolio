from django.shortcuts import render, get_object_or_404
from .models import BlogProject

# Create your views here.
def all_blogs(request):

    blog_project = BlogProject.objects.all()

    return render(request, 'blog/all_blogs.html', {'blog_project':blog_project})

def detail(request, blog_id):

    """
    takes a blog_id parameter that is then used by get_object_or_404() to grab that particular blog only. this is how we generalize the blog page instead of having to create a path for each new blog post. returns a 404 page if a blog with that id doesn't exist.
    """

    blog = get_object_or_404(BlogProject, pk=blog_id)

    return render(request, 'blog/detail.html', {'blog':blog})
