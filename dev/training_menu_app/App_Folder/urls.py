from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


app_name = "App"

urlpatterns = [
    path('', views.template_view, name='list'), 
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('user/', views.user_view, name='user'),
    path('other/', views.other_view, name='other'),
    path('opinionaire/', views.opinionaire_view, name='opinionaire')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)