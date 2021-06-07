from django.shortcuts import render,get_object_or_404
from .models import Post
from real.models import Product
# Create your views here.





def blog(request):
    sale = Product.objects.filter(category__name__icontains='Satılık')
    blog = Post.objects.order_by('-id')

    context = {
        'blog':blog,
        'sale':sale
    }
    return render(request,'history/blog_list.html',context)

def blog_detail(request,slug):
    product = get_object_or_404(Post, slug=slug)


    context={
        'product':product
    }
    return render(request,'history/blog_detail.html',context)



