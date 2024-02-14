from django.contrib import admin
from django.urls import path, include
from FirstWebApp import views as v1
from SecondWebApp import views as v2

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', v1.Homepage),
    path('register/', v1.Register),
    path('login/', v1.Login),
    path('second/', include("SecondWebApp.urls")),
    path('forms/', include("FormsWebApp.urls")),
    path('curd/', include("CURDApp.urls")),
    path('alert/', include("AlertApp.urls")),
    path('rest/', include("RestAPI.urls")),
    ]