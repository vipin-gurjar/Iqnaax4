from django.shortcuts import render
from .models import We_Different,About_image_gallery,Reason_to_shop,Counterup_content,About_Area_Content

# Create your views here.

def About(request):
    about_content = About_Area_Content.objects.first()
    we_different = We_Different.objects.all()
    about_Img = About_image_gallery.objects.all()
    reason_shop = Reason_to_shop.objects.all()
    counterup = Counterup_content.objects.first()
    context = {'wediff': we_different, 'about_Imgs':about_Img, 'reason_shops':reason_shop, 'counterup':counterup, 'about_content': about_content}
    return render(request, 'myapp/about.html', context)

    
    


