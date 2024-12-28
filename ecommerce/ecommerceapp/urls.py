from django.urls import path
from ecommerceapp import views
urlpatterns = [   
    path('', views.home,name="home"),
    path('about', views.about,name="about"),
    path('contact', views.contact,name="contact"),
    path('checkout/', views.checkout,name="checkout"),
    path('cart/', views.cart, name="cart"),
    path('handlerequest/', views.handlerequest,name="handlerequest"),
    path('termservice', views.term,name="termservice"),
    path('privacy', views.pripolicy,name="privacy"),
    path('profile', views.profile,name="profile"),

    
]