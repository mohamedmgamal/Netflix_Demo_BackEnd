from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from . import  views
urlpatterns = [
    path('login/', obtain_auth_token, name='api_token_auth'),
    path('signUp/', views.signUp, name='Registration'),
    path('addBill/', views.addBill, name="addBill"),
    path('logout/',views.logout,name="LogOut"),
    path('getCat/<str:cat>',views.getCat),
    path('getActor/<str:actor>', views.getActor),
    path('getEp/<int:show>/<int:user>/', views.getEpisodes),
    path('like/<int:show>', views.likes),
    path('disLike/<int:show>', views.disLikes),
    path('history/<int:user>',views.getHistory),
    path('getId/<str:username>',views.getId),
    path('ifun/<str:username>',views.ifUserName,)
]
