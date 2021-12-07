from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView # django provee de un login y un logaut para utilizar directamente

urlpatterns = [
    path('', views.feed, name='feed'), 
    path('profile/', views.profile, name='profile'),
    path('profile/<str:username>/', views.profile, name='profile'),
    path('register/', views.register, name='register'),
    path('login/', LoginView.as_view(template_name='social/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='social/logout.html'), name='logout'),
    path('post/', views.post, name='post'),
    path('follow/<str:username>', views.follow, name='follow'),
    path('unfollow/<str:username>', views.unfollow, name='unfollow'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # en esta parte fuimos
# a la documentacion de django https://docs.djangoproject.com/en/3.1/howto/static-files/#serving-files-uploaded-by-a-user-during-development
# para poder servir archivos multimedia cargados por el ususario
