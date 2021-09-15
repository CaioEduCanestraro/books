#from re import I
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers, urlpatterns
from books.api import viewsets as booksviewsets
from django.conf.urls.static import static
from django.conf import settings




route = routers.DefaultRouter()
route.register(r'books', booksviewsets.BooksViewSet, basename="Books")


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(route.urls))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
