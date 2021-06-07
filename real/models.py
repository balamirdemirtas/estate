from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.urls import reverse
from embed_video.fields import EmbedVideoField


class Agent(models.Model):
    name = models.CharField(max_length=50, blank=True)
    position  = models.CharField(max_length=50, blank=True)
    email = models.CharField(max_length=50, blank=True)
    telephone = models.CharField(max_length=50, blank=True)
    instagram = models.CharField(max_length=50, blank=True)
    facebook= models.CharField(max_length=50, blank=True)
    image = models.ImageField(upload_to='products/%y/%m/%d', blank=True)


    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=20, db_index=True)
    slug = models.SlugField(max_length=20, db_index=True, unique=True)



    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product_list_by_show', args=[self.slug])

class City(models.Model):

    name =  models.CharField(max_length=200, db_index=True,default='Şehir')


    def __str__(self):
        return self.name

class Available(models.Model):


    durum = models.CharField(max_length=200, db_index=True,default='Durum')

    def __str__(self):
        return self.durum

class Room(models.Model):

    position = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=20, db_index=True, unique=True)
    def __str__(self):
        return self.position


class Product(models.Model):
    status = models.BooleanField(default=True)
    category = models.ForeignKey(Category, related_name='Category', on_delete=models.CASCADE)
    city = models.ForeignKey(City, related_name='City', on_delete = models.CASCADE)
    available = models.ManyToManyField(Available, blank=True, default=None,related_name='Available')
    room = models.ForeignKey(Room, related_name='City', on_delete = models.CASCADE,verbose_name='Type')
    name = models.CharField(max_length=200, db_index=True,default='Proje İsmi')
    slug = models.SlugField(max_length=200, db_index=True)
    adress = models.CharField(max_length=200, db_index=True,default='Proje Adresi')
    price = models.CharField(max_length=200, db_index=True,default='Fiyatı')
    m2 = models.CharField(max_length=200, db_index=True,default='m2')
    bedroom = models.CharField(max_length=200, db_index=True,default='İnformation')
    shower = models.CharField(max_length=200, db_index=True,default='3')
    garage = models.CharField(max_length=200, db_index=True,default='1')
    image = models.ImageField(upload_to='products/%y/%m/%d', blank=True)
    manager = models.ImageField(upload_to='products/%y/%m/%d', blank=True)
    managername = models.CharField(max_length=200, db_index=True,default='İnformation')
    info = RichTextUploadingField()
    plans = models.ImageField(upload_to='products/%y/%m/%d', blank=True)
    yearofproduction = models.CharField(max_length=200, db_index=True,default='İnformation')
    hospital = models.CharField(max_length=200, db_index=True,default='İnformation')
    scholl = models.CharField(max_length=200, db_index=True,default='İnformation')
    market = models.CharField(max_length=200, db_index=True,default='İnformation')
    center = models.CharField(max_length=200, db_index=True,default='İnformation')
    sea = models.CharField(max_length=200, db_index=True,default='İnformation')
    highway = models.CharField(max_length=200, db_index=True,default='İnformation')
    video = EmbedVideoField()



    def __str__(self):
        return self.name



    def get_absolute_url(self):
        return reverse('real:product_detail', args=[self.slug, self.id])

class Images(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    title = models.CharField(max_length=50,blank=True)
    image = models.ImageField(blank=True, upload_to='images/')

    def __str__(self):
        return self.title




class Comment(models.Model):
    name = models.CharField(max_length=50, blank=True)
    job = models.CharField(max_length=50, blank=True)
    image = models.ImageField(blank=True, upload_to='images/')
    text = models.TextField(max_length=263, default='Ürün Aaçıklama 263 Ten az 263 çok olmuyacak')


    def __str__(self):
        return self.name



class Certificate(models.Model):
    image = models.ImageField(upload_to='products/%y/%m/%d', blank=True)
    name = models.CharField(max_length=200, db_index=True, default='Marka İsmi Giriniz', verbose_name='İsim')

    def __str__(self):
        return self.name



class About(models.Model):
    keyword = models.CharField(max_length=200, db_index=True,default='İnformation')
    image = models.ImageField(upload_to='products/%y/%m/%d', blank=True)
    info = RichTextUploadingField()



    def __str__(self):
        return self.keyword
