from django.urls import path
from . import views 


app_name = 'users'
urlpatterns = [
    path('login/', views.UserLogin.as_view(),name='UserLogin'),
    path('logout/', views.UserLogout.as_view(),name='UserLogout'),
    # path('login/',views.LoginView.as_view()),
]