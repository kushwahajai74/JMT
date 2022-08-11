from django.views import View
from homeJMT import views
from django.urls import path, include

urlpatterns = [
   
    path("",views.index,name="Home"),
    path("about",views.aboutus, name="About"),
    path('contact', views.contact, name="Contact"),
    path("index", views.index, name="Home"),
    path('<int:id>', views.product1, name="Product1"),
    path("saveEnquiry",views.saveEnquiry, name="saveEnquiry"),
    path('<str:category>', views.brand, name="brand")
]
