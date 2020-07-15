from django.shortcuts import render
from django.views.generic import ListView, DetailView, UpdateView
from django.views.generic.edit import CreateView
from . models import Post

# Create your views here.

class BlogListView(ListView):
    model = Post
    template_name = 'blog/home.html'

class BlogDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'

class BlogCreateView(CreateView):
    model = Post
    template_name = 'blog/post_new.html'
    fields = ('title','slug', 'author', 'context')

class BlogUpdateView(UpdateView):
    model = Post
    template_name = 'blog/post_edit.html'
    fields = ('title', 'context')

    """
    STATUS  = (
        ('rascunho', 'Rascunho'),
        ('publicado', 'Publicado'),
    )
    title   = models.CharField(max_length=250)
    slug    = models.SlugField(max_length=250)
    author  = models.ForeignKey(User,
                                on_delete=models.CASCADE)
    context = models.TextField() 
    publicado= models.DateTimeField(default=timezone.now)
    criado  = models.DateTimeField(auto_now_add=True)
    alterado= models.DateTimeField(auto_now=True)
    status  = models.CharField(max_length=10,
                                choices=STATUS,
                                default='rascunhos')
    objects = models.Manager()
    published= PublishedManager()
    """
