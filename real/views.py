from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from .models import Product, Category, Room, Agent, Comment, City, Images,Certificate,About
from django.db.models import Min,Max

# Create your views here.




def index(request):
    city = City.objects.all()
    room = Room.objects.all()
    sell = Product.objects.filter(category__slug__icontains='satilik')
    sold = Product.objects.filter(category__slug__icontains='satildi')
    agents = Agent.objects.all()[0:2]
    comments = Comment.objects.all()
    context = {
        'sell':sell,
        'sold':sold,
        'agents':agents,
        'comments':comments,
        'room':room,
        'city':city
    }

    return render(request,'central/index.html',context)


def show(request,category_slug = None):
    city = City.objects.all()
    room = Room.objects.all()
    products = Product.objects.filter(status=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        print("category", category)
        products = products.filter(category=category)
    return render(request,'central/show.html',{'products':products,'room':room,'city':city})

def filter(request):
    a = City.objects.all()
    room = Room.objects.all()
    position = request.GET.get('position')
    available = request.GET.get('available')
    city = request.GET.get('city')



    articles = Product.objects.filter(Q(room__slug__icontains=position)&Q(available__durum__icontains=available)&Q(city__name__icontains=city))


    return render(request,'central/filter.html',{'articles':articles,'a':a,'room':room})


def detail(request,slug,id):
    agent = Agent.objects.all()[0:2]
    product = get_object_or_404(Product, slug=slug, id=id)
    images = Images.objects.filter(product_id=id)


    context= {
        'product':product,
        'images':images,
        'agent':agent
    }
    return render(request,'central/detail.html',context)


def about(request):
    info = About.objects.all()
    return render(request, 'central/about.html',{'info':info})


def contact(request):
    return render(request,'central/contact.html')


def team(request):
    agent = Agent.objects.all()
    return render(request,'central/team.html',{'agent':agent})


def documents(request):
    story = Certificate.objects.all()
    return render(request,'central/certificate.html',{'story':story})