from django.urls import path
from ecommerceapp import views
urlpatterns = [   
    path('', views.home,name="home"),
    path('about', views.about,name="about"),
    path('contact', views.contact,name="contact"),
    path('blog', views.blog,name="blog"),
    path('checkout/', views.checkout,name="checkout"),
    path('handlerequest/', views.handlerequest,name="handlerequest"),
    path('termservice', views.term,name="termservice"),
    path('privacy', views.pripolicy,name="privacy"),
    
]