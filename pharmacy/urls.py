from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import index,login,dashboard,product

urlpatterns = [
    path('', index.index, name='index'),
    path('home/', index.home, name='home'),
    path('signup/', login.signup, name='signup'),
    path('dashboard/',login_required(dashboard.dashboard), name='dashboard'),
    path('logout/', login_required(login.signout), name='logout'),
    path('login/', login.signin, name='login'),
    path('products/', login_required(product.product) , name='product'),
    path('create_product/', login_required(product.create_product) , name='create_product'),
    path('edit_product/<int:pk>', login_required(product.edit_product) , name='edit_product'),


]