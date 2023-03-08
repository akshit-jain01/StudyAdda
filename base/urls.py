from django.urls import path
from .views import *

urlpatterns = [
    path('login/',LoginPage, name='login' ),
    path('logout/',LogoutPage, name='logout' ),
    path('register/',RegisterUser, name='register' ),
   
    path('', home, name='home'),
    path('rooms/<int:pk>/', room,name='rooms'),
    path('profile/<int:pk>',UserProfile, name='profile'),
   
    path('create-room/', createRoom, name='create-room'),
    path('update-room/<int:pk>', updateRoom, name='update-room'),
    path('delete-room/<int:pk>', deleteRoom, name='delete-room'),
    path('delete-message/<int:pk>', deleteMessage, name='delete-message'),

    path('update-user/', updateUser, name='update-user'),

    path('topics/', topicsPage, name='topics'),
    path('activity/', activityPage, name='activity'),
]