from django.contrib.auth import views as auth_views
from django.urls import include, path
from . import views

urlpatterns = [
    #previous login url
    # path("login/", views.user_login, name="login"),
    # login /logout urls
   
    # path('login/', auth_views.LoginView.as_view(), name="login"),
    # path('logout/', auth_views.LogoutView.as_view(), name="logout"),
    # path('password-change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    # path('password-change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    
    # #reset password urls
    # path('password-reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    # path('password-reset-done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    # path('password-reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    # path('password-reset_complete', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    
    path('', include('django.contrib.auth.urls')),
    path('', views.dashboard, name='dashboard'),
    path('register/', views.register, name='register'),
    path('edit/', views.edit, name='edit'),

]
# https://localhost:8000/images/create/?title=testowytytul&url=https://bimbla.pl/environment/cache/images/500_500_productGfx_13/Obrazek_Piesek.jpg
# https://127.0.0.1:8000/images/create/?title=testowytytul&url=https://bimbla.pl/environment/cache/images/500_500_productGfx_13/Obrazek_Piesek.jpg