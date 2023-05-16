from django.urls import path
from .views import index,login,dashboard, product

urlpatterns = [
    path('', index.index, name='index'),
    path('home/', index.home, name='home'),
    path('signup/', login.signup, name='signup'),
    path('dashboard/', dashboard.dashboard, name='dashboard'),
    path('logout/', login.signout, name='logout'),
    path('login/', login.signin, name='login'),
    path('products/', product.product , name='product'),


]