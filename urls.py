from django.contrib import admin
from django.urls import path
from userApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('adduser',views.adduser,name="adduser"),
    path('userlogin',views.userlogin,name="userlogin"),
    path('getaudio/<int:userid>',views.getaudio,name="getaudio"),
    path('downloadsecurity/<int:userid>',views.downloadsecurity,name="downloadsecurity"),
    path('comparevoice/<int:userid>',views.comparevoice,name="comparevoice"),
    path('sendotp',views.sendotp,name="sendotp"),
    path('payment',views.payment,name="payment")
]
