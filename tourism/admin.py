from django.contrib import admin
from .models import City, Room, Available, Product, Images, Category, Agent




class Picture(admin.TabularInline):
    model = Images


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name','slug']
    prepopulated_fields = {'slug': ('name',)}

class CityAdmin(admin.ModelAdmin):
    list_display = ['name']

class RoomAdmin(admin.ModelAdmin):
    list_display = ['position']
    prepopulated_fields = {'slug': ('position',)}

class AvailableAdmin(admin.ModelAdmin):
    list_display = ['durum']

class ProductAdmin(admin.ModelAdmin):
    list_display = ['id','name','slug','city','room']
    prepopulated_fields = {'slug': ('name',)}
    inlines = (Picture,)

class AgentAdmin(admin.ModelAdmin):
    list_display = ['name']



class ImageAdmin(admin.ModelAdmin):
    list_display = ['id']



admin.site.register(Category,CategoryAdmin)
admin.site.register(City,CityAdmin)
admin.site.register(Room,RoomAdmin)
admin.site.register(Available,AvailableAdmin)
admin.site.register(Product,ProductAdmin)
admin.site.register(Agent,AgentAdmin)
admin.site.register(Images,ImageAdmin)
