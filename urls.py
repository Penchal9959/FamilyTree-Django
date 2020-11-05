from django.contrib import admin
from django.urls import path, include
from tree import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.login, name="login"),
    # path('tree', include('tree.urls')),
    path('register/',views.register, name="register"),
    path('home/', views.home, name="home"),
    path('add/', views.addperson, name="add"),
    path('successfull/', views.successfull, name="successfull"),
    path('logout/', views.logout, name="logout"),
]