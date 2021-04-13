
from django.contrib import admin
from django.urls import path, include
admin.site.site_header = "Netflix Admin"
admin.site.site_title = "Netflix Admin Portal"
admin.site.index_title = "Welcome to Netflix"
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("RestApi.urls")),
]
