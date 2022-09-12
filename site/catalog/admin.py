from django.contrib import admin
from .models import worker
from .models import departament, news, product, Post

#admin.site.register(worker)
#admin.site.register(departament)
class departamentAdmin(admin.ModelAdmin):
    pass

admin.site.register(departament,departamentAdmin)

class workerAdmin(admin.ModelAdmin):
    list_display= ('FIO','date_of_birth','post','display_dep')

admin.site.register(worker,workerAdmin)

@admin.register(news)
class newsAdmin(admin.ModelAdmin):
    list_display = ('title', 'short_desc', 'date')

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass


@admin.register(product)
class ProductAdmin(admin.ModelAdmin):
    pass