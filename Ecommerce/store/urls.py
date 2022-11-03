from django.contrib import admin
from django.urls import path
from .views import Index
from .Views.login import Login, logout
from .Views.signup import Signup
from .Views.cart import Cart
from .Views.checkOut import CheckOut
from .Views.orders import OrderView

urlpatterns = [
    path('', Index.as_view(), name='homepage'),
    path('signup', Signup.as_view(), name='signup'),
    path('login', Login.as_view(), name='login'),
    path('logout', logout, name='logout'),
    path('cart', Cart.as_view(), name='cart'),
    path('check-Out', CheckOut.as_view(), name='checkout'),
path('orders', OrderView.as_view(), name='orders')

]