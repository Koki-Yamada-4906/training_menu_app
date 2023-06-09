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
    path('opinionaire/', views.opinionaire_view, name='opinionaire'),
    path('result/', views.result_view, name='result'),
    path('user/', views.user_view, name='user'),
    path('mypage/', views.mypage_view, name='mypage'),
    path('model_delete', views.model_delete_view, name='model_delete'),
    path('show_signup/', views.signup_view, name='show_signup'),
    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)