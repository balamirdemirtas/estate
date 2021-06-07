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
        return reverse('land_product_list_by_show', args=[self.slug])

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
    image = models.ImageField(upload_to='products/%y/%m/%d', blank=True)
    manager = models.ImageField(upload_to='products/%y/%m/%d', blank=True)
    managername = models.CharField(max_length=200, db_index=True, default='İnformation')
    info = RichTextUploadingField()
    plans = models.ImageField(upload_to='products/%y/%m/%d', blank=True)
    price = models.CharField(max_length=200, db_index=True,default='Fiyatı',verbose_name='Fiyat')
    star = models.CharField(max_length=200, db_index=True,default='Yıldız Sayısı',verbose_name='Yılsız Sayısı')
    oda = models.CharField(max_length=200, db_index=True,default='Oda Sayısı',verbose_name='Oda Sayısı')
    yatak = models.CharField(max_length=200, db_index=True,default='Yatak Sayısı',verbose_name='Yatak Sayısı')
    kat = models.CharField(max_length=200, db_index=True,default='Kat Sayısı',verbose_name='Kat Sayısı')
    binaYas = models.CharField(max_length=200, db_index=True,default='Bina Yaşı',verbose_name='Bina Yaşı')
    openm2 = models.CharField(max_length=200, db_index=True,default='Açık M2',verbose_name='Açık Me2')
    closem2 = models.CharField(max_length=200, db_index=True,default='Kapalı M2',verbose_name='Kapalı M2')
    kredi = models.CharField(max_length=200, db_index=True,default='Kredi Uygunluk',verbose_name='Kredi')
    yapiDurumu = models.CharField(max_length=200, db_index=True,default='Yapı Durumu',verbose_name='Yapı Durumu')
    airport = models.CharField(max_length=200, db_index=True,default='Hava Alanına Uzaklık')
    anayol = models.CharField(max_length=200, db_index=True,default='Anayola Uzaklık')
    center = models.CharField(max_length=200, db_index=True,default='Merkeze Uzaklık')
    sea = models.CharField(max_length=200, db_index=True,default='Denize Uzaklık')
    video = EmbedVideoField()



    def __str__(self):
        return self.name



    def get_absolute_url(self):
        return reverse('tourism:product_detail', args=[self.slug, self.id])

class Images(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    title = models.CharField(max_length=50,blank=True)
    image = models.ImageField(blank=True, upload_to='images/')

    def __str__(self):
        return self.title




