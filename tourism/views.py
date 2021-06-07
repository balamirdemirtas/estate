from django.db.models import Q
from django.shortcuts import render,get_object_or_404
from tourism.models import City,Room,Product,Category,Agent,Images




def tourism_list(request):
    city = City.objects.all()
    room = Room.objects.all()
    products = Product.objects.all()
    return render(request,'otel/tourism_list.html',{'products':products,'city':city,'room':room})



def show_tourism(request,category_slug = None):
    city = City.objects.all()
    room = Room.objects.all()
    products = Product.objects.filter(status=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
        print(products)
    return render(request,'otel/show_tourism.html',{'products':products,'room':room,'city':city})



def filter(request):
    a = City.objects.all()
    room = Room.objects.all()
    position = request.GET.get('position')
    available = request.GET.get('available')
    city = request.GET.get('city')



    articles = Product.objects.filter(Q(room__slug__icontains=position)&Q(available__durum__icontains=available)&Q(city__name__icontains=city))

    print(articles)
    return render(request,'otel/filter.html',{'articles':articles,'a':a,'room':room})


def detail(request,slug,id):
    agent = Agent.objects.all()[0:2]
    product = get_object_or_404(Product, slug=slug, id=id)
    images = Images.objects.filter(product_id=id)


    context= {
        'product':product,
        'images':images,
        'agent':agent
    }
    return render(request,'otel/tourism_detail.html',context)