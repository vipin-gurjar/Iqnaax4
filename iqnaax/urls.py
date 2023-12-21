
# from django.conf import settings
# from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include,re_path
from django.views.static import serve
# from django.contrib.staticfiles.urls import staticfiles_urlpatterns

admin.site.site_header = " <=> IQNAAX Admin Panel <=>"
admin.site.site_title = "Iqnaax Admin "
admin.site.index_title = "Welcome to Iqnaax Admin Panel"


urlpatterns = [
    path('', include("home.urls")),
    path('about/', include("about.urls")),
    path('blog/', include("blog.urls")),
    path('gallery/', include("gallery.urls")),
    path('shop/', include("shop.urls")),
    path('contact/', include("contact.urls")),
    path('', include("account.urls")),
    path('admin/', admin.site.urls),
    re_path(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
]

urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns= urlpatterns+ static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)













