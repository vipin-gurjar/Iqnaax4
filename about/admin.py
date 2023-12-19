from django.contrib import admin
from .models import About_Area_Content, We_Different,About_image_gallery,Reason_to_shop,Counterup_content


class AboutAreaModelAdmin(admin.ModelAdmin):
    list_display = ['content']

admin.site.register(About_Area_Content,AboutAreaModelAdmin)
    
@admin.register(We_Different)
class WeDifferentAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'different_Img']

    
@admin.register(About_image_gallery)
class AboutImageModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'about_img_gallery']
    
@admin.register(Reason_to_shop)
class ReasonModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'desc', 'medalImg']
    
@admin.register(Counterup_content)
class CounterupModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'desc']

