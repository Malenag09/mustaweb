from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
urlpatterns=[
    path('', views.song_list, name='song_list'),
    path('upload_song/', views.upload_song, name='upload_song'),
    path('song/<int:pk>/', views.song_detail, name='song_detail'),
    path('download/<int:pk>/', views.download,name='download'),
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='music/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='music/logout.html'),name='logout'),
    path('artist/<int:artist_id>/book/',views.book_artist, name='book_artist'),
    path('artists/', views.artist_list, name='artist_list'),
    path('artist/<int:pk>/', views.artist_detail, name='artist_detail'),
    path('artist/create/', views.create_artist, name='create_artist'),
    path('artist/<int:pk>/', views.update_artist, name='update_artist'),
    path('artist/<int:pk>/', views.delete_artist, name='delete_artist'),
    path('booking/<int:pk>/accept/', views.accept_booking, name='accept_booking'),
    path('booking/<int:pk>/reject/', views.redirect,name='reject_booking'),
    path('notifications/', views.notifications, name='notifications')
]